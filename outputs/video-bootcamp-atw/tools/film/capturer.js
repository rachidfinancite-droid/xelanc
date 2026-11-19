// Capture du film : node capturer.js <dossier sortie> [début s] [fin s] [fps] ; ou --cles <dossier> pour la planche d'images clés.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const FILM = 'file://' + path.resolve(__dirname, '../../film/film.html');
(async () => {
  const args = process.argv.slice(2);
  const cles = args[0] === '--cles';
  const out = cles ? args[1] : args[0];
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto(FILM);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(1500);
  const info = await p.evaluate(() => { renderAt(0); return { duree: FILM.duree, plan: FILM.plan.map(s => ({ k: s.k, tc: s.tc, t0: s.t0, t1: s.t1, n: s.units.length })), events: FILM.events }; });
  fs.writeFileSync(path.join(out, 'plan.json'), JSON.stringify(info, null, 1));
  if (cles) {
    // pour chaque écran, l'image une fois toutes les entrées faites
    for (const s of info.plan) {
      const t = Math.min(s.t1 - 0.4, s.t0 + 0.5 + s.n * 0.5 + 0.6);
      await p.evaluate(t => renderAt(t), t);
      await p.screenshot({ path: path.join(out, `cle_${String(s.k).padStart(2, '0')}.jpg`), type: 'jpeg', quality: 85 });
    }
  } else {
    const t0 = parseFloat(args[1] || '0'), t1 = Math.min(parseFloat(args[2] || info.duree), info.duree), fps = parseInt(args[3] || '30');
    const n = Math.round((t1 - t0) * fps);
    for (let i = 0; i < n; i++) {
      await p.evaluate(t => renderAt(t), t0 + i / fps);
      await p.screenshot({ path: path.join(out, `f_${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 92 });
      if (i % 150 === 0) console.log(i, '/', n);
    }
  }
  console.log('durée totale', info.duree.toFixed(1), 's');
  await b.close();
})();
