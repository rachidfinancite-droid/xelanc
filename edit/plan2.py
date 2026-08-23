# -*- coding: utf-8 -*-
"""Plan de montage v2 — chaque illustration est ancree sur CE QUI EST DIT
a cet instant precis (transcription Descript), plus sur le rythme."""
import json, sys

TOTAL  = 182.70
SCENES = [0.6, 31.4, 51.0, 78.2, 93.4, 109.8, 131.0, 157.2, 181.2]
AV_MAX = 4.7          # temps maximum ou Rachid reste seul a l'ecran

# ("av", duree) | ("il", duree, id_illustration, ce_qui_est_dit)
BEATS = [
 # ---------- S1 : la prison des 30 jours ----------
 ("av", 4.0),
 ("il", 3.0, "I01", "شحال مليون فالشهر باش تعيش مرتاح؟"),
 ("av", 2.6),
 ("il", 3.6, "I02", "خمس أيام — les 5 jours ou tu vis"),
 ("av", 2.8),
 ("il", 3.4, "I03", "٢٥ يوم الأخرى تبقى تنتظر"),
 ("av", 2.6),
 ("il", 3.2, "I04", "تنتظر الـ virement"),
 ("av", 2.4),
 ("il", 3.8, "I05", "هذا حبس ٣٠ يوم"),
 # ---------- S2 : c'est un systeme ----------
 ("av", 3.2),
 ("il", 3.0, "I06", "هذا نظام"),
 ("av", 3.0),
 ("il", 3.4, "I07", "عاجبه / كاره / ولف"),
 ("av", 3.2),
 ("il", 3.8, "I08", "داير ليا واحد traumatism"),
 # ---------- S3 : je suis venu en fuyant ----------
 ("av", 3.4),
 ("il", 3.2, "I09", "ما جيتش باش ننجح"),
 ("av", 3.4),
 ("il", 3.8, "I10", "جيت هارب من salary"),
 ("av", 2.8),
 ("il", 3.0, "I11", "ما بغيتش نبقى نتسنى"),
 ("av", 2.8),
 ("il", 3.2, "I12", "salary كل ٣٠ يوم"),
 ("av", 1.6),
 # ---------- S4 : une autre facon de gagner ----------
 ("av", 3.0),
 ("il", 3.4, "I13", "une autre façon de gagner"),
 ("av", 2.8),
 ("il", 3.0, "I14", "مرة كل semaine"),
 ("il", 3.0, "I15", "ولا مرة كل ساعة"),
 # ---------- S5 : le resultat inattendu ----------
 ("av", 3.2),
 ("il", 3.0, "I16", "النتيجة ما كنتش نتوقعها"),
 ("av", 2.8),
 ("il", 3.6, "I17", "ناعس وكتدخل الفلوس"),
 ("il", 3.8, "I18", "تفيق وتشوف شحال دخل"),
 # ---------- S6 : la porte de sortie ----------
 ("av", 3.2),
 ("il", 3.0, "I19", "المقاولة ماشي موضة ولا حلم"),
 ("av", 2.4),
 ("il", 3.8, "I20", "الباب ديال الخروج"),
 ("av", 2.8),
 ("il", 3.2, "I21", "نتحرك / نخدم / نتقرازل"),
 ("av", 2.8),
 # ---------- S7 : regles, pratiques, valeurs ----------
 ("il", 4.0, "I22", "وهاد الطريق"),
 ("av", 2.8),
 ("il", 4.6, "I23", "قواعد / ممارسات / قيم / أعراف"),
 ("av", 2.8),
 ("il", 4.6, "I24", "خلصت عليهم الثمن غالي"),
 ("av", 2.8),
 ("il", 4.6, "I25", "نلخص عليك الطريق"),
 # ---------- S8 : la prison ou le lion ----------
 ("av", 3.2),
 ("il", 3.6, "I26", "واش نتا فشي حبس تعجبك؟"),
 ("av", 2.6),
 ("il", 3.8, "I27", "ولا باغي تولي سبع؟"),
 ("av", 2.8),
 ("il", 3.2, "I28", "السبع كيجيب الفلوس من فم السباع"),
 ("av", 2.2),
 ("il", 4.1, "I29", "الحبس ولا السبع؟"),
]

FRAME_CYCLE = ["serre", "large", "moyen", "large", "serre", "moyen"]
AV_FRAMING  = {"large": (608, 1080, 441, 0),
               "moyen": (520,  924, 485, 22),
               "serre": (440,  782, 525, 46)}


def build():
    segs, t, fi, lf, lz = [], 0.0, 0, None, None
    for b in BEATS:
        kind, dur = b[0], b[1]
        s = {"start": round(t, 3), "dur": dur, "end": round(t + dur, 3), "kind": kind}
        if kind == "av":
            while FRAME_CYCLE[fi % len(FRAME_CYCLE)] == lf:
                fi += 1
            lf = FRAME_CYCLE[fi % len(FRAME_CYCLE)]; fi += 1
            lz = "out" if lz == "in" else "in"
            s.update(framing=lf, zoom=lz, crop=AV_FRAMING[lf])
        else:
            s.update(illus=b[2], dit=b[3])
        segs.append(s); t += dur
    return segs, t


def validate(segs, total):
    err, warn = [], []
    if abs(total - TOTAL) > 0.001:
        err.append(f"duree {total:.3f} != {TOTAL}")
    # Rachid ne reste jamais seul a l'ecran plus de AV_MAX
    run, runs = 0.0, []
    for s in segs:
        if s["kind"] == "av":
            run += s["dur"]
        elif run:
            runs.append(run); run = 0.0
    if run: runs.append(run)
    for r in runs:
        if r > AV_MAX + 1e-6:
            err.append(f"plage avatar continue de {r:.1f}s > {AV_MAX}s")
    # alternance zoom / cadrage
    zs = [s["zoom"] for s in segs if s["kind"] == "av"]
    fs = [s["framing"] for s in segs if s["kind"] == "av"]
    if any(a == b for a, b in zip(zs, zs[1:])): err.append("zoom repete")
    if any(a == b for a, b in zip(fs, fs[1:])): err.append("cadrage repete")
    # une illustration par idee, sans doublon
    ids = [s["illus"] for s in segs if s["kind"] == "il"]
    if len(ids) != len(set(ids)): err.append("illustration reutilisee")
    for s in segs:
        if s["dur"] > 5.0: err.append(f"plan de {s['dur']}s > 5s")
    cuts = [s["start"] for s in segs] + [total]
    for b in SCENES:
        if min(abs(c - b) for c in cuts) > 2.8:
            warn.append(f"frontiere {b}s sans coupe proche")
    return err, warn, runs


if __name__ == "__main__":
    segs, total = build()
    err, warn, runs = validate(segs, total)
    av = sum(s["dur"] for s in segs if s["kind"] == "av")
    il = sum(s["dur"] for s in segs if s["kind"] == "il")
    n_il = sum(1 for s in segs if s["kind"] == "il")
    print(f"{len(segs)} plans — {len(segs)-n_il} avatar / {n_il} illustrations")
    print(f"duree            : {total:.3f}s")
    print(f"Rachid a l'image : {av:6.1f}s  {av/total*100:4.1f} %   (etait 75,3 %)")
    print(f"illustrations    : {il:6.1f}s  {il/total*100:4.1f} %   (etait 16,1 %)")
    print(f"plage avatar la plus longue : {max(runs):.1f}s  (etait 12,8 s)")
    print(f"duree moyenne d'un plan     : {total/len(segs):.2f}s")
    for w in warn: print("  [warn]", w)
    for e in err:  print("  [ERREUR]", e)
    if err: sys.exit(1)
    json.dump(segs, open("/home/user/xelanc/edit/build/edl2.json", "w"),
              ensure_ascii=False, indent=1)
    print("OK -> build/edl2.json")
