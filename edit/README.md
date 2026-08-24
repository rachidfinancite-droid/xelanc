# Montage vertical 9:16 — « salaire trauma »

Chaîne de montage **100 % locale** (FFmpeg + Pillow + Chromium). Aucun crédit externe consommé.

## Sources
| Élément | Origine | Durée |
|---|---|---|
| Avatar HeyGen (voix ElevenLabs) | vidéo `91c32cab4b7a432d94decdbb0fb6795b` | 182,648 s |
| Transcription horodatée | projet Descript `852f094e…`, export SRT | 39 blocs |

Les deux cinématiques Higgsfield (graines, lion) ont été **écartées** : 15 s de matière ne
peuvent pas illustrer 8 scènes, et leur contenu ne correspondait pas au propos.
Les visuels sont désormais **29 illustrations construites sur mesure**, une par idée.

## Pipeline
1. `plan2.py` — construit l'EDL (`build/edl2.json`) et **valide** :
   Rachid jamais plus de 4,7 s d'affilée à l'écran, aucun plan > 5 s,
   zooms strictement alternés, cadrage jamais répété, une illustration par idée.
2. `illus/scenes.py` + `illus/base.py` — les 29 illustrations en HTML/CSS animé.
   Textes **en français**, chiffres latins. Charte navy `#132338` sur fond
   `#0B1524`, gris argenté `#AEBBC9`, blanc pur. Typographie **Inter**,
   embarquée en base64 (`fonts_inline.py`) : aucun accès réseau au rendu.
   Composition **alignée à gauche** — le centrage systématique était ce qui
   donnait au montage son air de diapositive générique.
3. `illus/rendu_illus.py` — Chromium piloté **image par image** : toutes les animations
   sont mises en pause puis leur `currentTime` est forcé à la milliseconde voulue.
   Le rendu est déterministe, indépendant de la vitesse machine.
4. `illus/overlays.py` — les mots-clés incrustés sur le visage, en séquences PNG RGBA.
   Chaque mot est placé à l'intersection entre le moment où il est **prononcé** (SRT)
   et un plan avatar.
5. `rendu2.py` — plans avatar : recadrage 9:16 centré sur le visage (x=745),
   zoom lent ancré sur le regard, et **correction du calage labial** : au temps
   *t* de la timeline, l'image du visage est prise au temps *t − 120 ms* de la
   source (`AVANCE_LEVRES`). Les lèvres de l'avatar HeyGen bougent avant le son ;
   corriger côté image plutôt que côté audio laisse la piste intacte et les
   illustrations calées.
6. `assemblage2.py` — concat, incrustation, puis **recopie de l'audio sans réencodage**.

## Résultat

`salaire-trauma-vertical.mp4` — 1080×1920, 30 fps, H.264, 182,73 s.

| | v1 | v2 |
|---|---|---|
| Rachid à l'image | 75,3 % | **43,8 %** |
| Illustrations | 16,1 % | **56,2 %** |
| Plage la plus longue sans illustration | 12,8 s | **4,6 s** |
| Plages > 5 s | 13 | **0** |
| Visuels distincts | 3 | **30** |
| Illustrations calées sur le propos | 1 / 11 | **29 / 29** |

Audio avatar : **empreinte PCM identique à la source, bit à bit** — vérifiée à chaque assemblage.

## Relancer
```sh
python3 plan2.py && python3 illus/rendu_illus.py && python3 rendu2.py \
  && python3 illus/overlays.py && python3 assemblage2.py
```
