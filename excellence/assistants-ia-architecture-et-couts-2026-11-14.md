# Les assistants IA Excellence : architecture et maîtrise des coûts · 14/11/2026

**Pour** : Rachid
**Proposition de Rachid** :
- une plateforme de montée en compétences continue (la « bible » : formations, parcours, bonnes pratiques) ;
- sept assistants : levée de fonds, valorisation, business model et création de valeur (dont la réduction des coûts), ressources, crédit, trésorerie, financier.

**Question** : comment éviter que des utilisateurs qui abusent fassent exploser la facture ?
**Étiquettes** : [M] tarif publié, [E] estimé, [H] hypothèse.

---

## 1. L'architecture recommandée

**Côté client** : sept assistants bien nommés, chacun avec sa page, ses exemples de questions et ses modèles.
**Côté technique** : **un seul moteur** avec sept « modes » (instructions, sources et outils propres à chaque assistant), et non sept agents séparés. Trois raisons :
1. **Une seule mémoire de l'entreprise** : les comptes déposés une fois servent à tous les assistants. L'assistant crédit voit la trésorerie, l'assistant valorisation voit le business model.
2. **Un seul budget à surveiller** par client.
3. **Un seul endroit à corriger** quand une règle change (loi de finances, BCEAO).

| Assistant | Ce qu'il fait | Ce qu'il produit |
|---|---|---|
| **Financier** (la porte d'entrée) | Diagnostic à partir des comptes, ratios, alertes, réponses générales | Rapport de diagnostic, plan d'action |
| **Trésorerie** | Prévision à 13 semaines, besoin en fonds de roulement, alertes | Plan de trésorerie, actions de cash |
| **Crédit** | Dossier de crédit, analyse d'offres de prêt, revue des frais bancaires | Dossier prêt à déposer, arguments de négociation |
| **Levée de fonds** | Recherche de financements (banques, fonds, bailleurs, subventions), préparation des demandes | Liste de financeurs ciblés, dossier, présentation aux investisseurs |
| **Valorisation** | Valeur de l'entreprise selon plusieurs méthodes, scénarios | Note de valorisation |
| **Business model et création de valeur** | Marges, prix de revient, réduction des coûts, leviers de rentabilité | Liste chiffrée d'économies, plan de création de valeur |
| **Ressources** | Modèles, check-lists, procédures, capsules de cours | Fichiers prêts à l'emploi |

L'assistant **Ressources** est aussi la **bible** : il relie chaque réponse aux cours, modèles et certificats de la plateforme. Il ne coûte presque rien à faire tourner, puisque c'est surtout de la recherche dans le catalogue.

---

## 2. Ce que coûte une question (API Claude, tarifs au 03/11/2026)

| Modèle | Entrée, par million de jetons | Sortie, par million de jetons | Usage conseillé |
|---|---|---|---|
| Claude Haiku 5.5 | $0,10 | $0,50 | Tri des questions, recherche dans la bible |
| Claude Sonnet 5.5 | $2 | $10 | La plupart des réponses et analyses |
| Claude Opus 5.5 | $4 | $20 | Les livrables lourds (dossier de crédit, valorisation) |

*Un jeton ≈ ¾ de mot. Une page de texte ≈ 600 à 800 jetons.*

| Type d'usage | Taille typique [E] | Coût par usage [E] |
|---|---|---|
| Question simple (fiscalité, définition, conseil rapide) | 8 000 jetons en entrée, 2 000 en sortie | **≈ $0,02 à 0,04** (Sonnet), < $0,01 (Haiku) |
| Analyse d'un document déposé (états financiers de 40 pages) | 40 000 en entrée, 8 000 en sortie | **≈ $0,15 à 0,30** |
| Livrable complet (dossier de crédit, business plan, valorisation) en plusieurs étapes | 150 000 à 300 000 jetons au total | **≈ $1 à 3** |

**La mise en cache** des instructions et de la bible (relue à $0,10 à 0,20 le million de jetons au lieu de $2 à 4) réduit le coût des questions de **30 à 60 %**.

---

## 3. Coût mensuel par place, selon l'usage

Une place à 450 par an, c'est **37,50 par mois**. Pour garder une bonne marge, le coût IA doit rester sous **≈ 15 à 20 % du prix, soit $6 à 8 par place et par mois** [H].

| Profil | Usage mensuel | Coût IA par mois [E] | Marge |
|---|---|---|---|
| Léger (la majorité) | 30 questions, 2 analyses | ≈ $1,50 | Très bonne |
| Normal | 100 questions, 10 analyses, 2 livrables | ≈ $8 | Correcte |
| **Gros utilisateur** | 400 questions, 40 analyses, 10 livrables | **≈ $35** | **Perte** |

Sans règles, il suffit de 10 % de gros utilisateurs pour manger la marge.

---

## 4. Les règles anti-abus

1. **Des crédits mensuels par place.** Exemple : **300 crédits par mois**. Question simple = 1 crédit, analyse de document = 10, livrable complet = 50. Le client voit son compteur. Une fois les crédits épuisés, il achète un **pack de crédits** ou passe à l'étage supérieur. **C'est la règle principale** : l'abus devient du chiffre d'affaires.
2. **Le bon modèle pour chaque tâche.** Le tri des questions et la bible passent par un modèle léger, la plupart des réponses par un modèle intermédiaire, les livrables lourds seulement par le modèle le plus puissant. Le client ne le voit pas.
3. **Des limites techniques** :
   - taille maximale des documents déposés ;
   - nombre de messages par conversation, au-delà duquel on en ouvre une nouvelle avec un résumé ;
   - nombre de requêtes par minute.
4. **Une place = une personne nommée.** Connexion personnelle et nombre d'appareils limité, pour empêcher le partage d'un compte entre 10 collaborateurs.
5. **Une clause d'usage raisonnable** dans les conditions générales.
6. **Un tableau de bord interne** : coût IA par client et par mois, alerte à 80 % du budget, liste des 20 plus gros consommateurs chaque semaine.
7. **Les experts humains, plafonnés** : nombre de questions transmises à un expert par mois selon l'étage (par exemple 0 pour l'étage Équipe, 4 pour l'étage Direction).
8. **Les rapports non urgents en traitement différé** (veille mensuelle, rapports périodiques) : le traitement par lots coûte 50 % de moins.

---

## 5. Ce que ça donne en résumé

| Élément | Choix |
|---|---|
| Ce que voit le client | 7 assistants + la bible + les experts |
| Ce qui tourne derrière | 1 moteur, 7 modes, 3 niveaux de modèle |
| Ce qui protège la marge | Crédits mensuels, packs de crédits, place nominative, plafond d'experts |
| Coût IA visé | ≤ $6 à 8 par place et par mois en moyenne |

**Prochaine étape** : fixer le barème de crédits par assistant, puis mesurer le vrai coût sur 20 cas réels (5 questions, 5 analyses, 5 livrables, 5 recherches dans la bible) avant de figer les prix.
