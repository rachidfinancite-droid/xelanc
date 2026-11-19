#!/bin/bash
# Rendu complet du film : capture en deux moitiés parallèles, bande son, encodage H.264 1080p30.
# Usage : rendre.sh <dossier travail> <fichier sortie mp4>
set -e
ICI="$(cd "$(dirname "$0")" && pwd)"
W="$1"; OUT="$2"
rm -rf "$W/h1" "$W/h2"; mkdir -p "$W"
node "$ICI/capturer.js" "$W/h1" 0 150 30 > "$W/h1.log" 2>&1 &
node "$ICI/capturer.js" "$W/h2" 150 9999 30 > "$W/h2.log" 2>&1 &
wait
DUREE=$(python3 -c "import json;print(json.load(open('$W/h1/plan.json'))['duree'])")
OUTRO="$ICI/../../film/outro/outro-financite.mp4"
OD=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUTRO")
XF=1.5   # fondu enchaîné du maillon ultime vers l'outro
TOTAL=$(python3 -c "print($DUREE + $OD - $XF)")
python3 "$ICI/son.py" "$W/h1/plan.json" "$W/son.wav" 0 "$TOTAL"
ffmpeg -loglevel error -y -framerate 30 -i "$W/h1/f_%05d.jpg" -c:v libx264 -pix_fmt yuv420p -crf 17 -preset medium "$W/v1.mp4"
ffmpeg -loglevel error -y -framerate 30 -i "$W/h2/f_%05d.jpg" -c:v libx264 -pix_fmt yuv420p -crf 17 -preset medium "$W/v2.mp4"
printf "file '%s'\nfile '%s'\n" "$W/v1.mp4" "$W/v2.mp4" > "$W/l.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/l.txt" -c copy "$W/v.mp4"
# film + outro Financité : image seule (sans sa musique), en fondu enchaîné ; la bande son du film continue dessous
OFF=$(python3 -c "print($DUREE - $XF)")
ffmpeg -loglevel error -y -i "$W/v.mp4" -i "$OUTRO" -i "$W/son.wav" -filter_complex \
  "[0:v]fps=30,format=yuv420p,setsar=1,settb=AVTB[v0];[1:v]fps=30,scale=1920:1080:flags=lanczos,format=yuv420p,setsar=1,settb=AVTB[v1];[v0][v1]xfade=transition=fade:duration=$XF:offset=$OFF[v]" \
  -map "[v]" -map 2:a -c:v libx264 -pix_fmt yuv420p -b:v 6M -maxrate 8M -bufsize 12M -preset medium -c:a aac -b:a 256k -ar 48000 -movflags +faststart -shortest "$OUT"
ffmpeg -loglevel error -y -i "$OUT" -vf scale=1280:-2 -c:v libx264 -b:v 1500k -maxrate 2M -bufsize 3M -preset medium -c:a aac -b:a 160k -movflags +faststart "${OUT%.mp4}-apercu.mp4"
echo "fini $OUT"
