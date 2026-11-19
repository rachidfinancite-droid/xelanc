const { chromium } = require('playwright');
const out = process.argv[2], FPS = 25;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file:///home/user/xelanc/outputs/video-bootcamp-atw/index.html?render');
  await p.evaluate(() => document.fonts.ready);
  const N = Math.round(await p.evaluate(() => window.TOTAL) * FPS);
  for (let i = 0; i < N; i++) {
    await p.evaluate(t => window.render(t), i / FPS);
    await p.screenshot({ path: `${out}/f${String(i).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    if (i % 500 === 0) console.log(i, '/', N);
  }
  console.log('done', N);
  await b.close();
})();
