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
  chunin, jonin, anbu, kage.
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

Paint seeds follow the same blocks: a clan's pieces use seeds from `<n>000` to `<n>999`
(Senju 1000-1999, Aburame 10000-10999), so no two pieces share a noise pattern by accident.

## Commands

From `tools/wardrobe/`:

```
python3 wardrobe.py                 # compile every piece into src/main/resources/assets/narutominecraft/wardrobe/
python3 wardrobe.py --check         # validate pieces, characters and clans
python3 render.py --clan hyuga      # docs/renders/clans/hyuga/: hair_N.png, outfits_N.png, mixes_N.png
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
