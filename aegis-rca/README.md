# 🕵️ Aegis-RCA — Agent de Diagnostic de Causes Racines

**Vision** : une fois que [vigilance](../vigilance/) détecte une anomalie, Aegis-RCA l'investigue — corrèle le contexte, consulte les procédures, propose un diagnostic et une recommandation, toujours soumis à validation humaine avant toute action.

**Contexte** : projet personnel, extension directe de vigilance (2026)
**Durée** : prototype développé sur 3 jours (17-19 juillet 2026)

**Où en est ce projet** :
- ✅ Fait : consommation des tickets vigilance, corrélation métriques Prometheus, RAG sur base de connaissance (procédures/post-mortems), sandbox d'auto-correction fonctionnel (1 succès mesuré), méthodologie d'évaluation rigoureuse (bancs internes avec seuils fixés à l'avance)
- 🚧 Pas encore fait : mémoire long-terme des corrections opérateur, observabilité de production, déploiement cloud (décisions documentées, pas construites) — c'est un prototype de recherche de 3 jours, pas un produit fini

---

::: {.panel-tabset}

## 🧑‍💼 Vue d'ensemble

**Le problème** : un système de détection d'anomalies comme `vigilance` dit *qu'*une machine se comporte anormalement — mais pas toujours *pourquoi*. Un opérateur reçoit une alerte et doit encore chercher la cause, consulter les procédures pertinentes, et décider quoi faire. C'est ce travail d'investigation qu'Aegis-RCA prend en charge automatiquement.

**Comment ça marche, en clair** : dès qu'un incident est ouvert, un agent (basé sur un modèle de langage exécuté en local, pas dans le cloud) rassemble le contexte — les métriques autour de l'incident, l'historique de la machine, les procédures internes pertinentes — puis rédige un diagnostic avec sa recommandation. Rien n'est exécuté automatiquement : un humain valide toujours avant qu'une action ne soit prise.

**Ce qui distingue ce projet, ce n'est pas juste "il y a un agent IA"** — c'est la méthode : chaque choix d'architecture a été soumis à l'avis de plusieurs IA différentes (Gemini, ChatGPT) puis vérifié contre des mesures réelles avant d'être adopté. Un exemple concret : un premier test semblait montrer que la technique choisie pour fiabiliser l'agent fonctionnait parfaitement (100 % de réussite) — une vérification plus poussée a révélé que ce succès venait en fait d'un détail différent du prompt, pas de la technique testée. Cette erreur a été détectée et corrigée avant de tirer une conclusion, plutôt que d'afficher un chiffre flatteur mais faux.

**Ce que ça démontre** : la capacité à construire un système d'IA agentique avec la même rigueur qu'une démarche scientifique — mesurer plutôt que supposer, documenter les échecs autant que les réussites, et rester honnête sur ce qui n'est pas encore prouvé (le module d'auto-correction n'a qu'un seul succès mesuré à ce stade, pas un taux fiable).

## 🔧 Détails techniques

## Architecture

- `aegis/consumer.py` — consommateur Redis at-least-once, anti-poison (ACK systématique) sur le flux `aegis:incidents` de vigilance
- `aegis/agent/investigator.py` — agent d'investigation : LLM local (Qwen3.6:27B via Ollama), orchestré par une machine à états Python explicite (pas de framework agent type LangGraph — décision mesurée, voir plus bas)
- `aegis/rag/` — RAG hybride (Qdrant) sur une base de connaissance versionnée : procédures (SOPs), post-mortems, fiches de référence
- `aegis/sandbox/` — auto-correction : exécution de code généré dans un conteneur Docker jetable et durci (user non-root, rootfs read-only, `--network=none`, cgroups pids-limit anti fork-bomb)
- `aegis/tools/metrics.py` — tool typé Prometheus (requêtes curées, best-effort)
- API FastAPI : `/health`, `/incidents`, `/incidents/{ticket}`

## Méthode — pas de décision d'architecture sans confrontation au réel

Chaque choix structurant a été soumis à deux avis externes (Gemini, ChatGPT) **puis vérifié contre le code et des bancs de mesure réels** avant adoption. Deux exemples représentatifs :

- **Tool-calling** : un premier banc semblait valider un stack à 100 % de succès. Une bissection plus poussée a montré que le succès venait d'un exemple JSON littéral présent dans le prompt système, pas de la contrainte de décodage structuré qu'on pensait tester — le banc validait le mauvais mécanisme. Correction appliquée avant d'écrire la moindre conclusion.
- **Machine à états maison vs LangGraph** : décision de rester sur une machine à états explicite tant que le graphe reste sous ~15 nœuds et qu'aucune pause n'est nécessaire en milieu d'exécution — le seuil de bascule est documenté explicitement, pas choisi par défaut.
- **Évaluation sans vérité terrain** : rubrique de questions binaires plutôt qu'une note globale (qui récompense la longueur), "fidélité au contexte" comme métrique reine, juge ≠ générateur (Qwen génère, mistral-small juge), comparaisons A/B systématiquement permutées, stabilité du juge mesurée avant d'y faire confiance.

## Preuves (bancs internes, résultats bruts versionnés)

| Banc | Résultat |
|---|---|
| Tool-calling (qwen3.6:27B, 300 appels) | 100 % JSON valide / outil correct / arguments corrects, une fois le piège ci-dessus corrigé |
| Incidents à cause connue (gate Phase C, 14 cas dont cas ambigus à dessein) | 6 itérations avant un run conforme aux seuils fixés à l'avance — runs ratés conservés, pas masqués |
| Auto-correction (sandbox) | 1 succès mesuré : 1 itération, 9,6 s, modèle réel |
| Calibration du juge | Stabilité mesurée sur répétitions, juge différent du générateur |
| Retrieval RAG | hit@1 = 0,969 · hit@4 = 1,000 · MRR = 0,984 sur 32 requêtes |

## Limites honnêtes

- Prototype de 3 jours de développement, Phase A/B seulement
- L'auto-correction n'a qu'une seule preuve de succès mesurée — pas un taux statistiquement robuste
- Nécessite le réseau Docker externe de vigilance pour tourner
- Mémoire long-terme, observabilité de production et déploiement cloud : décisions documentées, pas encore construites

:::

---

**Code source** : [github.com/cyril-bgs-dev-tech/aegis-rca](https://github.com/cyril-bgs-dev-tech/aegis-rca)
**Projet frère** : [vigilance](../vigilance/) (le système qu'Aegis-RCA investigue)
**Dernière mise à jour** : juillet 2026
**Contact** : cyril.bgs.dev.tech@gmail.com
