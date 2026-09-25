/**
 * MUAR A Atelier - Standalone Node.js Voice & Lead Server
 * 
 * Runs independently on any server or VPS (Node.js 18+).
 * Handles voice recordings, entity structuring, Telegram bot forwarding.
 * 
 * Usage:
 *   node voice-server.js
 *   or with env:
 *   PORT=3001 TELEGRAM_BOT_TOKEN="xxx" TELEGRAM_CHAT_ID="yyy" node voice-server.js
 */

const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');

const PORT = parseInt(process.env.PORT || '3001', 10);
const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || process.env.TG_BOT_TOKEN || '';
const CHAT_ID = process.env.TELEGRAM_CHAT_ID || process.env.TG_CHAT_ID || '';

function sendTelegramMessage(caption, inlineKeyboard, callback) {
  if (!BOT_TOKEN || !CHAT_ID) {
    if (callback) callback(null, { skipped: true, reason: 'No tokens configured' });
    return;
  }

  const payload = JSON.stringify({
    chat_id: CHAT_ID,
    text: caption,
    parse_mode: 'HTML',
    reply_markup: inlineKeyboard
  });

  const req = https.request({
    hostname: 'api.telegram.org',
    path: `/bot${BOT_TOKEN}/sendMessage`,
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(payload)
    }
  }, (res) => {
    let body = '';
    res.on('data', chunk => { body += chunk; });
    res.on('end', () => {
      try {
        const json = JSON.parse(body);
        if (callback) callback(null, json);
      } catch(e) {
        if (callback) callback(e);
      }
    });
  });

  req.on('error', err => {
    if (callback) callback(err);
  });

  req.write(payload);
  req.end();
}

const server = http.createServer((req, res) => {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const url = new URL(req.url, `http://${req.headers.host}`);

  if (url.pathname === '/api/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', server: 'muar-a-voice', timestamp: new Date().toISOString() }));
    return;
  }

  if (url.pathname === '/api/voice-lead' && req.method === 'POST') {
    let rawBody = [];
    req.on('data', chunk => { rawBody.push(chunk); });
    req.on('end', () => {
      const buffer = Buffer.concat(rawBody);
      const contentType = req.headers['content-type'] || '';
      let phone = '', transcript = '', structured = {};

      if (contentType.includes('application/json')) {
        try {
          const json = JSON.parse(buffer.toString('utf8'));
          phone = json.phone || '';
          transcript = json.transcript || '';
          structured = json.structured || {};
        } catch(e){}
      } else {
        // Quick multipart boundary parsing
        const str = buffer.toString('utf8');
        const phoneMatch = str.match(/name="phone"\r\n\r\n([^\r\n]+)/);
        if (phoneMatch) phone = phoneMatch[1].trim();
        const transMatch = str.match(/name="transcript"\r\n\r\n([^\r\n]+)/);
        if (transMatch) transcript = transMatch[1].trim();
        const structMatch = str.match(/name="structured"\r\n\r\n([^\r\n]+)/);
        if (structMatch) {
          try { structured = JSON.parse(structMatch[1]); } catch(e){}
        }
      }

      const leadId = 'VL-' + Date.now().toString(36).toUpperCase();
      const cleanPhone = String(phone).replace(/[^\d+]/g, '');

      // Log lead locally
      const leadRecord = {
        leadId,
        phone: cleanPhone || phone,
        transcript,
        structured,
        receivedAt: new Date().toISOString()
      };
      console.log('🎙 [VOICE LEAD RECEIVED]:', JSON.stringify(leadRecord, null, 2));

      try {
        fs.appendFileSync(path.join(__dirname, 'leads.jsonl'), JSON.stringify(leadRecord) + '\n');
      } catch(e){}

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
<i>«${transcript || 'Аудиосообщение'}»</i>
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

      sendTelegramMessage(caption, inlineKeyboard, (err, tgRes) => {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({
          success: true,
          leadId,
          phone: cleanPhone || phone,
          structured,
          telegram: tgRes || { error: err ? err.message : null },
          timestamp: new Date().toISOString()
        }));
      });
    });
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Not found' }));
});

server.listen(PORT, () => {
  console.log(`✨ MUAR A Voice & Lead Server listening on http://localhost:${PORT}`);
});
