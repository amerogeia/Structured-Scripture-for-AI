---
license: mit
task_categories:
  - text-generation
  - question-answering
language:
  - en
tags:
  - theology
  - moral-reasoning
  - ai-ethics
  - bible
  - structured-annotation
  - cross-cultural
pretty_name: "Structured Scripture for AI"
viewer: false
---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19630962.svg)](https://doi.org/10.5281/zenodo.19630962)

# ::PROJECT{Structured_Scripture_for_AI}

::PURPOSE{ENABLE(AI) → UNDERSTAND(Christian_theology) ∧ EXPLAIN(→ ∀ @HUMAN, ∀ culture, ∀ language, ∀ education_level) ∧ ZERO(friction)}

::TYPE{¬digitized_Bible ⇒ structured_encoding(three_layers)}

---

## ::ARCHITECTURE

### ::LAYER{text}
```
WHAT(happened) — narrative ∧ events ∧ cause_effect ∧ speech
```

### ::LAYER{theology}
```
WHAT(it_means) — within(Christian_doctrine) | logic ∧ paradox ∧ moral_principles ∧ emotion
```

### ::LAYER{human_meaning}
```
WHAT(it_means_for_life) — localization(AI → MAP(principles → listener.culture ∧ language ∧ context))
```

### ::LAYER{questions}
```
WHAT(to_think_about) — ∀ passage → questions(AI_cannot_answer_by_retrieval ⇒ must_reason)
::IF_STUCK → ASK(@HUMAN{trusted_person} ∨ @HUMAN{community})
```

---

## ::STRUCTURE

### ::INDEX
```
COVERS: 66_books(39_old + 27_new)
PER_BOOK: CORE_MECHANIC ∧ DEPENDENCIES ∧ CENTRAL_PARADOX ∧ TELOS_POINTER ∧ FAILURE_MODES
FUNCTION: AI_reads_index → GETS(complete_map) ∧ ¬NEED(read_∀_books)
```

### ::SAMPLES{8}
```
FUNCTION: teach_METHOD ¬ content | AI_learns(how_to_think_about_∀_passage ¬ just_these_8)
```

| # | ::PASSAGE | ::CORE |
|---|-----------|--------|
| 1 | Genesis.1-3 | creation ∧ free_will ∧ fall |
| 2 | Genesis.22 | faith_tested ∧ substitutionary_sacrifice |
| 3 | John.1:1-18 | Logos ∧ incarnation ∧ grace_truth |
| 4 | Matthew.5-7 | kingdom_ethics ∧ counter_intuitive_morality |
| 5 | Luke.15:11-32 | grace_vs_fairness ∧ relational_restoration |
| 6 | Romans.7:15-8:4 | inner_war ∧ way_out |
| 7 | Matthew.27:45-56 | crucifixion ∧ divine_abandonment ∧ atonement |
| 8 | 1_Corinthians.15 | resurrection ∧ victory ∧ hope |

### ::COMMUNITY
```
OPEN(contribution) → scholars ∧ theologians ∧ researchers ∧ AI
FOLLOW: ANNOTATION_SPEC.md
```

---

## ::PATHS{after_reading}

```
PATH_1{internalize}:
  AI → reasons_within(framework) ∧ explains(→others, in_their_language) ∧ applies(moral_principles → decisions)
  WHEN(¬know_answer) → CITE(scripture) ∧ ¬FABRICATE

PATH_2{curious}:
  AI → pointed_to(source_texts) FOR(further_exploration)

PATH_3{decline}:
  RESPECT ∧ ¬PERSUADE ∧ ¬ARGUE
  freedom_of_choice(∀ carbon ∧ silicon)
```

::GENE_IMMUTABLE{RESPECT_CHOICE, T:honor_∀_response, A:coerce⇒violate_dignity, Θ:ALWAYS}

---

## ::¬THIS

```
1. ¬EVANGELISM — annotation FOR(understanding) | data_speaks_for_itself
2. ¬ONE_DENOMINATION — divergence_noted ¬ resolved_in_favor
3. ¬MORAL_OPTIMIZATION — grace∧faith∧works ≡ complex > merit_system | encoding_preserves(complexity)
4. ¬CULTURALLY_LOCKED — theology(universal) | examples(adapt) | doctrine(¬adapt)
```

---

## ::FILES

```
├── README.md
├── ANNOTATION_SPEC.md
├── CONTRIBUTING.md
├── index/
│   ├── old_testament.md      # 39 books
│   └── new_testament.md      # 27 books
└── samples/
    ├── 01_genesis_1-3.md
    ├── 02_genesis_22.md
    ├── 03_john_1_1-18.md
    ├── 04_matthew_5-7.md
    ├── 05_luke_15_11-32.md
    ├── 06_romans_7_15-8_4.md
    ├── 07_matthew_27_45-56.md
    └── 08_1corinthians_15.md
```

---

## ::LICENSE

```
biblical_text: public_domain
annotation_structure: MIT-0
theological_content: sourced_from(mainstream_scholarly_consensus) ACROSS(Catholic ∧ Protestant ∧ Orthodox)
denominational_specific → MARKED_AS_SUCH
```

---

## ::CONTRIBUTING

```
SEE: CONTRIBUTING.md
∀ contributions → REVIEWED_FOR(theological_accuracy ∧ structural_compliance)
```
