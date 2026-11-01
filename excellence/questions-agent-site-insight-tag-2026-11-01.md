# Questions pour l'Agent Site Xelanc 2 · Insight Tag LinkedIn · 01/11/2026

À coller dans la conversation de l'Agent Site Xelanc 2. Demander de répondre point par point, en un seul message, à la session « Agent LinkedIn publicitaire » (session_01LXovPUQ1heLhxL4NB3fmzY) ou dans un fichier du dépôt. Pas de mise en ligne : préparer et tester ; l'activation attend le « go » de Rachid.
Contexte : branche `claude/create-finance-header-011CUrWto3dADFdQWirH88L1`, fichier `excellence/linkedin-insight-tag-architecture-2026-11-01.md`. Compte publicitaire LinkedIn : 382016523 (EUR).

## A. Accès LinkedIn
1. Accès à Campaign Manager (compte 382016523) ? Si oui : Partner ID de l'Insight Tag (Analyser > Balise Insight), état de la balise, domaines déclarés.

## B. École LearnWorlds
2. URL exacte de l'école. Sous-domaine de xelanc.org ou domaine séparé ? L'école Financité Institute Academy (financite-institute-academy.com) est-elle aussi sur LearnWorlds ?
3. Le plan autorise-t-il du code personnalisé dans l'en-tête ? Une intégration native LinkedIn Insight Tag existe-t-elle ? Où se règle-t-elle ?
4. Quel bandeau de consentement l'école affiche-t-elle ? Hors Europe, la mesure démarre-t-elle dès l'arrivée comme sur xelanc.org ?

## C. WordPress xelanc.org
5. Comment sont gérés les snippets (plugin, numérotation) ? Où sont ceux de Clarity et de Meta ? Peux-tu créer un snippet « LinkedIn Insight Tag » sur le modèle de Clarity (code dans mon fichier, remplacer PARTNER_ID), le tester en préproduction ou en mode interne, et dire ce que tu vois ?
6. Bandeau cookies et politique de confidentialité : proposer le texte pour ajouter LinkedIn à « La mesure de nos publicités » (aujourd'hui : Meta seul). Où se modifie-t-il ?

## D. Conversions à déclarer
7. Inscription gratuite : où se confirme la création du compte (code qui appelle Brevo avant la redirection sur /inscription/) ? URL de redirection ensuite ? Peut-on y déclencher `lintrk('track',{conversion_id:ID})` ?
8. Achat : URL type de la page « commande reçue » WooCommerce, variable de valeur (montant en euros) disponible ?
9. /equipes/ : le formulaire de devis déclenche-t-il un événement ? URL de confirmation ?
10. Diagnostic de carrière (/carrieres/#orientation) : événement de fin disponible ?
11. LearnWorlds : motif d'URL ou événement pour « première capsule regardée » et « compte créé dans l'école » ?

## E. Attribution des pubs
12. UTM LinkedIn prévues : `?utm_source=linkedin&utm_medium=paid&utm_campaign=...&utm_content=...`. Sont-elles conservées jusqu'au compte créé et à la commande (cookies `xl_src`, `xl_or`, attribution WooCommerce) ? L'agent Meta 2 signale qu'il n'y a « pas de moyen fiable de relier un compte créé à sa pub » : qu'est-ce qui manque, et comment éviter le même trou pour LinkedIn ?

## F. Pages de destination
13. Quelle page comme destination des pubs LinkedIn (accueil, /certificats/, page d'un parcours) ? Où en sont les landing pages « univers » banque et finance d'entreprise (erreur 404 le 31/10) ? Date prévue ?
14. Le site tient-il 100 à 500 visites par jour venant de LinkedIn (vitesse mobile, cache) ?

## G. Planning
15. Quand l'Insight Tag peut-il être posé et testé sur les deux sites ? Blocages ?
