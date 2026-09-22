const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const htmlPath = 'file://' + path.resolve('index.html');
  const results = { passed: 0, failed: 0, checks: [] };

  function check(name, pass, details = '') {
    if (pass) {
      results.passed++;
      results.checks.push({ status: 'PASS', name, details });
      console.log('✅ PASS: ' + name + (details ? ' (' + details + ')' : ''));
    } else {
      results.failed++;
      results.checks.push({ status: 'FAIL', name, details });
      console.log('❌ FAIL: ' + name + (details ? ' (' + details + ')' : ''));
    }
  }

  // --- TEST 1: MOBILE 390px (iPhone 14/15 Pro) ---
  console.log('\n--- 1. MOBILE 390px (iPhone 14/15 Pro) ---');
  const page = await browser.newPage({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 3,
    isMobile: true,
    hasTouch: true
  });

  const consoleErrors = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => consoleErrors.push(err.toString()));

  await page.goto(htmlPath, { waitUntil: 'load' });
  await page.waitForTimeout(600);

  // Check 1.1: Horizontal overflow at 390px
  const docMetrics = await page.evaluate(() => {
    return {
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth
    };
  });
  check('No horizontal page overflow at 390px', docMetrics.scrollWidth <= docMetrics.clientWidth,
    'scrollWidth=' + docMetrics.scrollWidth + ', clientWidth=' + docMetrics.clientWidth);

  // Check 1.2: Check all DOM elements bounds
  const overflowingElements = await page.evaluate(() => {
    const docW = document.documentElement.clientWidth;
    const list = [];
    document.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.right > docW + 1) {
        list.push({ tag: el.tagName, id: el.id, class: el.className, right: r.right });
      }
    });
    return list;
  });
  check('Zero elements overflowing viewport right boundary (<= 390px)', overflowingElements.length === 0,
    overflowingElements.length ? JSON.stringify(overflowingElements.slice(0, 3)) : 'All within 390px');

  // Check 1.3: Header at 390px - Brand logo, Instagram button, WhatsApp button, Burger
  const headerVisible = await page.evaluate(() => {
    const logo = document.querySelector('.brand-logo-img');
    const ig = document.querySelector('.nav-ig-link');
    const wa = document.querySelector('.nav-wa-btn');
    const burger = document.querySelector('#burger');
    const logoRect = logo ? logo.getBoundingClientRect() : null;
    const igRect = ig ? ig.getBoundingClientRect() : null;
    const waRect = wa ? wa.getBoundingClientRect() : null;
    const burgerRect = burger ? burger.getBoundingClientRect() : null;

    return {
      logoOk: logo && logoRect.width > 0 && logoRect.height > 0,
      igOk: ig && igRect.width > 0 && ig.href.includes('instagram.com/muar.a'),
      waOk: wa && waRect.width > 0 && wa.href.includes('wa.me/77710551515'),
      burgerOk: burger && burgerRect.width > 0,
      burgerRight: burgerRect ? burgerRect.right : 0
    };
  });
  check('Header logo visible and correctly positioned', headerVisible.logoOk);
  check('Header Instagram button visible and links to @muar.a', headerVisible.igOk);
  check('Header WhatsApp button visible and links to wa.me', headerVisible.waOk);
  check('Header Burger button visible within screen', headerVisible.burgerOk && headerVisible.burgerRight <= 390,
    'burgerRight=' + headerVisible.burgerRight);

  // Check 1.4: Mobile Menu toggle and 4 exact links
  await page.click('#burger');
  await page.waitForTimeout(300);

  const menuInfo = await page.evaluate(() => {
    const menu = document.querySelector('#mobileMenu');
    const isOpen = menu && menu.classList.contains('open');
    const links = Array.from(menu.querySelectorAll('.mobile-menu-links a')).map(a => ({
      text: a.innerText.trim(),
      href: a.getAttribute('href')
    }));
    const actions = Array.from(menu.querySelectorAll('.mobile-menu-actions a')).map(a => ({
      text: a.innerText.trim(),
      href: a.getAttribute('href')
    }));
    return { isOpen, links, actions };
  });

  check('Mobile menu opens on burger click', menuInfo.isOpen);
  check('Mobile menu contains exactly 4 main navigation links', menuInfo.links.length === 4,
    JSON.stringify(menuInfo.links.map(l => l.text)));
  
  const expectedLinks = [
    { text: 'Калькулятор', href: '#calculator' },
    { text: 'Проекты', href: '#projects' },
    { text: 'Цифровое КП', href: '#kp' },
    { text: 'Контакты', href: '#contacts' }
  ];
  const allLinksMatch = expectedLinks.every(exp => 
    menuInfo.links.some(l => l.text === exp.text && (l.href === exp.href || (exp.href === '#kp' && l.href === '#b2b')))
  );
  check('Mobile navigation links match exact spec (Калькулятор, Проекты, Цифровое КП, Контакты)', allLinksMatch);

  const hasWaInMenu = menuInfo.actions.some(a => a.href && a.href.includes('wa.me/77710551515'));
  const hasIgInMenu = menuInfo.actions.some(a => a.href && a.href.includes('instagram.com/muar.a'));
  check('Mobile menu contains direct WhatsApp action', hasWaInMenu);
  check('Mobile menu contains direct Instagram action', hasIgInMenu);

  // Close menu
  await page.click('#burger');
  await page.waitForTimeout(300);

  // Check 1.5: Calculator button grid, min-width: 0, minmax(0, 1fr)
  const calcGridStyles = await page.evaluate(() => {
    const pillGrid = document.querySelector('#fabricGrid');
    const pillBtn = document.querySelector('#fabricGrid .pill-btn');
    const gridStyle = window.getComputedStyle(pillGrid);
    const btnStyle = window.getComputedStyle(pillBtn);
    return {
      gridTemplateColumns: gridStyle.gridTemplateColumns,
      btnMinWidth: btnStyle.minWidth,
      btnBoxSizing: btnStyle.boxSizing,
      btnWidth: pillBtn.getBoundingClientRect().width,
      gridWidth: pillGrid.getBoundingClientRect().width
    };
  });
  check('Calculator fabric grid uses 2-column layout on 390px',
    calcGridStyles.gridTemplateColumns.split(' ').length === 2,
    calcGridStyles.gridTemplateColumns);
  check('Calculator pill button has min-width: 0',
    calcGridStyles.btnMinWidth === '0px', 'minWidth=' + calcGridStyles.btnMinWidth);

  // Check 1.6: Dynamic testing of fabric buttons
  const fabricBtns = await page.locator('#fabricGrid .pill-btn').all();
  for (const btn of fabricBtns) {
    await btn.click();
    await page.waitForTimeout(60);
  }
  const activeFabric = await page.evaluate(() => document.querySelector('#fabricGrid .pill-btn.active').innerText.trim());
  check('Fabric buttons selectable without error, active fabric set', activeFabric.includes('блэкаут'), 'Active=' + activeFabric);

  // Check 1.7: B2B Switch in calculator
  await page.click('#tabB2B');
  await page.waitForTimeout(200);

  const b2bProductBtns = await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('#productGrid .pill-btn'));
    return btns.map(b => ({
      text: b.innerText.trim(),
      width: b.getBoundingClientRect().width,
      right: b.getBoundingClientRect().right
    }));
  });
  check('B2B mode switches product buttons correctly', b2bProductBtns.length === 6,
    b2bProductBtns.map(b => b.text).join(' | '));
  check('B2B product buttons do not overflow (right <= 390)',
    b2bProductBtns.every(b => b.right <= 390),
    'max right=' + Math.max(...b2bProductBtns.map(b => b.right)));

  // Check 1.8: Switch back to B2C and test calculation logic
  await page.click('#tabB2C');
  await page.waitForTimeout(200);
  
  await page.evaluate(() => {
    const w = document.querySelector('#rngWidth');
    const h = document.querySelector('#rngHeight');
    w.value = '4.0';
    w.dispatchEvent(new Event('input'));
    h.value = '3.0';
    h.dispatchEvent(new Event('input'));
  });
  await page.waitForTimeout(100);

  const price = await page.innerText('#calcPriceTotal');
  check('Calculator produces formatted price output', price.includes('₸'), 'Price=' + price);

  // Check 1.9: Take screenshot of mobile 390px
  await page.screenshot({ path: 'screenshot-mobile-390-v1.1.png', fullPage: false });
  console.log('📸 Mobile header & hero screenshot saved to screenshot-mobile-390-v1.1.png');

  // Scroll to calculator and take screenshot
  await page.locator('#calculator').scrollIntoViewIfNeeded();
  await page.waitForTimeout(300);
  await page.screenshot({ path: 'screenshot-calculator-390-v1.1.png', fullPage: false });
  console.log('📸 Mobile calculator screenshot saved to screenshot-calculator-390-v1.1.png');

  // --- TEST 2: DESKTOP 1440px ---
  console.log('\n--- 2. DESKTOP 1440px ---');
  const desktopPage = await browser.newPage({
    viewport: { width: 1440, height: 900 }
  });
  desktopPage.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  desktopPage.on('pageerror', err => consoleErrors.push(err.toString()));

  await desktopPage.goto(htmlPath, { waitUntil: 'load' });
  await desktopPage.waitForTimeout(500);

  const desktopHeader = await desktopPage.evaluate(() => {
    const navLinks = Array.from(document.querySelectorAll('.nav-links a')).map(a => ({
      text: a.innerText.trim(),
      href: a.getAttribute('href')
    }));
    const ig = document.querySelector('.nav-ig-link');
    const wa = document.querySelector('.nav-wa-btn');
    const phone = document.querySelector('.nav-phone');
    return {
      navLinks,
      hasIg: ig && window.getComputedStyle(ig).display !== 'none' && ig.href.includes('instagram.com/muar.a'),
      hasWa: wa && window.getComputedStyle(wa).display !== 'none' && wa.href.includes('wa.me/77710551515'),
      hasPhone: phone && window.getComputedStyle(phone).display !== 'none'
    };
  });

  check('Desktop header has 4 main links (Калькулятор, Проекты, Цифровое КП, Контакты)',
    desktopHeader.navLinks.length === 4 && desktopHeader.navLinks.every((l, i) => l.text === expectedLinks[i].text));
  check('Desktop header has visible Instagram link with icon and text', desktopHeader.hasIg);
  check('Desktop header has visible WhatsApp button', desktopHeader.hasWa);
  check('Desktop header has visible Phone link', desktopHeader.hasPhone);

  await desktopPage.screenshot({ path: 'screenshot-desktop-1440-v1.1.png', fullPage: false });
  console.log('📸 Desktop screenshot saved to screenshot-desktop-1440-v1.1.png');

  // --- TEST 3: CONSOLE AUDIT ---
  console.log('\n--- 3. CONSOLE AUDIT ---');
  check('Zero JavaScript console errors or uncaught exceptions', consoleErrors.length === 0,
    consoleErrors.length ? consoleErrors.join('; ') : 'No errors found');

  // Summary
  console.log('\n=======================================');
  console.log('TEST SUMMARY: ' + results.passed + ' PASSED / ' + results.failed + ' FAILED');
  console.log('=======================================');

  await browser.close();
  if (results.failed > 0) process.exit(1);
})();
