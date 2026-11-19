// Rend les planches HTML en PDF (et une image PNG par planche dans le dossier passé en argument).
const { chromium } = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '..');
const outDir = process.argv[2];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  await p.goto('file://' + root + '/planches-chapitre-1.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(500);
  await p.pdf({ path: root + '/planches-chapitre-1.pdf', width: '1600px', height: '900px', printBackground: true });
  if (outDir) {
    const secs = await p.$$('section.page');
    for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: `${outDir}/pl${i}.png` });
  }
  await b.close();
  console.log('ok');
})();
