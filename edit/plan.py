# -*- coding: utf-8 -*-
"""Plan de montage vertical 9:16 — « salaire trauma ».
Genere l'EDL complet et valide les contraintes de rythme."""
import json, sys

TOTAL   = 182.70          # duree visuelle (l'audio fait 182.658 s, intact)
SCENES  = [0.6, 31.4, 51.0, 78.2, 93.4, 109.8, 131.0, 157.2, 181.2]

# --- Cadrages avatar (source 1920x1080, visage x~745, haut du crane y~95) ---
AV_FRAMING = {
    "large": (608, 1080, 441,  0),
    "moyen": (520,  924, 485, 22),
    "serre": (440,  782, 525, 46),
}
# --- Cadrages B-roll (source 1280x720) -----------------------------------
# La cinematique graines raconte une progression : semis (0-4 s) -> pousse
# (5-10 s). Chaque fragment prend un moment ET un cadrage differents.
BR_FRAMING = {
    "mains_semis":  (405, 720, 180,   0),
    "graine_pres":  (405, 720, 600,   0),
    "sol_chaud":    (405, 720, 780,   0),
    "pousse_jeune": (340, 604, 470, 110),
    "pousse":       (405, 720, 450,   0),
    "pousse_macro": (300, 533, 500,  80),
    "pousse_large": (405, 720, 520,   0),
    "lion_loin":    (405, 720, 250,   0),
    "lion_face":    (405, 720, 690,   0),
    "lion_yeux":    (286, 508, 760,  40),
    "lion_marche":  (405, 720, 430,   0),
}

# Beats : (kind, duree, param)
#   av    -> plan avatar (cadrage/zoom assignes automatiquement)
#   br    -> (clip, cadrage, t_in source)
#   card  -> id du carton
BEATS = [
    # ---------- S1 : 0.0 -> 31.4  « le hook / la prison des 30 jours » ----------
    ("av",   4.4, None),
    ("card", 2.4, "C1"),
    ("av",   4.2, None),
    ("br",   2.6, ("graines", "mains_semis",  1.0)),
    ("av",   4.0, None),
    ("av",   3.4, None),
    ("br",   2.8, ("graines", "graine_pres",  3.4)),
    ("av",   2.8, None),
    ("av",   4.8, None),
    # ---------- S2 : 31.4 -> 51.0  « c'est un systeme » ----------
    ("av",   2.2, None),
    ("card", 2.4, "C2"),
    ("av",   4.4, None),
    ("br",   2.6, ("graines", "sol_chaud",    4.6)),
    ("av",   4.2, None),
    ("av",   3.8, None),
    # ---------- S3 : 51.0 -> 78.2  « je suis venu en fuyant » ----------
    ("av",   2.6, None),
    ("card", 2.4, "C3"),
    ("av",   4.4, None),
    ("av",   4.2, None),
    ("br",   2.6, ("lion",    "lion_loin",    0.2)),
    ("av",   4.6, None),
    ("av",   3.2, None),
    ("br",   2.8, ("graines", "pousse_jeune", 6.0)),
    # ---------- S4 : 78.2 -> 93.4  « une autre facon de gagner » ----------
    ("av",   4.4, None),
    ("av",   3.6, None),
    ("br",   2.6, ("graines", "pousse",       6.9)),
    ("av",   4.6, None),
    # ---------- S5 : 93.4 -> 109.8  « le resultat inattendu » ----------
    ("card", 2.4, "C4"),
    ("av",   4.2, None),
    ("av",   4.4, None),
    ("br",   2.6, ("graines", "pousse_macro", 7.4)),
    ("av",   2.8, None),
    # ---------- S6 : 109.8 -> 131.0  « la porte de sortie » ----------
    ("card", 2.4, "C5"),
    ("av",   4.6, None),
    ("av",   3.8, None),
    ("br",   2.8, ("lion",    "lion_face",    2.2)),
    ("av",   4.4, None),
    ("av",   3.2, None),
    # ---------- S7 : 131.0 -> 157.2  « regles, pratiques, valeurs » ----------
    ("card", 2.2, "C6"),
    ("av",   4.6, None),
    ("av",   4.4, None),
    ("av",   3.8, None),
    ("br",   2.6, ("graines", "pousse_large", 7.0)),
    ("av",   4.8, None),
    ("av",   3.8, None),
    # ---------- S8 : 157.2 -> 181.2  « la prison ou le lion ? » ----------
    ("av",   4.2, None),
    ("br",   2.6, ("lion",    "lion_yeux",    2.5)),
    ("av",   4.4, None),
    ("av",   3.6, None),
    ("br",   2.8, ("lion",    "lion_marche",  2.45)),
    ("av",   3.4, None),
    ("av",   3.4, None),
    # ---------- Outro ----------
    ("card", 1.5, "C7"),
]

# --- Assignation automatique cadrage / zoom des plans avatar ---------------
FRAME_CYCLE = ["serre", "large", "moyen", "large", "serre", "moyen"]

def build():
    segs, t, fi, last_frame, last_zoom = [], 0.0, 0, None, None
    for kind, dur, param in BEATS:
        s = {"start": round(t, 3), "dur": dur, "end": round(t + dur, 3), "kind": kind}
        if kind == "av":
            # cadrage : jamais deux fois le meme d'affilee
            while FRAME_CYCLE[fi % len(FRAME_CYCLE)] == last_frame:
                fi += 1
            frame = FRAME_CYCLE[fi % len(FRAME_CYCLE)]
            fi += 1
            # zoom : strictement alterne avant / arriere
            zoom = "out" if last_zoom == "in" else "in"
            s.update(framing=frame, zoom=zoom, crop=AV_FRAMING[frame])
            last_frame, last_zoom = frame, zoom
        elif kind == "br":
            clip, frame, tin = param
            s.update(clip=clip, framing=frame, src_in=tin, crop=BR_FRAMING[frame],
                     zoom="in" if len(segs) % 2 == 0 else "out")
        else:
            s.update(card=param)
        segs.append(s)
        t += dur
    return segs, t

def validate(segs, total):
    errs, warns = [], []
    if abs(total - TOTAL) > 0.001:
        errs.append(f"duree totale {total:.3f} != {TOTAL}")
    # cartons <= 2.5 s
    for s in segs:
        if s["kind"] == "card" and s["dur"] > 2.5:
            errs.append(f"carton {s['card']} dure {s['dur']}s > 2.5s")
    # aucun plan > 5 s  (changement visuel toutes les 3-5 s)
    for s in segs:
        if s["dur"] > 5.0:
            errs.append(f"segment @{s['start']}s dure {s['dur']}s > 5s")
    # zoom alterne sur les plans avatar
    zs = [s["zoom"] for s in segs if s["kind"] == "av"]
    for a, b in zip(zs, zs[1:]):
        if a == b:
            errs.append("deux zooms identiques consecutifs")
    # cadrage avatar jamais repete d'affilee
    fs = [s["framing"] for s in segs if s["kind"] == "av"]
    for a, b in zip(fs, fs[1:]):
        if a == b:
            errs.append(f"cadrage {a} repete d'affilee")
    # coupe proche de chaque frontiere de scene
    cuts = [s["start"] for s in segs] + [total]
    for b in SCENES:
        if min(abs(c - b) for c in cuts) > 2.6:
            warns.append(f"frontiere de scene {b}s sans coupe proche")
    return errs, warns

if __name__ == "__main__":
    segs, total = build()
    errs, warns = validate(segs, total)
    n_av = sum(1 for s in segs if s["kind"] == "av")
    n_br = sum(1 for s in segs if s["kind"] == "br")
    n_cd = sum(1 for s in segs if s["kind"] == "card")
    print(f"{len(segs)} segments — {n_av} avatar / {n_br} b-roll / {n_cd} cartons")
    print(f"duree visuelle : {total:.3f}s   plan le plus long : {max(s['dur'] for s in segs)}s")
    print(f"duree moyenne d'un plan : {total/len(segs):.2f}s")
    for w in warns: print("  [warn]", w)
    for e in errs:  print("  [ERREUR]", e)
    if errs: sys.exit(1)
    json.dump(segs, open("/home/user/xelanc/edit/build/edl.json", "w"), indent=1)
    print("OK -> build/edl.json")
