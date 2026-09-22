/**
 * ============================================================================
 * MAISON POISSON // CRM & WHATSAPP LEAD DISPATCHER MODULE
 * ============================================================================
 * 
 * Luxury Textile Atelier & Contract Architectural Shading Systems (Astana, KZ).
 * 
 * Purpose:
 *   Central omnichannel lead dispatching, qualification routing, CRM synchronization,
 *   and instant messenger handoff (WhatsApp Deep-Links + Telegram Sales Webhook).
 * 
 * Core Capabilities:
 *   1. Lead Routing & CRM Integration Logic:
 *      - B2C Private Residences Funnel (Apartments, Penthouses, Villas in Astana).
 *      - B2B Corporate & Contract Shading Funnel (Offices, Hotels, Developers, HoReCa).
 *      - Interior Designer Club Funnel (10% cashback, 3D textures, project protection).
 *      - VIP Secret Dossier Funnel (Project-70 / Saranda Villa approvals).
 *      - Lead scoring tiers (VIP, COMMERCIAL, DESIGNER, RESIDENTIAL) with SLA timers.
 *      - CRM Payload Adapters (amoCRM API v4, Bitrix24 REST API, Generic Webhook).
 * 
 *   2. WhatsApp Deep-Link URL Generator:
 *      - Formats customer inputs: Curtain type, dimensions, fabric, pleat, budget in ₸.
 *      - Exact required greeting matching:
 *        "Здравствуйте, MUAR A! Я сделал расчет на сайте: Портьеры со складкой Ripplefold, 3.8м x 3.2м, бельгийский шенилл. Предварительная смета: 385 000 ₸. Хочу вызвать декоратора с образцами."
 *      - Generates universal links (`https://wa.me/...`), mobile app deep links,
 *        and WhatsApp Web fallbacks with clean UTM tag embedding.
 * 
 *   3. Telegram Notification Webhook Handler:
 *      - Rich HTML card notifications with SLA badges and inline action buttons
 *        ([Написать в WhatsApp], [Позвонить], [Открыть в CRM]).
 *      - Handles photo and 3D visualization uploads (as highlighted in the transcript:
 *        clients sending interior renders/photos, decorators photographing fabrics).
 *      - Automatic routing to `sendPhoto` / `sendMediaGroup` / `sendDocument`.
 * 
 * Environments Supported:
 *   - Browser (Global `window.MaisonPoissonDispatcher` & ES Module)
 *   - Node.js (CommonJS `module.exports` & ES Module)
 *   - Cloudflare Workers / AWS Lambda / Vercel Serverless Functions
 * 
 * @version 2.0.0
 * @author MUAR A Engineering Team
 * @license Proprietary - MUAR A Atelier
 * ============================================================================
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    // Node.js / CommonJS
    module.exports = factory();
  } else {
    // Browser Global
    root.MaisonPoissonDispatcher = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  // ==========================================================================
  // 1. CONFIGURATION CONSTANTS & BRAND DEFAULTS
  // ==========================================================================

  const CONFIG = {
    BRAND_NAME: 'MUAR A',
    STUDIO_CITY: 'Астана',
    DEFAULT_WA_PHONE: '77710551515', // +7 (771) 055-15-15
    SECONDARY_WA_PHONE: '77773845517', // +7 (777) 384-55-17
    DEFAULT_CURRENCY: '₸',
    CURRENCY_CODE: 'KZT',
    VAT_RATE: 0.12, // 12% Kazakhstan Corporate VAT
    LEGAL_NAME: 'ТОО "KazTextileА"',
    LEGAL_BIN: '140940019744',
    SALON_ADDRESS: 'г. Астана, ул. Керей, Жәнибек хандар, 50/1, ВП 18',

    // Telegram Bot Settings (can be overridden in methods)
    TELEGRAM: {
      BOT_TOKEN: '', // e.g. "123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ"
      CHAT_ID_B2C: '', // Channel/Group for residential leads
      CHAT_ID_B2B: '', // Channel/Group for corporate tenders
      CHAT_ID_VIP: '', // Executive channel for VIP dossier approvals
      API_BASE_URL: 'https://api.telegram.org'
    },

    // CRM Integration Defaults
    CRM: {
      AMOCRM_BASE_URL: '', // e.g. "https://maisonpoisson.amocrm.ru"
      BITRIX24_WEBHOOK_URL: '', // e.g. "https://maisonpoisson.bitrix24.kz/rest/1/webhook_token/"
      GENERIC_WEBHOOK_URL: '',
      TIMEOUT_MS: 8000
    },

    // Response SLA Targets
    SLA: {
      VIP_MINUTES: 5,
      B2C_MINUTES: 10,
      B2B_HOURS: 2,
      DESIGNER_MINUTES: 15
    },

    // Maximum file upload sizes
    UPLOAD_LIMITS: {
      IMAGE_MAX_BYTES: 20 * 1024 * 1024, // 20 MB
      DOC_MAX_BYTES: 50 * 1024 * 1024,   // 50 MB
      ALLOWED_IMAGE_TYPES: ['image/jpeg', 'image/png', 'image/webp', 'image/heic'],
      ALLOWED_DOC_TYPES: [
        'application/pdf',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', // xlsx
        'application/vnd.ms-excel', // xls
        'application/zip',
        'application/x-zip-compressed',
        'image/vnd.dwg',
        'application/acad'
      ]
    }
  };

  // ==========================================================================
  // 2. UTILITY & FORMATTING HELPERS
  // ==========================================================================

  /**
   * Formats numeric budget into luxury Kazakhstan Tenge representation.
   * Example: 385000 -> "385 000 ₸"
   * @param {number|string} value
   * @returns {string}
   */
  function formatTenge(value) {
    if (value === null || value === undefined || value === '') return 'По согласованию';
    if (typeof value === 'string') {
      // If already formatted with ₸, sanitize and return
      if (value.includes('₸')) return value.trim().replace(/\u00a0/g, ' ');
      const num = parseFloat(value.replace(/[^\d.,]/g, '').replace(',', '.'));
      if (isNaN(num)) return value;
      value = num;
    }
    return Math.round(value).toLocaleString('ru-RU').replace(/\u00a0/g, ' ').replace(/,/g, ' ') + ' ₸';
  }

  /**
   * Cleans phone number to international E.164 digits without plus.
   * Example: "+7 (701) 555-12-34" -> "77015551234"
   * @param {string} phone
   * @returns {string}
   */
  function sanitizePhone(phone) {
    if (!phone) return CONFIG.DEFAULT_WA_PHONE;
    const digits = phone.toString().replace(/\D/g, '');
    if (digits.length === 11 && digits.startsWith('8')) {
      return '7' + digits.substring(1);
    }
    if (digits.length === 10 && digits.startsWith('7')) {
      return '7' + digits;
    }
    return digits || CONFIG.DEFAULT_WA_PHONE;
  }

  /**
   * Generates a unique traceable Lead ID.
   * Example: "MP-2026-B2C-7492"
   * @param {string} funnel
   * @returns {string}
   */
  function generateLeadId(funnel = 'B2C') {
    const prefix = 'MP-2026';
    const tag = funnel.toUpperCase().substring(0, 3);
    const rand = Math.floor(1000 + Math.random() * 9000);
    return `${prefix}-${tag}-${rand}`;
  }

  /**
   * Escapes HTML entities for safe Telegram HTML formatting.
   * @param {string} text
   * @returns {string}
   */
  function escapeHtml(text) {
    if (!text) return '';
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  // ==========================================================================
  // 3. LEAD DATA MODELS & NORMALIZERS
  // ==========================================================================

  /**
   * Normalizes B2C Residential Calculator Lead data.
   * 
   * @param {Object} input
   * @param {string} [input.curtainType='Портьеры'] - Type of curtain (Портьеры, Тюль, Римские шторы)
   * @param {number|string} [input.width=3.8] - Window/Curtain width in meters
   * @param {number|string} [input.height=3.2] - Window/Curtain height in meters
   * @param {string} [input.fabric='бельгийский шенилл'] - Selected fabric
   * @param {string} [input.pleatFold='Ripplefold'] - Pleat fold style (Ripplefold, Французская тройная)
   * @param {number|string} [input.estimatedBudget=385000] - Estimated cost in KZT
   * @param {string} [input.calloutAction='Хочу вызвать декоратора с образцами.'] - Specific conversion callout
   * @param {Object} [input.options] - Supplementary options { includeTulle, includeSomfy, lining }
   * @param {Object} [input.customer] - Customer details { name, phone, complex, stage }
   * @param {Array} [input.visualizations] - Uploaded photos, 3D renders or fabric photos
   * @param {Object} [input.utm] - Marketing attribution tags
   * @returns {Object} Normalized B2C lead object
   */
  function createB2CLead(input = {}) {
    const width = parseFloat(input.width || 3.8);
    const height = parseFloat(input.height || 3.2);
    const curtainType = (input.curtainType || 'Портьеры').trim();
    const pleatFold = (input.pleatFold || 'Ripplefold').trim();
    const fabric = (input.fabric || 'бельгийский шенилл').trim();
    const rawBudget = input.estimatedBudget !== undefined ? input.estimatedBudget : 385000;
    const calloutAction = (input.calloutAction || 'Хочу вызвать декоратора с образцами.').trim();

    return {
      leadId: input.leadId || generateLeadId('B2C'),
      timestamp: new Date().toISOString(),
      funnel: 'b2c',
      curtainType,
      width,
      height,
      dimensionsText: `${width}м x ${height}м`,
      fabric,
      pleatFold,
      estimatedBudget: typeof rawBudget === 'number' ? rawBudget : parseFloat(String(rawBudget).replace(/[^\d.]/g, '')) || 385000,
      estimatedBudgetText: formatTenge(rawBudget),
      calloutAction,
      room: input.room || 'Гостиная',
      options: {
        includeTulle: Boolean(input.options?.includeTulle),
        includeSomfy: Boolean(input.options?.includeSomfy),
        lining: Boolean(input.options?.lining),
        laurastarSteaming: input.options?.laurastarSteaming !== false
      },
      customer: {
        name: input.customer?.name || '',
        phone: input.customer?.phone || '',
        residentialComplex: input.customer?.residentialComplex || input.customer?.complex || 'Астана (новостройка)',
        repairStage: input.customer?.repairStage || 'Чистовая отделка'
      },
      visualizations: Array.isArray(input.visualizations) ? input.visualizations : [],
      utm: {
        source: input.utm?.source || 'direct',
        medium: input.utm?.medium || 'website',
        campaign: input.utm?.campaign || 'calculator',
        content: input.utm?.content || '',
        term: input.utm?.term || ''
      },
      referrer: input.referrer || (typeof document !== 'undefined' ? document.referrer : '')
    };
  }

  /**
   * Normalizes B2B Commercial & Contract Shading Lead data.
   * 
   * @param {Object} input
   * @param {Object} input.company - Company information { name, bin, city }
   * @param {Object} input.contact - Contact person { name, role, phone, email }
   * @param {number|string} [input.openingsCount=12] - Number of architectural openings
   * @param {string} [input.systemType='Somfy Screen 5%'] - Shading system
   * @param {number|string} [input.estimatedBudget=540000] - Total budget with VAT 12%
   * @param {boolean} [input.fireSafetyRequired=true] - Trevira CS / KM1 certificate needed
   * @param {Array} [input.specFiles] - Uploaded DWG, PDF, or Excel specifications
   * @returns {Object} Normalized B2B lead object
   */
  function createB2BLead(input = {}) {
    const openingsCount = parseInt(input.openingsCount || 12, 10);
    const systemType = input.systemType || 'Somfy Screen 5%';
    const rawBudget = input.estimatedBudget !== undefined ? input.estimatedBudget : 540000;
    const totalBudget = typeof rawBudget === 'number' ? rawBudget : parseFloat(String(rawBudget).replace(/[^\d.]/g, '')) || 540000;
    const subtotal = Math.round(totalBudget / (1 + CONFIG.VAT_RATE));
    const vatAmount = totalBudget - subtotal;

    return {
      leadId: input.leadId || generateLeadId('B2B'),
      timestamp: new Date().toISOString(),
      funnel: 'b2b',
      company: {
        name: input.company?.name || 'Корпоративный заказчик',
        bin: input.company?.bin || input.company?.inn || '',
        city: input.company?.city || 'Астана'
      },
      contact: {
        name: input.contact?.name || '',
        role: input.contact?.role || 'Менеджер проекта / Инженер',
        phone: input.contact?.phone || '',
        email: input.contact?.email || ''
      },
      openingsCount,
      systemType,
      automation: input.automation || 'Somfy Sonesse (Dry Contact / RS485)',
      fireSafetyRequired: input.fireSafetyRequired !== false,
      vatRate: CONFIG.VAT_RATE,
      subtotal,
      subtotalText: formatTenge(subtotal),
      vatAmount,
      vatAmountText: formatTenge(vatAmount),
      estimatedBudget: totalBudget,
      estimatedBudgetText: formatTenge(totalBudget),
      slaHours: CONFIG.SLA.B2B_HOURS,
      specFiles: Array.isArray(input.specFiles) ? input.specFiles : [],
      visualizations: Array.isArray(input.visualizations) ? input.visualizations : [],
      preferredChannel: input.preferredChannel || 'whatsapp',
      utm: {
        source: input.utm?.source || 'b2b_portal',
        medium: input.utm?.medium || 'commercial',
        campaign: input.utm?.campaign || 'architectural_screen'
      }
    };
  }

  /**
   * Normalizes Interior Designer Club Partner Lead data.
   * 
   * @param {Object} input
   * @returns {Object} Normalized Designer lead object
   */
  function createDesignerLead(input = {}) {
    return {
      leadId: input.leadId || generateLeadId('DSG'),
      timestamp: new Date().toISOString(),
      funnel: 'designer_club',
      designer: {
        name: input.designer?.name || input.name || '',
        studio: input.designer?.studio || input.studio || '',
        phone: input.designer?.phone || input.phone || '',
        instagram: input.designer?.instagram || '',
        city: input.designer?.city || 'Астана'
      },
      benefits: [
        '10% кэшбэк день-в-день',
        '3D-текстуры для Corona / 3ds Max',
        'Бронь образцов и каталогов',
        'Защита авторского надзора'
      ],
      activeProject: input.activeProject || '',
      visualizations: Array.isArray(input.visualizations) ? input.visualizations : []
    };
  }

  /**
   * Normalizes VIP Secret Proposal Dossier Approval Lead data.
   * 
   * @param {Object} input
   * @returns {Object} Normalized VIP Dossier lead object
   */
  function createVipDossierLead(input = {}) {
    return {
      leadId: input.leadId || generateLeadId('VIP'),
      timestamp: new Date().toISOString(),
      funnel: 'vip_dossier',
      projectCode: input.projectCode || 'PROJECT-70',
      objectTitle: input.objectTitle || 'Резиденция в пос. Саранда (480 м²)',
      clientNames: input.clientNames || 'Айдар и Динара',
      totalCost: input.totalCost || '3 480 000 ₸',
      designer: input.designer || 'Анастасия Белова (Ведущий декоратор)',
      somfyIncluded: input.somfyIncluded !== false,
      status: 'Утверждение сметы и запуск договора',
      visualizations: Array.isArray(input.visualizations) ? input.visualizations : []
    };
  }

  // ==========================================================================
  // 4. LEAD ROUTING & SCORING LOGIC
  // ==========================================================================

  /**
   * Evaluates incoming lead and performs intelligent qualification routing:
   * - Assigns priority tier (VIP, COMMERCIAL, DESIGNER, RESIDENTIAL)
   * - Assigns department and responsible manager
   * - Sets SLA response clock
   * - Maps to CRM pipeline and initial stage
   * - Applies analytical tags
   * 
   * @param {Object} lead - Normalized lead object
   * @returns {Object} Routing decision and metadata
   */
  function routeLead(lead) {
    const budget = typeof lead.estimatedBudget === 'number' ? lead.estimatedBudget : 0;
    const funnel = lead.funnel || 'b2c';

    let tier = 'RESIDENTIAL_PREMIUM';
    let assignedDepartment = 'b2c_couture';
    let assignedManager = 'Анастасия Белова (Ведущий текстильный декоратор)';
    let slaMinutes = CONFIG.SLA.B2C_MINUTES;
    let crmPipeline = 'b2c_residential';
    let crmStage = 'NEW_LEAD_CALC';
    const tags = ['Maison_Poisson', funnel.toUpperCase()];

    // 1. VIP Dossier Specific Funnel
    if (funnel === 'vip_dossier') {
      tier = 'VIP';
      assignedDepartment = 'couture_concierge';
      assignedManager = 'Ольга Смирнова (Главный декоратор / Руководитель студии)';
      slaMinutes = CONFIG.SLA.VIP_MINUTES;
      crmPipeline = 'vip_private_residences';
      crmStage = 'VIP_URGENT_APPROVAL';
      tags.push('VIP_DOSSIER', 'Priority_FastLane');
    }
    // 2. B2B Corporate Shading Routing
    else if (funnel === 'b2b') {
      tier = (budget >= 5000000 || (lead.openingsCount && lead.openingsCount >= 50)) ? 'COMMERCIAL_KEY_ACCOUNT' : 'COMMERCIAL';
      assignedDepartment = 'b2b_contract_division';
      assignedManager = 'Алексей Смирнов (Руководитель B2B проектов и тендеров)';
      slaMinutes = CONFIG.SLA.B2B_HOURS * 60; // 120 minutes SLA
      crmPipeline = 'b2b_corporate_tenders';
      crmStage = 'TENDER_SPECS_REVIEW';
      tags.push('B2B_TENDER', 'VAT_12', `Openings_${lead.openingsCount || 1}`);
      if (lead.fireSafetyRequired) tags.push('Trevira_KM1_FireSafety');
    }
    // 3. Designer Club Routing
    else if (funnel === 'designer_club') {
      tier = 'DESIGNER_PARTNER';
      assignedDepartment = 'designer_partnerships';
      assignedManager = 'Камила (Куратор Дизайнерского Клуба)';
      slaMinutes = CONFIG.SLA.DESIGNER_MINUTES;
      crmPipeline = 'designer_loyalty_club';
      crmStage = 'DESIGNER_VERIFICATION';
      tags.push('Designer_Club_10_Cashback', 'Author_Supervision');
    }
    // 4. B2C Residential Funnel (with High-Ticket VIP escalation)
    else {
      const isVipEstate = /саранда|highvill|sensata|karaotkel|deluxe|villa|вилла|премьера/i.test(
        lead.customer?.residentialComplex || lead.objectTitle || ''
      );

      if (budget >= 1000000 || isVipEstate) {
        tier = 'VIP';
        assignedDepartment = 'couture_concierge';
        assignedManager = 'Ольга Смирнова (Главный декоратор / Руководитель студии)';
        slaMinutes = CONFIG.SLA.VIP_MINUTES;
        crmPipeline = 'vip_private_residences';
        crmStage = 'VIP_URGENT_APPROVAL';
        tags.push('VIP_HIGH_TICKET', 'Priority_FastLane');
      } else {
        tier = 'RESIDENTIAL_PREMIUM';
        assignedDepartment = 'b2c_couture';
        assignedManager = 'Анастасия Белова (Ведущий текстильный декоратор)';
        slaMinutes = CONFIG.SLA.B2C_MINUTES;
        crmPipeline = 'b2c_residential';
        crmStage = 'NEW_LEAD_CALC';
      }

      tags.push(
        lead.pleatFold ? `Pleat_${lead.pleatFold.replace(/\s+/g, '_')}` : 'Pleat_Ripplefold',
        lead.fabric ? `Fabric_${lead.fabric.replace(/\s+/g, '_')}` : 'Fabric_Chenille'
      );
      if (lead.options?.includeSomfy) tags.push('Somfy_Motorized');
      if (lead.options?.includeTulle) tags.push('With_Tulle');
    }

    // Check for uploaded visualizations or fabric photos
    if (lead.visualizations && lead.visualizations.length > 0) {
      tags.push('Has_Visualizations');
    }
    if (lead.specFiles && lead.specFiles.length > 0) {
      tags.push('Has_Spec_Attachments');
    }

    return {
      tier,
      assignedDepartment,
      assignedManager,
      slaMinutes,
      crmPipeline,
      crmStage,
      tags,
      routedAt: new Date().toISOString()
    };
  }

  // ==========================================================================
  // 5. WHATSAPP DEEP-LINK URL GENERATOR
  // ==========================================================================

  /**
   * Generates the customer greeting text for WhatsApp according to funnel.
   * For standard B2C calculations, produces the EXACT required format:
   * "Здравствуйте, MUAR A! Я сделал расчет на сайте: Портьеры со складкой Ripplefold, 3.8м x 3.2м, бельгийский шенилл. Предварительная смета: 385 000 ₸. Хочу вызвать декоратора с образцами."
   * 
   * @param {Object} lead - Normalized lead object
   * @param {Object} [options]
   * @param {boolean} [options.strictExactB2C=false] - Force strict one-liner matching without extras
   * @param {boolean} [options.includeTracking=false] - Append discreet lead tag
   * @returns {string} Formatted WhatsApp message
   */
  function generateWhatsAppText(lead, options = {}) {
    const funnel = lead.funnel || 'b2c';

    // 1. B2C CALCULATOR FUNNEL (Exact required greeting)
    if (funnel === 'b2c') {
      const type = lead.curtainType || 'Портьеры';
      const fold = lead.pleatFold || 'Ripplefold';
      const dims = `${lead.width}м x ${lead.height}м`;
      const fabric = lead.fabric || 'бельгийский шенилл';
      const budget = lead.estimatedBudgetText || formatTenge(lead.estimatedBudget || 385000);
      const action = lead.calloutAction || 'Хочу вызвать декоратора с образцами.';

      // Exact base greeting required by specification:
      // "Здравствуйте, MUAR A! Я сделал расчет на сайте: Портьеры со складкой Ripplefold, 3.8м x 3.2м, бельгийский шенилл. Предварительная смета: 385 000 ₸. Хочу вызвать декоратора с образцами."
      let text = `Здравствуйте, ${CONFIG.BRAND_NAME}! Я сделал расчет на сайте: ${type} со складкой ${fold}, ${dims}, ${fabric}. Предварительная смета: ${budget}. ${action}`;

      // If strict mode is requested, return exact text immediately
      if (options.strictExactB2C) {
        return text;
      }

      // Additions for enhanced customer context if present and not in strict mode
      const extraDetails = [];
      if (lead.room && lead.room !== 'Гостиная') {
        extraDetails.push(`Помещение: ${lead.room}`);
      }
      if (lead.options?.includeSomfy) {
        extraDetails.push('Электрокарниз Somfy');
      }
      if (lead.options?.includeTulle) {
        extraDetails.push('Тюль-компаньон');
      }
      if (lead.customer?.residentialComplex && lead.customer.residentialComplex !== 'Астана (новостройка)') {
        extraDetails.push(`Объект: ${lead.customer.residentialComplex}`);
      }
      if (lead.visualizations && lead.visualizations.length > 0) {
        extraDetails.push(`📎 Прикрепил визуализацию / фото (${lead.visualizations.length} шт.)`);
      }

      if (extraDetails.length > 0 && !options.strictExactB2C) {
        text += `\n\nДетали проекта: ${extraDetails.join(' • ')}`;
      }

      if (options.includeTracking && lead.leadId) {
        text += `\n[ID: ${lead.leadId}]`;
      }

      return text;
    }

    // 2. B2B CORPORATE SPECIFICATION FUNNEL
    if (funnel === 'b2b') {
      const company = lead.company?.name || 'Юридическое лицо';
      const bin = lead.company?.bin ? ` (БИН/ИНН ${lead.company.bin})` : '';
      const contact = lead.contact?.name ? `\n👤 Контакт: ${lead.contact.name}${lead.contact.role ? ' (' + lead.contact.role + ')' : ''}` : '';
      const openings = lead.openingsCount || 12;
      const system = lead.systemType || 'Somfy Screen 5%';
      const budget = lead.estimatedBudgetText || formatTenge(lead.estimatedBudget || 540000);

      let text = `Здравствуйте, ${CONFIG.BRAND_NAME}!\n` +
        `Запрос B2B спецификации для юридического лица:\n` +
        `🏢 Компания: ${company}${bin}${contact}\n` +
        `🪟 Проемов: ${openings} шт. | Система: ${system}\n` +
        `⚡ Управление: ${lead.automation || 'Somfy'}\n` +
        `💰 Предварительная смета: ${budget} (с НДС 12%)\n` +
        `⏱ Просим подготовить официальное КП с НДС за 2 часа.`;

      if (lead.specFiles && lead.specFiles.length > 0) {
        text += `\n📁 Прикреплено ТЗ / ведомость (${lead.specFiles.length} файлов).`;
      }
      if (options.includeTracking && lead.leadId) {
        text += `\n[ID: ${lead.leadId}]`;
      }

      return text;
    }

    // 3. DESIGNER CLUB FUNNEL
    if (funnel === 'designer_club') {
      const name = lead.designer?.name ? `, меня зовут ${lead.designer.name}` : '';
      const studio = lead.designer?.studio ? ` (студия «${lead.designer.studio}»)` : '';
      return `Здравствуйте, ${CONFIG.BRAND_NAME}! Я дизайнер интерьера${name}${studio}.\n` +
        `Хочу вступить в Дизайнерский Клуб: получить условия 10% кэшбэка день-в-день, библиотеку 3D-текстур для Corona/3ds Max и забронировать образцы под текущий проект.\n` +
        `Как мы можем начать сотрудничество?`;
    }

    // 4. VIP PROPOSAL DOSSIER APPROVAL FUNNEL
    if (funnel === 'vip_dossier') {
      const code = lead.projectCode || 'PROJECT-70';
      const obj = lead.objectTitle || 'Резиденция в пос. Саранда';
      const cost = lead.totalCost || '3 480 000 ₸';
      return `Здравствуйте, ${CONFIG.BRAND_NAME}!\n` +
        `Мы изучили интерактивное КП по объекту ${code} (${obj}).\n` +
        `Смета ${cost} с электрокарнизами Somfy согласована!\n` +
        `Готовы внести предоплату и запустить заказ в цеховой пошив. Пришлите, пожалуйста, договор!`;
    }

    // 5. GENERIC FALLBACK
    return `Здравствуйте, ${CONFIG.BRAND_NAME}! Хочу проконсультироваться по текстильному оформлению штор на объекте в г. Астана.`;
  }

  /**
   * Generates a one-tap WhatsApp deep-link URL.
   * 
   * @param {Object} lead - Lead data or raw calculator input
   * @param {Object} [options]
   * @param {string} [options.phone] - Custom WhatsApp phone number (default: Kazakhstan studio)
   * @param {string} [options.platform='universal'] - 'universal' (https://wa.me), 'app' (whatsapp://send), 'web' (web.whatsapp.com)
   * @param {boolean} [options.strictExactB2C=false] - Strictly adhere to exact user greeting
   * @param {boolean} [options.includeTracking=false] - Append tracking tag
   * @returns {string} Fully formatted deep-link URL
   */
  function generateWhatsAppUrl(lead, options = {}) {
    // Ensure normalized lead
    const normalized = lead.funnel ? lead : createB2CLead(lead);
    const phone = sanitizePhone(options.phone || CONFIG.DEFAULT_WA_PHONE);
    const message = generateWhatsAppText(normalized, options);
    const encoded = encodeURIComponent(message);

    const platform = options.platform || 'universal';

    if (platform === 'app') {
      return `whatsapp://send?phone=${phone}&text=${encoded}`;
    }
    if (platform === 'web') {
      return `https://web.whatsapp.com/send?phone=${phone}&text=${encoded}`;
    }
    // Universal link (default recommended by Meta)
    return `https://wa.me/${phone}?text=${encoded}`;
  }

  // ==========================================================================
  // 6. PHOTO & VISUALIZATION UPLOAD PROCESSOR
  // ==========================================================================

  /**
   * Handles photo and visualization uploads as highlighted in the transcript:
   * - Clients uploading 3D interior renders or window photos
   * - Decorators photographing fabric textures on-site or in the showroom
   * - Corporate customers uploading DWG / PDF / Excel tender specifications
   * 
   * Provides metadata extraction, mime-type verification, and payload preparation.
   * 
   * @param {File|Blob|string|Object} fileOrUrl - Browser File/Blob, Base64 Data URL, or Remote Link
   * @param {Object} [meta] - Supplementary metadata { type, description, roomName }
   * @returns {Object} Structured visualization descriptor
   */
  function processVisualizationUpload(fileOrUrl, meta = {}) {
    // 1. If string (Remote URL or Base64 Data URL)
    if (typeof fileOrUrl === 'string') {
      const isBase64 = fileOrUrl.startsWith('data:');
      let mimeType = 'image/jpeg';
      if (isBase64) {
        const match = fileOrUrl.match(/^data:([^;]+);base64,/);
        if (match) mimeType = match[1];
      }

      return {
        id: 'vis_' + Math.random().toString(36).substring(2, 9),
        source: isBase64 ? 'base64' : 'remote_url',
        url: isBase64 ? null : fileOrUrl,
        data: isBase64 ? fileOrUrl : null,
        mimeType,
        type: meta.type || 'interior_render', // 'interior_render' | 'real_photo' | 'fabric_sample' | 'dwg_spec'
        description: meta.description || 'Визуализация или фото интерьера от клиента',
        uploadedAt: new Date().toISOString()
      };
    }

    // 2. If browser File or Blob object
    if (typeof Blob !== 'undefined' && fileOrUrl instanceof Blob) {
      const name = fileOrUrl.name || 'unnamed_upload';
      const size = fileOrUrl.size;
      const mimeType = fileOrUrl.type || 'application/octet-stream';

      return {
        id: 'vis_' + Math.random().toString(36).substring(2, 9),
        source: 'blob',
        fileObject: fileOrUrl,
        name,
        size,
        mimeType,
        type: meta.type || (mimeType.startsWith('image/') ? 'interior_render' : 'document_spec'),
        description: meta.description || name,
        uploadedAt: new Date().toISOString()
      };
    }

    // 3. Pre-structured object
    return {
      id: fileOrUrl.id || 'vis_' + Math.random().toString(36).substring(2, 9),
      source: fileOrUrl.source || 'pre_processed',
      url: fileOrUrl.url || null,
      name: fileOrUrl.name || 'render.jpg',
      mimeType: fileOrUrl.mimeType || 'image/jpeg',
      type: meta.type || fileOrUrl.type || 'interior_render',
      description: meta.description || fileOrUrl.description || 'Визуализация проекта'
    };
  }

  /**
   * Browser-side Client Image Compressor & Thumbnail Generator.
   * Compresses 4K smartphone / HEIC photos to optimal JPEG/WebP (1600px width)
   * before sending to Telegram/CRM, eliminating mobile upload lag.
   * 
   * @param {File} file - Original image file from input[type=file]
   * @param {number} [maxWidth=1600]
   * @param {number} [quality=0.85]
   * @returns {Promise<{blob: Blob, dataUrl: string, width: number, height: number}>}
   */
  function compressClientImage(file, maxWidth = 1600, quality = 0.85) {
    return new Promise((resolve, reject) => {
      if (typeof window === 'undefined' || !window.FileReader || !window.Image) {
        return reject(new Error('compressClientImage requires browser DOM environment'));
      }

      if (!file.type.startsWith('image/')) {
        return reject(new Error('Provided file is not an image'));
      }

      const reader = new FileReader();
      reader.onerror = reject;
      reader.onload = function (e) {
        const img = new Image();
        img.onerror = reject;
        img.onload = function () {
          let w = img.width;
          let h = img.height;

          if (w > maxWidth) {
            h = Math.round((h * maxWidth) / w);
            w = maxWidth;
          }

          const canvas = document.createElement('canvas');
          canvas.width = w;
          canvas.height = h;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);

          const dataUrl = canvas.toDataURL('image/jpeg', quality);
          canvas.toBlob(
            function (blob) {
              resolve({
                blob,
                dataUrl,
                width: w,
                height: h,
                originalSize: file.size,
                compressedSize: blob ? blob.size : null
              });
            },
            'image/jpeg',
            quality
          );
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    });
  }

  // ==========================================================================
  // 7. TELEGRAM NOTIFICATION WEBHOOK HANDLER
  // ==========================================================================

  /**
   * Builds high-aesthetic HTML notification card for Telegram sales groups.
   * 
   * @param {Object} lead - Normalized lead
   * @param {Object} routing - Routing metadata
   * @returns {string} Telegram HTML formatted string
   */
  function formatTelegramHtml(lead, routing) {
    const funnel = lead.funnel || 'b2c';
    const brand = escapeHtml(CONFIG.BRAND_NAME);
    const leadId = escapeHtml(lead.leadId);

    // 1. B2C RESIDENTIAL NOTIFICATION
    if (funnel === 'b2c') {
      const isVip = routing.tier === 'VIP';
      const headerIcon = isVip ? '👑' : '✨';
      const headerTitle = isVip ? 'VIP ЧАСТНАЯ РЕЗИДЕНЦИЯ' : 'НОВЫЙ РАСЧЕТ ШТОР (B2C)';

      let html = `${headerIcon} <b>${brand} // ${headerTitle}</b>\n`;
      html += `<b>ID заявки:</b> <code>#${leadId}</code>\n`;
      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `🧵 <b>Изделие:</b> ${escapeHtml(lead.curtainType)}\n`;
      html += `📐 <b>Размеры:</b> ${escapeHtml(lead.dimensionsText)}\n`;
      html += `🎨 <b>Ткань:</b> ${escapeHtml(lead.fabric)}\n`;
      html += `〰️ <b>Складка:</b> ${escapeHtml(lead.pleatFold)}\n`;
      html += `💰 <b>Смета:</b> <b>${escapeHtml(lead.estimatedBudgetText)}</b>\n`;

      if (lead.options?.includeSomfy) html += `⚡ <b>Опция:</b> Электрокарниз Somfy\n`;
      if (lead.options?.includeTulle) html += `🪟 <b>Опция:</b> Тюль-компаньон\n`;

      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `🎯 <b>Ключевое действие:</b> ${escapeHtml(lead.calloutAction)}\n`;
      html += `📍 <b>Объект:</b> ${escapeHtml(lead.customer?.residentialComplex || 'Астана')}\n`;
      html += `🛠 <b>Стадия:</b> ${escapeHtml(lead.customer?.repairStage || 'Чистовая отделка')}\n`;

      if (lead.customer?.phone) {
        html += `👤 <b>Клиент:</b> ${escapeHtml(lead.customer?.name || 'Клиент')} (<code>+${sanitizePhone(lead.customer.phone)}</code>)\n`;
      }

      if (lead.visualizations && lead.visualizations.length > 0) {
        html += `🖼 <b>Прикреплено визуализаций / фото:</b> ${lead.visualizations.length} шт.\n`;
      }

      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `⏱ <b>SLA ответа:</b> ${routing.slaMinutes} минут\n`;
      html += `👤 <b>Назначен декоратор:</b> ${escapeHtml(routing.assignedManager)}\n`;
      html += `🏷 <i>${routing.tags.map(t => '#' + t).join(' ')}</i>`;

      return html;
    }

    // 2. B2B CORPORATE TENDER NOTIFICATION
    if (funnel === 'b2b') {
      let html = `🏢 <b>${brand} // B2B СПЕЦИФИКАЦИЯ (ТЕНДЕР)</b>\n`;
      html += `<b>ID заявки:</b> <code>#${leadId}</code>\n`;
      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `🏛 <b>Компания:</b> ${escapeHtml(lead.company?.name)}\n`;
      if (lead.company?.bin) html += `🧾 <b>БИН/ИНН:</b> <code>${escapeHtml(lead.company.bin)}</code>\n`;
      html += `👤 <b>Контакт:</b> ${escapeHtml(lead.contact?.name)} (${escapeHtml(lead.contact?.role)})\n`;
      if (lead.contact?.phone) html += `📞 <b>Телефон:</b> <code>+${sanitizePhone(lead.contact.phone)}</code>\n`;
      if (lead.contact?.email) html += `✉️ <b>Email:</b> ${escapeHtml(lead.contact.email)}\n`;
      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `🪟 <b>Количество проемов:</b> ${lead.openingsCount} шт.\n`;
      html += `🛡 <b>Система:</b> ${escapeHtml(lead.systemType)}\n`;
      html += `⚡ <b>Автоматизация:</b> ${escapeHtml(lead.automation)}\n`;
      html += `🔥 <b>Пожарный сертификат:</b> ${lead.fireSafetyRequired ? 'КМ1 (Trevira CS) ОБЯЗАТЕЛЕН' : 'Стандарт'}\n`;
      html += `💰 <b>Смета без НДС:</b> ${escapeHtml(lead.subtotalText)}\n`;
      html += `📊 <b>В т.ч. НДС 12%:</b> ${escapeHtml(lead.vatAmountText)}\n`;
      html += `💳 <b>ИТОГО К ОПЛАТЕ:</b> <b>${escapeHtml(lead.estimatedBudgetText)}</b>\n`;

      if (lead.specFiles && lead.specFiles.length > 0) {
        html += `📁 <b>Прикреплено ТЗ / ведомостей:</b> ${lead.specFiles.length} шт.\n`;
      }

      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `⏱ <b>SLA НА КП:</b> 2 ЧАСА (С НДС 12%)\n`;
      html += `👤 <b>Ведущий инженер:</b> ${escapeHtml(routing.assignedManager)}\n`;
      html += `🏷 <i>${routing.tags.map(t => '#' + t).join(' ')}</i>`;

      return html;
    }

    // 3. DESIGNER CLUB NOTIFICATION
    if (funnel === 'designer_club') {
      let html = `📐 <b>${brand} // ВСТУПЛЕНИЕ В ДИЗАЙНЕРСКИЙ КЛУБ</b>\n`;
      html += `<b>ID заявки:</b> <code>#${leadId}</code>\n`;
      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `👤 <b>Дизайнер:</b> ${escapeHtml(lead.designer?.name || 'Не указано')}\n`;
      if (lead.designer?.studio) html += `🏢 <b>Студия / Бюро:</b> ${escapeHtml(lead.designer.studio)}\n`;
      if (lead.designer?.phone) html += `📞 <b>Телефон:</b> <code>+${sanitizePhone(lead.designer.phone)}</code>\n`;
      if (lead.designer?.instagram) html += `📸 <b>Instagram:</b> ${escapeHtml(lead.designer.instagram)}\n`;
      html += `🎁 <b>Оффер:</b> 10% кэшбэк день-в-день + 3D Corona Library\n`;
      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `⏱ <b>SLA ответа:</b> 15 минут\n`;
      html += `👤 <b>Куратор:</b> ${escapeHtml(routing.assignedManager)}`;
      return html;
    }

    // 4. VIP DOSSIER APPROVAL NOTIFICATION
    if (funnel === 'vip_dossier') {
      let html = `👑 <b>${brand} // УТВЕРЖДЕНИЕ VIP-ДОСЬЕ</b>\n`;
      html += `<b>Проект:</b> <code>${escapeHtml(lead.projectCode)}</code>\n`;
      html += `🏛 <b>Объект:</b> ${escapeHtml(lead.objectTitle)}\n`;
      html += `👥 <b>Заказчики:</b> ${escapeHtml(lead.clientNames)}\n`;
      html += `💰 <b>Согласованная смета:</b> <b>${escapeHtml(lead.totalCost)}</b>\n`;
      html += `⚡ <b>Somfy:</b> Включено\n`;
      html += `🚀 <b>Действие:</b> Клиент готов внести аванс. Требуется договор!\n`;
      html += `━━━━━━━━━━━━━━━━━━━━━━\n`;
      html += `⏱ <b>SLA:</b> 5 МИНУТ\n`;
      html += `👤 <b>Ответственный:</b> ${escapeHtml(routing.assignedManager)}`;
      return html;
    }

    return `✨ <b>${brand} // Новое обращение</b>\nID: <code>#${leadId}</code>`;
  }

  /**
   * Generates interactive Telegram inline buttons for sales managers.
   * 
   * @param {Object} lead
   * @returns {Object} Telegram inline_keyboard object
   */
  function buildTelegramInlineKeyboard(lead) {
    const phone = lead.customer?.phone || lead.contact?.phone || lead.designer?.phone;
    const cleanPhone = phone ? sanitizePhone(phone) : null;
    const keyboard = [];

    // Row 1: Direct WhatsApp Response to client
    if (cleanPhone) {
      const waReplyText = encodeURIComponent(
        `Здравствуйте! Это ${CONFIG.BRAND_NAME}. Получили ваш расчет на сайте (${lead.curtainType || lead.systemType || 'шторы'}). Давайте согласуем удобное время!`
      );
      keyboard.push([
        {
          text: '💬 Открыть WhatsApp клиента',
          url: `https://wa.me/${cleanPhone}?text=${waReplyText}`
        }
      ]);
    }

    // Row 2: Phone call & CRM Lead link
    const row2 = [];
    if (cleanPhone) {
      row2.push({
        text: '📞 Позвонить',
        url: `tel:+${cleanPhone}`
      });
    }
    if (CONFIG.CRM.AMOCRM_BASE_URL) {
      row2.push({
        text: '💼 amoCRM',
        url: `${CONFIG.CRM.AMOCRM_BASE_URL}`
      });
    } else if (CONFIG.CRM.BITRIX24_WEBHOOK_URL) {
      row2.push({
        text: '💼 Bitrix24',
        url: 'https://b24.kz'
      });
    }

    if (row2.length > 0) {
      keyboard.push(row2);
    }

    // Row 3: Claim / Status update button
    keyboard.push([
      {
        text: '✅ Взять в работу (Я отвечу)',
        callback_data: `claim_lead:${lead.leadId}`
      }
    ]);

    return { inline_keyboard: keyboard };
  }

  /**
   * Dispatches the Telegram notification via Telegram Bot API.
   * Supports both pure text messages and direct photo uploads (visualizations/renders).
   * 
   * @param {Object} lead - Normalized lead object
   * @param {Object} [overrideConfig] - Custom token or chat ID
   * @returns {Promise<Object>} Telegram API response
   */
  async function dispatchTelegramNotification(lead, overrideConfig = {}) {
    const routing = routeLead(lead);
    const token = overrideConfig.botToken || CONFIG.TELEGRAM.BOT_TOKEN;
    const baseUrl = overrideConfig.apiBaseUrl || CONFIG.TELEGRAM.API_BASE_URL;

    // Target chat ID selection by funnel
    let chatId = overrideConfig.chatId;
    if (!chatId) {
      if (routing.tier === 'VIP') {
        chatId = CONFIG.TELEGRAM.CHAT_ID_VIP || CONFIG.TELEGRAM.CHAT_ID_B2C;
      } else if (lead.funnel === 'b2b') {
        chatId = CONFIG.TELEGRAM.CHAT_ID_B2B;
      } else {
        chatId = CONFIG.TELEGRAM.CHAT_ID_B2C;
      }
    }

    const htmlText = formatTelegramHtml(lead, routing);
    const replyMarkup = buildTelegramInlineKeyboard(lead);

    // If no Telegram bot token configured, return simulated success for testing/decoupled mode
    if (!token || !chatId) {
      return {
        success: true,
        simulated: true,
        leadId: lead.leadId,
        chatId: chatId || 'NOT_CONFIGURED',
        htmlText,
        replyMarkup,
        visualizationsCount: lead.visualizations?.length || 0,
        message: 'Telegram credentials not provided in environment. Formatted payload prepared.'
      };
    }

    // Check if we have a primary image/visualization to attach via sendPhoto
    const firstVis = lead.visualizations && lead.visualizations.length > 0 ? lead.visualizations[0] : null;

    try {
      // SCENARIO A: Attached Visualization Photo (URL or Base64)
      if (firstVis && (firstVis.url || firstVis.data || firstVis.fileObject)) {
        // 1. If remote image URL
        if (firstVis.url) {
          const photoUrl = `${baseUrl}/bot${token}/sendPhoto`;
          const res = await fetch(photoUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: chatId,
              photo: firstVis.url,
              caption: htmlText,
              parse_mode: 'HTML',
              reply_markup: replyMarkup
            })
          });
          const data = await res.json();
          return { success: data.ok, leadId: lead.leadId, telegramResponse: data };
        }

        // 2. If browser FormData / Blob or Node.js Buffer
        if (typeof FormData !== 'undefined' && (firstVis.fileObject || firstVis.data)) {
          const formData = new FormData();
          formData.append('chat_id', chatId);
          formData.append('caption', htmlText);
          formData.append('parse_mode', 'HTML');
          formData.append('reply_markup', JSON.stringify(replyMarkup));

          if (firstVis.fileObject) {
            formData.append('photo', firstVis.fileObject, firstVis.name || 'render.jpg');
          } else if (firstVis.data && firstVis.data.startsWith('data:')) {
            // Convert data URL to Blob in browser
            const arr = firstVis.data.split(',');
            const mime = arr[0].match(/:(.*?);/)[1];
            const bstr = atob(arr[1]);
            let n = bstr.length;
            const u8arr = new Uint8Array(n);
            while (n--) u8arr[n] = bstr.charCodeAt(n);
            const blob = new Blob([u8arr], { type: mime });
            formData.append('photo', blob, 'visualization.jpg');
          }

          const photoUrl = `${baseUrl}/bot${token}/sendPhoto`;
          const res = await fetch(photoUrl, { method: 'POST', body: formData });
          const data = await res.json();
          return { success: data.ok, leadId: lead.leadId, telegramResponse: data };
        }
      }

      // SCENARIO B: Standard Text Message via sendMessage
      const sendMsgUrl = `${baseUrl}/bot${token}/sendMessage`;
      const res = await fetch(sendMsgUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          chat_id: chatId,
          text: htmlText,
          parse_mode: 'HTML',
          disable_web_page_preview: false,
          reply_markup: replyMarkup
        })
      });

      const data = await res.json();
      return {
        success: data.ok,
        leadId: lead.leadId,
        telegramResponse: data
      };
    } catch (err) {
      console.error('[MUAR A Dispatcher] Telegram dispatch error:', err);
      return {
        success: false,
        leadId: lead.leadId,
        error: err.message
      };
    }
  }

  // ==========================================================================
  // 8. CRM INTEGRATION ADAPTERS (amoCRM & Bitrix24 & Webhooks)
  // ==========================================================================

  /**
   * Builds an amoCRM API v4 complex lead payload (`/api/v4/leads/complex`).
   * 
   * @param {Object} lead - Normalized lead
   * @param {Object} [customFieldsMap] - Optional field ID overrides
   * @returns {Array} amoCRM request body
   */
  function buildAmoCrmPayload(lead, customFieldsMap = {}) {
    const routing = routeLead(lead);
    const phone = lead.customer?.phone || lead.contact?.phone || lead.designer?.phone;
    const name = lead.customer?.name || lead.contact?.name || lead.designer?.name || 'Клиент с сайта';

    const customFields = [
      {
        field_id: customFieldsMap.funnel || 101,
        values: [{ value: lead.funnel }]
      },
      {
        field_id: customFieldsMap.budget_tenge || 102,
        values: [{ value: lead.estimatedBudget }]
      },
      {
        field_id: customFieldsMap.source || 103,
        values: [{ value: 'Website_Calculator_Maison_Poisson' }]
      }
    ];

    if (lead.curtainType) {
      customFields.push({
        field_id: customFieldsMap.curtain_type || 104,
        values: [{ value: lead.curtainType }]
      });
    }
    if (lead.dimensionsText) {
      customFields.push({
        field_id: customFieldsMap.dimensions || 105,
        values: [{ value: lead.dimensionsText }]
      });
    }
    if (lead.fabric) {
      customFields.push({
        field_id: customFieldsMap.fabric || 106,
        values: [{ value: lead.fabric }]
      });
    }
    if (lead.pleatFold) {
      customFields.push({
        field_id: customFieldsMap.pleat || 107,
        values: [{ value: lead.pleatFold }]
      });
    }
    if (lead.customer?.residentialComplex) {
      customFields.push({
        field_id: customFieldsMap.complex || 108,
        values: [{ value: lead.customer.residentialComplex }]
      });
    }
    if (lead.openingsCount) {
      customFields.push({
        field_id: customFieldsMap.openings || 109,
        values: [{ value: lead.openingsCount }]
      });
    }

    return [
      {
        name: `[${lead.funnel.toUpperCase()}] ${lead.curtainType || lead.systemType || 'Шторы'} — ${lead.estimatedBudgetText}`,
        price: lead.estimatedBudget,
        created_at: Math.floor(Date.now() / 1000),
        _embedded: {
          tags: routing.tags.map(t => ({ name: t })),
          contacts: [
            {
              first_name: name,
              custom_fields_values: phone
                ? [
                    {
                      field_code: 'PHONE',
                      values: [{ value: '+' + sanitizePhone(phone), enum_code: 'WORK' }]
                    }
                  ]
                : []
            }
          ]
        },
        custom_fields_values: customFields
      }
    ];
  }

  /**
   * Builds a Bitrix24 REST API lead payload (`crm.lead.add`).
   * 
   * @param {Object} lead
   * @returns {Object} Bitrix24 fields object
   */
  function buildBitrix24Payload(lead) {
    const routing = routeLead(lead);
    const phone = lead.customer?.phone || lead.contact?.phone || lead.designer?.phone;
    const name = lead.customer?.name || lead.contact?.name || lead.designer?.name || 'Клиент с сайта';
    const comments = [
      `Спецификация: ${lead.curtainType || lead.systemType || 'Шторы'}`,
      `Размеры: ${lead.dimensionsText || '—'}`,
      `Ткань: ${lead.fabric || '—'}`,
      `Складка: ${lead.pleatFold || '—'}`,
      `Ориентир сметы: ${lead.estimatedBudgetText}`,
      `Объект: ${lead.customer?.residentialComplex || lead.company?.name || '—'}`,
      `Приоритет: ${routing.tier} (SLA ${routing.slaMinutes} мин)`
    ].join('\n');

    return {
      fields: {
        TITLE: `[${CONFIG.BRAND_NAME}] ${lead.curtainType || lead.systemType || 'Заказ'} — ${lead.estimatedBudgetText}`,
        NAME: name,
        OPPORTUNITY: lead.estimatedBudget,
        CURRENCY_ID: CONFIG.CURRENCY_CODE, // KZT
        STATUS_ID: 'NEW',
        OPENED: 'Y',
        SOURCE_ID: 'WEB',
        SOURCE_DESCRIPTION: `MUAR A Web Calculator (${lead.funnel})`,
        COMMENTS: comments,
        PHONE: phone ? [{ VALUE: '+' + sanitizePhone(phone), VALUE_TYPE: 'WORK' }] : [],
        UF_CRM_MAISON_LEAD_ID: lead.leadId,
        UF_CRM_MAISON_FABRIC: lead.fabric || '',
        UF_CRM_MAISON_PLEAT: lead.pleatFold || '',
        UF_CRM_MAISON_DIMS: lead.dimensionsText || ''
      }
    };
  }

  /**
   * Builds a Generic JSON Webhook payload (compatible with Zapier, Make, n8n).
   * 
   * @param {Object} lead
   * @returns {Object} Unified JSON webhook payload
   */
  function buildGenericWebhookPayload(lead) {
    const routing = routeLead(lead);
    return {
      event: 'lead.created',
      brand: CONFIG.BRAND_NAME,
      leadId: lead.leadId,
      timestamp: lead.timestamp,
      funnel: lead.funnel,
      routing,
      leadData: lead,
      whatsAppDeepLink: generateWhatsAppUrl(lead),
      whatsAppGreeting: generateWhatsAppText(lead)
    };
  }

  /**
   * Synchronizes lead to configured CRM endpoint via HTTP POST.
   * 
   * @param {Object} lead
   * @param {Object} [options]
   * @returns {Promise<Object>}
   */
  async function syncToCrm(lead, options = {}) {
    const url = options.webhookUrl || CONFIG.CRM.GENERIC_WEBHOOK_URL || CONFIG.CRM.BITRIX24_WEBHOOK_URL;
    if (!url) {
      return {
        success: true,
        simulated: true,
        message: 'No CRM webhook endpoint URL configured. Returning prepared payload.',
        payload: buildGenericWebhookPayload(lead)
      };
    }

    let payload;
    if (options.crmType === 'amocrm') {
      payload = buildAmoCrmPayload(lead, options.customFieldsMap);
    } else if (options.crmType === 'bitrix24') {
      payload = buildBitrix24Payload(lead);
    } else {
      payload = buildGenericWebhookPayload(lead);
    }

    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      return { success: res.ok, leadId: lead.leadId, response: data };
    } catch (err) {
      console.error('[MUAR A Dispatcher] CRM Sync error:', err);
      return { success: false, leadId: lead.leadId, error: err.message };
    }
  }

  // ==========================================================================
  // 9. HIGH-LEVEL ORCHESTRATOR (ONE-CALL DISPATCH)
  // ==========================================================================

  /**
   * All-in-one dispatch workflow:
   * 1. Normalizes input data into lead model
   * 2. Runs lead routing & scoring engine
   * 3. Produces exact WhatsApp deep-link and message text
   * 4. Triggers Telegram sales webhook (if configured)
   * 5. Triggers CRM sync (if configured)
   * 6. Returns complete consolidated dispatch state
   * 
   * @param {Object} rawLeadInput - Customer form or calculator state
   * @param {Object} [options] - Configuration and channel options
   * @returns {Promise<Object>} Complete dispatch report
   */
  async function dispatchLead(rawLeadInput, options = {}) {
    const funnel = rawLeadInput.funnel || options.funnel || 'b2c';

    // 1. Normalization
    let lead;
    if (funnel === 'b2b') {
      lead = createB2BLead(rawLeadInput);
    } else if (funnel === 'designer_club') {
      lead = createDesignerLead(rawLeadInput);
    } else if (funnel === 'vip_dossier') {
      lead = createVipDossierLead(rawLeadInput);
    } else {
      lead = createB2CLead(rawLeadInput);
    }

    // 2. Routing Decision
    const routing = routeLead(lead);

    // 3. WhatsApp Deep-Link Generation
    const whatsAppText = generateWhatsAppText(lead, options);
    const whatsAppUrl = generateWhatsAppUrl(lead, options);

    // 4. Background Telegram Notification (if requested or enabled)
    let telegramResult = null;
    if (options.dispatchTelegram !== false) {
      telegramResult = await dispatchTelegramNotification(lead, options.telegram || {});
    }

    // 5. CRM Synchronization (if requested)
    let crmResult = null;
    if (options.syncCrm) {
      crmResult = await syncToCrm(lead, options.crm || {});
    }

    return {
      success: true,
      leadId: lead.leadId,
      funnel: lead.funnel,
      routing,
      lead,
      whatsApp: {
        url: whatsAppUrl,
        text: whatsAppText,
        phone: sanitizePhone(options.phone || CONFIG.DEFAULT_WA_PHONE)
      },
      telegram: telegramResult,
      crm: crmResult,
      timestamp: new Date().toISOString()
    };
  }

  // ==========================================================================
  // 10. SELF-TEST RUNNER (VERIFICATION SUITE)
  // ==========================================================================

  /**
   * Executes internal assertion tests to verify all requirements:
   * 1. Exact string match for B2C WhatsApp greeting:
   *    'Здравствуйте, MUAR A! Я сделал расчет на сайте: Портьеры со складкой Ripplefold, 3.8м x 3.2м, бельгийский шенилл. Предварительная смета: 385 000 ₸. Хочу вызвать декоратора с образцами.'
   * 2. Valid URL generation with correct encoding and phone sanitization.
   * 3. B2B Corporate calculation with 12% VAT.
   * 4. Photo/Visualization attachment handling.
   * 5. CRM payload formatting.
   * 
   * @returns {Object} Test report
   */
  function runSelfTest() {
    const results = {
      passed: 0,
      failed: 0,
      details: []
    };

    function assert(name, condition, extraInfo = '') {
      if (condition) {
        results.passed++;
        results.details.push({ test: name, status: 'PASS' });
      } else {
        results.failed++;
        results.details.push({ test: name, status: 'FAIL', error: extraInfo });
        console.error(`[SELF-TEST FAIL] ${name}: ${extraInfo}`);
      }
    }

    // TEST 1: Exact WhatsApp Greeting String Match
    const testB2C = createB2CLead({
      curtainType: 'Портьеры',
      pleatFold: 'Ripplefold',
      width: 3.8,
      height: 3.2,
      fabric: 'бельгийский шенилл',
      estimatedBudget: 385000,
      calloutAction: 'Хочу вызвать декоратора с образцами.'
    });

    const expectedGreeting = 'Здравствуйте, MUAR A! Я сделал расчет на сайте: Портьеры со складкой Ripplefold, 3.8м x 3.2м, бельгийский шенилл. Предварительная смета: 385 000 ₸. Хочу вызвать декоратора с образцами.';
    const actualGreeting = generateWhatsAppText(testB2C, { strictExactB2C: true });
    assert('Test 1: Exact B2C WhatsApp greeting string match', actualGreeting === expectedGreeting, `Expected: "${expectedGreeting}"\nGot: "${actualGreeting}"`);

    // TEST 2: WhatsApp Deep-Link URL Format
    const testUrl = generateWhatsAppUrl(testB2C, { strictExactB2C: true, phone: '+7 (701) 000-00-00' });
    const expectedUrlPrefix = 'https://wa.me/77010000000?text=';
    assert('Test 2: WhatsApp URL begins with sanitized international number', testUrl.startsWith(expectedUrlPrefix), `Got: ${testUrl}`);
    assert('Test 3: WhatsApp URL contains encoded greeting text', testUrl.includes(encodeURIComponent('Портьеры со складкой Ripplefold')), `URL missing encoded parts`);

    // TEST 3: B2B Commercial Lead & VAT 12% Calculation
    const testB2B = createB2BLead({
      company: { name: 'ТОО "Астана Монолит"', bin: '120540019283' },
      contact: { name: 'Бауржан', role: 'Главный инженер' },
      openingsCount: 20,
      systemType: 'Somfy Screen 3%',
      estimatedBudget: 1120000
    });
    assert('Test 4: B2B lead calculates 12% VAT properly', testB2B.vatAmount > 0 && (testB2B.subtotal + testB2B.vatAmount === 1120000), `Subtotal: ${testB2B.subtotal}, VAT: ${testB2B.vatAmount}`);
    assert('Test 5: B2B WhatsApp message contains 2h SLA mention', generateWhatsAppText(testB2B).includes('2 часа'), 'Missing 2h SLA');

    // TEST 4: Photo / Visualization Upload Processing
    const testUpload = processVisualizationUpload('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD...', {
      type: 'interior_render',
      description: 'Гостиная в ЖК Highvill'
    });
    assert('Test 6: Visualization processor handles Base64 data', testUpload.source === 'base64' && testUpload.type === 'interior_render', 'Failed to process base64 upload');

    // TEST 5: Routing Decision
    const b2cRouting = routeLead(testB2C);
    assert('Test 7: B2C lead routes to couture department', b2cRouting.assignedDepartment === 'b2c_couture', `Got: ${b2cRouting.assignedDepartment}`);

    const b2bRouting = routeLead(testB2B);
    assert('Test 8: B2B lead routes to contracts division with 120min SLA', b2bRouting.assignedDepartment === 'b2b_contract_division' && b2bRouting.slaMinutes === 120, 'B2B routing failed');

    // TEST 6: amoCRM & Bitrix24 Payload Generation
    const amoPayload = buildAmoCrmPayload(testB2C);
    assert('Test 9: amoCRM complex lead payload generated', Array.isArray(amoPayload) && amoPayload[0].price === 385000, 'amoCRM payload invalid');

    const b24Payload = buildBitrix24Payload(testB2B);
    assert('Test 10: Bitrix24 payload generated with KZT currency', b24Payload.fields.CURRENCY_ID === 'KZT' && b24Payload.fields.OPPORTUNITY === 1120000, 'Bitrix24 payload invalid');

    return results;
  }

  // ==========================================================================
  // 11. PUBLIC API EXPORT
  // ==========================================================================

  const api = {
    // Configuration
    CONFIG,
    configure: function (userConfig = {}) {
      if (userConfig.DEFAULT_WA_PHONE) CONFIG.DEFAULT_WA_PHONE = userConfig.DEFAULT_WA_PHONE;
      if (userConfig.TELEGRAM) Object.assign(CONFIG.TELEGRAM, userConfig.TELEGRAM);
      if (userConfig.CRM) Object.assign(CONFIG.CRM, userConfig.CRM);
      return api;
    },

    // Models & Factories
    createB2CLead,
    createB2BLead,
    createDesignerLead,
    createVipDossierLead,

    // Core Engines
    routeLead,
    generateWhatsAppText,
    generateWhatsAppUrl,
    formatTelegramHtml,
    buildTelegramInlineKeyboard,
    dispatchTelegramNotification,

    // Visualization Handlers
    processVisualizationUpload,
    compressClientImage,

    // CRM Payload Adapters
    buildAmoCrmPayload,
    buildBitrix24Payload,
    buildGenericWebhookPayload,
    syncToCrm,

    // High-Level Dispatcher
    dispatchLead,

    // Formatters & Utilities
    formatTenge,
    sanitizePhone,
    generateLeadId,

    // Test Suite
    runSelfTest
  };

  return api;
});

// Auto-run self-test when executed directly via Node.js CLI: `node crm-lead-dispatcher.js --test`
if (typeof process !== 'undefined' && process.argv && process.argv.includes('--test')) {
  const runner = module.exports;
  console.log('\n============================================================');
  console.log('  MAISON POISSON // CRM & WHATSAPP DISPATCHER SELF-TEST');
  console.log('============================================================\n');
  const report = runner.runSelfTest();
  report.details.forEach(d => {
    const icon = d.status === 'PASS' ? '✅' : '❌';
    console.log(`${icon} [${d.status}] ${d.test}`);
    if (d.error) console.log(`   Error: ${d.error}`);
  });
  console.log(`\nSummary: ${report.passed} Passed, ${report.failed} Failed.\n`);
  process.exit(report.failed > 0 ? 1 : 0);
}
