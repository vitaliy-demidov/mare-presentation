/**
 * MAISON TEXTILE — COMPLETE INTERACTIVE ENGINE (ASTANA)
 * 1. Procedural Silk & Koi Canvas (60 FPS, Canvas 2D / WebGL lightweight)
 * 2. Two Doors Switcher (B2C Residential vs B2B Corporate)
 * 3. Haute Couture Pleat & Fabric Calculator (Tenge ₸)
 * 4. Voice AI Assistant (SpeechRecognition + NLP Parser + WhatsApp Deeplink)
 * 5. Interactive Before/After Splitter
 * 6. Secret VIP KP Dossier (PROJECT-70 / ASTANA-VILLA) with 4K Loupe & Day/Night switcher
 * 7. B2B Corporate Systems & VAT Calculator
 */

// ==========================================================================
// 1. PROCEDURAL SILK & KOI CANVAS (LIGHTWEIGHT 60 FPS)
// ==========================================================================
(function initSilkCanvas() {
  const canvas = document.getElementById('silkBackgroundCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let width, height;
  let time = 0;
  let mouseX = 0, mouseY = 0, targetMouseX = 0, targetMouseY = 0;
  let isRunning = true;

  function resize() {
    width = canvas.width = canvas.parentElement.clientWidth;
    height = canvas.height = canvas.parentElement.clientHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  window.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    targetMouseX = e.clientX - rect.left;
    targetMouseY = e.clientY - rect.top;
  });

  // Koi Fish data (2 elegant koi swimming gracefully)
  const kois = [
    { x: 150, y: 200, speed: 0.8, angle: 0.4, length: 70, color: 'rgba(197, 168, 128, 0.22)' },
    { x: 450, y: 350, speed: 0.65, angle: 2.1, length: 90, color: 'rgba(158, 130, 85, 0.18)' }
  ];

  function draw() {
    if (!isRunning) return;
    time += 0.015;
    mouseX += (targetMouseX - mouseX) * 0.05;
    mouseY += (targetMouseY - mouseY) * 0.05;

    ctx.clearRect(0, 0, width, height);

    // Flowing Silk Wave lines (Vertical drapery folds)
    const waveCount = 7;
    for (let i = 0; i < waveCount; i++) {
      ctx.beginPath();
      const baseX = (width / (waveCount + 1)) * (i + 1);
      ctx.moveTo(baseX, 0);

      for (let y = 0; y <= height; y += 25) {
        const distToMouse = Math.hypot(baseX - mouseX, y - mouseY);
        const mouseRepel = Math.max(0, 45 - distToMouse * 0.12);
        const waveOffset = Math.sin(y * 0.008 + time + i) * 24 +
                           Math.cos(y * 0.015 - time * 0.8) * 12 +
                           (baseX < mouseX ? -mouseRepel : mouseRepel);
        ctx.lineTo(baseX + waveOffset, y);
      }

      ctx.strokeStyle = i % 2 === 0 ? 'rgba(197, 168, 128, 0.16)' : 'rgba(247, 245, 240, 0.06)';
      ctx.lineWidth = i === 3 ? 2 : 1;
      ctx.stroke();
    }

    // Gentle swimming Koi fish silhouettes
    kois.forEach((koi, idx) => {
      koi.x += Math.cos(koi.angle) * koi.speed;
      koi.y += Math.sin(koi.angle) * koi.speed;
      koi.angle += Math.sin(time * 0.5 + idx) * 0.008;

      if (koi.x < -100) koi.x = width + 100;
      if (koi.x > width + 100) koi.x = -100;
      if (koi.y < -100) koi.y = height + 100;
      if (koi.y > height + 100) koi.y = -100;

      ctx.save();
      ctx.translate(koi.x, koi.y);
      ctx.rotate(koi.angle);

      // Koi Body
      ctx.beginPath();
      ctx.ellipse(0, 0, koi.length * 0.45, koi.length * 0.16, 0, 0, Math.PI * 2);
      ctx.fillStyle = koi.color;
      ctx.fill();

      // Tail with sin wave motion
      const tailWiggle = Math.sin(time * 4 + idx) * 8;
      ctx.beginPath();
      ctx.moveTo(-koi.length * 0.35, 0);
      ctx.quadraticCurveTo(-koi.length * 0.65, tailWiggle * 0.5, -koi.length * 0.85, tailWiggle);
      ctx.lineTo(-koi.length * 0.75, -tailWiggle * 0.5);
      ctx.closePath();
      ctx.fillStyle = koi.color;
      ctx.fill();

      ctx.restore();
    });

    requestAnimationFrame(draw);
  }

  // Freeze RAF when offscreen or document hidden
  document.addEventListener('visibilitychange', () => {
    isRunning = !document.hidden;
    if (isRunning) requestAnimationFrame(draw);
  });

  requestAnimationFrame(draw);
})();

// ==========================================================================
// 2. TWO DOORS SWITCHER (B2C RESIDENTIAL VS B2B CORPORATE)
// ==========================================================================
let currentDoor = 'b2c'; // 'b2c' or 'b2b'

function switchDoor(door) {
  currentDoor = door;
  const b2cElements = document.querySelectorAll('.flow-b2c');
  const b2bElements = document.querySelectorAll('.flow-b2b');
  const btnB2C = document.getElementById('doorBtnB2C');
  const btnB2B = document.getElementById('doorBtnB2B');
  const statusBadge = document.getElementById('topDoorBadge');

  if (door === 'b2c') {
    b2cElements.forEach(el => el.classList.remove('hidden'));
    b2bElements.forEach(el => el.classList.add('hidden'));

    if (btnB2C) {
      btnB2C.className = "px-5 py-2.5 rounded-full text-xs font-semibold bg-obsidian text-white shadow-sm transition flex items-center gap-2";
    }
    if (btnB2B) {
      btnB2B.className = "px-5 py-2.5 rounded-full text-xs font-medium text-obsidian/70 hover:text-obsidian transition";
    }
    if (statusBadge) {
      statusBadge.innerHTML = 'Собственный цех 350 м² в Астане: открыт прием заказов на сезон 2026-2027';
    }
  } else {
    b2cElements.forEach(el => el.classList.add('hidden'));
    b2bElements.forEach(el => el.classList.remove('hidden'));

    if (btnB2B) {
      btnB2B.className = "px-5 py-2.5 rounded-full text-xs font-semibold bg-brass text-white shadow-sm transition flex items-center gap-2";
    }
    if (btnB2C) {
      btnB2C.className = "px-5 py-2.5 rounded-full text-xs font-medium text-obsidian/70 hover:text-obsidian transition";
    }
    if (statusBadge) {
      statusBadge.innerHTML = 'B2B Контрактный отдел: расчет с НДС 12% • Ткани Trevira CS (КМ1) • Экспресс-КП за 2 часа';
    }
  }
}

// ==========================================================================
// 3. HAUTE COUTURE PLEAT & FABRIC CALCULATOR (TENGE ₸)
// ==========================================================================
const B2C_PRICES = {
  fabrics: {
    chenille: { name: 'Шенилл Wind (Бельгия)', pricePerMeter: 24500, origin: 'Бельгия', density: '460 г/м²' },
    velvet: { name: 'Бархат Dedar Soft (Италия)', pricePerMeter: 28000, origin: 'Италия', density: '520 г/м²' },
    linen: { name: 'Европейский Лён Casamance', pricePerMeter: 19800, origin: 'Франция', density: '280 г/м²' },
    blackout: { name: '100% Blackout Soft Touch', pricePerMeter: 16500, origin: 'Турция', density: '360 г/м²' }
  },
  pleats: {
    wave: { name: 'Идеальная Волна (Wave)', ratio: 2.0, desc: 'Лаконичный ритм, шаг 16 см. Идеально для высоких потолков и новостроек.' },
    french: { name: 'Французская тройная (Pinch)', ratio: 2.5, desc: 'Ручная зашивка в 3 лепестка, максимальная пышность и светоизоляция.' },
    box: { name: 'Бантовая (Box Pleat)', ratio: 2.2, desc: 'Архитектурная строгая симметрия парадных гостиных и резиденций.' }
  },
  tailoringPerMeter: 6500, // ручной потайной шов, ВТО, премиум тесьма Bandex Австрия
  tullePerMeter: 12500,
  somfyMotor: 125000 // электрокарниз Somfy Glydea Ultra с интеграцией Алиса/HomeKit
};

let calcState = {
  product: 'curtains', // 'curtains', 'roman', 'bedspread'
  width: 3.2,
  height: 3.0,
  windows: 1,
  pleat: 'wave',
  fabric: 'chenille',
  includeTulle: true,
  includeSomfy: false
};

function updateB2CCalculator() {
  const fabricData = B2C_PRICES.fabrics[calcState.fabric];
  const pleatData = B2C_PRICES.pleats[calcState.pleat];

  // Fabric meter calculation
  const gatheredWidth = calcState.width * pleatData.ratio;
  const totalMeters = (gatheredWidth + 0.4) * calcState.windows; // +0.4m for hem/seams

  // Costs
  const fabricCost = totalMeters * fabricData.pricePerMeter;
  const tailoringCost = totalMeters * B2C_PRICES.tailoringPerMeter;
  const tulleCost = calcState.includeTulle ? (calcState.width * 2.2 * B2C_PRICES.tullePerMeter * calcState.windows) : 0;
  const motorCost = calcState.includeSomfy ? (B2C_PRICES.somfyMotor * calcState.windows) : 0;
  const totalEstimate = Math.round(fabricCost + tailoringCost + tulleCost + motorCost);

  // Update DOM elements
  const elTotal = document.getElementById('calcTotalEstimate');
  const elFabricName = document.getElementById('calcFabricName');
  const elMeters = document.getElementById('calcMeters');
  const elPleatDesc = document.getElementById('calcPleatDesc');
  const elTailoring = document.getElementById('calcTailoring');
  const elWidthVal = document.getElementById('calcWidthVal');
  const elHeightVal = document.getElementById('calcHeightVal');

  if (elTotal) elTotal.innerText = totalEstimate.toLocaleString('ru-RU') + ' ₸';
  if (elFabricName) elFabricName.innerText = fabricData.name;
  if (elMeters) elMeters.innerText = totalMeters.toFixed(1) + ' пог. м';
  if (elPleatDesc) elPleatDesc.innerText = pleatData.desc;
  if (elTailoring) elTailoring.innerText = tailoringCost.toLocaleString('ru-RU') + ' ₸';
  if (elWidthVal) elWidthVal.innerText = calcState.width + ' м';
  if (elHeightVal) elHeightVal.innerText = calcState.height + ' м';

  // Update Pleat SVG Preview
  updatePleatPreview(calcState.pleat);
}

function selectPleat(pleatKey) {
  calcState.pleat = pleatKey;
  ['wave', 'french', 'box'].forEach(k => {
    const btn = document.getElementById('btnPleat_' + k);
    if (btn) {
      if (k === pleatKey) {
        btn.classList.add('border-brass', 'bg-brass/10', 'text-obsidian', 'font-bold');
        btn.classList.remove('border-borderSubtle', 'bg-white');
      } else {
        btn.classList.remove('border-brass', 'bg-brass/10', 'text-obsidian', 'font-bold');
        btn.classList.add('border-borderSubtle', 'bg-white');
      }
    }
  });
  updateB2CCalculator();
}

function selectFabric(fabricKey) {
  calcState.fabric = fabricKey;
  ['chenille', 'velvet', 'linen', 'blackout'].forEach(k => {
    const card = document.getElementById('cardFabric_' + k);
    if (card) {
      if (k === fabricKey) {
        card.classList.add('border-brass', 'ring-1', 'ring-brass', 'bg-brass/5');
      } else {
        card.classList.remove('border-brass', 'ring-1', 'ring-brass', 'bg-brass/5');
      }
    }
  });
  updateB2CCalculator();
}

function updatePleatPreview(pleatType) {
  const container = document.getElementById('pleatShapeVisual');
  if (!container) return;

  if (pleatType === 'wave') {
    container.innerHTML = `
      <svg class="w-full h-16 text-brass" viewBox="0 0 320 60" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M10 30 Q 30 10, 50 30 T 90 30 T 130 30 T 170 30 T 210 30 T 250 30 T 290 30 T 310 30" stroke-linecap="round"/>
        <line x1="10" y1="30" x2="10" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="50" y1="30" x2="50" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="90" y1="30" x2="90" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="130" y1="30" x2="130" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="170" y1="30" x2="170" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="210" y1="30" x2="210" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="250" y1="30" x2="250" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
        <line x1="290" y1="30" x2="290" y2="58" stroke-opacity="0.3" stroke-width="1.5"/>
      </svg>
    `;
  } else if (pleatType === 'french') {
    container.innerHTML = `
      <svg class="w-full h-16 text-brass" viewBox="0 0 320 60" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M15 15 L 20 30 L 25 15 M 20 30 L 20 58 M 75 15 L 80 30 L 85 15 M 80 30 L 80 58 M 135 15 L 140 30 L 145 15 M 140 30 L 140 58 M 195 15 L 200 30 L 205 15 M 200 30 L 200 58 M 255 15 L 260 30 L 265 15 M 260 30 L 260 58 M 305 15 L 310 30" stroke-linecap="round"/>
      </svg>
    `;
  } else {
    container.innerHTML = `
      <svg class="w-full h-16 text-brass" viewBox="0 0 320 60" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M10 20 H 40 V 40 H 65 V 20 H 95 V 40 H 120 V 20 H 150 V 40 H 175 V 20 H 205 V 40 H 230 V 20 H 260 V 40 H 285 V 20 H 310" stroke-linejoin="round"/>
      </svg>
    `;
  }
}

function sendCalcToWhatsApp() {
  const fabricData = B2C_PRICES.fabrics[calcState.fabric];
  const pleatData = B2C_PRICES.pleats[calcState.pleat];
  const total = document.getElementById('calcTotalEstimate')?.innerText || '40 395 ₸';

  const text = `Здравствуйте, Maison Textile!
Я рассчитал предварительную смету штор на сайте:

🧵 Ткань: ${fabricData.name} (${fabricData.origin})
📐 Размеры окна: ${calcState.width} м (ширина) × ${calcState.height} м (высота)
🪟 Тип складки: ${pleatData.name}
✨ Опции: ${calcState.includeTulle ? '+ Тюль' : ''} ${calcState.includeSomfy ? '+ Электрокарниз Somfy' : ''}
💰 Ориентировочный бюджет: ${total}

Хочу согласовать бесплатный выезд дизайнера с чемоданом образцов на объект в Астане!`;

  window.open(`https://wa.me/77010000000?text=${encodeURIComponent(text)}`, '_blank');
}

// ==========================================================================
// 4. VOICE AI ASSISTANT (SPEECH RECOGNITION + TEXTILE NLP ENGINE)
// ==========================================================================

const FABRIC_CATALOG = {
  chenille: {
    key: 'chenille',
    name: 'Шенилл Wind',
    origin: 'Бельгия',
    pricePerMeterKZT: 24500,
    pricePerMeterRUB: 4900,
    density: '460 г/м²',
    aliases: ['шенилл', 'sheeneel', 'sheenel', 'шенил', 'chenille', 'шениловая', 'шениловые']
  },
  silk: {
    key: 'silk',
    name: 'Натуральный Шёлк D’Este',
    origin: 'Италия',
    pricePerMeterKZT: 32000,
    pricePerMeterRUB: 6400,
    density: '240 г/м²',
    aliases: ['шелк', 'шёлк', 'silk', 'шелковый', 'шелковые', 'натуральный шелк', 'итальянский шелк']
  },
  linen: {
    key: 'linen',
    name: 'Европейский Лён Casamance',
    origin: 'Франция',
    pricePerMeterKZT: 19800,
    pricePerMeterRUB: 3960,
    density: '280 г/м²',
    aliases: ['лен', 'лён', 'linen', 'эко-лен', 'эколен', 'льняной', 'льняные', 'casamance']
  },
  trevira: {
    key: 'trevira',
    name: 'Контрактный Trevira CS (КМ1)',
    origin: 'Франция',
    pricePerMeterKZT: 26000,
    pricePerMeterRUB: 5200,
    density: '380 г/м²',
    aliases: ['trevira', 'trevira cs', 'тревира', 'тревира кс', 'негорюч', 'негорючая', 'огнестойк', 'км1']
  },
  velvet: {
    key: 'velvet',
    name: 'Бархат Dedar Soft Touch',
    origin: 'Италия',
    pricePerMeterKZT: 28000,
    pricePerMeterRUB: 5600,
    density: '520 г/м²',
    aliases: ['бархат', 'велюр', 'velvet', 'dedar', 'жаккард', 'бархатные', 'велюровые']
  },
  blackout: {
    key: 'blackout',
    name: '100% Blackout Soft Touch',
    origin: 'Турция',
    pricePerMeterKZT: 16500,
    pricePerMeterRUB: 3300,
    density: '360 г/м²',
    aliases: ['блэкаут', 'blackout', 'блэк аут', 'светонепроницаем', '100% blackout']
  }
};

const PLEAT_CATALOG = {
  wave: {
    key: 'wave',
    name: 'Идеальная Волна (Wave 1:2.0)',
    ratio: 2.0,
    desc: 'Равномерный шаг 16 см, лаконичный ритм. Идеально для панорамных окон.',
    aliases: ['волна', 'wave', 'волнообразная', 'волны']
  },
  french: {
    key: 'french',
    name: 'Французская тройная (1:2.5)',
    ratio: 2.5,
    desc: 'Ручная зашивка складок в 3 лепестка, пышная драпировка.',
    aliases: ['французск', 'тройная', 'тройн', 'pinch', 'пинч']
  },
  box: {
    key: 'box',
    name: 'Бантовая (Box 1:2.2)',
    ratio: 2.2,
    desc: 'Архитектурная строгая симметрия парадных залов и кабинетов.',
    aliases: ['бант', 'бантовая', 'box']
  }
};

const ROOM_CATALOG = {
  kids: {
    key: 'kids',
    name: 'Детская комната',
    shortName: 'Детская',
    defaultFabric: 'chenille',
    defaultOrigin: 'Бельгия',
    aliases: ['детск', 'детская', 'детскую', 'для ребенка', 'для детей']
  },
  living: {
    key: 'living',
    name: 'Парадная гостиная',
    shortName: 'Гостиная',
    defaultFabric: 'silk',
    defaultOrigin: 'Италия',
    aliases: ['гостин', 'гостиная', 'гостиную', 'зал', 'гостинной']
  },
  office: {
    key: 'office',
    name: 'Кабинет руководителя / Офис',
    shortName: 'Кабинет',
    defaultFabric: 'trevira',
    defaultOrigin: 'Франция',
    aliases: ['кабинет', 'офис', 'переговорн', 'кабинета', 'кабинету', 'для юрлиц', 'b2b', 'бизнес']
  },
  bedroom: {
    key: 'bedroom',
    name: 'Мастер-спальня',
    shortName: 'Спальня',
    defaultFabric: 'linen',
    defaultOrigin: 'Франция',
    aliases: ['спальн', 'спальня', 'спальню', 'мастер-спальня', 'спальной']
  },
  kitchen: {
    key: 'kitchen',
    name: 'Кухня-столовая',
    shortName: 'Кухня',
    defaultFabric: 'linen',
    defaultOrigin: 'Франция',
    aliases: ['кухн', 'кухня', 'кухню', 'столов', 'кухонн']
  }
};

// Global Voice State
const voiceState = {
  currency: 'kzt', // 'kzt' or 'rub'
  room: 'Детская',
  fabricKey: 'chenille',
  origin: 'Бельгия',
  width: 3.0,
  height: 2.8,
  windows: 1,
  pleatKey: 'wave',
  isListening: false,
  transcript: '',
  tailoringRateKZT: 6500,
  rubRate: 0.20 // 1 KZT = 0.20 RUB
};

let recognition = null;
let audioContext = null;
let analyserNode = null;
let audioStream = null;
let waveformAnimId = null;

/**
 * Format currency amounts according to active currency
 */
function formatVoicePrice(kztAmount) {
  if (voiceState.currency === 'rub') {
    const rub = Math.round(kztAmount * voiceState.rubRate);
    return rub.toLocaleString('ru-RU') + ' ₽';
  }
  return Math.round(kztAmount).toLocaleString('ru-RU') + ' ₸';
}

/**
 * Initialize Voice AI Engine and UI listeners
 */
function initVoiceAI() {
  initAudioWaveformCanvas();
  setupSpeechRecognition();
  setupVoiceUIEvents();
  updateVoiceCalculationUI();
}

/**
 * Real-time Audio Waveform Canvas Visualizer (60 FPS)
 */
function initAudioWaveformCanvas() {
  const canvas = document.getElementById('audioWaveformCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let time = 0;
  const barCount = 32;

  function renderWaveform() {
    time += 0.04;
    const width = canvas.width;
    const height = canvas.height;
    ctx.clearRect(0, 0, width, height);

    let freqData = null;
    if (analyserNode && voiceState.isListening) {
      freqData = new Uint8Array(analyserNode.frequencyBinCount);
      analyserNode.getByteFrequencyData(freqData);
    }

    const barWidth = width / barCount - 2;

    for (let i = 0; i < barCount; i++) {
      let barHeight;

      if (freqData && voiceState.isListening) {
        const bin = Math.floor((i / barCount) * freqData.length * 0.75);
        const val = freqData[bin] || 0;
        barHeight = Math.max(4, (val / 255) * (height - 6));
      } else if (voiceState.isListening) {
        // Simulated speech energy when microphone permission granted without AudioContext
        const wave = Math.sin(time * 6 + i * 0.4) * Math.cos(time * 3 + i * 0.2);
        barHeight = Math.max(6, Math.abs(wave) * (height - 8) + 8);
      } else {
        // Idle gentle breathing rhythm
        const wave = Math.sin(time * 2 + i * 0.25);
        barHeight = Math.max(3, (wave * 0.5 + 0.5) * (height * 0.35) + 3);
      }

      const x = i * (barWidth + 2) + 1;
      const y = (height - barHeight) / 2;

      // Color gradient: champagne gold when idle, rose-red pulsing when listening
      const gradient = ctx.createLinearGradient(0, y, 0, y + barHeight);
      if (voiceState.isListening) {
        gradient.addColorStop(0, '#fda4af');
        gradient.addColorStop(1, '#e11d48');
      } else {
        gradient.addColorStop(0, '#C5A880');
        gradient.addColorStop(1, '#9E8255');
      }

      ctx.fillStyle = gradient;
      ctx.beginPath();
      const radius = Math.min(barWidth / 2, 2);
      ctx.roundRect ? ctx.roundRect(x, y, barWidth, barHeight, radius) : ctx.rect(x, y, barWidth, barHeight);
      ctx.fill();
    }

    waveformAnimId = requestAnimationFrame(renderWaveform);
  }

  if (!waveformAnimId) {
    waveformAnimId = requestAnimationFrame(renderWaveform);
  }
}

/**
 * Configure Web Speech API
 */
function setupSpeechRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    console.warn('Web Speech API is not supported in this browser. Fallback chips are active.');
    return;
  }

  try {
    recognition = new SpeechRecognition();
    recognition.lang = 'ru-RU';
    recognition.continuous = false;
    recognition.interimResults = true;

    recognition.onstart = () => {
      voiceState.isListening = true;
      updateVoiceVisualState(true, 'Слушаю вас... Назовите параметры');
      setupMicrophoneAudioStream();
    };

    recognition.onresult = (event) => {
      let interim = '';
      let final = '';

      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          final += event.results[i][0].transcript;
        } else {
          interim += event.results[i][0].transcript;
        }
      }

      const currentText = final || interim;
      setTranscriptDisplay(currentText);

      if (final) {
        processVoiceInput(final);
      }
    };

    recognition.onerror = (e) => {
      console.warn('SpeechRecognition error:', e.error);
      voiceState.isListening = false;
      updateVoiceVisualState(false, 'Нажмите микрофон или выберите готовый образец');
    };

    recognition.onend = () => {
      voiceState.isListening = false;
      updateVoiceVisualState(false, 'Готов к диалогу');
    };
  } catch (err) {
    console.warn('Error creating SpeechRecognition:', err);
  }
}

/**
 * Connect microphone audio stream to AnalyserNode for real audio visualizer
 */
async function setupMicrophoneAudioStream() {
  if (analyserNode) return;
  try {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      audioStream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        audioContext = new AudioCtx();
        const source = audioContext.createMediaStreamSource(audioStream);
        analyserNode = audioContext.createAnalyser();
        analyserNode.fftSize = 64;
        source.connect(analyserNode);
      }
    }
  } catch (e) {
    // User denied mic stream or in non-secure context; fallback mathematical wave continues smoothly
  }
}

/**
 * Toggle voice recording on/off
 */
function toggleVoiceListening() {
  if (!recognition) {
    setupSpeechRecognition();
  }

  if (!recognition) {
    setTranscriptDisplay('Голосовой ввод не поддерживается в этом браузере. Выберите готовый образец ниже:');
    return;
  }

  if (voiceState.isListening) {
    recognition.stop();
  } else {
    try {
      recognition.start();
    } catch (err) {
      console.warn('Recognition start error:', err);
    }
  }
}

/**
 * Update visual microphone and status states
 */
function updateVoiceVisualState(listening, statusText) {
  voiceState.isListening = listening;

  const btnMic = document.getElementById('btnMic') || document.getElementById('micBtn') || document.getElementById('btnVoiceMic');
  const actionArea = document.getElementById('micActionArea');
  const heroCard = document.getElementById('voiceHeroCard');
  const statusLabel = document.getElementById('voiceStatusText') || document.getElementById('micHint') || document.getElementById('voiceStatusLabel');
  const headerState = document.getElementById('headerVoiceStateText');

  if (btnMic) {
    if (listening) {
      btnMic.classList.add('btn-mic-listening', 'rec', 'btn-mic-active');
    } else {
      btnMic.classList.remove('btn-mic-listening', 'rec', 'btn-mic-active');
    }
  }

  if (actionArea) {
    listening ? actionArea.classList.add('is-listening') : actionArea.classList.remove('is-listening');
  }

  if (heroCard) {
    listening ? heroCard.classList.add('is-listening') : heroCard.classList.remove('is-listening');
  }

  if (statusLabel) {
    statusLabel.innerText = statusText;
  }

  if (headerState) {
    headerState.innerText = listening ? 'Слушаю вас...' : 'Voice AI Консьерж';
  }
}

/**
 * Set transcript text in bubble
 */
function setTranscriptDisplay(text) {
  const el = document.getElementById('transcriptText') || document.getElementById('voiceTranscriptText');
  const bubble = document.getElementById('transcriptBubble');

  if (el) {
    el.innerHTML = `«${text}»`;
  }
  if (bubble) {
    bubble.classList.add('is-active');
  }
}

/**
 * Domain NLP Entity Extractor:
 * Extracts Room, Fabric, Origin/Style, Dimensions, Pleat, and Quantity.
 */
function parseVoiceEntities(rawText) {
  const lower = rawText.toLowerCase().trim();
  let extracted = {
    room: voiceState.room,
    fabricKey: voiceState.fabricKey,
    origin: voiceState.origin,
    width: voiceState.width,
    height: voiceState.height,
    pleatKey: voiceState.pleatKey,
    windows: voiceState.windows
  };

  // 1. EXTRACT ROOM
  for (const rKey in ROOM_CATALOG) {
    const roomItem = ROOM_CATALOG[rKey];
    if (roomItem.aliases.some(alias => lower.includes(alias))) {
      extracted.room = roomItem.shortName;
      // If fabric not yet explicitly set, inherit room recommendation
      if (!lower.includes('шенил') && !lower.includes('sheen') && !lower.includes('шелк') && !lower.includes('лен') && !lower.includes('trevira') && !lower.includes('бархат')) {
        extracted.fabricKey = roomItem.defaultFabric;
        extracted.origin = roomItem.defaultOrigin;
      }
      break;
    }
  }

  // 2. EXTRACT FABRIC (Explicit check, including Asima's phonetic 'sheeneel')
  for (const fKey in FABRIC_CATALOG) {
    const fabricItem = FABRIC_CATALOG[fKey];
    if (fabricItem.aliases.some(alias => lower.includes(alias))) {
      extracted.fabricKey = fKey;
      extracted.origin = fabricItem.origin;
      break;
    }
  }

  // 3. EXTRACT ORIGIN / COUNTRY OVERRIDE
  if (lower.includes('бельг') || lower.includes('belgium') || lower.includes('wind')) {
    extracted.origin = 'Бельгия';
  } else if (lower.includes('итал') || lower.includes('italy') || lower.includes('dedar')) {
    extracted.origin = 'Италия';
  } else if (lower.includes('франц') || lower.includes('france') || lower.includes('casamance')) {
    extracted.origin = 'Франция';
  } else if (lower.includes('турц') || lower.includes('turkey')) {
    extracted.origin = 'Турция';
  }

  // 4. EXTRACT DIMENSIONS (e.g. "3 на 2.80", "3.2 на 2.8", "окно 4 на 3")
  const dimMatch = lower.match(/(?:окно|окна|проем|размер)?\s*(\d+(?:[.,]\d+)?)\s*(?:на|x|х|по)\s*(\d+(?:[.,]\d+)?)/i);
  if (dimMatch) {
    const w = parseFloat(dimMatch[1].replace(',', '.'));
    const h = parseFloat(dimMatch[2].replace(',', '.'));
    if (!isNaN(w) && w >= 0.5 && w <= 25) extracted.width = w;
    if (!isNaN(h) && h >= 1.0 && h <= 12) extracted.height = h;
  }

  // 5. EXTRACT PLEAT TYPE
  for (const pKey in PLEAT_CATALOG) {
    const pleatItem = PLEAT_CATALOG[pKey];
    if (pleatItem.aliases.some(alias => lower.includes(alias))) {
      extracted.pleatKey = pKey;
      break;
    }
  }

  // 6. EXTRACT WINDOWS QUANTITY (e.g. "2 окна", "5 окон", "10 проемов")
  const winMatch = lower.match(/(\d+)\s*(?:окна|окон|окно|проемов|проема|проем|шт)/i);
  if (winMatch) {
    const q = parseInt(winMatch[1], 10);
    if (!isNaN(q) && q >= 1 && q <= 100) extracted.windows = q;
  }

  return extracted;
}

/**
 * Process text recognized by voice or triggered by sample buttons
 */
function processVoiceInput(text) {
  const entities = parseVoiceEntities(text);

  voiceState.room = entities.room;
  voiceState.fabricKey = entities.fabricKey;
  voiceState.origin = entities.origin;
  voiceState.width = entities.width;
  voiceState.height = entities.height;
  voiceState.pleatKey = entities.pleatKey;
  voiceState.windows = entities.windows;

  updateVoiceCalculationUI();

  // If on main page, sync on-page calculator directly
  if (typeof syncMainPageCalculator === 'function') {
    syncMainPageCalculator(entities);
  }
}

/**
 * Synchronize with the main portal calculator if present on the page
 */
function syncMainPageCalculator(entities) {
  if (typeof calcState !== 'undefined' && calcState.b2c) {
    calcState.b2c.w = entities.width;
    calcState.b2c.h = entities.height;
    calcState.b2c.q = entities.windows;

    const inW = document.getElementById('b2c-w');
    const inH = document.getElementById('b2c-h');
    const inQ = document.getElementById('b2c-q');
    if (inW) inW.value = entities.width;
    if (inH) inH.value = entities.height;
    if (inQ) inQ.value = entities.windows;

    // Set fabric chip
    const fabChip = document.querySelector(`.chips[data-group="fabric"] .chip[data-v="${entities.fabricKey}"]`);
    if (fabChip) fabChip.click();

    // Set pleat chip
    const foldChip = document.querySelector(`.chips[data-group="fold"] .chip[data-v="${entities.pleatKey}"]`);
    if (foldChip) foldChip.click();

    if (typeof recalc === 'function') {
      recalc(false);
    }
  }
}

/**
 * Calculate totals and update all UI elements & WhatsApp CTA
 */
function updateVoiceCalculationUI() {
  const fabric = FABRIC_CATALOG[voiceState.fabricKey] || FABRIC_CATALOG.chenille;
  const pleat = PLEAT_CATALOG[voiceState.pleatKey] || PLEAT_CATALOG.wave;

  // Textile formula: (Width * Pleat Ratio + 0.4m hem) * windows
  const gatheredPerWindow = voiceState.width * pleat.ratio;
  const totalMeters = (gatheredPerWindow + 0.4) * voiceState.windows;

  const fabricCostKZT = totalMeters * fabric.pricePerMeterKZT;
  const tailoringCostKZT = totalMeters * voiceState.tailoringRateKZT;
  const totalCostKZT = fabricCostKZT + tailoringCostKZT;

  // DOM Elements
  const elRoom = document.getElementById('resRoom');
  const elDims = document.getElementById('resDimensions');
  const elFabric = document.getElementById('resFabric');
  const elOrigin = document.getElementById('resOriginBadge');
  const elMeters = document.getElementById('resMeters');
  const elPleat = document.getElementById('resPleat');
  const elTotal = document.getElementById('resTotalCost');
  const elFabricCost = document.getElementById('resFabricCost');
  const elTailoringCost = document.getElementById('resTailoringCost');
  const elPriceNote = document.getElementById('resPriceNote');
  const elTitle = document.getElementById('resTitle');

  if (elRoom) elRoom.innerText = voiceState.room;
  if (elDims) elDims.innerText = `${voiceState.width.toFixed(2)} × ${voiceState.height.toFixed(2)} м` + (voiceState.windows > 1 ? ` (${voiceState.windows} ок.)` : '');
  if (elFabric) {
    elFabric.innerHTML = `${fabric.name} <span class="fabric-badge-origin" id="resOriginBadge">${voiceState.origin}</span>`;
  }
  if (elMeters) elMeters.innerText = `${totalMeters.toFixed(1)} пог. м`;
  if (elPleat) elPleat.innerText = pleat.name;
  if (elTotal) elTotal.innerText = formatVoicePrice(totalCostKZT);
  if (elFabricCost) elFabricCost.innerText = formatVoicePrice(fabricCostKZT);
  if (elTailoringCost) elTailoringCost.innerText = formatVoicePrice(tailoringCostKZT);
  if (elTitle) elTitle.innerText = `Индивидуальный комплект: ${voiceState.room}`;

  if (elPriceNote) {
    elPriceNote.innerText = voiceState.currency === 'rub' ? 'под ключ с доставкой по СНГ' : 'под ключ с пошивом в Астане';
  }

  // Update fallback interactive chips active states
  syncFallbackChipsUI();

  // Update WhatsApp Deep-Link
  updateWhatsAppLink(fabric, pleat, totalMeters, totalCostKZT, fabricCostKZT, tailoringCostKZT);
}

/**
 * Highlight corresponding active buttons in the fallback chips group
 */
function syncFallbackChipsUI() {
  // Room chips
  document.querySelectorAll('#roomChipsGroup .interactive-chip').forEach(btn => {
    const val = btn.dataset.val;
    btn.classList.toggle('active', val === voiceState.room || (val === 'Кабинет' && voiceState.room.includes('Кабинет')));
  });

  // Fabric chips
  document.querySelectorAll('#fabricChipsGroup .interactive-chip').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.val === voiceState.fabricKey);
  });

  // Dimension chips
  const dimStr = `${voiceState.width}x${voiceState.height}`;
  document.querySelectorAll('#dimensionChipsGroup .interactive-chip').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.val === dimStr);
  });

  // Pleat chips
  document.querySelectorAll('#pleatChipsGroup .interactive-chip').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.val === voiceState.pleatKey);
  });
}

/**
 * Generate customized WhatsApp Deep-Link
 */
function updateWhatsAppLink(fabric, pleat, totalMeters, totalKZT, fabricKZT, tailoringKZT) {
  const btnWa = document.getElementById('btnWhatsApp');
  if (!btnWa) return;

  const totalFormatted = formatVoicePrice(totalKZT);
  const fabricFormatted = formatVoicePrice(fabricKZT);
  const tailoringFormatted = formatVoicePrice(tailoringKZT);

  const phone = '77017775522'; // Official Maison Poisson concierge WhatsApp
  const message = `Здравствуйте, Maison Poisson!
Я рассчитал шторы через Voice AI ассистента на сайте:

🏠 *Помещение:* ${voiceState.room}
🧵 *Ткань:* ${fabric.name}
🌍 *Страна производства:* ${voiceState.origin}
📐 *Размеры окна:* ${voiceState.width.toFixed(2)} × ${voiceState.height.toFixed(2)} м ${voiceState.windows > 1 ? `(${voiceState.windows} окон)` : ''}
🪟 *Геометрия драпировки:* ${pleat.name}
✂️ *Расход ткани:* ${totalMeters.toFixed(1)} пог. м
💰 *Итоговая смета под ключ:* ${totalFormatted}
   • Ткань: ${fabricFormatted}
   • Премиум-пошив + австрийская лента Bandex: ${tailoringFormatted}
⏳ *Срок готовности в цехе:* 5-7 рабочих дней

Хочу посмотреть живые образцы ткани (${voiceState.origin}) и согласовать бесплатный выезд дизайнера-замерщика на объект в Астане!`;

  btnWa.href = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
}

/**
 * Setup Click listeners for Sample Prompts, Fallback Chips, Currency Switcher, and Reset
 */
function setupVoiceUIEvents() {
  // Mic Button
  const btnMic = document.getElementById('btnMic') || document.getElementById('micBtn') || document.getElementById('btnVoiceMic');
  if (btnMic) {
    btnMic.onclick = (e) => {
      e.preventDefault();
      toggleVoiceListening();
    };
  }

  // Quick Sample Prompt Chips
  document.querySelectorAll('.query-chip').forEach(chip => {
    chip.onclick = () => {
      const q = chip.dataset.query;
      if (q) {
        setTranscriptDisplay(q);
        processVoiceInput(q);
        if (navigator.vibrate) navigator.vibrate(20);
      }
    };
  });

  // Currency Switch Buttons
  const btnKzt = document.getElementById('btnCurKzt');
  const btnRub = document.getElementById('btnCurRub');

  if (btnKzt && btnRub) {
    btnKzt.onclick = () => {
      voiceState.currency = 'kzt';
      btnKzt.classList.add('active');
      btnRub.classList.remove('active');
      updateVoiceCalculationUI();
    };

    btnRub.onclick = () => {
      voiceState.currency = 'rub';
      btnRub.classList.add('active');
      btnKzt.classList.remove('active');
      updateVoiceCalculationUI();
    };
  }

  // Reset Button
  const btnReset = document.getElementById('btnReset');
  if (btnReset) {
    btnReset.onclick = () => {
      voiceState.room = 'Детская';
      voiceState.fabricKey = 'chenille';
      voiceState.origin = 'Бельгия';
      voiceState.width = 3.0;
      voiceState.height = 2.8;
      voiceState.windows = 1;
      voiceState.pleatKey = 'wave';
      setTranscriptDisplay('Нажмите микрофон и скажите: «Детская ткань sheeneel, производство Бельгия, окно 3 на 2.80»');
      updateVoiceCalculationUI();
    };
  }

  // Fallback Interactive Chips (1-tap selection)
  document.querySelectorAll('.interactive-chip').forEach(chip => {
    chip.onclick = () => {
      const type = chip.dataset.type;
      const val = chip.dataset.val;

      if (type === 'room') {
        voiceState.room = val;
        // Adjust default fabric/origin for room if not locked
        if (val === 'Кабинет') {
          voiceState.fabricKey = 'trevira';
          voiceState.origin = 'Франция';
        } else if (val === 'Гостиная') {
          voiceState.fabricKey = 'silk';
          voiceState.origin = 'Италия';
        } else if (val === 'Детская') {
          voiceState.fabricKey = 'chenille';
          voiceState.origin = 'Бельгия';
        }
      } else if (type === 'fabric') {
        voiceState.fabricKey = val;
        if (chip.dataset.origin) {
          voiceState.origin = chip.dataset.origin;
        } else if (FABRIC_CATALOG[val]) {
          voiceState.origin = FABRIC_CATALOG[val].origin;
        }
      } else if (type === 'dimension') {
        const parts = val.split('x');
        voiceState.width = parseFloat(parts[0]);
        voiceState.height = parseFloat(parts[1]);
      } else if (type === 'pleat') {
        voiceState.pleatKey = val;
      }

      setTranscriptDisplay(`${voiceState.room}, ${FABRIC_CATALOG[voiceState.fabricKey].name} (${voiceState.origin}), ${voiceState.width} на ${voiceState.height} м`);
      updateVoiceCalculationUI();
      if (navigator.vibrate) navigator.vibrate(15);
    };
  });
}

// Global hook for index.html floating button
window.startVoiceInput = toggleVoiceListening;
window.applySampleVoice = function(query) {
  setTranscriptDisplay(query);
  processVoiceInput(query);
};
window.VoiceAIEngine = {
  state: voiceState,
  parse: parseVoiceEntities,
  process: processVoiceInput,
  toggle: toggleVoiceListening,
  fabrics: FABRIC_CATALOG,
  pleats: PLEAT_CATALOG,
  rooms: ROOM_CATALOG
};

// ==========================================================================
// 5. INTERACTIVE BEFORE / AFTER SPLIT SLIDER
// ==========================================================================
(function initBeforeAfterSlider() {
  const container = document.getElementById('beforeAfterContainer');
  const afterLayer = document.getElementById('afterLayer');
  const handle = document.getElementById('splitHandle');
  if (!container || !afterLayer || !handle) return;

  let isDragging = false;

  function updatePosition(x) {
    const rect = container.getBoundingClientRect();
    let pos = (x - rect.left) / rect.width;
    pos = Math.max(0.05, Math.min(0.95, pos));
    const percent = pos * 100;
    afterLayer.style.clipPath = `polygon(0 0, ${percent}% 0, ${percent}% 100%, 0 100%)`;
    handle.style.left = `${percent}%`;
  }

  container.addEventListener('mousedown', (e) => {
    isDragging = true;
    updatePosition(e.clientX);
  });
  window.addEventListener('mousemove', (e) => {
    if (isDragging) updatePosition(e.clientX);
  });
  window.addEventListener('mouseup', () => isDragging = false);

  container.addEventListener('touchstart', (e) => {
    isDragging = true;
    updatePosition(e.touches[0].clientX);
  }, { passive: true });
  window.addEventListener('touchmove', (e) => {
    if (isDragging) updatePosition(e.touches[0].clientX);
  }, { passive: true });
  window.addEventListener('touchend', () => isDragging = false);
})();

// ==========================================================================
// 6. VIP SECRET PROPOSAL DOSSIER (PROJECT-70 / ASTANA-VILLA)
// ==========================================================================
const VIP_PROJECTS_DB = {
  'PROJECT-70': {
    code: 'PROJECT-70',
    title: 'Резиденция в пос. Саранда (480 м²)',
    client: 'Айдар и Динара',
    designer: 'Анастасия Белова (Ведущий декоратор)',
    rooms: [
      { name: 'Парадная гостиная (3 окна в пол)', fabric: 'Бельгийский шенилл Wind Pure #402', pleat: 'Волна 1:2.0', light: 'Мягкий рассеянный', sum: '1 480 000 ₸' },
      { name: 'Мастер-спальня', fabric: 'Итальянский бархат Dedar + 100% Blackout', pleat: 'Французская тройная', light: '100% Ночь', sum: '1 120 000 ₸' },
      { name: 'Детская сюита', fabric: 'Натуральный лён Casamance (Франция)', pleat: 'Римские шторы + портьеры', light: 'Комфорт', sum: '880 000 ₸' }
    ],
    somfyIncluded: true,
    totalCost: '3 480 000 ₸',
    status: 'Пошив в собственном цехе (Готовность 75%)',
    deliveryDate: '14 октября 2026 г.'
  }
};

function openSecretKP() {
  const codeInput = document.getElementById('secretCodeInput');
  let code = (codeInput?.value || '').trim().toUpperCase();
  if (!code) code = 'PROJECT-70';

  let project = VIP_PROJECTS_DB[code] || VIP_PROJECTS_DB['PROJECT-70'];

  // Fill modal
  document.getElementById('vipClientName').innerText = project.client;
  document.getElementById('vipPropertyTitle').innerText = project.title;
  document.getElementById('vipDesigner').innerText = project.designer;
  document.getElementById('vipTotalCost').innerText = project.totalCost;
  document.getElementById('vipDeliveryDate').innerText = project.deliveryDate;
  document.getElementById('vipStatusText').innerText = project.status;

  const modal = document.getElementById('secretKPDossierModal');
  if (modal) {
    modal.classList.remove('hidden');
    modal.classList.add('flex');
  }
}

function closeSecretKP() {
  const modal = document.getElementById('secretKPDossierModal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }
}

function switchDayNight(mode) {
  const renderImg = document.getElementById('vipRenderVisual');
  const btnDay = document.getElementById('btnLightDay');
  const btnEvening = document.getElementById('btnLightEvening');
  const btnNight = document.getElementById('btnLightNight');

  [btnDay, btnEvening, btnNight].forEach(b => b?.classList.remove('bg-brass', 'text-white'));

  if (mode === 'day') {
    btnDay?.classList.add('bg-brass', 'text-white');
    if (renderImg) renderImg.style.filter = 'brightness(1.1) contrast(1.02)';
  } else if (mode === 'evening') {
    btnEvening?.classList.add('bg-brass', 'text-white');
    if (renderImg) renderImg.style.filter = 'brightness(0.9) sepia(0.25) contrast(1.08)';
  } else {
    btnNight?.classList.add('bg-brass', 'text-white');
    if (renderImg) renderImg.style.filter = 'brightness(0.45) contrast(1.2)';
  }
}

function approveVipDossierWhatsApp() {
  const code = 'PROJECT-70';
  const text = `Здравствуйте, Maison Textile!
Мы изучили интерактивное КП по объекту ${code} (Вилла в пос. Саранда).
Смета 3 480 000 ₸ с электрокарнизами Somfy полностью согласована!
Готовы внести предоплату и запустить заказ в пошив. Пришлите, пожалуйста, договор!`;

  window.open(`https://wa.me/77010000000?text=${encodeURIComponent(text)}`, '_blank');
}

// ==========================================================================
// 7. B2B CORPORATE ESTIMATOR (VAT 12% + SOMFY)
// ==========================================================================
function updateB2BCalculator() {
  const openings = parseInt(document.getElementById('b2bOpeningsSlider')?.value || 12, 10);
  const systemType = document.getElementById('b2bSystemType')?.value || 'screen';
  const elOpeningsVal = document.getElementById('b2bOpeningsVal');
  const elTotal = document.getElementById('b2bTotalCost');
  const elVat = document.getElementById('b2bVatAmount');

  if (elOpeningsVal) elOpeningsVal.innerText = openings + ' проемов';

  let basePerOpening = 45000;
  if (systemType === 'blackout') basePerOpening = 52000;
  if (systemType === 'wood') basePerOpening = 68000;
  if (systemType === 'trevira') basePerOpening = 74000;

  const subtotal = openings * basePerOpening;
  const vat = Math.round(subtotal * 0.12);
  const total = subtotal + vat;

  if (elTotal) elTotal.innerText = total.toLocaleString('ru-RU') + ' ₸';
  if (elVat) elVat.innerText = 'В том числе НДС 12%: ' + vat.toLocaleString('ru-RU') + ' ₸';
}

function sendB2BToWhatsApp() {
  const openings = document.getElementById('b2bOpeningsSlider')?.value || 12;
  const system = document.getElementById('b2bSystemType')?.selectedOptions[0]?.text || 'Somfy Screen 5%';
  const total = document.getElementById('b2bTotalCost')?.innerText || '540 000 ₸';

  const text = `Здравствуйте! Запрос B2B спецификации для юридического лица:
Объект: Коммерческая недвижимость / Офис
Количество проемов: ${openings}
Система: ${system}
Ориентировочный бюджет: ${total} (с НДС 12%)

Просим подготовить официальное коммерческое предложение и проект договора за 2 часа.`;

  window.open(`https://wa.me/77010000000?text=${encodeURIComponent(text)}`, '_blank');
}

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  updateB2CCalculator();
  updateB2BCalculator();
  initVoiceAI();
});
