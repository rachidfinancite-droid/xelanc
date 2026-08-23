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
