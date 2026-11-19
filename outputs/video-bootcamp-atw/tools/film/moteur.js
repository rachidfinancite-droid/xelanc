/* Moteur du film GRE · CCE.
   Reprend les écrans 1920×1080 des planches (div.fr), les empile sur une scène,
   et les anime image par image : window.renderAt(t) dessine l'instant t (secondes).
   Méthode « La finance avance vite » : grille de 0,5 s (120 BPM), lignes qui roulent (ROLL),
   chiffres qui frappent (SLAM), fond en léger mouvement de caméra, sortie inverse avant la fin de l'écran. */
(function () {
  const GRILLE = 0.5;
  const ease = x => 1 - Math.pow(1 - Math.min(Math.max(x, 0), 1), 3);
  const snap = t => Math.round(t / GRILLE) * GRILLE;

  function preparer() {
    const VOIX = window.FILM_VOIX || {};
    const frames = [...document.querySelectorAll('section.page')].map(sec => {
      const fr = sec.querySelector('.fr'); if (!fr) return null;
      const tc = (sec.querySelector('.tc') || {}).textContent || '';
      return { fr, tc };
    }).filter(Boolean);
    const stage = document.createElement('div'); stage.id = 'stage'; document.body.appendChild(stage);
    let t = 0;
    const plan = [], events = [];
    frames.forEach(({ fr, tc }, k) => {
      fr.style.transform = 'none'; fr.style.position = 'absolute'; fr.style.inset = '0';
      fr.style.opacity = 0; fr.style.visibility = 'hidden';
      stage.appendChild(fr);
      // unités animées : enfants directs, ou petits-enfants quand un enfant est une liste (grille, colonne)
      const kids = [...fr.children].filter(e => e.tagName !== 'STYLE');
      const bg = [], units = [];
      kids.forEach(e => {
        const cs = getComputedStyle(e);
        const plein = e.offsetWidth >= 1900 && e.offsetHeight >= 1060;
        if (plein && !e.textContent.trim()) { bg.push(e); return; }
        if (e.tagName === 'svg') { units.push({ el: e, fx: 'rise' }); return; }
        const sous = [...e.children].filter(c => c.tagName !== 'STYLE');
        const liste = (cs.display.includes('flex') || cs.display.includes('grid')) && sous.length >= 2 && e.textContent.trim().length > 0;
        if (liste) sous.forEach(c => units.push({ el: c }));
        else units.push({ el: e });
      });
      units.forEach(u => { u.base = u.el.style.transform || ''; });
      bg.forEach(b => { b.dataset.base = b.style.transform || ''; });
      units.forEach(u => {
        if (u.fx) return;
        const txt = u.el.textContent.replace(/\s+/g, ' ').trim();
        const chiffre = /^[\d\s ,.\/%+]+(h|%|MDH|\/100)?\b/.test(txt) || u.el.querySelector('.kv b,.kn b,.vn strong,.rs b,.og-st2 b,.pk b');
        u.fx = (u.el.tagName === 'IMG' || u.el.querySelector('img')) ? 'slam' : chiffre ? 'slam' : (txt.length ? 'roll' : 'rise');
      });
      // durée : entrée des unités sur la grille, puis temps de lecture
      const mots = fr.textContent.trim().split(/\s+/).length;
      const v = VOIX[String(k + 1)];
      let at = 0.5;
      units.forEach((u, i) => { u.at = at; at += (i === units.length - 1 ? 0 : (u.fx === 'slam' ? 0.5 : 0.5)); });
      const entree = at + 0.5;
      let duree = Math.min(Math.max(entree + 1.2 + mots / 9, 4), 8.5);
      if (v) duree = Math.max(duree, (v.debut || entree) + v.duree + 1.0);
      duree = snap(duree);
      const t0 = t, t1 = t + duree;
      units.forEach(u => { u.t = t0 + u.at; events.push({ t: u.t, type: u.fx }); });
      if (v) events.push({ t: t0 + (v.debut || entree), type: 'voix', fichier: v.fichier, duree: v.duree });
      plan.push({ k: k + 1, tc, fr, bg, units, t0, t1, voix: v });
      t = t1;
    });
    window.FILM = { plan, events, duree: t };
  }

  function roll(el, p, sortie, base) {
    // p : progression de l'entrée (0→1 en 0,2 s) ; rebond amorti après
    if (p <= 0) { el.style.opacity = 0; return; }
    const e = ease(p);
    const rx = -95 * (1 - e), ty = 55 * (1 - e), bl = 10 * (1 - e);
    el.style.opacity = Math.min(1, e * 1.4) * (1 - sortie);
    el.style.transform = base + ` perspective(1400px) translateY(${ty - 40 * sortie}%) rotateX(${rx + 80 * sortie}deg)`;
    el.style.filter = (bl + 10 * sortie) > 0.05 ? `blur(${bl + 10 * sortie}px)` : 'none';
  }
  function slam(el, p, sortie, base) {
    if (p <= 0) { el.style.opacity = 0; return; }
    const e = ease(p);
    el.style.opacity = Math.min(1, e * 1.6) * (1 - sortie);
    el.style.transform = base + ` scale(${1.3 - 0.3 * e - 0.08 * sortie})`;
    el.style.filter = sortie > 0.01 ? `blur(${8 * sortie}px)` : 'none';
  }
  function rise(el, p, sortie, base) {
    if (p <= 0) { el.style.opacity = 0; return; }
    const e = ease(p);
    el.style.opacity = e * (1 - sortie);
    el.style.transform = base + ` translateY(${40 * (1 - e) - 30 * sortie}px)`;
  }

  window.renderAt = function (t) {
    if (!window.FILM) preparer();
    const { plan } = window.FILM;
    for (const s of plan) {
      const actif = t >= s.t0 - 0.001 && t < s.t1;
      s.fr.style.visibility = actif ? 'visible' : 'hidden';
      s.fr.style.opacity = actif ? 1 : 0;
      if (!actif) continue;
      const d = t - s.t0, D = s.t1 - s.t0;
      // caméra : léger zoom continu ; fond en Ken Burns un peu plus marqué
      s.bg.forEach(b => { b.style.transform = b.dataset.base + ` scale(${1.02 + 0.06 * d / D})`; b.style.transformOrigin = '60% 40%'; });
      let shake = 0;
      for (const u of s.units) {
        const p = (t - u.t) / (u.fx === 'slam' ? 0.18 : u.fx === 'roll' ? 0.2 : 0.4);
        const sortie = Math.min(Math.max((t - (s.t1 - 0.22)) / 0.18, 0), 1);
        if (u.fx === 'roll') {
          roll(u.el, p, sortie, u.base);
          const r = t - u.t - 0.2;  // rebond amorti
          if (r > 0 && r < 0.6 && sortie === 0) u.el.style.transform += ` translateY(${Math.exp(-14 * r) * Math.sin(40 * r) * 6}%)`;
        } else if (u.fx === 'slam') {
          slam(u.el, p, sortie, u.base);
          const q = t - u.t - 0.18; if (q > 0 && q < 0.12) shake = Math.max(shake, 6 * (1 - q / 0.12));
        } else rise(u.el, p, sortie, u.base);
      }
      // tremblement du plan après une frappe ; fondu d'entrée de l'écran
      const sx = shake ? (Math.sin(t * 120) * shake) : 0, sy = shake ? (Math.cos(t * 97) * shake) : 0;
      s.fr.style.transform = `translate(${sx}px,${sy}px)`;
      s.fr.style.opacity = Math.min(1, d / 0.25);
    }
    // sous-titres de la voix
    const st = document.getElementById('soustitre'); let txt = '';
    for (const s of plan) if (s.voix && t >= s.t0 && t < s.t1) {
      const r = t - s.t0 - (s.voix.debut || 0);
      for (const [a, b, x] of s.voix.subs || []) if (r >= a && r < b + (b === s.voix.subs[s.voix.subs.length - 1][1] ? 1.2 : 0)) txt = x;
    }
    st.innerHTML = txt ? '<span>' + txt.replace(/\n/g, '<br>') + '</span>' : '';
    // fondu au noir final
    const fin = window.FILM.duree;
    document.getElementById('noir').style.opacity = Math.min(Math.max((t - (fin - 1.9)) / 1.9, 0), 1);
  };
})();
