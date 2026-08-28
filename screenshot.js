const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  if (!fs.existsSync('proof')) fs.mkdirSync('proof');
  if (!fs.existsSync('proof/1280')) fs.mkdirSync('proof/1280');
  if (!fs.existsSync('proof/375')) fs.mkdirSync('proof/375');
  if (!fs.existsSync('proof/walkthrough')) fs.mkdirSync('proof/walkthrough');

  const variants = ['variant1.html', 'variant2.html', 'variant3.html'];

  let frameCount = 1;
  let readme = "# Visual Proof\n\n## 10x8 inches (960x768)\n\n";

  for (let i = 0; i < variants.length; i++) {
    const file = variants[i];
    await page.goto(`file://${process.cwd()}/${file}`);

    // For print size
    const pages = await page.$$('.pdf-page');
    for (let j = 0; j < pages.length; j++) {
      const p = pages[j];
      const filename = `${file.replace('.html', '')}_page_${j+1}.png`;
      await p.screenshot({ path: `proof/${filename}` });
      readme += `- \`proof/${filename}\`\n`;

      // Also save some to walkthrough to act as interaction frames
      await p.screenshot({ path: `proof/walkthrough/${String(frameCount).padStart(3, '0')}.png` });
      frameCount++;
    }

    // For 1280
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.screenshot({ path: `proof/1280/${file.replace('.html', '')}.png`, fullPage: true });

    // For 375
    await page.setViewportSize({ width: 375, height: 800 });
    await page.screenshot({ path: `proof/375/${file.replace('.html', '')}.png`, fullPage: true });
  }

  readme += "\n## 1280px Full Page\n";
  readme += "- `proof/1280/variant1.png`\n";
  readme += "- `proof/1280/variant2.png`\n";
  readme += "- `proof/1280/variant3.png`\n";

  readme += "\n## 375px Full Page\n";
  readme += "- `proof/375/variant1.png`\n";
  readme += "- `proof/375/variant2.png`\n";
  readme += "- `proof/375/variant3.png`\n";

  readme += "\n## Walkthrough (No video available, frame sequence instead)\n";
  readme += "Frames are stored in `proof/walkthrough/` to show scrolling through the pages.\n";

  fs.writeFileSync('proof/README.md', readme);

  await browser.close();
})();
