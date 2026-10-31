# Simulation InMail sur 30 jours · la machine qui se finance elle-même · 31/10/2026

Agent GTM, à la demande de Rachid. [H] hypothèse. Aucun de ces taux n'est encore mesuré.

## Les règles de la simulation (celles de Rachid)

- **22 jours ouvrés** : 30 jours sans les week-ends.
- **Jour 1 : 50 InMails**, envoyés à des personnes bien choisies. Ce socle de 50 envois par jour reste financé par Rachid, soit ≈ 21 € par jour (≈ 460 € sur le mois).
- **Chaque vente** : abonnement à 299 €, soit **287 € encaissés** après ≈ 4 % de frais de paiement.
- **La moitié de l'argent encaissé est réinjectée** dans le budget InMail.
- **Coût d'un envoi** : ≈ 0,45 $ (0,42 €) [E].
- **Délai de 2 jours ouvrés** entre la vente et l'argent disponible pour la pub. C'est le minimum réaliste pour les versements carte. Mobile Money peut demander plus.
- **Montée d'au plus +30 % par jour.** LinkedIn ne délivre pas un budget multiplié par 30 du jour au lendemain, et la qualité des cibles baisse si l'on élargit trop vite.

## Scénario A · le taux de Rachid, 10 % d'achat, constant tout le mois

| Semaine | Envois | Dépense pub | Ventes | Encaissé | Réinjecté (50 %) | Envois par jour en fin de semaine |
|---|---|---|---|---|---|---|
| S1 (J1-J5) | 358 | 150 € | 36 | 10 275 € | 2 368 € | 109 |
| S2 (J6-J10) | 1 269 | 533 € | 127 | 36 420 € | 10 820 € | 400 |
| S3 (J11-J15) | 4 698 | 1 973 € | 470 | 134 833 € | 39 922 € | 1 483 |
| S4 (J16-J20) | 17 421 | 7 317 € | 1 742 | 499 983 € | 147 977 € | 5 501 |
| S5 (J21-J22) | 16 447 | 6 908 € | 1 645 | 472 029 € | 139 669 € | 9 296 |

**Fin du mois** :
- ≈ 40 000 InMails envoyés pour ≈ 16 900 € de pub ;
- ≈ 4 000 ventes et ≈ 1,15 M€ encaissés ;
- budget du dernier jour : ≈ 9 300 envois, soit ≈ 3 900 € par jour.

## Scénario B · le même départ, mais le taux baisse quand on élargit les listes

On commence au taux de Rachid sur les meilleures cibles, puis le taux baisse :
- 10 % sur les 1 000 premiers envois ;
- 5 % jusqu'à 5 000 envois ;
- 2 % jusqu'à 20 000 envois ;
- 1 % au-delà.

| Semaine | Envois | Dépense pub | Ventes | Encaissé | Réinjecté (50 %) | Envois par jour en fin de semaine |
|---|---|---|---|---|---|---|
| S1 (J1-J5), taux 10→10 % | 358 | 150 € | 36 | 10 275 € | 2 368 € | 109 |
| S2 (J6-J10), taux 10→5 % | 1 269 | 533 € | 107 | 30 680 € | 10 820 € | 400 |
| S3 (J11-J15), taux 5→5 % | 4 698 | 1 973 € | 235 | 67 416 € | 22 171 € | 1 483 |
| S4 (J16-J20), taux 2→2 % | 17 421 | 7 317 € | 348 | 99 997 € | 40 892 € | 5 501 |
| S5 (J21-J22), taux 1→1 % | 16 447 | 6 908 € | 164 | 47 203 € | 27 934 € | 9 296 |

**Fin du mois** :
- ≈ 40 000 InMails envoyés pour ≈ 16 900 € de pub ;
- ≈ 890 ventes et ≈ 256 000 € encaissés ;
- taux de fin de mois : 1 %.

Pour mémoire, un taux de 1 % constant donne ≈ 400 ventes et ≈ 115 000 €. Un taux de 0,5 % constant donne ≈ 200 ventes et ≈ 58 000 €.

## Ce que la simulation apprend

1. **L'argent n'est jamais le frein.** La machine se finance seule dès que plus de 0,3 % des envois achètent. Une vente de 287 € dont on réinjecte la moitié paie ≈ 340 envois. À partir de la deuxième semaine, l'argent réinjecté s'accumule plus vite qu'on ne peut le dépenser : voir la colonne « réserve » des tableaux jour par jour.
2. **Le vrai plafond, c'est l'audience.**
   - 40 000 envois en un mois, c'est 25 à 70 % des DAF, RAF et dirigeants actifs sur LinkedIn dans nos 13 pays.
   - Une même personne ne peut recevoir qu'un InMail sponsorisé tous les 30 à 45 jours.
   - **Le mois 2 ne peut pas répéter le mois 1** : il faut de nouveaux pays, de nouveaux métiers ou de nouvelles listes.
3. **Le taux baissera quand on quittera les 1 000 premières cibles choisies à la main.** C'est l'écart entre les scénarios A et B : 1,15 M€ contre 256 000 €. Les deux premières semaines donnent la vérité. Si les 358 envois de la semaine 1 rapportent ≈ 36 ventes, Rachid avait raison. S'ils en rapportent 3 ou 4, on est à 1 %.
4. **Le deuxième plafond, c'est l'exécution.** À partir de la semaine 3, il y a 50 à 900 ventes par jour selon le scénario. Il faut :
   - un paiement en deux clics (carte, Mobile Money testé en réel, virement avec coordonnées) ;
   - une facture automatique au nom de l'entreprise ;
   - un accès ouvert immédiatement ;
   - une réponse aux questions dans la journée.
   Sinon, les ventes se perdent et la réputation s'abîme.
5. **La règle de pilotage.** On ne monte de +30 % que si le taux de la veille reste au-dessus du seuil fixé, par exemple 2 %. Sinon, on garde le budget et on change de message ou de cible.

## Annexe 1 · Scénario A jour par jour

| Jour | Envois | Dépense | Taux | Ventes | Encaissé | Réinjecté | Réserve non dépensée |
|---|---|---|---|---|---|---|---|
| J1 | 50 | 21 € | 10 % | 5.0 | 1 435 € | 0 € | 0 € |
| J2 | 50 | 21 € | 10 % | 5.0 | 1 435 € | 0 € | 0 € |
| J3 | 65 | 27 € | 10 % | 6.5 | 1 866 € | 718 € | 711 € |
| J4 | 84 | 35 € | 10 % | 8.4 | 2 411 € | 718 € | 1 414 € |
| J5 | 109 | 46 € | 10 % | 10.9 | 3 128 € | 933 € | 2 322 € |
| J6 | 141 | 59 € | 10 % | 14.1 | 4 047 € | 1 205 € | 3 490 € |
| J7 | 183 | 77 € | 10 % | 18.3 | 5 252 € | 1 564 € | 4 998 € |
| J8 | 237 | 100 € | 10 % | 23.7 | 6 802 € | 2 023 € | 6 943 € |
| J9 | 308 | 129 € | 10 % | 30.8 | 8 840 € | 2 626 € | 9 460 € |
| J10 | 400 | 168 € | 10 % | 40.0 | 11 480 € | 3 401 € | 12 714 € |
| J11 | 520 | 218 € | 10 % | 52.0 | 14 924 € | 4 420 € | 16 937 € |
| J12 | 676 | 284 € | 10 % | 67.6 | 19 401 € | 5 740 € | 22 414 € |
| J13 | 878 | 369 € | 10 % | 87.8 | 25 199 € | 7 462 € | 29 528 € |
| J14 | 1 141 | 479 € | 10 % | 114.1 | 32 747 € | 9 701 € | 38 770 € |
| J15 | 1 483 | 623 € | 10 % | 148.3 | 42 562 € | 12 599 € | 50 768 € |
| J16 | 1 927 | 809 € | 10 % | 192.7 | 55 305 € | 16 373 € | 66 353 € |
| J17 | 2 505 | 1 052 € | 10 % | 250.5 | 71 894 € | 21 281 € | 86 603 € |
| J18 | 3 256 | 1 368 € | 10 % | 325.6 | 93 447 € | 27 652 € | 112 909 € |
| J19 | 4 232 | 1 777 € | 10 % | 423.2 | 121 458 € | 35 947 € | 147 099 € |
| J20 | 5 501 | 2 310 € | 10 % | 550.1 | 157 879 € | 46 724 € | 191 533 € |
| J21 | 7 151 | 3 003 € | 10 % | 715.1 | 205 234 € | 60 729 € | 249 280 € |
| J22 | 9 296 | 3 904 € | 10 % | 929.6 | 266 795 € | 78 939 € | 324 336 € |

## Annexe 2 · Scénario B jour par jour

| Jour | Envois | Dépense | Taux | Ventes | Encaissé | Réinjecté | Réserve non dépensée |
|---|---|---|---|---|---|---|---|
| J1 | 50 | 21 € | 10 % | 5.0 | 1 435 € | 0 € | 0 € |
| J2 | 50 | 21 € | 10 % | 5.0 | 1 435 € | 0 € | 0 € |
| J3 | 65 | 27 € | 10 % | 6.5 | 1 866 € | 718 € | 711 € |
| J4 | 84 | 35 € | 10 % | 8.4 | 2 411 € | 718 € | 1 414 € |
| J5 | 109 | 46 € | 10 % | 10.9 | 3 128 € | 933 € | 2 322 € |
| J6 | 141 | 59 € | 10 % | 14.1 | 4 047 € | 1 205 € | 3 490 € |
| J7 | 183 | 77 € | 10 % | 18.3 | 5 252 € | 1 564 € | 4 998 € |
| J8 | 237 | 100 € | 10 % | 23.7 | 6 802 € | 2 023 € | 6 943 € |
| J9 | 308 | 129 € | 10 % | 30.8 | 8 840 € | 2 626 € | 9 460 € |
| J10 | 400 | 168 € | 5 % | 20.0 | 5 740 € | 3 401 € | 12 714 € |
| J11 | 520 | 218 € | 5 % | 26.0 | 7 462 € | 4 420 € | 16 937 € |
| J12 | 676 | 284 € | 5 % | 33.8 | 9 701 € | 2 870 € | 19 544 € |
| J13 | 878 | 369 € | 5 % | 43.9 | 12 599 € | 3 731 € | 22 927 € |
| J14 | 1 141 | 479 € | 5 % | 57.1 | 16 373 € | 4 850 € | 27 319 € |
| J15 | 1 483 | 623 € | 5 % | 74.2 | 21 281 € | 6 300 € | 33 017 € |
| J16 | 1 927 | 809 € | 2 % | 38.5 | 11 061 € | 8 187 € | 40 415 € |
| J17 | 2 505 | 1 052 € | 2 % | 50.1 | 14 379 € | 10 641 € | 50 025 € |
| J18 | 3 256 | 1 368 € | 2 % | 65.1 | 18 689 € | 5 530 € | 54 209 € |
| J19 | 4 232 | 1 777 € | 2 % | 84.6 | 24 292 € | 7 189 € | 59 642 € |
| J20 | 5 501 | 2 310 € | 2 % | 110.0 | 31 576 € | 9 345 € | 66 697 € |
| J21 | 7 151 | 3 003 € | 1 % | 71.5 | 20 523 € | 12 146 € | 75 860 € |
| J22 | 9 296 | 3 904 € | 1 % | 93.0 | 26 680 € | 15 788 € | 87 765 € |
