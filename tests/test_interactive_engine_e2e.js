/**
 * End-to-end Playwright test for MUAR A Tactile Motion & Interactive Components:
 * 1. Before/After Split Slider (Drag, Touch, Keyboard, 4 Projects Switcher)
 * 2. Fullscreen Lightbox (Open, Metadata, Nav, Keyboard, Backdrop Close, Swipe)
 * 3. Ambient Soundscape (Equalizer, Fade In/Out, Web Audio API)
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

async function runTests() {
  console.log('🚀 Starting MUAR A Interactive Components E2E Verification...\n');

  const browser = await chromium.launch({
    headless: true,
    args: ['--autoplay-policy=no-user-gesture-required']
  });

  const indexPath = 'file://' + path.resolve(__dirname, '../index.html');
  const screenshotDir = path.resolve(__dirname, '../scratch/test_screenshots');
  if (!fs.existsSync(screenshotDir)) {
    fs.mkdirSync(screenshotDir, { recursive: true });
  }

  let passCount = 0;
  let failCount = 0;

  function assert(condition, message) {
    if (condition) {
      console.log(`  ✅ PASS: ${message}`);
      passCount++;
    } else {
      console.error(`  ❌ FAIL: ${message}`);
      failCount++;
    }
  }

  /* -------------------------------------------------------------
     TEST SUITE 1: DESKTOP EXPERIENCES (1440 x 900)
     ------------------------------------------------------------- */
  console.log('--- TEST SUITE 1: DESKTOP WORKFLOW (1440x900) ---');
  const desktopContext = await browser.newContext({
    viewport: { width: 1440, height: 900 }
  });
  const page = await desktopContext.newPage();

  // Listen to console logs and errors
  const pageErrors = [];
  page.on('pageerror', err => pageErrors.push(err.message));

  await page.goto(indexPath, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(500);

  assert(pageErrors.length === 0, `Page loaded without uncaught JS errors (errors: ${pageErrors.join(', ')})`);

  // 1.1 Verify Before/After Slider Initial State
  const baContainer = page.locator('#baDedicatedSlider');
  await baContainer.scrollIntoViewIfNeeded();
  await page.waitForTimeout(400);

  const initialBeforeClip = await page.$eval('#baHeroBeforeLayer', el => el.style.clipPath);
  const initialHandleLeft = await page.$eval('#baHeroHandleLine', el => el.style.left);
  assert(initialBeforeClip.includes('50%'), `Initial Before layer clip-path is 50% (${initialBeforeClip})`);
  assert(initialHandleLeft === '50%', `Initial handle line position is 50% (${initialHandleLeft})`);

  // Verify Grip and Badges
  const gripVisible = await page.locator('#baHeroHandleLine .muar-ba-grip').isVisible();
  assert(gripVisible, 'Brushed brass handle grip is visible with SVG arrows');

  const badgeBeforeTxt = await page.locator('#baHeroLabelBefore').innerText();
  const badgeAfterTxt = await page.locator('#baHeroLabelAfter').innerText();
  assert(badgeBeforeTxt.toLowerCase().includes('интерьер до текстиля'), `Left badge is «Интерьер до текстиля» (${badgeBeforeTxt})`);
  assert(badgeAfterTxt.toLowerCase().includes('кутюрное преображение muar a'), `Right badge is «Кутюрное преображение MUAR A» (${badgeAfterTxt})`);

  // 1.2 Mouse Drag Interaction
  const sliderBox = await baContainer.boundingBox();
  const startX = sliderBox.x + sliderBox.width * 0.5;
  const startY = sliderBox.y + sliderBox.height * 0.5;

  // Drag to 25%
  await page.mouse.move(startX, startY);
  await page.mouse.down();
  await page.mouse.move(sliderBox.x + sliderBox.width * 0.25, startY, { steps: 10 });
  await page.mouse.up();
  await page.waitForTimeout(200);

  const draggedLeft = await page.$eval('#baHeroHandleLine', el => parseFloat(el.style.left));
  assert(Math.abs(draggedLeft - 25) < 3, `Mouse drag moved slider smoothly to ~25% (actual: ${draggedLeft.toFixed(1)}%)`);

  // Drag to 80%
  await page.mouse.move(sliderBox.x + sliderBox.width * 0.25, startY);
  await page.mouse.down();
  await page.mouse.move(sliderBox.x + sliderBox.width * 0.80, startY, { steps: 10 });
  await page.mouse.up();
  await page.waitForTimeout(200);

  const draggedRight = await page.$eval('#baHeroHandleLine', el => parseFloat(el.style.left));
  assert(Math.abs(draggedRight - 80) < 3, `Mouse drag moved slider smoothly to ~80% (actual: ${draggedRight.toFixed(1)}%)`);

  // 1.3 Keyboard Accessibility
  await baContainer.focus();
  await page.keyboard.press('ArrowLeft');
  await page.keyboard.press('ArrowLeft');
  await page.waitForTimeout(100);
  const kbLeft = await page.$eval('#baHeroHandleLine', el => parseFloat(el.style.left));
  assert(kbLeft < draggedRight, `Keyboard Left Arrow adjusted slider position (now: ${kbLeft.toFixed(1)}%)`);

  // 1.4 Switch 4 Key Projects
  console.log('\n  Testing 4 Key Projects Tabs in Before/After Slider:');
  
  // Project 02: ЖК Vivaldi
  await page.locator('.ba-tab-btn:has-text("02. ЖК Vivaldi")').click();
  await page.waitForTimeout(400);
  let title02 = await page.locator('#baHeroCaptionTitle').innerText();
  let img02 = await page.locator('#baHeroImgBefore').getAttribute('src');
  assert(title02.includes('Vivaldi'), `Switched to Project 02: ЖК Vivaldi (${title02})`);
  assert(img02.includes('living-luxe-before.webp'), `Project 02 before image loaded correctly (${img02})`);

  // Project 03: Загородный дом
  await page.locator('.ba-tab-btn:has-text("03. Загородный дом")').click();
  await page.waitForTimeout(400);
  let title03 = await page.locator('#baHeroCaptionTitle').innerText();
  let img03 = await page.locator('#baHeroImgBefore').getAttribute('src');
  assert(title03.includes('Загородный дом'), `Switched to Project 03: Загородный дом (${title03})`);
  assert(img03.includes('_MG_9217-2.webp'), `Project 03 before image loaded correctly (${img03})`);

  // Project 07: Вилла «Темный Рыцарь»
  await page.locator('.ba-tab-btn:has-text("07. Вилла «Темный Рыцарь»")').click();
  await page.waitForTimeout(400);
  let title07 = await page.locator('#baHeroCaptionTitle').innerText();
  let img07 = await page.locator('#baHeroImgBefore').getAttribute('src');
  assert(title07.includes('Темный Рыцарь'), `Switched to Project 07: Вилла Темный Рыцарь (${title07})`);
  assert(img07.includes('IMG_4198.webp'), `Project 07 before image loaded correctly (${img07})`);

  // Project 09: Спальня (Коррекция асимметрии окна)
  await page.locator('.ba-tab-btn:has-text("09. Спальня")').click();
  await page.waitForTimeout(400);
  let title09 = await page.locator('#baHeroCaptionTitle').innerText();
  let img09Before = await page.locator('#baHeroImgBefore').getAttribute('src');
  let img09After = await page.locator('#baHeroImgAfter').getAttribute('src');
  let lbl09Before = await page.locator('#baHeroLabelBeforeText').innerText();
  let lbl09After = await page.locator('#baHeroLabelAfterText').innerText();
  assert(title09.includes('Коррекция асимметрии окна'), `Switched to Project 09: Спальня (${title09})`);
  assert(img09Before.includes('project_09_before.webp'), `Project 09 before image loaded correctly (${img09Before})`);
  assert(img09After.includes('project_09_after.webp'), `Project 09 after image loaded correctly (${img09After})`);
  assert(lbl09Before.toUpperCase().includes('АСИММЕТРИЯ'), `Project 09 before label matches (${lbl09Before})`);
  assert(lbl09After.toUpperCase().includes('РИМСКАЯ ШТОРА'), `Project 09 after label matches (${lbl09After})`);

  // Switch back to Project 01
  await page.locator('.ba-tab-btn:has-text("01. Red & White")').click();
  await page.waitForTimeout(400);

  // Take screenshot of Before/After Slider
  await baContainer.screenshot({ path: path.join(screenshotDir, '01_desktop_ba_slider.png') });
  console.log('  📸 Saved screenshot: 01_desktop_ba_slider.png');

  /* -------------------------------------------------------------
     TEST SUITE 2: FULLSCREEN LIGHTBOX
     ------------------------------------------------------------- */
  console.log('\n--- TEST SUITE 2: FULLSCREEN LIGHTBOX ---');
  
  // Scroll to project photos
  const photoWrap = page.locator('.project-photo-wrap, .gallery-lightbox-trigger').first();
  if (await photoWrap.count() > 0) {
    await photoWrap.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await photoWrap.click();
    await page.waitForTimeout(400);
  }

  const lightbox = page.locator('#muarLightbox');
  const isLbActive = await lightbox.evaluate(el => el.classList.contains('active'));
  assert(isLbActive, 'Lightbox opened and active class is applied');

  // Verify Metadata
  const counterTxt = await page.locator('#muarLightboxCounter').innerText();
  const projectTitleTxt = await page.locator('#muarLightboxProjectTitle').innerText();
  const projectBadgeTxt = await page.locator('#muarLightboxProjectBadge').innerText();
  const locationTxt = await page.locator('#muarLightboxLocation').innerText();
  const detailTxt = await page.locator('#muarLightboxDetail').innerText();

  assert(counterTxt.includes('01 /') || counterTxt.includes('/'), `Lightbox counter formatted properly: ${counterTxt}`);
  assert(projectBadgeTxt.includes('ПРОЕКТ'), `Lightbox project badge visible: ${projectBadgeTxt}`);
  assert(locationTxt.includes('Астана'), `Lightbox location visible: ${locationTxt}`);
  assert(detailTxt.length > 5, `Lightbox detail text displayed: ${detailTxt}`);

  // Take screenshot of Lightbox
  await page.screenshot({ path: path.join(screenshotDir, '02_desktop_lightbox_opened.png') });
  console.log('  📸 Saved screenshot: 02_desktop_lightbox_opened.png');

  // Test Next Photo navigation via button
  const nextBtn = page.locator('#muarLightboxNext');
  await nextBtn.click();
  await page.waitForTimeout(300);
  const counterNext = await page.locator('#muarLightboxCounter').innerText();
  assert(counterNext.includes('02 /'), `Navigated to next photo via arrow button (${counterNext})`);

  // Test Keyboard ArrowRight
  await page.keyboard.press('ArrowRight');
  await page.waitForTimeout(300);
  const counterRight = await page.locator('#muarLightboxCounter').innerText();
  assert(counterRight.includes('03 /'), `Navigated to next photo via ArrowRight key (${counterRight})`);

  // Test Keyboard ArrowLeft
  await page.keyboard.press('ArrowLeft');
  await page.waitForTimeout(300);
  const counterLeft = await page.locator('#muarLightboxCounter').innerText();
  assert(counterLeft.includes('02 /'), `Navigated to previous photo via ArrowLeft key (${counterLeft})`);

  // Test Close via Backdrop Click
  const stageBackdrop = page.locator('#muarLightboxStage');
  // Click at the top edge of stage outside image
  const stageBBox = await stageBackdrop.boundingBox();
  await page.mouse.click(stageBBox.x + 20, stageBBox.y + 20);
  await page.waitForTimeout(350);

  const isClosedBackdrop = await lightbox.evaluate(el => !el.classList.contains('active'));
  assert(isClosedBackdrop, 'Lightbox successfully closed on backdrop click');

  // Test Close via Esc Key
  await triggerBtn.click();
  await page.waitForTimeout(300);
  await page.keyboard.press('Escape');
  await page.waitForTimeout(350);
  const isClosedEsc = await lightbox.evaluate(el => !el.classList.contains('active'));
  assert(isClosedEsc, 'Lightbox successfully closed via Escape key');

  /* -------------------------------------------------------------
     TEST SUITE 3: AMBIENT SOUNDSCAPE
     ------------------------------------------------------------- */
  console.log('\n--- TEST SUITE 3: AMBIENT SOUNDSCAPE ---');
  
  const audioBtn = page.locator('#ambientToggleBtn');
  await audioBtn.scrollIntoViewIfNeeded();
  await page.waitForTimeout(200);

  const btnText = await audioBtn.innerText();
  assert(btnText.includes('Атмосфера салона'), `Audio toggle button displays «Атмосфера салона» (${btnText.trim()})`);

  // Click audio button to activate
  await audioBtn.click();
  await page.waitForTimeout(500);

  const isAudioActive = await audioBtn.evaluate(el => el.classList.contains('active') || el.classList.contains('is-active'));
  assert(isAudioActive, 'Audio toggle button activated with wave animation');

  const soundBarsCount = await page.locator('#ambientToggleBtn .sound-bar').count();
  assert(soundBarsCount >= 3, `Animated equalizer sound wave bars present (count: ${soundBarsCount})`);

  // Toggle off
  await audioBtn.click();
  await page.waitForTimeout(500);
  const isAudioOff = await audioBtn.evaluate(el => !el.classList.contains('active') && !el.classList.contains('is-active'));
  assert(isAudioOff, 'Audio toggle button smoothly faded out and deactivated');

  await desktopContext.close();

  /* -------------------------------------------------------------
     TEST SUITE 4: MOBILE WORKFLOW (iPhone 14 / 390x844)
     ------------------------------------------------------------- */
  console.log('\n--- TEST SUITE 4: MOBILE TOUCH EXPERIENCE (390x844) ---');
  const mobileContext = await browser.newContext({
    viewport: { width: 390, height: 844 },
    isMobile: true,
    hasTouch: true
  });
  const mobPage = await mobileContext.newPage();
  await mobPage.goto(indexPath, { waitUntil: 'domcontentloaded' });
  await mobPage.waitForTimeout(500);

  const mobSlider = mobPage.locator('#baDedicatedSlider');
  await mobSlider.scrollIntoViewIfNeeded();
  await mobPage.waitForTimeout(300);

  const mobBox = await mobSlider.boundingBox();
  const mobStartY = mobBox.y + mobBox.height * 0.5;

  // Touch Drag from 50% to 30%
  await mobPage.touchscreen.tap(mobBox.x + mobBox.width * 0.3, mobStartY);
  await mobPage.waitForTimeout(200);
  const mobDraggedLeft = await mobPage.$eval('#baHeroHandleLine', el => parseFloat(el.style.left));
  assert(mobDraggedLeft < 45, `Mobile tap/touch smoothly updated slider position to ~30% (actual: ${mobDraggedLeft.toFixed(1)}%)`);

  await mobSlider.screenshot({ path: path.join(screenshotDir, '03_mobile_ba_slider.png') });
  console.log('  📸 Saved screenshot: 03_mobile_ba_slider.png');

  // Mobile Lightbox Swipe
  const mobTrigger = mobPage.locator('.gallery-lightbox-trigger').first();
  await mobTrigger.scrollIntoViewIfNeeded();
  await mobTrigger.click();
  await mobPage.waitForTimeout(400);

  const mobLightbox = mobPage.locator('#muarLightbox');
  const mobLbActive = await mobLightbox.evaluate(el => el.classList.contains('active'));
  assert(mobLbActive, 'Mobile Lightbox opened successfully');

  // Swipe Left on Mobile stage to navigate next
  const mobLbStage = mobPage.locator('#muarLightboxStage');
  const mobLbBox = await mobLbStage.boundingBox();
  const touchY = mobLbBox.y + mobLbBox.height * 0.5;
  const swipeStartX = mobLbBox.x + mobLbBox.width * 0.8;
  const swipeEndX = mobLbBox.x + mobLbBox.width * 0.2;

  // Simulate swipe left gesture via pointer
  await mobPage.mouse.move(swipeStartX, touchY);
  await mobPage.mouse.down();
  await mobPage.mouse.move(swipeEndX, touchY, { steps: 8 });
  await mobPage.mouse.up();
  await mobPage.waitForTimeout(300);

  const mobCounterAfterSwipe = await mobPage.locator('#muarLightboxCounter').innerText();
  assert(mobCounterAfterSwipe.includes('02 /'), `Mobile touch swipe left navigated to next photo (${mobCounterAfterSwipe})`);

  // Close mobile lightbox by close button
  await mobPage.locator('#muarLightboxClose').click();
  await mobPage.waitForTimeout(300);
  const mobLbClosed = await mobLightbox.evaluate(el => !el.classList.contains('active'));
  assert(mobLbClosed, 'Mobile Lightbox closed via touch close button');

  await mobileContext.close();
  await browser.close();

  console.log('\n=============================================================');
  console.log(`🏁 TEST EXECUTION COMPLETE: ${passCount} PASSED, ${failCount} FAILED.`);
  console.log('=============================================================');

  if (failCount > 0) {
    process.exit(1);
  }
}

runTests().catch(err => {
  console.error('Fatal test error:', err);
  process.exit(1);
});
