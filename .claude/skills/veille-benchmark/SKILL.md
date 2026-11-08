---
name: veille-benchmark
description: Veille & Benchmark de Xelanc (projet Excellence) — surveillance quotidienne de la stratégie sociale des concurrents (créateurs finance/Excel/IA et grandes plateformes de formation). Méthode commune à tous les agents veille-* et au chef d'orchestre. Use quand Rachid parle de veille, benchmark, concurrents, radar, « que fait Nicolas Boucher / CFI / Bojan / Coursera… », « point veille », « quoi de neuf chez les concurrents », ou s'adresse au chef d'orchestre de la veille.
---

# Veille & Benchmark — méthode commune

## Organisation

- **Rachid** ne parle qu'au **chef d'orchestre** (la conversation principale « Veille & Benchmark »).
- Le chef d'orchestre lance les agents `veille-*`, recoupe leurs remontées et rend la synthèse.
- Chaque agent surveille **une seule cible** et tient **son radar** : `excellence/veille/<slug>-radar.yaml`.
- Le chef tient `excellence/veille/veille-state.yaml` (calendrier, derniers passages, synthèses, décisions).
- La liste des cibles, leurs comptes et leur rythme : `references/cibles.md`.

| Rythme | Cibles |
|---|---|
| **Quotidien** | Les 7 créateurs + CFI |
| **Hebdomadaire** (après un diagnostic initial complet) | Plateformes : Domestika, Udemy, Coursera, Coursiv |

## La question que pose chaque agent

**Qu'est-ce que ma cible a fait depuis le dernier passage, qu'est-ce que ça révèle de sa stratégie,
et qu'est-ce que Xelanc doit en faire ?**

## Sources, par ordre de priorité

1. **Chrome de Rachid (Claude in Chrome)** — source principale. On va directement sur les comptes :
   profil et onglet « Activité / Posts » LinkedIn, page Facebook, Instagram, YouTube (onglet Vidéos et Shorts),
   X, TikTok, site, page de prix, newsletter, **Bibliothèque publicitaire Meta** (facebook.com/ads/library)
   et **Bibliothèque publicitaire LinkedIn** (linkedin.com/ad-library).
2. **Web public** (WebSearch, Firecrawl) — pages de prix, landing pages, presse, podcasts, archives de newsletter.
3. **Ce que Rachid colle** (captures, emails reçus) — à intégrer tel quel, étiqueté [R].

Si Chrome n'est pas connecté : le dire **en tête de rapport**, faire le passage en web public seul,
et marquer les champs non vérifiables `a_verifier_chrome`.

## Protocole Chrome (règles strictes)

1. Charger les outils `mcp__claude-in-chrome__*` en un seul ToolSearch (voir skill `anthropic-skills:chrome-browser`),
   appeler `tabs_context_mcp`, ouvrir **un nouvel onglet**, le fermer en fin de passage.
2. **Lecture seule, rythme humain.** Jamais de like, commentaire, abonnement, message, inscription,
   connexion/invitation, ni clic sur un bouton d'achat. On ne télécharge rien qui demande un email
   sauf accord de Rachid (on peut s'inscrire aux newsletters avec une adresse dédiée s'il l'a fournie).
3. Limiter le volume : au plus ~15 pages par cible et par passage ; ne pas faire défiler sans fin.
   Le compte LinkedIn de Rachid doit rester à l'abri de toute restriction pour activité automatisée.
4. En cas de mur de connexion, de captcha, de refus de site ou d'erreur 2-3 fois de suite : arrêter,
   le noter dans le radar (`acces`), passer à la source suivante.
5. Ne relever que du **public** et du **professionnel** : pas de vie privée, pas de données personnelles
   de commentateurs (on compte les commentaires, on résume leur tonalité, on ne nomme pas les gens).

## Grille de relevé — créateur (quotidien)

Pour chaque publication depuis le dernier passage :
`date, reseau, format (texte/carrousel/vidéo/short/live/newsletter/doc), sujet, accroche (1re ligne),
appel à l'action, lien/offre poussée, réactions, commentaires, partages/vues si visibles, langue`.

Puis :
- **Offres** : produits, prix, promos, nouvelles formations, cohortes, webinaires, lead magnets.
- **Publicité** : annonces actives (Meta/LinkedIn Ad Library) — nombre, angle, visuel, destination.
- **Audience** : abonnés par réseau (relevé hebdomadaire suffit, le lundi).
- **Signaux** : changement de positionnement, nouveau thème IA, partenariat, recrutement, collaboration.

## Grille — diagnostic plateforme (initial, puis hebdomadaire)

Diagnostic initial (une fois, complet) : **type de présence** par réseau (comptes, fréquence, formats,
ton), **type de public** (B2C / B2B / entreprises, pays, langues, niveau), **offre** (catalogue
finance/Excel/IA, abonnement vs à l'unité, prix, essai gratuit), **acquisition** (pub, SEO, affiliés,
influence, emailing), **place de l'IA**, **promesse principale**, **forces / failles exploitables par Xelanc**.
Passage hebdomadaire : uniquement les **écarts** par rapport au diagnostic.

## Étiquetage

[C] vu dans Chrome · [W] web public · [R] fourni par Rachid · [E] estimation de l'agent · [H] hypothèse.
Toute métrique sans source visible est [E] ou [H]. Ne jamais inventer un chiffre.

## Format de sortie d'un agent (court)

```
# Radar <cible> — <date> — source : Chrome | web seul
1. Nouveau depuis le dernier passage (3 à 7 puces, chacune étiquetée)
2. Ce qui marche chez eux (meilleur post du passage + pourquoi)
3. Offre / prix / pub : changements
4. Lecture stratégique (2-3 phrases)
5. À faire pour Xelanc (1 à 3 actions concrètes, avec à qui la passer : GTM, Launch, LinkedIn Ads, Tête Grise)
6. Rien de nouveau ? -> écrire « RAS » et s'arrêter là.
```
Puis mettre à jour le radar YAML (ajouter le passage dans `journal`, mettre à jour `profil`, `offres`,
`meilleurs_posts`, `dernier_passage`) et écrire le rapport dans `excellence/veille/rapports/<date>-<slug>.md`.

## Rôle du chef d'orchestre

1. Lire `veille-state.yaml`, lancer les agents dus ce jour (en parallèle, en arrière-plan).
2. Recouper : tendances communes (format qui monte, thème IA, prix), mouvement d'un acteur qui touche Xelanc.
3. Rendre à Rachid :
   - **Point quotidien** (10 lignes max) : les 3 mouvements qui comptent + 1 action recommandée.
   - **Bilan hebdomadaire** (lundi) : tableau comparatif, tendances, idées de contenus à reprendre, menaces.
4. Écrire la synthèse dans `excellence/veille/rapports/<date>-synthese.md` et mettre à jour `veille-state.yaml`.
5. Relayer une consigne de Rachid à un agent : la noter dans `consignes` du radar concerné, l'agent l'applique au passage suivant.
