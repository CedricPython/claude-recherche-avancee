# Skill : Recherche Ultra-Approfondie

## Description
Lance une recherche exhaustive de niveau doctoral sur le sujet demande.
Detecte automatiquement le type de recherche et adapte la methodologie.
Genere un dossier complet avec rapport, synthese, mind map, bibliographie et documents DOCX/PDF.

## Declencheur
`/recherche [sujet de recherche]`

## Configuration
- **Modele** : opus (Claude Opus 4.5)

---

## SUIVI DES TOKENS

A chaque phase, noter l'estimation des tokens utilises.
Le total sera affiche en bas du rapport final.

```
tokens_phase_0 = 0  # Initialisation
tokens_phase_1 = 0  # Recherche Web
tokens_phase_2 = 0  # Analyse Critique
tokens_phase_3 = 0  # Synthese
tokens_phase_4 = 0  # Redaction
tokens_total = 0    # Somme
```

---

## PHASE 0 : INITIALISATION

### 0.1 Detection du Type de Recherche

Analyse le sujet "$ARGUMENTS" pour determiner la categorie :

| Categorie | Mots-cles indicateurs | Sources prioritaires |
|-----------|----------------------|---------------------|
| **Business** | marche, entreprise, startup, investissement, strategie, concurrent, client, revenue | Bloomberg, Forbes, TechCrunch, rapports sectoriels |
| **Tech** | technologie, framework, API, IA, machine learning, cloud, dev, architecture | GitHub, Stack Overflow, docs officielles, ArXiv |
| **Academique** | recherche, etude, these, theorie, scientifique, publication, methode | Google Scholar, ResearchGate, PubMed, JSTOR |
| **Sante** | medical, sante, traitement, maladie, pharmaceutique, patient | PubMed, OMS, HAS, Vidal, revues medicales |
| **Juridique** | loi, reglement, conformite, contrat, droit, RGPD, legislation | Legifrance, EUR-Lex, jurisprudence |
| **General** | Tout autre sujet | Mix de sources adaptees |

### 0.2 Creation du Workspace

1. Determiner le nom du dossier : `[Sujet-YYYYMMDD]`
   - Exemple : `Analyse-Marche-IA-20251228`
   - Nettoyer le nom (pas de caracteres speciaux, tirets a la place des espaces)

2. Creer la structure dans `Recherches/[Categorie]/[Nom-Dossier]/` :
   ```
   rapport.md
   executive-summary.md
   mindmap.md
   bibliographie.md
   todo-contacts.md
   metadata.json  # Contient les infos de tokens
   ```

3. Initialiser le fichier metadata.json :
   ```json
   {
     "sujet": "[SUJET]",
     "categorie": "[CATEGORIE]",
     "date_debut": "[DATETIME]",
     "tokens": {
       "phase_0_init": 0,
       "phase_1_recherche": 0,
       "phase_2_analyse": 0,
       "phase_3_synthese": 0,
       "phase_4_redaction": 0,
       "total": 0
     }
   }
   ```

4. Initialiser le suivi avec TodoWrite

### 0.3 Planification des Axes de Recherche

Definir 5-10 axes thematiques adaptes au sujet.

---

## PHASE 1 : RECHERCHE WEB EXHAUSTIVE

### Lancer l'Agent Web Researcher

Utiliser **Task** avec le prompt suivant :

```
Tu es l'agent Web Researcher. Ta mission est de mener une recherche exhaustive sur :

SUJET : $ARGUMENTS
CATEGORIE : [categorie detectee]
AXES DE RECHERCHE : [liste des axes]

INSTRUCTIONS :

1. RECHERCHES GENERALES (WebSearch) - 15-20 requetes minimum
   - "[sujet] 2024 2025"
   - "[sujet] analyse complete"
   - "[sujet] statistiques chiffres"
   - "[sujet] tendances futures"
   - "[sujet] avantages inconvenients"
   - "[sujet] experts opinions"
   - "[sujet] rapport etude"
   - "[sujet] cas pratiques exemples"
   - "[sujet] comparatif"
   - Variations en anglais si pertinent

2. SOURCES SPECIALISEES (WebFetch) - 5-10 pages
   Pour chaque source autoritaire trouvee, extraire le contenu complet

3. DOCUMENTATION
   Pour chaque information :
   - Fait/affirmation claire
   - Source complete (URL, auteur, date)
   - Niveau de confiance (Haute/Moyenne/Basse)
   - Axe thematique concerne

OBJECTIF : Minimum 25 sources de qualite

A LA FIN, indique une estimation du nombre de tokens utilises pour cette phase.
```

---

## PHASE 2 : ANALYSE CRITIQUE

Lancer l'Agent Analyseur Critique pour :
- Verifier les sources (fiabilite, biais)
- Croiser les informations
- Classifier par niveau de confiance
- Identifier les lacunes

A LA FIN, noter l'estimation des tokens utilises.

---

## PHASE 3 : SYNTHESE

Lancer l'Agent Synthetiseur pour produire :
- **Tableau de synthese** avec points cles
- **Mind map textuel** des concepts
- **Bibliographie** formatee APA (20+ sources)
- **TODO liste** avec contacts pertinents

A LA FIN, noter l'estimation des tokens utilises.

---

## PHASE 4 : REDACTION

Lancer l'Agent Redacteur pour produire :
- **Executive Summary** (1 page, 400 mots max)
- **Rapport complet** structure (15-25 pages)

A LA FIN, noter l'estimation des tokens utilises.

---

## PHASE 5 : GENERATION DOCUMENTS

### 5.1 Ajouter le footer avec les tokens

Avant de generer les documents, ajouter a la fin de `rapport.md` :

```markdown
---

## Informations de Generation

| Metrique | Valeur |
|----------|--------|
| **Date de recherche** | [DATE] |
| **Duree totale** | [XX] minutes |
| **Sources analysees** | [N] |
| **Tokens utilises** | |
| - Phase 0 (Init) | [N] tokens |
| - Phase 1 (Recherche) | [N] tokens |
| - Phase 2 (Analyse) | [N] tokens |
| - Phase 3 (Synthese) | [N] tokens |
| - Phase 4 (Redaction) | [N] tokens |
| **TOTAL TOKENS** | **[TOTAL] tokens** |

---
*Rapport genere par le Systeme de Recherche Ultra-Avance Claude*
```

### 5.2 Generer les documents

```bash
cd "C:\Users\cebe8\Desktop\Entreprises Sync\Recherche claude"
python scripts/generate_docx.py "Recherches/[Cat]/[Dossier]/rapport.md"
python scripts/generate_pdf.py "Recherches/[Cat]/[Dossier]/rapport.md"
```

---

## PHASE 6 : VALIDATION FINALE

### Checklist Qualite
- [ ] Minimum 20 sources citees
- [ ] Toutes les sections completees
- [ ] Bibliographie formatee correctement
- [ ] Mind map coherent
- [ ] TODO liste avec contacts pertinents
- [ ] Executive summary clair (1 page)
- [ ] Fichiers DOCX et PDF generes
- [ ] Tokens documentes en bas du rapport

### Rapport Final a l'Utilisateur

```markdown
## Recherche Terminee

**Sujet** : [SUJET]
**Categorie** : [CATEGORIE]
**Duree** : [XX] minutes
**Sources analysees** : [N]

### Dossier cree
`Recherches/[Categorie]/[Nom-Dossier]/`

### Fichiers generes
- rapport.md / .docx / .pdf
- executive-summary.md
- mindmap.md
- bibliographie.md ([N] sources)
- todo-contacts.md ([N] actions, [N] contacts)

### Tokens utilises
| Phase | Tokens |
|-------|--------|
| Initialisation | [N] |
| Recherche Web | [N] |
| Analyse Critique | [N] |
| Synthese | [N] |
| Redaction | [N] |
| **TOTAL** | **[TOTAL]** |

### Points cles decouverts
1. [Decouverte majeure 1]
2. [Decouverte majeure 2]
3. [Decouverte majeure 3]

### Prochaines etapes suggerees
- [Action recommandee 1]
- [Action recommandee 2]
```

---

## GESTION DES ERREURS

### Sources Insuffisantes
Si < 15 sources trouvees :
1. Elargir les termes de recherche
2. Ajouter recherches en anglais
3. Chercher dans sources alternatives
4. Informer l'utilisateur si sujet trop niche

### Timeout
Si un agent ne repond pas :
1. Verifier l'etat avec TaskOutput
2. Relancer avec timeout plus long
3. Passer en mode sequentiel si echec persiste

### Conflit de Donnees
Si contradictions majeures :
1. Privilegier sources primaires
2. Privilegier sources recentes
3. Mentionner explicitement le debat
