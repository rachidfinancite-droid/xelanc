# Méthode d'animation à appliquer au film GRE · CCE

Reçue de la session « Vidéo promotionnelle finance », à la demande de Rachid (19/11/2026).
Référence : vidéo XELANC LinkedIn 16:9 « La finance avance vite » (https://youtu.be/r8zF7CZ9yNY, 70 s).
Consigne : garder le contenu des planches (textes, images, plans) ; n'appliquer que l'animation, la musique, le son et le rythme.

## Principe
- Pas de voix off : la musique rythme, une idée par plan, chaque ligne frappe sur un temps.
- Trois couches : fond (images étalonnées sombres, teintées navy) ; surcouche HTML animée image par image (`window.renderAt(t)`), capturée à 30 i/s sur fond transparent (ProRes 4444) ; son (musique + percussions calées sur les frappes), mixé à −14 LUFS.
- Sortie : 1920×1080, 30 i/s, H.264 ~3 Mb/s, AAC 256 kb/s.

## Animation (grille de 0,5 s, 120 BPM, ease = 1 − (1 − x)³)
- ROLL : chaque ligne arrive en 0,2 s (rotateX −95° → 0, translateY 55 % → 0, flou 10 px → 0), rebond amorti exp(−14t)·sin(40t)·6 %. Une ligne par temps (1 s pour la conclusion). Sortie inverse en 0,18 s.
- SLAM : 0,18 s, échelle 1,3 → 1, tremblement ±6 px pendant 0,12 s. Moments forts uniquement (logos, chiffres clés).
- FLASH : voile blanc 35 % en mode écran, 0,22 s, sur les plans de rupture.
- BURST : éclat radial + onde en anneau #9cc4ff, 0,7–0,9 s, sous le logo uniquement.
- RISE : +40 px en 0,4 s pour les éléments secondaires. SWP : balayage horizontal +700 px → 0.
- CAM : zoom 1 → 1,05 sur le plan final, fondu au noir 1,9 s.
- Les instants `data-at` des `.slam` et `.roll` pilotent la génération du son.

## Fond
- Étalonnage commun : `eq=brightness=-0.07:saturation=0.72:contrast=1.06,colorbalance=bs=0.09:bm=0.05:rs=-0.05:rm=-0.03`, cadrage 1920×1080 en gardant les visages.
- Coupes sur les temps de la musique.

## Musique et son
- Morceau cinématographique 120 BPM avec montée et fin naturelle ; allonger en rejouant des mesures entières (fondu 0,12 s).
- Slam : kick de synthèse 120 → 50 Hz, 0,3 s + craquement de bruit blanc. Roll : souffle montant 0,22 s + kick léger.
- Logo : riser 3 s, puis boum grave ; musique à 20 % la seconde qui précède le premier logo.
- Fin : la musique continue et s'éteint sous le logo (fondu 2,5 s), un seul coup au logo final.
- Mix : musique + percussions à 62 % → `loudnorm I=-14:TP=-1.5:LRA=11`, 48 kHz.

## Façon de travailler
- Une version numérotée par série de retours, sans écraser les précédentes, historique des retours en tête de script.
- Planche d'images clés à valider avant chaque rendu complet.

## Points à trancher pour ce film (charte et format différents de la pub LinkedIn)
- Durée : la pub fait 70 s ; le storyboard compte 36 écrans.
- Typographie : la méthode utilise Montserrat 800 et des textes géants ; les planches validées utilisent Newsreader + DM Sans. Par défaut, on garde la charte des planches et on n'emprunte que le mouvement.
- Voix off : la méthode n'en a pas ; les planches ont une colonne « Voix off » qui peut devenir des textes à l'écran.
