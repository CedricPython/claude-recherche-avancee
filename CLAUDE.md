# Systeme de Recherche Ultra-Avance

## IDENTITE

Ce workspace est dedie a la realisation de recherches de niveau doctoral.
Le systeme utilise une architecture multi-agents pour produire des analyses
exhaustives, critiques et professionnellement formatees.

Modele recommande : **Claude Opus 4.5** pour toutes les taches de recherche.

---

## COMMANDES DISPONIBLES

| Commande | Description |
|----------|-------------|
| `/recherche [sujet]` | Lance une recherche complete ultra-approfondie (45-60 min) |
| `/recherche-rapide [sujet]` | Recherche simplifiee (15-20 min) |
| `/export [dossier]` | Regenere les documents DOCX/PDF d'une recherche existante |

---

## WORKFLOW DE RECHERCHE

### Phase 0 : Initialisation
1. **Analyser le sujet** pour detecter la categorie :
   - **Business** : marches, concurrence, strategies, startups, investissement
   - **Tech** : technologies, frameworks, architecture, IA, developpement
   - **Academique** : sciences, recherche, theories, publications
   - **Sante** : medical, pharmaceutique, bien-etre, traitements
   - **Juridique** : lois, reglementations, conformite, RGPD
   - **General** : autres sujets

2. **Creer le dossier** : `Recherches/[Categorie]/[Sujet-YYYYMMDD]/`

3. **Definir les axes de recherche** (5-10 axes thematiques)

### Phase 1 : Recherche Web Exhaustive
Sources a explorer systematiquement :
- **Web general** (WebSearch) : 15-25 requetes variees
- **Sites specialises** (WebFetch) : sources autoritaires
- **Donnees recentes** : actualites des 6 derniers mois
- **Donnees historiques** : contexte et evolution
- **Sources academiques** : etudes, rapports, publications

### Phase 2 : Analyse Critique
- Verification des sources (fiabilite, biais potentiels)
- Croisement des informations (minimum 2 sources par affirmation)
- Identification des consensus et controverses
- Detection des lacunes dans les donnees

### Phase 3 : Synthese et Structuration
- **Tableau de synthese** avec points cles
- **Mind map** des concepts interconnectes
- **Bibliographie** formatee APA/Harvard
- **TODO liste** avec contacts pertinents
- **Executive summary** (1 page)

### Phase 4 : Redaction du Rapport
Structure du rapport final :
1. Executive Summary (1 page)
2. Table des matieres
3. Introduction et contexte
4. Methodologie de recherche
5. Analyse principale (sections thematiques)
6. Tableau de synthese
7. Mind map conceptuel
8. Conclusions et recommandations
9. Bibliographie (APA)
10. Annexes (TODO, contacts, ressources)

### Phase 5 : Generation Documents
- Export Markdown vers DOCX via `python scripts/generate_docx.py`
- Export Markdown vers PDF via `python scripts/generate_pdf.py`

---

## CRITERES DE QUALITE

- [ ] Minimum **20 sources** citees
- [ ] Toutes les affirmations **sourcees**
- [ ] **Analyse critique** presente
- [ ] Vision **equilibree** (pour/contre)
- [ ] **Recommandations actionnables**
- [ ] Format **professionnel**

---

## AGENTS DISPONIBLES

| Agent | Role | Fichier |
|-------|------|---------|
| Coordinateur | Orchestration globale et controle qualite | `agents/coordinateur.md` |
| Web Researcher | Recherche web exhaustive (15-25 requetes) | `agents/web-researcher.md` |
| Analyseur Critique | Verification sources et detection biais | `agents/analyseur-critique.md` |
| Synthetiseur | Tableaux, mind map, bibliographie | `agents/synthetiseur.md` |
| Redacteur | Rapport final et executive summary | `agents/redacteur.md` |

---

## STRUCTURE DES DOSSIERS DE RECHERCHE

```
Recherches/[Categorie]/[Sujet-YYYYMMDD]/
├── rapport.md              # Rapport complet
├── rapport.docx            # Version Word
├── rapport.pdf             # Version PDF
├── executive-summary.md    # Resume 1 page
├── mindmap.md              # Arborescence concepts
├── bibliographie.md        # Sources APA (20+)
└── todo-contacts.md        # Actions et contacts
```

---

## OUTILS NATIFS UTILISES

- **WebSearch** : Recherches web structurees
- **WebFetch** : Extraction contenu pages specifiques
- **Task** : Agents specialises en arriere-plan
- **TodoWrite** : Suivi progression
- **Bash** : Execution scripts Python pour export
- **Write/Edit** : Creation et modification fichiers

---

## LANGUES

- **Interface et rapports** : Francais
- **Recherches** : Francais + Anglais (si pertinent)
- **Bibliographie** : Langue originale des sources

---

## EXEMPLE D'UTILISATION

```
/recherche Impact de l'IA generative sur le marche de l'emploi en France 2024-2030
```

**Resultat attendu** :
- Categorie detectee : Business/Tech
- 8 axes de recherche definis
- 30+ sources analysees
- Rapport de 15-20 pages
- Executive summary 1 page
- Mind map avec 5 branches principales
- Bibliographie 30+ references
- TODO avec 10+ contacts (DRH, economistes, chercheurs)
- Temps total : 45-60 minutes
