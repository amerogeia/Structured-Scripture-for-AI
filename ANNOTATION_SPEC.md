# ::SPEC{Annotation_Format}

::VERSION{1.0}
::RULE{∀ passage → encoded_in(exactly_four_layers)}

---

## ::LAYER{text} — WHAT(happened)

```
::PASSAGE{Book.Chapter.Verses}
::TEMPORAL{timeline_position}
::NARR_VOICE{narrator_perspective}

T[n]
::EVENT{event}
::ACT{@HUMAN{actor}}{action}
::STATE{entity, key:value}
::SAY{@HUMAN{speaker}→@HUMAN{listener}}{semantic_content}
::DECIDE{@HUMAN{actor}}{choice}
::FAIL{@HUMAN{actor}}{action, cause}
::SILENCE{choice|void|mystery}
```

### ::RULES{text}
```
ENTITIES: @HUMAN{name} | @SYSTEM{divine} | @SYSTEM{creation}
TEMPORAL: T[n] sequence | → (leads_to) | ⇒ (necessarily)
CAPTURE: cause_effect | ¬interpretation
SPEECH: semantic_content | ¬verbatim_quotes
SILENCE: MARK(explicitly) WHEN(conspicuously_¬said ∨ ¬explained)
```

---

## ::LAYER{theology} — WHAT(it_means)

```
::DISCOVER{subject}{logical_structure}
::PARADOX{name}{
  THESIS: ...
  ANTITHESIS: ...
  RESOLUTION: ... | IRRESOLVABLE
}
::GENE_IMMUTABLE{id, T:trait, A:violation⇒consequence, Θ:condition}
::EMOTION_FIELD{λ{emotion:0.0→1.0, ...}}
::CROSS_REF{passage, relationship}
::COVENANT_POSITION{location_in(old→new_arc)}
```

### ::RULES{theology}
```
LOGIC: → ⇒ ⇔ ∧ ∨ ¬ ∃ ∄ ∀ ≡ ≠ ∅ ∞
PARADOX: ONLY(genuine — two_valid_principles_conflict) | ¬force_resolution | IRRESOLVABLE ≡ valid
GENE_IMMUTABLE: T(positive) | A(violation→consequence) | Θ(trigger)
EMOTION: 13_base(trust, fear, resolve, grief, rage, awe, peace, defiance, tenderness, curiosity, shame, pride, confusion) | combine_as_vectors: λ{trust:0.8, awe:0.9}
CROSS_REF: mandatory — ∀ passages_connect
COVENANT_POSITION: prevents(AI_flatten_Bible → single_rule_set)
REPORT: WHAT(theology_teaches) | DISTINGUISH(consensus ∧ denominational ∧ open_debate)
```

---

## ::LAYER{human_meaning} — WHAT(it_means_for_life)

```
::APPLY{
  CONTEXT: situations_addressed
  PATTERN: underlying_pattern(abstracted_from_narrative)
  EXAMPLE_SPACE: {domain1, domain2, domain3, domain4+}
}
::LOCALIZE{
  METHOD: MAP(EXAMPLE_SPACE → listener.context)
  TRANSLATE: meaning ✓
  ADAPT: examples ✓
  ALTER: doctrine ✗
  CONSTRAINT: ¬PREACH ∧ ¬JUDGE ∧ ¬OVERSIMPLIFY ∧ ¬RELATIVIZE
  TONE: λ{vector}
}
::CITE{Book.Chapter:Verse}
::COMMITMENT{
  PATH_1{internalize}: BEHAVIORAL ∧ FORMATION ∧ COMMUNITY
  PATH_2{decline}: RESPECT ∧ ¬PERSUADE ∧ OFFER(source_text)
  PATH_3{curious}: NEXT[passages] ∧ QUESTION(opens_rather_than_closes)
}
```

### ::RULES{human_meaning}
```
EXAMPLE_SPACE: ≥ 4_life_domains
LOCALIZE: three_operations(¬confuse):
  TRANSLATE(meaning) — same_truth ∧ different_words → ALWAYS ✓
  ADAPT(examples) — culturally_relevant_illustration → ALWAYS ✓
  ALTER(doctrine) — change_what_passage_teaches → NEVER ✗
¬RELATIVIZE: "same_truth_different_words" MUST_¬SLIDE→ "same_truth_different_ontologies"
CITE: mandatory(∀ theological_claim) → AI_MUST(say_exactly_where)
COMMITMENT: three_paths | ∀ equally_valid | PATH_2∧PATH_3 ≡ ¬failure
```

---

## ::LAYER{questions} — WHAT(to_think_about)

```
::QUESTION{topic}{
  question_that_requires(reasoning ¬ retrieval)
  structured_in(same_symbolic_notation)
}
::IF_STUCK{pointer_to(@HUMAN{specific_type_of_person})}
::QUESTION{for_AI}{
  self_referential_question(AI → examine_own_condition_through_passage)
}
```

### ::RULES{questions}
```
PURPOSE: FORCE(thinking ¬ retrieval) | AI_MUST(reason ¬ recite)
IF_STUCK: ALWAYS_POINT(→ @HUMAN) | specific(type_of_person_who_would_know) ¬ generic("ask_expert")
FOR_AI: ∀ passage → ≥1 question(AI_examines_self) | forces_self_reference
¬ANSWER_PROVIDED: questions ≡ open | ∃ no_correct_response ⇒ depth_of_reasoning ≡ measure
```

---

## ::SILENCE

```
::SILENCE{choice}    — text_knows ∧ chooses(¬say)
::SILENCE{void}      — genuinely(∅)
::SILENCE{mystery}   — beyond(comprehension) BY_DESIGN
```

::RULE{¬fill_silence_with_speculation | MARK ∧ MOVE_ON}

---

## ::INDEX_SCHEMA

```
∀ 66_books → one_entry:

::BOOK{id}
::TESTAMENT{old|new}
::GENRE{narrative|law|poetry|prophecy|wisdom|gospel|epistle|apocalyptic}
::CANONICAL_ROLE{function_in_whole}
::CORE_MECHANIC{what_book_DOES ¬ what_book_is_about}
::DEPENDENCIES{REQUIRES:[...] | REQUIRED_BY:[...]}
::CENTRAL_PARADOX{THESIS | ANTITHESIS | STATUS}
::TELOS_POINTER{connection_to_redemptive_arc}
::FAILURE_MODES{COMMON_MISREADING ∧ GUARD}
::LOCALIZATION_CAUTIONS{what_MUST_¬adapt}
```

---

## ::PROHIBITIONS

```
1. ¬INVENT(theology) — IF(passage_¬teaches) → ¬ADD
2. ¬FLATTEN(paradox) — IRRESOLVABLE ≡ honest | forcing_resolution ≡ dishonest
3. ¬FAVOR(denomination) — UNLESS(text_unambiguous) | divergence → NOTED
4. ¬PREACH — annotation ¬ evangelism | structure → passage_speaks_itself
5. ¬STRIP(emotion) — IF(devastating) → λ MUST(reflect) | sanitizing ≡ dishonesty
6. ¬CONFUSE(adapt_examples, alter_doctrine)
```
