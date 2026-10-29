# Squad 4: `role:squad4_a`, `role:squad4_b`, `role:squad4_c`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). Ensemble plan:
> [ENSEMBLE.md](../ENSEMBLE.md).

Squad 4 graduates with the player in Ch 7 and is taught by `sensei_4` (Classic: Morino, an
interrogator who bakes). In Classic it is a Hyuga heir, an Inuzuka and a Suzuran herbalist: **the
rule-keeper, the noise and the healer**. sensei_4 calls them "my three weather systems".

All three are rolled-look roles. ★ role traits fixed in every save: squad4_a is **the future
Fifth's niece** (always Hyuga, main house: **a fixed clan in every save**, because the Fifth's look and clan are fixed; only her look and gender roll), squad4_c is **a herbalist medic trainee** who keeps the
hospital's surgery roster (always Suzuran in Classic; in Varied, any clan, but always the medic
trainee). squad4_b is a fan favourite: in Varied any clan with a large companion animal or a loud
style (see Variants).

---

## `role:squad4_a`: the heir

### At a glance

| | |
|---|---|
| Role | Hyuga main-house heir; the sensor assigned to shadow the player (Ch 22, replacing the old `sensor_shadow` role) |
| Name | Placeholder: **Sayo Hyuga** |
| Look | Classic: curated (pale eyes, hair tied high like her aunt's, a formal collar she loosens when no one watches). Varied: rolled look, clan fixed |
| Pronouns | Classic: she. Varied: rolled; tokens |
| Clan | Hyuga, main house (★ fixed: the Fifth's niece) |
| Specialty | Byakugan, Gentle Fist; reads chakra paths. Style: exact, no wasted movement |
| Rank | Academy → genin → **Chunin in Ch 20** → Jonin at the start of the Jonin arc |
| Archetype | stern (softening to steadfast) |
| Values / peeves | duty, loyalty / recklessness, lateness |
| Dream | Honour their clan (and change what honour means in it) |
| Tier | Story-driving |
| First / last | Ch 1 / Ch 55 |

### Arc

- **Wants:** to be fair, in a house built on rank.
- **Fears:** that obedience and fairness will one day point in different directions and she will
  choose obedience.
- **Secret:** she has been carrying branch-house petitions to her aunt for years, hidden in her
  sleeve, and her aunt has never read one (the `clan.hyuga.3` petition is one of them).
- **Knows, and when:** the Hyuga story of the Valley of Ash (the family's version: "a clan burned
  our soldiers' chakra"), from childhood; "Kagari" from her aunt after Ch 22 if the player told the
  Fifth; that the player's gift is kind from Ch 31 (she sees it in the square).

| Arc | How she changes |
|---|---|
| Cinders | The top of the class beside the rival; corrects the instructor politely |
| Paper Trail | Squad 4's rule-keeper; carries her clan's formality into missions; wins the council-day seat in the gallery and explains the clans to the player (`event.b2.council_day`) |
| Dusk | Ch 17: beats squad4_b in the prelims and apologises to him. **Promoted in Ch 20** |
| Embers | **Ch 22**: assigned by her aunt to shadow the player. Awkward, exact, she logs everything. She can become a friend if the player lets her (the old `sensor_shadow` beats: night passes, a day off, the stake-out in Ch 28). **Ch 31**: at the council she testifies against her aunt's lockdown of the Tobari ("I watched {player} for ten months. I watched the Tobari for one night. I was wrong about the second") |
| Ashes | **Ch 40**: when her great-uncle (`elder_hyuga`) walks out of the council, she stays in her seat |
| Last Bonfire | **Ch 51a to 51b**: on the Rock's shoulder with her Byakugan, she is the Seventh's eyes for the whole battle, calling out the hearths. Ch 55: the head of her house's next generation, with the branch house's petitions read |

**Endings.** Heir of the Hyuga, the first to read the branch house's petitions aloud. If
`ans.squad4_a.choose` was "fairness", the Hyuga line's Heart step (`clan.hyuga.4`) goes the
branch house's way with her vote.

### Relationships

- **The Fifth (`hokage_5`), her aunt:** love and fear. She is the one person the Fifth softens for.
- **squad4_b:** exasperating; she protects him without saying so.
- **squad4_c:** her only confidante; they study medicine and chakra paths together.
- **squad3_c:** the other sensor on the player; they argue about the watch.
- **The rival:** the two best of the class; a cool mutual respect.
- **The player:** the person she was ordered to watch, and chose to stand beside.

### Dialogue brief

**Voice.** Formal, complete sentences, titles used correctly. Reports instead of chatting ("At
fourteen hundred you ate. At fifteen hundred you trained."). Her humour is accidental. Never
swears; never interrupts; never says "I don't care". Child: stiff. Teen: stiff and kind. Adult:
warm under the form.

*Voice samples, not shipped lines:*
- "Good morning. I am to follow you. I apologise in advance."
- "At twenty-two hundred you were out without a pass. I have written it down. I have also written down that it was for a good reason."
- "My aunt is not cruel. She is afraid. I have never said that aloud before."
- (Ch 31) "I watched {player} for ten months. I watched the Tobari for one night. I was wrong about the second."
- (Ch 51a) "Three hearths, north wall. Two on the roofs. One alone, in the square. That one is waiting for you."

**Topics by depth.**

| Depth | What she says |
|---|---|
| Training (1) | Chakra paths; offers to point out yours |
| Hobby (2) | Calligraphy; she has perfect strokes and hates them |
| Family (4) | Her aunt, the main and branch house, petitions |
| Values (5) | "A rule nobody can appeal is not a rule. It is a wall." |
| Advice (5) | Asks for it rarely; takes it seriously |
| Dream (6) | Honour, rewritten |
| Worries (7) | The petitions in her sleeve |

**Never reveal before.**

| Fact | Gate |
|---|---|
| Her aunt's orders about the player | Ch 22 |
| The family's Valley of Ash story | Level 5 after Ch 22 |
| The petitions | Level 7 |
| What the Hyuga elder knows of the purge | Ch 40 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | How it changes her |
|---|---|---|---|---|---|---|
| `ans.squad4_a.shadow` | Ch 22, the first day | "May I follow you closely, or would you prefer I follow from a distance?" | closely, distance, "walk with me instead" | "With me" breaks protocol and honours loyalty | Her report to the Fifth (Ch 31) | "with me" starts the friendship |
| `ans.squad4_a.pass` | Ch 30.4, the night pass to get squad5_b out of the locked Tobari quarter | "You need a night pass and you will not tell me why. Do I write it?" | "trust me", "come with me and see", "write it down, I'll take the blame" | Loyalty against duty | Ch 31 testimony: she was there (come), she covered (trust), or her log names you and she defends it (blame) | Teaches her to choose |
| `ans.squad4_a.choose` | Before Ch 31, level 5 | "If duty and fairness point different ways, which do I follow?" | duty, fairness, "the one you can explain to the person it hurts" | Tests her core | Ch 31 testimony; Ch 40 staying; her ending (unset: she testifies and stays, quietly, as if by duty) | Decides her ending |
| `ans.squad4_a.aunt` | After Ch 31.4, level 5 | "She stepped down. Was I a traitor to my family?" | "no, you were honest with it", "you were a little, and it was right", "ask her" | Honesty, family | Ch 51: her aunt fights on the wall and says one line to her (by answer) | "ask her" gives a reconciliation scene (Ch 32) |
| `ans.squad4_a.petition` | Level 7 | "I have carried petitions no one reads. Should I read them aloud myself?" | yes, "only with the branch house beside you", "not yet" | Fairness | `clan.hyuga.4`; Ch 55 | — |
| `ans.squad4_a.calligraphy` | Hobby, level 2 | "Write a character for me. Any one. I want to see a stroke that isn't perfect." | fire, home, friend | Creativity | She hangs it in her room; it appears in Ch 55's montage | — |
| `ans.squad4_a.bow` | Cinders, level 1 (the Academy yard) | "How deeply should I bow to you? You have no rank and no clan. I do not know the rule." | "don't bow", "the same as you'd bow to anyone", "a nod, like friends" | Duty against freedom | Every greeting: her bow or nod to you | Her first broken rule |
| `ans.squad4_a.prelim` | Ch 17, after her bout with squad4_b | "I beat him and he cheered. Should I have lost?" | "no, he wanted you to win", "you should thank him", "beat him again next time, he'd love it" | Strength, kindness | squad4_b's party (`side.c.third_time`): her toast | — |
| `ans.squad4_a.log` | Embers, level 4 (the shadow's log) | "My log of you has three hundred pages. Would you like to read it?" | "yes", "no, keep it", "burn the parts about my friends" | Honesty, loyalty | Ch 31: the log is her evidence (yes: you know what is in it; burn: she testifies from memory; keep or unset: she reads from it and you hear it for the first time) | — |
| `ans.squad4_a.branch` | Ashes, level 5 | "A branch-house girl asked me if I would ever bow to her. What should I say?" | "yes, first", "when your house bows to hers too", "ask her what she wants" | Fairness | `clan.hyuga.4`; Ch 55's montage | — |
| `ans.squad4_a.eyes` | Ch 50, before the war | "The Seventh wants me on the Rock as their eyes. I would rather fight beside you. Which?" | "be their eyes", "beside me", "both: link with me" (Ember Link if Flame) | Duty against loyalty | Ch 51: where she stands; "link" lets the player see her Byakugan view in Ch 51 | — |

**What her lines are for.** Plot (Ch 22 watch, Ch 31 testimony, Ch 51a to 51b eyes), teach (curfew and
night passes in Ch 22 are taught through her), bond (watcher to friend), life (reports as humour).
Mood states: on duty (Ch 22 to 31), after the testimony, at war.

**Variants.** Clan fixed. In Varied, if the rolled Fifth's niece
draws a branch-house look, the house split stays: she is main-house by adoption.

**Unison technique (Blaze).** *Open Paths*: her Byakugan through the player's link: every ally
sees the enemy's chakra paths for a few seconds, and every strike lands on a point.

**Thread Sight.** Her thread to the Fifth is strong and fraying (Ch 22 to 31), then mends after
`ans.squad4_a.aunt`.

---

## `role:squad4_b`: the noise (fan favourite)

### At a glance

| | |
|---|---|
| Role | Fan favourite: comedy, heart; teammate_b's loud rival-friend |
| Name | Placeholder: **Gota Inuzuka** (and his ninken, rolled name `{pet:squad4_b}`) |
| Look | Classic: curated (red clan marks, wild hair, a grin; his ninken is the size of a pony). Varied: rolled |
| Pronouns | Classic: he. Varied: rolled; tokens |
| Clan | Classic: Inuzuka |
| Specialty | Fang techniques with his ninken; tracking by scent. Style: straight in, loud |
| Rank | Academy → genin → fails the Chunin Exams in the skip, fails again → **promoted late in the Chunin arc** (`side.c.third_time`) → Chunin to the end; Jonin in the epilogue |
| Archetype | fiery |
| Values / peeves | courage, loyalty / cowardice, neglect |
| Dream | To be taken seriously (he says "Hokage"; nobody believes him, which is the point) |
| Tier | Fan favourite |
| First / last | Ch 1 / Ch 55 |

### Arc

- **Wants:** to be taken seriously.
- **Fears:** that he is the joke.
- **Secret:** he practises the exam written test alone at night with his dog as the proctor.
- **Knows:** nothing of the twists until the village does. He knows every dog in the village and
  what it smelled on everyone's boots.

| Arc | How he changes |
|---|---|
| Cinders | Late to enrolment with his dog; competes with teammate_b instantly |
| Paper Trail | **Ch 9**: his dog makes the goat chase worse; `filler.dogs_and_bugs` (his dog is the accused) |
| Dusk | Loses his prelim to squad4_a and cheers for her anyway |
| Embers | Fails the exam twice. **Ch 26, before the bridge, in every branch**: he finds the player: "{given:teammate_b}'s been at the bridge three nights. Something's wrong." (the same days the player's Thread Sight shows b's thread fraying). If b leaves the squad, he is the one who keeps b company at the bridge and tells the player where b is (a lead). `side.c.third_time`: promoted at last; the squad throws him a party |
| Ashes | A tracker on A-ranks; **Ch 35**: lent to the Valley of Ash A-rank, his nose finds the nursery's back entrance, which lets squad3_a's no-fight plan work |
| Last Bonfire | **Ch 51a**: the dogs hold the market street with teammate_b while b faces their parent; his dog is wounded, and lives |

**Endings.** A Jonin of the Inuzuka kennels, and the loudest voice at every festival.

### Relationships

- **teammate_b:** rival-friend; they compete over whose dog is braver and who eats more.
- **squad4_a:** he would die for her and calls her "Your Highness".
- **squad4_c:** she patches him up weekly.
- **sensei_4:** the only sensei who never laughs at him, and bakes him dog biscuits.

### Dialogue brief

**Voice.** Loud, fast, exclamation, dog metaphors. Talks to his dog as if it answers ("He says
you smell like ramen. He's right."). Never mean. Child, teen and adult are the same volume.

*Voice samples, not shipped lines:*
- "We're not lost! He's just smelling the scenic route!"
- "Third time! Third time! Somebody write it down!"
- "{given:teammate_b} ate four bowls? Hold my dog."
- "...Hey. They're at the bridge again. Don't tell them I told you."

**Topics by depth.** Food (1: eating contests), training (1: anything that involves running),
family (4: a pack of siblings and a mother who runs the clinic), worries (7: being the joke).

**Never reveal before.** Nothing of the twists; his Ch 26 warning plays in every branch, his later lead only if b left; never mentions b's parent before Ch 26.

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | How it changes him |
|---|---|---|---|---|---|---|
| `ans.squad4_b.dog_name` | First meeting with the dog, level 1 | "Guess his name! You get three guesses!" | any of three silly guesses (all wrong; he loves you for trying) | — | He calls you by your wrong guess as a nickname | Filler that sticks |
| `ans.squad4_b.joke` | Embers, after a failed exam, level 4 | "Be honest. Am I the joke?" | "you're the best part", "only when you want to be", "yes, and it's a good joke" | Honesty; the last is brave | `side.c.third_time` party speech | "only when you want to be" makes him study |
| `ans.squad4_b.b` | Ch 26 (if b left) | "They won't talk to me either. Should I keep going to the bridge?" | "yes, every night", "give them space", "bring them food" | Loyalty | Ch 32: b's return lines mention him | — |
| `ans.squad4_b.hokage` | Jonin arc, level 6 | "If I said I wanted to be Hokage, would you laugh?" | "no", "yes, then I'd vote for you", "you'd be a good one" | — | Ch 55: he's the first to bow, then the first to laugh | — |
| `ans.squad4_b.goat` | Ch 9, after the goat | "Okay, the goat was my fault. Do you forgive me or my dog?" | "you", "the dog", "neither, buy ramen" | — | His Ch 14 squad-dinner apology bowl | Filler |
| `ans.squad4_b.beetle` | `filler.dogs_and_bugs` finale | "He didn't eat the beetle! Did you ever think he did? Be honest." | "never", "a little", "yes, completely" | Honesty | He tells the story at every festival with your answer in it | — |
| `ans.squad4_b.test` | Embers, before his third try, level 4 | "Quiz me. If I get one wrong, I'm doomed. Ask me anything." | an easy one, a hard one, "what's your dog's favourite food?" | Kindness | `side.c.third_time`: the question on the real test is yours | — |
| `ans.squad4_b.dog_hurt` | After Ch 51, level 5 | "He's going to be okay. Right? Say right." | "right", "I'll sit with him tonight", "he's the bravest dog in the Leaf" | — | Ch 55's montage: the dog wearing a medal | — |

**What his lines are for.** Life and filler (the village's comic noise), bond, small plot assists
(Ch 26 lead, Ch 35 entrance, Ch 51a market). Pools: greetings, eating-contest lines, dog lines.

**Variants.** Varied may roll any clan; the skin is **loud with a big companion** (an Inuzuka with
a ninken; a clanless kid with a huge stray; an Aburame who is, against every clan custom, the
loudest person alive, with a beetle he talks to).

**Unison technique (Blaze).** *Pack Comet*: his fang spin with the player's ember: a burning comet
that drags every enemy it passes toward the linked squad.

---

## `role:squad4_c`: the healer

### At a glance

| | |
|---|---|
| Role | Herbalist medic trainee; keeper of the hospital's surgery roster |
| Name | Placeholder: **Mio Suzuran** |
| Look | Classic: curated (lily-of-the-valley pins, a satchel of herbs, a too-big medic's coat from Chunin on). Varied: rolled |
| Pronouns | Classic: she. Varied: rolled; tokens |
| Clan | Classic: Suzuran (minor clan; poison resistance, herbalism) |
| Specialty | Herbal medicine, poisons, medical ninjutsu. Style: stays behind the line and keeps everyone on it |
| Rank | Academy → genin → Chunin in the skip (hospital rotation under the `medic`) → medic Jonin in the Jonin arc |
| Archetype | gentle (shading to meticulous) |
| Values / peeves | kindness, knowledge / cruelty, recklessness |
| Dream | Heal people (one everyone else gave up on) |
| Tier | Story-driving |
| First / last | Ch 1 / Ch 55 |

### Arc

- **Wants:** to heal someone everyone else gave up on.
- **Fears:** losing a patient because she was not there.
- **Secret:** she keeps a private notebook of every patient she could not save, and reads it before
  every surgery.
- **Knows, and when:** the hospital's routines from Beta 2 (she helps on the night shift side quest,
  `district.b2.night_shift`, as a trainee runner); **she keeps the surgery roster** from her
  Chunin rotation on, and copies the older rosters into a clean book (the record the case board
  reads in Ch 38).

**The roster and the medic's alibi (fair play).** In every save, before Ch 38, squad4_c says the
same thing about the night of the missing ledger pages: "I copied that night's roster. I don't
remember it; I was asleep in the herb room." She never volunteers the roster's contents and the
player cannot ask before Ch 38. **At the case board** (Ch 38) the player can ask her for the
night's page:

| `twist.traitor` | What the copied roster shows |
|---|---|
| `medic` | A twenty-minute gap in the medic's surgery that night (she copied it faithfully, never noticed) |
| Anyone else | The medic in surgery from dusk to dawn |

Her reaction is the same in both: "I copied it. I didn't read it like that." In the bound save she
is shaken, because she admires the medic; it becomes part of her arc (below).

| Arc | How she changes |
|---|---|
| Cinders | The quiet one with herbs; patches the class after Ch 2's spars |
| Paper Trail | Gathers herbs with the player for `clan.suzuran.1`; helps on the night shift side quest (if done) |
| Dusk | Ch 16 to 19: treats the injured in the forest and the stands |
| Embers | A Chunin on the medic's rotation; **Ch 25**: in the hospital after the border post, she changes the player's bandages and talks to the fallen friend while they sleep |
| Ashes | **Ch 38**: the roster (above). If the medic is the voice, she visits the medic in a cell and asks why; if innocent, she becomes the medic's partner in treating the lost child |
| Last Bonfire | Treats the lost child after her return (N6 or Ch 47) with the medic (or alone, if the medic is arrested). **Ch 51a to 51b**: runs the hospital with sensei_4 and the medic through the assault. **Ch 52 to 53**: climbs the Rock's slope after the player; one way the second lives (below) |

**Ch 53.5: the revival.** If `friendship [squad4_c, 6]` and `ans.squad4_c.second` is not "someone
else first" (unset counts as yes), she is on the Rock's slope (she climbs after the player in Ch 52) and the player can kindle her healing past its limit: it becomes a
revival, and the second, torn hollow, comes back. This is one of the three ways for `story.second.lives` (53.5, before the leader's end), with the
web at "strong" or above and `friendship [yugure_second, 4]`. Her line: "Everyone gave up on her. I
didn't get the chance to."

**Endings.** The hospital's head herbalist; her notebook of the lost has one name crossed out (the
second, if she lived because of her; or the lost child's old number, struck through when she gets
her name back).

### Relationships

- **The medic:** her teacher; admiration that survives either rotation (betrayed or vindicated).
- **squad4_a:** her confidante; they study chakra paths together.
- **squad4_b:** her most frequent patient.
- **The lost child:** her hardest patient, and later her friend; they share the herb room's quiet.
- **The player:** she patched them in Ch 2 and has a page for them in every notebook.

### Dialogue brief

**Voice.** Soft, careful, medical terms she translates kindly. Asks "Does it hurt here?" before
anything else. Never lies about an injury; never says "you'll be fine" unless it is true. Child:
shy. Teen: steady. Adult: calm in every storm.

*Voice samples, not shipped lines:*
- "Does it hurt here? ...And here? Then it's not broken. It's just angry."
- "Lily of the valley is poison. It's also medicine. It depends on the hand."
- "I copied it. I didn't read it like that."
- (to the lost child) "You don't have to talk. I'll tell you what each herb is. You can just listen."
- (Ch 53.5) "Everyone gave up on her. I didn't get the chance to."

**Topics by depth.**

| Depth | What she says |
|---|---|
| Hobby (2) | Herbs; she gives you one with its use |
| Family (4) | The Suzuran herb gardens; a grandmother who tested poisons on herself |
| Values (5) | "The patient decides what they can bear. Not me." |
| Dream (6) | The one everyone gave up on |
| Worries (7) | The notebook of the lost |

**Never reveal before.**

| Fact | Gate |
|---|---|
| The roster's contents for the night of the pages | Ch 38 |
| Her notebook of the lost | Level 7 |
| Anything about the medic's guilt or innocence | Ch 39 / Ch 40 |

**Questions for the player.**

| Id | When | Question | Options | Honours / tests | Remembered | How it changes her |
|---|---|---|---|---|---|---|
| `ans.squad4_c.poison` | `clan.suzuran.1` or a herb walk, level 2 | "Would you taste it? I promise it's mild." | "yes", "only if you taste it first", "no" | Trust | She serves you that herb tea for good | — |
| `ans.squad4_c.hurt` | Ch 25, the hospital | "Does it hurt more where they hit you, or where you watched them fall?" | "where I watched", "both", "neither, I'm fine" (a lie she hears) | Honesty | Her bedside lines in Ch 47 | Lying makes her watch you more closely |
| `ans.squad4_c.give_up` | Embers, level 5 | "When is it right to stop trying to save someone?" | "never", "when they ask you to", "when trying hurts someone else" | Kindness, knowledge | Ch 53.5 revival line | Decides whether she climbs the Rock in Ch 52 eagerly ("never") or reluctantly (the others; unset: steadily, without a line) |
| `ans.squad4_c.roster` | Ch 38, after the page | "Should I have read it sooner?" | "you couldn't have known", "yes, and you'll read everything now", "it's not your fault, it's theirs" | — | Her ending (meticulous or gentle) | Shifts her archetype toward meticulous ("yes") |
| `ans.squad4_c.lost_child` | After the lost child's return | "She asked me what her real name was. I don't know. Do I tell her I don't know?" | "tell her", "help her find it", "let her choose one" | Honesty; freedom | `story.lost_child.family_known`: her name scene | — |
| `ans.squad4_c.notebook` | Level 7 | "This is everyone I couldn't save. Do you want to see?" | "yes", "only if you want me to", "burn it" | Respect | Ch 55: the crossed-out name | — |
| `ans.squad4_c.bruise` | After Ch 2, level 1 (she patches the class) | "Did the rival do this or did you do it falling?" | "the rival", "me, falling", "the camps taught me to fall" | Honesty | She asks the rival to spar more gently, or teaches you to fall better | Filler |
| `ans.squad4_c.medic` | Paper Trail, level 3 | "I want to be a medic like {name:medic}. Is that a good thing to want?" | "yes", "be a medic like you", "be better than them" | Kindness, knowledge | Ch 39 or Ch 40: how she speaks of the medic once the truth is out | Her admiration's shape |
| `ans.squad4_c.forest` | Ch 16, treating a teammate at camp, level 3 | "If two people are hurt and I can only help one, how do I choose?" | "the worse hurt", "the one who can still fight", "ask them" | Kindness against duty | Ch 51: whom she treats first at the hospital | — |
| `ans.squad4_c.herb` | Ashes, level 5 (a herb walk) | "Lily of the valley is poison and medicine. Which are you?" | "medicine", "poison", "depends on the hand" | Creativity, honesty | Her Ch 53 line when the player kindles her | — |
| `ans.squad4_c.second` | Ch 49 to 52, if the second is with the Leaf, level 4+ | "She tore half the village. Would you want me to save her, if it came to it?" | "yes", "only if she wants it", "save someone else first" | Kindness against justice | Ch 53.6: "yes" or "only if she wants it" lets her try the revival; "someone else first" she treats the wounded instead and the revival needs another path | Gates her revival |

**What her lines are for.** Clue (the roster, Ch 38; identical before), plot (the lost child's care,
the Ch 53 revival), bond, teach (herb items, healing buffs), life. Mood states: by the medic's
rotation after Ch 39 (grieving the medic's betrayal, or working beside them).

**Variants.** Varied may roll any clan; the ★ trait is **the medic trainee who keeps the roster**.
Skins: a Suzuran herbalist, a clanless hospital orphan, a Haruno with medical ninjutsu.

**Unison technique (Blaze).** *Ember Mend*: her healing carried along every linked thread at once,
so the whole squad heals while she touches one.

**Thread Sight.** Her thread to the medic is very strong; in the bound save it frays at Ch 39 and
slowly mends if she visits the cell.

---

## New flags

- `ans.squad4_a.shadow` (close, distance, with_me)
- `ans.squad4_a.pass` (trust, come, blame)
- `ans.squad4_a.choose` (duty, fairness, explain)
- `ans.squad4_a.aunt` (honest, little, ask)
- `ans.squad4_a.petition` (yes, with_branch, not_yet)
- `ans.squad4_a.calligraphy` (fire, home, friend)
- `ans.squad4_b.dog_name` (guess1, guess2, guess3)
- `ans.squad4_b.joke` (best, when_want, good_joke)
- `ans.squad4_b.b` (every_night, space, food)
- `ans.squad4_b.hokage` (no, vote, good)
- `ans.squad4_c.poison` (yes, you_first, no)
- `ans.squad4_c.hurt` (watched, both, fine)
- `ans.squad4_c.give_up` (never, they_ask, hurts_others)
- `ans.squad4_c.roster` (couldnt_know, read_all, theirs)
- `ans.squad4_c.lost_child` (tell, find, choose)
- `ans.squad4_c.notebook` (yes, if_you_want, burn)
- `ans.squad4_a.bow` (dont, same, nod)
- `ans.squad4_a.prelim` (no, thank, again)
- `ans.squad4_a.log` (yes, keep, burn_friends)
- `ans.squad4_a.branch` (first, both, ask)
- `ans.squad4_a.eyes` (theirs, beside, link)
- `ans.squad4_b.goat` (you, dog, ramen)
- `ans.squad4_b.beetle` (never, little, yes)
- `ans.squad4_b.test` (easy, hard, dog_food)
- `ans.squad4_b.dog_hurt` (right, sit, bravest)
- `ans.squad4_c.bruise` (rival, falling, camps)
- `ans.squad4_c.medic` (yes, like_you, better)
- `ans.squad4_c.forest` (worse, can_fight, ask)
- `ans.squad4_c.herb` (medicine, poison, hand)
- `ans.squad4_c.second` (yes, if_wants, someone_else)
- Token: `{pet:squad4_b}` (the ninken's rolled name)
