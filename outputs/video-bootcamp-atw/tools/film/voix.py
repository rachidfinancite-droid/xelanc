"""Prépare les passages audio des capsules (un par bloc et un pour l'origination) et voix.json pour le moteur.
Sources : versions légères Wistia téléchargées dans le dossier de travail (caps/v)."""
import json, os, subprocess, sys
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
CAPS = sys.argv[1]                       # dossier caps (vidéos sources)
PLAN = json.load(open(sys.argv[2]))      # plan.json (pour trouver les écrans)
OUT = os.path.join(RACINE, 'film', 'voix'); os.makedirs(OUT, exist_ok=True)
# écran (début de tc), fichier source, morceaux, sous-titres (temps source)
V = [
    ('Bloc 01 · ouverture', 'bloc1-coherences', '01', [(166.4, 181.3)], [
        (166.4, 170.7, "Ce que nous finançons, ce ne sont pas vraiment les entreprises."),
        (170.7, 173.8, "Ce que nous finançons, ce sont des cohérences."),
        (173.8, 181.3, "Des cohérences entre un secteur, un modèle qui fonctionne\net une exécution crédible.")]),
    ('Bloc 02 · ouverture', 'bloc2-business-plan', 'bp05', [(76.9, 77.75), (80.6, 85.82)], [
        (76.9, 77.75, "Les banquiers méritent"),
        (80.6, 85.82, "de recevoir un business plan\nà la hauteur des engagements qu'on leur demande.")]),
    ('Bloc 03 · ouverture', 'bloc3-erreur-evitee', '14', [(170.2, 171.55), (172.55, 180.45)], [
        (170.2, 171.55, "Parce que vous savez,"),
        (172.55, 175.1, "les dirigeants oublient beaucoup de choses,"),
        (175.1, 180.45, "mais ils n'oublient jamais le banquier\nqui leur a évité une erreur.")]),
    ('Action terrain · ouverture', 'origination-confrere', '09', [(118.4, 130.35)], [
        (118.4, 122.1, "Et rappelez-vous ce qui se joue de l'autre côté du silence."),
        (122.1, 127.8, "L'entreprise que vous n'osez pas appeler aujourd'hui,\nun confrère l'appellera peut-être demain."),
        (127.8, 130.35, "Le potentiel ne vous attend pas.")]),
]
voix = {}
for tc, nom, src, parts, subs in V:
    k = next(s['k'] for s in PLAN['plan'] if s['tc'].startswith(tc))
    f = os.path.join(OUT, nom + '.wav')
    n = len(parts)
    fc = ''.join(f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS[a{i}];' for i, (a, b) in enumerate(parts))
    fc += ''.join(f'[a{i}]' for i in range(n)) + f'concat=n={n}:v=0:a=1,afade=t=in:d=0.05,areverse,afade=t=in:d=0.15,areverse,loudnorm=I=-16:TP=-2:LRA=7[o]'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', os.path.join(CAPS, 'v', src + '.mp4'), '-filter_complex', fc,
                    '-map', '[o]', '-ac', '1', '-ar', '48000', f], check=True)
    def rel(t):
        acc = 0
        for a, b in parts:
            if a - 0.01 <= t <= b + 0.01: return acc + t - a
            acc += b - a
        return acc
    duree = sum(b - a for a, b in parts)
    voix[str(k)] = dict(fichier=nom + '.wav', duree=round(duree, 2), debut=1.5,
                        subs=[[round(rel(a), 2), round(rel(b), 2), t] for a, b, t in subs])
    print(k, tc, nom, round(duree, 1), 's')
json.dump(voix, open(os.path.join(ICI, 'voix.json'), 'w'), ensure_ascii=False, indent=1)
