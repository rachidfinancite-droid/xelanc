// Rend les visuels en PNG 1080 x 1350. Usage : node src/render.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const src = __dirname;
const out = path.join(__dirname, '..');
const jobs = [
  ['v1-maitre.html', 'v1-maitre.png'],
  ['v2-valeur.html', 'v2-valeur.png'],
  ['v3-panier.html', 'v3-panier.png', 'Carte bancaire ou virement.'],
  ['v3-panier.html', 'v3-panier-mobile-money.png', 'Mobile Money (Orange, MTN, Moov, Wave), carte ou virement.'],
  ['v4-echeance.html', 'v4-echeance.png'],
  ...['or', 'emeraude', 'violet', 'corail', 'argent'].map(t => ['v1-maitre.html', `v1-maitre-${t}.png`, null, `t-${t}`]),
  ...['blanc', 'gris', 'anthracite', 'ivoire', 'bleu-vif'].map(t => ['v1-maitre.html', `v1-fond-${t}.png`, null, `bg b-${t}`]),
  ['v1-maitre.html', 'v1-selection-ivoire.png', null, 'bg b-ivoire framed'],
];

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (const [file, png, payment, theme] of jobs) {
    let html = fs.readFileSync(path.join(src, file), 'utf8');
    if (payment) html = html.replace('PAYMENT_LINE', payment);
    if (theme) html = html.replace('<body class="', `<body class="${theme} `);
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
