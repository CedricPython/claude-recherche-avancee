# Skill : Export Documents

## Description
Regenere les documents DOCX et PDF a partir d'un dossier de recherche existant.
Utile apres modification manuelle des fichiers Markdown.

## Declencheur
`/export [chemin du dossier]`

## Exemples
```
/export Recherches/Business/Analyse-Marche-IA-20251228
/export Recherches/Tech/Framework-React-20251228
```

---

## INSTRUCTIONS

### Verification du Dossier

1. Verifier que le dossier "$ARGUMENTS" existe
2. Verifier la presence des fichiers Markdown :
   - rapport.md (principal)
   - executive-summary.md
   - Autres fichiers optionnels

### Generation des Documents

Pour chaque fichier .md present :

```bash
cd "C:\Users\cebe8\Desktop\Entreprises Sync\Recherche claude"

# Rapport principal
python scripts/generate_docx.py "$ARGUMENTS/rapport.md"
python scripts/generate_pdf.py "$ARGUMENTS/rapport.md"

# Executive summary
python scripts/generate_docx.py "$ARGUMENTS/executive-summary.md"
python scripts/generate_pdf.py "$ARGUMENTS/executive-summary.md"
```

### Rapport

```markdown
## Export Termine

**Dossier** : $ARGUMENTS

### Fichiers generes
- rapport.docx
- rapport.pdf
- executive-summary.docx
- executive-summary.pdf

### Emplacement
Les fichiers sont dans le meme dossier que les sources Markdown.
```

---

## GESTION DES ERREURS

### Dossier non trouve
```
Erreur : Le dossier "$ARGUMENTS" n'existe pas.

Dossiers disponibles :
[lister les dossiers dans Recherches/]
```

### Fichiers manquants
```
Attention : Certains fichiers source sont manquants.

Fichiers trouves :
- [liste des .md presents]

Fichiers manquants :
- [liste des .md absents]

Generation partielle effectuee.
```

### Erreur de generation
```
Erreur lors de la generation de [fichier].

Cause possible :
- Python non installe
- Dependances manquantes (pip install python-docx)
- Erreur de syntaxe dans le Markdown

Solution :
1. Verifier l'installation : pip show python-docx
2. Installer si necessaire : pip install python-docx markdown
3. Verifier le fichier Markdown source
```
