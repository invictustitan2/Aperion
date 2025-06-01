const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const url = 'http://127.0.0.1:5002'; // Change to your site’s main URL
  await page.goto(url);

  console.log(`🔍 Checking all links on: ${url}`);

  const links = await page.$$eval('a', as => as.map(a => a.href));
  let brokenLinks = 0;

  for (const link of links) {
    const res = await page.goto(link, { waitUntil: 'domcontentloaded' });
    const status = res.status();
    if (status >= 400) {
      console.log(`❌ Broken link: ${link} (status: ${status})`);
      brokenLinks++;
    } else {
      console.log(`✅ OK: ${link} (status: ${status})`);
    }
    await page.goBack(); // Go back to the index page to keep checking others
  }

  console.log(`\n🟩 Link check complete! Broken links: ${brokenLinks}`);
  await browser.close();
})();
