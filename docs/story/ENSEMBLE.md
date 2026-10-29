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
the **role traits** marked ★ stay fixed in every save, whatever the clan. Three roles also keep
their **clan** in every save because a fixed-look Hokage is their relative: `squad3_b` (Akimichi,
the Fourth's grandson), `squad3_c` (Yamanaka, the Sixth's nephew) and `squad4_a` (Hyuga, the Fifth's
niece). Pronouns below are Classic; all ensemble looks are rolled in Varied, so dialogue uses
pronoun tokens.

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

**Voices that must not blur.** The rival issues challenges and asks questions dressed as insults
(no catchphrase, no scorekeeping). `sensei_2` keeps score. `squad5_c` prices things ("Pay it.").

## The senseis

| Role | Specialty | History and ties | Want | Flaw | Arc |
|---|---|---|---|---|---|
| `sensei` | Fire and ninjutsu (a fire user burned on the Ash Road); reads people | The Ash Road team (with `fallen_parent` and `sensei_3`); `sensei_2`'s rival since the Academy; `sensei_5`'s old sealing student | To keep this squad alive | Silence; carries guilt instead of saying it | Captain → sensei → the Seventh ([file](CHARACTERS/sensei.md)) |
| `sensei_2` | Senbon, footwork, the Hokage's guard | Your sensei's classmate and self-declared rival: a running tally of senbon-footwork contests on guard rotations (threading senbon through the wall walk's lantern rings, racing the gate's signal relay). He keeps score: **38 to 211** against him at Ch 8, **51 to 290** by Ch 42, and keeps count anyway. Was not on the Ash Road mission and has always half-blamed himself for not being there | To win one contest that matters | Treats everything as a game so nothing can hurt | Pillar jonin → the Fifth's Jonin Commander, enforcing a curfew he hates → sides with the player at the council (Ch 31) → holds the main gate in the war and dies asking "Did I win?" with the player and the Seventh beside him (Ch 51b; he sent Squad 2 to the Rock's stair and the Residence steps). His notebook's last line: "Held the gate longer than you would have. 52 to 290. Mine." |
| `sensei_3` | Genjutsu of the Yuhi grove (falling leaves); Classic look: grey eyes, short-cropped hair | The Ash Road team's survivor: the sensei sent her back to signal for help, so she lived; the two have never talked about that night | To be forgiven by the one person who never blamed her | Cannot accept being spared | Teaches the trio → reads the Ash Road report with your sensei (Ch 37.0) and finally speaks of that night → in the war, her genjutsu hides the Academy's evacuation (Ch 51a) |
| `sensei_4` | Interrogation, binding, reading lies the ordinary way | A Morino: the village fears his clan; at home he bakes for his squad | To be trusted, not feared | Believes the worst of people first; it is usually right, and it costs him | Interrogates the smuggler (Ch 14), the tester (Ch 23), tries to hold back the porter's seal (Ch 28), sits with the player at the case board (Ch 38: asks good questions, never gives answers), makes the arrest (Ch 39) |
| `sensei_5` | Sealing, Uzumaki chakra | Old (Uzumaki live long); taught half the senseis, and sealing to the player's sensei ("my quiet one"); knew the Third | To pass on everything before he goes | Talks too much, listens too late | Seals the stadium gates for the evacuation (Ch 19), breaks the archive's old seals with the keeper (Ch 36), teaches the village to break cinder seals (Ch 50), holds the array's last anchor shut on the Rock while the player fights (Ch 52) |

## The genin, beyond the original cast

| Role | Specialty and style | Want | Flaw | Story weight (main path) |
|---|---|---|---|---|
| `squad3_a` (Nara) | Shadow binding; shogi; plans ten moves ahead | Never to be the reason a plan fails | Freezes when the unexpected happens | Ch 16: her plan saves both squads in the forest; Ch 50: she plans the hunt for the eighty-one anchors; Ch 51a.5: when the main gate breaks her plan breaks with it, and she builds the second line behind it, improvising for the first time |
| `squad3_b` (Akimichi) | Expansion; a cook | To be a chef and a shinobi both, and not his grandfather's shadow | Thinks he must carry the Fourth's weight | The Fourth's fate hits him first (Ch 19: on the stair beside the player, he runs to his grandfather, hit on the same stair; Ch 20 to 21: the farewell feast, a caretaker's life, or the Empty Seat rescue in which he carries his grandfather out); Ch 51a holds the Academy door; Ch 55 stands beside the player when the stipend is written into law in the Fourth's name |
| `squad3_c` (Yamanaka) | Sensing, mind techniques; the flower shop | To be sure of people | Reads people so well he trusts no one | Ch 3 senses the flare; Ch 22 is the sensor who flags the player "Anomalous" and carries the guilt; Ch 44 senses the "too many voices" in the lost child; Ch 49 to 50 senses the array's anchors |
| `squad4_a` (Hyuga) | Byakugan, Gentle Fist | To be fair, in a house built on rank | Obeys until it is too late | Ch 22 is assigned to shadow the player, and becomes a friend; Ch 31 testifies against her aunt's lockdown; Ch 40 stays when her great-uncle walks out; Ch 51b is the Seventh's eyes from the Rock's shoulder and guides your crossing |
| `squad4_b` (Inuzuka) *fan favourite* | Fang techniques with a ninken the size of a pony | To be taken seriously | Loud at the wrong moments | teammate_b's loud rival-friend; Ch 26 keeps b company if b leaves; Ch 51a the dogs hold the market street with b. `side.c.third_time`: promoted at last |
| `squad4_c` (Suzuran) | Herbalism, poisons, medical ninjutsu | To heal someone everyone else gave up on | Hides behind work | Works beside the medic; the surgery roster is hers (the medic's alibi, Ch 38); treats the lost child after her return; Ch 53: kindled, her healing becomes a revival (one way the second can live) |
| `squad5_a` (Sarutobi) | Staff combat, fire | To be Hokage | Believes in the village like a scripture | The player's rival for the Eighth's seat, cheerfully. Ch 40: the Third kept the silence, and his faith breaks; Ch 42 the council balks at naming a Hokage who signed the Ash Road field report, and his public stand carries the vote; Ch 55 becomes the Eighth's Jonin Commander after `sensei_2` |
| `squad5_b` (Tobari) | Silent scouting, smothering | That her quarter is seen | Says nothing even when she should | Ch 30 to 31: her quarter is locked down; she is the player's partner in the lanes and the drain; her grandmother, a Tobari elder, is the first near-stranger to kindle toward the player |
| `squad5_c` (no clan) | Kenjutsu and ninjutsu, self-taught | Never to be poor or powerless again | Takes any power offered. Counts coins under his breath; "Pay it." | Ch 19 fights the blade beside your sensei and takes a cut (a scar later); Ch 28.5 grieves the porter, who once carried his sister's cot up four floors; joins the ANBU young; is recruited by the Undercroft (the sealing team's heirs) and sent to take the lost child. Ch 44 hunts her; in N6 (or, without the Night Watch, the morning after Ch 47) he comes for her and the player talks him down or fights him. **A betrayal or not**. Ch 51a: on the wall, if he left the ANBU or stood down |

## Where the ensemble moves the plot

| Ch | Who | What |
|---|---|---|
| 1 | All | The class at enrolment |
| 3 | squad3_c | Senses the flare: "Your chakra just moved into theirs." |
| 6 | squad3_b, squad3_a | Join the study night with food from the barbecue house; squad3_b is the Fourth's grandson |
| 7 | Senior squad, rival | The senior squad watches the graduation; nobody from the rival's family is there |
| 8 | All senseis | Assignment (8.1): in the Academy hall `sensei_2` challenges your sensei to a senbon-footwork contest on the spot, loses, and writes "38 to 211" in his notebook |
| 10 | sensei_3 | At the memorial stone with your sensei |
| 14 | sensei_4 | Interrogates the smuggler |
| 16 | squad3 | A truce in the forest; squad3_a's plan |
| 17 | squad5_c | Wins his preliminary in seconds |
| 19 | sensei_2, sensei_5, squad5_c, squad3_b | The Hokage's seat, the sealed gates, the fight with the blade, the Fourth hit on the east stair carrying children (squad3_b on that stair) |
| 21 | squad3_b, sensei_2 | The Fourth's year; the Empty Seat rescue (taken) |
| 22 | squad3_c, squad4_a | The flag; the shadow |
| 23 | sensei_4 | The tester |
| 26 | squad4_b | With b |
| 28 | sensei_4, sensei_5, squad5_c | The porter's seal; the porter's room |
| 30 to 31 | squad5_b, squad4_a, sensei_2 | The Tobari crisis |
| 35 | squad3, squad4_b | The Valley of Ash: squad3_a's no-fight plan; squad4_b's nose finds the back entrance |
| 36 | sensei_5 | The archive's seals |
| 37.0 | sensei_3 | The Ash Road report: she finally speaks of that night |
| 38 to 39 | sensei_4, squad4_c | The case board; the arrest |
| 40 | squad5_a, squad4_a | Faith and fairness at the council |
| 42 | squad5_a | The contested naming of the Seventh: his public "I'm with them" carries the vote |
| 44, 47, N-branch | squad5_c, squad3_c | The lost child |
| 49 to 50 | squad3_a, squad3_c, sensei_5 | The anchors |
| 51a | the former Fifth, squad5_a, squad5_b, squad3_a, sensei_3, squad3_b, sensei_4, squad4_c, teammate_b, squad4_b, classmate_c, classmate_d, squad5_c | Dusk: the wall (the former Fifth, squad5_a, the Tobari, the Hagane; later squad5_c), the main gate's lanes (squad5_b) and second line (squad3_a, 51a.5), the Academy (the instructor, sensei_3, squad3_b), the hospital (sensei_4, squad4_c, the medic), the market street (teammate_b, squad4_b), the Residence steps (classmate_d, classmate_c) |
| 51b | sensei_2 (dies), squad4_a, the blade, the keeper, the rival | The Door, in order: the gate ("Did I win?"), the crossing (squad4_a's eyes), the blade's last duel (he turns), the archive door, the rival on the Rock's stair, the climb |
| 52 | sensei_5, the blade | The Rock: sensei_5 holds an anchor channel shut; the blade fights the leader beside you and lives |
| 53 | squad4_c, everyone | Every fire |
| 55 | squad5_a, squad3_b, classmate_d | The Eighth's first day |
