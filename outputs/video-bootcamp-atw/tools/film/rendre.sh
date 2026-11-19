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
python3 "$ICI/son.py" "$W/h1/plan.json" "$W/son.wav" 0 "$DUREE"
ffmpeg -loglevel error -y -framerate 30 -i "$W/h1/f_%05d.jpg" -c:v libx264 -pix_fmt yuv420p -crf 17 -preset medium "$W/v1.mp4"
ffmpeg -loglevel error -y -framerate 30 -i "$W/h2/f_%05d.jpg" -c:v libx264 -pix_fmt yuv420p -crf 17 -preset medium "$W/v2.mp4"
printf "file '%s'\nfile '%s'\n" "$W/v1.mp4" "$W/v2.mp4" > "$W/l.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/l.txt" -c copy "$W/v.mp4"
ffmpeg -loglevel error -y -i "$W/v.mp4" -i "$W/son.wav" -map 0:v -map 1:a -c:v libx264 -pix_fmt yuv420p -b:v 6M -maxrate 8M -bufsize 12M -preset medium -c:a aac -b:a 256k -ar 48000 -movflags +faststart -shortest "$OUT"
echo "fini $OUT"
