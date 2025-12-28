# Système de Recherche Ultra-Avancé avec Claude Code

Un système de recherche de niveau doctoral, adaptatif et autonome, utilisant Claude Code pour mener des recherches exhaustives et générer des rapports professionnels.

## Fonctionnalités

- **Recherche multi-agents** : 5 agents spécialisés (Web Researcher, Analyseur Critique, Synthétiseur, Rédacteur, Coordinateur)
- **Détection automatique** du type de recherche (Business, Tech, Académique, Santé, Juridique, Général)
- **20+ sources** analysées et croisées
- **Génération automatique** de rapports DOCX et PDF
- **Suivi des tokens** utilisés par recherche

## Commandes Disponibles

| Commande | Description | Durée |
|----------|-------------|-------|
| `/recherche [sujet]` | Recherche complète ultra-approfondie | 45-60 min |
| `/recherche-rapide [sujet]` | Recherche express | 15-20 min |
| `/export [dossier]` | Régénérer les documents DOCX/PDF | 2 min |

## Installation

### Prérequis

- [Claude Code](https://claude.ai/code) installé
- Python 3.8+
- Node.js (optionnel, pour génération PDF)

### Dépendances Python

```bash
pip install -r scripts/requirements.txt
```

### Pour la génération PDF (optionnel)

```bash
# Option A : md-to-pdf (recommandé)
npm install -g md-to-pdf

# Option B : Pandoc
winget install JohnMacFarlane.Pandoc
```

## Utilisation

1. Ouvrez ce dossier avec Claude Code
2. Lancez une recherche :

```
/recherche Impact de l'IA générative sur le marché de l'emploi en France
```

3. Les résultats seront dans `Recherches/[Catégorie]/[Sujet-Date]/`

## Structure des Livrables

Chaque recherche génère :

```
Recherches/Business/Mon-Sujet-20251228/
├── rapport.md          # Rapport complet (15-25 pages)
├── rapport.docx        # Version Word
├── rapport.pdf         # Version PDF
├── executive-summary.md # Résumé 1 page
├── mindmap.md          # Arborescence des concepts
├── bibliographie.md    # 20+ sources format APA
└── todo-contacts.md    # Actions et contacts pertinents
```

## Structure du Projet

```
.
├── .claude/
│   ├── commands/       # Skills (/recherche, /recherche-rapide, /export)
│   └── settings.local.json
├── agents/             # 5 agents spécialisés
├── templates/          # Modèles de documents
├── scripts/            # Scripts Python (DOCX, PDF)
├── Recherches/         # Dossiers de recherche générés
└── CLAUDE.md           # Configuration du projet
```

## Mode Ultrathink

Pour une réflexion très approfondie, ajoutez `ultrathink` au début :

```
ultrathink /recherche Analyse approfondie du marché
```

## Licence

MIT
