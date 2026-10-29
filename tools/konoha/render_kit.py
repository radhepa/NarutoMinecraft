#!/usr/bin/env python3
"""Preview renders of the Konoha kit, into docs/renders/konoha/.

    python3 tools/konoha/render_kit.py --blocks       # blocks.png: every prototype block, assembled
    python3 tools/konoha/render_kit.py --buildings    # one sheet per design program, plus street.png
    python3 tools/konoha/render_kit.py                # both

Run blocks.py first: blocks are drawn from the compiled assets.
"""
from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path

from PIL import ImageDraw

import preview as P


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/renders/konoha"
BLUEPRINTS = Path(__file__).with_name("blueprints")
NS = "narutominecraft:"

# Each kit cell: a title and the blocks that show the piece assembled (x, y, z, state).
KIT = [
    ("Shoji screen", [(0, 0, 0, "shoji_screen[facing=south,half=lower]"), (0, 1, 0, "shoji_screen[facing=south,half=upper]"),
                      (1, 0, 0, "dark_shoji_screen[facing=south,half=lower]"), (1, 1, 0, "dark_shoji_screen[facing=south,half=upper]")]),
    ("Tatami", [(x, 0, z, ("aged_tatami" if x == 2 else "tatami") + f"[axis={'z' if x < 2 else 'x'}]")
                for x in range(3) for z in range(2)]),
    ("Paper lanterns", [(0, 0, 0, "red_paper_lantern"), (1, 0, 0, "white_paper_lantern")]),
    ("Stone lanterns", [(0, 0, 0, "stone_lantern[facing=south,half=lower]"), (0, 1, 0, "stone_lantern[facing=south,half=upper]"),
                        (1, 0, 0, "mossy_stone_lantern[facing=south,half=lower]"), (1, 1, 0, "mossy_stone_lantern[facing=south,half=upper]")]),
    ("Noren", [(x, 0, 0, f"{n}_noren[facing=south]") for x, n in enumerate(("indigo", "red", "tea", "ramen"))]),
    ("Water tanks", [(0, 0, 0, "water_tank[part=bottom]"), (0, 1, 0, "water_tank[part=middle]"), (0, 2, 0, "water_tank[part=top]"),
                     (1, 0, 0, "water_tank[part=single]")]),
    ("Kawara ridge", [(0, 0, z, "minecraft:deepslate_tiles") for z in range(3)]
     + [(0, 1, z, "grey_kawara_ridge[axis=z]") for z in range(3)]
     + [(1, 0, z, "minecraft:waxed_oxidized_cut_copper") for z in range(3)] + [(1, 1, z, "green_kawara_ridge[axis=z]") for z in range(3)]
     + [(2, 0, z, "minecraft:waxed_cut_copper") for z in range(3)] + [(2, 1, z, "orange_kawara_ridge[axis=z]") for z in range(3)]),
    ("Utility pole and wire", [(0, y, 0, "utility_pole[axis=z,part=pole]") for y in range(3)] + [(0, 3, 0, "utility_pole[axis=z,part=top]")]
     + [(x, 3, 0, f"power_wire[axis=x,sag={min(x, 4 - x)}]") for x in (1, 2, 3)]
     + [(4, y, 0, "utility_pole[axis=z,part=pole]") for y in range(3)] + [(4, 3, 0, "utility_pole[axis=z,part=transformer]")]),
    ("Awnings", [(x, y, -1, "minecraft:smooth_sandstone") for x in range(3) for y in range(3)]
     + [(x, 2, 0, f"{c}_awning[facing=south]") for x, c in enumerate(("red", "green", "indigo"))]),
]


def full_state(s: str) -> str:
    return s if ":" in s else NS + s


def blocks_sheet():
    cols, cw, chh = 3, 560, 470
    rows = (len(KIT) + cols - 1) // cols
    W, H = cols * cw, rows * chh + 110
    canvas = P.new_canvas(W, H)
    for i, (title, blocks) in enumerate(KIT):
        sc = P.Scene()
        for x, y, z, s in blocks:
            sc.put((x, y, z), full_state(s))
        lo, hi = sc.bounds()
        span = max(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2])
        scale = min(150, 300 / span) * P.SS
        col, row = i % cols, i // cols
        cx, cy = (col * cw + cw / 2) * P.SS, (110 + row * chh + chh / 2 + 10) * P.SS
        sc.draw(canvas, cx, cy, scale, yaw=-35, pitch=28)
    img = P.save_canvas(canvas, OUT / "blocks.png", "Konoha kit: prototype blocks",
                        "Python-authored models and textures (tools/konoha/blocks.py), drawn from the compiled assets")
    d = ImageDraw.Draw(img)
    for i, (title, _) in enumerate(KIT):
        col, row = i % cols, i // cols
        d.text((col * cw + 24, 110 + row * chh + 8), title, fill=(70, 48, 32), font=P.font(20, True))
    img.save(OUT / "blocks.png")
    for i, (title, blocks) in enumerate(KIT):  # one close-up per piece, for checking details
        sc = P.Scene()
        for x, y, z, s in blocks:
            sc.put((x, y, z), full_state(s))
        lo, hi = sc.bounds()
        span = max(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2])
        c = P.new_canvas(900, 700)
        sc.draw(c, 450 * P.SS, 380 * P.SS, min(260, 520 / span) * P.SS, yaw=-35, pitch=28)
        P.save_canvas(c, OUT / "blocks" / (title.lower().replace(" ", "_") + ".png"), title)
    print("wrote", OUT / "blocks.png")


def load_blueprint(path: Path) -> P.Scene:
    bp = json.loads(path.read_text())
    sc = P.Scene()
    for y, layer in enumerate(bp["layers"]):
        for z, row in enumerate(layer):
            for x, ch in enumerate(row):
                if ch != " " and ch != ".":
                    sc.put((x, y, z), bp["palette"][ch])
    return sc, bp


def building_sheet(name: str):
    sc, bp = load_blueprint(BLUEPRINTS / f"{name}.json")
    lo, hi = sc.bounds()
    span = max(hi[0] - lo[0], hi[1] - lo[1], hi[2] - lo[2])
    W, H = 1800, 900
    canvas = P.new_canvas(W, H)
    scale = 560 / span * P.SS
    sc.draw(canvas, 470 * P.SS, 500 * P.SS, scale, yaw=-35, pitch=26)
    sc.draw(canvas, 1330 * P.SS, 500 * P.SS, scale, yaw=145, pitch=26)
    w, h, d = bp["size"]
    P.save_canvas(canvas, OUT / f"{name}.png", bp["title"],
                  f"{w} x {d} footprint, {h} tall. Front (street side) and back. tools/konoha/buildings/{name}.py")
    if bp.get("cutaway"):
        canvas = P.new_canvas(1800, 900)
        for i, cut in enumerate(bp["cutaway"]):
            sc.draw(canvas, (470 + 860 * i) * P.SS, 520 * P.SS, scale, yaw=-35, pitch=38, cut_y=cut)
        P.save_canvas(canvas, OUT / f"{name}_cutaway.png", bp["title"] + ": cutaway",
                      "Floors cut at " + " and ".join(f"y = {c}" for c in bp["cutaway"]) + "; markers are not drawn")
    print("wrote", OUT / f"{name}.png")


def street():
    """The three designs side by side on a street with poles and wires, as the paste tool would set them."""
    import street as S
    sc = S.scene()
    lo, hi = sc.bounds()
    canvas = P.new_canvas(2000, 1100, top=(214, 229, 240), bottom=(236, 230, 214))
    span = max(hi[0] - lo[0], hi[2] - lo[2])
    sc.draw(canvas, 1000 * P.SS, 560 * P.SS, 1380 / span * P.SS, yaw=-28, pitch=30)
    P.save_canvas(canvas, OUT / "street.png", "A Konoha street",
                  "The home, the tea house and the apartment block pasted on one street, with poles, wires, lanterns and a toro")
    print("wrote", OUT / "street.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--blocks", action="store_true")
    ap.add_argument("--buildings", action="store_true")
    a = ap.parse_args()
    both = not (a.blocks or a.buildings)
    if a.blocks or both:
        blocks_sheet()
    if a.buildings or both:
        for path in sorted(BLUEPRINTS.glob("*.json")):
            building_sheet(path.stem)
        street()


if __name__ == "__main__":
    main()
