#!/usr/bin/env python3
"""The Konoha kit's custom blocks, authored in Python in the style of Village Friends'
tools/tavern/furniture.py: each block is a function that paints its textures and lays out its model
elements, and the compiler writes the blockstates, block models, item models and textures.

    python3 tools/konoha/blocks.py            # compile into src/main/resources/assets/narutominecraft/
    python3 tools/konoha/blocks.py --check    # also validate against tools/konoha/blocks.json

Only the prototype set lives here so far (KONOHA_BUILD.md, "Prototypes"); the full list, with
variants, slices and complexity, is the catalogue in blocks.json. Java registration waits for
Phase 0: every block below records the properties, light, collision and behaviour it needs.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

from pixels import Tex, shade

ROOT = Path(__file__).resolve().parents[2]
NS = "narutominecraft"
ASSETS = ROOT / "src/main/resources/assets" / NS
CATALOGUE = Path(__file__).with_name("blocks.json")

# Shared tones of the kit (KONOHA_BUILD.md, "Style guide").
HINOKI = "#c9a46c"      # light cypress: shoji frames, new timber
HINOKI_DARK = "#9b7748"
CEDAR = "#6b4a2f"       # dark stained timber
LACQUER = "#2a2422"     # black lacquer and iron
PAPER = "#efe7d2"       # washi
STONE = "#a3a198"       # granite of lanterns and memorials
POLE = "#4a3a2c"        # creosoted pole wood
CERAMIC = "#e9e6dc"
TANK = "#cfd2cc"        # painted steel of the rooftop tanks (check against the art)


# -- model elements ---------------------------------------------------------------------------
FACES = ("north", "south", "east", "west", "up", "down")


def auto_uv(face, f, t):
    """Minecraft's default UVs for an element face, from its position."""
    x1, y1, z1 = f
    x2, y2, z2 = t
    return {"north": [16 - x2, 16 - y2, 16 - x1, 16 - y1], "south": [x1, 16 - y2, x2, 16 - y1],
            "west": [z1, 16 - y2, z2, 16 - y1], "east": [16 - z2, 16 - y2, 16 - z1, 16 - y1],
            "up": [x1, z1, x2, z2], "down": [x1, 16 - z2, x2, 16 - z1]}[face]


def box(f, t, tex, skip=(), uv=None, rotation=None, light=0, shade_=True):
    """One model element. tex is a texture key for every face or {face: key}; uv overrides
    {face: [u1, v1, u2, v2]}; rotation is {"origin", "axis", "angle"} (angle a multiple of 22.5)."""
    faces = {}
    for face in FACES:
        key = tex.get(face) if isinstance(tex, dict) else tex
        if key is None or face in skip:
            continue
        faces[face] = {"uv": [round(v, 3) for v in (uv or {}).get(face, auto_uv(face, f, t))], "texture": "#" + key}
    el = {"from": [round(v, 3) for v in f], "to": [round(v, 3) for v in t], "faces": faces}
    if rotation:
        el["rotation"] = rotation
    if light:
        el["light_emission"] = light
    if not shade_:
        el["shade"] = False
    return el


@dataclass
class Block:
    id: str
    textures: dict[str, Tex]
    models: dict[str, list]                 # model name -> elements
    model_textures: dict[str, dict]         # model name -> {key: texture name}
    states: dict                            # blockstate variants: "prop=value,..." -> {"model", "y", ...}
    item: str                               # the model the item shows
    meta: dict = field(default_factory=dict)  # registration notes for Phase 0


BLOCKS: list[Block] = []


def block(fn):
    BLOCKS.extend(fn())
    return fn


def facing_states(model_for, extra: dict | None = None):
    """Variants for a horizontal 'facing' block whose models face north."""
    out = {}
    for facing, y in (("north", 0), ("east", 90), ("south", 180), ("west", 270)):
        if extra:
            for key, models in extra.items():
                for value, model in models.items():
                    out[f"facing={facing},{key}={value}"] = {"model": model_for(model), **({"y": y} if y else {})}
        else:
            out[f"facing={facing}"] = {"model": model_for(None), **({"y": y} if y else {})}
    return out


def ref(name):
    return f"{NS}:block/konoha/{name}"


# -- 1. shoji screen --------------------------------------------------------------------------
def shoji_paper(frame, seed, upper):
    t = Tex(PAPER).grain(seed, .02)
    for x in (5, 10):
        t.vline(x, frame)
    for y in ((3, 7, 11) if upper else (3, 7)):
        t.hline(y, frame)
    return t


@block
def shoji():
    """Shoji screen: a fixed two-block wall panel of washi on a kumiko lattice, with a kick board.
    The sliding shoji door (catalogue: shoji_door) shares these textures."""
    out = []
    for prefix, frame in (("", HINOKI), ("dark_", CEDAR)):
        frame_line = shade(frame, .8)
        wood = Tex(frame).grain(301, .05, "y")
        board = Tex(shade(frame, .92)).grain(302, .05, "x").hline(0, shade(frame, .7))
        lower = shoji_paper(frame_line, 303, False)
        upper = shoji_paper(frame_line, 304, True)
        stiles = [box((0, 0, 7), (1.5, 16, 9), "wood"), box((14.5, 0, 7), (16, 16, 9), "wood")]
        models = {
            f"{prefix}shoji_screen_lower": stiles + [box((1.5, 0, 7), (14.5, 5, 9), "board"),
                                                     box((1.5, 5, 7.7), (14.5, 16, 8.3), "paper", skip=("up", "down"))],
            f"{prefix}shoji_screen_upper": stiles + [box((1.5, 14.5, 7), (14.5, 16, 9), "wood"),
                                                     box((1.5, 0, 7.7), (14.5, 14.5, 8.3), "paper_upper", skip=("up", "down"))],
        }
        tex = {f"{prefix}shoji_frame": wood, f"{prefix}shoji_board": board, f"{prefix}shoji_paper": lower,
               f"{prefix}shoji_paper_upper": upper}
        keys = {"wood": f"{prefix}shoji_frame", "board": f"{prefix}shoji_board", "paper": f"{prefix}shoji_paper",
                "paper_upper": f"{prefix}shoji_paper_upper", "particle": f"{prefix}shoji_frame"}
        out.append(Block(
            f"{prefix}shoji_screen", tex, models, {m: keys for m in models},
            facing_states(ref, {"half": {"lower": f"{prefix}shoji_screen_lower", "upper": f"{prefix}shoji_screen_upper"}}),
            f"{prefix}shoji_screen_lower",
            {"properties": {"facing": "horizontal", "half": ["lower", "upper"]}, "shape": "pane 2 px, two blocks tall",
             "behaviour": "placed as a pair like a door; no light through (opaque paper reads better than translucency)"}))
    return out


# -- 2. tatami --------------------------------------------------------------------------------
def tatami_top(base, seed):
    t = Tex(base).grain(seed, .03, "x")
    for y in range(0, 16, 2):
        t.hline(y, shade(base, .9), 2, 13)
    heri = "#26332a"
    t.rect(0, 0, 1, 15, heri).rect(14, 0, 15, 15, heri)
    for y in range(1, 16, 4):  # the woven pattern of the cloth border
        t.px(0, y, "#3d5242").px(15, y, "#3d5242")
    return t


@block
def tatami():
    """Tatami mat, 2 px thick: the rush weave runs across the mat and the cloth border (heri) runs
    down its long sides, so two blocks in a row read as one 1 x 2 mat. axis = the long direction."""
    out = []
    for prefix, base in (("", "#a9b56a"), ("aged_", "#c8b36a")):
        top = tatami_top(base, 311)
        side = Tex(shade(base, .85)).grain(312, .04, "y")
        el = [box((0, 0, 0), (16, 2, 16), {"up": "top", "down": "side", "north": "side", "south": "side",
                                             "east": "side", "west": "side"})]
        name = f"{prefix}tatami"
        out.append(Block(name, {f"{name}_top": top, f"{name}_side": side}, {name: el},
                         {name: {"top": f"{name}_top", "side": f"{name}_side", "particle": f"{name}_side"}},
                         {"axis=z": {"model": ref(name)}, "axis=x": {"model": ref(name), "y": 90}}, name,
                         {"properties": {"axis": ["x", "z"]}, "shape": "carpet-like 2 px slab",
                          "behaviour": "flooring; furniture-tagged so a player can lay it in their flat"}))
    return out


# -- 3. paper lantern (chochin) ---------------------------------------------------------------
@block
def paper_lantern():
    """Chochin: a ribbed paper lantern hanging from a cord, lacquered caps top and bottom."""
    out = []
    for prefix, body, band in (("red_", "#c8302a", None), ("white_", "#f0e3c2", "#c8302a")):
        side = Tex(body)
        for y in range(16):
            if y % 2:
                side.hline(y, shade(body, .86))
        side.rect(5, 2, 10, 13, shade(body, 1.08))  # the candle glows through the middle
        if band:
            side.rect(0, 5, 15, 9, band).hline(5, shade(band, .8)).hline(9, shade(band, .8))
        cap = Tex(LACQUER).grain(321, .05)
        top = Tex(body).grain(322, .03)
        body_faces = {"north": "side", "south": "side", "east": "side", "west": "side", "up": "top", "down": "top"}
        els = [box((2.5, 3, 4.5), (13.5, 11.5, 11.5), body_faces, light=12),
               box((4.5, 3, 2.5), (11.5, 11.5, 13.5), body_faces, light=12),
               box((3.5, 3, 3.5), (12.5, 11.5, 12.5), body_faces, light=12)]
        for y0, y1 in ((1.5, 3), (11.5, 13)):  # the paper narrows toward both rims
            els += [box((3.5, y0, 5), (12.5, y1, 11), body_faces, light=12), box((5, y0, 3.5), (11, y1, 12.5), body_faces, light=12)]
        els += [box((5, 0.5, 5), (11, 1.5, 11), "cap"), box((5, 13, 5), (11, 14, 11), "cap"),
                box((7.5, 14, 7.5), (8.5, 16, 8.5), "cap")]
        name = f"{prefix}paper_lantern"
        out.append(Block(name, {f"{name}_side": side, f"{name}_top": top, "lacquer": cap}, {name: els},
                         {name: {"side": f"{name}_side", "top": f"{name}_top", "cap": "lacquer", "particle": f"{name}_side"}},
                         {"": {"model": ref(name)}}, name,
                         {"light": 13, "shape": "lantern-sized box, hangs from the block above or stands",
                          "behaviour": "light source; furniture-tagged"}))
    return out


# -- 4. stone lantern (toro) ------------------------------------------------------------------
@block
def stone_lantern():
    """Toro: a two-block granite lantern, base and post below, the light box and its roof above."""
    out = []
    for prefix, moss in (("", False), ("mossy_", True)):
        stone = Tex(STONE).grain(331, .07)
        top = Tex(shade(STONE, 1.06)).grain(332, .06)
        if moss:
            for t in (stone, top):
                for i, (x, y) in enumerate([(1, 2), (4, 1), (9, 3), (12, 1), (14, 4), (6, 2), (2, 5), (11, 6)]):
                    t.px(x, y, "#5f7a3a" if i % 2 else "#6e8a44")
            for x in range(16):
                top.px(x, (x * 7) % 16, "#62803c")
        window = Tex(STONE).grain(333, .07).rect(4, 3, 11, 12, "#3a3530").rect(5, 4, 10, 11, "#ffd47a")
        window.rect(7, 4, 8, 11, "#f0b85a")
        faces = {"north": "stone", "south": "stone", "east": "stone", "west": "stone", "up": "top", "down": "stone"}
        lower = [box((1, 0, 1), (15, 3, 15), faces), box((3, 3, 3), (13, 4, 13), faces), box((5, 4, 5), (11, 16, 11), faces)]
        upper = [box((2, 0, 2), (14, 2, 14), faces),
                 box((4, 2, 4), (12, 8, 12), {"north": "window", "south": "window", "east": "window", "west": "window",
                                               "up": "top", "down": "stone"}, light=10),
                 box((0.5, 8, 0.5), (15.5, 10, 15.5), faces), box((2, 10, 2), (14, 11.5, 14), faces),
                 box((4.5, 11.5, 4.5), (11.5, 12.5, 11.5), faces), box((6, 12.5, 6), (10, 15, 10), faces),
                 box((7, 15, 7), (9, 16, 9), faces)]
        name = f"{prefix}stone_lantern"
        keys = {"stone": f"{prefix}lantern_stone", "top": f"{prefix}lantern_stone_top", "window": "lantern_window",
                "particle": f"{prefix}lantern_stone"}
        out.append(Block(name, {f"{prefix}lantern_stone": stone, f"{prefix}lantern_stone_top": top, "lantern_window": window},
                         {f"{name}_lower": lower, f"{name}_upper": upper}, {f"{name}_lower": keys, f"{name}_upper": keys},
                         facing_states(ref, {"half": {"lower": f"{name}_lower", "upper": f"{name}_upper"}}), f"{name}_upper",
                         {"properties": {"facing": "horizontal", "half": ["lower", "upper"]}, "light": 12,
                          "behaviour": "two-block placement like a door; light in the upper half"}))
    return out


# -- 5. noren ---------------------------------------------------------------------------------
@block
def noren():
    """Noren: the split shop curtain hung across the top of a doorway, on a rod. Walk-through.
    Printed noren carry a dyed kanji; the back shows it mirrored, as dyed cloth does."""
    out = []
    for name, cloth, mark, glyph in (("indigo_noren", "#2d3f6e", "#e9e4d6", None), ("red_noren", "#b42a26", "#f0e8d6", None),
                                     ("tea_noren", "#2d3f6e", "#e9e4d6", ("茶", 11, 110)),
                                     ("ramen_noren", "#b42a26", "#f5eedf", ("麺", 13, 90))):
        t = Tex(cloth).grain(341, .04, "y")
        t.hline(15, shade(cloth, .75)).hline(14, mark)
        if glyph:
            t.glyph(glyph[0], mark, size=glyph[1], cy=7.5, threshold=glyph[2])
        else:
            t.stamp([".##.", "#..#", "#..#", ".##."], 6, 5, {"#": mark})  # a plain house mark
        rod = Tex(CEDAR).grain(342, .05, "x")
        els = [box((0, 14.5, 7.25), (16, 16, 8.75), "rod")]
        for x0, x1 in ((0, 5.1), (5.45, 10.55), (10.9, 16)):
            els.append(box((x0, 3, 7.8), (x1, 14.5, 8.2), "cloth", skip=("up",)))
        out.append(Block(name, {name: t, "noren_rod": rod}, {name: els},
                         {name: {"cloth": name, "rod": "noren_rod", "particle": name}},
                         facing_states(lambda _: ref(name)), name,
                         {"properties": {"facing": "horizontal"}, "shape": "no collision; selection box only",
                          "behaviour": "decorative; furniture-tagged for shops a player owns later"}))
    return out


# -- 6. rooftop water tank --------------------------------------------------------------------
def tank_body(y0, y1):
    f = {"north": "side", "south": "side", "east": "side", "west": "side", "up": "lid", "down": "lid"}
    return [box((1, y0, 4), (15, y1, 12), f), box((4, y0, 1), (12, y1, 15), f), box((2, y0, 2), (14, y1, 14), f)]


@block
def water_tank():
    """The round water tank on Konoha's flat roofs: legs, a riveted drum and a domed lid. A tank is
    one block wide and one to four tall (part = single, or bottom, middle and top stacked)."""
    side = Tex(TANK).grain(351, .03, "y")
    for x in (2, 7, 12):
        side.vline(x, shade(TANK, .86))
    side.hline(1, shade(TANK, .8)).hline(14, shade(TANK, .8))
    side.rect(9, 2, 9, 9, "#a8836a").px(9, 10, "#b8987f").px(10, 3, "#b08c74")  # a rust streak
    lid = Tex(shade(TANK, .94)).grain(352, .03)
    for x, y in [(5, 3), (10, 3), (3, 6), (12, 6), (3, 9), (12, 9), (5, 12), (10, 12)]:
        lid.px(x, y, shade(TANK, .78))
    steel = Tex("#3c4044").grain(353, .06)
    corners = ((2.5, 2.5), (12, 2.5), (2.5, 12), (12, 12))
    legs = lambda h: [box((x, 0, z), (x + 1.5, h, z + 1.5), "steel") for x, z in corners]
    lid_els = lambda y: [box((3, y, 3), (13, y + 1.5, 13), "lid"), box((5, y + 1.5, 5), (11, y + 2.5, 11), "lid"),
                         box((6.5, y + 2.5, 6.5), (9.5, y + 3, 9.5), "steel"), box((11.5, y - 2, 7.5), (12.5, y + 3.5, 8.5), "steel")]
    models = {
        "water_tank_single": legs(3) + [box((2, 3, 2), (14, 4, 14), "steel")] + tank_body(4, 12) + lid_els(12),
        "water_tank_bottom": legs(5) + [box((2, 5, 2), (14, 6, 14), "steel")] + tank_body(6, 16),
        "water_tank_middle": tank_body(0, 16),
        "water_tank_top": tank_body(0, 9) + lid_els(9),
    }
    keys = {"side": "water_tank_side", "lid": "water_tank_lid", "steel": "tank_steel", "particle": "water_tank_side"}
    return [Block("water_tank", {"water_tank_side": side, "water_tank_lid": lid, "tank_steel": steel}, models,
                  {m: keys for m in models}, {f"part={p}": {"model": ref(f"water_tank_{p}")} for p in ("single", "bottom", "middle", "top")},
                  "water_tank_single",
                  {"properties": {"part": ["single", "bottom", "middle", "top"]},
                   "behaviour": "part updates from the blocks above and below, like a pointed dripstone column"})]


# -- 7. kawara ridge --------------------------------------------------------------------------
@block
def kawara_ridge():
    """The rounded ridge cap that vanilla stairs cannot make: laid along a roof's peak on top of the
    last row of tile stairs or slabs. Colours match the three roof tiles of the kit."""
    out = []
    for prefix, base in (("grey_", "#4d535d"), ("green_", "#4f8f7a"), ("orange_", "#b8653f")):
        side = Tex(base).grain(361, .04)
        for x in (0, 8):
            side.vline(x, shade(base, .82))
        side.hline(15, shade(base, .7))
        side.hline(0, shade(base, 1.15))
        top = Tex(shade(base, 1.06)).grain(362, .04)
        for x in (0, 8):
            top.vline(x, shade(base, .85))
        top.hline(7, shade(base, 1.2)).hline(8, shade(base, 1.2))
        f = {"north": "side", "south": "side", "east": "end", "west": "end", "up": "top", "down": "side"}
        end = Tex(shade(base, .9)).grain(363, .04).rect(6, 9, 9, 15, shade(base, .6))
        els = [box((0, 0, 4), (16, 3, 12), f), box((0, 3, 5), (16, 5, 11), f), box((0, 5, 6.5), (16, 6, 9.5), f)]
        name = f"{prefix}kawara_ridge"
        out.append(Block(name, {f"{name}_side": side, f"{name}_top": top, f"{name}_end": end}, {name: els},
                         {name: {"side": f"{name}_side", "top": f"{name}_top", "end": f"{name}_end", "particle": f"{name}_side"}},
                         {"axis=x": {"model": ref(name)}, "axis=z": {"model": ref(name), "y": 90}}, name,
                         {"properties": {"axis": ["x", "z"]}, "shape": "6 px tall cap"}))
    return out


# -- 8. utility pole and wire -----------------------------------------------------------------
@block
def utility_pole():
    """The wooden utility poles along every Konoha street: a creosoted post, a crossarm with two
    ceramic insulators, and a pole-mounted transformer on some. Wires run between crossarms."""
    wood = Tex(POLE).grain(371, .07, "y")
    for y in (3, 9):
        wood.px(1, y, shade(POLE, .7)).px(2, y, shade(POLE, .7))
    ceramic = Tex(CERAMIC).grain(372, .03).hline(1, "#c9c5b9").hline(4, "#c9c5b9").hline(7, "#c9c5b9")
    can = Tex("#7d8486").grain(373, .04).hline(2, "#5d6466").hline(13, "#5d6466")
    wire = Tex("#1d1d1f")
    post = box((6, 0, 6), (10, 16, 10), "wood")
    top = [box((6, 0, 6), (10, 13, 10), "wood"), box((5.5, 13, 5.5), (10.5, 14, 10.5), "wood"),
           box((0, 10, 7), (16, 12, 9), "wood"), box((1.5, 12, 7.25), (3, 14, 8.75), "ceramic"),
           box((13, 12, 7.25), (14.5, 14, 8.75), "ceramic")]
    transformer = top + [box((7, 2, 10), (9, 4, 11), "wood"), box((5, 1, 11), (11, 9, 15), "can")]
    keys = {"wood": "pole_wood", "ceramic": "insulator", "can": "transformer", "particle": "pole_wood"}
    states = {}
    for axis, y in (("x", 0), ("z", 90)):
        for part in ("pole", "top", "transformer"):
            states[f"axis={axis},part={part}"] = {"model": ref(f"utility_pole_{part}"), **({"y": y} if y else {})}
    pole = Block("utility_pole", {"pole_wood": wood, "insulator": ceramic, "transformer": can},
                 {"utility_pole_pole": [post], "utility_pole_top": top, "utility_pole_transformer": transformer},
                 {m: keys for m in ("utility_pole_pole", "utility_pole_top", "utility_pole_transformer")}, states,
                 "utility_pole_top", {"properties": {"axis": ["x", "z"], "part": ["pole", "top", "transformer"]},
                                      "shape": "4 x 4 post; the crossarm has no collision"})
    wstates = {}
    for axis, y in (("x", 0), ("z", 90)):
        for sag in (0, 1, 2):
            wstates[f"axis={axis},sag={sag}"] = {"model": ref(f"power_wire_{sag}"), **({"y": y} if y else {})}
    # two strands, one through each insulator: a wire running along x meets a pole whose crossarm
    # runs along z (pole axis=z, wire axis=x)
    wires = {f"power_wire_{s}": [box((0, 13.6 - s, z), (16, 14 - s, z + .5), "wire") for z in (2, 13.5)] for s in (0, 1, 2)}
    wire_block = Block("power_wire", {"power_wire": wire}, wires,
                       {m: {"wire": "power_wire", "particle": "power_wire"} for m in wires}, wstates, "power_wire_1",
                       {"properties": {"axis": ["x", "z"], "sag": [0, 1, 2]},
                        "shape": "no collision",
                        "behaviour": "the paste tool strings it between pole tops along a street, axis across the crossarms"})
    return [pole, wire_block]


# -- 9. awning --------------------------------------------------------------------------------
@block
def awning():
    """A shop awning: canvas sloping out from the wall at 22.5 degrees over a scalloped valance.
    Placed on the outside of a wall, above a door or a shop front, one block per metre of front."""
    out = []
    for prefix, a, b in (("red_", "#b8322c", "#efe6d2"), ("green_", "#3f6f45", "#e8e2cc"), ("indigo_", "#2d3f6e", "#2d3f6e")):
        canvas = Tex(a).grain(381, .03, "y")
        if b != a:
            for x in range(16):
                if (x // 4) % 2:
                    canvas.vline(x, b)
        valance = canvas.copy()
        for x in range(16):  # scalloped hem
            if x % 4 in (0, 3):
                valance.px(x, 15, "#000000", 0)
        frame = Tex("#3b3d40").grain(382, .05)
        tilt = {"origin": [8, 13, 16], "axis": "x", "angle": -22.5}  # check the sign in game: the front must drop
        els = [box((0, 13, 1.5), (16, 13.6, 18), "canvas", rotation=tilt),
               box((1, 12.2, 1.5), (2, 13, 16), "frame", rotation=tilt), box((14, 12.2, 1.5), (15, 13, 16), "frame", rotation=tilt),
               box((0, 4, 2.4), (16, 7.6, 2.8), "valance", skip=("up", "down"))]
        name = f"{prefix}awning"
        out.append(Block(name, {f"{name}": canvas, f"{name}_valance": valance, "awning_frame": frame}, {name: els},
                         {name: {"canvas": name, "valance": f"{name}_valance", "frame": "awning_frame", "particle": name}},
                         facing_states(lambda _: ref(name)), name,
                         {"properties": {"facing": "horizontal (the direction it reaches out)"},
                          "shape": "no collision below the canvas; the canvas top is walkable for roof running"}))
    return out


# -- compile ----------------------------------------------------------------------------------
def compile_all():
    written = 0
    tex_names = set()
    for b in BLOCKS:
        for name, tex in b.textures.items():
            if name not in tex_names:
                tex.save(ASSETS / "textures/block/konoha" / f"{name}.png")
                tex_names.add(name)
        for model, elements in b.models.items():
            keys = {k: f"{NS}:block/konoha/{v}" for k, v in b.model_textures[model].items()}
            data = {"parent": "minecraft:block/block", "textures": keys, "elements": elements}
            write_json(ASSETS / "models/block/konoha" / f"{model}.json", data)
            written += 1
        write_json(ASSETS / "blockstates" / f"{b.id}.json", {"variants": b.states})
        write_json(ASSETS / "items" / f"{b.id}.json", {"model": {"type": "minecraft:model", "model": ref(b.item)}})
    return len(BLOCKS), written, len(tex_names)


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")


def check():
    cat = json.loads(CATALOGUE.read_text())
    ids = {v["id"] for b in cat["custom"] for v in b["variants"]}
    errors = [f"{b.id}: authored here but not in blocks.json" for b in BLOCKS if b.id not in ids]
    for b in BLOCKS:
        for model, elements in b.models.items():
            for el in elements:
                for v in el["from"] + el["to"]:
                    if not -16 <= v <= 32:
                        errors.append(f"{model}: element outside the model limits")
                for face in el["faces"].values():
                    if face["texture"][1:] not in b.model_textures[model]:
                        errors.append(f"{model}: unknown texture key {face['texture']}")
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    n, models, textures = compile_all()
    print(f"{n} blocks, {models} models, {textures} textures -> {ASSETS.relative_to(ROOT)}")
    if args.check:
        errors = check()
        for e in errors:
            print("error:", e)
        sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
