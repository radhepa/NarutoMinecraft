# The ensemble

> **SPOILERS: for developers only.** Part of the [story bible](STORY_BIBLE.md).

The Leaf of this story is a class, not a squad. The player's class graduates as **four squads**,
and a **senior squad** a year ahead takes the same Chunin Exams. Five Jonin teach them. Every one
is a real character with a clan (or "no clan" and an ordinary family name), a specialty, a voice,
a want, a flaw and an arc, and most of them move the main plot at least once.

Names are rolled per save and written **Given Family**. Placeholders below are samples only.

## The class (Classic clans)

The class leans toward the noble clans so familiar names appear early (8 noble, 2 minor, 1
clanless, plus the player). Varied saves roll the class with the ranks session's class weights;
the **role traits** marked ★ stay fixed in every save, whatever the clan.

| Squad | Sensei | Members |
|---|---|---|
| **1** | `sensei` (no clan; quiet, burn scar) | The player; `teammate_a` (Kurama, genjutsu painter); `teammate_b` (no clan, brawler with a stray pup) |
| **2** | `sensei_2` (Shiranui; senbon; cool, teasing; your sensei's self-declared rival) | `rival` (Uchiha, prodigy); `classmate_c` (Kinoshita, carpenter's child); `classmate_d` (Gekko, kenjutsu prodigy) |
| **3** | `sensei_3` (Yuhi; genjutsu; the third member of the Ash Road team) | `squad3_a` (Nara, strategist); `squad3_b` (Akimichi, ★ the Fourth's grandson); `squad3_c` (Yamanaka, ★ sensor) |
| **4** | `sensei_4` (Morino; interrogator; stern face, bakes at home) | `squad4_a` (Hyuga main house, ★ the future Fifth's niece, Byakugan); `squad4_b` (Inuzuka, huge ninken); `squad4_c` (Suzuran, ★ herbalist medic trainee) |
| **Senior** | `sensei_5` (Uzumaki; ★ sealing master; old, loud, warm) | `squad5_a` (Sarutobi, staff fighter, ★ wants to be Hokage); `squad5_b` (Tobari, ★ night scout of the Tobari quarter); `squad5_c` (★ no clan, ordinary family name; a clanless prodigy from a poor home who outworks everyone) |

**Clan power.** On average the clan-born are stronger: the rival and squad4_a lead the class.
The exception is squad5_c, the strongest genin of all and clanless, who got there by working three
jobs and training at night. squad4_b and teammate_b start lowest and catch up late.

**Promotion (Ch 20).** The player, the rival, squad5_c, squad4_a, and whichever of the player's
teammates has the higher power level. The rest of the main ensemble make Chunin at the next
season's exams, during the time skip. squad4_b fails twice and is promoted late in the Chunin arc
(a side story, `side.c.third_time`).

## Two tiers

| Tier | Who | What they do |
|---|---|---|
| **Story-driving** | All five senseis; the rival; teammates a and b; squad3_a, squad3_b, squad3_c; squad4_a, squad4_c; squad5_a, squad5_b, squad5_c | Each moves the main plot at least once (a clue, a choice, a rescue, a betrayal or not, a sacrifice) |
| **Fan-favourite** | `classmate_c`, `classmate_d`, `squad4_b` | Side quests, bonds, comedy and heart; small, warm moments in the main path |

## The senseis

| Role | Specialty | History and ties | Want | Flaw | Arc |
|---|---|---|---|---|---|
| `sensei` | Lightning and ninjutsu; reads people | The Ash Road team (with `fallen_parent` and `sensei_3`); `sensei_2`'s rival since the Academy | To keep this squad alive | Silence; carries guilt instead of saying it | Captain → sensei → the Seventh ([file](CHARACTERS/sensei.md)) |
| `sensei_2` | Senbon, speed, the Hokage's guard | Your sensei's classmate and self-declared rival (a running tally of absurd contests: who eats slower, who can stand on one foot through a council meeting). Was not on the Ash Road mission and has always half-blamed themself for not being there | To win one contest that matters | Treats everything as a game so nothing can hurt | Pillar jonin → the Fifth's Jonin Commander, enforcing a curfew he hates → sides with the player at the council (Ch 31) → dies holding the main gate in the war (Ch 51), "winning" the last contest |
| `sensei_3` | Genjutsu, the Yuhi grove | The Ash Road team's survivor: the sensei sent her back to signal for help, so she lived; the two have never talked about that night | To be forgiven by the one person who never blamed her | Cannot accept being spared | Teaches the trio → reads the Ash Road report in the archive with your sensei (Ch 36) and finally speaks of that night → in the war, her genjutsu hides the Academy's evacuation (Ch 51) |
| `sensei_4` | Interrogation, binding, reading lies the ordinary way | A Morino: the village fears his clan; at home he bakes for his squad | To be trusted, not feared | Believes the worst of people first; it is usually right, and it costs him | Interrogates the smuggler (Ch 14), the tester (Ch 23), tries to hold back the porter's seal (Ch 28), sits with the player at the case board (Ch 38: asks good questions, never gives answers), makes the arrest (Ch 39) |
| `sensei_5` | Sealing, Uzumaki chakra | Old (Uzumaki live long); taught half the senseis; knew the Third | To pass on everything before he goes | Talks too much, listens too late | Seals the stadium gates for the evacuation (Ch 19), breaks the archive's old seals with the keeper (Ch 36), teaches the village to break cinder seals (Ch 50), holds the array's last anchor shut on the Rock while the player fights (Ch 52) |

## The genin, beyond the original cast

| Role | Specialty and style | Want | Flaw | Story weight (main path) |
|---|---|---|---|---|
| `squad3_a` (Nara) | Shadow binding; shogi; plans ten moves ahead | Never to be the reason a plan fails | Freezes when the unexpected happens | Ch 16: her plan saves both squads in the forest; Ch 50: she plans the hunt for the eighty-one anchors; Ch 51: when the gate falls her plan breaks, and she improvises for the first time |
| `squad3_b` (Akimichi) | Expansion; a cook | To be himself and not his grandfather's grandson | Thinks he must carry the Fourth's weight | The Fourth's fate hits him first (Ch 19 to 21: grief, a caretaker's life, or the Empty Seat rescue he insists on joining); Ch 51 holds the Academy door; Ch 55 restores the stipend with the player |
| `squad3_c` (Yamanaka) | Sensing, mind techniques; the flower shop | To be sure of people | Reads people so well he trusts no one | Ch 3 senses the flare; Ch 22 is the sensor who flags the player "Anomalous" and carries the guilt; Ch 44 senses the "too many voices" in the lost child; Ch 49 to 50 senses the array's anchors |
| `squad4_a` (Hyuga) | Byakugan, Gentle Fist | To be fair, in a house built on rank | Obeys until it is too late | Ch 22 is assigned to shadow the player, and becomes a friend; Ch 31 testifies against her aunt's lockdown; Ch 40 stays when her great-uncle walks out; Ch 51 is the Seventh's eyes |
| `squad4_b` (Inuzuka) *fan favourite* | Fang techniques with a ninken the size of a pony | To be taken seriously | Loud at the wrong moments | teammate_b's loud rival-friend; Ch 26 keeps b company if b leaves; Ch 51 the dogs hold the market street with b. `side.c.third_time`: promoted at last |
| `squad4_c` (Suzuran) | Herbalism, poisons, medical ninjutsu | To heal someone everyone else gave up on | Hides behind work | Works beside the medic; the surgery roster is hers (the medic's alibi, Ch 38); treats the lost child after her return; Ch 53: kindled, her healing becomes a revival (one way the second can live) |
| `squad5_a` (Sarutobi) | Staff combat, fire | To be Hokage | Believes in the village like a scripture | The player's rival for the Eighth's seat, cheerfully. Ch 40: the Third kept the silence, and his faith breaks; Ch 42 he chooses the Seventh's side anyway; Ch 55 becomes the Eighth's Jonin Commander after `sensei_2` |
| `squad5_b` (Tobari) | Silent scouting, smothering | That her quarter is seen | Says nothing even when she should | Ch 30 to 31: her quarter is locked down; she is the player's partner in the lanes and the drain; her grandmother, a Tobari elder, is the first near-stranger to kindle toward the player |
| `squad5_c` (no clan) | Kenjutsu and ninjutsu, self-taught | Never to be poor or powerless again | Takes any power offered | Ch 19 fights the blade beside your sensei and takes a scar; joins the ANBU young; is recruited by the Undercroft (N-branch) and sent to take the lost child. Ch 44 or Ch 47: he comes for her; the player talks him down or fights him. **A betrayal or not** |

## Where the ensemble moves the plot

| Ch | Who | What |
|---|---|---|
| 1 | All | The class at enrolment |
| 3 | squad3_c | Senses the flare: "Your chakra just moved into theirs." |
| 6 | squad3_b, squad3_a | Join the study night with food from the barbecue house; squad3_b is the Fourth's grandson |
| 7 | Senior squad, rival | The senior squad watches the graduation; nobody from the rival's family is there |
| 8 | All senseis | Assignment; sensei_2 challenges your sensei to a contest on the spot |
| 10 | sensei_3 | At the memorial stone with your sensei |
| 14 | sensei_4 | Interrogates the smuggler |
| 16 | squad3 | A truce in the forest; squad3_a's plan |
| 17 | squad5_c | Wins his preliminary in seconds |
| 19 | sensei_2, sensei_5, squad5_c, squad3_b | The Kage box, the sealed gates, the duel with the blade, the Fourth |
| 21 | squad3_b, sensei_2 | The Fourth's year; the Empty Seat rescue (taken) |
| 22 | squad3_c, squad4_a | The flag; the shadow |
| 23 | sensei_4 | The tester |
| 26 | squad4_b | With b |
| 28 | sensei_4 | The porter's seal |
| 30 to 31 | squad5_b, squad4_a, sensei_2 | The Tobari crisis |
| 35 | squad3 | The Valley of Ash with your old squad |
| 36 | sensei_3, sensei_5 | The archive |
| 38 to 39 | sensei_4, squad4_c | The case board; the arrest |
| 40 | squad5_a, squad4_a | Faith and fairness at the council |
| 44, 47, N-branch | squad5_c, squad3_c | The lost child |
| 49 to 50 | squad3_a, squad3_c, sensei_5 | The anchors |
| 51 | sensei_2 (dies), sensei_3, squad3_a, squad3_b, squad4_a, squad4_b, teammate_b | The war |
| 52 | sensei_5 | The Rock |
| 53 | squad4_c, everyone | Every fire |
| 55 | squad5_a, squad3_b, classmate_d | The Eighth's first day |
