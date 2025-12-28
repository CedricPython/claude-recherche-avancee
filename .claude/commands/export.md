---
description: Regenere les documents DOCX/PDF d'une recherche existante
allowed-tools: Bash(*), Read(*), Write(*), Glob(*)
---

# Export Documents

Regenere les documents DOCX et PDF pour le dossier : **$ARGUMENTS**

## Instructions

1. Verifier que le dossier existe
2. Lister les fichiers .md presents
3. Generer les documents :

```bash
python scripts/generate_docx.py "$ARGUMENTS/rapport.md"
python scripts/generate_pdf.py "$ARGUMENTS/rapport.md"
python scripts/generate_docx.py "$ARGUMENTS/executive-summary.md"
python scripts/generate_pdf.py "$ARGUMENTS/executive-summary.md"
```

4. Confirmer les fichiers generes

## Exemple d'utilisation

```
/export Recherches/Business/Mon-Sujet-20251228
```
