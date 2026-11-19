"""Section « Action terrain : l'origination ».
Sources : Revue des travaux d'origination (30 dossiers au 17/11/2026), Programme du bootcamp d'origination,
La méthode du pitch (jour 1), Accompagnement des tables rondes (jour 1)."""

SCRIM = '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,20,40,.86) 0%,rgba(8,20,40,.68) 34%,rgba(8,20,40,.32) 60%,rgba(8,20,40,0) 82%)"></div>'
GRIS = '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 28% 18%,#f7f7f6 0%,#ececeb 45%,#dedfe0 100%)"></div>'
NUIT = '<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 30%,#173158 0%,#0b1a33 60%,#060f20 100%)"></div>'
FILET = '<div style="position:absolute;left:640px;top:180px;bottom:180px;width:2px;background:rgba(95,208,234,.8)"></div>'

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
.og-st{border-top:2px solid #5fd0ea;padding-top:24px}
.og-st b{display:block;font-family:var(--serif);font-size:96px;font-weight:500;color:#fff;line-height:1;white-space:nowrap}
.og-st span{display:block;font-size:28px;line-height:1.35;color:#c9d6e6;margin-top:16px}
.og-st2{border-top:2px solid #5fd0ea;padding-top:22px}.og-st2 span{display:block;font-size:34px;line-height:1.3;color:#fff;font-weight:500}.og-st2 b{display:block;font-family:var(--serif);font-size:92px;font-weight:500;color:#5fd0ea;line-height:1;margin-top:10px}
.og-sec{display:grid;grid-template-columns:380px 1fr 60px;align-items:center;gap:20px;margin-bottom:24px;font-size:31px;color:#d6dfeb}
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
.og-v{display:flex;align-items:baseline;gap:30px;border-top:1px solid rgba(95,208,234,.45);padding-top:18px}
.og-v small{width:300px;flex:none;white-space:nowrap;font-size:21px;letter-spacing:.12em;text-transform:uppercase;color:#5fd0ea;font-weight:600}
.og-v b{font-family:var(--serif);font-size:48px;font-weight:600;color:#fff}
.kvg{position:absolute;left:880px;right:110px;top:56%;transform:translateY(-50%);display:flex;flex-direction:column}
.kv{display:grid;grid-template-columns:420px 1fr;align-items:center;column-gap:36px;border-top:2px solid rgba(95,208,234,.75);padding:24px 0}
.kv b{font-family:var(--serif);font-size:124px;font-weight:500;color:#5fd0ea;line-height:1;font-variant-numeric:lining-nums;white-space:nowrap}
.kv span{font-size:38px;line-height:1.25;color:#fff;font-weight:500}
.fr .kt,.fr .kt *{text-wrap:nowrap;white-space:nowrap}
.ktop{position:absolute;left:110px;top:70px;font-size:44px;letter-spacing:.2em;text-transform:uppercase;color:#fff;background:#139fc4;font-weight:700;padding:14px 30px 12px;border-radius:6px}
.kk{font-size:24px;letter-spacing:.26em;text-transform:uppercase;color:#5fd0ea;font-weight:600}
.kng{position:absolute;left:700px;right:110px;top:50%;transform:translateY(-50%);display:grid;grid-template-columns:1fr 1fr;column-gap:70px;row-gap:64px}
.kn{border-top:2px solid #5fd0ea;padding-top:24px}
.kn b{display:block;font-family:var(--serif);font-size:150px;font-weight:500;color:#5fd0ea;line-height:.95;font-variant-numeric:lining-nums;white-space:nowrap}
.kn span{display:block;font-size:32px;line-height:1.3;color:#fff;margin-top:16px;font-weight:500}
.pk{border-top:2px solid #5fd0ea;padding-top:16px}
.pk b{display:block;font-family:var(--serif);font-size:80px;font-weight:500;color:#5fd0ea;line-height:1;font-variant-numeric:lining-nums}
.pk span{display:block;font-size:26px;line-height:1.3;color:#fff;margin-top:8px}
.kfg{position:absolute;left:120px;top:300px;width:1680px;display:grid;grid-template-columns:230px repeat(4,1fr);column-gap:36px;row-gap:0}
.kf-l{border-top:1px solid rgba(95,208,234,.5);padding-top:30px;font-size:21px;letter-spacing:.2em;text-transform:uppercase;color:#5fd0ea;font-weight:600}
.kf{border-top:1px solid rgba(255,255,255,.16);padding:22px 0 26px}
.kf b{display:block;font-family:var(--serif);font-size:78px;font-weight:500;color:#5fd0ea;line-height:1;font-variant-numeric:lining-nums}
.kf span{display:block;font-size:23px;line-height:1.3;color:#d9e2ee;margin-top:10px}
.og-tl{flex:1;border-top:4px solid #5fd0ea;padding-top:26px}
.og-tl small{display:block;font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:#5fd0ea;font-weight:600}
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
            '<div style="font-family:var(--serif);font-size:50px;font-weight:500;line-height:1.15;color:#5fd0ea;margin-top:24px">Octobre – novembre</div>'
            '<div style="font-size:24px;letter-spacing:.24em;color:#d9e2ee;margin-top:14px">2026</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-50%);width:760px;text-shadow:0 2px 20px rgba(0,0,0,.35)">'
            '<div style="font-family:var(--serif);font-size:150px;font-weight:600;line-height:.98;color:#fff">L\'origination</div>'
            '<div style="font-family:var(--serif);font-size:72px;font-weight:500;font-style:italic;line-height:1.08;color:#fff;margin-top:20px">être à l\'origine de l\'entrée en relation</div></div>')
    out.append(page(left, nxt(), 'Action terrain · ouverture', "L'origination", 'Aucune. Montée musicale.',
                    "Même construction que les ouvertures de blocs : à gauche « Action terrain » et la période, à droite le titre complet.",
                    'Image : bibliothèque Higgsfield'))

    # 2. Objectif
    left = (NUIT + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:600;line-height:1.02;color:#fff">Objectif<br>du terrain</div>'
            '<div style="font-size:24px;letter-spacing:.24em;color:#5fd0ea;margin-top:26px;text-transform:uppercase">Mise en application</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-58%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:88px;font-weight:500;line-height:1.06;color:#fff">Aller chercher<br>de nouvelles relations,<br><em style="color:#5fd0ea">et concrétiser<br>l\'entrée en relation.</em></div>'
            '<div style="font-size:36px;line-height:1.4;color:#c9d6e6;margin-top:40px">En appliquant les bonnes pratiques : repérer, qualifier, préparer l\'entrée en relation.</div></div>')
    out.append(page(left, nxt(), 'Action terrain · objectif', 'La confirmation de tout le parcours',
                    "« Tout ce qui a été appris prend ici son sens : face à une vraie entreprise, qui n'est pas encore cliente. »",
                    "À gauche, « Objectif du terrain ». À droite, la phrase en grand puis le sous-titre.",
                    'Programme du bootcamp d\'origination'))

    # 3. Le profil
    left = (GRIS +
            '<div style="position:absolute;left:120px;top:90px"><div class="sur">Le profil visé</div></div>'
            '<div style="position:absolute;left:120px;top:300px;width:1680px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:500;color:#9aa8ba;line-height:1.05;text-decoration:line-through;text-decoration-color:#9db6d6;text-decoration-thickness:6px">Un gestionnaire administratif</div>'
            '<div style="font-family:var(--serif);font-size:100px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:40px">Un banquier qui va chercher ses clients,<br><em style="color:#139fc4">sait les convaincre et les accompagner.</em></div></div>'
            '<div style="position:absolute;left:120px;top:850px;display:flex;gap:50px;font-family:var(--serif);font-size:48px;font-weight:600;color:#0f2744">'
            '<span>Prospecter</span><span style="color:#5fd0ea">·</span><span>Qualifier</span><span style="color:#5fd0ea">·</span>'
            '<span>Convaincre</span><span style="color:#5fd0ea">·</span><span>Accompagner</span></div>')
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
            '<div style="font-family:var(--serif);font-size:64px;font-weight:600;color:#0f2744;line-height:1.08;margin-top:12px">424 entrées en relation potentielles identifiées,<br>72 prospects validés</div></div>'
            f'<div style="position:absolute;left:120px;top:320px;width:1700px">{rows}</div>'
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
    stats = [('91 %', "PME non clientes, qui décident de leur banque au Maroc"), ('43 %', "Entreprises tournées vers l'international"),
             ('88 %', "Prospects portés par un événement propre à l'entreprise")]
    st = ''.join(f'<div class="og-st2"><span>{nb(b)}</span><b>{nb(a)}</b></div>' for a, b in stats)
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
    deals = [('Semences · agro-industrie', 'Arzak Seeds Trade', 'Béni Mellal', "Nouvelle unité de conditionnement et de stockage.", '50', 'MDH et plus d\'investissement'),
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

    # 8. Le bootcamp d'origination : en tiers, les quatre temps forts en colonne
    tl = [('Jour 1 · matin', 'Revue et classification'), ('Jour 1 · après-midi', 'Tables rondes sectorielles'),
          ('Jour 2 · matin', 'Face aux métiers de la banque'), ('Jour 2 · après-midi', 'Feuille de route individuelle')]
    rows = ''.join(f'<div class="og-v"><small>{a}</small><b>{nb(b)}</b></div>' for a, b in tl)
    left = (NUIT + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:78px;font-weight:600;line-height:1.04;color:#fff">Bootcamp<br>d\'origination</div>'
            '<div style="font-family:var(--serif);font-size:50px;font-weight:500;color:#5fd0ea;margin-top:24px">19 – 20 novembre</div>'
            '<div style="font-size:24px;letter-spacing:.24em;color:#d9e2ee;margin-top:14px">2026</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-50%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:500;line-height:1.04;color:#fff">Du dossier<br><em style="color:#5fd0ea">au pitch qui convainc.</em></div>'
            f'<div style="margin-top:46px;display:flex;flex-direction:column;gap:22px">{rows}</div></div>')
    out.append(page(left, nxt(), 'Action terrain · bootcamp', 'Deux jours pour être prêt',
                    "« Deux jours pour transformer chaque dossier en un pitch défendable : pourquoi elle, pourquoi maintenant, pourquoi nous. »",
                    "À gauche, « Bootcamp d'origination » et les dates. À droite, le titre, puis les quatre temps forts qui tombent l'un sous l'autre.",
                    "Programme du bootcamp d'origination"))

    # 9. Le dernier maillon
    left = (NUIT + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:96px;font-weight:600;line-height:1.02;color:#fff">Le dernier<br>maillon</div>'
            '<div style="font-family:var(--serif);font-size:50px;font-weight:500;color:#5fd0ea;margin-top:24px">Janvier 2027</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-55%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:110px;font-weight:600;line-height:1.02;color:#fff">Soutenance<br><em style="color:#5fd0ea">et certification</em></div>'
            '<div style="font-size:36px;line-height:1.4;color:#c9d6e6;margin-top:40px">Chaque participant défend ses prospects devant un jury, comme en comité. Puis vient la prise de contact, accompagnée par le manager.</div></div>')
    out.append(page(left, nxt(), 'Action terrain · dernier maillon', 'La soutenance',
                    "« Dernier maillon du parcours : la soutenance devant le jury, et la certification. »",
                    "À gauche, « Le dernier maillon » et la date. À droite, « Soutenance et certification », puis le sous-titre.",
                    "Revue des travaux d'origination, p. 33"))

    # 10 à 14. L'expérience d'upskilling en chiffres : une ouverture, puis un écran par famille de chiffres.
    import base64, os
    A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')
    def photo(rel):
        return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(A, rel), 'rb').read()).decode()
    BAS = '<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,20,40,.82) 0%,rgba(8,20,40,.45) 30%,rgba(8,20,40,.80) 60%,rgba(8,20,40,.94) 100%)"></div>'
    VOILE = '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,20,40,.94) 0%,rgba(8,20,40,.86) 30%,rgba(8,20,40,.72) 60%,rgba(8,20,40,.66) 100%)"></div>'
    FIL4 = '<div style="position:absolute;left:800px;top:220px;bottom:130px;width:2px;background:rgba(95,208,234,.8)"></div>'
    def colonne(kick, titre, extra=''):
        return (f'<div class="ktop">{kick}</div>'
                '<div style="position:absolute;left:110px;top:54%;transform:translateY(-50%);width:580px">'
                f'<div class="kt" style="font-family:var(--serif);font-size:90px;font-weight:600;color:#fff;line-height:1.04">{titre}</div>{extra}</div>')
    def chiffres(bg, kick, titre, cells, tc, role, vo, src, voile=None):
        tiles = ''.join(f'<div class="kv"><b>{a}</b><span>{nb(b)}</span></div>' for a, b in cells)
        left = (f'<div style="position:absolute;inset:0;background:url({bg}) center/cover"></div>' + (voile or VOILE) + FIL4 +
                colonne(kick, titre) + f'<div class="kvg">{tiles}</div>')
        out.append(page(left, nxt(), tc, role, vo,
                        "À gauche, le titre en grand. À droite, les quatre chiffres tombent l'un sous l'autre et défilent jusqu'à leur valeur.", src))

    # Ouverture
    left = (f'<div style="position:absolute;inset:0;background:url({photo("bannieres/clean/c4.jpg")}) center/cover"></div>' + SCRIM + FILET +
            '<div style="position:absolute;left:110px;top:50%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:84px;font-weight:600;line-height:1.02;color:#fff">Promotion<br>2026</div>'
            '<div style="font-family:var(--serif);font-size:46px;font-weight:500;color:#5fd0ea;margin-top:24px">GRE · CCE</div></div>'
            '<div style="position:absolute;left:720px;top:50%;transform:translateY(-50%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:120px;font-weight:600;line-height:1.0;color:#fff">L\'expérience<br>d\'upskilling,<br><em style="color:#5fd0ea">en chiffres</em></div></div>')
    out.append(page(left, nxt(), 'En chiffres · ouverture', 'L\'expérience en chiffres',
                    "« Sept mois de parcours. Voici ce qu'ils ont produit. »",
                    "À gauche, « Promotion 2026 · GRE · CCE ». À droite, le titre, ligne par ligne.",
                    "Bannière de la compétence 2.1"))

    chiffres(photo('bannieres/clean/c1.jpg'), 'Le parcours', 'Sept mois,<br><em style="color:#5fd0ea">du premier<br>cours au terrain</em>',
             [('30', 'participants, GRE et CCE'), ('9', 'cours en ligne : 8 compétences, 3 blocs'),
              ('7', 'mois de parcours, d\'avril à novembre'), ('2', 'jours de bootcamp d\'origination')],
             'En chiffres · le parcours', 'Le parcours',
             "« Trente banquiers, neuf cours, sept mois, et deux jours de bootcamp pour finir. »",
             "Programme du parcours, plateforme Thinkific")

    # La plateforme : la vraie page d'accueil dans un cadre de navigateur, et les chiffres à droite
    shot = photo('plateforme.jpg')
    rows = ''.join(f'<div class="pk"><b>{a}</b><span>{nb(b)}</span></div>' for a, b in
                   [('215', 'capsules vidéo réparties dans les 9 cours'), ('6\u202f450', 'capsules terminées : 100 % du programme suivi'),
                    ('800', 'heures de formation en ligne'), ('27 h', 'par participant en moyenne')])
    # La plateforme, écran dédié : la vraie page d'accueil en grand
    left = ('<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 40%,#1b3a66 0%,#0b1a33 60%,#060f20 100%)"></div>'
            '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:1680px;border-radius:16px;overflow:hidden;box-shadow:0 50px 120px rgba(0,0,0,.6);background:#fff">'
            '<div style="height:64px;background:#e9ecf1;display:flex;align-items:center;gap:12px;padding:0 26px">'
            '<i style="width:16px;height:16px;border-radius:50%;background:#ff5f57"></i><i style="width:16px;height:16px;border-radius:50%;background:#febc2e"></i><i style="width:16px;height:16px;border-radius:50%;background:#28c840"></i>'
            '<div style="margin-left:30px;flex:1;height:42px;border-radius:21px;background:#fff;display:flex;align-items:center;padding-left:26px;font-size:28px;color:#1d3350;font-weight:500">🔒&nbsp; banking.xelanc.com</div></div>'
            f'<div style="height:880px;background:url({shot}) top center/cover"></div></div>')
    out.append(page(left, nxt(), 'En chiffres · la plateforme', 'banking.xelanc.com',
                    "« Tout le parcours en ligne passe par une plateforme dédiée : banking.xelanc.com. »",
                    "La page d'accueil de la plateforme, en grand, dans un navigateur. L'adresse s'inscrit dans la barre, puis légère avancée de caméra.",
                    "banking.xelanc.com"))

    # La plateforme, ses chiffres : même mise en page que les autres écrans
    chiffres(shot.replace('url(', 'url(') , 'La plateforme', 'Une école<br><em style="color:#5fd0ea">ouverte<br>en continu</em>',
             [('215', 'capsules vidéo réparties dans les 9 cours'), ('6\u202f450', 'capsules terminées : 100 % du programme suivi'),
              ('800', 'heures de formation en ligne'), ('27 h', 'par participant en moyenne')],
             'En chiffres · la plateforme', 'La plateforme en chiffres',
             "« Deux cent quinze capsules, huit cents heures de formation, et cent pour cent du programme suivi. »",
             "Plateforme Thinkific",
             voile='<div style="position:absolute;inset:0;background:url(' + shot + ') 100% 55%/230% auto"></div><div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,15,32,.85) 0%,rgba(6,15,32,.55) 40%,rgba(6,15,32,.30) 100%)"></div>')

    chiffres(photo('cas/terralis.jpg'), 'La preuve', 'Personne<br>n\'est <em style="color:#5fd0ea">resté<br>en route</em>',
             [('100\u202f%', 'des cours terminés : 270 sur 270'), ('30\u202f/\u202f30', 'participants ont terminé les 9 cours'),
              ('9', 'épreuves de validation'), ('6', 'études de cas sur des entreprises réelles')],
             'En chiffres · la preuve', 'La preuve',
             "« Cent pour cent des cours terminés. Neuf épreuves, six études de cas réelles. »",
             "Plateforme Thinkific, rapports d'évaluation 04a à 04i")

    chiffres(photo('cas/maghreb.jpg'), 'Le terrain', 'Des<br>compétences<br><em style="color:#5fd0ea">mises au travail</em>',
             [('424', 'entreprises repérées et notées'), ('145', 'fiches prospect rédigées'),
              ('72', 'prospects validés pour la soutenance'), ('30\u202f/\u202f30', 'participants ont remis leurs travaux')],
             'En chiffres · le terrain', 'Le terrain',
             "« Quatre cent vingt-quatre entreprises repérées. Soixante-douze prospects prêts à être défendus. »",
             "Revue des travaux d'origination")

    # Entrée dans le programme, juste avant les trois blocs
    left = (f'<div style="position:absolute;inset:0;background:url({photo("bannieres/clean/c5.jpg")}) center/cover"></div>' + SCRIM + FILET +
            '<div class="ktop">Le programme</div>'
            '<div style="position:absolute;left:110px;top:54%;transform:translateY(-50%);width:470px">'
            '<div style="font-family:var(--serif);font-size:84px;font-weight:600;line-height:1.04;color:#fff">Entrons<br>dans le<br>programme</div></div>'
            '<div style="position:absolute;left:720px;top:54%;transform:translateY(-50%);width:1100px">'
            '<div style="font-family:var(--serif);font-size:104px;font-weight:500;line-height:1.04;color:#fff">Trois blocs,<br><em style="color:#5fd0ea">huit compétences,</em><br>une action terrain.</div></div>')
    out.append(page(left, nxt(), 'Entrée dans le programme', 'Entrons dans le programme',
                    "« Voici comment ces chiffres ont été construits, bloc par bloc. »",
                    "À gauche, « Entrons dans le programme ». À droite, les trois lignes tombent l'une après l'autre.",
                    "Bannière de la compétence 2.2"))

    return STYLE + ''.join(out), n[0]
