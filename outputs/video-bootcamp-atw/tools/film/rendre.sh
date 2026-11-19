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
# film + outro Financité (logo animé, « Accompagner votre réussite »)
OUTRO="$ICI/../../film/outro/outro-financite.mp4"
ffmpeg -loglevel error -y -i "$W/v.mp4" -i "$W/son.wav" -i "$OUTRO" -filter_complex \
  "[0:v]fps=30,format=yuv420p,setsar=1[v0];[2:v]fps=30,scale=1920:1080,format=yuv420p,setsar=1[v1];[1:a]aformat=sample_rates=48000:channel_layouts=stereo[a0];[2:a]aformat=sample_rates=48000:channel_layouts=stereo[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" \
  -map "[v]" -map "[a]" -c:v libx264 -pix_fmt yuv420p -b:v 6M -maxrate 8M -bufsize 12M -preset medium -c:a aac -b:a 256k -ar 48000 -movflags +faststart "$OUT"
ffmpeg -loglevel error -y -i "$OUT" -vf scale=1280:-2 -c:v libx264 -b:v 1500k -maxrate 2M -bufsize 3M -preset medium -c:a aac -b:a 160k -movflags +faststart "${OUT%.mp4}-apercu.mp4"
echo "fini $OUT"
