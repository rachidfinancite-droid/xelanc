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
  ['v1-maitre.html', 'v1-gris-grand-logo.png', null, 'bg b-gris framed biglogo'],
  ['v1-maitre.html', 'v1-blanc-grand-logo.png', null, 'bg b-blanc framed biglogo'],
  ['v1-box.html', 'v1-box-gris.png', null, 'bg b-gris framed box'],
  ['v1-box.html', 'v1-box-blanc.png', null, 'bg b-blanc framed box'],
  ['v1-inscription.html', 'v1-inscription-gris.png', null, 'bg b-gris framed box'],
  ['v1-inscription.html', 'v1-inscription-blanc.png', null, 'bg b-blanc framed box'],
  ['v1-tout.html', 'v1-tout-gris.png', null, 'bg b-gris framed box tout'],
  ['v1-tout.html', 'v1-tout-blanc.png', null, 'bg b-blanc framed box tout'],
  ['v1-tout-150.html', 'v1-tout-150-gris.png', null, 'bg b-gris framed box tout'],
  ['v1-tout-150.html', 'v1-tout-150-blanc.png', null, 'bg b-blanc framed box tout'],
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
    // Ajuste chaque ligne .fit à la largeur commune du bloc (--W), et le bloc de chiffres par zoom.
    await page.evaluate(() => {
      const W = parseFloat(getComputedStyle(document.body).getPropertyValue('--W'));
      if (!W) return;
      document.querySelectorAll('.fit').forEach(el => {
        const target = el.classList.contains('bx-tag') ? W * 0.634 : W;
        for (let i = 0; i < 4; i++) {
          const w = el.getBoundingClientRect().width;
          el.style.fontSize = parseFloat(getComputedStyle(el).fontSize) * target / w + 'px';
        }
      });
      document.querySelectorAll('.fitzoom').forEach(el => { el.style.zoom = W / el.getBoundingClientRect().width; });
    });
    const overflow = await page.evaluate(() => document.body.scrollHeight > 1350 || document.body.scrollWidth > 1080);
    await page.screenshot({ path: path.join(out, png) });
    fs.unlinkSync(tmp);
    console.log(png, overflow ? 'DEBORDE' : 'ok');
  }
  await browser.close();
})();
