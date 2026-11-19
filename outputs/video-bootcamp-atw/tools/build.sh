#!/usr/bin/env bash
# Reconstruit la vidéo : rendu des images puis assemblage avec la musique.
set -euo pipefail
D="$(cd "$(dirname "$0")/.." && pwd)"
F="$(mktemp -d)"
node "$D/tools/render.js" "$F"
ffmpeg -loglevel error -y -framerate 25 -i "$F/f%05d.jpg" -i "$D/assets/musique.m4a" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart \
  "$D/recap-bootcamp-GRE-CCE.mp4"
rm -rf "$F"
echo "OK : $D/recap-bootcamp-GRE-CCE.mp4"
