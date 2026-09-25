/**
 * Cloudflare Pages Serverless Function: /api/voice-lead
 * 
 * Handles voice recording uploads, smart textile entity structuring,
 * WhatsApp deep-link generation, and instant Telegram lead dispatching.
 */

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Requested-With',
      'Access-Control-Max-Age': '86400'
    }
  });
}

export async function onRequestPost(context) {
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json; charset=utf-8'
  };

  try {
    const contentType = context.request.headers.get('content-type') || '';
    let phone = '';
    let transcript = '';
    let structured = {};
    let audioBlob = null;
    let audioName = 'voice_lead.webm';
    let funnel = 'b2c';

    if (contentType.includes('multipart/form-data')) {
      const formData = await context.request.formData();
      phone = formData.get('phone') || '';
      transcript = formData.get('transcript') || '';
      funnel = formData.get('funnel') || 'b2c';
      
      const rawStructured = formData.get('structured');
      if (rawStructured) {
        try {
          structured = typeof rawStructured === 'string' ? JSON.parse(rawStructured) : rawStructured;
        } catch(e) {
          structured = {};
        }
      }

      const audioFile = formData.get('audio');
      if (audioFile && typeof audioFile.arrayBuffer === 'function') {
        audioBlob = audioFile;
        audioName = audioFile.name || 'voice_lead.webm';
      }
    } else {
      const json = await context.request.json().catch(() => ({}));
      phone = json.phone || '';
      transcript = json.transcript || '';
      structured = json.structured || {};
      funnel = json.funnel || 'b2c';
    }

    const leadId = 'VL-' + Date.now().toString(36).toUpperCase();
    const cleanPhone = String(phone).replace(/[^\d+]/g, '');

    // Telegram Bot notification
    const botToken = context.env.TELEGRAM_BOT_TOKEN || context.env.TG_BOT_TOKEN;
    const chatId = context.env.TELEGRAM_CHAT_ID || context.env.TG_CHAT_ID;

    let tgSent = false;
    let tgError = null;

    if (botToken && chatId) {
      try {
        const room = structured.room || 'Не указано';
        const fabric = structured.fabric || 'Подбор по каталогам';
        const dims = structured.dimensions || 'Стандартные';
        const budget = structured.budget || 'По смете ателье';
        const task = structured.task || 'Консультация декоратора';

        const caption = 
`🎙 <b>НОВАЯ ГОЛОСОВАЯ ЗАЯВКА · MUAR A</b>
━━━━━━━━━━━━━━━━━━━━
🆔 <b>Код:</b> <code>${leadId}</code>
👤 <b>Телефон:</b> <code>${cleanPhone || phone || 'Не указан'}</code>
📍 <b>Помещение:</b> ${room}
📐 <b>Окна:</b> ${dims}
🎨 <b>Ткань:</b> ${fabric}
💰 <b>Ориентир бюджета:</b> <b>${budget}</b>
🎯 <b>Задача:</b> ${task}
🗣 <b>Надиктовано:</b>
<i>«${transcript || 'Аудиосообщение без распознанного текста'}»</i>
━━━━━━━━━━━━━━━━━━━━
⚡ <b>SLA ответа:</b> 10 минут`;

        const waText = encodeURIComponent(
          `Здравствуйте! Я дежурный текстильный декоратор MUAR A (Астана).\n` +
          `Получили вашу голосовую заявку [${leadId}] по проекту (${room}, ${fabric}, ${dims}).\n` +
          `Готовы рассчитать точную смету и предложить выезд с каталогами.`
        );
        const waUrl = cleanPhone ? `https://wa.me/${cleanPhone.replace('+', '')}?text=${waText}` : 'https://wa.me/77710551515';

        const inlineKeyboard = {
          inline_keyboard: [
            [
              { text: '💬 Ответить в WhatsApp', url: waUrl },
              ...(cleanPhone ? [{ text: '📞 Позвонить', url: `tel:${cleanPhone}` }] : [])
            ]
          ]
        };

        // If audio file is attached, send via sendVoice
        if (audioBlob) {
          const tgForm = new FormData();
          tgForm.append('chat_id', chatId);
          tgForm.append('voice', audioBlob, audioName);
          tgForm.append('caption', caption);
          tgForm.append('parse_mode', 'HTML');
          tgForm.append('reply_markup', JSON.stringify(inlineKeyboard));

          const tgRes = await fetch(`https://api.telegram.org/bot${botToken}/sendVoice`, {
            method: 'POST',
            body: tgForm
          });
          const tgJson = await tgRes.json().catch(() => ({}));
          tgSent = tgJson.ok;
          if (!tgSent) {
            // fallback to sendMessage
            const msgRes = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                chat_id: chatId,
                text: caption,
                parse_mode: 'HTML',
                reply_markup: inlineKeyboard
              })
            });
            const msgJson = await msgRes.json().catch(() => ({}));
            tgSent = msgJson.ok;
          }
        } else {
          // Send text message
          const msgRes = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: chatId,
              text: caption,
              parse_mode: 'HTML',
              reply_markup: inlineKeyboard
            })
          });
          const msgJson = await msgRes.json().catch(() => ({}));
          tgSent = msgJson.ok;
        }
      } catch(err) {
        tgError = err.message;
      }
    }

    return new Response(JSON.stringify({
      success: true,
      leadId,
      phone: cleanPhone || phone,
      structured,
      transcript,
      telegram: {
        attempted: Boolean(botToken && chatId),
        sent: tgSent,
        error: tgError
      },
      timestamp: new Date().toISOString()
    }), {
      status: 200,
      headers: corsHeaders
    });

  } catch(err) {
    return new Response(JSON.stringify({
      success: false,
      error: err.message
    }), {
      status: 500,
      headers: corsHeaders
    });
  }
}
