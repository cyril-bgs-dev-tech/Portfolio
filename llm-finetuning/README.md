# LLM_finetuning

**Affiner et distiller des LLM sur des comptes rendus cliniques français, et mesurer ce que chaque technique apporte vraiment.**
Une seule carte graphique (RTX 5090, 32 Go de VRAM), aucune location de calcul, aucune donnée de patient réel.

> Ce dépôt est une **vitrine** : il explique le projet et sa méthode.
> Le code, les données dérivées et les preuves de chaque run sont dans un dépôt **privé**.
> **La présentation détaillée (diapositives, protocole, résultats et leurs preuves) est transmise sur demande**
> à [cyril.bgs.dev@gmail.com](mailto:cyril.bgs.dev@gmail.com?subject=LLM_finetuning%20%3A%20demande%20de%20pr%C3%A9sentation).
> Elle peut aussi être déroulée en entretien technique.

---

## La question

Quand on adapte un LLM à un texte spécialisé, de nombreuses techniques promettent un gain : réglage fin
par LoRA, distillation d'un gros modèle vers un petit, pré-entraînement sur une tâche voisine, ou
plusieurs de ces leviers ensemble. Peu de comparaisons le montrent proprement : références faibles,
réglages inégaux, test réutilisé, gain annoncé sans intervalle de confiance.

**LLM_finetuning répond à une question simple : quelle technique donne un gain réel, et de combien,
face à une référence solide et correctement réglée ?** Si aucune n'en donne, le livrable est un verdict
négatif documenté et reproductible.

## La tâche

Prédire le **chapitre CIM-10** d'un séjour à partir de ses comptes rendus, en français.
Les textes viennent de **PARHAF**, un corpus ouvert de comptes rendus cliniques **fictifs**, écrits par
des internes et relus par des pairs (licences CC BY 4.0 et Etalab 2.0). Aucune donnée de santé réelle
n'est utilisée, et le projet n'en revendique aucun usage clinique : les conclusions portent sur des
données fictives.

## La méthode

- **Références fortes d'abord.** Une classe majoritaire pour la borne basse, un TF-IDF avec
  régression logistique, un encodeur de la famille BERT en français biomédical, puis des LLM affinés par
  LoRA. Une technique n'a de valeur que si elle bat la meilleure référence, pas la plus faible.
- **Protocole gelé avant la première mesure.** Métrique, seuil d'utilité, nombre de graines, budget de
  GPU et grille de réglage sont écrits, hachés (SHA-256) et vérifiés à chaque contrôle. Trois relectures
  adversariales avant le gel.
- **Verdict en trois valeurs.** *Gain confirmé*, *absence de gain utile*, ou *non résolu*. Un écart non
  résolu reste non résolu, même quand il est flatteur.
- **Comparaisons appariées.** Mêmes patients, mêmes plis, mêmes graines ; intervalles de confiance par
  bootstrap ; la conclusion porte sur les écarts, pas sur des scores isolés.
- **Test scellé.** Ouvert une seule fois, derrière un garde de code, un marqueur et un journal d'accès.
- **Anti-fuite.** Découpage par patient, plis par auteur en contrôle, détection de doublons et de
  gabarits, raccourcis mesurés plutôt que supposés.
- **Honnêteté sur la puissance.** La puissance statistique du protocole est simulée avant de lancer
  les entraînements, et ses limites sont dites d'avance : tant que le verdict n'est pas résolu, le
  cycle est classé *exploratoire* et aucun gain n'est annoncé.
- **Incertitude et abstention.** Calibration, prédiction conforme avec couverture mesurée, et politique
  d'abstention : un classifieur utile sait aussi dire qu'il ne sait pas.
- **Claim-gate.** Une affirmation ne sort du dépôt qu'avec sa preuve (un run, un fichier, une
  commande), ou elle ne sort pas.

## Ce que le projet a déjà établi côté méthode

- Un protocole écrit pour être tenu, et dont les défauts (puissance insuffisante pour un seuil trop
  fin, recette d'entraînement trop courte qui sous-estimait les modèles appris) sont **constatés,
  consignés et corrigés par versions**, pas effacés.
- Un résultat inattendu traité comme tel : le score dépend du mode de découpage (par patient ou par
  auteur). Les deux valeurs sont rapportées, trois explications sont posées, aucune n'est tranchée
  sans preuve.
- Une ingénierie qui rend les erreurs visibles : tests automatiques, typage strict, registre de runs
  en écriture seule, décisions d'architecture tracées, tests éprouvés par mutation, wiki dont les
  citations sont vérifiées contre les sources.
- Des coûts mesurés et non estimés : mémoire de pointe, durée d'entraînement et latence d'inférence
  de chaque famille de modèles, quantification testée sur la tâche.

## Où en est le projet (4 octobre 2026)

Le premier cycle exploratoire est mené, des références aux LLM affinés par LoRA, avec les mesures
d'incertitude, de robustesse et de coût. **Aucun verdict confirmatoire n'est rendu** : il viendra d'un
second cycle sous protocole révisé, avec plusieurs plis et plusieurs graines, puis d'une ouverture
unique du test scellé. La distillation et le pré-entraînement sur tâche voisine restent à comparer
dans ce cadre. Les chiffres sont volontairement absents de cette page : ils se lisent avec leurs
intervalles, leurs réserves et leurs preuves, dans la présentation détaillée.

## Comment le projet est construit

Développé par une seule personne, avec des agents de code (Claude Code, Codex) sous un contrat écrit :
règles de périmètre disque, aucune publication sans accord, journal daté des décisions et des erreurs,
questions rangées pour l'humain, audits croisés par d'autres modèles puis vérifiés à la source.

**Stack** : Python · PyTorch · Hugging Face (Transformers, PEFT, TRL) · scikit-learn · SciPy · pandas ·
pytest · mypy strict · ruff · uv · Docker

## Contact

Cyril Bourgeois, Data Scientist et ingénieur ML
Présentation détaillée sur demande : [cyril.bgs.dev@gmail.com](mailto:cyril.bgs.dev@gmail.com?subject=LLM_finetuning%20%3A%20demande%20de%20pr%C3%A9sentation)
[Portfolio](https://cyril-bgs-dev-tech.github.io/Portfolio/) ·
[LinkedIn](https://www.linkedin.com/in/cyril-bourgeois-65a739150) ·
[Kaggle](https://www.kaggle.com/cyrilbourgeois)
