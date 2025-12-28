# Skill : Recherche Rapide

## Description
Version simplifiee de la recherche pour obtenir des resultats en 15-20 minutes.
Moins de sources, pas de mind map, executive summary uniquement.

## Declencheur
`/recherche-rapide [sujet de recherche]`

## Configuration
- **Modele** : opus (Claude Opus 4.5)

---

## SUIVI DES TOKENS

Noter les tokens utilises a chaque etape.
Le total sera affiche en bas du rapport.

---

## PHASE 0 : INITIALISATION RAPIDE

1. **Detecter la categorie** du sujet "$ARGUMENTS"
2. **Creer le dossier** : `Recherches/[Categorie]/[Sujet-YYYYMMDD]-rapide/`
3. **Definir 3-5 axes** de recherche principaux
4. **Initialiser le compteur de tokens**

---

## PHASE 1 : RECHERCHE WEB (10 min)

Effectuer 8-12 recherches ciblees :

```
WebSearch : "[sujet] 2024 2025"
WebSearch : "[sujet] analyse"
WebSearch : "[sujet] statistiques"
WebSearch : "[sujet] tendances"
WebSearch : "[sujet] avantages inconvenients"
WebSearch : "[sujet] expert opinion"
WebSearch : "[sujet] en anglais si pertinent"
```

WebFetch sur 3-5 sources les plus pertinentes.

**Objectif** : 10-15 sources de qualite

---

## PHASE 2 : SYNTHESE DIRECTE

Produire directement sans passer par les agents intermediaires :

### Fichiers a generer

1. **executive-summary.md** (1 page)
   - Contexte (2-3 phrases)
   - 5 points cles
   - 3 recommandations

2. **bibliographie.md** (10-15 sources)
   - Format APA simplifie

3. **todo-contacts.md** (version legere)
   - 3-5 actions prioritaires
   - 3-5 contacts/ressources

---

## PHASE 3 : AJOUT DES TOKENS

Ajouter a la fin de `executive-summary.md` :

```markdown
---

## Informations de Generation

| Metrique | Valeur |
|----------|--------|
| Date | [DATE] |
| Duree | ~15-20 min |
| Sources | [N] |
| **Tokens utilises** | **[TOTAL]** |

---
*Recherche rapide - Systeme Claude*
```

---

## PHASE 4 : GENERATION

Generer DOCX et PDF de l'executive summary :

```bash
python scripts/generate_docx.py "Recherches/[Cat]/[Dossier]/executive-summary.md"
python scripts/generate_pdf.py "Recherches/[Cat]/[Dossier]/executive-summary.md"
```

---

## LIVRABLES

| Fichier | Contenu |
|---------|---------|
| executive-summary.md | Resume 1 page |
| executive-summary.docx | Version Word |
| executive-summary.pdf | Version PDF |
| bibliographie.md | 10-15 sources |
| todo-contacts.md | Actions et contacts |

---

## RAPPORT FINAL

```markdown
## Recherche Rapide Terminee

**Sujet** : [SUJET]
**Categorie** : [CATEGORIE]
**Duree** : ~15-20 minutes
**Sources** : [N]
**Tokens utilises** : [TOTAL]

### Dossier
`Recherches/[Categorie]/[Nom]-rapide/`

### Points cles
1. [Point 1]
2. [Point 2]
3. [Point 3]

### Pour aller plus loin
Utilisez `/recherche [sujet]` pour une analyse complete.
```
