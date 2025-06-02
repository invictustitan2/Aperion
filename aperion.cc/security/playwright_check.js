const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  let errorExcerpt = "";

  try {
    const response = await page.goto("http://aperion.cc", { waitUntil: "load", timeout: 15000 });
    console.log(`🌐 Status: ${response.status()}`);
    if (response.status() !== 200) {
      console.log("❌ Error Excerpt:");
      const excerpt = await page.content();
      errorExcerpt = excerpt.substring(0, 500).replace(/\s+/g, " ");
      console.log(errorExcerpt);
    } else {
      console.log("✅ No error detected.");
    }
  } catch (error) {
    console.log("❌ Exception during page load:", error.message);
    errorExcerpt = error.message;
  }

  await browser.close();

  // Save excerpt for Verity summary
  const fs = require("fs");
  fs.writeFileSync("/var/www/aperion.cc/security/playwright_error_excerpt.log", errorExcerpt || "No error detected.");
})();
