# Configuration du Systeme de Recherche

**Version** : 1.1
**Derniere mise a jour** : 28 decembre 2025

---

## MODE DE RECHERCHE : ULTRA-APPROFONDI

Ce fichier definit les parametres OBLIGATOIRES pour toute recherche `/recherche`.
Ces parametres doivent etre respectes systematiquement.

---

## PARAMETRES QUANTITATIFS OBLIGATOIRES

### Phase 1 : Recherche Web

| Parametre | Minimum | Objectif | Maximum |
|-----------|---------|----------|---------|
| **WebSearch** (requetes) | 20 | 25 | 35 |
| **WebFetch** (pages analysees) | 8 | 12 | 20 |
| **Agents paralleles** | 2 | 3 | 5 |
| **Sources finales** | 25 | 30 | 50 |

### Phase 2 : Analyse

| Parametre | Obligatoire |
|-----------|-------------|
| Verification croisee | Minimum 2 sources par affirmation |
| Analyse critique | Biais, limites, contradictions |
| Donnees chiffrees | Tarifs, statistiques, dates |

### Phase 3 : Livrables

| Livrable | Obligatoire |
|----------|-------------|
| rapport.md | Oui - 15-25 pages |
| rapport.docx | Oui |
| rapport.pdf | Oui |
| executive-summary.md | Oui - 1 page max |
| mindmap.md | Oui |
| bibliographie.md | Oui - 25+ sources APA |
| todo-contacts.md | Oui - 10+ contacts |

---

## DUREE ESTIMEE PAR PHASE

| Phase | Duree min | Duree max |
|-------|-----------|-----------|
| Phase 0 : Initialisation | 2 min | 5 min |
| Phase 1 : Recherche Web | 20 min | 30 min |
| Phase 2 : Analyse | 10 min | 15 min |
| Phase 3 : Synthese | 5 min | 10 min |
| Phase 4 : Redaction | 10 min | 15 min |
| Phase 5 : Export | 2 min | 5 min |
| **TOTAL** | **45 min** | **60 min** |

---

## UTILISATION OBLIGATOIRE DES AGENTS

Pour garantir la profondeur, lancer des agents en parallele :

### Agent 1 : Recherche principale
```
Task(subagent_type="Explore", prompt="Rechercher [sujet] - sources principales")
```

### Agent 2 : Recherche tarifaire/chiffree
```
Task(subagent_type="Explore", prompt="Rechercher tarifs, prix, couts, statistiques pour [sujet]")
```

### Agent 3 : Recherche avis/temoignages
```
Task(subagent_type="Explore", prompt="Rechercher avis, temoignages, retours d'experience sur [sujet]")
```

---

## CHECKLIST AVANT CLOTURE

Avant de terminer une recherche, verifier :

- [ ] 20+ WebSearch effectuees
- [ ] 8+ WebFetch sur sites officiels
- [ ] 2+ agents lances en parallele
- [ ] Tarifs/prix documentes (si applicable)
- [ ] 25+ sources dans bibliographie
- [ ] PDF genere avec succes
- [ ] Duree totale >= 30 minutes

---

## CONFIGURATION TECHNIQUE

### Generation PDF

**Outil principal** : weasyprint (Python)
**Fallback** : md-to-pdf (Node.js) ou Pandoc

Installation requise :
```bash
pip install weasyprint markdown
```

### Dependances Python

```bash
pip install python-docx weasyprint markdown
```

---

## NOTES POUR L'ASSISTANT

1. **Ne jamais raccourcir** : Meme si le sujet semble simple, respecter les minimums
2. **Toujours chercher les tarifs** : Prix, couts, frais = information critique
3. **Agents paralleles** : Lancer au moins 2 agents pour diversifier les sources
4. **Verification PDF** : Tester la generation avant de conclure
5. **Transparence** : Si un parametre ne peut etre atteint, l'expliquer a l'utilisateur

---

## HISTORIQUE DES MODIFICATIONS

| Date | Version | Modification |
|------|---------|--------------|
| 28/12/2025 | 1.0 | Creation initiale |
| 28/12/2025 | 1.1 | Ajout parametres obligatoires, checklist, agents |
