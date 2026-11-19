"""Section « Action terrain : l'origination ».
Sources : Revue des travaux d'origination (30 dossiers au 17/11/2026), Programme du bootcamp d'origination,
La méthode du pitch (jour 1), Accompagnement des tables rondes (jour 1)."""

SCRIM = '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,20,40,.86) 0%,rgba(8,20,40,.68) 34%,rgba(8,20,40,.32) 60%,rgba(8,20,40,0) 82%)"></div>'
GRIS = '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 28% 18%,#f7f7f6 0%,#ececeb 45%,#dedfe0 100%)"></div>'
NUIT = '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 30%,#173158 0%,#0b1a33 60%,#060f20 100%)"></div>'
FILET = '<div style="position:absolute;left:640px;top:180px;bottom:180px;width:2px;background:rgba(200,169,106,.8)"></div>'

STYLE = """<style>
.og-step{flex:1;background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(15,39,68,.16);padding:40px 38px;display:flex;flex-direction:column}
.og-step .n{font-family:var(--serif);font-size:96px;font-weight:600;color:#139fc4;line-height:.9}
.og-step span{font-size:19px;letter-spacing:.2em;text-transform:uppercase;color:#6f8198;margin-top:18px;font-weight:600}
.og-step b{display:block;font-family:var(--serif);font-size:52px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:8px}
.og-step p{font-size:29px;line-height:1.42;color:#3f5168;margin:20px 0 0}
.og-step .kp{margin-top:auto;border-top:2px solid #e3e5e8;padding-top:18px;font-size:24px;color:#0f2744;font-weight:500}
.og-step .kp strong{font-family:var(--serif);font-size:64px;font-weight:600;color:#139fc4;margin-right:10px}
.og-fun{display:flex;align-items:center;gap:30px;margin-bottom:26px}
.og-fun .l{width:520px;font-size:30px;color:#3f5168}
.og-fun .b{height:58px;border-radius:12px;background:#0f2744}
.og-fun .v{font-family:var(--serif);font-size:64px;font-weight:600;color:#139fc4;min-width:150px}
.og-st{border-top:2px solid #c8a96a;padding-top:24px}
.og-st b{display:block;font-family:var(--serif);font-size:104px;font-weight:500;color:#fff;line-height:1;white-space:nowrap}
.og-st span{display:block;font-size:28px;line-height:1.35;color:#c9d6e6;margin-top:16px}
.og-sec{display:grid;grid-template-columns:330px 1fr 60px;align-items:center;gap:20px;margin-bottom:22px;font-size:27px;color:#d6dfeb}
.og-sec .t{height:22px;background:rgba(255,255,255,.12);border-radius:11px;overflow:hidden}.og-sec .t i{display:block;height:100%;background:#5fd0ea;border-radius:11px}
.og-sec b{font-family:var(--serif);font-size:36px;color:#fff;text-align:right}
.og-deal{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(15,39,68,.16);padding:36px 34px;display:flex;flex-direction:column}
.og-deal span{font-size:18px;letter-spacing:.2em;text-transform:uppercase;color:#139fc4;font-weight:600}
.og-deal b{display:block;font-family:var(--serif);font-size:46px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:10px;min-height:96px}
.og-deal em{display:block;font-style:normal;font-size:23px;color:#6f8198;margin-top:6px}
.og-deal p{font-size:27px;line-height:1.42;color:#3f5168;margin:18px 0 18px}
.og-deal .m{margin-top:auto;border-top:2px solid #e3e5e8;padding-top:14px}
.og-deal .m strong{font-family:var(--serif);font-size:84px;font-weight:600;color:#139fc4;line-height:.95}
.og-deal .m small{display:block;font-size:22px;color:#0f2744;font-weight:500;margin-top:6px}
.og-tl{flex:1;border-top:4px solid #c8a96a;padding-top:26px}
.og-tl small{display:block;font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:#c8a96a;font-weight:600}
.og-tl b{display:block;font-family:var(--serif);font-size:44px;font-weight:600;color:#fff;line-height:1.08;margin-top:12px}
.og-tl p{font-size:24px;line-height:1.4;color:#c9d6e6;margin:14px 0 0}
</style>"""


def make(start, nb, img):
    n = [start]

    def nxt():
        n[0] += 1
        return n[0]

    def page(left, num, tc, role, vo, ecran, src):
        return (f'\n<section class="page"><div class="left"><div class="fw"><div class="fr" style="background:#0b1a33">{left}</div></div></div>'
                f'<div class="right"><div class="n">{num:02d}</div><div class="tc">{tc}</div><div class="role">{role}</div>'
                f'<div class="lab">Voix off</div><div class="vo">{vo}</div>'
                f'<div class="lab">À l\'écran</div><div class="t">{ecran}</div></div>'
                f'<div class="foot">Écran {num} · {src}</div></section>')

    out = []
    bg = img('origination')

    # 1. Ouverture
    left = (f'<div style="position:absolute;inset:0;background:url({bg}) center/cover"></div>' + SCRIM + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:110px;font-weight:600;line-height:1;color:#fff">Action<br>terrain</div>'
            '<div style="font-family:var(--serif);font-size:50px;font-weight:500;line-height:1.15;color:#c8a96a;margin-top:24px">Octobre – novembre</div>'
            '<div style="font-size:24px;letter-spacing:.24em;color:#d9e2ee;margin-top:14px">2026</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-50%);width:760px;text-shadow:0 2px 20px rgba(0,0,0,.35)">'
            '<div style="font-family:var(--serif);font-size:150px;font-weight:600;line-height:.98;color:#fff">L\'origination</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:500;font-style:italic;line-height:1.08;color:#fff;margin-top:20px">être à l\'origine du deal</div></div>')
    out.append(page(left, nxt(), 'Action terrain · ouverture', "L'origination", 'Aucune. Montée musicale.',
                    "Même construction que les ouvertures de blocs : à gauche « Action terrain » et la période, à droite le titre complet.",
                    'Image : bibliothèque Higgsfield'))

    # 2. Objectif
    left = (NUIT + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:600;line-height:1.02;color:#fff">Objectif<br>du terrain</div>'
            '<div style="font-size:24px;letter-spacing:.24em;color:#c8a96a;margin-top:26px;text-transform:uppercase">Mise en application</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-58%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:104px;font-weight:500;line-height:1.04;color:#fff">Aller chercher l\'entreprise,<br><em style="color:#c8a96a">et la convaincre.</em></div>'
            '<div style="font-size:36px;line-height:1.4;color:#c9d6e6;margin-top:40px">Mettre en œuvre tout le parcours sur de vraies entreprises : repérer, qualifier, préparer l\'entrée en relation.</div></div>')
    out.append(page(left, nxt(), 'Action terrain · objectif', 'La confirmation de tout le parcours',
                    "« Tout ce qui a été appris prend ici son sens : face à une vraie entreprise, qui n'est pas encore cliente. »",
                    "À gauche, « Objectif du terrain ». À droite, la phrase en grand puis le sous-titre.",
                    'Programme du bootcamp d\'origination'))

    # 3. Le profil
    left = (GRIS +
            '<div style="position:absolute;left:120px;top:90px"><div class="sur">Le profil visé</div></div>'
            '<div style="position:absolute;left:120px;top:300px;width:1680px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:500;color:#9aa8ba;line-height:1.05;text-decoration:line-through;text-decoration-color:#a8324a;text-decoration-thickness:6px">Un gestionnaire administratif</div>'
            '<div style="font-family:var(--serif);font-size:110px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:40px">Un banquier qui va chercher<br>ses clients, <em style="color:#139fc4">et sait leur tenir tête.</em></div></div>'
            '<div style="position:absolute;left:120px;top:780px;display:flex;gap:50px;font-family:var(--serif);font-size:48px;font-weight:600;color:#0f2744">'
            '<span>Prospecter</span><span style="color:#c8a96a">·</span><span>Qualifier</span><span style="color:#c8a96a">·</span>'
            '<span>Convaincre</span><span style="color:#c8a96a">·</span><span>Défendre en comité</span></div>')
    out.append(page(left, nxt(), 'Action terrain · profil', 'Le CCE et le GRE complets',
                    "« Le métier ne se joue pas seulement derrière un bureau. Il se joue chez le client. »",
                    "La première ligne s'affiche, puis se fait barrer en rouge. La seconde arrive en grand, la fin en cyan.",
                    'Doctrine du programme'))

    # 4. La démarche en trois étapes
    steps = [
        ('1', 'Fiche 1', 'Repérer', "Dix à quinze entreprises du territoire, notées sur 20 : déclencheur, potentiel, accessibilité, adéquation à l'offre, risque.", '13/20', 'seuil conseillé'),
        ('2', 'Fiche 2', 'Faire valider', "Les sept meilleures cibles présentées au manager, qui en retient cinq. Aucun contact avant la soutenance.", '5', 'cibles par participant'),
        ('3', 'Fiche 3', 'Documenter', "Une fiche prospect par cible : business model, déclencheur, besoin, angle, porte d'entrée, objections, réponse globale.", '145', 'fiches prospect'),
    ]
    cards = ''.join(f'<div class="og-step"><div class="n">{a}</div><span>{b}</span><b>{c}</b><p>{nb(d)}</p>'
                    f'<div class="kp"><strong>{e}</strong>{f}</div></div>' for a, b, c, d, e, f in steps)
    left = (GRIS +
            '<div style="position:absolute;left:120px;top:70px"><div class="sur">La démarche · trois étapes conduites par les participants</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:12px">Du territoire au dossier</div></div>'
            f'<div style="position:absolute;left:120px;top:280px;width:1680px;height:600px;display:flex;gap:36px">{cards}</div>')
    out.append(page(left, nxt(), 'Action terrain · démarche', 'Trois fiches, trois gestes',
                    "« Chacun a d'abord regardé son propre territoire. Puis il a choisi, avec son manager. Puis il a documenté. »",
                    "Les trois cartes arrivent une par une, leur chiffre défile en bas.",
                    "Revue des travaux d'origination, p. 5"))

    # 5. L'entonnoir
    fun = [('Entreprises repérées et notées', 424), ('Cibles présentées aux managers', 210), ('Cibles étudiées', 161),
           ('Fiches prospect rédigées', 145), ('Prospects retenus pour la soutenance', 72)]
    rows = ''.join(f'<div class="og-fun"><div class="l">{nb(t)}</div><div class="b" style="width:{int(v / 424 * 860)}px{";background:#139fc4" if v == 72 else ""}"></div>'
                   f'<div class="v">{v}</div></div>' for t, v in fun)
    left = (GRIS +
            '<div style="position:absolute;left:120px;top:70px"><div class="sur">Le travail de sélection</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:12px">De 424 entreprises à 72 prospects</div></div>'
            f'<div style="position:absolute;left:120px;top:270px;width:1700px">{rows}</div>'
            '<div style="position:absolute;left:120px;top:900px;display:flex;gap:90px;font-size:30px;color:#0f2744">'
            '<span><b style="font-family:var(--serif);font-size:56px;color:#139fc4">30/30</b>&nbsp; participants ont remis leurs travaux</span>'
            '<span><b style="font-family:var(--serif);font-size:56px;color:#139fc4">5,9</b>&nbsp; entreprises repérées pour un prospect retenu</span></div>')
    out.append(page(left, nxt(), 'Action terrain · sélection', 'Une vraie sélection',
                    "« Ils ont repéré plus de quatre cents entreprises. Ils n'en ont gardé que les meilleures. »",
                    "Les barres poussent l'une après l'autre ; la dernière, celle des 72 prospects, passe en cyan.",
                    "Revue des travaux d'origination, p. 6"))

    # 6. Le portefeuille
    secs = [('BTP et génie civil', 27), ('Agroalimentaire', 20), ('Plasturgie, emballage', 17), ('Distribution, négoce', 15),
            ('Métallurgie, matériaux', 14), ('Chimie, pharmacie, santé', 11)]
    bars = ''.join(f'<div class="og-sec"><span>{nb(t)}</span><div class="t"><i style="width:{int(v / 27 * 100)}%"></i></div><b>{v}</b></div>' for t, v in secs)
    stats = [('91 %', "de PME non clientes, qui décident de leur banque au Maroc"), ('43 %', "tournées vers l'international"),
             ('88 %', "des prospects retenus portés par un événement propre à l'entreprise")]
    st = ''.join(f'<div class="og-st"><b>{nb(a)}</b><span>{nb(b)}</span></div>' for a, b in stats)
    left = (NUIT +
            '<div style="position:absolute;left:120px;top:80px"><div class="kick">Le portefeuille construit</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:500;color:#fff;line-height:1.05;margin-top:14px">Un vivier réel, ancré dans l\'économie productive</div></div>'
            f'<div style="position:absolute;left:120px;top:330px;width:900px"><div style="font-size:22px;letter-spacing:.2em;color:#9db6d6;margin-bottom:26px">161 CIBLES · 16 SECTEURS · 8 RÉGIONS</div>{bars}</div>'
            f'<div style="position:absolute;left:1110px;top:320px;width:700px;display:flex;flex-direction:column;gap:40px">{st}</div>')
    out.append(page(left, nxt(), 'Action terrain · portefeuille', "L'économie réelle",
                    "« Des PME marocaines, non clientes, dans les secteurs qui font l'économie du pays. »",
                    "Les barres des secteurs poussent, puis les trois chiffres à droite défilent l'un après l'autre.",
                    "Revue des travaux d'origination, p. 9 et 10"))

    # 7. Des dossiers représentatifs
    deals = [('Immobilier · tourisme d\'affaires', 'Mfadel Group', 'Casablanca Finance City', "Complexe Radisson, ouverture en 2028.", '850', 'MDH de projet'),
             ('Agroalimentaire', 'Fortune Maroc', 'Bouskoura', "Extension de l'usine, une seconde de 65 MDH annoncée.", '220', 'MDH d\'extension'),
             ('Câblerie', 'FBR Cables', 'Berrechid', "Usine inaugurée : 165 emplois, 70 000 km de câble par an.", '200', 'MDH investis'),
             ('Paiement · fintech', 'ORA Technologies', 'Casablanca', "Levée de série A, dont 2 M$ d'investisseurs marocains.", '10', 'M$ levés')]
    cards = ''.join(f'<div class="og-deal" style="width:396px"><span>{nb(a)}</span><b>{nb(b)}</b><em>{nb(c)}</em><p>{nb(d)}</p>'
                    f'<div class="m"><strong>{e}</strong><small>{nb(f)}</small></div></div>' for a, b, c, d, e, f in deals)
    left = (GRIS +
            '<div style="position:absolute;left:120px;top:70px"><div class="sur">Des opportunités concrètes · sources publiques</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:12px">Un événement précis, une réponse adaptée</div></div>'
            f'<div style="position:absolute;left:120px;top:280px;height:620px;display:flex;gap:32px">{cards}</div>')
    out.append(page(left, nxt(), 'Action terrain · dossiers', 'Des deals, pas des exercices',
                    "« Derrière chaque fiche, un vrai projet : des dizaines, parfois des centaines de millions de dirhams. »",
                    "Quatre dossiers représentatifs, même forme que les cartes d'épreuves ; le montant défile en cyan.",
                    "Revue des travaux d'origination, p. 20 et 21"))

    # 8. Le bootcamp d'origination
    tl = [('Jour 1 · matin', 'Revue et classification', "Chaque portefeuille revu et classé par secteur."),
          ('Jour 1 · après-midi', 'Tables rondes sectorielles', "Douze tables, une par filière ; la méthode du pitch en sept temps."),
          ('Jour 2 · matin', 'Face aux métiers', "Regards croisés avec les métiers de la banque, premiers pitchs devant eux."),
          ('Jour 2 · après-midi', 'Feuille de route', "Recommandations et préparation individuelle de la soutenance.")]
    cols = ''.join(f'<div class="og-tl"><small>{a}</small><b>{nb(b)}</b><p>{nb(c)}</p></div>' for a, b, c in tl)
    left = (NUIT +
            '<div style="position:absolute;left:120px;top:80px"><div class="kick">Le bootcamp d\'origination · 19 et 20 novembre</div>'
            '<div style="font-family:var(--serif);font-size:84px;font-weight:500;color:#fff;line-height:1.05;margin-top:14px">Du dossier au pitch qui convainc</div></div>'
            f'<div style="position:absolute;left:120px;top:400px;width:1680px;display:flex;gap:44px">{cols}</div>'
            '<div style="position:absolute;left:120px;top:860px;display:flex;gap:100px">'
            '<div class="og-st" style="border:none;padding:0"><b style="font-size:84px">2</b><span>journées</span></div>'
            '<div class="og-st" style="border:none;padding:0"><b style="font-size:84px">12</b><span>tables rondes sectorielles</span></div>'
            '<div class="og-st" style="border:none;padding:0"><b style="font-size:84px">7</b><span>temps de pitch</span></div>'
            '<div class="og-st" style="border:none;padding:0"><b style="font-size:84px">1</b><span>pitch par participant</span></div></div>')
    out.append(page(left, nxt(), 'Action terrain · bootcamp', 'Deux jours pour être prêt',
                    "« Deux jours pour transformer chaque dossier en un pitch défendable : pourquoi elle, pourquoi maintenant, pourquoi nous. »",
                    "Les quatre temps forts se dévoilent de gauche à droite, puis les quatre chiffres montent en bas.",
                    "Programme du bootcamp ; tables rondes, jour 1"))

    # 9. La suite
    left = (NUIT + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:600;line-height:1.02;color:#fff">La suite</div>'
            '<div style="font-size:24px;letter-spacing:.24em;color:#c8a96a;margin-top:26px;text-transform:uppercase">Certification</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-55%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:200px;font-weight:600;line-height:.9;color:#5fd0ea">72</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:500;line-height:1.08;color:#fff;margin-top:20px">prospects défendus<br><em style="color:#c8a96a">devant un jury.</em></div>'
            '<div style="font-size:34px;line-height:1.4;color:#c9d6e6;margin-top:36px">Puis la prise de contact, accompagnée par le manager.</div></div>')
    out.append(page(left, nxt(), 'Action terrain · la suite', 'Du pitch à la relation',
                    "« Prochaine étape : la soutenance. Puis le terrain, le vrai, avec le manager à leurs côtés. »",
                    "À gauche, « La suite ». À droite, le 72 en grand, puis la phrase et le sous-titre.",
                    "Revue des travaux d'origination, p. 33"))
    return STYLE + ''.join(out), n[0]
