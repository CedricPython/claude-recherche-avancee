---
description: Recherche express sur un sujet (15-20 min)
allowed-tools: Bash(*), Read(*), Write(*), Edit(*), WebSearch(*), WebFetch(*), TodoWrite(*), Glob(*), Grep(*)
---

# Recherche Rapide

Version express de la recherche sur : **$ARGUMENTS**

## PHASE 1 : INITIALISATION

1. Detecter la categorie du sujet
2. Creer le dossier : `Recherches/[Categorie]/[Sujet-YYYYMMDD]-rapide/`
3. Definir 3-5 axes de recherche principaux

## PHASE 2 : RECHERCHE WEB (10 min)

Effectuer 8-12 recherches ciblees :
- "[sujet] 2024 2025"
- "[sujet] analyse"
- "[sujet] statistiques"
- "[sujet] tendances"
- "[sujet] avantages inconvenients"
- "[sujet] en anglais si pertinent"

WebFetch sur 3-5 sources les plus pertinentes.

**Objectif** : 10-15 sources de qualite

## PHASE 3 : SYNTHESE DIRECTE

Produire directement :

1. **executive-summary.md** (1 page)
   - Contexte (2-3 phrases)
   - 5 points cles
   - 3 recommandations

2. **bibliographie.md** (10-15 sources format APA)

3. **todo-contacts.md** (version legere)
   - 3-5 actions prioritaires
   - 3-5 contacts/ressources

## PHASE 4 : GENERATION

```bash
python scripts/generate_docx.py "Recherches/[Cat]/[Dossier]/executive-summary.md"
python scripts/generate_pdf.py "Recherches/[Cat]/[Dossier]/executive-summary.md"
```

## RAPPORT FINAL

Afficher :
- Dossier cree
- Points cles (3-5)
- Sources (10-15)
- Tokens utilises
- Suggestion : "/recherche [sujet]" pour analyse complete
