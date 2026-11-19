// Compose les bannières des cours 1 à 5 sur le modèle des bannières du bloc 3 :
// photo à droite étalonnée bleu nuit, dégradé navy à gauche, titre blanc gras, filet bleu clair, sous-titre.
const { chromium } = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '..');
const A = p => 'file://' + path.join(root, 'assets', p);

const COURS = [
  { id: 'c1', titre: 'Lecture 360°', sous: 'Écosystème sectoriel<br>et business model', pos: '62% 40%' },
  { id: 'c2', titre: 'Analyse<br>financière', sous: 'Structurer et réussir<br>son analyse', pos: '70% 40%' },
  { id: 'c3', titre: 'Aspects juridiques<br>et fiscaux', sous: 'Au service de<br>la relation de crédit', pos: '72% 40%' },
  { id: 'c4', titre: 'Décision<br>de crédit', sous: "Lire l'entreprise<br>pour trancher juste", pos: '75% 40%' },
  { id: 'c5', titre: 'Financement<br>de la croissance', sous: 'Les bonnes pratiques<br>du banquier', pos: '68% 40%' },
];

const page = c => `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:DMS;src:url(${A('fonts/dm-sans-latin-700-normal.woff2')});font-weight:700}
@font-face{font-family:DMS;src:url(${A('fonts/dm-sans-latin-400-normal.woff2')});font-weight:400}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1600px;height:900px;overflow:hidden;background:#0b1a33;font-family:DMS,sans-serif}
.ph{position:absolute;inset:0;background:url(${A('soul/' + c.id + '.png')}) ${c.pos}/cover no-repeat;filter:saturate(.75) contrast(1.05) brightness(.82)}
.tint{position:absolute;inset:0;background:#123a6b;mix-blend-mode:color;opacity:.38}
.grad{position:absolute;inset:0;background:linear-gradient(90deg,#0b1a33 0%,rgba(11,26,51,.96) 26%,rgba(11,26,51,.78) 42%,rgba(11,26,51,.25) 62%,rgba(11,26,51,0) 78%)}
.vig{position:absolute;inset:0;background:radial-gradient(ellipse at 75% 45%,transparent 45%,rgba(5,12,26,.45) 100%)}
.txt{position:absolute;left:88px;top:50%;transform:translateY(-50%);width:820px;color:#fff}
h1{font-size:86px;font-weight:700;line-height:1.04;letter-spacing:-.01em}
.rule{width:96px;height:5px;background:#8fb6ea;border-radius:3px;margin:44px 0 34px}
p{font-size:38px;line-height:1.3;color:#e8eef7}
</style></head><body><div class="ph"></div><div class="tint"></div><div class="grad"></div><div class="vig"></div>
<div class="txt"><h1>${c.titre}</h1><div class="rule"></div><p>${c.sous}</p></div></body></html>`;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  for (const c of COURS) {
    const tmp = path.join(require('os').tmpdir(), '_banniere_tmp.html');
    require('fs').writeFileSync(tmp, page(c));
    await p.goto('file://' + tmp, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(root, 'assets', 'bannieres', c.id + '.jpg'), type: 'jpeg', quality: 90 });
  }
  await b.close();
  console.log('ok');
})();
