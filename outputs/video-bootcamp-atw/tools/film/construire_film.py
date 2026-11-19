"""Construit film.html à partir des planches validées : mêmes écrans, plus le moteur d'animation."""
import json, os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
voix = json.load(open(os.path.join(ICI, 'voix.json'))) if os.path.exists(os.path.join(ICI, 'voix.json')) else {}
s = open(os.path.join(RACINE, 'planches-artifact.html')).read()
css = """<style>
html,body{margin:0;padding:0!important;background:#060f20;overflow:hidden}
section.page{display:none!important}
#stage{position:fixed;left:0;top:0;width:1920px;height:1080px;overflow:hidden;background:#060f20}
#stage .fr{will-change:transform,opacity}
#noir{position:fixed;left:0;top:0;width:1920px;height:1080px;background:#000;opacity:0;pointer-events:none;z-index:10}
</style>"""
js = open(os.path.join(ICI, 'moteur.js')).read()
s = s.replace('</head>', css + '</head>', 1) if '</head>' in s else css + s
s += f'\n<div id="noir"></div>\n<script>window.FILM_VOIX={json.dumps(voix)};</script>\n<script>{js}</script>\n'
open(os.path.join(RACINE, 'film', 'film.html'), 'w').write(s)
print('film.html', len(s) // 1024, 'Ko')
