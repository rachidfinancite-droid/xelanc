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
    '01': dict(n=4, detail="3 examens de compétence<br>et 1 cas de synthèse",
               exams=["Lecture 360° et business model", "Analyse financière orientée risque", "Lecture juridique et fiscale"]),
    '02': dict(n=2, detail="1 quiz de certification<br>et 1 cas de synthèse", exams=["Analyse financière de crédit"]),
    '03': dict(n=3, detail="1 examen de compétence<br>et 2 cas de synthèse", exams=["Traitement des objections"]),
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
.rs{border-top:2px solid #c8a96a;padding-top:28px}
.rs b{display:block;font-family:var(--serif);font-size:110px;font-weight:500;color:#fff;line-height:1;white-space:nowrap}
.rs span{display:block;font-size:30px;line-height:1.35;color:#c9d6e6;margin-top:20px}
</style>"""


def make(blocs, banner, nb, start):
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

        # 3. Une compétence par écran : la bannière en plein écran, nos textes posés dedans
        for c in b['cours']:
            img = banner(c['id'])
            left = (f'<img src="{img}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover">'
                    '<div style="position:absolute;inset:0;background:linear-gradient(0deg,rgba(6,16,34,.95) 0%,rgba(6,16,34,.75) 20%,rgba(6,16,34,0) 42%)"></div>'
                    f'<div style="position:absolute;left:105px;top:70px" class="kick">Compétence {c["num"]}</div>'
                    '<div style="position:absolute;left:105px;top:845px;width:1700px">'
                    f'<div style="font-size:31px;line-height:1.35;color:#e6edf6">{nb(ECRAN_DESC[c["id"]])}</div>'
                    '<div style="display:flex;align-items:baseline;gap:22px;margin-top:22px">'
                    '<span style="width:56px;height:3px;background:#c8a96a;display:inline-block;transform:translateY(-10px)"></span>'
                    f'<span style="font-family:var(--serif);font-style:italic;font-size:44px;color:#fff">{nb(c["objectif"])}</span></div></div>')
            out.append(page(left, nxt(), f'Bloc {k} · compétence {c["num"]}', c['titre'].split(' :')[0],
                            "À écrire au montage, sans reprendre le texte de l'écran.",
                            "La bannière entre en plein écran avec un lent zoom avant. Le descriptif monte en bas, puis l'objectif s'écrit en italique.",
                            'Bannière et descriptif : plateforme banking.xelanc.com'))

        # 4. La validation : combien d'épreuves, lesquelles
        v = VALID[k]
        exams = ''.join(f'<div class="ex"><span>Examen</span>{nb(e)}</div>' for e in v['exams'])
        cases = ''.join(
            f'<div class="cs"><span>{nb(cs["type"])}</span><b>{nb(cs["nom"])}</b><i>{nb(cs["quoi"])}</i>'
            f'<div class="cs3"><div><strong>{cs["comp"]}</strong>compétences</div><div><strong>{cs["moy"]}</strong>sur 100</div>'
            f'<div><strong>{cs["cert"]}&nbsp;%</strong>certifiés</div></div></div>' for cs in b['cas'])
        pl = 's' if v['n'] > 1 else ''
        left = ('<div style="position:absolute;inset:0;background:linear-gradient(135deg,#060f20 0%,#0f2744 100%)"></div>'
                '<div style="position:absolute;left:130px;top:120px;width:560px"><div class="kick">La validation</div>'
                f'<div style="font-family:var(--serif);font-size:360px;font-weight:500;color:#fff;line-height:.9;margin-top:20px">{v["n"]}</div>'
                f'<div style="font-family:var(--serif);font-size:58px;color:#fff;line-height:1.05">épreuve{pl}<br>de validation</div>'
                f'<div style="font-size:28px;color:#9db6d6;margin-top:26px;line-height:1.35">{v["detail"]}</div></div>'
                f'<div style="position:absolute;left:780px;top:130px;width:1030px;display:flex;flex-direction:column;gap:24px">{exams}{cases}</div>')
        out.append(page(left, nxt(), f'Bloc {k} · validation', 'Prouver, pas déclarer',
                        "« Chaque compétence passe une épreuve. Et le bloc se ferme sur un dossier réel, sans mode d'emploi. »",
                        "Le chiffre géant compte jusqu'au nombre d'épreuves. Puis les examens, puis le cas de synthèse comme un titre de film.",
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
