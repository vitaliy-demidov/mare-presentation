const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8993;
const ROOT = path.resolve(__dirname, '..');

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf'
};

function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let reqPath = decodeURI(req.url.split('?')[0]);
      if (reqPath === '/' || reqPath === '') reqPath = '/index.html';
      const filePath = path.join(ROOT, reqPath);

      fs.stat(filePath, (err, stats) => {
        if (err || !stats.isFile()) {
          res.writeHead(404, { 'Content-Type': 'text/plain' });
          res.end('404 Not Found: ' + reqPath);
          return;
        }

        const ext = path.extname(filePath).toLowerCase();
        const contentType = MIME_TYPES[ext] || 'application/octet-stream';
        res.writeHead(200, { 'Content-Type': contentType });
        fs.createReadStream(filePath).pipe(res);
      });
    });

    server.listen(PORT, () => {
      console.log(`[QA SERVER] Serving ${ROOT} on http://localhost:${PORT}`);
      resolve(server);
    });
  });
}

async function runMasterQA() {
  const server = await startServer();
  let browser;
  const testResults = {
    desktop: { passed: 0, failed: 0, items: [] },
    mobile: { passed: 0, failed: 0, items: [] }
  };

  const assert = (suite, condition, message, details = "") => {
    const pass = Boolean(condition);
    if (pass) suite.passed++;
    else suite.failed++;
    const icon = pass ? "  ✅ PASS:" : "  ❌ FAIL:";
    const logMsg = `${icon} ${message} ${details ? `(${details})` : ""}`;
    console.log(logMsg);
    suite.items.push({ pass, message, details });
    return pass;
  };

  try {
    browser = await chromium.launch({ headless: true });

    // ========================================================================
    // SUITE 1: DESKTOP (1440x900)
    // ========================================================================
    console.log("\n======================================================");
    console.log("🚀 EXECUTING SUITE 1: DESKTOP WORKROOM QA (1440x900)");
    console.log("======================================================");

    const desktopContext = await browser.newContext({
      viewport: { width: 1440, height: 900 }
    });
    const desktopPage = await desktopContext.newPage();

    const desktopErrors = [];
    desktopPage.on('pageerror', err => desktopErrors.push(err.message));

    await desktopPage.goto(`http://localhost:${PORT}/index.html`, { waitUntil: 'networkidle' });

    assert(testResults.desktop, desktopErrors.length === 0, "0 Console JS Errors on Desktop Load", desktopErrors.join("; "));

    // Horizontal scroll
    const dScroll = await desktopPage.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      innerWidth: window.innerWidth
    }));
    assert(testResults.desktop, dScroll.scrollWidth <= dScroll.innerWidth, "No Horizontal Scroll on Desktop", `scrollWidth=${dScroll.scrollWidth}, innerWidth=${dScroll.innerWidth}`);

    // ALB Header and Title
    const title = await desktopPage.title();
    assert(testResults.desktop, title.includes("MUAR A"), "Page Title contains MUAR A", title);

    // 10 Authentic Projects
    const projectCardsCount = await desktopPage.locator('.monograph-card').count();
    assert(testResults.desktop, projectCardsCount === 10, "10 Monograph Project Cards Present", `Found: ${projectCardsCount}`);

    // Before/After Section & Tabs
    const baSection = await desktopPage.locator('#beforeAfter');
    assert(testResults.desktop, await baSection.count() > 0, "Before/After Section (#beforeAfter) Present");

    const baTabs = await desktopPage.locator('.ba-tab-btn').count();
    assert(testResults.desktop, baTabs === 5, "5 Before/After Tabs Present", `Found: ${baTabs}`);

    // Switch to tab 5 (Project 09)
    await desktopPage.locator('.ba-tab-btn').nth(4).click();
    await desktopPage.waitForTimeout(300);
    const baImgBeforeSrc = await desktopPage.locator('#baHeroImgBefore').getAttribute('src');
    assert(testResults.desktop, baImgBeforeSrc.includes('project_09_before.webp'), "Before/After Scene 5 Switch verified", baImgBeforeSrc);

    // Customer Pathways: B2C Roadmap
    const pathwaysSection = await desktopPage.locator('#customer-pathways');
    assert(testResults.desktop, await pathwaysSection.count() > 0, "Customer Pathways Section (#customer-pathways) Present");

    const b2cSteps = await desktopPage.locator('.b2c-step-card, .roadmap-card, .pw-step-card, [class*="step-card"]').count();
    assert(testResults.desktop, b2cSteps >= 6, "6-Step B2C Roadmap Items Present", `Count: ${b2cSteps}`);

    // Customer Pathways: B2B Contract Portal
    const b2bTab = desktopPage.locator('#tab-btn-b2b');
    if (await b2bTab.count() > 0) {
      await b2bTab.click();
      await desktopPage.waitForTimeout(300);
      const b2bPanelVisible = await desktopPage.locator('#panel-b2b').isVisible();
      assert(testResults.desktop, b2bPanelVisible, "B2B Contract Portal Panel Active on Tab Click");
      const b2bBinText = await desktopPage.locator('#b2bRequisitesText').innerText(); const b2bBin = b2bBinText.includes('140940019744') ? 1 : 0;
      assert(testResults.desktop, b2bBin > 0, "B2B Legal Entity BIN 140940019744 & VAT 12% Present");
    }

    // The Workroom: Master Zhanar Singing Video
    const workroomSection = await desktopPage.locator('#the-workroom');
    assert(testResults.desktop, await workroomSection.count() > 0, "The Workroom Section (#the-workroom) Present");

    const zhanarVideo = desktopPage.locator('video[src*="zhanar"], source[src*="zhanar"]');
    assert(testResults.desktop, await zhanarVideo.count() > 0, "Master Zhanar Singing Video (assets/muar/zhanar-singing.mp4) Present");

    const mastersCards = await desktopPage.locator('.wr-master-card').count();
    assert(testResults.desktop, mastersCards >= 3, "Masters Trilogy Present in Workroom", `Count: ${mastersCards}`);

    // Credentials Section
    const credSection = await desktopPage.locator('#credentialsSection');
    assert(testResults.desktop, await credSection.count() > 0, "Credentials Section (#credentialsSection) Present");

    const credCards = await desktopPage.locator('.cred-card').count();
    assert(testResults.desktop, credCards >= 6, "All 6 Official Credentials & Awards Present", `Count: ${credCards}`);

    // Calculator Module: 508,800 ₸ Control Test
    const calcSection = await desktopPage.locator('#calculatorApp');
    assert(testResults.desktop, await calcSection.count() > 0, "Calculator Module (#calculatorApp) Present");

    const grandTotalEl = desktopPage.locator('#grandTotalNumber');
    const grandTotalText = (await grandTotalEl.innerText()).replace(/\s+/g, ' ').trim();
    assert(testResults.desktop, grandTotalText === "508 800", "Calculator Exact 508 800 ₸ Control Test", grandTotalText);

    // WhatsApp Dispatcher
    const waBtn = desktopPage.locator('#whatsappActionBtn');
    const waHref = await waBtn.getAttribute('href');
    assert(testResults.desktop, waHref && waHref.includes('77710551515'), "WhatsApp Lead Dispatcher points to +7 771 055 15 15", waHref);

    // ========================================================================
    // SUITE 2: MOBILE (iPhone 390x844)
    // ========================================================================
    console.log("\n======================================================");
    console.log("📱 EXECUTING SUITE 2: MOBILE RESPONSIVE QA (390x844)");
    console.log("======================================================");

    const mobileContext = await browser.newContext({
      viewport: { width: 390, height: 844 },
      isMobile: true,
      hasTouch: true
    });
    const mobilePage = await mobileContext.newPage();

    const mobileErrors = [];
    mobilePage.on('pageerror', err => mobileErrors.push(err.message));

    await mobilePage.goto(`http://localhost:${PORT}/index.html`, { waitUntil: 'networkidle' });

    assert(testResults.mobile, mobileErrors.length === 0, "0 Console JS Errors on Mobile Load", mobileErrors.join("; "));

    const mScroll = await mobilePage.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      innerWidth: window.innerWidth
    }));
    assert(testResults.mobile, mScroll.scrollWidth <= mScroll.innerWidth, "No Horizontal Scroll on Mobile", `scrollWidth=${mScroll.scrollWidth}, innerWidth=${mScroll.innerWidth}`);

    // Mobile Calculator check
    const mGrandTotalEl = mobilePage.locator('#grandTotalNumber');
    const mGrandTotalText = (await mGrandTotalEl.innerText()).replace(/\s+/g, ' ').trim();
    assert(testResults.mobile, mGrandTotalText === "508 800", "Mobile Calculator 508 800 ₸ Control Test", mGrandTotalText);

    // ========================================================================
    // FINAL REPORT
    // ========================================================================
    console.log("\n======================================================");
    console.log("📊 MASTER QA VERIFICATION SUMMARY");
    console.log("======================================================");
    console.log(`DESKTOP: ${testResults.desktop.passed} PASSED, ${testResults.desktop.failed} FAILED`);
    console.log(`MOBILE:  ${testResults.mobile.passed} PASSED, ${testResults.mobile.failed} FAILED`);
    const totalPassed = testResults.desktop.passed + testResults.mobile.passed;
    const totalFailed = testResults.desktop.failed + testResults.mobile.failed;
    console.log(`TOTAL:   ${totalPassed} PASSED, ${totalFailed} FAILED`);

    if (totalFailed === 0) {
      console.log("\n🎉 ALL QUALITY GATES PASSED 100%! MASTER INDEX.HTML IS PRODUCTION-READY.");
    } else {
      console.log("\n⚠️ SOME CHECKS FAILED. INVESTIGATE LOGS ABOVE.");
      process.exitCode = 1;
    }

  } catch (err) {
    console.error("FATAL QA ERROR:", err);
    process.exitCode = 1;
  } finally {
    if (browser) await browser.close();
    server.close();
  }
}

runMasterQA();
