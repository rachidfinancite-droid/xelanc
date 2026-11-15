// Rend les visuels en PNG 1080 x 1350. Usage : node src/render.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const src = __dirname;
const out = path.join(__dirname, '..');
const jobs = [
  ['v1-maitre.html', 'v1-maitre.png'],
  ['v2-certificat.html', 'v2-certificat.png'],
  ['v3-panier.html', 'v3-panier.png', 'Carte bancaire ou virement.'],
  ['v3-panier.html', 'v3-panier-mobile-money.png', 'Mobile Money (Orange, MTN, Moov, Wave), carte ou virement.'],
  ['v4-echeance.html', 'v4-echeance.png'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const [file, png, payment] of jobs) {
    let html = fs.readFileSync(path.join(src, file), 'utf8');
    if (payment) html = html.replace('PAYMENT_LINE', payment);
    const tmp = path.join(src, '_tmp.html');
    fs.writeFileSync(tmp, html);
    await page.goto('file://' + tmp, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const overflow = await page.evaluate(() => document.body.scrollHeight > 1350 || document.body.scrollWidth > 1080);
    await page.screenshot({ path: path.join(out, png) });
    fs.unlinkSync(tmp);
    console.log(png, overflow ? 'DEBORDE' : 'ok');
  }
  await browser.close();
})();
