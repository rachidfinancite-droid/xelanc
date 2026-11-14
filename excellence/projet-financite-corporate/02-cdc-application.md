# Cahier 02 · L'application Financité Corporate · v1 · 14/11/2026

**Objectif** : une application web qui donne au DAF, au dirigeant et à l'équipe :
- la bibliothèque de compétences ;
- le copilote ;
- les simulateurs ;
- les 4 assistants ;
- les questions au mentor.

**Construction** : par Rachid, avec Claude Code, une étape par session [D].
**Ce qui reste dans LearnWorlds** : cours, parcours, évaluations, certificats.

---

## 1. Les utilisateurs et leurs droits

| Rôle | Peut |
|---|---|
| **Administrateur entreprise** (souvent le DAF) | Gérer les places, inviter, voir l'usage de son entreprise, acheter des crédits |
| **Utilisateur DAF et Dirigeant** | Tout ce qui suit, plus : assistants, simulateurs, copilote, mentor |
| **Utilisateur Équipe** | Bibliothèque de compétences, IA de la semaine, lien vers ses cours |
| **Expert Financité** | Recevoir et répondre aux questions « Demandez au mentor » |
| **Administrateur Financité** | Clients, coûts, contenus, financeurs, qualité |

---

## 2. Le profil de l'entreprise (saisi une fois)

Pays, secteur, taille (salariés, tranche de CA), régime fiscal, référentiel comptable (SYSCOHADA ou CGNC), banques principales (facultatif).

**C'est la seule donnée conservée** sur l'entreprise, hors comptes utilisateurs et historique d'usage.

---

## 3. Les écrans

| Écran | Contenu |
|---|---|
| **Accueil** | Une barre « Posez votre question », les raccourcis (bibliothèque, simulateurs, assistants), l'IA de la semaine, les prochaines échéances fiscales, le compteur de crédits |
| **Bibliothèque de compétences** | Recherche, domaines, fiches en 10 blocs (cahier 04), bloc « avec vos chiffres », « Mes compétences » |
| **Copilote** | Conversation ; possibilité de coller un texte ou de déposer un document pour la question du moment |
| **Simulateurs** | 7 simulateurs : rentabilité d'un devis, coût d'un délai client, escompte, coût réel d'un crédit, coût d'un salarié, seuil de rentabilité, calculs fiscaux |
| **Assistants** | Crédit, Levée de fonds, Valorisation, Création de valeur. Chacun : saisie guidée → analyse → livrable Word |
| **Demandez au mentor** | Formulaire, compteur de questions restantes, historique des réponses |
| **Mon entreprise** (admin) | Places, invitations, usage, crédits, factures |
| **Back-office Financité** | Clients, coûts IA, file des questions aux experts, contenus, base des financeurs, cas de référence |

---

## 4. Les règles fonctionnelles

### 4.1 Données
- Les documents déposés pour une question **sont supprimés après traitement** (délai à fixer, par exemple 24 h).
- Les chiffres saisis dans les simulateurs et les assistants **ne sont pas conservés**, sauf si l'utilisateur enregistre volontairement un livrable.
- Les livrables enregistrés sont visibles **uniquement par l'entreprise qui les a créés**.

### 4.2 Crédits [H, barème à fixer]
- **300 crédits par place DAF et par mois** :
  - fiche compétence ou question au copilote : 1 crédit ;
  - analyse de document : 10 crédits ;
  - livrable d'assistant : 50 crédits.
- Alerte à 80 %. Blocage à 100 %, avec proposition de pack.
- **Les places Équipe** : bibliothèque de compétences avec un plafond mensuel raisonnable.

### 4.3 Demandez au mentor
- 2 questions par mois et par accès DAF, réponse sous 72 h ouvrées.
- L'IA prépare un premier jet pour l'expert. **L'expert valide, corrige et signe.**
- Notification au client par email, et plus tard par WhatsApp.

### 4.4 Rendez-vous automatiques
- Lundi : IA de la semaine.
- Vendredi : veille.
- Avant chaque échéance fiscale du pays : rappel et liste de contrôle.

---

## 5. Architecture technique [D, recommandation du 14/11]

| Composant | Choix |
|---|---|
| Application web | Next.js |
| Base de données, comptes, fichiers | Supabase, **région Europe**, avec isolation des données par entreprise (règles d'accès au niveau des lignes) |
| IA | API Claude. Modèle léger pour le tri et la bibliothèque, modèle intermédiaire pour la plupart des réponses, modèle puissant pour les livrables lourds. Mise en cache des instructions et de la base de connaissance |
| Base de connaissance | Cours de Rachid et recueil de règles, indexés pour la recherche (cahier 03) |
| Paiement | Stripe (carte), facture et virement pour les entreprises [À vérifier pour XELANC FZCO] |
| Hébergement | Vercel (ou équivalent), région connue |
| Emails | Service d'envoi transactionnel (Brevo existant) |
| Lien LearnWorlds | Liens profonds vers les capsules ; connexion unique plus tard |

**Environnements** : test et production séparés dès le premier jour.
**Secrets** : jamais dans le code ; plafond de dépense mensuel sur la clé API.

---

## 6. La première version (MVP, objectif ≈ 6 semaines)

| Inclus | Exclu (plus tard) |
|---|---|
| Comptes, profil d'entreprise, invitations | Paiement en ligne (facturation manuelle au début) |
| Bibliothèque de compétences (100 fiches préparées + génération à la demande) | Point trésorerie, relances clients |
| Copilote | Accès WhatsApp |
| 3 simulateurs (devis, crédit, coût d'un salarié) | Branchement aux logiciels comptables |
| Assistant Crédit | Compteur d'économies |
| Demandez au mentor | Version anglaise |
| Compteur de crédits simple, tableau de bord des coûts | |

Les assistants Levée de fonds, Valorisation et Création de valeur arrivent dans les 4 à 6 semaines suivantes.

---

## 7. Exigences non fonctionnelles

| Exigence | Niveau attendu |
|---|---|
| Isolation des données | Un utilisateur ne voit jamais les données d'une autre entreprise (testé volontairement) |
| Temps de réponse | Fiche compétence < 10 s ; livrable d'assistant < 3 min, avec indication de progression |
| Disponibilité | 99 % hors maintenance annoncée |
| Mobile | Utilisable sur téléphone (dirigeants) |
| Langue | Français ; anglais à M+12 |
| Journalisation | Coûts IA, erreurs, usage par entreprise ; aucune donnée financière dans les journaux |

---

## 8. Méthode de construction

- **Une étape = une session Claude Code.** Chaque session se termine par :
  - un test fait par Rachid ;
  - une sauvegarde du code (commit) ;
  - la mise à jour de `ETAT.md`.
- Les cas de référence des assistants repassent à chaque modification.
- **Ordre des étapes** : socle et comptes → profil → bibliothèque → copilote → simulateurs → assistant Crédit → mentor → crédits et tableau de bord → revue de sécurité → pilote.
