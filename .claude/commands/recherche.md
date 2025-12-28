---
description: Lance une recherche ultra-approfondie sur un sujet (45-60 min)
allowed-tools: Bash(*), Read(*), Write(*), Edit(*), WebSearch(*), WebFetch(*), Task(*), TodoWrite(*), Glob(*), Grep(*)
---

# Recherche Ultra-Approfondie

Lance une recherche exhaustive de niveau doctoral sur : **$ARGUMENTS**

## PHASE 0 : INITIALISATION

### Detection du Type de Recherche

Analyse le sujet pour determiner la categorie :

| Categorie | Mots-cles indicateurs |
|-----------|----------------------|
| **Business** | marche, entreprise, startup, investissement, strategie, concurrent |
| **Tech** | technologie, framework, API, IA, machine learning, cloud, dev |
| **Academique** | recherche, etude, these, theorie, scientifique, publication |
| **Sante** | medical, sante, traitement, maladie, pharmaceutique |
| **Juridique** | loi, reglement, conformite, contrat, droit, RGPD |
| **General** | Tout autre sujet |

### Creation du Workspace

1. Creer le dossier : `Recherches/[Categorie]/[Sujet-YYYYMMDD]/`
2. Initialiser les fichiers : rapport.md, executive-summary.md, mindmap.md, bibliographie.md, todo-contacts.md

## PHASE 1 : RECHERCHE WEB EXHAUSTIVE

Effectuer 15-25 recherches WebSearch :
- "[sujet] 2024 2025"
- "[sujet] analyse complete"
- "[sujet] statistiques chiffres"
- "[sujet] tendances futures"
- "[sujet] avantages inconvenients"
- "[sujet] experts opinions"
- "[sujet] rapport etude"
- Variations en anglais si pertinent

Extraire 5-10 pages avec WebFetch sur les sources autoritaires.

**Objectif** : Minimum 25 sources de qualite

## PHASE 2 : ANALYSE CRITIQUE

- Verifier les sources (fiabilite, biais)
- Croiser les informations (min 2 sources par affirmation)
- Classifier par niveau de confiance (Haute/Moyenne/Basse)
- Identifier les lacunes

## PHASE 3 : SYNTHESE

Produire :
- **Tableau de synthese** avec points cles
- **Mind map textuel** des concepts
- **Bibliographie** formatee APA (20+ sources)
- **TODO liste** avec contacts pertinents

## PHASE 4 : REDACTION

Produire :
- **Executive Summary** (1 page, 400 mots max)
- **Rapport complet** structure (15-25 pages)

## PHASE 5 : GENERATION DOCUMENTS

Ajouter en fin de rapport les tokens utilises, puis generer :

```bash
python scripts/generate_docx.py "Recherches/[Cat]/[Dossier]/rapport.md"
python scripts/generate_pdf.py "Recherches/[Cat]/[Dossier]/rapport.md"
```

## RAPPORT FINAL

A la fin, afficher :
- Dossier cree
- Fichiers generes (rapport.md/.docx/.pdf, executive-summary.md, mindmap.md, bibliographie.md, todo-contacts.md)
- Nombre de sources
- Total tokens utilises
- 3 points cles decouverts
- Prochaines etapes suggerees
