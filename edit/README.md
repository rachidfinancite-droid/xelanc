# Montage vertical 9:16 — « salaire trauma »

Chaîne de montage FFmpeg + Pillow, entièrement locale (aucun crédit externe consommé).

## Sources
| Élément | Origine | Durée |
|---|---|---|
| Avatar HeyGen (voix ElevenLabs) | vidéo `91c32cab4b7a432d94decdbb0fb6795b` | 182,648 s |
| Cinématique graines | CloudFront Higgsfield | 10,04 s |
| Cinématique lion | CloudFront Higgsfield | 5,04 s |
| Transcription horodatée | projet Descript `852f094e…` export SRT | 39 blocs |

## Pipeline
1. `plan.py` — construit l'EDL (`build/edl.json`) et **valide** les contraintes
   de rythme : aucun plan > 5 s, cartons ≤ 2,5 s, zooms strictement alternés,
   cadrage avatar jamais répété deux fois de suite, coupe à chaque frontière de scène.
2. `textes.py` — rend les mots-clés et les cartons en **Noto Naskh Arabic** via
   Pillow `direction="rtl", language="ar"` (Raqm/HarfBuzz). Pas de `arabic_reshaper`.
3. `rendu.py` — rend les 53 segments en 1080×1920 : recadrage centré sur le visage,
   zoom lent ancré sur le regard, B-roll ralenti 24→30 fps, cartons animés.
4. `assemblage.py` — concatène, incruste les 13 mots-clés calés sur le SRT,
   puis **recopie l'audio de l'avatar sans réencodage ni coupe**.

## Charte
navy `#1E2A3B` · crème `#EFE7D8` · or `#B89554`

## Relancer
```sh
python3 plan.py && python3 textes.py && python3 rendu.py && python3 assemblage.py
```

## Résultat livré

`salaire-trauma-vertical.mp4` — 1080×1920, 30 fps, H.264, 182,73 s.

| Contrainte demandée | Résultat |
|---|---|
| Changement visuel toutes les 3–5 s | 53 plans, moyenne **3,45 s**, le plus long **4,8 s** |
| Zoom lent alterné avant/arrière | 35 plans avatar, alternance `IOIOIO…` sans répétition |
| Alternance large / serré | large ×12, moyen ×11, serré ×12, jamais deux fois de suite |
| Mots-clés arabes animés | 13, calés au SRT, tiers inférieur (ne couvrent jamais le visage) |
| Cartons pleins écran ≤ 2,5 s | 7 cartons, max **2,4 s** |
| Cinématiques refragmentées | 11 fragments, **11 cadrages distincts**, exposition relevée |
| Recadrage 9:16 visage bien placé | crop centré x=745, zoom ancré sur le regard |
| Audio avatar intact | **empreinte PCM identique à la source, bit à bit** |
