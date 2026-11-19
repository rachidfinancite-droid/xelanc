"""Version 2 des extraits : élargis, 4 remplacé, sous-titres incrustés (DM Sans, bandeau navy)."""
import os, subprocess
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, 'ext2'); os.makedirs(OUT, exist_ok=True)
# nom, capsule, morceaux [(début, fin)] dans la source, sous-titres [(début source, fin source, texte)]
CLIPS = [
    ('1-lecture360-coherences', '01', [(166.4, 180.5)], [
        (166.5, 170.7, "Ce que nous finançons, ce ne sont pas vraiment les entreprises."),
        (170.7, 173.8, "Ce que nous finançons, ce sont des cohérences."),
        (173.8, 180.5, "Des cohérences entre un secteur, un modèle qui fonctionne\net une exécution crédible.")]),
    ('2-lecture360-anticipez', '02', [(149.3, 159.0)], [
        (149.3, 153.6, "Laissez-moi vous donner une recommandation :\nsi vous voulez être un banquier excellent,"),
        (153.6, 159.0, "ne vous contentez pas d'analyser. Anticipez.")]),
    ('3-juridique-riche-pauvre', '05', [(118.6, 125.4)], [
        (118.6, 121.5, "Le résultat nous dit que l'entreprise est riche,"),
        (121.5, 125.4, "mais le compte bancaire nous montre\nque l'entreprise est pauvre.")]),
    ('4-prospection-meriter-le-temps', '10', [(176.9, 191.9)], [
        (176.9, 180.5, "On ne vous accorde pas du temps parce que vous en demandez,"),
        (180.5, 184.1, "mais parce que vous méritez qu'on vous en accorde."),
        (184.1, 191.9, "Et cette légitimité-là, personne ne vous la donne :\nvous la construisez par votre posture.")]),
    ('5-prospection-confrere-demain', '09', [(118.4, 130.0)], [
        (118.4, 122.1, "Et rappelez-vous ce qui se joue de l'autre côté du silence."),
        (122.1, 127.8, "L'entreprise que vous n'osez pas appeler aujourd'hui,\nun confrère l'appellera peut-être demain."),
        (127.8, 130.0, "Le potentiel ne vous attend pas.")]),
    ('6-conseil-evite-une-erreur', '14', [(170.2, 171.55), (172.55, 179.9)], [
        (170.2, 171.55, "Parce que vous savez,"),
        (172.55, 175.1, "les dirigeants oublient beaucoup de choses,"),
        (175.1, 179.9, "mais ils n'oublient jamais le banquier\nqui leur a évité une erreur.")]),
]
HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: S,DM Sans 9pt,50,&H00FFFFFF,&H00FFFFFF,&H28331A0B,&H28331A0B,-1,0,0,0,100,100,0,0,3,22,0,2,120,120,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
for nom, cap, parts, subs in CLIPS:
    # temps de sortie : on enchaîne les morceaux
    def rel(t):
        acc = 0
        for a, b in parts:
            if a - 0.01 <= t <= b + 0.01:
                return acc + (t - a)
            acc += b - a
        return acc
    total = sum(b - a for a, b in parts)
    ass = HEAD + ''.join(f'Dialogue: 0,{ts(rel(a))},{ts(min(rel(b), total) - 0.02)},S,,0,0,0,,{t.replace(chr(10), chr(92) + "N")}\n' for a, b, t in subs)
    af = os.path.join(OUT, nom + '.ass'); open(af, 'w').write(ass)
    src = os.path.join(D, 'v', cap + '.mp4')
    n = len(parts)
    fc = ''.join(f'[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS[a{i}];' for i, (a, b) in enumerate(parts))
    fc += ''.join(f'[v{i}][a{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=1[vc][ac];'
    o = round(total - 0.25, 2)
    fc += f"[vc]fade=t=in:d=0.15,fade=t=out:st={o}:d=0.25,ass={af}:fontsdir={os.path.join(D, 'fonts')}[vo];[ac]afade=t=in:d=0.08,afade=t=out:st={o}:d=0.25[ao]"
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', src, '-filter_complex', fc, '-map', '[vo]', '-map', '[ao]',
                    '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
                    os.path.join(OUT, nom + '.mp4')], check=True)
    print(nom, round(total, 1), 's', flush=True)
lst = os.path.join(OUT, 'concat.txt')
open(lst, 'w').write(''.join(f"file '{c[0]}.mp4'\n" for c in CLIPS))
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', os.path.join(OUT, '0-les-6-extraits-a-la-suite.mp4')], check=True)
os.remove(lst)
