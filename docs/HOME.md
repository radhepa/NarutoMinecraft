# Home

Your apartment, and the homes after it. A small, bare flat the Hokage gives an orphan (you always
start clanless, with no family), which slowly fills with your life: a futon you upgrade, a ramen
corner, chests of things you picked up, keepsakes and curios from everything you did, the
squad photo on the wall, a plant you keep alive, a pet asleep at the foot of the bed, and friends
who drop by, comment on the mess and notice that you kept their gift. It should feel like coming
home, not like managing a house.

**No spoilers here.** Story beats that happen at your door or in your home are owned by the story
and referenced only by hook id ([The story at home](#14-the-story-at-home)).

The engine is the pure Java module `life/home` (no Minecraft; JDK 25 like `life/bonds`):
`./gradlew :life:home:test`, and `./gradlew :life:home:simulate` for the pacing tables. It reads
and writes friendships only through the bond engine ([BONDS.md](../BONDS.md),
[LIFE_TOGETHER.md](../LIFE_TOGETHER.md)).

## Contents

1. [Design rules](#1-design-rules)
2. [The flat](#2-the-flat)
3. [A day at home](#3-a-day-at-home)
4. [Comfort, style and sets](#4-comfort-style-and-sets)
5. [Tidiness](#5-tidiness)
6. [Rest](#6-rest)
7. [Keepsakes, curios, photos and chests](#7-keepsakes-curios-photos-and-chests)
8. [The plant and the pet](#8-the-plant-and-the-pet)
9. [Visitors and spare keys](#9-visitors-and-spare-keys)
10. [The training corner](#10-the-training-corner)
11. [Money](#11-money)
12. [Growing up: homes by era](#12-growing-up-homes-by-era)
13. [Multiplayer](#13-multiplayer)
14. [The story at home](#14-the-story-at-home)
15. [Furniture](#15-furniture)
16. [Keepsakes](#16-keepsakes)
17. [What the map needs](#17-what-the-map-needs)
18. [The engine](#18-the-engine)
19. [Pacing](#19-pacing)
20. [By beta slice](#20-by-beta-slice)
21. [Open questions](#21-open-questions)

## 1. Design rules

1. **Small and lived-in.** The Academy flat is one room. It starts nearly empty and is full by the
   end of the beta; a bigger home is something you grow into.
2. **Never a chore.** Mess, stale food and a thirsty plant are jokes and nudges, never penalties.
   Nothing at home can hurt you, cost you a friend, or be lost.
3. **Everything says something about you.** What you buy, what you keep and what you hang are seen
   by the people who visit, and they react to it.
4. **Small bonuses, capped.** A comfy home rests you a little better, a training corner fills a
   quiet evening; neither replaces going out into the village.
5. **The bond engine owns friendship.** The home asks it who is close and who is free, and tells it
   what a visit did. It keeps no numbers of its own about people.

## 2. The flat

Your home is a VF house: the House Plaque's flood fill gives its bounds (`home/HouseBounds`), and
furnish mode works only inside them (ROADMAP.md §7, "Your apartment and furniture"). **Classic**
saves always get the same flat; **Varied** saves roll one of the Academy candidates from the save
seed (`Flat.starting`, stream `home`). The Konoha build session builds them and lists them in
`homes.json`.

### The Classic flat: `flat.leaf_block.3a`

Third floor of the Leaf apartment block. Inside it is 9 blocks wide and 7 deep, ceilings 3 high,
plus a 4 × 2 balcony. One block per character; north is up, toward the Hokage Rock.

```
                 +--------+
                 |balcony |   4 x 2, railing, faces the Hokage Rock
                 |  4 x 2 |
     +---W--W--W-+--[D]---+-------------+
     |                    |  bathroom   |   W = window (the Rock)
     |                    |   3 x 3     |   [D] = balcony door
     |     main room      | tub mirror  |
     |       6 x 6        |   sink      |
     |                    +-------------+
     |  futon, low table, |kitchenette  |
     |  cupboard          |   3 x 4     |
     |                    | stove sink  |
     +-------+------------+ counter     |
     |genkan | nook 4 x 1 |             |
     | 2 x 1 |            |             |
     +--[D]--+------------+-------------+
       mailbox (outside the door)
```

| Room | Floor (blocks) | Fixed | What goes there |
|---|---|---|---|
| Main room | 6 × 6 | window wall facing the Rock | Bed, tables, seating, chests, shelves, wall pieces, training corner |
| Kitchenette | 3 × 4 | stove (heat for the Hearth pot), sink | Cupboard, icebox, cooking pot, prep table, kettle |
| Bathroom | 3 × 3 | bathtub, mirror (outfits), sink | Bath mat, towel rack |
| Genkan (entry) | 2 × 1 | the door, the mailbox outside | Shoe rack, umbrella stand |
| Closet nook | 4 × 1 | — | The wardrobe cabinet (outfits), chests and barrels |
| Balcony | 4 × 2 | railing | Planters, wind chime, bench, laundry line |

You move in with a **futon, a low table, a cupboard, a storage chest, the wardrobe cabinet and a
cooking pot** (the item registry's `kit:start`, with the apartment key). The flat has **22 floor
cells** for furniture (a futon takes 2, a cushion 1, rugs, tatami and wall
pieces none), room for **one bed**, and **3 spare keys**. It holds at most **60 comfort**.

### Varied candidates

| Id | Shape | View | Balcony |
|---|---|---|---|
| `flat.leaf_block.3a` | The Classic flat | Hokage Rock | 4 × 2 |
| `flat.leaf_block.2c` | A corner flat: main room 7 × 5, smaller bathroom | Hokage Rock | 3 × 2 |
| `flat.riverside_row.1b` | Ground floor; a 4 × 3 yard instead of a balcony | The river | yard |
| `flat.market_loft.4` | An attic over a shop: main room 7 × 6, low 2-block ceiling, a skylight | Rooftops | none (balcony pieces cannot be placed) |

Every candidate has the same fixtures, 21 to 23 cells and 3 keys, so no roll is better than another.

## 3. A day at home

| When | At home |
|---|---|
| 6:00 | Wake in your own bed. The alarm clock (if you bought one) rings comically. Well Rested from the night (section 6) |
| Morning | **Mirror or wardrobe cabinet:** change outfits. **Mailbox:** the stipend envelope (every morning), notes from friends who came by while you were out, invitations slipped under the door, clan summons, neighbours' notes, gifts |
| Breakfast | **Eat from the cupboard** or cook at the Hearth & Harvest pot. Food keeps a few days and then goes stale: a stale meal gives one Well Fed tier less and a funny line (`home.pantry.stale.milk`), a very stale one no Well Fed and a funnier line. Never sickness. An icebox keeps perishables twice as long |
| Before leaving | Water the plant, feed the pet, pick up a dish or two |
| Evening | Friends may drop by (section 9); cook for friends; short practice (section 10); **write in the journal at the desk** (the quest log opens on today's page) |
| Night | **Sleep** in your own bed to clear fatigue; before midnight for Well Rested |

How long food keeps (`Pantry.KEEPS`): onigiri, dango, bento 2 days; home-cooked dishes 3; milk 4;
bread and fruit 5; vegetables 6; most else 7; dried fish 30; rice 60; green tea 90; instant ramen
120; soldier pills a year. Very stale is three times that.

## 4. Comfort, style and sets

Every piece has **comfort** (what rest reads) and **style** (what visitors notice):

```
comfort = pieces, diminishing within a category (1, 0.5, 0.25... so six cushions are not six times one)
          + set bonuses + a cared-for plant (1 to 3) + a pet living here (2)
          (a kotatsu counts double in winter), at most the home's cap,
          less 10% (at most 5) while the place is messy
style   = each different piece's style once + 1 per keepsake and photo on show + half the set bonuses
```

| Tier | Comfort from | Feels like |
|---|---|---|
| Bare | 0 | The day you moved in (a futon, a table and a cupboard: 8) |
| Cosy | 10 | A few things of your own |
| Comfortable | 20 | The Leaf set complete |
| Homely | 38 | A lived-in Genin's flat |
| Beloved | 55 | The very top of a small flat (the Academy flat holds 60) |

**Sets.** Two pieces of a set add 1 comfort, four add 3, the whole set 5 and turns on its perk.
Visitors whose personality loves a set enjoy a home that shows two or more of its pieces.

| Set | Pieces | Perk (whole set) | Loved by |
|---|---|---|---|
| **Leaf** (`leaf`) | futon, low table, floor cushion, tatami mat, paper lamp, scroll shelf, folding screen, Leaf banner | *Home Sweet Home*: Well Rested lasts an hour longer | warmhearted, steadfast, gentle |
| **Ramen corner** (`ramen`) | ramen cup tower, noren curtain, ramen poster, bowl shelf, Ichiraku stool | *Ramen at Home*: instant ramen at home counts as a Leaf dish (a little chakra back) | fiery, playful, warmhearted, adventurous |
| **Balcony** (`balcony`) | balcony planter, wind chime, balcony bench, laundry line, bonsai | *Morning Air*: plants grow a quarter faster; visitors enjoy the view | gentle, imaginative, shy, reserved |
| **Training corner** (`training`) | training dummy, meditation mat, weight rack, weapon rack, target board | *Dojo*: home practice counts up to an hour and a half a day | proud, stern, fiery, protective, meticulous |
| **Tea corner** (`tea`) | tea set, tea table, zabuton pair, hanging scroll, ikebana vase | *Tea Time*: green tea at home holds fatigue off half an hour more | thoughtful, stern, gentle, meticulous, pragmatic |
| **Festival** (`festival`) | lantern string, festival mask, goldfish bowl, fan display, festival drum | *Festive*: hangouts at home go a little better | playful, curious, imaginative, warmhearted |
| **Clan colours** (`clan.<id>`, 25) | a banner, a folding screen and a lantern in the clan's colours | *Clan Colours*: members of that clan enjoy it; your own clan's set adds comfort | members of the clan |

You start with two Leaf pieces, so the first set is already under way.

## 5. Tidiness

Living makes a little mess: a meal's dishes (+1), an empty ramen cup (+1, and the cups stack up
visibly, up to six), cooking (+2), guests (+1 each). Mess stops at 12.

| State | Mess | What happens |
|---|---|---|
| Tidy | 0 to 3 | Fussy visitors approve |
| Lived-in | 4 to 7 | Nothing, except the ramen cups being remarked on |
| Messy | 8 to 12 | Comfort 10% lower (at most 5); visitors comment: easygoing friends do not mind, fussy ones tease you |

**Cleaning** is one action at the sink (a few seconds) and puts everything away. A tidy key holder
who visits while you are away may tidy up for you, and leaves a note. Mess never costs friendship.

## 6. Rest

Your own bed always clears fatigue (ROADMAP.md §7, "The daily cycle"). Going to bed before midnight
gives **Well Rested**, and a comfier home makes it a little better:

| Tier | Chakra regen | Until | Also |
|---|---|---|---|
| Bare | +10% | 12:00 | The roadmap's Well Rested, unchanged |
| Cosy | +10% | 13:00 | |
| Comfortable | +12% | 13:00 | |
| Homely | +15% | 14:00 | |
| Beloved | +15% | 15:00 | Fatigue starts an hour later that night |

The complete Leaf set adds an hour. A late night (to bed between midnight and 2:00) still gives a
light Well Rested (+5% until 11:00) in a Homely or Beloved home. Other beds (hospital, bedroll) clear
fatigue without the bonus, as the roadmap says.

## 7. Keepsakes, curios, photos and chests

**Keepsakes** are things kept for what they mean: every filler finale and clan welcome gives one
(SIDE_QUESTS.md §2.6), some side quests, bond quests and missions do, story moments may, and **any
gift a friend gives you can be kept and shown**. **Curios** are the other half: useless but
charming loot with a line of flavour text (a cracked mask, an old coin, a broken kunai with a name
scratched in), from missions, bandit camps, exploring, festivals and side quests (the item
registry's `curio_*` items and loot tables). All of them are ordinary items: keep them in chests,
sell them at the pawn shop, or show them.

Showing things is plain Minecraft and furniture: up to **six** stand on their own (the sill, the
table, the tops of things), and display furniture holds more: a display shelf 6, a display case 4,
a curio cabinet 12, a wall mount 1, a weapon rack 4. Each thing on show adds 1 style; three or more
curios on show get remarked on (`home.visit.curios`).

When a friend visits and sees **their gift on show**, they notice it, once (`home.visit.kept_gift`):
the bond engine's `Gifts.seenDisplayed`, which the giver remembers (`saw_gift_displayed`). Gifts
come from the bond engine's record of what you were given (`Gifts.received`: who, what, when, the
occasion).

### Chests and storage

Storage is **plain Minecraft chests and barrels** (27 slots each), nothing custom: no sorting,
search or filing screens, no item decay, no weight, nothing that punishes keeping lots of things.
You start with one chest; every chest, barrel or tansu you buy adds 27 slots, and they take one
floor cell each (a step tansu two), so the Academy flat comfortably holds four to six and a bigger
home many more. A typical player has 54 slots by the end of the beta and could fit several times
that.

**Photos** are taken at milestones and hang in photo frames (1 each). A photo's people are roles,
so it shows whoever the save bound to them. After a time skip a milestone can be retaken: the
newest version hangs, the older ones go in the album. Someone in a photo remarks on it the first
time they see each version.

| Photo | Slice | Taken |
|---|---|---|
| `photo.class` | Beta 1 | Ch 2: the whole Academy class |
| `photo.graduation` | Beta 1 | Ch 7: graduation day |
| `photo.squad` | Beta 2 | Ch 8: the new squad with its sensei |
| `photo.first_c_rank` | Beta 2 | Ch 11: the squad on the road |
| `photo.leaf_festival` | Beta 2 | The Leaf Festival, with whoever came along |
| `photo.chunin_exams` | Beta 3 | Ch 20: the evening after the results, at Ichiraku |
| `photo.squad.teen`, `photo.squad.adult` | later | The squad retaken after each time skip |
| `photo.jonin`, `photo.wedding`, `photo.family`, `photo.hokage` | later | Later milestones |

The story session may add its own under `photo.story.<hook>`.

## 8. The plant and the pet

**The houseplant** (or a bonsai) grows from a sprout to grand over about two seasons if you water
it every few days: faster in spring, slower in winter, a quarter faster with the balcony set.
Forgotten for three days it droops, after ten it wilts; it never dies, and one watering perks it
up. From its fourth stage it flowers in spring and summer, and visitors notice. A healthy plant
adds 1 to 3 comfort.

**Your pet** (ROADMAP.md §7, "Pets") lives here once it has a pet bed: it sleeps there or at the
foot of your bed, waits at home during missions it cannot join, and adds 2 comfort. The pet bowl
is where you feed it; VF's pet code does the rest. Visitors greet it.

## 9. Visitors and spare keys

Who comes to your door is decided once a day from the save seed and the bond engine
(`Visits.daily`):

| Visit | Who and when |
|---|---|
| **Drop-in** | A friend at bond level 3 or more, at most one a day, each no more than once in five days: about 1.5% a day plus 1% per level above 3, more for warm and open people and for key holders, in a free evening hour |
| **Crashing after a mission** | The day the squad comes back from a mission, each teammate at level 3 or more comes over with a 20% chance (together if both), at most every four days |
| **The sensei checks on you** | From Genin, at level 2 or more, about once a week ("Are you eating properly?"). In the Academy years the instructor does, about every ten days |
| **Neighbours knock** | About once in ten days: a cup of sugar, a parcel taken in, the noise upstairs, thanks, gossip. The authored neighbour quests (SIDE_QUESTS.md, "The Neighbours") come on top |
| **Home hangouts** | You invite friends over (section 9.1) |
| **Clan summons** | A clan messenger knocks in the morning or leaves a letter (SIDE_QUESTS.md §2.3); raised by the clan quests, not by this scheduler |

**When you are out** they leave a note in the mailbox. A **key holder** who finds you out waits
inside if you are back within two hours. When you have been away all day (a mission on the road),
a warm-hearted key holder may leave food in the cupboard, and a tidy one may tidy up.

**When you are in**, the visit plays out: the visitor reacts to the place, at most three remarks,
from these pools (each may have per-personality variants, `.<archetype>`):

| Key | When |
|---|---|
| `home.visit.kept_gift` | Their gift is on show (once per gift) |
| `home.visit.photo.<milestone>` | They are in a photo on the wall (once per version) |
| `home.visit.mess.dont_mind` / `.fussy` / `home.visit.mess` | The place is messy (easygoing, fussy, everyone else) |
| `home.visit.ramen_cups` | Three or more ramen cups on show |
| `home.visit.curios` | Three or more curios on show |
| `home.visit.tidy` | A fussy visitor, a tidy flat |
| `home.visit.decor.<set>` / `.clan` | Two or more pieces of a set they love, or clan-coloured pieces of their clan's (you are clanless, so these are a friend's gift or a choice of colours) |
| `home.visit.plant.flowering`, `home.visit.pet` | The plant is in flower; the pet is home |
| `home.visit.comfort.<tier>` | Always: what they think of the place |
| `home.note.<kind>` | Notes left in the mailbox (`drop_in`, `sensei_check`, `left_food`, `tidied`, `neighbour.<why>`...) |

How much they enjoyed it (0 to 1) goes to the bond engine: any visit is contact and warmth; a good
one (0.4+) is the `hung_out` shared experience; a very good one (0.65+) a little more warmth. A mess
lowers how much they enjoyed it, never the bond.

### 9.1 Home hangouts

Proposed to the bond engine as activities at `home` (hosted by you), so asking, tastes, highlights
and rituals work as they do at Ichiraku. `home_dinner` is already in its catalog; the others count
as a plain shared experience until it carries them.

| Hangout | Hours | From level | Up to | Act | Loved by | Slice |
|---|---|---|---|---|---|---|
| `study_night` | 18–23 | 2 | 4 | studying | thoughtful, meticulous, curious, shy | Beta 1 |
| `cook_together` | 17–22 | 3 | 4 | a meal | warmhearted, playful, gentle | Beta 1 |
| `balcony_stargazing` | 20–24 | 4 | 3 | hanging out | curious, imaginative, shy, thoughtful | Beta 1 |
| `home_dinner` (exists) | 18–21 | 5 | 6 | a meal | warmhearted, protective, steadfast | Beta 1 |
| `squad_crash` | 18–23 | 3 | 3 | hanging out | fiery, adventurous, playful | Beta 2 |
| `tea_at_home` | 13–20 | 4 | 3 | hanging out | thoughtful, stern, gentle, pragmatic | Beta 2 |

Hosting adds a little mess (one per guest, one more for a meal).

### 9.2 Spare keys

At **bond level 6** (Close Friend) you can give someone a spare key: a moment between you in the bond
engine (`home.spare_key`). The Academy flat has three keys. Key holders drop by a little more often,
wait inside for you, and may leave food or tidy while you are away. You can take a key back
quietly; nobody is told.

## 10. The training corner

Short practice at home: the **training dummy** (taijutsu forms), **hand-sign drills** (no piece
needed), **meditation** on the mat (chakra control), and **study** at the scroll shelf or desk. It
counts at **40% of a training ground's rate**, and at most **one in-game hour a day** counts (an
hour and a half with the whole training set). One hand-sign drill a day counts toward mastering a
jutsu. It fills a quiet evening; real training stays at the training grounds.

## 11. Money

- **The orphan's stipend:** 30 ryo every morning in the mailbox, **for the whole game** (it does
  not stop at Genin). The item registry owns the number (`economy.json`); day 1's welcome purse
  includes the first one.
- **No rent, ever.** Every home is yours without rent (the user's decision). The Jonin house is
  still bought (about 30,000 ryo); moving is free.
- **Furniture** is 10 to 1,200 ryo a piece and sells back at half price (starter and fixed pieces
  are not sold). The Leaf set's six pieces to buy cost 280 ryo, about an in-game week of Academy
  savings, as the roadmap asks of the first proper set.
- **The pawn shop** buys curios and loot as before. Selling the last one of something is your
  choice; nothing warns or keeps a record beyond the item itself.
- A typical player spends about 1,200 ryo on the home over the beta, almost all of it before the
  festival; after that the flat is full and money goes to gear and scrolls.

## 12. Growing up: homes by era

| Era | Home | Holds | Beds | Keys | How you get it |
|---|---|---|---|---|---|
| Academy and Genin (beta) | **The Academy flat** (one room, kitchenette, bathroom, balcony; 22 cells) | 60 comfort | 1 | 3 | The Hokage's gift (Ch 1) |
| Chunin | **A two-room flat with a balcony** (`flat.leaf_block.5b`: main room, bedroom, kitchen, bathroom, a bigger balcony; 34 cells) | 80 | 2 | 4 | Given with the promotion (no rent) |
| Jonin | **A small house** (`house.residential.small`: living room, two bedrooms, kitchen, bathroom, a garden; 56 cells) | 95 | 4 | 5 | Buy it, about 30,000 ryo |
| Clan founder | **Your clan's estate** | 110 | 8 | 8 | Found or restore a clan (ROADMAP.md §11, "Player clans") |
| Hokage | **Quarters in the Residence** | 110 | 6 | 6 | The last arc |

- **Moving** is a farewell quest (`home.farewell.<home>`, this design's to author; the first move
  also raises the story's hook `story.home.farewell`):
  a last evening in the old place, the neighbours, handing back the key. Then friends help pack
  everything into moving crates (items that keep their contents) and you set it out again in
  furnish mode. **Everything comes along:** furniture, chests, keepsakes, photos, the plant, the
  pet and your key holders (they get a new key). What does not fit stays in its crate until you
  make room.
- **A partner can move in** (adults, after the wedding; BONDS.md §10): they need a bed of their own
  or a double futon to share, and they may furnish too. Marrying into a clan (or founding one) is
  how a clanless player later gets a clan's colours as their own.
- **Children** (post-game) need a child's futon, and their drawings join the keepsakes.
- **Only the Academy flat is in the beta**; the rest is designed here and built later.

## 13. Multiplayer

One home per player. Each player gets their own flat in the apartment block (Classic gives players
the block's flats in order; Varied rolls each player's from their own stream), with their own
mailbox, keys and furniture. Only the owner (and later a spouse) can furnish or move things.
Another player can be given a spare key like a resident and may then wait inside, use the stations
and sit down, but not furnish. Visits and reactions run per home and per player.

## 14. The story at home

The home exposes places where story beats can happen: **the door**, **the mailbox**, **the window
and balcony**, **the bed**, and **a visitor waiting inside**. Which beats use them, and what
happens, is the story's; this file lists only the hook ids the story session gave (no content).

| Hook | Slice | Place |
|---|---|---|
| `story.home.door_fixed` | Beta 1 | door |
| `story.home.evening_visit` | Beta 1 | visitor |
| `story.home.door_mark` | Beta 1 | door |
| `story.home.dream` | Beta 1 | bed |
| `story.home.night_talk` | Beta 2 | window or balcony |
| `story.home.farewell` | later | the first move |
| 7 more hooks | later | door, mailbox, window, bed, inside, a visitor waiting |

One later hook needs a placeable piece, `pinboard` (a wall piece, given by the story). The story
also has **8 keepsakes** (`Keepsake.story(<hook>)`, one of them shown by the bed) and **3 photos**
of its own (`photo.story.<hook>`); their ids live in the story's files.

## 15. Furniture

**156 pieces**: 6 fixtures, 6 starter pieces, 69 more for the beta and later, and 75 clan pieces.
In the beta: **143** (68 without the clan pieces). Ids follow the item registry where it has the
piece (`storage_chest`, `barrel`, `tansu_chest`, `step_tansu`, `wardrobe_cabinet`,
`display_case`, `display_shelf`, `curio_cabinet`, `wall_mount`, `scroll_shelf`, `weapon_rack`). Ids are bare here; the item registry namespaces
them (`shinobi_life:<id>`) and tags them `shinobi_life:furniture`. Prices are proposals for the
items session's `economy.json`. Comfort / style / floor cells.

### Fixtures and starter pieces (Beta 1)

| Id | What | C / S / cells | Source |
|---|---|---|---|
| `window`, `mailbox`, `mirror`, `sink`, `stove`, `bathtub` | Built into the flat; the mirror changes outfits, the stove heats the Hearth pot, the sink cleans | 0 / 0–1 / 0 | fixed |
| `futon` | The first bed | 4 / 1 / 2 | starter (Leaf set) |
| `low_table` | Meals and the journal | 2 / 1 / 1 | starter (Leaf set) |
| `cupboard` | The pantry | 1 / 0 / 1 | starter |
| `storage_chest` | A vanilla chest, 27 slots (10 ryo for more) | 0 / 0 / 1 | starter |
| `wardrobe_cabinet` | Outfits live here | 0 / 1 / 1 | starter |
| `cooking_pot` | VF Hearth & Harvest pot, on the stove | 1 / 1 / 0 | starter |

### Beta 1

| Id | C / S / cells | Ryo | Set or note |
|---|---|---|---|
| `floor_cushion` | 2 / 1 / 1 | 20 | leaf |
| `tatami_mat` | 3 / 1 / 0 | 30 | leaf |
| `paper_lamp` | 2 / 2 / 1 | 40 | leaf |
| `scroll_shelf` | 1 / 2 / 1 | 60 | leaf; study at home |
| `folding_screen` | 1 / 2 / 1 | 80 | leaf |
| `leaf_banner` | 0 / 3 / 0 | 50 | leaf |
| `ramen_cup_tower` | 0 / 2 / 1 | 15 | ramen |
| `noren_curtain` | 1 / 2 / 0 | 35 | ramen |
| `ramen_poster` | 0 / 2 / 0 | 20 | ramen |
| `bowl_shelf` | 0 / 2 / 1 | 40 | ramen |
| `ichiraku_stool` | 2 / 2 / 1 | — | ramen; reward of `filler.ramen_thief.3` |
| `balcony_planter` | 1 / 2 / 1 | 40 | balcony; a plant |
| `wind_chime` | 1 / 2 / 0 | 20 | balcony |
| `balcony_bench` | 2 / 1 / 1 | 70 | balcony |
| `laundry_line` | 1 / 1 / 0 | 15 | balcony |
| `training_dummy` | 0 / 1 / 1 | 60 | training |
| `meditation_mat` | 1 / 1 / 1 | 30 | training |
| `thick_futon` | 7 / 2 / 2 | 220 | the bed upgrade |
| `desk` | 1 / 1 / 1 | 70 | the journal; study |
| `prep_table` | 1 / 1 / 1 | 90 | VF Hearth prep table |
| `icebox` | 1 / 0 / 1 | 160 | food keeps twice as long |
| `tea_kettle` | 1 / 1 / 0 | 25 | green tea at home |
| `rug` | 2 / 1 / 0 | 40 | |
| `curtains` | 1 / 1 / 0 | 25 | |
| `wall_clock` | 0 / 1 / 0 | 30 | |
| `calendar` | 0 / 1 / 0 | 10 | shows the village's events |
| `alarm_clock` | 0 / 1 / 0 | 15 | rings at 6:00 |
| `shoe_rack` | 0 / 1 / 1 | 20 | genkan |
| `umbrella_stand` | 0 / 1 / 1 | 15 | genkan |
| `bath_mat`, `towel_rack` | 1 / 1 / 0 | 10, 15 | bathroom |
| `houseplant` | 1 / 2 / 1 | 25 | the plant you water |
| `pet_bed`, `pet_bowl` | 1 / 1 / 1, 0 / 0 / 1 | 40, 10 | your pet lives here |
| `barrel` | 0 / 1 / 1 | 15 | a vanilla barrel, 27 slots |
| `workbench` | 0 / 0 / 2 | 150 | the apartment's workbench (ROADMAP.md §7) |
| `display_shelf` | 0 / 1 / 0 | 45 | shows 6 |
| `wall_mount` | 0 / 1 / 0 | 15 | shows 1 |
| `photo_frame` | 0 / 1 / 0 | 15 | hangs 1 photo |

### Beta 2

| Id | C / S / cells | Ryo | Set or note |
|---|---|---|---|
| `bonsai` | 1 / 3 / 1 | 180 | balcony; a plant |
| `weight_rack` | 0 / 1 / 1 | 120 | training |
| `weapon_rack` | 0 / 2 / 0 | 90 | training |
| `target_board` | 0 / 1 / 0 | 50 | training |
| `tea_set` | 1 / 2 / 0 | — | tea; reward of `side.b2.tea_master` |
| `tea_table` | 2 / 2 / 1 | 90 | tea |
| `zabuton_pair` | 3 / 1 / 1 | 50 | tea |
| `hanging_scroll` | 0 / 3 / 0 | 60 | tea |
| `ikebana_vase` | 1 / 2 / 1 | 45 | tea |
| `lantern_string`, `festival_mask`, `fan_display`, `festival_drum` | 1/3/0, 0/2/0, 0/2/0, 0/2/1 | 40, 25, 20, 80 | festival; Leaf Festival stalls |
| `goldfish_bowl` | 1 / 2 / 1 | — | festival; won at goldfish scooping |
| `clay_oven` | 1 / 1 / 1 | 150 | VF Hearth oven |
| `small_forge` | 0 / 0 / 2 | 400 | the apartment's forge (ROADMAP.md §7) |
| `andon_lamp` | 2 / 2 / 1 | 70 | |
| `kotatsu` | 6 / 2 / 2 | 450 | counts double in winter |
| `display_case` | 0 / 2 / 1 | 250 | shows 4 |
| `curio_cabinet` | 0 / 2 / 1 | 200 | shows 12 |
| `tansu_chest`, `step_tansu` | 1 / 3 / 1, 1 / 3 / 2 | 180, 320 | chests, 27 slots each |
| `clan_banner.<clan>`, `clan_screen.<clan>`, `clan_lantern.<clan>` | 0/3/0, 1/2/1, 2/2/1 | 60, 120, 70 | for the 8 wave-1 clans, sold in their quarters |

**Beta 2.5:** the same three clan pieces for the other 17 clans. **Beta 3:** `bedroll` (1 / 0 / 1,
40 ryo), for camping; it is not your bed and gives no Well Rested.

### Later (designed now)

`wooden_bed` (9 / 3 / 3, 600), `double_futon` (8 / 2 / 3, 500; two sleep in it), `child_futon`
(4 / 1 / 1, 150), `pinboard` (the story's), `irori_hearth` (5 / 3 / 4, 1,200; a sunken
hearth for the house), `engawa_bench` (3 / 2 / 2, 250), `garden_lantern` (1 / 3 / 1, 200).

## 16. Keepsakes

**39 keepsakes** here (14 from quests and events, 25 from the clan welcomes), plus any gift you
keep, the story's 8, the item registry's mission keepsakes, and **52 curios** (`curio_*`, from its
loot tables). The quest that gives each is its id; its name and look are the items and quest
sessions'. Info cards (`info_card`) and clan crests (`clan_crest`) are items too, kept in chests or
shown like anything else.

| Keepsake | From | Slice |
|---|---|---|
| `shogi_board` | `side.b1.shogi` | Beta 1 |
| `cat_figurine` | `district.b1.neighbours.3` | Beta 1 |
| `framed_ladle` | `filler.ramen_thief.3` | Beta 1 |
| `village_painting` (a gift from *teammate_a*) | `bond.b1.classmate_a` | Beta 1 |
| `race_ribbon` | `side.b2.rooftop_race` | Beta 2 |
| `price_war_token` | `district.b2.price_war.4` | Beta 2 |
| `ferry_lantern` | `district.b2.ferryman.3` | Beta 2 |
| `post_splinter` | `district.b2.unbeatable_post` | Beta 2 |
| `lake_lantern` | `filler.lake_lanterns.4` | Beta 2 |
| `dogs_and_bugs_token` | `filler.dogs_and_bugs.3` | Beta 2 |
| `shrine_charm` | `filler.silent_bell.3` (Varied pool) | Beta 2 |
| `teammate_a_keepsake`, `teammate_b_keepsake` (gifts) | `bond.b2.teammate_a.2`, `bond.b2.teammate_b.2` | Beta 2 |
| `festival_prize` | the Leaf Festival's games | Beta 2 |
| `clan_keepsake.<clan>` (8) | `clan.<clan>.1`, wave 1 | Beta 2 |
| `clan_keepsake.<clan>` (17) | `clan.<clan>.1`, wave 2 | Beta 2.5 |
| `gift:<id>` | any gift from a friend (the bond engine's gift id), kept to show; its giver notices | any |
| `curio_*` | loot: missions, bandit camps, exploring, festivals, side quests | any |
| `story:<hook>` | story moments, by hook id | per the story |

## 17. What the map needs

For the Konoha build session (the apartment block, the flats and `homes.json`):

- **The Leaf apartment block** in the residential district, three or four floors, an outside
  stair, a landing per floor with two or three doors, a mailbox by each door, the landlady's flat
  on the ground floor, and a child's flat upstairs (the neighbour quests use it). Seen from the
  Classic flat's window: the Hokage Rock.
- **Each flat** as section 2 sketches it: a House Plaque inside (so VF's flood fill gives the
  bounds), the fixtures as blocks (window, mailbox, mirror, sink, stove, bathtub), a door to
  the balcony, and open floor everywhere furniture may go. The balcony must be inside the bounds
  (a railing and a roof edge so the flood fill closes it), or listed in `homes.json` as an extra
  area.
- **The four Academy candidates** (section 2) and, for later, the two-room flat (`flat.leaf_block.5b`)
  and a small house (`house.residential.small`).
- **`homes.json`**, one entry per home:
  `{"id", "tier", "plaque": [x,y,z], "door": [x,y,z], "mailbox": [x,y,z], "rooms": [{"id","w","d","h"}], "cells", "keys", "view", "balcony", "spawn": [x,y,z]}`.
  The engine's `Flat` record mirrors it.
- **Anchors** for the glue: the bed spot, the stove (for the pot), the sink (cleaning), the
  mirror, the wardrobe cabinet's spot, the starting chest's spot, the desk spot, the balcony rail (stargazing), and a spot by the door where a
  visitor or a key holder waits.

## 18. The engine

`life/home` (package `dev.shinobi.life.home`), pure Java on the bond engine. Phase 0's Life mod
depends on it and does the Minecraft side: furnish mode, the blocks, the screens, the mailbox's
letters as VF Sealed Letters, visitors walking in on VF routines.

| Class | What it does |
|---|---|
| `Piece`, `FurnitureSet`, `Catalog` | The furniture, sets, keepsakes and starter pieces as data |
| `Flat` | Homes as `homes.json` describes them; the Classic flat and the Varied roll |
| `Home` | One player's home: furniture (cells, the one-bed rule, balconies), chest slots, keepsakes and curios on show, photos and the album, mess, keys, the pet, residents, moving, the stipend |
| `Comfort` | Comfort, style, tiers, set bonuses and perks |
| `Rest` | Well Rested from the night |
| `Pantry`, `Plant`, `Mailbox` | The cupboard and staleness; the houseplant; the mailbox |
| `Visits` | Who comes to the door, notes and waiting inside, reactions, hosting, spare keys |
| `Practice` | Home practice, capped |
| `Friends`, `BondFriends`, `HomeHangout` | The bridge to the bond engine, and the proposed home activities |

**Hooks into the bond engine** (no friendship numbers are duplicated): `BondWorld.effectiveLevel`,
`bonded`, `Schedule.free` and the personality for who visits; `talk`, `together`,
`act(HUNG_OUT)` and `addFriendship` for how a visit went; `Gifts.seenDisplayed` for a gift on show;
`setBondFlag("home.noticed:<what>")` for a photo; `moment("home.spare_key")` for a key; `Together.invite` and `Together.go`
for hosted hangouts in its catalog. Requested from the bonds session: the home hangouts of section
9.1 in `Activity.CATALOG`, and an act of its own for a visit to your home, in place of the plain
`hung_out` used today. The squad-after-a-mission and away-all-day rules read Core's
`MissionEnded` event (`with_squad`, `slept_away`; MISSIONS.md §11).

**Tests** (`./gradlew :life:home:test`, 44): the catalog's shape and counts, the Classic and Varied
flats, comfort and its diminishing returns, caps, mess, seasons, clan sets, keepsakes and photos;
Well Rested by tier and late nights; mess, staleness, the icebox, the plant's growth and wilting;
practice caps; the stipend every morning; chest slots; the one-bed rule, balconies, moving and crates,
a spouse moving in; visits through the real bond engine (strangers do not drop by, determinism by
seed, a gift on show noticed once through `Gifts`, mess never costing friendship, keys at level 6 as a moment, notes,
waiting inside, food left while away, a hosted dinner through `Together`); and the pacing below
across five seeds.

**Waits for Phase 0:** furnish mode and the ghost preview, the blocks and models, the House Plaque
bounds, the mailbox's letters, visitors walking in, the curio loot tables, the save attachment (`shinobi_life:home`,
format 1), reading `homes.json` and `economy.json`, and Core's seed streams (the engine uses
`life/bonds`' `Seeds`, which must give the same numbers).

## 19. Pacing

`./gradlew :life:home:simulate` (seed 20261029): a typical player through the beta, 46 in-game
days of 20 real minutes, with the chapters on ROADMAP.md §8's days (the camp nights, the far
village and five days in the Forest of Death away from home). They go home every night they can,
sleep before midnight most nights, buy furniture with what is left after food, do about two thirds
of the side quests, talk to the squad most days, and clean up when it gets messy about half the
time.

| Slice | Days | Nights home / away | Real minutes awake at home a day | Visitors a week | Met / notes | Well Rested nights |
|---|---|---|---|---|---|---|
| Beta 1 | 12 | 12 / 0 | 4.2 | 0.6 | 1 / 0 | 10 of 12 |
| Beta 2 | 24 | 16 / 8 | 3.6 | 2.9 | 7 / 3 | 16 of 16 |
| Beta 3 | 10 | 5 / 5 | 4.5 | 2.1 | 0 / 2 | 5 of 5 |

- **How often home:** every night except the 13 away chapters (33 of 46), about a fifth of each
  day's 20 minutes awake there (morning and evening).
- **Visitors:** about one every two to three in-game days in Genin life (an hour of play sees one
  or two): sensei check-ins, the squad crashing after a mission, neighbours, hosted evenings, and a
  key holder's food while you are away. Few in the Academy weeks, when nobody is close yet. Across
  five seeds: 1 to 3 a week over the beta.
- **Comfort over time:**

| Day | Comfort | Tier | Style | Pieces | Ryo spent | Keepsakes shown | Photos |
|---|---|---|---|---|---|---|---|
| 0 | 8.5 | Bare | 6.5 | 6 | 0 | 0 | 0 |
| 6 | 23.5 | Comfortable | 21.5 | 15 | 285 | 2 | 1 |
| 9 | 27.5 | Comfortable (Leaf set complete) | 31.5 | 19 | 430 | 3 | 1 |
| 12 (graduation) | 31 | Comfortable | 40 | 25 | 625 | 3 | 2 |
| 18 | 40 | Homely | 51.5 | 31 | 1,010 | 4 | 2 |
| 24 | 41 | Homely | 62 | 36 | 1,120 | 5 | 4 |
| 30 (festival) | 42.5 | Homely, the flat full | 70.5 | 38 | 1,185 | 8 | 4 |
| 45 (results) | 42.5 | Homely | 73.5 | 38 | 1,185 | 11 | 4 |

  The flat is full around the festival; mess dips it by up to 5 now and then; Beloved stays out of
  reach of a small flat in the beta, which is what the Chunin flat is for.
- **Small things:** 7 cleanings and 10 messy evenings in 46 days; 9 stale meals (one every five
  days, a joke, not a diet); the plant flowers by the end of Genin life; one spare key given;
  home practice adds about 1.4 training-ground hours over the beta; 54 chest slots.

`FirstFifteenHoursTest` holds these bounds across seeds.

## 20. By beta slice

| Slice | Home |
|---|---|
| **Beta 1** | The Academy flat (Classic, or rolled in Varied); furnish mode; fixtures and starter pieces; chests and barrels; curios and keepsakes on show; the Leaf, ramen, balcony and first training pieces; mailbox, mirror and wardrobe cabinet, cupboard and staleness, the Hearth pot, the desk and journal; comfort, sets and Well Rested; tidiness; display shelves and the first photos; the houseplant; the pet bed and bowl; drop-ins, the instructor's visits, neighbours, notes; study nights and cooking at home; home practice; the stipend |
| **Beta 2** | The tea, festival and full training sets; the forge, the clay oven, the kotatsu, display cases; clan pieces for the 8 wave-1 clans and their keepsakes; the sensei's check-ins; the squad crashing after missions; spare keys and key holders; tea at home; the squad and festival photos; tansu chests, display cases and curio cabinets |
| **Beta 2.5** | Clan pieces and keepsakes for the other 17 clans |
| **Beta 3** | The bedroll; coming home after the Forest of Death to food a key holder left; the exams photo |
| **Later** | The two-room flat, the house, the clan estate and the Hokage's quarters; moving and the farewell quest; a partner moving in; children; photo retakes after the time skips |

## 21. Open questions

- **Varied flats:** four candidates of equal size. Should a roll ever give a slightly bigger or
  smaller flat, or should they differ only in shape and view?
- **Visitor rhythm:** one visitor every two to three in-game days in Genin life. Right, or should
  friends drop by more?
- **Spare keys at bond level 6:** the right closeness? And should key holders ever let themselves
  in when you are home asleep (a breakfast surprise), or only when you are out?
- **Stale food:** a joke every few days for a player who forgets the cupboard. Funny, or should the
  icebox come with the flat?
