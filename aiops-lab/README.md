# 🏗️ AIOps Lab : plateforme d'infrastructure de recherche

**En une phrase** : une plateforme d'infrastructure entièrement décrite par le code, qu'on peut détruire et reconstruire hors ligne, et dont chaque étape n'est déclarée finie qu'avec une preuve.

**Contexte** : projet personnel  
**Période** : juillet 2026, en cours  
**Organisation** : 9 phases, chacune fermée par une porte de validation

**Où en est ce projet** (état au 5 octobre 2026) :

- ✅ 6 portes sur 9 fermées, dont la livraison vérifiée (1er octobre 2026)
- 🚧 7e porte en cours : plateforme IA et connaissances, 4 livrables sur 11 terminés

---

## 🧑‍💼 Vue d'ensemble

**Le problème** : une infrastructure qu'on ne sait pas reconstruire depuis zéro n'est pas maîtrisée. On croit qu'elle est décrite par le code, jusqu'au jour où il faut la remonter et qu'une étape manuelle oubliée bloque tout.

**Ce que fait le projet** : il construit une plateforme Kubernetes pilotée en GitOps, puis la met à l'épreuve pour de vrai : destruction complète, reconstruction hors ligne, mise à jour sous charge, refus des déploiements non conformes.

**Ce que ça démontre** : une approche de l'infrastructure fondée sur la preuve. Chaque porte n'est fermée qu'avec des éléments vérifiables, pas sur une impression que « ça marche ».

## Une plateforme reconstruite depuis le code

```{mermaid}
flowchart LR
    A["Code<br/>Terraform, Helm"] --> B["Cluster K3s"]
    B --> C["Argo CD<br/>GitOps"]
    C --> D["Control plane<br/>servi par digest"]
    E["Registre OCI local"] --> D
    F["CI hors ligne<br/>scan, SBOM, signature"] --> E
    B --> G["Prometheus, Grafana<br/>SLO"]
```

---

## 📊 Ce qui a été prouvé

| Épreuve | Résultat |
|---|---|
| Reconstruction | infrastructure **détruite pour de vrai** puis reconstruite hors ligne depuis le code |
| Exécution de référence | rejouée **réseau coupé**, zéro trafic sortant mesuré |
| Chaîne de livraison hors ligne | image, scan Trivy (**zéro faille haute ou critique**), SBOM de 51 composants, signature Cosign |
| Mise à jour sous charge | rolling update, **864 requêtes, 0 échec** |
| Politiques d'admission | **7 politiques**, chacune prouvée par un rejet réel |
| Porte « livraison vérifiée » | validation agrégée **passée** le 1er octobre 2026 |

---

## 🔬 Méthode

- **Portes de validation** : une phase n'est close qu'avec ses preuves archivées.
- **Hors ligne par conception** : registre OCI local, chaîne de livraison sans accès extérieur.
- **Livraison par digest** : ce qui tourne dans le cluster est identifié par son empreinte, pas par une étiquette modifiable.
- **Observabilité** : Prometheus, Grafana et objectifs de service (SLO).

---

## 🛠️ Stack technique

| Catégorie | Technologies |
|---|---|
| **Orchestration** | Kubernetes (K3s), Helm |
| **Infrastructure as Code** | Terraform |
| **GitOps** | Argo CD |
| **Observabilité** | Prometheus, Grafana |
| **Chaîne d'approvisionnement** | Trivy, SBOM, Cosign, registre OCI local |
| **Conteneurs** | Docker |

---

## 🎯 Compétences démontrées

- **Infrastructure as Code** et GitOps
- **Sécurité de la chaîne de livraison** : scan, inventaire logiciel, signature, admission
- **Fiabilité** : reconstruction prouvée, mise à jour sans interruption mesurée
- **Rigueur** : avancement découpé en portes, chaque affirmation appuyée par une preuve

---

**Code source** : dépôt privé, accès sur demande  
**Dernière mise à jour** : novembre 2026  
**Contact** : cyril.bgs.dev@gmail.com
