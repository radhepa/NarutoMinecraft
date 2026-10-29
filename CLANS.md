# Clans

A clan is a family of the Hidden Leaf that the living village fills with residents. Each clan has
its own wardrobe pieces (hairstyles, tops, bottoms, headwear) and one data file,
`tools/wardrobe/clans/<id>.json`, which says how its members are assembled. Residents are mixed the
Village Friends way (`wardrobe.clan_resident`, after OutfitFactory): the hairstyle, hair color, eyes,
complexion and marks come from the seed alone; an outfit template is picked, its bottom kept half
the time and otherwise swapped for any compatible bottom the clan wears. So every hairstyle meets
every outfit, and a clan of 10 outfits and 15 hairstyles yields thousands of looks.

## The clan file

```json
{
  "id": "hyuga", "name": "Hyuga",
  "tagline": "One line on the clan's look",
  "standing": "noble", "ability": "Byakugan: near-360 degree sight that sees chakra",
  "palettes":    {"HYUGA_BRANCH": {"name": "Hyuga Branch", "P": "#...", "S": "#...", "A": "#...", "L": "#...", "M": "#...", "K": "#...", "D": "#..."}},
  "hair_colors": {"HYUGA_INDIGO": {"name": "Hyuga Indigo", "ramp": ["#14141f", "#1f2033", "#2c2e4a", "#3f4268", "#5c6191"]}},
  "eye_colors":  {},
  "marks":       {"caged_bird": {"rects": [[0, -7.2, 2.4, 0.3]], "color": "#3d7a3a", "mirror": false}},
  "pool": {
    "hair": ["h401_...", "..."], "hair_colors": ["HYUGA_INDIGO", "ESPRESSO"], "eye_colors": ["BYAKUGAN"],
    "palettes": ["HYUGA_BRANCH"], "headwear": [null, null, "w02_forehead_protector"],
    "bottoms": ["b01_shinobi_trousers"], "complexions": [0, 1],
    "marks": [{"id": "caged_bird", "chance": 0.3}]
  },
  "outfits": [
    {"id": "training_wrap", "name": "Training Wrap", "top": "t401_...", "bottom": "b401_...", "rank": "genin", "palettes": ["HYUGA_BRANCH"]}
  ]
}
```

- `palettes`, `hair_colors`, `eye_colors` and `marks` add entries to the shared tables
  (`palettes.json`, `hair_colors.json`, `eye_colors.json`, `living_eyes.MARKS`). An id may be
  defined only once across the shared tables and every clan: prefix new ids with the clan name.
- `pool` lists what any member may draw. `headwear` may hold `null` (bare head); repeat an entry to
  weight it. `bottoms` are extra bottoms a member may swap onto any compatible top, on top of the
  outfits' own bottoms. Pool entries may name shared pieces (`h03_uchiha_spikes`, `b01_...`).
- `outfits` are the designed top + bottom pairs. `palettes` on an outfit overrides the pool's for
  that outfit (a ceremonial white set, a black mourning set). `rank` is one of academy, genin,
  chunin, jonin, anbu, kage, civilian.
- `standing` is `noble` (the great clans, 1-15) or `minor` (the families that pad out the village,
  16-25). `ability` is one line on the clan's technique or bloodline, or null for an ordinary family.
- Marks are thin planes on the face: `[x, y, width, height]` in face pixels, x from the face centre
  (-4..4), y from the top of the head (-8) to the chin (0), eyes on rows -4..-2. `mirror` repeats
  each rect on the other side of the face; `color` null draws a darker shade of the skin.
- JSON numbers need a leading zero: `0.5`, not `.5`.

## Mix and match

Pieces must be able to mismatch. Build tops and bottoms to the shared tag rules (`tags`,
`requires`, `rejects` in META) so a top from one outfit sits with another outfit's bottom, and give
hairstyles `gender: "unisex"` unless they are truly one-gender. Use `locked_to` (both pieces naming
each other) only for a set that is one garment, like a full kimono or a jumpsuit. A hairstyle must
not hang over the eyes (`wardrobe.py --check` enforces it); a fringe may reach the brows.

## Reference images

Design from real reference art, not memory alone. Before building a hairstyle or outfit, find
images of the characters it is based on (the Naruto Fandom wiki, official anime and manga art
across Part I, Shippuden and Boruto, the clan crest). Download them into a scratch folder outside
the repo (never commit them), look at them, and compare each render side by side with its
reference until the silhouette, hair shape, colors and details read as the character's style.

## Piece ids

Every clan owns a block of ids so clans can be built in parallel without clashing:

| # | Clan | Hair | Tops | Bottoms | Headwear |
|---|------|------|------|---------|----------|
| 1 | Senju | h101-h115 | t101-t110 | b101- | w101- |
| 2 | Uzumaki | h201-h215 | t201-t210 | b201- | w201- |
| 3 | Uchiha | h301-h315 | t301-t310 | b301- | w301- |
| 4 | Hyuga | h401-h415 | t401-t410 | b401- | w401- |
| 5 | Nara | h501-h515 | t501-t510 | b501- | w501- |
| 6 | Akimichi | h601-h615 | t601-t610 | b601- | w601- |
| 7 | Yamanaka | h701-h715 | t701-t710 | b701- | w701- |
| 8 | Inuzuka | h801-h815 | t801-t810 | b801- | w801- |
| 9 | Sarutobi | h901-h915 | t901-t910 | b901- | w901- |
| 10 | Aburame | h1001-h1015 | t1001-t1010 | b1001- | w1001- |
| 11 | Hatake | h1101-h1115 | t1101-t1110 | b1101- | w1101- |
| 12 | Kurama | h1201-h1215 | t1201-t1210 | b1201- | w1201- |
| 13 | Shimura | h1301-h1315 | t1301-t1310 | b1301- | w1301- |
| 14 | Yuhi | h1401-h1415 | t1401-t1410 | b1401- | w1401- |
| 15 | Gekko | h1501-h1515 | t1501-t1510 | b1501- | w1501- |
| 16 | Shiranui (minor) | h1601-h1615 | t1601-t1610 | b1601- | w1601- |
| 17 | Morino (minor) | h1701-h1715 | t1701-t1710 | b1701- | w1701- |
| 18 | Umino (minor) | h1801-h1815 | t1801-t1810 | b1801- | w1801- |
| 19 | Haruno (minor) | h1901-h1915 | t1901-t1910 | b1901- | w1901- |
| 20 | Namiashi (minor) | h2001-h2015 | t2001-t2010 | b2001- | w2001- |
| 21 | Hagane (minor) | h2101-h2115 | t2101-t2110 | b2101- | w2101- |
| 22 | Kinoshita (minor, original) | h2201-h2215 | t2201-t2210 | b2201- | w2201- |
| 23 | Tsuchigumo (minor, ability) | h2301-h2315 | t2301-t2310 | b2301- | w2301- |
| 24 | Suzuran (minor, original, ability) | h2401-h2415 | t2401-t2410 | b2401- | w2401- |
| 25 | Tobari (minor, original, ability) | h2501-h2515 | t2501-t2510 | b2501- | w2501- |

Paint seeds follow the same blocks: a clan's pieces use seeds from `<n>000` to `<n>999`
(Senju 1000-1999, Aburame 10000-10999), so no two pieces share a noise pattern by accident.

## Collections: the general wardrobe

Most of the village belongs to no great clan. Their clothes live in collections,
`tools/wardrobe/collections/<id>.json`, in the clan file's schema plus `"role": "shinobi"` or
`"civilian"` (no `standing`). Collections are not separate looks: clanless residents mix across every
collection of their role at once (`wardrobe.general_resident`), so a top from one collection meets a
bottom from another and a hairstyle from a third. Build every collection piece to mismatch freely;
a matching outfit is the template, never the rule. Civilians wear the civilian collections' clothes
and draw from every shinobi collection's hairstyles as well as their own.

| Collection | Role | Hair | Tops | Bottoms | Headwear | Seeds |
|---|---|---|---|---|---|---|
| core | shinobi | h02-h09 (shared) | t02, t13-t21 | b01-b08 | w02, w09 | (existing) |
| academy_genin | shinobi | hg001-hg010 | tg001-tg020 | bg001-bg020 | wg001-wg004 | 31000-31999 |
| field | shinobi | hg011-hg020 | tg021-tg040 | bg021-bg040 | wg005-wg008 | 32000-32999 |
| kunoichi | shinobi | hg021-hg030 | tg041-tg060 | bg041-bg060 | wg009-wg012 | 33000-33999 |
| specialist | shinobi | hg031-hg040 | tg061-tg080 | bg061-bg080 | wg013-wg016 | 34000-34999 |
| rugged | shinobi | hg041-hg050 | tg081-tg100 | bg081-bg100 | wg017-wg020 | 35000-35999 |
| market | civilian | hc001-hc005 | tc001-tc025 | bc001-bc025 | wc001-wc005 | 36000-36999 |
| household | civilian | hc006-hc010 | tc026-tc050 | bc026-bc050 | wc006-wc010 | 37000-37999 |

## Population

`tools/wardrobe/population.json` sets how often each kind of resident appears, in weights per
thousand: civilians (450), clanless shinobi (280), the ten minor clans (10-17 each) and the noble
clans (2-15 each: an Uchiha or a Hyuga is about one resident in seventy, a Hatake one in five
hundred). `wardrobe.village_resident` draws a group by weight, then a resident from it; civilians and
clanless shinobi take an ordinary family name from `family_names`. A group whose files have not
landed is skipped and the rest renormalise. Every clan needs a weight (`--check` enforces it).

## Commands

From `tools/wardrobe/`:

```
python3 wardrobe.py                 # compile every piece into src/main/resources/assets/narutominecraft/wardrobe/
python3 wardrobe.py --check         # validate pieces, characters and clans
python3 render.py --clan hyuga      # docs/renders/clans/hyuga/: hair_N.png, outfits_N.png, mixes_N.png
python3 render.py --collection field  # the same set for a collection, in docs/renders/collections/field/
python3 render.py --general         # clanless shinobi mixed across every collection: docs/renders/general/
python3 render.py --village         # residents drawn by population weight, plus the share of each group
python3 render.py --hair h401_x h402_y --colors HYUGA_INDIGO --out /tmp/hair.png
python3 render.py t401_x            # not for clan pieces; use --clan, or a character sheet
```

`render.py --clan` draws the hairstyles five to a chart (front and back), every outfit template as
designed, and ten residents mixed at random. Look at all of them before committing: the mixes are
the test that the pieces really mismatch.

## Shared helpers

- `anime.py`: `lock`, `spike`, `bangs`, `sidelocks`, `back_fan`, `ring_shell`, `cel_box`, and for long
  hair `curtain` (a back sheet with a pointed hem), `tie` (a hair tie or a cloth wrap) and `braid`.
- `paint.py`: `scalp`, `fabric`, `strip_fabric`, `solid`, `band`, `hem`.
- `kit.py`: `body`, `sleeves`, `neckline`, `collar`, `belt`, `pouch`, `flaps`, `legs`, `footwear`, `leg_ring`.
- `kit_shinobi.py`: `sandals`, `wraps`, `bandage`, `mesh`, `forehead_protector`, `flak_vest`, `tanto`.
- `glyphs.py`: `stamp` for crests drawn from text rows.

Ponytails rotate forward (positive x, e.g. 14 or 20) so they do not clip into the head. Headwear
that hides the hair needs `inflate` of at least .62 or it z-fights with the hair layer.
