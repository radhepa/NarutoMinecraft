# `role:hokage_5`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md).

## At a glance

| | |
|---|---|
| Role | The Fifth Hokage, named in Ch 20; steps down in Ch 31 |
| Look (fixed) | A severe woman of about fifty, pale Byakugan eyes, black hair tied high and tight, a narrow face carved on the Rock (Ch 32). Hokage robes worn buttoned to the throat; after Ch 31 a plain Hyuga main-house kimono and a sensor's headband |
| Pronouns | She / her |
| Clan | Hyuga (main house); the `elder_hyuga` is her uncle |
| Rank | Jonin, sensor captain, then Hokage |
| Archetype | `stern` (warmth -.1, bold .3, pride .4, discipline .9, open -.5) |
| Values | Duty, loyalty |
| Peeves | Recklessness, lateness |
| Dream | Protect the village |
| First appears | Ch 19 (in the Kage box beside the Fourth, a sensor captain) |
| Named | Ch 20.2 |
| Steps down | Ch 31.4 |
| Last appears | Ch 51.1 (on the wall), Ch 55 (at the inauguration) |

## Arc

### Why she fears the Kagari (a real reason)

1. **The Hyuga record of the Valley of Ash.** The Hyuga were in that valley. Her great-grandfather's
   Byakugan saw the chakra torn out of four thousand soldiers at once, flowing in one direction,
   toward one man. He wrote it down. Every main-house child reads it at twelve. She can recite it.
   The Hyuga call that direction of flow "the lean".
2. **The Ash Road (Y-8).** As a young sensor captain she led the response team to the Ash Road
   ambush. She saw `fallen_parent`'s body and the ash-violet char on the chakra paper scattered
   around it, and the sensei, burned, trying to pull a corpse out of a fire. She signed nothing (the
   elders sealed it) but she knew it was not bandits. Someone hunts that blood, and where it is,
   people die.
3. **The stadium (Ch 19).** With her Byakugan she saw the attack's chakra **lean** toward a child on
   the east stair. The lean from the record. Then she heard the word "Kagari" from a sensor's
   report. She was named Hokage the next day.

4. **The gift as a weapon.** What the Hyuga record really describes is not only taking: the Kagari
   could also *push* chakra into their own soldiers until those soldiers' techniques went past
   any limit the body should allow. The record calls the Kagari's allies in that war "monsters
   made of men". She fears a gift that can make any shinobi monstrous, and a village that would be
   tempted to use it (she is right about the second half: see the Undercroft).

She is not a bigot about the blood; she is a soldier who has seen what follows it twice and will
not see it a third time inside her walls.

### Wants

Order, so no one else is hollowed. A village that sees threats coming.

### Fears

That she is the hard, frightened kind of leader who did the Quiet Ending (she does not know about
it until Ch 40, and when she learns it, it is the worst day of her life).

### What she knows, and when

| By | She knows |
|---|---|
| Ch 20 | The lean; the word; the Ash Road was Yūgure |
| Ch 22 | That the player is "anomalous", and (if told) the word |
| Ch 31 | That her lockdown was wrong and the Tobari innocent |
| Ch 40 | The Quiet Ending. She attends the council as former Hokage and stays when her uncle walks out |

### How she changes

| Stretch | Who she is |
|---|---|
| Ch 20 to 31 | The hard line: curfews, sensor sweeps (the Yamanaka sensor `squad3_c` is the one who flags the player "Anomalous" in Ch 22), the player watched by her niece `squad4_a`; her Jonin Commander is `sensei_2`. Fair but cold; she never lies to the player and never insults them |
| Ch 31 | She steps down to take responsibility, quoting the player's own answer back to herself |
| Jonin arc | She trains young sensors and comes to the Ch 40 council; she apologises to the Tobari publicly (a `clan_event tobari +` beat) |
| Ch 51 | She fights on the wall beside the Tobari she locked down. Her Byakugan finds the array's anchors as they flare; she calls them out to the defenders |

## Dialogue brief

### Voice

- **Clipped, formal, exact.** Full sentences, no softening words. She asks one question at a time
  and waits.
- **She addresses the player by rank** ("Chunin {family:player}" — the dialogue session should use
  `{name:player}` or the rank alone if the family token is empty) until she steps down; after, by
  given name, which surprises them.
- **She reports what she sees with the Byakugan as fact**: "Your chakra leans."
- **Never says:** "Kagari" first (she makes the player say it, or the elder); a threat; "I'm sorry"
  before Ch 31.

*Voice samples, not shipped lines:*

- (Ch 20.2) "Curfew begins at twenty-two hundred. Sensors will walk every street. This is not
  punishment. It is attention."
- (Ch 22.2) "What did the woman in the stadium say to you?"
- (Ch 31.4) "I asked you what you would do if your power endangered this village. I should have
  asked myself."
- (Ch 51.1) "Anchor on the east granary, third beam. Go. I see it burning."

### Never reveal before

| Line or fact | Not before |
|---|---|
| The Hyuga record of the Valley (in words) | Ch 22 at the earliest, only if the player asks "Why do you fear it?" (topic opens at `friendship 2`); in full at Ch 31.4 |
| That she was on the Ash Road response | Ch 31 (her stepping-down talk) or after; in lineage B she says it to the player only after Ch 48 if they ask |
| The word "Kagari" from her own mouth | Ch 31.4 |

### Questions for the player

| Id | When | Question | Options | Honours / tests | Remembered | How it changes her |
|---|---|---|---|---|---|---|
| `ans.hokage_5.word` | Ch 22.2 | "What did the woman in the stadium say to you?" | silent (keep the promise), tell ("Kagari"), why (ask why she wants to know) | Silent honours loyalty but violates her duty; tell honours duty | Ch 31.4: silent: "You kept your sensei's secret from a Hokage. I would have done the same at your age. I'd have been wrong too"; tell: "You told me the truth when it cost you" | Telling makes her trust the player a little; she softens her niece's orders (`squad4_a`, the Hyuga sensor who shadows the player) |
| `ans.hokage_5.danger` | Ch 22.3 | "If your power endangered this village, what would you do?" | leave, control, trust (the village to help) | Leave honours duty; control honours discipline; trust tests her | Ch 31.4 (quoted back), Ch 51.1 ("You said you'd trust the village. Here it is") | "Trust" is the answer that brings her down: she realises she never trusted it |
| `ans.hokage_5.fear` | Ch 22 to 30, a talk at `friendship 2` (optional) | (Player asks: "Why are you afraid of it?") She answers with a question: "Have you ever seen a field of people lying down at once?" | yes (the nurseries), no, I've seen one person | Honesty | Ch 31.4: she adds the Valley story if the player asked | Opens her Valley record early |
| `ans.hokage_5.wrong` | Ch 32 to 40, a visit to her after she steps down | "Was I wrong to be afraid? Or only wrong in what I did?" | wrong to be afraid, only in what you did, neither | Honesty; "only in what you did" honours her duty | Ch 40: she stays at the council; Ch 51.1 | "Only in what you did" lets her come back to serve; "wrong to be afraid" makes her train sensors to look for help, not threats (a line in Ch 51) |
| `ans.hokage_5.hyuga` | Ch 40, after the council | "My uncle walked out. Should the Hyuga apologise too? We were in that valley. We were on that council." | yes, it's not your crime, only if you mean it | Family vs honesty | Ch 51.1 (she fights beside the Tobari; if "yes", the Hyuga main house sends its sensors to the wall) | Moves `clan_relation hyuga` with the village and the Tobari |
| `ans.hokage_5.beside` | Ch 51.1 | "Will you let me fight beside you? I owe you a wall." | yes, you owe the Tobari not me, go where you're needed | Loyalty | Ch 55: she stands at the inauguration on the player's left or with the Tobari | — |
| `ans.hokage_5.lean` | Ch 22.2, after the word | "Your chakra leans toward your sensei when you are afraid. Do you know why?" | they saved me; I don't know; does yours lean toward anyone? | Honesty; the last tests her | Ch 31.4: if asked about hers, she answers it there: "Toward my niece. I never told her" | Asking makes her human in the player's eyes earlier (a `squad4_a` line about it later) |
| `ans.hokage_5.curfew` | Ch 25 to 30, the first night-pass request | "You requested a night pass. For what?" | training; a friend; I don't owe you that | Honesty vs freedom | Ch 31.3 (the council hears whether the player ever lied to her) | "I don't owe you that" makes her deny the pass and respect the answer |
| `ans.hokage_5.successor` | Ch 31.4 | "Who should come after me? You may answer. Hyuga do not usually ask." | the Yamanaka, your Jonin Commander, someone who isn't afraid | Duty | Ch 32.1: she names the Sixth either way, but quotes you if "isn't afraid" ("I was told someone who isn't afraid. He is afraid of nothing but lying") | — |
| `ans.hokage_5.niece` | Ch 32 to 40, a visit | "My niece still follows you, off duty now. Should I worry?" | no, she's my friend; she's better than her orders were; ask her | Family | `squad4_a`'s own arc (her aunt's blessing or worry) | "Ask her" makes the Fifth talk to her niece, a reconciliation in their house |
| `ans.hokage_5.face` | Ch 55, at the inauguration | "Will you keep my face on the Rock? After what I did?" | yes; yes, with the Tobari's story beside it; it isn't mine to decide | Duty / honesty | Epilogue: a plaque beside her face, or nothing | — |

### What her lines are for

| Function | Where |
|---|---|
| **Pressure** | The Chunin arc's antagonist inside the walls; her rules are the arc's systemic friction (curfew) |
| **Theme** | Fear of the blood, made understandable, then corrected by the player's own answer |
| **Redemption** | Ch 31, 40, 51 |
| **Mood states** | `hokage` (cold), `stepped_down` (formal, warmer), `wall` (battle) |
| **Pools** | `story.hokage_5.<chapter>.<beat>`, bond pools in her voice from Ch 32 (`bond.greet.level.<n>.hokage_5`) |

### Variants

| Flag | Changes |
|---|---|
| `twist.fourth_fate` | Ch 20.2: falls: named at the funeral; crippled: named by the Fourth from his bed ("She is hard. The Leaf needs hard for a while"); taken: "until he returns", and she keeps his chair empty beside hers |
| `twist.lineage = fallen` | After Ch 48: she tells the player she saw their parent on the Ash Road, and that they were trying to get the sensei out, not the other way round |

## New flags

- `ans.hokage_5.fear` (field_yes, no, one_person)
- `ans.hokage_5.wrong` (afraid, what_you_did, neither)
- `ans.hokage_5.hyuga` (yes, not_your_crime, mean_it)
- `ans.hokage_5.beside` (yes, tobari, needed)
- `ans.hokage_5.lean` (saved_me, dont_know, yours)
- `ans.hokage_5.curfew` (training, friend, dont_owe)
- `ans.hokage_5.successor` (yamanaka, commander, unafraid)
- `ans.hokage_5.niece` (friend, better, ask_her)
- `ans.hokage_5.face` (yes, tobari_plaque, not_mine)
