# Insight Tag LinkedIn · architecture de pose sur les deux sites · 01/11/2026

Agent LinkedIn Ads. [M] relevé dans le code public aujourd'hui · [H] à vérifier. Rien n'est posé : ce document est le plan, le code est un modèle à faire poser et tester par le webmaster.

## 1. Ce qui est déjà en place sur xelanc.org (WordPress) [M]

- **Pas de gestionnaire de balises** (pas de Google Tag Manager) : chaque outil est chargé par un petit code maison (snippets WordPress).
- Outils présents : **GA4** `G-1197EQWRNE` (avec mode consentement), **pixel Meta** `1675136700655139`, **Microsoft Clarity**, **Brevo**, suivi interne du tunnel, capture des UTM (cookies `xl_src`, `xl_or`) et attribution des commandes WooCommerce.
- **Consentement** : cookie `xln_consent` (valeurs `granted` / `denied`), géré par le bandeau (`xlnConsent`).
  - **Europe et Royaume-Uni** : rien ne démarre avant « Accepter ».
  - **Ailleurs** (nos pays cibles) : la mesure démarre dès l'arrivée, « Refuser » l'arrête (règle déjà appliquée à Meta et Clarity, GO Rachid du 29/10).
- **Aucun Insight Tag** : ni `snap.licdn.com`, ni `_linkedin_partner_id`.
- Le bandeau cookies ne cite que Meta pour la mesure des publicités : **LinkedIn doit y être ajouté**, ainsi que dans la politique de confidentialité.

## 2. Architecture cible

```
        Campaign Manager (compte 382016523)
        └─ 1 seul Partner ID  ──────────────┐
                                            │ même identifiant sur les deux sites
   xelanc.org (WordPress)          École LearnWorlds
   ├─ snippet « LinkedIn »         ├─ code personnalisé (en-tête)
   │  même logique que Clarity/Meta│  Insight Tag, mêmes conversions
   ├─ conversions (événements)     └─ pas de bandeau Xelanc : vérifier
   └─ domaine déclaré                 le consentement LearnWorlds
        └─ les 2 domaines sont déclarés dans l'Insight Tag
```

**Principe** : un seul Partner ID pour tout le groupe. La même personne vue sur xelanc.org puis sur l'école (ou l'inverse) est reconnue, pour le reciblage et pour la mesure des conversions.

## 3. Ce qu'il faut pour commencer (ton côté)

1. **Le Partner ID** : Campaign Manager → compte 382016523 → *Analyser* → *Balise Insight* (Insight Tag) → *Voir la balise*. Copie le numéro (c'est un identifiant public, visible dans le code de n'importe quel site qui l'utilise).
2. **L'adresse exacte de l'école LearnWorlds** (elle n'apparaît pas dans le dépôt) et si elle est sur un sous-domaine de xelanc.org ou sur un domaine séparé.
3. **Qui pose** : le webmaster (WordPress) et toi ou l'administrateur de l'école (LearnWorlds). Je n'ai accès à aucun des deux admin depuis cette session.

## 4. Pose sur xelanc.org (WordPress)

- **Où** : un nouveau snippet, dans le même système que ceux de Clarity et de Meta (mêmes numéros de série, même cache), chargé sur toutes les pages publiques.
- **Quand il démarre** : hors Europe, tout de suite ; en Europe, après `xln_consent = granted`. `denied` : ne rien charger.
- **Modèle de code** (à adapter au style des autres snippets ; remplacer `PARTNER_ID`) :

```html
<script>
(function(){
  var PID = "PARTNER_ID";
  function g(n){var m=document.cookie.match('(^|;)\\s*'+n+'=([^;]*)');return m?decodeURIComponent(m[2]):'';}
  var tz=''; try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'';}catch(x){}
  var UE=/^(Europe|Atlantic\/(Reykjavik|Canary|Madeira|Azores|Faroe))\//.test(tz);
  var on=false;
  function load(){
    if(on) return; on=true;
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(PID);
    (function(l){
      if(!l){window.lintrk=function(a,b){window.lintrk.q.push([a,b])};window.lintrk.q=[]}
      var s=document.getElementsByTagName("script")[0], b=document.createElement("script");
      b.type="text/javascript"; b.async=true;
      b.src="https://snap.licdn.com/li.lms-analytics/insight.min.js";
      s.parentNode.insertBefore(b,s);
    })(window.lintrk);
  }
  function go(){
    var c=g('xln_consent');
    if(c==='denied') return;
    if(c==='granted' || !UE) load();
  }
  go();
  var prev=window.xlnConsent;                       // se greffe sur le bandeau, comme Brevo
  if(typeof prev==='function'){ window.xlnConsent=function(v){ var r=prev.apply(this,arguments); if(v==='granted') load(); return r; }; }
})();
</script>
```

- **Bandeau et politique de confidentialité** : ajouter LinkedIn à la ligne « La mesure de nos publicités » (aujourd'hui : « cookies de Meta »).
- **Droit** : hors Europe, la règle appliquée est celle de Meta et Clarity. À faire valider pour les pays visés (loi 09-08 / CNDP au Maroc) avant le premier euro.

## 5. Pose sur l'école LearnWorlds

- **Où** : réglages de l'école → suivi / code personnalisé dans l'en-tête, avec le même code (sans la lecture de `xln_consent`, qui n'existe pas sur ce domaine).
- **À vérifier [H]** : si le plan LearnWorlds de l'école autorise du code personnalisé, si une intégration native LinkedIn existe, et quel consentement l'école affiche à ses visiteurs. Je n'ai pas pu le lire d'ici.
- **Point de vigilance** : si l'école est sur un autre domaine que xelanc.org, la personne change de domaine entre les deux ; c'est le même Partner ID sur les deux qui permet de la suivre.

## 6. Conversions à déclarer dans Campaign Manager

| # | Conversion | Où elle se produit | Méthode |
|---|---|---|---|
| 1 | **Inscription gratuite** (compte créé) | xelanc.org `/inscription/` | Événement `lintrk('track',{conversion_id:ID})` déclenché par le code existant juste après la création du compte réussie (comme l'identification Brevo) ; à défaut, règle sur l'URL de la page de confirmation |
| 2 | **Achat** (valeur) | WooCommerce, page « commande reçue » | Règle sur l'URL + valeur de la commande en euros |
| 3 | **Demande de devis Équipes** | `/equipes/` | Événement au envoi du formulaire |
| 4 | **Diagnostic de carrière terminé** | `/carrieres/#orientation` | Événement en fin de diagnostic |
| 5 | **Première capsule regardée** | École LearnWorlds | Règle sur l'URL de la leçon ou événement |

Règles : une conversion = une action utile ; fenêtre d'attribution 30 jours après clic, 7 jours après vue ; aucune conversion déclarée sur un simple chargement de page de paiement (le pixel Meta gonfle déjà les « paniers » pour cette raison).

## 7. Vérification (je peux faire la partie visible)

1. Campaign Manager → Balise Insight → état **Actif** et les deux domaines listés.
2. Relecture du code public de xelanc.org : présence de `snap.licdn.com` et du Partner ID (je peux le faire dès que c'est posé).
3. Test d'une inscription réelle : la conversion 1 doit apparaître dans Campaign Manager sous 24 à 48 h.
4. Test depuis un navigateur « Europe » (rien avant Accepter) et un navigateur « Maroc » (démarrage immédiat).
5. Rien n'est lancé en pub avant que les points 1 à 4 passent.
