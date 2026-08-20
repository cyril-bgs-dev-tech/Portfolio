# 🌬️ Correction apprise des prévisions de qualité de l'air

**Post-traitement des prévisions européennes CAMS aux stations françaises** — le modèle
apprend la **correction** `observation − CAMS`, puis l'**ajoute** à la prévision CAMS. Quatre polluants : NO₂, O₃,
PM10, PM2,5.

> **Ce que ce projet démontre n'est pas un score, c'est un protocole.** La méthode est
> publiée depuis 2023 ; ce qui a de la valeur ici est de l'avoir **mesurée honnêtement**, et
> d'avoir cherché où elle échoue.

📦 **Dépôt** : [correction-previsions-qualite-air](https://github.com/cyril-bgs-dev-tech/correction-previsions-qualite-air)

---

## 🎯 La contrainte qui définit le produit

Le modèle doit corriger **en un point où il n'y a aucune station**. Aucune observation
locale n'entre à l'inférence, pas même celle de la veille. C'est ce qui rend le problème
difficile — et ce qui élimine la moitié des méthodes publiées, qui supposent un réseau dense
disponible en temps réel.

L'évaluation est donc en **double aveugle** : le modèle est testé sur des stations
entièrement absentes de son apprentissage, pendant un mois également absent.

---

## 📊 Le résultat

**Pile complète, double aveugle station *et* mois cachés, J+1, 24 mois de support commun :**

| polluant | `PARTOUT` — aucune observation du point | aux stations — avec son historique |
|---|---|---|
| **NO₂** | **+39,6 %** | +45,7 % |
| **PM10** | **+20,2 %** | +26,3 % |
| **O₃** | **+17,9 %** | +24,1 % |
| **PM2,5** | **+11,8 %** | +19,6 % |

*Réduction de RMSE contre CAMS brut. **Citer deux chiffres, jamais un** : `PARTOUT` vaut là
où rien ne mesure — c'est le seul que CAMS ne sait pas faire.*

**Contre la chaîne opérationnelle**, mêmes stations et mêmes jours, à J+1 : le produit
archivé de PREV'AIR porte dans sa métadonnée `CHIMERE combined to surface real time
observations` — c'est **AS-CHI**, leur adaptation statistique. L'écart va de **+13,7 %**
(O₃) à **+66,9 %** (PM2,5) à notre avantage, **sur dix-sept jours seulement** : leur archive
n'expose que six jours glissants et ne peut pas remonter le temps.

---

## 🔬 Ce qui distingue ce travail

### Le mécanisme est établi, pas supposé

Le dernier levier trouvé — sept traceurs de **composition** du champ CAMS que le dépôt ne
téléchargeait pas — rend +1,5 à +6,0 %. Une **permutation conditionnelle** tranche son
mécanisme : permuter la composition *à l'intérieur* de chaque couple (station, mois)
conserve exactement l'histogramme par site et par saison, et ne détruit que l'appariement au
**jour**. Elle **efface la totalité du gain**, sur les quatre polluants.

Ce n'est donc ni un encodeur site×saison, ni un proxy de régime : le modèle exploite
l'**écart du jour** à la composition habituelle du lieu.

### Les seuils sont fixés avant de regarder

Chaque test porte son critère de décision **écrit dans l'en-tête du script**, avant la
première mesure — et la phrase à écrire si le test échoue. L'attribution par valeur de
Shapley a d'ailleurs **renoncé** à attribuer un gain à un groupe de traceurs sur PM2,5,
faute d'avoir franchi son propre seuil.

### Une affirmation du projet a été réfutée par sa propre mesure

Le dossier affirmait que ses leviers ne se dégradent pas avec l'échéance. Le balayage de J0
à J+3 — la dernière échéance que CAMS Europe produise — le met à l'épreuve.

⚠️ **Ces scores ne sont pas ceux du tableau précédent.** Pour comparer quatre échéances
entre elles, il faut une **pile identique aux quatre** : CAMS, terrain, calendrier,
typologie et tendance récente — **ni spéciation, ni GEOS-CF**, dont la couverture varie
avec l'horizon. C'est donc une mesure de **sensibilité**, à lire pour sa pente, pas pour
son niveau.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/v5_echeances_sombre.svg">
  <img alt="De J0 à J+3, le gain sur le NO₂ reste stable de 37,1 % à 36,7 % (0,38 point), tandis que celui sur l'ozone tombe de 9,3 % à 7,0 % (2,25 points)." src="assets/v5_echeances_clair.svg" width="100%">
</picture>

| | J0 | J+1 | J+2 | J+3 | plage | verdict |
|---|---|---|---|---|---|---|
| NO₂ | +37,1 % | +37,1 % | +36,9 % | +36,7 % | 0,38 pt | ✅ **stable** |
| O₃ | +9,3 % | +9,1 % | +8,5 % | **+7,0 %** | 2,25 pt | 🔴 **réfutée** |

Et le classement suit le mécanisme invoqué : l'apport de la typologie de station — qui mesure
à quel point le résidu est attaché au **lieu** — vaut **+9,0 pt sur NO₂** et **−0,2 sur O₃**.
Le polluant dont l'erreur est un effet de site résiste à l'échéance ; celui qui ne l'est pas
se dégrade. *L'affirmation était juste sur son mécanisme et trop large dans sa portée.*

---

## 🛡️ Les défauts trouvés dans nos propres résultats

Chaque ligne est un défaut **silencieux** — rien ne plantait, tout était plausible :

| ce qui était faux | comment on l'a su | ce qui l'empêche aujourd'hui |
|---|---|---|
| « J+1 » désignait en fait **J0** | lu dans les données, pas dans le nom | `libelle_echeance()` dérive le libellé |
| une colonne `rmse_realmlp` contenait du **LightGBM** | un relecteur externe a rouvert le CSV | un garde refuse d'écrire une étiquette qui affirme une identité |
| le PDF **ne contenait pas** le chiffre que le document désigne comme le seul citable | mesure de largeur en média impression | l'export **refuse** et nomme l'élément |
| un mois absent codait l'**année** | revue externe, puis recherche du jumeau | le garde **mesure** la couverture de chaque famille |
| l'échéance publiée était **J+2**, la mesure est **J+1** — une erreur qui **flattait** | premier jour couvert, horizon par horizon | mécanisé après être revenue une fois |

> **La règle du dépôt** : *une règle violée deux fois devient du code, ou elle disparaît.*
> Douze règles, dont dix exécutables.

---

## 📅 L'horizon réglementaire — pourquoi ce travail a un usage

La directive **(UE) 2024/2881** fait deux choses que l'on cite toujours séparément : elle
**divise par deux** les valeurs limites annuelles au 1ᵉʳ janvier 2030, et elle rend la
**modélisation obligatoire** dans toute zone où un seuil est dépassé. Multipliées, elles
donnent l'argument que ni l'une ni l'autre ne porte seule — abaisser le seuil **multiplie
mécaniquement** le nombre de zones où modéliser devient une obligation légale.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/v4_seuil_2030_sombre.svg">
  <img alt="Le nombre de stations en dépassement passe de 6 aujourd'hui à 109 en 2030, soit un facteur 18,2, sans qu'aucune émission n'ait changé." src="assets/v4_seuil_2030_clair.svg" width="100%">
</picture>

Compté sur le parc réel, moyennes annuelles 2025, à air constant : **6 stations en
dépassement aujourd'hui, 109 en 2030** — un facteur **×18,2** sur 408 évaluées. En
Occitanie, 2 → 5, et **4 des 13 départements n'ont aucune station retenue** : pour eux la
conformité 2030 ne peut pas être posée depuis la mesure. C'est le cas que la directive
confie explicitement à la modélisation.

**Et là où le modèle devient opposable, sa qualité devient un point de contrôle** — c'est le
critère FAIRMODE qui en décide. Part des stations satisfaisant `MQI_f ≤ 1` à J+1, critère
atteint à partir de **90 %** :

| polluant | CAMS brut | corrigé · `PARTOUT` | corrigé · aux stations |
|---|---|---|---|
| **NO₂** | **41,4 %** ✗ | 87,9 % ✗ | **96,2 %** ✓ |
| PM10 | 87,8 % ✗ | 98,4 % ✓ | **100 %** ✓ |
| O₃ | 93,6 % ✓ | 97,4 % ✓ | **99,2 %** ✓ |

Le NO₂ est le cas critique, et ce n'est pas une coïncidence : c'est à la fois le polluant où
le produit européen échoue le plus et celui dont la valeur limite est divisée par deux. Son
biais passe de −14,27 à −0,43 µg/m³.

🔴 **Le critère n'est pas franchi partout, et le dire fait partie du résultat** : sans aucune
observation du point, le NO₂ reste à 87,9 %, *sous* la barre. Il ne la franchit qu'aux
stations instrumentées.

---

## 🧰 Stack

**Python** · LightGBM · PyTorch *(RealMLP-TD porté)* · Optuna · xarray/netCDF4 · pandas ·
scikit-learn · Streamlit · Playwright

**Données** — CAMS Europe (Copernicus/ECMWF, 28 variables), NASA **GEOS-CF** *(modèle de
chimie indépendant)*, observations LCSQA/Geod'Air, ERA5 *(réanalyse : plafond, non
déployable)*, Copernicus DEM GLO-30, IGN Géoplateforme, PREV'AIR/INERIS.

**Volume** — corpus de **36 mois** (2023-08 → 2026-07), **28,0 M d'enregistrements horaires**. Prévisions extraites à **476 points** ; **438 stations effectivement évaluées**, de 236 (PM2,5) à 344 (NO₂) selon le polluant.

---

## 📐 Le protocole d'évaluation

Quatre cellules, selon ce qui est caché :

| épreuve | station | mois | ce qu'elle mesure |
|---|---|---|---|
| spatiale | **cachée** | vue | transfert vers un lieu non instrumenté |
| temporelle | vue | **caché** | tenue dans le temps |
| **double aveugle** | **cachée** | **caché** | **la condition de déploiement** |
| chronologique | **cachée** | **caché**, passé seul | extrapolation réelle |

Les masques d'entraînement sont donnés **explicitement**, jamais par complément — le
complément du test double aveugle contient encore le mois caché sur d'autres stations, ce
qui rendrait l'épreuve plus facile que chacune des deux prises séparément.

L'incertitude vient d'un **bootstrap circulaire par blocs de mois** sur les différences
appariées : les plis ne sont pas indépendants, les groupes de stations tournent et deux plis
partagent 93 % de leur apprentissage. La version à six mois est la sensibilité obligatoire.

---

## 🔴 Ce que ce projet ne démontre pas

- **La détection d'épisodes reste faible** : 3 des 33 épisodes PM10 réellement déclenchés par
  les préfectures. Même l'observation parfaite n'en attrape que 21 — la décision préfectorale
  intègre des critères que la concentration seule ne contient pas.
- **Dix-sept jours de duel ne concluent rien** contre la chaîne opérationnelle. C'est un
  ordre de grandeur.
- **Au seuil réglementaire ozone de 180 µg/m³**, 3 dépassements détectés sur 32.
- **Le flux GEOS-CF v1 est retiré depuis janvier 2026** et v2 n'est pas le même prédicteur
  (15,4 µg/m³ d'écart sur l'ozone au recouvrement). Un déploiement aujourd'hui exigerait de
  re-valider son apport.

*Ces limites sont publiées au même titre que les résultats favorables.*
