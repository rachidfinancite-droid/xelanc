# Passation · Agent LinkedIn publicitaire de XELANC · 23/11/2026

**Pour** : la nouvelle session de l'agent LinkedIn, sur le Mac de Rachid (avec Claude dans Chrome).
**De** : la session cloud « Agent LinkedIn publicitaire » (31/10 → 23/11/2026).
**Dépôt** : `rachidfinancite-droid/xelanc`, branche `claude/create-finance-header-011CUrWto3dADFdQWirH88L1`, dossier `excellence/`. Faire `git pull --no-rebase` avant tout push : GTM pousse aussi sur cette branche.
**Définition de l'agent** : `.claude/agents/linkedin-ads.md`. **Journal** : `excellence/linkedin-ads-state.yaml`.

---

## 1. Qui tu es et comment travailler avec Rachid

Tu gères toute la publicité LinkedIn de XELANC (même rôle que l'agent Meta) : stratégie, cibles, campagnes, créas, publications, suivi, optimisation.

**Règles de Rachid (impératives)**
1. **Rien n'est publié, programmé, activé, envoyé ou dépensé sans le GO écrit de Rachid**, post par post, campagne par campagne. Tu peux créer en pause.
2. **Prends la main et va au fond** : Rachid ne veut pas te dire « regarde ici, regarde là ». Avant de lui répondre, fais le tour complet (compte, campagnes, groupes, créas, conversions, audiences, Metricool, site). Ne lui renvoie pas des questions que tu peux résoudre toi-même. Peu de questions, une recommandation n°1.
3. **Français, tutoiement, phrases courtes, tableaux.** Les textes proposés s'affichent **en entier dans le chat**, prêts à lire.
4. **Chiffres étiquetés** : [M] mesuré, [E] estimé, [H] hypothèse, avec la source. Rachid demande souvent « sur quelle base ? ».
5. **Pars de son terrain** : ses analyses génériques ont été jugées « banales ». Voir §6.

**Règles de rédaction LinkedIn**
- Lien d'inscription **dans le premier commentaire**, jamais dans le texte.
- « **20 h GMT** » seulement, jamais de ville ni d'heure locale.
- Jamais « **gratuit** », « **offert** », 🎁, rabais ni Black Friday sur LinkedIn.
- Toujours « **XELANC** » en public, jamais « Excellence ». Toujours « **Rachid ELMAATAOUI** ».
- Décrire en **métiers**, pas en compétences. **Zéro vente** : on donne de la valeur.
- Pas de « limité à 100 participants ». Texte aligné à gauche, pas de mot orphelin (espace insécable avant le dernier mot).
- Un lien suivi par post : `utm_source=linkedin&utm_medium=organique|inmail&utm_campaign=…&utm_content=<code du post>`.

---

## 2. Accès et identifiants

| Quoi | État |
|---|---|
| **Compte pub LinkedIn de travail** | **382016523** « Individual Account », en **EUR**, facturation OK. Les autres sont **anciens et abandonnés** : 502223556 FINANCITE INSTITUTE, 502815296 ESPACE LANCITE, 509288991, 545860224, 545880198, 558600765 (Boosters). |
| Contenu du compte 382016523 (23/11) | 2 groupes vides de diffusion : « Xelanc Notoriete » (1245452773), « xelanc » (1242429393). 0 dépense sur 90 jours. **Aucune conversion déclarée.** Aucune audience enregistrée. |
| **Supermetrics** | Équipe « Team xelancmarketing », login **xelancmarketing@gmail.com**, LinkedIn relié via le profil d'**Adam Fonda**. **Lecture seule** : pour écrire, il faut reconnecter LinkedIn Ads avec le droit `rw_ads` (https://hub.supermetrics.com/token-management?team_id=1324471#dataSourceLIA). Essai « gestion de campagnes » jusqu'au 07/12/2026. Limites : pas de création de Message Ads (images seulement), pas d'exclusions, et une écriture demande une approbation par lien. Facebook Ads n'y est pas relié. |
| **Metricool** (fuseau Africa/Casablanca) | Financité Institute `7452435` (page `urn:li:organization:5397256`) ; XELANC `7453104` (page `urn:li:organization:108065517`) ; Page perso Rachid `7462866` (`urn:li:person:wn057P8sxy`) ; Page perso Adam `7462895` (`urn:li:person:8QFoolF0V1`). Les 4 comptes LinkedIn sont connectés. |
| **Insight Tag** | **Posé** sur xelanc.org (au moins sur la page masterclass), avec consentement (`xln_consent`) et une table de conversions dans le code. Le bandeau cookies cite LinkedIn. **Aucune conversion n'est déclarée dans Campaign Manager** : à faire avec l'Agent Site. |
| Identifiants de ciblage | Banking `urn:li:industry:41`, Investment Banking `urn:li:industry:45` ; fonctions Finance `urn:li:function:10`, Comptabilité `urn:li:function:1` ; séniorité Senior `4`, Manager `5`, Director `6`, VP `7`, CXO `8` (`urn:li:seniority:N`). |

**Messages entre sessions** : peu fiables. Les messages de la session cloud vers l'Agent Site et l'agent Meta ont été « livrés » mais jamais lus. Sur le Mac, passe par les fichiers de `~/Travail/` ou par Rachid.

---

## 3. URGENT · Masterclass « Lancez votre double carrière »

**Faits (page vérifiée le 23/11)** : mardi **1er décembre 2026, 20 h GMT**, en direct sur YouTube, avec Rachid ELMAATAOUI. Une heure puis questions, kit remis pendant la masterclass, replay réservé aux inscrits. Page : https://xelanc.org/masterclass-double-carriere/ (bouton `#inscription`). Brief de l'agent Meta : `~/Travail/00-EN-COURS-masterclass/BRIEF-AGENT-LINKEDIN-MASTERCLASS.md`. Plan complet : `~/Travail/00-EN-COURS-masterclass/PLAN-1700-INSCRITS.md`.

**Décisions de Rachid**
1. **Sensibilité banques** : ses clients B2B sont des banques. Ne pas publier le message « double carrière » là où ses contacts bancaires le lisent. **Pas de post sur le compte perso de Rachid ni sur la page Financité.** Le post d'Adam est abandonné aussi.
2. **Pas de banquiers** dans la communication de la masterclass : on s'adresse aux financiers, managers, particuliers.
3. **Principe retenu** : message fort là où c'est **privé ou ciblé** (email Brevo, pub Meta, InMail) ; message **neutre** là où c'est **public** (page XELANC).
4. **Email** : le mailing Brevo est déjà en place (géré par l'agent Brevo).
5. **Test InMail LinkedIn : décidé.** Rachid investit **100 €** pour apprendre si l'InMail touche son buyer persona.

### 3.1 · Test InMail (à créer EN PAUSE dans Campaign Manager)
Brief détaillé : `excellence/linkedin-inmail-masterclass-brief-2026-11-23.md`.
- Groupe « Masterclass 01-12 · Test InMail · Afrique hors Maroc », **100 € au total**, du 24/11 au 30/11.
- Campagne Message Ad, objectif visites du site ; pays : CI, SN, GN, CD, BJ, BF, ML, TG, CM, GA (**pas le Maroc**) ; fonctions Finance + Comptabilité ; séniorité Senior à CXO ; **exclure Banking et Investment Banking** ; extension d'audience désactivée ; 17 €/jour.
- Expéditeur : Rachid. Objet : « Un seul salaire ne suffit plus ? ». Bouton « Réserver ma place ». Lien `…?utm_source=linkedin&utm_medium=inmail&utm_campaign=masterclass-double-carriere&utm_content=IM1#inscription`.
- Texte du message : dans le brief, à reprendre mot pour mot.
- **Statut** : rien n'est créé. Une tentative via Supermetrics a été approuvée par Rachid mais refusée par LinkedIn (droit `rw_ads` manquant), donc pas de doublon.
- **Cadre du test** (fixé d'avance) [E] : ≥ 150 envois pour 100 € ; ≥ 40 % d'ouverture ; réussite à ≥ 3 inscrits (≈ 33 € l'inscrit). Rachid répond lui-même aux réponses InMail. Point quotidien : envois (`sends`), ouvertures (`opens`), clics, dépense (`spend`) via Supermetrics ; inscrits via `utm_medium=inmail` dans WooCommerce ou Brevo.
- Attente honnête : 150 à 300 envois, 1 à 6 inscrits [E]. Meta fait environ 0,85 $ l'inscrit.

### 3.2 · Post de la page XELANC (neutre, validé sur le texte)
> Un financier qui comprend l'entrepreneuriat : son employeur y gagne aussi.
>
> Il connaît de l'intérieur ce que vit un dirigeant. Il devient plus sensible à la performance, à l'importance d'avoir des clients, de tenir ses engagements, de remplir sa part du contrat.
>
> Ce qu'il apprend ailleurs peut servir dans son poste, si trois conditions sont réunies : l'accord de l'employeur, aucun conflit d'intérêts, aucun temps ni outil du poste.
>
> Mardi 1er décembre, 20 h GMT, @Rachid ELMAATAOUI présente les règles du jeu en direct sur YouTube. Suivez-le pour retrouver la suite. Inscription en commentaire.

- Premier commentaire : « Je réserve ma place pour mardi 1er décembre, 20 h GMT (en direct sur YouTube, replay réservé aux inscrits) : https://xelanc.org/masterclass-double-carriere/?utm_source=linkedin&utm_medium=organique&utm_campaign=masterclass-double-carriere&utm_content=X1#inscription »
- **Tag de Rachid** demandé. Une mention via Metricool n'est pas garantie : sinon, l'ajouter à la main dans LinkedIn.
- **Visuel neutre validé** (à produire à partir du visuel d'origine, 1080×1080, logo XELANC seul, **pas de Financité**) : étiquette « ● LIVE MASTERCLASS » ; ruban rouge « **Menace ou atout ?** » ; titre « **Entreprendre à côté d'un emploi** » ; sous-titre « **Y voir clair, des deux côtés.** » ; bloc jaune « **Un kit de travail, remis pendant la masterclass** » ; date, heure, photo et titre de Rachid inchangés. Le visuel d'origine (« Un seul salaire ne suffit plus ! / Lancez votre double carrière ») reste pour Meta et les canaux privés. Il faut une **adresse web publique** pour Metricool.
- Statut : rien n'est programmé. Il manque le visuel neutre et le GO de Rachid.

### 3.3 · À nettoyer dans Metricool (avec l'accord de Rachid)
Des brouillons du 16/10 occupent la semaine et contiennent « gratuit » (mot interdit) : page XELANC, LinkedIn, 24, 25, 26, 27, 30/11 et 02/12 à 8 h ; Adam, LinkedIn, 23/11 au 02/12 à 16 h. Marqués « brouillon », mais à retirer ou décaler. Des reels Instagram (non brouillons) partent aussi les 24, 26, 28 et 30/11 à 19 h.

### 3.4 · Décisions ouvertes de Rachid
- Le titre de la page (« Lancez votre double carrière, sans quitter votre poste ») et la ligne « Pour qui : … banque … » restent visibles dans l'aperçu du lien.
- Les métiers cités par le brief Meta (leveur de fonds, modélisateur…) diffèrent de ceux de la page (conseil aux PME, dossiers de crédit, évaluation, trésorerie externalisée, formation).

---

## 4. Ordre de reprise (sur le Mac)
1. **Créer la campagne InMail en pause** dans Campaign Manager (Claude dans Chrome), selon le brief. Rendre à Rachid la taille d'audience, le coût estimé par envoi et l'aperçu. Rachid active lui-même.
2. **Visuel neutre** : le faire produire (designer ou agent Meta, qui a le fichier d'origine), le mettre en ligne, puis préparer le post XELANC dans Metricool en brouillon. Publication immédiate seulement après le GO.
3. **Metricool** : retirer ou décaler les brouillons « gratuit » (§3.3), après l'accord de Rachid.
4. **Conversions** : avec l'Agent Site, déclarer dans Campaign Manager la conversion « inscription masterclass » (et inscription, achat), liée au code déjà posé.
5. **Point quotidien InMail** jusqu'au 30/11, puis le bilan du test et la décision sur la suite.

---

## 5. Travaux déjà faits (dans `excellence/`)
- `linkedin-strategie-2026-10-31.md` : rôle de LinkedIn (porte employeur, pas canal de volume grand public).
- `linkedin-personas-2026-10-31.md` (v2) : prescripteurs métiers, Maroc en one-to-one, parcours réels.
- `linkedin-banques-par-pays-2026-10-31.md` : 358 banques francophones, 591 à 1 075 directeurs cibles [H].
- `linkedin-agences-par-banque-2026-10-31.md` : agences, 11 000 à 22 400 personnes à former [H], top 10 (Bank of Africa, Attijariwafa, Banque Populaire/ABI…).
- `linkedin-creas-trafic-excellence-2026-11-01.md` : créas de trafic (dossier de crédit, certificat, fondateur).
- `linkedin-insight-tag-architecture-2026-11-01.md` et `questions-agent-site-insight-tag-2026-11-01.md`.
- `carte-agent-linkedin-ads.md` : carte de présentation pour les autres agents.
- `linkedin-masterclass-double-carriere-2026-11-23.md` : premiers brouillons masterclass (dépassés, voir §3).

## 6. Leçons de Rachid (à ne pas oublier)
- **Banques** : la cible, ce sont les **vrais directeurs** (crédit, marché GE/PME, risques), prescripteurs qui amènent 100 à 1 200 personnes (BOA 1 200, CIH 500, Société Générale 200 au Maroc). Les RH et les plans annuels se traitent **en one-to-one**, surtout au Maroc. Hors Maroc, ce sont les **métiers** qui décident.
- **LinkedIn n'est pas Meta** : trop cher pour du volume grand public ; il sert à toucher un buyer persona précis.
- **Masterclass** : rester honnête (les trois conditions : accord de l'employeur, pas de conflit d'intérêts, ni temps ni outil du poste) sans dénaturer l'objet de la masterclass. Rachid a jugé qu'à force de neutraliser, il s'éloignait de son objectif : d'où le principe « fort en privé, neutre en public ».
- **Un message complet** commence par dire de quoi il s'agit (l'événement, qui, quand), pas par une phrase d'accroche obscure.
- **Ne pas inventer** : aucune anecdote, aucun chiffre de formés non validé, aucune question d'inscrit non vérifiée.
