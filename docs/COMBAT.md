# Combat

The fighting of the Shinobi Modpack: taijutsu, weapons and ninjutsu as three equal pillars, the hand-sign
system, the full technique catalogue from E to S rank, the 25 clans' techniques, squad and nature
combinations, the bestiary and its AI, bosses, difficulty and feel, progression across the 60-hour story,
and the beta's loadout. It is built in Shinobi Combat (`shinobi_combat`, [ROADMAP.md](../ROADMAP.md#the-pack-separate-mods)).

**No spoilers here.** This file describes systems and data. Story enemies are named by role or neutral id;
what a story boss is lives only in the developers-only [story bible](story/STORY_BIBLE.md), keyed by its id.

**Where it lives.**

| Piece | Where |
|---|---|
| Authoring (the source of truth) | `tools/combat/*.py`: one module per area; `python3 tools/combat/build.py --check` compiles and validates |
| Compiled data | `data/combat/` (143 JSON files, each with `"format": 1`). Phase 0 moves it into the Combat mod's datapack: `combat/src/main/resources/data/shinobi_combat/` |
| Generated reference pages | [combat/techniques.md](combat/techniques.md) (the catalogue), [combat/clans.md](combat/clans.md), [combat/styles.md](combat/styles.md) (combo trees), [combat/bestiary.md](combat/bestiary.md) (enemies, groups, bosses), [combat/animations.md](combat/animations.md) |
| Pure-Java core | [`combat/core`](../combat/core), package `dev.shinobi.combat`: no Minecraft, deterministic, JUnit 5, release 25 |
| Duel simulator | `combat/core/src/test/java/dev/shinobi/combat/sim`: `./gradlew :combat:core:simulate` (balance tables), `:combat:core:trace` (one fight hit by hit) |

```
python3 tools/combat/build.py --check     # compile data/combat/ and docs/combat/, check ids, references, signs, spoilers
./gradlew :combat:core:test               # 48 tests, including the balance guards
./gradlew :combat:core:simulate           # the balance tables (-Pseed=N -Pruns=N)
./gradlew :combat:core:trace -Pargs="sim.beta.taijutsu.11 combat:boss.ch11.bandit_chief 11 shinobi 1"
```

| Counts | |
|---|---|
| Techniques | 220: 95 in the catalogue, 100 clan techniques (25 clans x 4 tiers), 25 lesser techniques; by rank E 6, D 12, C 74, B 51, A 43, S 34 |
| Styles | 9 taijutsu and 12 weapon styles, 105 moves, 8 inner gates |
| Weapons and tools | 25 weapons, 24 tools and consumables, 3 coatings (stats keyed by the items session's item ids) |
| Enemies | 40 human and 11 animal types, 23 groups, 21 bosses (9 in the beta) |
| Combos | 7 nature combos, 11 squad combos, 7 unison families, 9 commands, 5 formations |
| Clips | 233 animation clips (P0 62, P1 107, P2 28, P3 36) |

## Contents

1. [Core resources](#1-core-resources)
2. [Damage, armour and the nature triangle](#2-damage-armour-and-the-nature-triangle)
3. [Status effects](#3-status-effects)
4. [Taijutsu](#4-taijutsu)
5. [Weapons](#5-weapons)
6. [Ninjutsu and hand signs](#6-ninjutsu-and-hand-signs)
7. [Clans](#7-clans)
8. [Combination play](#8-combination-play)
9. [Kindling Bond](#9-kindling-bond)
10. [Enemies](#10-enemies)
11. [Difficulty and feel](#11-difficulty-and-feel)
12. [Progression](#12-progression)
13. [The beta loadout](#13-the-beta-loadout)
14. [The combat core](#14-the-combat-core)
15. [Balance](#15-balance)
16. [Animations](#16-animations)
17. [What waits for Phase 0](#17-what-waits-for-phase-0)
18. [Ids for other systems](#18-ids-for-other-systems)
19. [Open questions](#19-open-questions)

## 1. Core resources

*Data: `core/resources.json`, `core/scaling.json`.* Four bars and two hidden meters. Each pillar has its own
fuel, so a close fighter and a caster are limited by different things.

| Resource | Rule |
|---|---|
| **Health** | Vanilla hearts: 10 at level 1, one more every 6 levels (19 at level 60, ROADMAP Levels), plus gear and clan hearts. Out of combat it regenerates 0.25 a second after 5 s. |
| **Toughness** | The player's body hardens with level: incoming damage is divided by 1 + 0.025 (level - 1). Hearts stay readable while enemies scale. |
| **Chakra** | 50 + 3 per level (53 at level 1, 104 at 18, 200 at 50). Regenerates 0.6 + 1% of the bar a second; x0.75 in a fight, x4 meditating (sneak and stand still a second). Pills and food restore it. |
| **Chakra control** | 0 to 100, from training, not levels (the leaf exercise +5, tree walking +10, water walking +10, medical training +10). Cost x1.15 at 0 down to x0.85 at 100; signs 4 ticks each, 3 from control 80; it stretches wall-runs and gates precision styles and medical ninjutsu. |
| **Stamina** | 100 (+5 per taijutsu rank). Taijutsu and weapons run on it: a light 3, a heavy 12, a dodge 22, a block 4 per point blocked. Refills 30 a second after a 0.75 s pause: about three seconds from empty. Empty: *winded* (no dodge) and a broken guard staggers. |
| **Poise** | Hidden toughness: 20 for the player (+2 per taijutsu rank, more in Strong Fist), 15 to 200 for enemies. Every hit carries poise damage; at 0 the target staggers for 16 ticks (it interrupts casts) and poise refills. Bosses show a poise ring when low. |
| **Momentum** | 0 to 100: +6 a landed hit, +25 a parry, +15 a perfect dodge; -30 when hit; it decays after 2 s. Finishers spend it: the close-range answer to a full chakra bar. |
| **Exhaustion** | Chakra at 0 or a *desperate cast* (casting short by at most a quarter of the cost, paying the shortfall at 0.5 HP a point) leaves you *chakra-exhausted* (slow, half stamina regen, no casting) until a fifth of the bar is back. Closing an inner gate leaves *gate strain*. Shinobi Life's fatigue writes the movement, damage and chakra-regen modifiers combat reads. |

**Scaling.** Levels are power, ranks are story. Everything you deal grows 3% a level, taijutsu 4% (the
roadmap's +1% a level on top). Each **pillar** (taijutsu, weapons, ninjutsu) has a rank from 1 to 10, raised
by use in real fights, drills and a mentor's trial at ranks 3, 6 and 9, worth +7% a rank to that pillar. The
three ranks together cannot pass 3 + level / 2: mid-game you specialise, late-game you round out. Enemies'
health grows 5.5% a level, their damage 3%.

**The player is clanless** (the owner's decision): 10 hearts, chakra 53, control 35, stamina 110, poise 20
(`core/knacks.json`). The creator's **knack** gives +5% to one pillar (`combat:knack.taijutsu`, `weapons`,
`ninjutsu`) or +2% to each (`combat:knack.balanced`, the default), with a starter item from the items
session. The creator's **affinity** is shown at the Genin ceremony as your leaning; choosing it there gives
+10% power with that nature.

## 2. Damage, armour and the nature triangle

*Data: `core/damage_types.json`, `core/armour.json`, `core/natures.json`. Code: `Damage`, `DamageType`, `Nature`, `Scaling`.*

**Damage types.** `physical.blunt` (poise x1.5), `physical.slash`, `physical.pierce` (ignores 30% of armour),
`ninjutsu.fire|wind|lightning|earth|water|none`, `chakra` (Gentle Fist and insects: drains chakra, half to
health, ignores armour), `genjutsu` and `sealing` (no health damage; their strength meets will), `poison`
(over time), `true` (gate strain, desperate casts).

**One hit.** base x level power x pillar rank x the attacker's multipliers (style tier, counter x1.5, focus
x1.25, gates, clan, Bonfire), then the defender's armour of the matching class, the nature triangle against
its affinity, its guard, its statuses (soaked, hardened) and, for the player, toughness. Enemies scale by
their level, their tier's damage multiplier and the difficulty instead of a pillar.

**Armour.** Three classes: *physical* (gear: forehead protector 1, mesh shirt 3, arm and shin guards 2, flak
vest 6, ANBU armour 8), *chakra* (vests, earth armour, some clans) and *will* (genjutsu and sealing: 10 +
0.5 a level, Morino +10, Yuhi and Kurama +8). Reduction = armour / (armour + 20), at most 60%; will scales an
illusion's duration by 1 - will / (will + 40).

**Guard.** A block takes 60% off melee (Iron Guard 75%), 80% off thrown tools, 30% off jutsu (wind pierces 30%
of that) and nothing off genjutsu; it costs 4 stamina per point stopped. A parry or a dodge avoids the hit.

**The nature triangle.** Fire beats wind, wind beats lightning, lightning beats earth, earth beats water,
water beats fire: a cycle of five. A defender with an affinity takes x1.25 from the nature that beats theirs
and x0.8 from the nature theirs beats. When two jutsu collide the stronger nature passes through at half
power; equal natures compare power and the larger keeps the difference. Your own natures' jutsu cost x0.75.

## 3. Status effects

*Data: `core/status_effects.json` (65 statuses). Code: `StatusEffects`.* Each status has a duration, stacks,
what it stops (acting, moving, weaving), what it changes (speed, damage taken), what it cleanses and what it
becomes at full stacks.

| Group | Statuses |
|---|---|
| Damage over time | burning (water cleanses it), bleeding (3 stacks), poisoned (5 stacks; Suzuran immune, Aburame resist) |
| Elemental | shocked (a short stun, then slow), soaked (lightning x1.3, fire x0.7, puts out burning), chilled (slow) |
| Control | stunned, staggered, knocked down, airborne, bound (cannot move), possessed (copies the caster), paralysed, asleep (damage wakes), numbed (3 stacks paralyse), drowsy (3 stacks sleep), fear, confused, blinded, smoked |
| Sealing | silenced, chakra sealed, nature sealed, points closed (Gentle Fist: 64 stacks seal chakra) |
| Self | hardened (earth: physical x0.5), shrouded (lightning armour), expanded (Akimichi), the five blade flows, hidden, disguised, decoy, sensing, focus, counter window, gate strain, chakra exhausted, winded |

**Genjutsu is one shared effect** (`genjutsu`, with a variant: shifted, fear, confusion, phantoms, darkness,
feathers, world, painted, binding, eyes). A caught target sees a client-side illusion (fake entities, a
distorted screen, a wrong HUD) and moves at 60%. It breaks when the target weaves Release (Ram, costing 10 +
half the illusion's rank cost), takes damage over 10% of its health, is touched by a teammate, sees a flash
bomb, or (Sharingan stage 2) watched it being cast. Most genjutsu need the target to see the caster. On a
player it never takes the camera for more than 2 s.

**Diminishing returns.** Within 15 s a second stun lasts half as long, a third a quarter, a fourth not at all;
the same for binds, seals and mind effects. Bosses take half from the first and are immune after the second.

## 4. Taijutsu

*Data: `styles/taijutsu.json`, `styles/gates.json`; every move: [combat/styles.md](combat/styles.md). Code: `Move`, `Style`, `ComboMachine`.*

Taijutsu is a full pillar, never a fallback. Its moves form **combo trees**: each move is reached by an input
path (L light, H heavy held 8 ticks, D after a dodge, P after a parry, J in the air, X off a dash, G while
guarding), with startup, active and recovery frames and a window for the next input. Inputs up to 2 ticks
early are buffered; inside a string vanilla's attack cooldown does not apply. Strings end on a move whose
window is closed (a knockback, a launcher's air string, a finisher).

**Academy taijutsu**, everyone's base (14 moves): jab, cross, roundhouse (the third knocks back), heavy,
flying kick and lunge off a dash, then from Genin the counter (after a parry), sweep (knockdown), launcher
(L L H), a four-hit air string with an air spike, and the palm rush finisher (60 momentum). Every other style
lays its moves over these: where it has a move you qualify for, it plays; otherwise the Academy move does.

| Style | Who | Feel | Slice |
|---|---|---|---|
| Academy taijutsu | everyone | balanced forms; the base | Beta 1 |
| **Strong Fist** | anyone: the master's trial at taijutsu rank 3 and a week of weighted training | hard and fast; heavies keep poise; Leaf Hurricane, Leaf Rising Wind, Leaf Whirlwind, Leaf Great Whirlwind; the gates open Primary Lotus, Reverse Lotus and Morning Peacock | Beta 2 |
| **Iron Guard** | anyone; the gate guards teach it (Hagane friendship 5) | defensive: punish every blow you block; the iron wall | Beta 2 |
| **Swaying Willow** (the flowing, drunken-looking style) | anyone; a wandering master's side line | every dodge is an attack, the rhythm cannot be read | Chunin |
| **Blossom Strength** | control 70 (Haruno) or 80 (anyone) | chakra-timed heavies that crater the ground (never the map) and break guards | Chunin / Jonin |
| **Lightning Body** | lightning nature, taijutsu rank 7 | lightning armour and wrestling throws | Jonin |
| **Gentle Fist** | Hyuga (needs the Byakugan): an NPC kit | palms that drain chakra and close points; Palm Rotation; 64 and 128 Palms | Beta 2 (NPC) |
| **Iron Body** | Akimichi: an NPC kit | weight as a weapon; Human Boulder; expansion | Beta 2 (NPC) |
| **Beast Fang** | Inuzuka: an NPC kit | on all fours with a ninken | Beta 2 (NPC) |

**Style tiers.** Initiate, adept, expert, master, grandmaster (x1.0 to x1.4), opened at taijutsu ranks 1, 3,
5, 7 and 9 by use and a mentor's trial. Each tier opens moves: finishers at tiers 2 to 5.

**Guard, parry and counters.** Block with right click (Beta 1). Start a block inside the parry window (Story 6
ticks, Shinobi 4, Hard 3) before a melee hit lands: no damage, the attacker staggers for 20 ticks, +25
momentum and a 12-tick counter window (x1.5). Parrying a thrown kunai knocks it down (weapons rank 3 catches
it). Ninjutsu, grabs and red-flash moves cannot be parried. Counters come from parries (P L), Iron Guard's
block counter, Swaying Willow's dodge strikes and counter techniques (Palm Rotation, substitution feints).

**Dodges.** Double-tap a direction or Left Alt: 4 blocks, 6 invulnerable ticks, 22 stamina, 1.5 s cooldown.
Inside the perfect window (Story 8, Shinobi 6, Hard 5) it grants *focus* (+25% on the next attack) and +15
momentum. **Substitution**: dodge as a hit lands with 10 chakra: blink 5 blocks, 12 i-frames, a log takes the
blow; once per 20 s (enemies of Genin rank and up: once a fight).

**Stagger and poise.** See [Core resources](#1-core-resources): heavies, blunt weapons and earth break poise;
a stagger interrupts any cast, and bosses drop into a stagger phase on each poise break.

**Weight and body.** The training weights (Beta 2) slow you 15% and raise taijutsu XP x1.5; releasing them
gives +30% speed for 10 s. The Akimichi's weight is a clan kit (Iron Body, Expansion).

**The inner gates** (Strong Fist tier 3 and taijutsu rank 5 for the first, one more rank per gate). Hold Style
(B) and Weave to open the next gate: each adds damage (+20% at the first to +90% at the sixth) and speed and
drains health while open, then leaves gate strain. Gates 1 and 2 at Chunin, 3 and 4 at Jonin, 5 and 6 on the
road to Hokage, 7 post-game; the eighth is never playable.

**How taijutsu stays competitive all game.**

- It costs stamina, which refills in about three seconds; ninjutsu costs chakra, which takes a minute.
- It scales +4% a level against +3% for the others, plus its pillar rank, the style tier (up to x1.4) and the gates (up to +90%).
- Any melee hit interrupts an enemy weaving, and signs take 4 ticks each: a fighter who closes the gap shuts a caster down. Body Flicker closes it.
- Momentum finishers are the close-range answer to an S-rank jutsu: no chakra, cinematic, bigger at each tier.
- Parries, counters and poise breaks matter against every enemy; bosses have taijutsu openings.
- Enemies that turn ninjutsu (samurai armour, chakra absorbers, barrier users) appear from the Chunin arc.
- Chakra-infused styles (Gentle Fist, Blossom Strength, Lightning Body, chakra flow) let close fighters burst without leaving their pillar.
- The simulator holds it to account: a taijutsu build beats a level-matched elite 64 to 92% of the time on Shinobi at every level from Genin, and its fight length stays flat (8 to 12 s) across the game ([Balance](#15-balance)).

## 5. Weapons

*Data: `weapons/weapons.json` (stats keyed by item id), `weapons/tools.json`, `weapons/coatings.json`, `weapons/throwing.json`, `styles/weapons.json`.*
The items session owns the item registry, prices, crafting and durability; combat owns the stats.

**Melee weapons** (damage multiplies the style moves marked weapon_mult, so it sits near a fist's 2.0: a
blade's edge is reach, slashing, parry frames and its techniques, never twice a punch).

| Item | Damage, type | Reach | Style | Slice |
|---|---|---|---|---|
| `item:practice_kunai` | 1.4 blunt | 2.6 | Academy blade | Beta 1 |
| `item:kunai` | 2.0 pierce (thrown 3.0) | 2.6 | Academy blade | Beta 2 |
| `item:tanto` | 2.3 slash | 2.8 | Academy blade | Beta 2 |
| `item:bokken` | 1.8 blunt | 3.3 | Crescent Moon | Beta 2 (Gekko dojo) |
| `item:ninjato`, `item:katana` | 2.5, 2.7 slash | 3.2, 3.5 | Crescent Moon | Beta 3 |
| `item:kokuto` | 2.5 slash, silent | 3.2 | Wave-foot | Beta 2.5 (from the Namiashi) |
| `item:sarutobi_staff`, `item:bo_staff` | 2.2, 1.9 blunt | 4.5, 4.0 | Monkey King staff | Beta 2 |
| `item:iron_mace` | 2.6 blunt, guard x2 | 3.0 | Mace arts | Beta 2.5 (from the Hagane) |
| `item:weighted_chain`, `item:kusarigama` | 1.8 blunt, 2.0 slash | 5.0, 6.0 | Chain arts | Beta 3, Chunin |
| `item:war_fan`, `item:battle_fan` | 2.0, 2.2 blunt | 2.8, 3.4 | Fan arts | Chunin |
| `item:white_sabre`, `item:chakra_blades`, `item:chakra_metal_kunai` | 3.1, 2.6, 2.4 | 3.0, 2.8, 2.6 | White Fang, Academy blade | Jonin |
| `item:knuckle_wraps`, `item:knuckle_guards` | +0.5, +1.0 to lights | — | taijutsu gear | Beta 1, Beta 2 |

Grades (the items session's standard, fine and masterwork) multiply damage x1.0, x1.1, x1.2. Clan weapons
are given or sold by their clan after its welcome quest at Good Neighbor standing.

**Throwing.** Tap to throw at the crosshair, hold to aim (an arc preview on Story). Kunai (3.0, 12 ticks of
recovery, retrievable, carries a paper bomb or wire), shuriken (2.2, 10 ticks; a fan of three from weapons
rank 2: x1.3 damage, 30% harder to dodge), manji (3.2, bleeding), senbon (1.5, silent, ignores 80% of armour,
carries coatings twice; headshots numb from weapons rank 4), the windmill shuriken (Chunin: pierces three and
returns). Spread grows when moving and shrinks with weapons rank; Story bends 5 degrees toward a lock-on
target. Thrown tools embed for 60 s: walk over them to pick them up, a wired kunai comes back on the throw
key. The thrown tools you carry are lost on death (ROADMAP Death); practice tools never are. The **tool
pouch** (G) throws from 4 pouch slots without touching the hotbar (6 with the large pouch, +1 at weapons
ranks 4 and 8, +2 with a flak vest).

**Tools.** Paper bombs (6, radius 3, 30-tick fuse: a lit tag is seen and walked out of about half the time;
one every 3 s per thrower; a mine for 60 s; Ram detonates every bomb you placed), smoke (enemies lose you),
flash (blinds everyone facing it; breaks allies' genjutsu), stink bombs (animals and civilians flee),
ninja wire (tripwires, tethers, binds, a fire line), makibishi, sealing tags (capture), barrier tags, pills
(soldier, blood, food, chakra candy), salves and antidotes, insect repellent and scent powder.

**Coatings** (Suzuran poisons, crafted at the apothecary table): numbing (6 hits), sleep (4 hits; bosses only
drowsy) and venom (6 hits) on a blade, kunai, shuriken or senbon.

**Weapon styles.** Academy blade, throwing arts, needle arts (Shiranui), Crescent Moon kenjutsu (the Gekko:
wide arcs, a draw-cut counter, the Dance of the Crescent Moon), wave-foot kenjutsu (the Namiashi: short silent
strokes, a guard that steps aside and cuts back), White Fang (Hatake), Monkey King staff (Sarutobi), chain
arts, fan arts, mace arts (Hagane), wire arts (Kinoshita) and Iaido (post-game).

**Weapon-plus-jutsu.** Exploding-tag kunai, Shadow Shuriken, Manipulated Shuriken, Windmill Triple, the
wind-channelled shuriken (double damage, pierces two, range 32), the lightning-charged blade and the other
four blade flows, Dragon Flame down a wire, the storage-scroll barrage, Explosive Kunai Barrage, Rising Twin
Dragons and Shuriken Shadow Clone. They scale with the average of the weapons and ninjutsu pillars and cost
chakra like ninjutsu of their rank.

## 6. Ninjutsu and hand signs

*Data: `core/signs.json`, `techniques/*.json`; the full catalogue: [combat/techniques.md](combat/techniques.md). Code: `HandSign`, `Weaver`, `SignBook`, `Mastery`, `Chakra`, `Cooldowns`.*

**Hand signs.** Twelve signs. Hold **Weave** (R) and enter signs **typed** (keys 1 to 0, - and =) or on the
**radial** wheel (Rat at the top, clockwise, 30 degrees a sign; mouse or stick, a dead zone in the middle).
Release to cast. Each sign takes 4 ticks (3 from control 80, one less at ninjutsu ranks 5 and 10, never under
2). Improvements on the roadmap's input:

- **Prefix hints**: while you weave, the HUD lists the techniques you know that start with the signs so far.
- **Buffering**: a sign pressed in the last 2 ticks of the one before is kept, so fast typists never drop one.
- **Hold or toggle** Weave, chosen in the settings.
- **Auto-sign** (accessibility): pick a known technique from the quick wheel and the signs play themselves at 6 ticks a sign, no fizzles.
- **Mastery shortening without ambiguity**: a mastered technique casts with half its signs, a perfected one with one (E to C: none, from a quick slot), but the sign book lengthens a short form until no other technique you know could be meant.

A wrong sequence fizzles (a quarter of the cost lost). Melee hits, staggers and knockdowns interrupt a weave
(half the cost lost); a thrown or jutsu hit interrupts only if it deals 15% of your health. On Story only
staggers, knockdowns and hits over 10% interrupt the player.

**Mastery.** Uses raise a technique from novice through practiced and mastered to perfected (C rank: 15, 50,
130 uses; a real fight counts 2, a training use or a home drill 1). Practiced costs x0.95, mastered x0.9 with
half the signs and a quick slot (Z, X, C, V), perfected x0.8 and +10% power.

**Rank defaults** (each technique may override): E level 1, D 5, C 10, B 18, A 30, S 42; chakra 5, 10, 16,
30, 50, 80; base power 0, 5, 10, 14, 21, 32; cooldown 2, 3, 6, 10, 18, 40 s.

**The catalogue** (95 techniques, every one with nature, rank, level, signs, chakra, cast, cooldown, its
mechanic in Minecraft terms, counters, who teaches it and its slice): [combat/techniques.md](combat/techniques.md).

| Family | Techniques (E to S) |
|---|---|
| Neutral (14) | Clone, Transformation, Substitution, Release, Rope Escape, Field First Aid, Hiding in Camouflage, Body Flicker, Shadow Clone, Multi Shadow Clone, Clone Great Explosion, Spiralling Sphere, Great Spiralling Sphere, Chakra Threads |
| Fire (10) | Ember Shot, Great Fireball (the ceremony's), Phoenix Sage Fire, Dragon Flame, Fire Dragon Bullet, Flame Wall, Ash Pile Burning, Great Dragon Fire, Majestic Destroyer Flame, Great Fire Annihilation |
| Wind (9) | Gale Palm, Great Breakthrough (the ceremony's), Vacuum Wave, Blade of Wind, Vacuum Bullets, Pressure Damage, Sickle Weasel, Vacuum Great Sphere, Spiralling Shuriken |
| Lightning (8) | Spark Needle, Stunning Palm (the ceremony's), False Darkness, Lightning Hound, Thunder Cage, Lightning Blade, Lightning Armour, Kirin |
| Earth (9) | Headhunter, Mud Wall (the ceremony's), Mud River, Rock Skin, Stone Spears, Earth Dragon Bullet, Flowing Rampart, Light-Weight Rock, Earth Splitting |
| Water (10) | Water Bullet, Wild Water Wave (the ceremony's), Water Wall, Hiding Mist, Water Prison, Water Clone, Water Dragon, Great Waterfall, Shark Bomb, Thousand Feeding Sharks |
| Genjutsu (8) | False Surroundings, Hell Viewing, Sly Mind Affect, Mist Servant, Bringer of Darkness, Mirror Reversal, Temple of Nirvana, Sea of Ink |
| Medical (5) | Mystical Palm, Chakra Scalpel, Poison Extraction, Resuscitation, Strength of a Hundred |
| Sensing (3) | Chakra Sensing, Wide Sensing, Chakra Reading |
| Fuinjutsu (6) | Binding Tag, Four-Tag Barrier, Storage Scroll Barrage, Chakra Suppression, Five Elements Seal, Marked Teleport |
| Weapon techniques (13) | see [Weapons](#5-weapons) |

Techniques never change the map: fire never sets blocks alight, walls and barriers are short-lived entities,
fissures and craters are effects. Summoning (and with it tailed beasts) is out of scope.

**Medical ninjutsu.** Anyone with control 50 who trains with the medic (Beta 3): Mystical Palm heals by
control (a shared experience with the healed squadmate); Resuscitation revives a downed squadmate at once.
Squadmates are knocked out, never killed.

**Sensing.** Chakra Sensing shows living things through walls within 16 blocks (48 with Wide Sensing) and
reveals hidden and disguised ones; it beats smoke, mist and clones. Enemy sensors are why stealth needs
Tobari's curtain, mist or distance.

**Fuinjutsu.** Sealing tags capture a downed, stunned or bound enemy (a mission objective), make barriers,
seal chakra and natures, store weapons and mark teleports.

**Chakra movement** (Beta 2; client-side, the server checks and charges chakra): the ninja run (+15%), roof
and tree hopping (Beta 1 at night), the chakra jump (up to 3x, no fall damage while chakra lasts), tree
walking, wall-running (3 s, longer with control), water-walking (a mixin on `canStandOnFluid`; a stagger dunks
you), silent step, then air step (Chunin) and wind glide (Jonin). Control lowers their costs.

**Natures.** The first at the Genin ceremony (its C-rank signature), the second at Chunin (a nature master's
three trials), the third at Jonin; more through bonds by resonance ([Kindling Bond](#9-kindling-bond)). Your
natures' jutsu cost x0.75; other natures' jutsu cannot be learned.

## 7. Clans

*Data: `clans/<clan>.json`; every technique: [combat/clans.md](combat/clans.md).*

All 25 clans, each with passives, a suggested nature, four tiers of techniques (tier 1 at Genin, level 10;
tier 2 Chunin, 20; tier 3 Jonin, 32; tier 4 the road to Hokage, 44), kekkei genkai stages where they have one,
and a **lesser technique** a friend can learn. **The player is clanless**, so clan tiers and kekkei genkai are
the kits of clan residents, teammates, rivals, sparring partners and enemies; the player's clan route is each
clan's lesser technique at clan friendship 7, the clan's weapon after its welcome, and the styles clans teach.
Joining a clan later (by marriage or invitation) teaches its signature technique (tier 1), never a
bloodline. The clan files keep the full tiers so clan-born play can return without new data.

| Clan | Tier 1 (Genin) | Tier 2 (Chunin) | Tier 3 (Jonin) | Tier 4 (road) | Lesser |
|---|---|---|---|---|---|
| Senju (Wood Release) | Binding Roots | Wooden Barrier | Wood Clone | Deep Forest Bloom | Vitality Breathing |
| Uzumaki (chakra x1.3) | Sealing Chains | Chain Fence | Vitality Seal | Adamantine Chain Cage | Seal Basics |
| Uchiha (Sharingan) | Phoenix Flower with hidden shuriken | Dragon Flame Triple | Sharingan Genjutsu | Flame Storm | Fire Breath |
| Hyuga (Byakugan) | Gentle Fist | Palm Rotation | Vacuum Palm Barrage | Sixty-Four Palms Protection | Eight Trigrams Stance |
| Nara | Shadow Possession | Shadow Neck Bind | Shadow Sewing | Shadow Gathering | Shadow Stitch |
| Akimichi | Expansion | Partial Expansion | Super Expansion | Calorie Control: Butterfly | Hearty Meal |
| Yamanaka | Mind Body Disturbance | Mind Transfer | Mind Link | Mind Destruction | Flower Sense |
| Inuzuka | Fang over Fang | Dynamic Marking | Tunnelling Fang | Twin-Headed Wolf | Keen Nose |
| Sarutobi | Monkey King Staff Forms | Fire Flow Staff | Clan Ash Pile Burning | Staff of a Thousand Lengths | Will of Fire |
| Aburame | Insect Swarm | Insect Clone | Insect Sphere | Hive Storm | Bug Sense |
| Hatake | Ninken Tracker | White Fang Arts | Tracking Fang | Lightning Cutter | Silent Tracking |
| Kurama | Painted Illusion | Painted Beasts | Living Canvas | Final Brushstroke | Ink Mind |
| Shimura | Vacuum Blades | Vacuum Volley | Sealing Curse (ANBU) | Great Vacuum | Cold Discipline |
| Yuhi | Tree Binding | Thorn Garden | Rose Reversal | Tree Binding Death | Crimson Eye |
| Gekko | Dance of the Crescent Moon | Moon Shadow Step | Full Moon Slash | New Moon Blade | Moonlit Breathing |
| Shiranui | Needle Spit | Pressure Needles | Thousand Needles | Hokage Guard Formation | Needle arts |
| Morino | Stern Presence | Interrogation Hold | Iron Will | Breaking Point | Unshaken |
| Umino | Cover | Rally | Tidewall | A Teacher's Resolve | Steady Voice |
| Haruno | Chakra Precision | Blossom Strength | Petal Shield | Seal of a Hundred Blossoms | Focused Mind |
| Namiashi | Wave Step | Wave-foot Arts | Black Tide | Hokage's Blade | Wave-foot basics |
| Hagane | Mace Arts | Iron Guard Mastery | Steel Bracer Counter | Gate Wall | Iron Guard |
| Kinoshita | Trap Craft | Timber Barricade | Wire Web | Carpenter's Fortress | Wire arts |
| Tsuchigumo | Earth Binding Web | Spider Web Wall | Earth Spider Armour | (the sealed forbidden art) | Web Snare |
| Suzuran (poison-immune) | Lily Blood: Coatings | Lily Poultice | Poison Mist | Bloom of Bells | Herb Lore |
| Tobari | Night Curtain | Lantern Dim | Curtain Veil | Great Curtain | Soft Steps |

The seven minor clans without a bloodline (Shiranui, Morino, Umino, Haruno, Namiashi, Hagane, Kinoshita) have
**family arts**: learned skills, not blood. **Kekkei genkai**: the Byakugan (16, 32, 50 blocks, then chakra
flow), the Sharingan (earlier telegraphs, a doubled parry window and genjutsu breaking, copying a technique
it watches; no further stage unless the story adds one) and Wood Release, by stage with rank. NPC clan power
(the ranks session) shifts an NPC's level only: no extra stat multiplier per clan; the kits carry the flavour.
A player clan's clan art is any C to A technique its founder has mastered, not a kekkei genkai.

## 8. Combination play

*Data: `combos/nature.json`, `combos/squad.json`, `combos/tactics.json`.*

**Nature combos between allies**: a fire jutsu through an ally's wind gust becomes a Firestorm (x1.5 power and
radius); lightning into soaked targets is a Storm Surge (stun, chains 4); fire through mud makes Lava Bullets;
water over Mud River a Mudslide; wind through a wave Gale Rain; lightning through wind, timed to 5 ticks, a
Thunder Gust; fire into an earth wall a Magma Wall.

**Squad combo techniques**: launcher relay (a teammate launches, you air-combo), clone feint, bomb line,
pincer, distract and take (the bell test's lesson), shadow and strike (a Nara possesses, everyone crits),
fang and swarm, cover fire, the triad formation (Nara, Akimichi and Yamanaka), barrier and fire, and the
squad finisher at cohesion 80.

**Commands** (hold H for a wheel): attack my target, defend me, follow, hold, spread, regroup, combo (picks one
you can do), retreat, heal. **Formations**: line, arrowhead, ring, pincer, hidden.

**Cohesion** ([BONDS.md §7](../BONDS.md#7-the-squad)) changes how the squad fights:

| Cohesion | Effect |
|---|---|
| 0 to 29 | commands take 16 ticks; 1 in 10 ignored; combo damage -10% |
| 30 to 59 | commands take 10 ticks |
| 60 to 79 | commands take 4 ticks; combo damage +10%; nature-combo windows 10 ticks longer |
| 80 to 100 | combo damage +20%; the squad finisher; once a fight a teammate takes a hit that would down you |

A teammate at friendship 6 joins nature combos with you without a command; at 8 they call combos themselves.
Every squad combo landed is a shared experience for the bond engine. Teammates are built like the player
(the same pillar scaling, their niche edge from the ranks session's growth model), fight by their squad role
(vanguard, support, sensor, medic), are knocked out and never killed, and never take friendly fire (Hard: area
jutsu deal 25% to allies).

## 9. Kindling Bond

*Data: `core/kindle.json`. Code: `Kindle`, played by the duel simulator.* The owner approved this design. Power
flows outward, through people: it grows with how many people you have truly bonded with and how deep those
bonds go. It is meant to be as strong as the great eye techniques without reading as a copying eye. The bond
engine (Shinobi Life) owns bond levels, tiers and gates; combat reads them through `Kindle.Bonds`, which
Shinobi Life's glue adapts: `tier(who)` = `Kindling.combatTier`, `web()` = Bonfire's strength
(`Kindling.bonfire(w).strength()`), `bonfireOpen()` = `Kindling.bonfire(w).lit()`. An active quarrel drops a
bond exactly one tier (a Spark goes out), a falling-out puts it out, and nothing burns before the story's awakening.

| Tier | Gate (the bond engine's) | Opens |
|---|---|---|
| Spark | friendship 6 | Thread Sight, small kindles |
| Flame | friendship 8 | full Kindle, Ember Link |
| Blaze | friendship 10 or a spouse | Ember Mark, unison techniques |
| Bonfire | a large bond web | the ultimate |

- **Thread Sight** (always on): bonds appear as threads of light. In a fight you read your bonded allies'
  health, chakra and cooldowns along their threads, a telegraphed attack on one flares on its thread 4 ticks
  early (6 at Flame, 8 at Blaze) so you can cover or parry for them, and any bonded ally is a beacon anywhere
  on the map. Strangers and enemies have no thread to you, so it reads them poorly.
- **Kindle** (K while a bonded ally weaves): your chakra goes into their technique and it goes past its
  limits: x1.4 power and x1.2 area at Spark, x1.9 and x1.4 at Flame, x2.4 and x1.6 at Blaze; healing x1.5 to
  x2.5 and revives from Flame; range x1.5 to x4 (a sensor's range covers the village). It costs you 0.6, 0.8 or
  1.0 of their cost, once per ally every 20, 15 or 10 s. You never learn the technique: they do it, bigger.
- **Ember Link** (Flame): you and up to three bonded allies become one flame for 30 s: one shared chakra pool
  (a caster pays their share first), a hit on any of you keeps half on the one struck and splits the rest
  across the others (you feel their pain), and you can look through a linked ally's eyes.
- **Unison techniques** (Blaze): one per pairing, your nature crossed with the ally's niche: Painted <nature>
  with a genjutsu painter, Twin Comet (three fangs with a ninken) with a close fighter, a doubled nature unison
  with a ninjutsu ally, Hearth with a medic, Beacon Sight with a sensor, Ember Rain with a weapon user, a
  Burning Seal with a sealer. 25 chakra each, once a fight a pairing: two A-rank casts in one blow.
- **Ember Mark** (Blaze): an ember left in a deeply bonded ally: travel to their side or summon them to yours
  across any distance; in a fight, once, swap places with them.
- **Bonfire** (the ultimate): draw on every bond at once for 20 s. Its strength is the bond engine's (each
  flame weighted by tier 1, 2 or 4 times its strength, dimmed by quarrels, plus 0.5 for each community
  reached). With m = 1 + 1.5 (1 - e^(-strength / 35)): your damage x m, damage taken x 1 / sqrt(m), chakra
  regen x (1 + strength / 25), allies' power x (1 + (m - 1) / 2). A loner (strength 2 to 4) gets x1.1, a
  candle; 12 x1.44, a campfire; a typical player at 60 hours (19) x1.63, a bonfire; a devoted one (22) x1.70,
  an inferno. Afterwards 60 s of burnout.

**Costs**: while linked you feel your allies' pain; past three kindles in a minute each burns 10% of your
chakra bar and 30 stamina; a quarrel dims that person's tier, a falling-out snuffs it; it is useless with
strangers until you bond with them. **Natures** come through bonds by resonance: fight beside someone often
enough and their trial can teach you their nature; you never copy it. **The look**: an ember mark on the palm
or chest (never an eye), threads of light, ember-gold chakra. **In the beta**: none of it ships; the story
decides when Spark opens.

## 10. Enemies

*Data: `enemies/<id>.json` (one loadout file each), `enemies/_ai.json`, `enemies/_groups.json`, `bosses/<id>.json`;
everything: [combat/bestiary.md](combat/bestiary.md).*

**One brain.** Every human enemy is one shinobi entity drawn with VF's resident model and our wardrobe;
animals are vanilla-based entities with our brain. A loadout file gives tier, rank, levels, preferred band,
style, weapons, techniques, tools, armour, traits and AI overrides.

| Tier | Health | Damage | Poise | Thinks between actions |
|---|---|---|---|---|
| mook | x1.0 | x0.75 | 15 | 10 ticks |
| elite | x2.2 | x1.0 | 30 | 6 ticks |
| miniboss | x3.5 | x1.15 | 60 | 5 ticks |
| boss | x7 (per boss file) | x1.15 (beta bosses x0.7 to x1.0) | 100+ | 4 ticks |

**Range bands** (ROADMAP): close (0 to 3 blocks: taijutsu, grabs, guard), mid (3 to 10: throws, D and C jutsu,
dashes) and far (10 to 24: big jutsu, bows, traps, sensing, retreating to heal). A fighter that prefers a
farther band backs off at 60% of its speed and only on half its decisions, so a closer catches it. Groups
coordinate bands: a cell is always one close, one far.

**Tells and telegraphs.** Every enemy attack has a wind-up pose and a sound (light 4 ticks, throw 6, heavy 10,
grab 12, a signature 20; jutsu show their signs), scaled by difficulty; unblockables flash red on Story and
Shinobi. Dodge chances by rank (Genin 20%, Chunin 35%, Jonin 50%) grow with how readable the attack is: slow,
telegraphed attacks are dodged more; a jutsu's signs say one is coming, only its travel lets you dodge it.

**Reactions to the player's habits** (scaled by difficulty): the same jutsu three times in 30 s is dodged 15%
more each time; a player who never guards meets feints and fast chains; one who always guards meets guard
breaks, grabs, bombs and wind; dodging the same side gets led; staying far brings body flickers and smoke;
staying close brings substitutions and knockback; turtling in cover brings bombs over it; low chakra brings
pressure; a parry streak brings unblockables. The sensei comments on habits in barks.

**Attack tokens.** At most 1 (Story), 2 (Shinobi) or 3 (Hard) enemies attack the player at once; the rest
throw, circle, reposition or fight your teammates. Bosses always hold a token. **Flinch**: a landed hit
cancels a mook's or elite's wind-up; bosses flinch only when their poise breaks.

**The bestiary.** Sparring partners (classmates, Genin, Chunin, each clan's); bandits (thug, knife-fighter,
archer, brute, ronin, chief); village trouble (street toughs, pickpockets, a cat burglar); smugglers, rogue
genin, rogue bombers and illusionists, rogue chunin; enemy scouts, sensors and cells (a vanguard and a support
who fight in pairs); foreign exam genin (fan, sonic, puppeteer, needles, brawler); later rogue jonin, hunter-nin,
foreign chunin and jonin, samurai (armour that turns ninjutsu), mercenary captains, a bandit warlord, puppet
masters, sealing adepts, sensor leaders, assassins, cell veterans, chakra absorbers (they drink ninjutsu) and
a legendary missing-nin. Animals: wolves, boars, bears, thieving monkeys, hawks, deer (never hostile), and
in the Forest of Death giant centipedes, leeches, snakes (wild animals, not summons), tigers and, later,
spiders.

**Bosses** (phases with adds, openings for every pillar and a signature tell each):

| Boss | Chapter | Shape |
|---|---|---|
| `combat:boss.ch2.rival_spar` | 2 | a spar with `role:rival` (non-lethal, 30%); losing is allowed and remembered |
| `combat:boss.ch8.bell_test` | 8 | `role:sensei`: an objective (take the bells with a teammate), unwinnable alone by design |
| `combat:boss.ch11.bandit_chief` | 11 | mace overheads, smoke and bombs, an archer, then a knife-fighter |
| `combat:boss.ch14.road_ambush` | 14 | an enemy cell holds the road with smoke, makibishi and mines while a runner flees |
| `combat:boss.ch16.forest_team` | 16 | a hunting exam team in the trees (three on three) |
| `combat:boss.ch16.forest_beast` | 16 | a giant snake: tail sweeps, lunges, a swallow you fight out of |
| `combat:boss.ch17.prelim` | 17 | a one-on-one bout against one rolled exam rival (non-lethal, judged) |
| `combat:boss.ch19.finals` | 19 | the finals bout, `role:rival` by default (non-lethal, judged) |
| `combat:boss.ch19.stadium_cell` | 19 | attackers in the stands: defend and protect |
| later | Chunin to road | a missing-nin bounty, a mercenary fort, a samurai captain, a puppet theatre; eight story bosses by neutral id (`chunin.story_1` ... `road.final`), defined in the story bible |

**Sparring and exam fights.** Sparring never kills: it ends at 30% health or a yield (hold Y), with no level
loss; residents are knocked out, never killed (VF Knockouts). Ranked residents spar from friendship 3 (BONDS
`spar_won`, `spar_lost`). Exam bouts are stopped by the proctor at 10%. Combat emits **judging** metrics for
Progression's promotion judging: damage dealt and taken, time, parries, perfect dodges, distinct techniques,
pillars used, combos and the longest, interrupts, squad combos, allies and civilians protected, smart counters,
yields.

## 11. Difficulty and feel

*Data: `core/difficulty.json`, `core/feel.json`.*

| Setting | Story (default) | Shinobi | Hard |
|---|---|---|---|
| Parry and perfect-dodge windows | 6 and 8 ticks | 4 and 6 | 3 and 5 |
| Enemy telegraphs | x1.5, with a flash | x1.0 | x0.75 |
| Enemy damage and health | 60%, 90% | 100% | 130%, 115% |
| Enemy dodging | x0.7 | x1.0 | x1.25 |
| Attack tokens | 1 | 2 | 3 |
| Habit adaptation | half | full | x1.5 |
| Light hits interrupt your weave | no | yes | yes |
| Aim assist | 5 degrees | 2 | 0 |
| Death | one level | one level | two levels |
| Cinematic camera | on | on | off |

Every number lives in data (overridable per world) and the setting can change at any time. Toggles: auto-sign,
hold or toggle for guard and weave, camera shake, hit-stop, flash effects, subtitled tells, auto lock-on,
slowed combat.

**Feel.** Hit-stop freezes both fighters' animation (light 1 tick, heavy and launcher 3, finisher 5, parry 4,
boss phase 8); the server freezes only the target's AI, so it is safe over a network. Camera shake from heavy
0.15 to boss slams 0.6. I-frames: dodge 6 (+4 perfect), substitution 12, the whole finisher cinematic, get-up
10 (+2 on Story). The first frame of a strike plays on the client the tick you press (client-predicted); the
server confirms with a sweep (60 degrees, 3 blocks) and 2 ticks of lag compensation. Lock-on on the middle
mouse button (24 blocks); attacks curve 15 degrees toward the target in front. Targets: a mook in 4 to 8 s, an
elite in 10 to 20, a boss in 60 to 150; the player survives 6 to 10 mook hits; 60 fps with 12 fighters and 20
projectiles. Cinematics (skippable, off on Hard) on finishers, A and S jutsu, squad combos and boss phases.

**Accessibility.** Auto-sign, hold versus tap for guard and weave, a radial wheel for controllers, subtitled
tells, flash and shake toggles, slowed combat, and Story's generous windows.

**PvP (later multiplayer).** Duels by invitation to 30% health and 3v3 arena battles; levels and ranks
normalised (default level 30); Shinobi timings, no aim assist, no habit adaptation; diminishing returns on
every control group; genjutsu on a player at most 3 s of screen effect, never the camera; Mind Transfer cannot
target players; substitution every 25 s; Palm Rotation and barriers on 10 s cooldowns; S-rank off by default;
no PvP in the village outside arenas.

## 12. Progression

*Data: `progression/timeline.json`.* When each technique, style and weapon arrives across the 60-hour story:
from mentors (the instructor, the sensei, the medic, nature masters, clan elders, the Strong Fist master, a
weapon master, a sensor master, a genjutsu master, a fuinjutsu master), the scroll shop, mission rewards,
friendly clans and the Hokage's archive.

| Stretch | Levels | Pillar cap | Arrives |
|---|---|---|---|
| Academy (Beta 1, 0 to 4 h) | 1 to 5 | 5 | Academy taijutsu (block, dodge), practice kunai and shuriken, smoke bombs and wire; the chakra bar and signs; Clone, Transformation, Substitution, Release, Rope Escape, First Aid; roof hopping |
| Genin (Beta 2, 4 to 12 h) | 5 to 15 | 10 | parry and counter, launcher and air combos, palm rush; Strong Fist and Iron Guard; kunai, shuriken, senbon, tanto, bombs, tags, the pouch, coatings, clan weapons and clan-taught styles; chakra movement; Body Flicker, Hiding in Camouflage; the nature ceremony's C-rank and the scroll shop's D-ranks; genjutsu basics, Binding Tag; lesser clan techniques |
| Chunin Exams (Beta 3, 12 to 15 h) | 15 to 18 | 12 | the exam reward (one C-rank chosen by the sensei); Leaf Great Whirlwind; bokken, ninjato, katana and Crescent Moon; the weighted chain; Mystical Palm, Chakra Sensing, Four-Tag Barrier, Hiding Mist, Mist Servant, blade flows |
| Chunin (15 to 28 h) | 18 to 30 | 18 | B-rank; the second nature; Shadow Clone; gates 1 and 2, Primary Lotus; Swaying Willow, Blossom Strength (Haruno); windmill shuriken, kusarigama and the fans; storage scrolls; Kindling Bond's Spark when the story opens it |
| Jonin (28 to 45 h) | 30 to 42 | 24 | A-rank (Lightning Blade, Spiralling Sphere, Multi Shadow Clone); the third nature; gates 3 and 4; Lightning Body, White Fang; Resuscitation, Five Elements Seal; Flame and Blaze |
| ANBU (optional) | from 35 | — | stealth, ANBU armour, assassin tools |
| Road to Hokage (45 to 60 h) | 42 to 50 | 28 | S-rank from the archive; gates 5 and 6, Morning Peacock; Great Spiralling Sphere, Spiralling Shuriken, Strength of a Hundred; Bonfire |
| Post-game | 50 to 60 | 30 | gate 7, Iaido, every pillar to 10 |

## 13. The beta loadout

*Data: `progression/beta_loadout.json`.* Smaller than the full game, deep enough that fights feel great by the
Chunin Exams.

- **Taijutsu**: Academy taijutsu in full (14 moves), Strong Fist tiers 1 and 2, Iron Guard tier 1; block,
  parry, counter, dodge and perfect dodge, substitution, poise and stagger, momentum and finishers, the
  launcher and air combos. (Gentle Fist, Iron Body and Beast Fang appear as NPC kits.)
- **Weapons**: practice kunai and shuriken, kunai, shuriken, manji, senbon, tanto, bokken, ninjato, katana,
  kokuto, the Sarutobi staff, bo staff, weighted chain, iron mace, fist wraps and steel tekko; paper, smoke,
  flash and stink bombs, wire, makibishi, sealing and barrier tags, both pouches, pills, salves and the three
  coatings; ten weapon styles; throws with retrieval and tethers, the pouch, coatings, blade flows, bomb mines.
- **Ninjutsu**: 32 catalogue techniques (Academy 5, Body Flicker, Hiding in Camouflage, the five ceremony
  C-ranks, the five D-ranks, the second C-ranks of the exam reward, genjutsu basics, Mystical Palm, Chakra
  Sensing, Binding Tag, the weapon techniques up to C) and 25 lesser clan techniques; typed and radial signs
  with prefix hints and auto-sign, mastery to perfected, the nature triangle, genjutsu and Release, chakra
  movement, sensing, sealing tags, nature combos with teammates.
- **Per player**: about 10 to 14 techniques by the end of the beta, two or three styles, five to eight weapons
  and tools in regular use.
- **Enemies**: 26 human and 10 animal types and 9 bosses reachable in the beta.
- **Not in the beta**: B-rank and above, the gates, Shadow Clone, the second nature, NPC clan tiers 2 to 4,
  Swaying Willow, Blossom Strength, Lightning Body, White Fang, the windmill shuriken, kusarigama and fans,
  medical and sensing above C, Kindling Bond.

## 14. The combat core

The pure-Java module `combat:core` (package `dev.shinobi.combat`, Minecraft-free, deterministic): Phase 0's
Combat mod depends on it (`implementation project(':combat:core')`) and adds the world glue.

| Class | What |
|---|---|
| `Nature` | the triangle, affinity multipliers, clashes |
| `DamageType`, `Damage`, `Scaling` | damage types, the hit formula, armour, guard, toughness, level and pillar scaling, hearts, chakra |
| `Chakra`, `Pool`, `Cooldowns` | the chakra bar (regen, control, own nature, mastery, desperate casts, exhaustion); stamina and poise bars; cooldowns on a tick clock |
| `HandSign`, `Weaver`, `SignBook`, `Mastery` | signs, typed keys and the radial wheel, weaving with buffering and interrupts, mastery-shortened sequences kept unambiguous, the prefix hint |
| `Move`, `Style`, `ComboMachine` | combo trees laid over Academy taijutsu; the combo state machine with windows, buffering, tier, momentum and gate gating |
| `StatusEffects` | durations, stacks, damage over time, cleansing, stacks that turn into other statuses, diminishing returns (bosses separately) |
| `RangeBands`, `Difficulty` | the brain's bands; difficulty modes |
| `Kindle` | Kindling Bond: tiers, kindle boosts and costs, overuse, Ember Link, Bonfire, Thread Sight warnings |
| `CombatData`, `Json` | loads data/combat/ into typed records |

Tests: 48 (nature and damage, resources, signs and mastery, combos and statuses, data integrity, Kindle, and
the balance guards below). The **duel simulator** (test sources, `sim/`) plays fights tick by tick on a line:
the brain keeps its band and picks the best of its combo strings, throws and techniques by expected damage
over time; attacks are telegraphed and the target may dodge, parry, block or substitute; strings run on the
`ComboMachine`'s timings; weaving takes its signs' ticks and can be interrupted; poise breaks stagger;
momentum, gates, buffs, statuses, flinch, attack tokens, clones as decoys, Kindling Bond, teammates' niche
edges and a ninken pup, and boss phases with adds all apply. It is a balance model, not the game: positions
are one-dimensional and every fighter uses the same simple brain.

## 15. Balance

From `./gradlew :combat:core:simulate` (seed 20261029, 200 fights a cell, average player skill: dodge 35%,
parry 15%, block 30% of readable attacks). Builds are generated from the catalogue at each level
(`data/combat/sim/builds.json`): a specialist puts about 55% of the pillar cap into its pillar, a balanced
build spreads it.

**Time to kill, Shinobi**: win rate and mean seconds against a level-matched rogue genin (mook) and rogue
chunin (elite).

| Level | taijutsu mook | elite | weapons mook | elite | ninjutsu mook | elite | balanced mook | elite |
|---|---|---|---|---|---|---|---|---|
| 5 | 90% 8.4s | 23% 12.3s | 89% 7.2s | 4% 14.6s | 12% 5.8s | 0% | 93% 7.4s | 1% 15.4s |
| 10 | 100% 7.0s | 72% 10.5s | 100% 4.1s | 49% 10.2s | 96% 7.5s | 26% 13.8s | 100% 5.7s | 52% 13.5s |
| 15 | 100% 6.6s | 85% 10.5s | 100% 3.9s | 95% 6.9s | 99% 6.9s | 70% 11.3s | 100% 5.8s | 50% 12.6s |
| 18 | 99% 7.3s | 64% 10.6s | 100% 5.3s | 94% 8.9s | 100% 4.3s | 78% 12.0s | 100% 5.5s | 82% 12.1s |
| 25 | 100% 7.6s | 90% 12.3s | 100% 4.7s | 100% 9.4s | 100% 4.2s | 99% 11.5s | 100% 2.8s | 61% 11.3s |
| 30 | 100% 7.6s | 80% 11.2s | 100% 3.1s | 99% 8.4s | 100% 2.9s | 95% 11.0s | 100% 2.6s | 95% 3.3s |
| 40 | 100% 6.9s | 92% 10.2s | 100% 1.5s | 100% 8.7s | 100% 2.5s | 100% 5.6s | 100% 2.5s | 96% 5.0s |
| 50 | 98% 6.5s | 68% 9.4s | 100% 2.9s | 100% 8.0s | 100% 1.7s | 94% 12.0s | 100% 2.3s | 82% 11.0s |
| 60 | 100% 6.4s | 75% 9.8s | 100% 2.8s | 100% 8.4s | 100% 1.7s | 92% 13.5s | 100% 2.1s | 86% 11.1s |

On Story every build wins 100% against both from level 10 on (elites in 7 to 14 s). At level 5 an Academy
student is not meant to beat a Chunin; a pure-ninjutsu Academy build has no damaging jutsu yet.

**By technique rank**, at the level each opens (ninjutsu specialist): damage a cast D 6.9, C 12.7, B 27.3, A
67.5, S 124.1; damage a chakra point 0.89, 0.84, 0.91, 1.35, 1.55; a full bar holds 9.6, 5.3, 3.5, 2.8 and 2.2
casts. Higher ranks are more efficient but a bar holds few of them.

**Builds play their pillar**: against the elite, the taijutsu build deals 59 to 69% of its damage with
taijutsu, the weapons build 85 to 99% with weapons, the ninjutsu build 61 to 79% with ninjutsu, the balanced
build splits.

**Build against build** (row's win rate, both average skill, Shinobi rules): at level 30 it is a
rock-paper-scissors cycle (taijutsu beats weapons 87%, weapons beats ninjutsu 78%, ninjutsu beats taijutsu
68%); at level 18 ninjutsu leads (77 to 83%); late the balanced build, a superset once the cap lets everyone
round out, wins most pairings. PvP is a later system; this is a guard, not a target.

**The beta's bosses** (win rate, mean seconds, player health left; novice in brackets):

| Boss | Squad | Story: taijutsu / weapons / ninjutsu / balanced | Shinobi: taijutsu / weapons / ninjutsu / balanced |
|---|---|---|---|
| ch2.rival_spar | alone | 100% (100%) / 100% / 100% / 100% | 89% (84%) / 64% (59%) / 70% (71%) / 77% (77%) |
| ch11.bandit_chief | +2 | 100% / 100% / 100% / 100% | 71% (70%) / 97% (95%) / 84% (74%) / 87% (79%) |
| ch14.road_ambush | +2 | 100% / 100% / 100% / 100% | 98% / 98% / 97% / 97% |
| ch16.forest_beast | +2 | 100% / 100% / 100% / 100% | 100% / 100% / 100% / 100% |
| ch16.forest_team | +2 | 100% / 100% / 100% / 100% | 80% (70%) / 97% (95%) / 61% (50%) / 69% (66%) |
| ch17.prelim | alone | 100% / 100% / 100% / 100% | 77% (74%) / 87% (86%) / 78% (72%) / 72% (61%) |
| ch19.finals | alone | 100% / 97% / 98% / 99% | 80% (74%) / 48% (34%) / 73% (63%) / 52% (38%) |
| ch19.stadium_cell | +2 | 90% (82%) / 98% / 91% (78%) / 97% | 42% (22%) / 52% (39%) / 53% (39%) / 38% (33%) |

Story is forgiving (90 to 100% at average skill, 78 to 100% for novices); Shinobi is a challenge, not a wall
(38 to 100%). Boss fights run 7 to 20 s of simulated time. The bell test is a scripted objective, not
simulated.

**Teammates' contribution** (the ranks session's typical player with its tuned offsets; target 70 to 110% of
the player's damage and control combined, Shinobi, the squad against two rogue genin and a rogue chunin):

| Chapter | Player level | teammate_a (genjutsu): damage / control / combined | teammate_b (taijutsu, pup): damage / control / combined |
|---|---|---|---|
| Ch 8 | 6 | 68% / 0% / 75% | 211% / 0% / 211% |
| Ch 11 | 11 | 45% / 475% / 55% | 92% / 56% / 91% |
| Ch 14 | 15 | 77% / 120% / 78% | 117% / 152% / 118% |
| Ch 16 | 17 | 76% / 89% / 77% | 120% / 154% / 121% |
| Ch 20 | 18 | 57% / 106% / 58% | 117% / 378% / 123% |
| 28 h | 30 | 76% / 55% / 75% | 71% / 140% / 73% |
| 45 h | 41 | 83% / 173% / 85% | 94% / 244% / 96% |
| 60 h | 50 | 71% / 266% / 74% | 77% / 25% / 76% |

One control-second counts as half a second of the player's damage. teammate_a now sits in the band from Ch 14
on except at Ch 20 (58%) and Ch 11 (55%), where it holds enemies five times as long as the player but deals
under half the damage; teammate_b out-hits a balanced player at Ch 8 (no damaging jutsu before level 8) and
runs a little hot through Beta 3.

**Kindling Bond** (the squad against a bounty boss two levels up and an elite, Shinobi; win rate, seconds,
player health left; Bonfire at the bond engine's strengths):

| Kindling | Level 30 | Level 45 |
|---|---|---|
| none | 95% 10 s 4% | 77% 11 s 4% |
| Spark (kindle) | 98% 9 s 5% | 82% 10 s 4% |
| Flame (kindle, Ember Link) | 93% 7 s 37% | 74% 10 s 36% |
| Blaze (and a unison technique) | 96% 7 s 44% | 86% 10 s 36% |
| Blaze and Bonfire, strength 3 (a loner) | 99% 6 s 49% | 97% 8 s 47% |
| Blaze and Bonfire, strength 12 | 100% 6 s 59% | 99% 5 s 65% |
| Blaze and Bonfire, strength 19 (typical at 60 h) | 100% 5 s 62% | 99% 5 s 65% |
| Blaze and Bonfire, strength 22 (devoted) | 100% 5 s 63% | 99% 5 s 68% |

Kindles give a steady edge; Ember Link moves damage off the player (4% health left to 37%); Bonfire turns a
hard fight into a rout and grows with the bond web.

**Guards** (`BalanceTest`): on Story every build beats every beta boss 80% of the time (novices 60%); on Shinobi
no beta boss is under 25% for any build; every build beats a level-matched elite 90% on Story and 40% on
Shinobi from level 10, in 1 to 25 s; no pillar averages under 20% against the other two in PvP at levels 18,
30 and 50; the simulator is deterministic.

**Known gaps**: burst builds (weapons, ninjutsu, balanced) clear mooks two to four times faster than taijutsu
from level 25, because one A-rank cast or weapon technique one-shots a mook; taijutsu's elite fights stay the
most even. The Ch 19 stadium fight is the hardest beta fight on Shinobi (38 to 53%).

## 16. Animations

*Data: `animations.json`; the list: [combat/animations.md](combat/animations.md).* 233 clips keyed the way VF
keys its clips (`tools/combat/animations.py`: id to ticks, loop, who, first person, priority, slice, and
`keys` to be authored), compiled later to `assets/narutominecraft/resident_animations/*.json` for residents and
to the player poser's folder for the player.

| Priority | Clips | What |
|---|---|---|
| P0 (the Phase 0 spike and Beta 1) | 62 | stance and walk, the prologue's crouch, slip-out and carry, roof hop, dodges, substitution, block, hit reactions, stagger, knockout, yield, victory, meditation, tired slouch; the twelve signs, transition, fizzle and Release; push-palms; Academy taijutsu; blade slashes and throws; first aid; salute, nod, kids' wave, spar bow; petting and the workbench |
| P1 (Beta 2) | 107 | ninja run, chakra jump, wall-run, tree walk, water stance; parry, perfect dodge, knockdowns, launches and air juggles, binds, genjutsu daze, burning and shock; cast poses for each nature and the clan techniques; launcher, air strings, palm rush; Strong Fist, Gentle Fist, Iron Body, Beast Fang, Iron Guard; staff, mace, wire, wave-foot; tools; squad commands and the bell test |
| P2 (Beta 3) | 28 | kenjutsu, chain and fan arts, Mystical Palm, sensing, barrier tags, revive, sleep; the stadium crowd and the proctor |
| P3 (later) | 36 | gates and lotuses, Swaying Willow, Blossom Strength, Lightning Body, Lightning Blade, Spiralling Sphere, Water Prison, Mind Transfer, air step, glide |

The Phase 0 spike plays `combat.tai.academy.jab` on the player in third and first person.

## 17. What waits for Phase 0

Everything in Minecraft: the Combat mod itself; the client mixin on the attack key and the server combo
runner around `ComboMachine`; the sweep hit detection (60 degrees, 3 blocks) with hurt-invulnerability
lowered inside chains; dodge, block and parry input; the Weave key with typed and radial input, prefix hints
and auto-sign; the chakra bar, stamina and the HUD; thrown-tool entities, embedding and retrieval; the tool
pouch; technique entities (projectiles, walls, barriers, swarms, clones), status visuals and the genjutsu
client illusions; chakra movement (the `canStandOnFluid` mixin, wall-runs, the chakra jump); the shinobi enemy
entity and its brain on top of `RangeBands` and the loadout files; sparring and knockouts through VF; the
player poser and the clips; hit-stop, shake and cinematics; loading `data/combat/` from the datapack into
`CombatData`'s records; registering conditions (`combat:knows`, `knows_technique`, `nature`) and actions
(`teach_technique`, `combat:teach`, `kindle`) in Core; Core's stat modifiers for fatigue; the region's arenas.

## 18. Ids for other systems

All ids are `combat:` namespaced (`combat:fire.great_fireball`, `combat:style.strong_fist`,
`combat:enemy.bandit_chief`, `combat:group.bandits_small`, `combat:boss.ch11.bandit_chief`,
`combat:knack.weapons`, `combat:squad.launcher_relay`).

- **Items**: weapon and tool stats are keyed by the items registry's ids (`item:kunai`, `item:practice_kunai`,
  `item:sarutobi_staff`...); drops use `drop:<enemy id without the prefix>`.
- **Missions**: `spawn_group` takes enemy and group ids; mission bands by rank (`enemies/_groups.json`); hooks
  `combat:defeated`, `combat:surrendered`, `combat:captured`, `combat:perform`, `combat:no_damage_taken` and
  `combat:spotted`.
- **Character creation**: `combat:knack.*`, the clanless start, the affinity rule.
- **Dialogue**: barks `dlg:combat.<event>.<speaker>`, `dlg:combat.sensei_tip.<habit>`,
  `dlg:combat.boss.<boss id>.phase_<n>` (`data/combat/barks.json`).
- **Bonds**: `Kindle.Bonds`; squad cohesion and friendship read from Shinobi Life.
- **Ranks**: NPC fields level, rank, tier, clan, kit, niche and niche edge; stats derive from level. A kit
  `combat:ally.<role>` is built by rule from those fields (`data/combat/allies/_kits.json`: niche to focus,
  clan tiers by level, nature, style), with named kits for the Classic squad.

## 19. Open questions

- **Clan-born play.** The player is clanless for now; the clan files keep all four tiers so it can return. If
  it does, which tier does a clan-born player start at, and does the clanless +10 stamina and +5 control stay?
- **Mentor roles.** The catalogue names mentors the cast does not have yet: `role:strong_fist_master`,
  `role:willow_master`, `role:weapon_master`, `role:sensor_master`, `role:genjutsu_master`,
  `role:fuinjutsu_master`, `role:samurai_master`, `role:nature_master.<nature>`, `role:clan_elder.<clan>`.
  Should they be cast roles, or residents bound by the map?
- **Burst late game.** Should A and S rank one-shot mooks (fast and showy), or should mook health grow faster
  so taijutsu's steady pace keeps up?
- **Kindling Bond in the beta**: none of it ships. Should Spark appear in Beta 3 as a teaser, or wait for the story?
- **Teammate shares**: Painted Beasts now opens at level 15 for the Kurama (an exception to tier 2 at 20) and
  the ninken grows with its owner; teammate_a is still under target at Ch 11 and Ch 20, and teammate_b over at
  Ch 8 and Beta 3. More kit or offset tuning?
- **PvP** is untuned beyond the guard; it waits for multiplayer.
