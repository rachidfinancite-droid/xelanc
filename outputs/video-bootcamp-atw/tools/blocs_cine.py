"""Mise en scène cinématographique des blocs : ouverture, promesse, une compétence par écran
(bannière en plein écran, textes posés dedans), validation, résultats."""

ACCROCHE = {
    '01': ("Avant de financer,<br><em>comprendre.</em>",
           "Lire le secteur, le business model, les chiffres et le cadre juridique : une entreprise se comprend avant de se financer."),
    '02': ("De l'analyse<br>à la <em>décision.</em>",
           "Un avis argumenté, chiffré, défendable en comité : c'est là que se joue la qualité d'un engagement."),
    '03': ("Gagner le client,<br><em>le garder.</em>",
           "Challenger un projet, aller chercher l'entreprise au bon moment, devenir son partenaire de référence."),
}
VO_OBJ = {'01': "Tout commence par la compréhension.", '02': "Puis vient le moment de trancher.", '03': "Et enfin, la relation."}

VALID = {
    '01': dict(n=4, exams=[("Lecture 360°<br>et business model", "73", "76"), ("Analyse financière<br>orientée risque", "81", "83"),
                           ("Lecture juridique<br>et fiscale", "84", "97")]),
    '02': dict(n=2, exams=[("Analyse financière<br>de crédit", "98", "100")]),
    '03': dict(n=3, exams=[("Traitement<br>des objections", "90", "87")]),
}

RESULT = {
    '01': ("Une promotion qui monte en puissance.",
           [("97 %", "de certifiés au troisième examen, contre 76 % au premier"),
            ("90 %", "certifiés sur La Table de l'Atlas"),
            ("84/100", "meilleure moyenne : juridique et fiscal")]),
    '02': ("Le cœur du métier, maîtrisé.",
           [("98/100", "moyenne au quiz de certification"),
            ("100 %", "de certifiés au quiz"),
            ("88 %", "franchissent ACHAPOST, le palier le plus exigeant")]),
    '03': ("Les épreuves les plus dures, les mieux réussies.",
           [("100 %", "de certifiés sur TERRALIS et sur AZURA"),
            ("81/100", "AZURA : la meilleure moyenne des cas de synthèse"),
            ("28 / 28", "apprenants évalués sur AZURA, tous certifiés")]),
}

ECRAN_DESC = {
    'c1': "Lire le secteur et le business model avant les chiffres.",
    'c2': "Qualifier un dossier, mesurer le risque réel, défendre sa position en comité.",
    'c3': "Les signaux que les chiffres cachent : structure, garanties, fiscalité.",
    'c4': "Les défaillances que les bilans rentables cachent. Un DCR juste, sur les vrais cashflows.",
    'c5': "Crédit moyen terme, leasing, investissement : le bon financement, au rythme du projet.",
    'c6': "Structurer le projet, poser les hypothèses, bâtir des prévisions cohérentes.",
    'c7': "Cibler les entreprises à potentiel, construire une vraie raison de les appeler.",
    'c8': "Partir du besoin du client, jamais du produit, et piloter la relation dans la durée.",
}

STYLE = """<style>
.kick{font-size:24px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:#c8a96a}
.acc{font-family:var(--serif);font-size:150px;font-weight:500;line-height:1.02;color:#fff}.acc em{color:#c8a96a}
.cp{flex:1;border-top:2px solid rgba(200,169,106,.6);padding-top:16px;font-size:26px;line-height:1.3;color:#dbe3ee}
.cp span{display:block;font-family:var(--serif);font-size:34px;color:#c8a96a}
.ex{border-left:3px solid #c8a96a;padding:6px 0 6px 26px;font-family:var(--serif);font-size:44px;color:#fff;line-height:1.1}
.ex span{display:block;font-family:var(--sans);font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:#9db6d6;margin-bottom:6px}
.cs{border-left:3px solid #e8798c;padding:6px 0 6px 26px}
.cs span{display:block;font-size:20px;letter-spacing:.24em;text-transform:uppercase;color:#e8798c}
.cs b{display:block;font-family:var(--serif);font-size:72px;font-weight:600;color:#fff;line-height:1;margin-top:8px}
.cs i{display:block;font-style:normal;font-size:26px;line-height:1.35;color:#c9d6e6;margin-top:12px}
.cs3{display:flex;gap:46px;margin-top:16px}.cs3 div{font-size:20px;color:#9db6d6}
.cs3 strong{display:block;font-family:var(--serif);font-size:52px;font-weight:600;color:#fff;line-height:1}
.vx{background:#fff;border-radius:22px;box-shadow:0 12px 28px rgba(15,39,68,.16);padding:34px 36px;display:flex;flex-direction:column}
.vx span{font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:#6f8198}.vx b{font-family:var(--serif);font-size:44px;font-weight:600;color:#0f2744;line-height:1.1;margin-top:12px;min-height:98px}
.vr{border-top:2px solid #e3e5e8;margin-top:22px;padding-top:18px}.vr strong{font-family:var(--serif);font-size:72px;font-weight:600;color:#0f2744;line-height:1}.vr em{font-style:normal;font-size:28px;color:#6f8198;margin-left:6px}.vr i{display:block;font-style:normal;font-size:24px;color:#3f5168;margin-top:6px}
.vs{background:#0f2744;border-radius:22px;box-shadow:0 14px 30px rgba(15,39,68,.25);padding:40px 46px;display:flex;align-items:center;gap:50px}
.vs span{font-size:20px;letter-spacing:.22em;text-transform:uppercase;color:#c8a96a}.vs b{display:block;font-family:var(--serif);font-size:70px;font-weight:600;color:#fff;line-height:1;margin-top:10px}.vs i{display:block;font-style:normal;font-size:27px;line-height:1.35;color:#c9d6e6;margin-top:14px}
.vsn{flex:none;text-align:right}.vsn strong{font-family:var(--serif);font-size:110px;font-weight:600;color:#fff;line-height:1}.vsn em{font-style:normal;font-size:34px;color:#9db6d6;margin-left:6px}.vsn i{display:block;font-style:normal;font-size:24px;color:#c8a96a;margin-top:8px}
.rs{border-top:2px solid #c8a96a;padding-top:28px}
.rs b{display:block;font-family:var(--serif);font-size:110px;font-weight:500;color:#fff;line-height:1;white-space:nowrap}
.rs span{display:block;font-size:30px;line-height:1.35;color:#c9d6e6;margin-top:20px}
</style>"""


def make(blocs, banner, nb, start, clean_banner):
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
    for b in blocs:
        k = b['num']
        first = banner(b['cours'][0]['id'])
        acc, sous = ACCROCHE[k]

        # 1. Ouverture : la première bannière du bloc, floutée et assombrie, et le nom du bloc
        left = (f'<div style="position:absolute;inset:-40px;background:url({first}) center/cover;filter:blur(14px) brightness(.38) saturate(.6)"></div>'
                '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(6,16,34,.92) 0%,rgba(6,16,34,.55) 60%,rgba(6,16,34,.3) 100%)"></div>'
                '<div style="position:absolute;left:130px;top:250px;width:1500px">'
                f'<div class="kick">Bloc {k} &nbsp;·&nbsp; {b["periode"]}</div>'
                f'<div style="font-family:var(--serif);font-size:230px;font-weight:500;line-height:.95;color:#fff;margin-top:30px">{b["nom"]}</div>'
                '<div style="width:120px;height:3px;background:#c8a96a;margin-top:50px"></div>'
                f'<div style="font-family:var(--serif);font-style:italic;font-size:54px;color:#d9e2ee;margin-top:36px">{nb(b["sous"])}</div></div>')
        out.append(page(left, nxt(), f'Bloc {k} · ouverture', b['nom'], 'Aucune. Montée musicale.',
                        "La première bannière du bloc, floutée et assombrie, sert de décor. Le nom du bloc apparaît, puis le filet doré se trace.",
                        'Bannière de la plateforme'))

        # 2. La promesse du bloc
        comps = ''.join(f'<div class="cp"><span>{c["num"]}</span>{nb(c["titre"].split(" :")[0])}</div>' for c in b['cours'])
        left = ('<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 30%,#173158 0%,#0b1a33 60%,#060f20 100%)"></div>'
                '<div style="position:absolute;left:130px;top:150px" class="kick">L\'objectif</div>'
                f'<div class="acc" style="position:absolute;left:130px;top:240px;width:1650px">{acc}</div>'
                f'<div style="position:absolute;left:130px;top:640px;width:1100px;font-size:34px;line-height:1.45;color:#c9d6e6">{nb(sous)}</div>'
                f'<div style="position:absolute;left:130px;top:860px;width:1660px;display:flex;gap:56px">{comps}</div>')
        out.append(page(left, nxt(), f'Bloc {k} · objectif', 'La promesse du bloc', f'« {VO_OBJ[k]} »',
                        "La phrase s'écrit mot à mot, le mot en italique doré arrive en dernier. Les compétences du bloc s'alignent en bas.",
                        b['obj_src']))

        # 3. Une compétence par écran : la bannière en plein écran (sans son texte incrusté),
        #    le titre complet en un seul bloc, puis l'objectif en sous-titre.
        for c in b['cours']:
            img = clean_banner(c['id'])
            veil = ('<div style="position:absolute;inset:0;background:linear-gradient(90deg,#0b1a33 0%,#0b1a33 66%,rgba(11,26,51,.6) 74%,rgba(11,26,51,0) 86%)"></div>'
                    if c['id'] in ('c6', 'c7', 'c8') else
                    '<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,26,51,.6) 0%,rgba(11,26,51,0) 60%)"></div>')
            left = (f'<img src="{img}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">{veil}'
                    '<div style="position:absolute;left:120px;top:50%;transform:translateY(-50%);width:900px">'
                    f'<div class="kick">Compétence {c["num"]}</div>'
                    f'<div style="font-family:var(--serif);font-size:74px;font-weight:600;line-height:1.06;color:#fff;margin-top:26px">{nb(c["ecran_titre"])}</div>'
                    '<div style="width:110px;height:3px;background:#c8a96a;margin:42px 0 36px"></div>'
                    f'<div style="font-family:var(--serif);font-style:italic;font-size:48px;line-height:1.2;color:#e9eef5">{nb(c["objectif"])}</div></div>')
            out.append(page(left, nxt(), f'Bloc {k} · compétence {c["num"]}', c['titre'].split(' :')[0],
                            "À écrire au montage, sans reprendre le texte de l'écran.",
                            "La bannière entre en plein écran avec un lent zoom avant. Le titre monte en un seul bloc, le filet doré se trace, puis l'objectif s'écrit en italique.",
                            'Bannière : plateforme banking.xelanc.com'))

        # 4. La validation, sur fond gris : les examens côte à côte, puis le ou les cas de synthèse à part
        v = VALID[k]
        ne = len(v['exams'])
        cw = 520 if ne == 3 else 620
        exams = ''.join(
            f'<div class="vx" style="width:{cw}px"><span>Examen {i + 1}</span><b>{e[0]}</b>'
            f'<div class="vr"><strong>{e[1]}</strong><em>/100</em><i>{e[2]}&nbsp;% de certifiés</i></div></div>'
            for i, e in enumerate(v['exams']))
        nc = len(b['cas'])
        sw = 1680 if nc == 1 else 820
        cases = ''.join(
            f'<div class="vs" style="width:{sw}px"><div style="flex:1;min-width:0"><span>{nb(cs["type"])}</span><b>{nb(cs["nom"])}</b>'
            f'<i>{nb(cs["quoi_court"])}</i></div>'
            f'<div class="vsn"><strong>{cs["moy"]}</strong><em>/100</em><i>{cs["cert"]}&nbsp;% de certifiés</i></div></div>' for cs in b['cas'])
        pl = 's' if v['n'] > 1 else ''
        left = ('<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 28% 18%,#f7f7f6 0%,#ececeb 45%,#dedfe0 100%)"></div>'
                '<div style="position:absolute;left:120px;top:80px"><div class="sur">La validation · bloc ' + k + '</div>'
                f'<div style="font-family:var(--serif);font-size:72px;font-weight:600;color:#0f2744;line-height:1.05;margin-top:12px">{v["n"]} épreuve{pl} de validation</div></div>'
                f'<div style="position:absolute;left:120px;top:250px;display:flex;gap:60px">{exams}</div>'
                f'<div style="position:absolute;left:120px;top:{730 if nc == 1 else 720}px;display:flex;gap:40px">{cases}</div>')
        out.append(page(left, nxt(), f'Bloc {k} · validation', 'Prouver, pas déclarer',
                        "« Chaque compétence passe une épreuve. Et le bloc se ferme sur un dossier réel, sans mode d'emploi. »",
                        "Les cartes des examens arrivent l'une après l'autre, leur note défile en bas. Puis le bloc du cas de synthèse se pose, avec sa note.",
                        "Rapports à l'Académie, 22/10/2026"))

        # 5. Résultats : les chiffres qui vendent
        titre, stats = RESULT[k]
        st = ''.join(f'<div class="rs"><b>{nb(x)}</b><span>{nb(y)}</span></div>' for x, y in stats)
        left = ('<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 30% 80%,#173158 0%,#0b1a33 55%,#060f20 100%)"></div>'
                f'<div style="position:absolute;left:130px;top:140px" class="kick">Les résultats · bloc {k}</div>'
                f'<div style="position:absolute;left:130px;top:220px;width:1650px;font-family:var(--serif);font-size:96px;font-weight:500;line-height:1.05;color:#fff">{nb(titre)}</div>'
                f'<div style="position:absolute;left:130px;top:560px;width:1660px;display:grid;grid-template-columns:repeat(3,1fr);gap:60px">{st}</div>'
                '<div style="position:absolute;left:130px;top:975px;font-size:20px;color:#6f8198">Seuils de certification : 70/100 pour les examens (80 % pour la prospection), 60/100 pour les cas de synthèse.</div>')
        out.append(page(left, nxt(), f'Bloc {k} · résultats', 'Le chiffre qui reste', '« Et la promotion a tenu la barre. »',
                        "Le titre, puis les trois chiffres qui défilent jusqu'à leur valeur, l'un après l'autre.",
                        'Évaluation globale du programme, 22/10/2026'))
    return STYLE + ''.join(out), n[0]
