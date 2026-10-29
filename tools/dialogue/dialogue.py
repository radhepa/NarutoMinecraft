"""Compiles the Leaf's dialogue into data/narutominecraft/dialogue/ (DIALOGUE.md).

Sources are plain text in Village Friends' dialogue format, extended with context tags, a function tag and kinds:

  tools/dialogue/lines/*.txt          handwritten pools
  tools/dialogue/generated/*.txt      pools written by compose.py (committed, reviewable; do not edit by hand)
  tools/dialogue/exchanges/*.txt      overheard talk between two residents
  tools/dialogue/questions/*.txt      questions residents ask the player, with 2-4 answers
  docs/story/dialogue/**/*.txt        story-gated pools (SPOILERS: the story bible's companion; compiled to story.json)

A pool heading names the pool, then context tags, then an optional Core condition:

    ## greet.time  time=evening  personality=fiery|playful  fn=react
    Evening already? I could go another round. [EXCLAIM]
    The lanterns are lit, {player}! ~lanterns_lit

    ## chat.village  fn=worldbuild  rank=!civilian | when: {"flag": "story.ch7.done"}

Tags: key=value, alternatives with |, negation with a leading !, numeric ranges for level (level=3..10).
Every heading needs fn= (or a file default "#! fn: worldbuild"): teach guide quest reveal_character deepen_bond
foreshadow worldbuild react callback hook commerce filler. kind= is line (the default: never repeated), repeat
(the repeatable set: "we already talked", closing lines), or cycle (barks, shop transactions, ambient: every line
once before any comes back). A line may end with [MOOD] and with ~group: lines sharing a group are one piece of
content in different voices, so once any is heard all are spent.

    python tools/dialogue/dialogue.py            # compile
    python tools/dialogue/dialogue.py --check    # validate and confirm the compiled files are current
    python tools/dialogue/dialogue.py --stats    # counts by pool family, kind and function
    python tools/dialogue/dialogue.py --report   # coverage matrix, filler mix and bond-key coverage
    python tools/dialogue/dialogue.py --lint FILE...   # validate some source files only (fast, for writers)
"""
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[1]
OUT = PROJECT / 'src/main/resources/data/narutominecraft/dialogue'
STORY = PROJECT / 'docs/story/dialogue'
LOCK = ROOT / 'ids.lock'
BOND_KEYS = ROOT / 'bond_keys.txt'
RULES = json.loads((ROOT / 'rules.json').read_text(encoding='utf-8'))

FUNCTIONS = {'teach', 'guide', 'quest', 'reveal_character', 'deepen_bond', 'foreshadow', 'worldbuild', 'react',
             'callback', 'hook', 'commerce', 'filler'}
KINDS = {'line', 'repeat', 'cycle'}
MOODS = {'EXCLAIM', 'QUESTION', 'HEART', 'NOTE', 'ANGER', 'SWEAT', 'DOTS', 'SLEEP', 'SPARKLE', 'IDEA', 'GLOOM', 'BLUSH'}
ARCHETYPES = ['warmhearted', 'thoughtful', 'playful', 'adventurous', 'meticulous', 'steadfast', 'reserved', 'imaginative',
              'pragmatic', 'curious', 'protective', 'gentle', 'proud', 'fiery', 'shy', 'stern']
NOBLE = ['senju', 'uzumaki', 'uchiha', 'hyuga', 'nara', 'akimichi', 'yamanaka', 'inuzuka', 'sarutobi', 'aburame', 'hatake',
         'kurama', 'shimura', 'yuhi', 'gekko']
MINOR = ['shiranui', 'morino', 'umino', 'haruno', 'namiashi', 'hagane', 'kinoshita', 'tsuchigumo', 'suzuran', 'tobari']
VALUES = {'loyalty', 'courage', 'kindness', 'honesty', 'duty', 'freedom', 'strength', 'knowledge', 'family', 'creativity'}
# Tones the bond engine resolves against the asker's traits (life/bonds AnswerTag, agreed with the bonds session).
TONES = {'warm', 'gentle', 'joking', 'teasing', 'stern', 'cold', 'kind', 'blunt', 'honest', 'loyal', 'ambitious', 'playful',
         'cautious', 'bold', 'humble', 'proud', 'dutiful', 'free', 'evasive', 'rude', 'curious', 'family'}
QUESTION_KINDS = {'opinion', 'dilemma', 'advice', 'preference', 'player_past', 'player_plans', 'confession'}

# Context tags a heading may test, and the values each takes (None: any snake_case word; 'int': a number or range).
TAGS = {
    'personality': set(ARCHETYPES), 'clan': set(NOBLE + MINOR), 'group': {'civilian', 'clanless', 'noble', 'minor'},
    'rank': {'civilian', 'academy', 'genin', 'chunin', 'jonin', 'anbu', 'kage'},
    'player_rank': {'academy', 'genin', 'chunin', 'jonin', 'anbu', 'hokage'},
    'stage': {'child', 'teen', 'adult'}, 'player_stage': {'child', 'teen', 'adult'},
    'gender': {'male', 'female', 'nonbinary'}, 'tier': {'cast', 'named', 'resident', 'passerby'},
    'level': 'int', 'band': {'stranger', 'acquaintance', 'friend', 'close', 'best'},
    'quarrel': {'none', 'argument', 'cold_shoulder', 'making_up', 'falling_out'},
    'time': {'dawn', 'morning', 'noon', 'afternoon', 'evening', 'night', 'late'},
    'weather': {'clear', 'rain', 'thunder', 'snow'}, 'season': {'spring', 'summer', 'autumn', 'winter'},
    'market': {'yes'}, 'same_clan': {'yes', 'no'}, 'clan_status': {'born', 'member', 'other', 'clanless'},
    'mood': {'festive', 'proud', 'calm', 'uneasy', 'tense', 'grieving'}, 'slice': {'beta1', 'beta2', 'beta3'},
    'event': {'leaf_festival', 'new_year', 'chunin_exams', 'graduation', 'clan_day', 'wedding', 'birthday',
              'border_incident', 'market_day', 'exam_week', 'first_snow', 'cherry_blossoms', 'moon_viewing'},
    'district': {'academy', 'market', 'main_street', 'residential', 'gate', 'hokage_rock', 'residence', 'training',
                 'hospital', 'shrine', 'river', 'clan_quarter', 'apartments', 'forest', 'stadium', 'outside',
                 'carpenters_lane', 'academy_streets', 'riverside', 'artists_lane', 'uchiha_quarter', 'stadium_streets'},
    'relation': {'friends', 'family', 'couple', 'coworkers', 'neighbors', 'rivals', 'clan', 'strangers', 'kids',
                 'shinobi', 'elders', 'parent_child', 'customers'},
    'player_temperament': {'bold', 'steady', 'cheerful', 'quiet', 'curious', 'stubborn'},
    'job': None, 'role': None, 'place': None, 'shop': None, 'part': None, 'speaker': None, 'habit': None,
    'deed': None, 'story': None,
}
WEIGHTS = RULES['tag_weights']
TOKENS = {'player', 'player_family', 'player_full', 'player_rank', 'player_clan', 'speaker', 'friend', 'neighbor', 'rival',
          'partner', 'kin', 'place', 'district', 'item', 'dish', 'special', 'technique', 'client', 'target', 'count',
          'pay', 'event', 'season', 'weekday', 'time', 'shop', 'other', 'clan', 'teller', 'victim', 'activity',
          'village', 'gift', 'nature', 'when', 'birthday', 'celebrant', 'boss', 'squad'}
# Tokens that take a reference ({they:role:sensei}); is/are, has/have, was/were and s agree with the pronoun ({they:x} {is:x}).
REF_TOKENS = {'name', 'given', 'family', 'they', 'them', 'their', 'theirs', 'themself', 'twist', 'pet', 'is', 'has', 'was', 's'}
CONDITIONS = {'all', 'any', 'not', 'flag', 'rank_at_least', 'rank_at_most', 'level_at_least', 'quest_state', 'friendship',
              'clan', 'clanless', 'age_stage', 'time_between', 'calendar', 'at_place', 'has_item', 'has_ryo',
              'knows_technique', 'nature', 'mode', 'difficulty', 'random', 'district', 'clan_status', 'event_active',
              'bond_meter', 'bond_memory', 'bond_moment', 'bond_state', 'romance_stage', 'kindling', 'knows_fact',
              'squad_cohesion', 'in_squad', 'squad_can_return', 'standing', 'jealous', 'clan_friendship', 'clan_relation',
              'village_mood', 'hook_open', 'kindling_uses', 'bond_web', 'ritual', 'hangouts', 'answered', 'heard'}
ACTIONS = {'set_flag', 'start_quest', 'advance_quest', 'give_item', 'take_item', 'give_ryo', 'add_friendship',
           'bond_event', 'shared_moment', 'reveal_fact', 'favor', 'deed', 'bond_flag', 'news', 'unlock', 'resolve_hook'}
MAX_LINE, MAX_LABEL = 300, 34
ALL_AGES = ('bond.', 'talk.', 'hangout.', 'gift.', 'reaction.', 'life.', 'followup.', 'callback.', 'again', 'close')
# Families whose keys may end in a personality (BondDialogue's <key>.<archetype>); elsewhere ".proud" is just a word.
PERSONALITY_SUFFIXED = ('bond.greet', 'bond.levelup', 'bond.jealous', 'bond.birthday', 'bond.romance', 'talk.', 'life.', 'hangout.', 'gift.',
                        'reaction', 'callback.contradict', 'again', 'close', 'followup.', 'combat.')
ROMANCE = re.compile(r"\b(kiss\w*|flirt\w*|crush(es)?|sweetheart\w*|darling|romanc\w*|romantic|in love|love letter\w*|"
                     r"go(ing)? on a date|dating|marry me|propos\w+ to|handsome|gorgeous|blush\w* at you)\b", re.I)
PRONOUN = re.compile(r"\b(he|him|his|himself|she|her|hers|herself)\b", re.I)
KIN = re.compile(r"\b(mother|father|mom|mum|dad|ma|pa|papa|mama|brother|sister|grand(ma|pa|mother|father)|granny|gramps|"
                 r"son|daughter|wife|husband|uncle|aunt|auntie|nephew|niece|boy|girl|man|woman|lady|gentleman|"
                 r"grandson|granddaughter|widow|widower|priest|priestess|mister|missus|old man|old woman|king|queen|"
                 r"tom|mare|stallion|hen|rooster|cow|bull)\b", re.I)
ADDRESS = re.compile(r"\b(young man|young lady|lad|lass|laddie|missy|sonny|my boy|my girl|good sir|ma'am|madam|"
                     r"little lady|little man|sir)\b", re.I)
CANON = re.compile(r"\b(naruto|sasuke|kakashi|hinata|shikamaru|choji|chouji|kiba|shino|neji|tenten|gaara|itachi|"
                   r"jiraiya|tsunade|orochimaru|minato|kushina|hiruzen|tobirama|hashirama|madara|obito|iruka|asuma|"
                   r"kurenai|danzo|konohamaru|teuchi|kabuto|nagato|boruto|sarada|himawari|might guy|rock lee|"
                   r"dattebayo|believe it)\b", re.I)


class Error(Exception):
    pass


def fail(where, message):
    raise Error(f'{where}: {message}')


# -- spoilers ---------------------------------------------------------------------------------------------

def spoiler_terms():
    """Terms that give the story away: proper nouns the story bible bolds or code-quotes and no public doc uses, plus
    docs/story/dialogue/spoiler_terms.txt. Read from the bible at build time so this tool never spells them out."""
    bible = PROJECT / 'docs/story/STORY_BIBLE.md'
    if not bible.exists():
        return []
    public = ' '.join(p.read_text(encoding='utf-8').lower() for p in PROJECT.glob('*.md'))
    text = bible.read_text(encoding='utf-8')
    terms = set()
    for t in re.findall(r'\*\*([^*]{3,30})\*\*', text):
        t = t.strip(' .,:')
        if t and t[0].isupper() and len(t.split()) <= 3 and not re.search(r'[:(]', t):
            terms.add(t)
    extra = STORY / 'spoiler_terms.txt'
    if extra.exists():
        terms |= {line.strip() for line in extra.read_text(encoding='utf-8').splitlines() if line.strip() and not line.startswith('#')}
    out = []
    for t in sorted(terms):
        plain = t.lower()
        if plain not in public or (extra.exists() and t in extra.read_text(encoding='utf-8')):
            out.append(t)
    return out


# -- tags and text ----------------------------------------------------------------------------------------

def parse_tag(where, raw):
    if '=' not in raw:
        fail(where, f'expected key=value, got {raw!r}')
    key, value = raw.split('=', 1)
    if key not in TAGS and key not in ('fn', 'kind'):
        fail(where, f'unknown tag {key!r}')
    return key, value


def tag_values(where, key, value):
    neg = value.startswith('!')
    body = value[1:] if neg else value
    allowed = TAGS[key]
    if allowed == 'int':
        m = re.fullmatch(r'(\d+)(?:\.\.(\d+))?', body)
        if not m:
            fail(where, f'{key} takes a number or a range like 3..10')
        lo, hi = int(m.group(1)), int(m.group(2) or m.group(1))
        return {'range': [lo, hi]}
    values = body.split('|')
    for v in values:
        if allowed is None:
            if not re.fullmatch(r'[a-z0-9_:.]+', v):
                fail(where, f'bad {key} value {v!r}')
        elif v not in allowed:
            fail(where, f'unknown {key} {v!r} (one of {", ".join(sorted(allowed))})')
    return {'not' if neg else 'any': sorted(values)}


def check_condition(where, cond):
    if isinstance(cond, list):
        for c in cond:
            check_condition(where, c)
        return
    if not isinstance(cond, dict) or len(cond) != 1:
        fail(where, f'a condition is an object with one key: {cond!r}')
    (key, value), = cond.items()
    if key not in CONDITIONS:
        fail(where, f'unknown condition {key!r}')
    if key in ('all', 'any'):
        check_condition(where, value)
    elif key == 'not':
        check_condition(where, value)


TOKEN = re.compile(r'\{([a-z_]+)(?::([^{}]+))?\}')


def check_text(where, text, terms, tags, gated, limit=MAX_LINE, pool=''):
    if not text.strip():
        fail(where, 'empty text')
    if len(text) > limit:
        fail(where, f'too long ({len(text)} > {limit}): {text[:60]}...')
    if text.count('{') != text.count('}'):
        fail(where, 'unbalanced braces')
    for name, arg in TOKEN.findall(text):
        if name in REF_TOKENS:
            if not arg:
                fail(where, f'{{{name}}} needs a reference, like {{{name}:role:sensei}}')
            if name == 'twist' and not gated:
                fail(where, '{twist:...} belongs in story-gated pools only')
        elif name == 'hokage':
            if not (arg or '').isdigit():
                fail(where, '{hokage:N} takes a number')
        elif pool.startswith('mission.') and not arg:
            pass  # missions fill any of their template's slot names ({pet_spot}, {claimant}...)
        elif name not in TOKENS or arg:
            fail(where, f'unknown token {{{name}{":" + arg if arg else ""}}}')
    plain = TOKEN.sub('', text)
    if CANON.search(plain):
        fail(where, f'canon name or catchphrase {CANON.search(plain).group(0)!r}: original characters only, names as tokens')
    for name in NAME_LITERALS:
        if re.search(r'\b' + re.escape(name) + r'\b', plain):
            fail(where, f'literal name {name!r}: names are tokens ({{name:role:x}}, {{given:...}}, {{player}})')
    if ADDRESS.search(plain):
        fail(where, f'gendered address {ADDRESS.search(plain).group(0)!r}: the player is addressed by token or neutrally')
    if PRONOUN.search(plain) and not KIN.search(plain):
        fail(where, f'gendered pronoun {PRONOUN.search(plain).group(0)!r} with no gendered word to anchor it: use {{they:ref}}')
    if ROMANCE.search(plain):
        ok = all(_excludes_child(tags, k) for k in ('stage', 'player_stage'))
        if not ok:
            fail(where, f'romance ({ROMANCE.search(plain).group(0)!r}) needs stage and player_stage that exclude child')
    if not gated:
        low = plain.lower()
        for term in terms:
            if re.search(r'\b' + re.escape(term.lower()) + r'\b', low):
                fail(where, 'a story-bible term outside the story-gated pools (move the line to docs/story/dialogue/)')


def _excludes_child(tags, key):
    t = tags.get(key)
    if t is None:
        return key == 'stage'  # lines default to teen and adult speakers; the beta's player is always a child
    if 'any' in t:
        return 'child' not in t['any']
    return 'child' in t.get('not', [])


def family_names():
    pop = json.loads((PROJECT / 'tools/wardrobe/population.json').read_text(encoding='utf-8'))
    names = set(pop.get('family_names', []))
    given = PROJECT / 'village/src/main/resources/data/narutominecraft/names/given.json'
    if given.exists():
        for pool in json.loads(given.read_text(encoding='utf-8')).values():
            if isinstance(pool, list):
                names |= set(pool)
    return sorted(names)


NAME_LITERALS = family_names()


# -- sources ----------------------------------------------------------------------------------------------

MARKERS = re.compile(r'\s*(?:\[([A-Z]+)\]|~([a-z0-9_]+))\s*$')


def split_markers(where, text):
    mood = group = None
    while True:
        m = MARKERS.search(text)
        if not m:
            break
        if m.group(1):
            if m.group(1) not in MOODS:
                fail(where, f'unknown mood [{m.group(1)}]')
            mood = m.group(1)
        else:
            group = m.group(2)
        text = text[:m.start()].rstrip()
    return text, mood, group


def parse_heading(where, line, defaults):
    body, _, cond = line[3:].partition(' | when:')
    parts = body.split()
    if not parts:
        fail(where, 'empty heading')
    pool = parts[0]
    if not re.fullmatch(r'[a-z0-9_.]+', pool):
        fail(where, f'bad pool key {pool!r}')
    tags, fn, kind = {}, defaults.get('fn'), defaults.get('kind', 'line')
    for k, v in defaults.get('tags', {}).items():
        tags[k] = v
    # Bond keys carry a personality as their last segment (talk.food.fiery): it is a tag, the pool is talk.food.
    head, _, last = pool.rpartition('.')
    if last in ARCHETYPES and head and head.startswith(PERSONALITY_SUFFIXED):
        pool, tags['personality'] = head, {'any': [last]}
    for raw in parts[1:]:
        key, value = parse_tag(where, raw)
        if key == 'fn':
            fn = value
        elif key == 'kind':
            kind = value
        else:
            tags[key] = tag_values(where, key, value)
    # The bond engine's and the repeat set's pools are said by everyone, children too, unless a line says otherwise.
    if pool.startswith(ALL_AGES) and 'stage' not in tags:
        tags['stage'] = {'any': ['adult', 'child', 'teen']}
    if not fn:
        fail(where, f'{pool}: every pool needs fn= (one or more of {", ".join(sorted(FUNCTIONS))})')
    fns = fn.split(',')
    for f in fns:
        if f not in FUNCTIONS:
            fail(where, f'unknown function {f!r}')
    if kind not in KINDS:
        fail(where, f'unknown kind {kind!r}')
    when = None
    if cond.strip():
        try:
            when = json.loads(cond)
        except json.JSONDecodeError as e:
            fail(where, f'bad condition JSON: {e}')
        check_condition(where, when)
    # The player is always publicly a clanless orphan (the owner's decision): no line may treat them as clan kin.
    for key, bad in (('same_clan', 'yes'), ('clan_status', 'born'), ('clan_status', 'member')):
        if bad in tags.get(key, {}).get('any', []):
            fail(where, f'{key}={bad}: the player is always clanless; write clan_status=clanless reactions instead')
    if 'foreshadow' in fns and 'story' not in tags:
        fail(where, 'foreshadow lines are keyed by story id: add story=<id>')
    return {'pool': pool, 'tags': tags, 'fn': fns, 'kind': kind, 'when': when}


def read_defaults(where, line, defaults):
    key, _, value = line[2:].partition(':')
    key, value = key.strip(), value.strip()
    if key == 'fn':
        defaults['fn'] = value
    elif key == 'kind':
        defaults['kind'] = value
    elif key == 'tags':
        defaults['tags'] = {}
        for raw in value.split():
            k, v = parse_tag(where, raw)
            defaults['tags'][k] = tag_values(where, k, v)
    else:
        fail(where, f'unknown file default {key!r}')


def sources(gated):
    base = STORY if gated else ROOT
    if not base.exists():
        return {}, {}, {}
    pick = (lambda d: sorted((base / d).rglob('*.txt'))) if gated else (lambda d: sorted((base / d).glob('*.txt')))
    return ({p: 'lines' for p in pick('lines')} | {p: 'lines' for p in ([] if gated else pick('generated'))},
            {p: 'exchanges' for p in pick('exchanges')}, {p: 'questions' for p in pick('questions')})


def read_lines(path, gated, terms, out):
    defaults, head = {}, None
    for n, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        line = raw.strip()
        where = f'{path.relative_to(PROJECT)}:{n}'
        if line.startswith('#!'):
            read_defaults(where, line, defaults)
            continue
        if not line or line.startswith('# ') or line == '#':
            continue
        if line.startswith('## '):
            head = parse_heading(where, line, defaults)
            continue
        if head is None:
            fail(where, 'line before any "## pool" heading')
        text, mood, group = split_markers(where, line)
        check_text(where, text, terms, head['tags'], gated, pool=head['pool'])
        out.append({**head, 'text': text, 'mood': mood, 'group': group, 'gated': gated, 'where': where})


def read_exchanges(path, gated, terms, out):
    defaults, head, current = {}, None, None

    def close():
        if current:
            if len(current['turns']) < 2:
                fail(current['where'], 'an exchange needs at least two turns (A: and B:)')
            out.append(current)

    for n, raw in enumerate(path.read_text(encoding='utf-8').splitlines() + [''], 1):
        line = raw.strip()
        where = f'{path.relative_to(PROJECT)}:{n}'
        if line.startswith('#!'):
            read_defaults(where, line, defaults)
            continue
        if line.startswith('# ') or line == '#':
            continue
        if not line:
            close(); current = None
            continue
        if line.startswith('## '):
            close(); current = None
            head = parse_heading(where, line, defaults)
            continue
        if head is None:
            fail(where, 'text before any "## pool" heading')
        if line.startswith('lead:'):
            if current is None:
                fail(where, 'lead: belongs to an exchange')
            current['lead'] = line[5:].strip()
            continue
        m = re.match(r'^([AB]):\s*(.+)$', line)
        if not m:
            fail(where, 'exchange turns look like "A: line" or "B: line"')
        text, mood, _ = split_markers(where, m.group(2))
        check_text(where, text, terms, head['tags'], gated)
        if current is None:
            current = {**head, 'kind': 'cycle' if head['kind'] == 'line' else head['kind'], 'turns': [], 'lead': None,
                       'gated': gated, 'where': where}
        current['turns'].append({'who': m.group(1).lower(), 'text': text, 'mood': mood})


ANSWER = re.compile(r'^-\s*(.+?)\s*::\s*(.+)$')


def parse_answer(where, raw, terms, tags, gated, index):
    m = ANSWER.match(raw)
    if not m:
        fail(where, 'answers look like "- Label :: reply {values:+honesty} {tone:warm}"')
    label, reply = m.group(1).strip(), m.group(2).strip()
    answer = {'id': f'a{index}', 'label': label, 'values': {}, 'tone': None, 'pole': 0, 'actions': []}
    for key, arg in re.findall(r'\{(values|tone|pole|do|id):([^{}]*)\}', reply):
        if key == 'values':
            for v in arg.split():
                sign, name = (v[0], v[1:]) if v[0] in '+-' else ('+', v)
                if name not in VALUES:
                    fail(where, f'unknown value {name!r}')
                answer['values'][name] = 1 if sign == '+' else -1
        elif key == 'tone':
            if arg not in TONES:
                fail(where, f'unknown tone {arg!r} (one of {", ".join(sorted(TONES))})')
            answer['tone'] = arg
        elif key == 'pole':
            answer['pole'] = int(arg)
        elif key == 'id':
            answer['id'] = arg
        else:
            try:
                act = json.loads(arg)
            except json.JSONDecodeError as e:
                fail(where, f'bad action JSON: {e}')
            if not isinstance(act, dict) or len(act) != 1 or next(iter(act)) not in ACTIONS:
                fail(where, f'unknown action {arg}')
            answer['actions'].append(act)
    reply = re.sub(r'\s*\{(values|tone|pole|do|id):[^{}]*\}', '', reply)
    reply, mood, _ = split_markers(where, reply)
    answer['mood'] = mood
    check_text(where, label, terms, tags, gated, MAX_LABEL)
    check_text(where, reply, terms, tags, gated)
    answer['label'], answer['reply'] = label, reply.strip()
    return answer


def read_questions(path, gated, terms, out, ids):
    current, defaults = None, {}
    for n, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        line = raw.strip()
        where = f'{path.relative_to(PROJECT)}:{n}'
        if line.startswith('#!'):
            read_defaults(where, line, defaults)
            continue
        if not line or line.startswith('# ') or line == '#':
            continue
        if line.startswith('? '):
            head = [p.strip() for p in re.split(r'\s\|\s', line[2:])]
            qid = head[0]
            if not re.fullmatch(r'q\.[a-z0-9_.]{2,60}', qid):
                fail(where, f'bad question id {qid!r} (q.<topic>.<name>)')
            if qid in ids:
                fail(where, f'duplicate question id {qid}')
            ids.add(qid)
            q = {'id': qid, 'fn': (defaults.get('fn') or '').split(',') if defaults.get('fn') else [], 'level': 0,
                 'tags': dict(defaults.get('tags', {})), 'when': None, 'axis': None, 'follows': None, 'depth': 1,
                 'asks': [], 'answers': [], 'gated': gated, 'where': where, 'kind': 'question', 'qkind': None,
                 'public': False, 'gap': 0, 'sets': None}
            for part in head[1:]:
                key, _, value = part.partition(':')
                key, value = key.strip(), value.strip()
                if key == 'fn':
                    q['fn'] = value.split()
                elif key == 'level':
                    q['level'] = int(value)
                elif key == 'axis':
                    q['axis'] = value
                elif key == 'follows':
                    q['follows'] = value
                elif key == 'depth':
                    q['depth'] = int(value)
                elif key == 'tags':
                    for raw_tag in value.split():
                        k, v = parse_tag(where, raw_tag)
                        q['tags'][k] = tag_values(where, k, v)
                elif key == 'when':
                    q['when'] = json.loads(value)
                    check_condition(where, q['when'])
                elif key == 'kind':
                    if value not in QUESTION_KINDS:
                        fail(where, f'unknown question kind {value!r} (one of {", ".join(sorted(QUESTION_KINDS))})')
                    q['qkind'] = value
                elif key == 'public':
                    q['public'] = value in ('yes', 'true')
                elif key == 'gap':
                    q['gap'] = int(value)
                elif key == 'sets':
                    q['sets'] = value
                else:
                    fail(where, f'unknown question option {key!r}')
            if not q['fn'] or any(f not in FUNCTIONS for f in q['fn']):
                fail(where, f'{qid}: fn: needs functions from {", ".join(sorted(FUNCTIONS))}')
            current = q
            out.append(q)
            continue
        if current is None:
            fail(where, 'text before a "? q.id" heading')
        if line.startswith('Q:'):
            text = line[2:].strip()
            check_text(where, text, terms, current['tags'], gated)
            current['asks'].append(text)
        elif line.startswith('-'):
            current['answers'].append(parse_answer(where, line, terms, current['tags'], gated, len(current['answers']) + 1))
        else:
            fail(where, f'expected "Q:" or "- answer": {line[:40]}')
    for q in out:
        if not q['asks'] or not 2 <= len(q['answers']) <= 4:
            fail(q['where'], f'{q["id"]}: a question needs a "Q:" line and 2-4 answers')
        if len({a['id'] for a in q['answers']}) != len(q['answers']):
            fail(q['where'], f'{q["id"]}: duplicate answer ids')


# -- ids ----------------------------------------------------------------------------------------------------

def content_key(item):
    if item['kind'] == 'question':
        return 'q\t' + item['id']
    text = item.get('text') or ' / '.join(t['text'] for t in item['turns'])
    return hashlib.sha1((item['pool'] + '\n' + text).encode('utf-8')).hexdigest()[:16]


def assign_ids(items, lock, write):
    ids, nxt = lock.get('ids', {}), lock.get('next', 1)
    for item in items:
        key = content_key(item)
        if key not in ids:
            ids[key] = nxt
            nxt += 1
        item['num'] = ids[key]
    groups, gnext = lock.get('groups', {}), lock.get('next_group', 1)
    for item in items:
        g = item.get('group')
        if g:
            gkey = item['pool'] + '~' + g
            if gkey not in groups:
                groups[gkey] = gnext
                gnext += 1
            item['group_num'] = groups[gkey]
    return {'format': 1, 'next': nxt, 'next_group': gnext, 'ids': ids, 'groups': groups}


# -- near duplicates ----------------------------------------------------------------------------------------

def words(text):
    text = TOKEN.sub(' tok ', text.lower())
    return re.findall(r"[a-z']+", text)


def shingles(text):
    w = words(text)
    return set(w) | {a + ' ' + b for a, b in zip(w, w[1:])}


def near_duplicates(items, threshold=0.72):
    """Pairs of lines a player could hear that say nearly the same thing (Jaccard over words and word pairs)."""
    texts = [(i, it) for i, it in enumerate(items) if it.get('text') and it['kind'] != 'repeat']
    sh = {i: shingles(it['text']) for i, it in texts}
    tri = defaultdict(list)
    for i, it in texts:
        w = words(it['text'])
        for gram in set(zip(w, w[1:], w[2:])):
            tri[gram].append(i)
    pairs = set()
    for gram, members in tri.items():
        if len(members) > 150:
            continue
        for a in range(len(members)):
            for b in range(a + 1, len(members)):
                pairs.add((members[a], members[b]))
    found = []
    for a, b in pairs:
        ia, ib = items[a], items[b]
        if ia.get('group') and ia.get('group') == ib.get('group') and ia['pool'] == ib['pool']:
            continue  # the same content in two voices: retired together
        sa, sb = sh[a], sh[b]
        j = len(sa & sb) / max(1, len(sa | sb))
        if j >= threshold:
            found.append((j, ia, ib))
    return sorted(found, key=lambda x: -x[0])


# -- compile ------------------------------------------------------------------------------------------------

def specificity(item):
    s = sum(WEIGHTS.get(k, 1) for k in item['tags'])
    if item.get('when'):
        s += WEIGHTS['when']
    return s


def load_all():
    terms = spoiler_terms()
    lines, exchanges, questions, qids = [], [], [], set()
    for gated in (False, True):
        ls, ex, qs = sources(gated)
        for p in ls:
            read_lines(p, gated, terms, lines)
        for p in ex:
            read_exchanges(p, gated, terms, exchanges)
        for p in qs:
            read_questions(p, gated, terms, questions, qids)
    seen = Counter((it['pool'], it['text'], json.dumps(it['tags'], sort_keys=True)) for it in lines)
    dups = [k for k, c in seen.items() if c > 1]
    if dups:
        fail('lines', f'{len(dups)} duplicate lines, e.g. {dups[0]!r}')
    texts = Counter(it['text'] for it in lines if it['kind'] != 'repeat' and len(it['text']) > 12)
    cross = [t for t, c in texts.items() if c > 1]
    if cross:
        fail('lines', f'{len(cross)} lines appear in more than one pool, e.g. {cross[0]!r}')
    for q in questions:
        if q['follows'] and q['follows'] not in qids:
            fail(q['where'], f'follows an unknown question {q["follows"]}')
    return lines, exchanges, questions


def compiled(item):
    out = {'id': item['num'], 'pool': item['pool']}
    if item['tags']:
        out['tags'] = item['tags']
    if item.get('when') is not None:
        out['when'] = item['when']
    out['fn'] = item['fn']
    if item['kind'] != 'line':
        out['kind'] = item['kind']
    out['spec'] = specificity(item)
    if item.get('group_num'):
        out['group'] = item['group_num']
    if item.get('mood'):
        out['mood'] = item['mood']
    if 'turns' in item:
        out['turns'] = [{k: v for k, v in t.items() if v is not None} for t in item['turns']]
        if item.get('lead'):
            out['lead'] = item['lead']
    else:
        out['text'] = item['text']
    return out


def compiled_question(q):
    out = {'id': q['id'], 'num': q['num'], 'fn': q['fn'], 'level': q['level']}
    if q.get('qkind'):
        out['kind'] = q['qkind']
    for k in ('tags', 'when', 'axis', 'follows', 'public', 'gap', 'sets'):
        if q.get(k):
            out[k] = q[k]
    out['depth'] = q['depth']
    out['asks'] = q['asks']
    out['answers'] = [{k: v for k, v in a.items() if v not in (None, {}, [], 0)} | {'id': a['id']} for a in q['answers']]
    return out


def family(pool):
    head = pool.split('.')[0]
    return head if head in FILES else 'misc'


FILES = ['greet', 'chat', 'talk', 'bond', 'hangout', 'callback', 'followup', 'life', 'village', 'hook', 'shop', 'mission',
         'combat', 'ambient', 'event', 'again', 'close', 'react', 'teach', 'job', 'reaction', 'gift']


def build():
    lines, exchanges, questions = load_all()
    items = lines + exchanges + questions
    lock = json.loads(LOCK.read_text(encoding='utf-8')) if LOCK.exists() else {}
    new_lock = assign_ids(items, lock, True)
    files = defaultdict(list)
    story = {'format': 1, '_doc': 'SPOILERS: story-gated dialogue, compiled from docs/story/dialogue/.', 'lines': [], 'questions': []}
    for it in lines + exchanges:
        (story['lines'] if it['gated'] else files[family(it['pool'])]).append(compiled(it))
    qs = []
    for q in questions:
        (story['questions'] if q['gated'] else qs).append(compiled_question(q))
    out = {}
    for name in sorted(files):
        out[f'{name}.json'] = {'format': 1, 'lines': sorted(files[name], key=lambda x: x['id'])}
    out['questions.json'] = {'format': 1, 'questions': qs}
    out['story.json'] = story
    rules = {k: v for k, v in RULES.items() if not k.startswith('_')}
    out['rules.json'] = rules
    max_id = new_lock['next'] - 1
    out['manifest.json'] = {'format': 1, 'max_id': max_id, 'max_group': new_lock['next_group'] - 1,
                            'files': sorted(k for k in out if k != 'manifest.json'),
                            'counts': {k: len(v.get('lines', v.get('questions', []))) for k, v in out.items() if k not in ('rules.json',)}}
    return out, new_lock, (lines, exchanges, questions)


def render(data):
    return json.dumps(data, ensure_ascii=False, separators=(',', ':'), sort_keys=False) + '\n'


# -- reports ------------------------------------------------------------------------------------------------

def matches(tags, ctx):
    for key, t in tags.items():
        v = ctx.get(key)
        if 'range' in t:
            if v is None or not t['range'][0] <= v <= t['range'][1]:
                return False
        elif 'any' in t:
            if v not in t['any']:
                return False
        elif v in t.get('not', []):
            return False
    if 'stage' not in tags and ctx.get('stage') == 'child':
        return False
    return True


BANDS = {'stranger': 0, 'acquaintance': 2, 'friend': 4, 'close': 6, 'best': 9}


def coverage(lines):
    """Fresh lines reachable for every personality x clan voice x rank x relationship band, for greet and chat."""
    facets = {topic: [f['pool'] for f in RULES['facets'][topic]] for topic in ('greet', 'chat')}
    by_pool = defaultdict(list)
    for it in lines:
        if it['kind'] == 'line' and not it['gated'] and not it.get('when'):
            by_pool[it['pool']].append(it)
    voices = [('civilian', None)] + [('clanless', None)] + [('noble' if c in NOBLE else 'minor', c) for c in NOBLE + MINOR]
    ranks = ['civilian', 'academy', 'genin', 'chunin', 'jonin']
    table = {}
    for topic, pools in facets.items():
        counts = []
        for p in ARCHETYPES:
            for group, clan in voices:
                for rank in ranks:
                    if (group == 'civilian') != (rank == 'civilian'):
                        continue
                    for band, level in BANDS.items():
                        ctx = {'personality': p, 'group': group, 'clan': clan, 'rank': rank, 'band': band, 'level': level,
                               'stage': 'adult', 'player_stage': 'child', 'player_rank': 'genin', 'time': 'morning',
                               'weather': 'clear', 'season': 'spring', 'tier': 'resident', 'district': 'market'}
                        n, fill = 0, 0
                        seen_groups = set()
                        for pool in pools:
                            for it in by_pool.get(pool, []):
                                if matches(it['tags'], ctx):
                                    g = it.get('group')
                                    if g and (pool, g) in seen_groups:
                                        continue
                                    if g:
                                        seen_groups.add((pool, g))
                                    n += 1
                                    fill += 'filler' in it['fn']
                        counts.append((n, fill, (p, clan or group, rank, band)))
        counts.sort()
        table[topic] = counts
    return table


def report(lines, exchanges, questions):
    print('Coverage (distinct fresh pieces reachable, one morning in spring at the market, by a genin player):')
    for topic, counts in coverage(lines).items():
        ns = [c[0] for c in counts]
        worst = counts[0]
        filler = sum(c[1] for c in counts) / max(1, sum(ns))
        print(f'  {topic:6} cells {len(ns)}  min {ns[0]} (e.g. {"/".join(worst[2])})  median {ns[len(ns) // 2]}  max {ns[-1]}'
              f'  filler share {filler:.0%}')
    fn = Counter(f for it in lines + exchanges for f in it['fn'][:1])
    total = sum(fn.values())
    print('Function mix (primary function, every line and exchange):')
    for f, c in fn.most_common():
        print(f'  {f:18} {c:6}  {c / total:5.1%}')
    print('Filler share by pool family (cap', f"{RULES['filler_cap']:.0%} of an NPC's fresh lines, enforced at run time):")
    fam = defaultdict(Counter)
    for it in lines + exchanges:
        fam[it['pool'].split('.')[0]]['all'] += 1
        fam[it['pool'].split('.')[0]]['filler'] += 'filler' in it['fn']
    for k, c in sorted(fam.items()):
        print(f'  {k:10} {c["filler"]:5} / {c["all"]:5}  {c["filler"] / max(1, c["all"]):5.1%}')
    if BOND_KEYS.exists():
        keys = [k.strip() for k in BOND_KEYS.read_text(encoding='utf-8').splitlines() if k.strip()]
        have = {it['pool'] for it in lines}
        missing = [k for k in keys if k not in have]
        print(f'Bond engine pools (DialogueKeys.required): {len(keys) - len(missing)} of {len(keys)} written; '
              f'{len(missing)} still to write, e.g. {", ".join(missing[:6])}')


def stats(lines, exchanges, questions):
    fam = Counter(it['pool'].split('.')[0] for it in lines)
    print('Lines by family:')
    for k, c in fam.most_common():
        print(f'  {k:10} {c}')
    print(f'  exchanges  {len(exchanges)} ({sum(len(e["turns"]) for e in exchanges)} turns)')
    print(f'  questions  {len(questions)} ({sum(len(q["answers"]) for q in questions)} answers)')
    kinds = Counter(it['kind'] for it in lines + exchanges)
    print('By kind:', dict(kinds), ' story-gated:', sum(it['gated'] for it in lines + exchanges + questions))
    pools = Counter(it['pool'] for it in lines)
    print(f'Pools: {len(pools)}')


def lint(paths):
    terms = spoiler_terms()
    lines, ex, qs = [], [], []
    for p in paths:
        p = Path(p).resolve()
        gated = STORY in p.parents
        kind = p.parent.name
        if kind == 'questions':
            read_questions(p, gated, terms, qs, set())
        elif kind == 'exchanges':
            read_exchanges(p, gated, terms, ex)
        else:
            read_lines(p, gated, terms, lines)
    dups = near_duplicates(lines)
    for j, a, b in dups[:40]:
        print(f'near duplicate ({j:.2f}): {a["where"]} / {b["where"]}\n    {a["text"]}\n    {b["text"]}')
    print(f'{len(lines)} lines, {len(ex)} exchanges, {len(qs)} questions: OK' + (f' ({len(dups)} near duplicates)' if dups else ''))
    return 1 if dups else 0


def main():
    try:
        if '--lint' in sys.argv:
            raise SystemExit(lint([a for a in sys.argv[1:] if not a.startswith('--')]))
        out, lock, (lines, exchanges, questions) = build()
        dups = near_duplicates(lines)
        if dups:
            for j, a, b in dups[:25]:
                print(f'near duplicate ({j:.2f}): {a["where"]} / {b["where"]}\n    {a["text"]}\n    {b["text"]}')
            raise Error(f'{len(dups)} near-duplicate pairs')
    except Error as e:
        raise SystemExit(str(e))
    if '--stats' in sys.argv:
        stats(lines, exchanges, questions)
    if '--report' in sys.argv:
        report(lines, exchanges, questions)
    total = len(lines) + len(exchanges) + len(questions)
    if '--check' in sys.argv:
        stale = [n for n, d in out.items() if not (OUT / n).exists() or (OUT / n).read_text(encoding='utf-8') != render(d)]
        if stale or not LOCK.exists() or json.loads(LOCK.read_text(encoding='utf-8')) != lock:
            raise SystemExit(f'dialogue is out of date ({", ".join(stale) or "ids.lock"}): run python tools/dialogue/dialogue.py')
        print(f'Dialogue is up to date: {total} pieces ({len(lines)} lines, {len(exchanges)} exchanges, {len(questions)} questions).')
        return
    OUT.mkdir(parents=True, exist_ok=True)
    for name, data in out.items():
        (OUT / name).write_text(render(data), encoding='utf-8')
    LOCK.write_text(json.dumps(lock, indent=0, sort_keys=True) + '\n', encoding='utf-8')
    print(f'Dialogue: {total} pieces: {len(lines)} lines in {len({l["pool"] for l in lines})} pools, '
          f'{len(exchanges)} exchanges, {len(questions)} questions; ids up to {lock["next"] - 1}.')


if __name__ == '__main__':
    main()
