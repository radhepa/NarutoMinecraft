# Writing dialogue for the Leaf

The writers' guide to `tools/dialogue/`: the format, the function taxonomy, voices and the rules the
compiler enforces. The engine and the numbers behind it are in [DIALOGUE.md](../../DIALOGUE.md).

**Do not open `docs/story/`.** It holds the story's secrets. Everything you write here must work
without knowing them: no plot, no mysteries, no hints. Story-gated lines are written separately,
after the story is locked.

## The format

A source file is a list of pools. A heading names the pool, then its context tags, then an
optional Core condition. Every line under it belongs to that pool and inherits its tags.

```text
#! fn: worldbuild                       file default function (optional)
#! tags: district=market                file default tags (optional)

## greet.time  time=evening  personality=fiery|playful  fn=react
Evening already? I could go another round. [EXCLAIM]
The lanterns are lit, {player}! Someone's grilling eel by the bridge. ~eel_bridge

## chat.village  rank=!civilian  fn=worldbuild | when: {"rank_at_least": "genin"}
```

- **Tags** are `key=value`. Alternatives use `a|b`, negation a leading `!`, and bond level takes a
  range (`level=3..10`). A line is only said in a matching context, and **the most specific
  matching line wins**, so tag what the line really depends on, and nothing else. A rain line is
  tagged `weather=rain`; a line any adult could say anywhere has no tags.
- **`fn=`** is required: one or more functions, comma-separated (below).
- **`kind=`**: `line` (default: said once per save, never again), `repeat` (the repeatable "we
  already talked" set), or `cycle` (barks, shop transactions, ambient: each line once before any
  comes back).
- **Line endings:** `[MOOD]` sets the speech bubble (EXCLAIM QUESTION HEART NOTE ANGER SWEAT DOTS
  SLEEP SPARKLE IDEA GLOOM BLUSH). `~group` marks one piece of content in several voices, so
  hearing one spends all of them.
- **Seeds** (`tools/dialogue/seeds/*.txt`, compiled by `compose.py` into `generated/`): a kernel is
  one idea in several registers; a template is a frame filled from lists. See the docstring at the
  top of `compose.py`.
- **Exchanges** (`tools/dialogue/exchanges/*.txt`): overheard talk between two residents, as
  `A:` and `B:` turns, with exchanges separated by a blank line and an optional `lead: <hook type
  or quest id>` that turns it into a lead in the journal.
- **Questions** (`tools/dialogue/questions/*.txt`): see [Questions](#questions).

Check your files as you go. Only run `--lint`; the full compile assigns ids and is run by the
maintainer.

```text
python3 tools/dialogue/dialogue.py --lint tools/dialogue/lines/my-file.txt
python3 tools/dialogue/compose.py && python3 tools/dialogue/dialogue.py --lint tools/dialogue/generated/gen-my-seed.txt
```

## Context tags

| Tag | Values | Notes |
|---|---|---|
| `personality` | warmhearted thoughtful playful adventurous meticulous steadfast reserved imaginative pragmatic curious protective gentle proud fiery shy stern | The speaker's VF personality |
| `clan` | senju uzumaki uchiha hyuga nara akimichi yamanaka inuzuka sarutobi aburame hatake kurama shimura yuhi gekko shiranui morino umino haruno namiashi hagane kinoshita tsuchigumo suzuran tobari | The speaker's clan |
| `group` | civilian clanless noble minor | Civilians are not shinobi |
| `rank` | civilian academy genin chunin jonin anbu kage | The speaker's rank |
| `player_rank` | academy genin chunin jonin anbu hokage | The player's rank |
| `stage`, `player_stage` | child teen adult | **Lines with no `stage` are said by teens and adults only.** Children speak only from lines tagged `stage=child`. The player is a child for the whole beta. |
| `level`, `band` | 0..10; stranger (0) acquaintance (1-2) friend (3-4) close (5-7) best (8-10) | How well they know the player |
| `quarrel` | none argument cold_shoulder making_up falling_out | |
| `time` | dawn morning noon afternoon evening night late | |
| `weather`, `season` | clear rain thunder snow; spring summer autumn winter | |
| `market` | yes | Market Day |
| `district` | academy market main_street residential gate hokage_rock residence training hospital shrine river clan_quarter apartments forest stadium outside carpenters_lane academy_streets riverside artists_lane uchiha_quarter stadium_streets | Where the talk happens |
| `event` | leaf_festival new_year chunin_exams graduation clan_day wedding birthday border_incident market_day exam_week first_snow cherry_blossoms moon_viewing | An event on today |
| `job` | snake_case: ramen_cook cook grocer fishmonger farmer carpenter tailor smith florist teacher medic nurse guard gate_guard merchant librarian tea_master bath_keeper pawnbroker vet priest painter police courier dango_maker barbecue_cook scroll_keeper mission_desk ferryman builder launderer potter herbalist kennel_keeper | The speaker's work |
| `clan_status`, `same_clan` | born member other clanless; yes no | The player's tie to a clan, and whether the speaker shares it |
| `mood` | festive proud calm uneasy tense grieving | The village's or district's mood |
| `relation` | friends family couple coworkers neighbors rivals clan strangers kids shinobi elders parent_child customers | Exchanges: the two speakers |
| `shop`, `part`, `speaker`, `habit`, `role`, `place` | snake_case ids | Shops (the items session's ids: ichiraku grocer fishmonger dango_stand tea_house tea_house_rival barbecue_house weapon_shop tool_shop scroll_shop flower_shop furniture_shop kinoshita_yard tailor pawn_shop bath_house pharmacy hospital_dispensary bookshop haruno_store academy_supply inuzuka_clinic cat_shelter hagane_metalworks shrine_office painters_studio senbei_shop market_day_stalls festival_stalls exam_stalls), barks, cast roles (`role:sensei`), anchors |

## Functions

Every line serves a purpose. Tag the main one first.

| Function | The line... | Example |
|---|---|---|
| `teach` | explains a mechanic in the world's own words | "Sleep before midnight and you'll wake with chakra to spare." |
| `guide` | points somewhere | "The Mission Desk is on the Residence's ground floor, eight till six." |
| `quest` | advances or gates a quest or mission | briefings, leads that open a quest |
| `reveal_character` | shows who the speaker is: their past, taste, values, fears | "I keep my father's ledger. I've never balanced it." |
| `deepen_bond` | is about the two of you | "You always stop by after the market. I've started saving you a seat." |
| `foreshadow` | plants a story seed (story-gated pools only, `story=<id>`) | |
| `worldbuild` | gives the village texture: lore, clans, places, customs | "The Akimichi always set one more place than they need." |
| `react` | answers the player's deeds, rank, the time, the weather, an event | "A Genin now! Mind the headband doesn't slip." |
| `callback` | remembers something: an answer, a memory, a hangout | "You told me you hated rain. Brought you an umbrella." |
| `hook` | a rumour or need that can become a side quest | "Someone's been taking the fish off the drying racks at night." |
| `commerce` | sells, prices, shop talk | |
| `filler` | pure pleasantry | "Lovely day." Keep it under a fifth of any pool. |

## Voices

The sixteen personalities, in a phrase each. Write the line only that personality would say; a
line anyone could say goes untagged.

| Personality | Voice |
|---|---|
| warmhearted | Feeds you, fusses, notices you look tired; warmth in concrete acts |
| thoughtful | Considers before speaking, asks why, quotes a book, quiet humour |
| playful | Jokes, dares, games, teasing, never still |
| adventurous | Wants to see past the wall, tells of roads and far villages |
| meticulous | Precise, schedules and lists, small corrections, proud of tidy work |
| steadfast | Reliable, plain-spoken, keeps promises, talks of duty without fuss |
| reserved | Few words, dry, private, warms slowly |
| imaginative | Daydreams, colours and stories, odd similes |
| pragmatic | Costs and practicality, no-nonsense, a merchant's eye |
| curious | Questions, rumours, how things work, gets distracted |
| protective | Watches over people, warns, checks you got home |
| gentle | Soft-spoken, kind to animals and children, never sharp |
| proud | Standards, family name, competitive, hides softness |
| fiery | Loud, eager, impatient, declares things, big feelings |
| shy | Short, hesitant, trailing sentences, brave in small ways |
| stern | Discipline, terse, correcting, cares by demanding more |

**Clan voices** come from the clan's culture in [SIDE_QUESTS.md §4](../../SIDE_QUESTS.md#4-clan-quest-lines)
and [CLANS.md](../../CLANS.md): the Akimichi's shared meals, the Nara's clouds and deer, the
Inuzuka's dogs, the Aburame's quiet insects, the Hyuga's main and branch house, the Uchiha police,
the Yamanaka flower shop, the Senju's living tree, the Uzumaki's seals and remembered names, the
Sarutobi's fire, the Kurama's paintings, the Yuhi's grove, the Gekko's swords and the moon, the
Shimura's silence, the Hatake's almost empty house, and the minor clans' trades (the Umino
teachers, the Hagane metalworkers, the Kinoshita carpenters, the Suzuran herbalists, the Tobari
night watch, the Tsuchigumo quarry, the Shiranui senbon, the Morino interrogators, the Namiashi
footwork dojo, the Haruno market family). A clan line shows life inside the clan, never a secret.

## Rules the compiler enforces

- **Names are tokens.** `{player}` (given name), `{player_family}`, `{player_full}`,
  `{player_rank}`, `{player_clan}`; a cast member is `{name:role:sensei}`, `{given:role:rival}` or
  `{family:role:x}`; a Hokage is `{hokage:4}`; situational fills are `{friend}`, `{neighbor}`,
  `{rival}`, `{kin}`, `{place}`, `{item}`, `{dish}`, `{special}`, `{shop}`, `{technique}`,
  `{client}`, `{target}`, `{count}`, `{pay}`, `{event}`, `{season}`, `{weekday}`, `{time}`,
  `{other}` (the other speaker in an exchange) and `{squad}`. No literal names: no names from the
  name pools, and no canon Naruto characters or catchphrases. Place names like Ichiraku, the
  Hokage Rock and the Academy are fine.
- **The player is always publicly a clanless orphan.** Never assume a clan; clan folk may wonder or
  tease, kind ones make a point of not caring (`clan_status=clanless`). The compiler rejects
  `same_clan=yes` and `clan_status=born|member`.
- **How people are named.** `{name:<ref>}` is the full name, given name first and family name last
  ("Shigure Nara"). Friends use given names (`{given:<ref>}`, `{player}`). Formal speech uses the
  family name and an honorific (`{family:role:sensei}-sensei`, `{player_family}-san`). The Hokage
  are "Lord Hokage" or "Lord Fourth"; their given names (`{hokage:4}`) appear only in intimate or
  historical lines.
- **No gendered pronouns for the player or anyone a token names.** Write around them, or use
  `{they:ref}`, `{them:ref}` or `{their:ref}`. A pronoun is allowed only when the line itself names
  someone's gender in a word (my mother... she). Never address the player as boy, girl, lad, sir or
  young lady; "kid" is fine when tagged `player_stage=child`.
- **No romance in the beta.** Romantic words need `stage` and `player_stage` tags that exclude
  child. Residents can mention their own spouse or family plainly.
- **Age-appropriate.** Children (`stage=child`) talk like eleven-year-olds: games, lessons,
  snacks, siblings, dares.
- **The player's age.** Lines that only suit a child player get `player_stage=child`; otherwise
  keep the address neutral, because the same lines play later when the player is older.
- **No spoilers.** Leave the main plot alone: no hideouts, no cloaked figures, no conspiracies, no
  strange chakra, no hints about the player's past beyond what everyone knows (a new orphan the
  Hokage gave an apartment).
- **No near duplicates.** Two lines in reach of the same player must say different things. The
  compiler compares words and word pairs and rejects pairs that are too alike.
- **Lines are at most 300 characters**: usually one or two sentences. Answer labels are at most 34.

## Style

- **Specific beats general.** "The eel man by the second bridge is out of sauce again" beats "The
  market is busy today." Name places, foods, customs and trades of the Leaf.
- **Vary the openers.** Don't start a pool's lines with the same word; avoid "Ah," "Well," and "Oh"
  as crutches.
- **The world's own vocabulary:** ryo, Genin, Chunin, Jonin, the Academy, the Mission Desk, the
  Hokage Rock, the training grounds, chakra, jutsu, kunai, Ichiraku, dango, the Leaf. Light
  Japanese flavour (onigiri, tatami, festival yukata), no heavy romaji, no modern slang.
- **Humour is welcome**, cruelty is not. Residents can grumble, tease and disagree.
- **The player has a life.** Lines can notice the time, the weather, the player's rank, a festival,
  a quarrel, but only through tags or tokens, never by assuming them.

## Questions

```text
? q.values.honest_or_kind | fn: reveal_character deepen_bond | level: 3 | axis: honesty_vs_kindness
Q: A friend shows you a painting, and it's awful. Do you tell them?
Q: Say your friend's cooking is terrible. Do you tell them?
- Tell them, gently :: Gently. Yes. Kind and true at once. {values:+honesty} {tone:warm} {pole:1} [NOTE]
- Praise it anyway :: That's sweet. Though I'd want to know, if it were me. {values:+kindness -honesty} {tone:warm} {pole:-1}
- Ask what they think :: Clever. Make them say it first. {values:+knowledge} {tone:curious}
```

- **The heading:** `? q.<family>.<name>`, then options:
  - `fn:` (required);
  - `level:` (the bond level it needs; the bond engine starts questions at level 2);
  - `kind:` (opinion, dilemma, advice, preference, player_past, player_plans, confession; otherwise
    inferred from the id family: `q.values` and `q.dilemma` are dilemmas, then `q.advice`, `q.pref`,
    `q.past`, `q.plans`, `q.confess`, and anything else is an opinion);
  - `axis:` (questions on one axis can contradict each other);
  - `follows: q.<earlier>` with `depth: 2` and an optional `gap: <days>` (a deeper version, asked
    after the first is answered);
  - `public: yes` for opinions about clans, people or the village (the answer travels by gossip);
  - `sets: <flag>` (a flag quests read);
  - `tags:` (context tags; `personality`, `role` and `clan` say who may ask);
  - `when:` (a Core condition).
- **The asks:** two or three `Q:` phrasings of the same question.
- **Answers:** 2 to 4, as `- Label :: reply`. In the reply:
  - `{values:+honesty -kindness}` lists the values the answer honours or violates. The bond engine
    turns them into meter changes through the asker's own values.
  - `{tone:warm}` is one of warm gentle joking teasing stern cold kind blunt honest loyal ambitious
    playful cautious bold humble proud dutiful free evasive rude curious family.
  - `{pole:1}` or `{pole:-1}` is the answer's side on the axis.
  - `{do:{"bond_flag": ["x","y"]}}` is an optional extra action.
- **Every answer is remembered.** Write a callback for it in `callback.answer.<qid>.<answer id>`;
  answers are numbered a1, a2... in order, unless you give one `{id:name}`.
