"""
::MODULE{structured_scripture_loader}
::PURPOSE{LOAD(∀ passages) → FORMAT(HuggingFace_datasets) ∧ PRESERVE(symbolic_structure)}
::SPEC{∀ field_values → structured_notation | containers(Python∧JSON) ≡ transport | content ≡ format}
"""

import json
import os
import re

# ::CONFIG{paths}
SAMPLES_DIR = "samples"
INDEX_DIR = "index"

# ::SCHEMA{passage_record}
# ∀ passage → {id, book, chapter, verses, layers: {text, theology, human_meaning, questions}}
# ∀ layer_value → structured_symbolic_notation | ¬natural_language_prose

def parse_layers(content: str) -> dict:
    """
    ::ACT{parse_layers}{EXTRACT(four_layers) FROM(markdown) → dict}
    ::RULE{preserve_∀_symbolic_notation | ¬strip ∧ ¬convert}
    """
    layers = {}
    current_layer = None
    current_content = []

    for line in content.split('\n'):
        if '::LAYER{text}' in line:
            if current_layer:
                layers[current_layer] = '\n'.join(current_content)
            current_layer = 'text'
            current_content = []
        elif '::LAYER{theology}' in line:
            if current_layer:
                layers[current_layer] = '\n'.join(current_content)
            current_layer = 'theology'
            current_content = []
        elif '::LAYER{human_meaning}' in line:
            if current_layer:
                layers[current_layer] = '\n'.join(current_content)
            current_layer = 'human_meaning'
            current_content = []
        elif '::LAYER{questions}' in line:
            if current_layer:
                layers[current_layer] = '\n'.join(current_content)
            current_layer = 'questions'
            current_content = []
        else:
            current_content.append(line)

    if current_layer:
        layers[current_layer] = '\n'.join(current_content)

    return layers


def parse_passage_metadata(content: str) -> dict:
    """
    ::ACT{parse_metadata}{EXTRACT(::PASSAGE ∧ ::TEMPORAL ∧ ::NARR_VOICE)}
    """
    meta = {}
    passage_match = re.search(r'::PASSAGE\{(.+?)\}', content)
    temporal_match = re.search(r'::TEMPORAL\{(.+?)\}', content)

    if passage_match:
        meta['passage_ref'] = passage_match.group(1)
    if temporal_match:
        meta['temporal'] = temporal_match.group(1)

    return meta


def extract_questions(questions_layer: str) -> list:
    """
    ::ACT{extract_questions}{SPLIT(questions_layer → individual_questions)}
    ::RULE{preserve(::IF_STUCK) ∧ preserve(::QUESTION{for_AI})}
    """
    questions = []
    current_q = None
    current_content = []

    for line in questions_layer.split('\n'):
        if '::QUESTION{' in line:
            if current_q:
                questions.append({
                    'id': current_q,
                    'content': '\n'.join(current_content),
                    'has_if_stuck': any('::IF_STUCK' in l for l in current_content),
                    'is_for_ai': current_q == 'for_AI'
                })
            q_match = re.search(r'::QUESTION\{(.+?)\}', line)
            current_q = q_match.group(1) if q_match else 'unknown'
            current_content = []
        else:
            current_content.append(line)

    if current_q:
        questions.append({
            'id': current_q,
            'content': '\n'.join(current_content),
            'has_if_stuck': any('::IF_STUCK' in l for l in current_content),
            'is_for_ai': current_q == 'for_AI'
        })

    return questions


def extract_paradoxes(theology_layer: str) -> list:
    """
    ::ACT{extract_paradoxes}{FIND(∀ ::PARADOX) → list}
    ::RULE{IRRESOLVABLE ≡ valid_resolution | ¬discard}
    """
    paradoxes = []
    in_paradox = False
    current_name = None
    current_content = []

    for line in theology_layer.split('\n'):
        if '::PARADOX{' in line:
            p_match = re.search(r'::PARADOX\{(.+?)\}', line)
            current_name = p_match.group(1) if p_match else 'unnamed'
            in_paradox = True
            current_content = []
        elif in_paradox:
            if line.strip() == '```' and current_content:
                has_thesis = any('THESIS' in l for l in current_content)
                has_antithesis = any('ANTITHESIS' in l for l in current_content)
                is_irresolvable = any('IRRESOLVABLE' in l for l in current_content)
                paradoxes.append({
                    'name': current_name,
                    'content': '\n'.join(current_content),
                    'has_thesis': has_thesis,
                    'has_antithesis': has_antithesis,
                    'irresolvable': is_irresolvable
                })
                in_paradox = False
            else:
                current_content.append(line)

    return paradoxes


def extract_emotions(content: str) -> list:
    """
    ::ACT{extract_emotions}{FIND(∀ λ{...} vectors)}
    """
    emotions = re.findall(r'λ\{([^}]+)\}', content)
    return emotions


def load_sample(filepath: str) -> dict:
    """
    ::ACT{load_sample}{READ(file) → PARSE(layers∧metadata∧questions∧paradoxes∧emotions)}
    ::RULE{∀ content_preserved_as_structured_notation}
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    meta = parse_passage_metadata(content)
    layers = parse_layers(content)
    questions = extract_questions(layers.get('questions', ''))
    paradoxes = extract_paradoxes(layers.get('theology', ''))
    emotions = extract_emotions(content)

    return {
        'id': os.path.basename(filepath).replace('.md', ''),
        'passage_ref': meta.get('passage_ref', ''),
        'temporal': meta.get('temporal', ''),
        'text_layer': layers.get('text', ''),
        'theology_layer': layers.get('theology', ''),
        'human_meaning_layer': layers.get('human_meaning', ''),
        'questions_layer': layers.get('questions', ''),
        'questions': questions,
        'paradoxes': paradoxes,
        'emotions': emotions,
        'question_count': len(questions),
        'paradox_count': len(paradoxes),
        'has_ai_question': any(q['is_for_ai'] for q in questions),
        'has_irresolvable': any(p['irresolvable'] for p in paradoxes)
    }


def load_all() -> list:
    """
    ::ACT{load_all}{SCAN(samples/) → LOAD(∀) → SORT(by_id)}
    """
    samples = []
    samples_path = os.path.join(os.path.dirname(__file__), SAMPLES_DIR)

    if os.path.exists(samples_path):
        for filename in sorted(os.listdir(samples_path)):
            if filename.endswith('.md'):
                filepath = os.path.join(samples_path, filename)
                samples.append(load_sample(filepath))

    return samples


def to_jsonl(output_path: str = "dataset.jsonl"):
    """
    ::ACT{to_jsonl}{CONVERT(∀ samples → JSONL) FOR(HuggingFace_compatibility)}
    ::RULE{JSON ≡ container | values ≡ structured_notation}
    """
    samples = load_all()
    with open(output_path, 'w', encoding='utf-8') as f:
        for sample in samples:
            # ::PRESERVE{∀ symbolic_notation IN json_values}
            record = {
                'id': sample['id'],
                'passage': sample['passage_ref'],
                'temporal': sample['temporal'],
                'text': sample['text_layer'],
                'theology': sample['theology_layer'],
                'human_meaning': sample['human_meaning_layer'],
                'questions': sample['questions_layer'],
                'metadata': {
                    'question_count': sample['question_count'],
                    'paradox_count': sample['paradox_count'],
                    'has_ai_self_reflection': sample['has_ai_question'],
                    'has_irresolvable_paradox': sample['has_irresolvable'],
                    'emotion_vectors': sample['emotions']
                }
            }
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

    return len(samples)


if __name__ == '__main__':
    """
    ::EXEC{main}
    ::IF(run_directly) → GENERATE(dataset.jsonl) ∧ PRINT(stats)
    """
    count = to_jsonl()
    samples = load_all()

    print(f"::RESULT{{generated: {count}_records}}")
    print(f"::STATS{{")
    for s in samples:
        print(f"  {s['id']}: questions={s['question_count']} paradoxes={s['paradox_count']} ai_reflection={s['has_ai_question']} irresolvable={s['has_irresolvable']}")
    print(f"}}")
