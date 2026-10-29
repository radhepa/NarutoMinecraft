# Naruto Minecraft

A Naruto-themed Minecraft mod built on the resident model from Village Friends: the player mesh with its overlay layers, the six skin complexions, the Starlit pixel face and the palette-locked wardrobe of textured 3D pieces. This first stage is only about the look of the characters. It has no Java, entities or gameplay yet.

![The line-up](docs/renders/lineup.png)

## Characters

| Character | Face | Hair | Headwear | Top | Bottom | Palette |
|---|---|---|---|---|---|---|
| Hokage | Shinobi Face (blue eyes) | Kage Spikes (gold) | Kage Hat | Hokage Haori | Shinobi Trousers | Hokage |
| Leaf Ninja | Shinobi Face | Leaf Spikes (chestnut) | Forehead Protector | Konoha Flak Vest | Shinobi Trousers | Konoha Jonin |
| Uchiha | Sharingan Face (glows) | Uchiha Spikes (blue-black) | Forehead Protector | Uchiha High Collar | Uchiha Shorts | Uchiha |

Each character has a sheet in `docs/renders/`, with front, side, back, mid-stride and close-up views.

## How the pieces work

The Village Friends wardrobe engine is kept in `tools/wardrobe/` and extended:

- **Kinds:** besides hair, tops and bottoms there are **faces** (painted on the head, plus optional decal pieces) and **headwear** (hats and headbands over the hair). A headwear module can hide hair pieces by id prefix (`hides_hair`), so the kage hat hides the crown spikes but keeps the bangs.
- **Eye colors:** the `E` key role resolves through `eye_colors.json` (Dark, Sky Blue, Sharingan), the way `H` resolves through hair colors.
- **Decals:** small pieces drawn at 2x, 3x or 6x resolution through the piece `scale`: the 火 panel and back kanji, the swirls, the leaf plate, the Uchiha fan and the Sharingan eyes. A face with `"emissive": true` renders its decals fullbright.
- **Palettes:** every Naruto palette keeps the same meaning per role, so pieces mix: `S` is white cloth and bandages, `A` red, `L` tan leather, `M` steel, `K` dark navy, `D` navy cloth. `P` is the character's main color: flak green for Hokage and Konoha Jonin, dark navy for Uchiha.
- **Characters:** `tools/wardrobe/characters/*.json` dresses each character with one piece of each kind, a palette, hair and eye colors and a complexion.

```text
python tools/wardrobe/wardrobe.py            # compile every piece to src/main/resources/assets/narutominecraft/wardrobe/
python tools/wardrobe/wardrobe.py --check    # validate and confirm the outputs are current
python tools/wardrobe/render.py --all        # render every character sheet and the line-up
python tools/wardrobe/render.py uchiha       # one sheet
```

The tools need Python 3 with Pillow and NumPy. The renders come from an offline renderer that uses the exact Minecraft geometry and box-UV mapping. They are not in-game screenshots. Never hand-edit the compiled PNG and JSON files.
