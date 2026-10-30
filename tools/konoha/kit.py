"""The Konoha building kit for design programs (tools/konoha/buildings/*.py).

A design program builds a Plan with the helpers below and writes a blueprint. The style guide in
KONOHA_BUILD.md is the source of the palettes here: change a palette here and every design that
uses it changes on its next compile.

Coordinates: x east, y up, z south, as in Minecraft. y = 0 is the plot's ground layer (the paste
tool lays it flush with the street), the street side of a plot is south (+z) before rotation, and
the paste tool rotates a blueprint to face its street.

Blueprint output (`Plan.blueprint`): layers bottom to top, rows north to south, one palette
character per block, plus markers (House Plaque, beds, residents, seats, the door anchor). The
writer is isolated in `Plan.blueprint` so it can emit Village Friends' blueprint format exactly
once that format is checked against tools/village_blueprints/ (see KONOHA_BUILD.md, "Open questions").
"""
from __future__ import annotations

import json
import math
from pathlib import Path

NS = "narutominecraft"
OUT = Path(__file__).with_name("blueprints")

# -- palettes (KONOHA_BUILD.md, style guide) ---------------------------------------------------
WALLS = {
    "cream": {"wall": "smooth_sandstone", "trim": "cut_sandstone", "band": "terracotta", "base": "stone_bricks",
              "post": "stripped_spruce_log[axis=y]"},
    "white": {"wall": "smooth_quartz", "trim": "calcite", "band": "red_terracotta", "base": "stone_bricks",
              "post": "stripped_dark_oak_log[axis=y]"},
    "terracotta": {"wall": "terracotta", "trim": "smooth_sandstone", "band": "brown_terracotta", "base": "stone_bricks",
                   "post": "stripped_dark_oak_log[axis=y]"},
    "plaster_orange": {"wall": "smooth_red_sandstone", "trim": "smooth_sandstone", "band": "red_terracotta",
                       "base": "stone_bricks", "post": "stripped_dark_oak_log[axis=y]"},
}
ROOFS = {
    "grey": {"stairs": "deepslate_tile_stairs", "slab": "deepslate_tile_slab", "full": "deepslate_tiles",
             "ridge": f"{NS}:grey_kawara_ridge"},
    "green": {"stairs": "waxed_oxidized_cut_copper_stairs", "slab": "waxed_oxidized_cut_copper_slab",
              "full": "waxed_oxidized_cut_copper", "ridge": f"{NS}:green_kawara_ridge"},
    "orange": {"stairs": "waxed_cut_copper_stairs", "slab": "waxed_cut_copper_slab", "full": "waxed_cut_copper",
               "ridge": f"{NS}:orange_kawara_ridge"},
    "wood": {"stairs": "dark_oak_stairs", "slab": "dark_oak_slab", "full": "dark_oak_planks",
             "ridge": "stripped_dark_oak_log"},
}

FIRE = ["...#...",  # the fire kanji, seven by seven
        "#..#..#",
        ".#.#.#.",
        "...#...",
        "..#.#..",
        ".#...#.",
        "#.....#"]
FENCES = ("_fence",)
PANES = ("glass_pane", "iron_bars")
CHARS = "#@%&*+=-~^:;!?$ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789<>()[]{}/|\\_,'`\""


def mc(state: str) -> str:
    return state if ":" in state else "minecraft:" + state


def base_name(state: str) -> str:
    return state.split("[")[0]


class Plan:
    def __init__(self, id: str, title: str, size: tuple[int, int, int], kind: str, notes: str = ""):
        self.id, self.title, self.size, self.kind, self.notes = id, title, size, kind, notes
        self.blocks: dict[tuple[int, int, int], str] = {}
        self.markers: list[dict] = []
        self.cutaway: list[int] = []

    # -- primitives ---------------------------------------------------------------------------
    def set(self, x, y, z, state):
        w, h, d = self.size
        if not (0 <= x < w and 0 <= y < h and 0 <= z < d):
            raise ValueError(f"{self.id}: ({x}, {y}, {z}) is outside {self.size}")
        if state is None:
            self.blocks.pop((x, y, z), None)
        else:
            self.blocks[(x, y, z)] = mc(state)

    def fill(self, x0, y0, z0, x1, y1, z1, state):
        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y0, y1) + 1):
                for z in range(min(z0, z1), max(z0, z1) + 1):
                    self.set(x, y, z, state)

    def clear(self, x0, y0, z0, x1, y1, z1):
        self.fill(x0, y0, z0, x1, y1, z1, None)

    def get(self, x, y, z):
        return self.blocks.get((x, y, z))

    def marker(self, type_, pos, **data):
        self.markers.append({"type": type_, "pos": list(pos), **data})

    # -- the Konoha kit -----------------------------------------------------------------------
    def walls(self, x0, z0, x1, z1, y0, y1, style: str, posts=True):
        """A rectangle of plaster walls with timber corner posts."""
        p = WALLS[style]
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.set(x, y, z0, p["wall"])
                self.set(x, y, z1, p["wall"])
            for z in range(z0, z1 + 1):
                self.set(x0, y, z, p["wall"])
                self.set(x1, y, z, p["wall"])
        if posts:
            for x, z in ((x0, z0), (x1, z0), (x0, z1), (x1, z1)):
                self.fill(x, y0, z, x, y1, z, p["post"])

    def band(self, x0, z0, x1, z1, y, style):
        """The terracotta band Konoha buildings carry at each floor line."""
        p = WALLS[style]
        for x in range(x0, x1 + 1):
            for z in (z0, z1):
                if self.get(x, y, z) != mc(p["post"]):
                    self.set(x, y, z, p["band"])
        for z in range(z0, z1 + 1):
            for x in (x0, x1):
                if self.get(x, y, z) != mc(p["post"]):
                    self.set(x, y, z, p["band"])

    def window(self, x, y, z, h=1, pane="white_stained_glass_pane"):
        for dy in range(h):
            self.set(x, y + dy, z, pane)

    def fire_sign(self, cx, cy, z):
        """The white disc with a red ring and the red fire kanji, nine blocks across, facing south (the Hokage Residence, the Academy)."""
        for dx in range(-4, 5):
            for dy in range(-4, 5):
                d = math.hypot(dx, dy)
                if d <= 4.5:
                    ch = FIRE[3 - dy][dx + 3] if abs(dx) <= 3 and abs(dy) <= 3 else "."
                    self.set(cx + dx, cy + dy, z, "red_concrete" if d > 3.6 or ch == "#" else "white_concrete")

    def gable_roof(self, x0, x1, z0, z1, y, style, gable_style=None, overhang=1, pitch="low"):
        """A tile gable roof, ridge along x, over the walls x0..x1, z0..z1, eaves at height y.
        pitch "low" climbs half a block per row in alternating bottom and top slabs (the gentle
        Konoha roof); "steep" climbs a block per row in stairs. The span with its overhang must be
        odd so the ridge has a centre row. Returns the height of the ridge block."""
        r = ROOFS[style]
        za, zb = z0 - overhang, z1 + overhang
        if (zb - za) % 2:
            raise ValueError(f"{self.id}: roof span {zb - za + 1} is even; adjust overhang or depth")
        mid = (za + zb) // 2
        xs = range(x0 - overhang, x1 + overhang + 1)

        def course(k):  # (height, state) of the row k rows in from the eave, for the north slope
            if pitch == "steep":
                return y + k, f"{r['stairs']}[facing=south,half=bottom]"
            return y + k // 2, f"{r['slab']}[type={'bottom' if k % 2 == 0 else 'top'}]"

        for k in range(mid - za):
            yk, north = course(k)
            south = north.replace("facing=south", "facing=north")
            for x in xs:
                self.set(x, yk, za + k, north)
                self.set(x, yk, zb - k, south)
        ytop = course(mid - za)[0]
        for x in xs:
            self.set(x, ytop, mid, r["full"])
            self.set(x, ytop + 1, mid, f"{r['ridge']}[axis=x]")
        # eave lips: upside-down stairs under the first course, the kit's shadow line
        for x in xs:
            for z, f in ((za, "north"), (zb, "south")):
                if self.get(x, y - 1, z) is None:
                    self.set(x, y - 1, z, f"{r['stairs']}[facing={f},half=top]")
        # gable triangles: plaster under the tiles at both ends
        if gable_style:
            wall = WALLS[gable_style]["wall"]
            for z in range(z0, z1 + 1):
                k = min(z - za, zb - z)
                top = ytop - 1 if z == mid else course(k)[0] - 1
                for yy in range(y, top + 1):
                    for x in (x0, x1):
                        if self.get(x, yy, z) is None:
                            self.set(x, yy, z, wall)
        return ytop + 1

    def flat_roof(self, x0, x1, z0, z1, y, style, roof="smooth_stone"):
        """A flat roof slab with a one-block parapet: where Konoha keeps its water tanks."""
        p = WALLS[style]
        self.fill(x0, y, z0, x1, y, z1, roof)
        for x in range(x0, x1 + 1):
            self.set(x, y + 1, z0, p["trim"])
            self.set(x, y + 1, z1, p["trim"])
        for z in range(z0, z1 + 1):
            self.set(x0, y + 1, z, p["trim"])
            self.set(x1, y + 1, z, p["trim"])

    def water_tank(self, x, y, z, height=3):
        ns = NS
        if height == 1:
            self.set(x, y, z, f"{ns}:water_tank[part=single]")
            return
        self.set(x, y, z, f"{ns}:water_tank[part=bottom]")
        for dy in range(1, height - 1):
            self.set(x, y + dy, z, f"{ns}:water_tank[part=middle]")
        self.set(x, y + height - 1, z, f"{ns}:water_tank[part=top]")

    def shoji(self, x, y, z, facing="south", dark=False):
        b = f"{NS}:{'dark_' if dark else ''}shoji_screen"
        self.set(x, y, z, f"{b}[facing={facing},half=lower]")
        self.set(x, y + 1, z, f"{b}[facing={facing},half=upper]")

    def door(self, x, y, z, facing, wood="spruce"):
        self.set(x, y, z, f"{wood}_door[facing={facing},half=lower,hinge=left,open=false]")
        self.set(x, y + 1, z, f"{wood}_door[facing={facing},half=upper,hinge=left,open=false]")

    # -- output -------------------------------------------------------------------------------
    def connect(self):
        """Fence and pane connections, as Minecraft would compute them on placement."""
        dirs = {"north": (0, 0, -1), "south": (0, 0, 1), "east": (1, 0, 0), "west": (-1, 0, 0)}
        for pos, state in list(self.blocks.items()):
            name = base_name(state)
            fam = FENCES if name.endswith("_fence") else PANES if name.endswith(PANES) else None
            if not fam:
                continue
            props = []
            for d, (dx, dy, dz) in dirs.items():
                nb = self.blocks.get((pos[0] + dx, pos[1] + dy, pos[2] + dz))
                ok = nb is not None and (base_name(nb).endswith(fam) or solid(nb))
                props.append(f"{d}={'true' if ok else 'false'}")
            self.blocks[pos] = f"{name}[{','.join(props)}]"

    def blueprint(self) -> dict:
        self.connect()
        w, h, d = self.size
        palette, chars = {}, {}
        for state in sorted(set(self.blocks.values())):
            ch = CHARS[len(chars)]
            chars[state] = ch
            palette[ch] = state
        layers = []
        for y in range(h):
            layers.append(["".join(chars.get(self.blocks.get((x, y, z)), ".") for x in range(w)) for z in range(d)])
        return {"format": "konoha-blueprint/1", "id": self.id, "title": self.title, "kind": self.kind,
                "size": [w, h, d], "street": "south", "notes": self.notes, "cutaway": self.cutaway,
                "palette": palette, "layers": layers, "markers": self.markers}

    def write(self):
        OUT.mkdir(exist_ok=True)
        bp = self.blueprint()
        (OUT / f"{self.id}.json").write_text(json.dumps(bp, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        counts = {}
        for s in self.blocks.values():
            counts[base_name(s)] = counts.get(base_name(s), 0) + 1
        custom = sum(v for k, v in counts.items() if k.startswith(NS))
        print(f"{self.id}: {len(self.blocks)} blocks ({custom} custom), {len(bp['palette'])} states, "
              f"{len(self.markers)} markers")
        return bp


def solid(state: str) -> bool:
    n = base_name(state)
    if n.startswith(NS):
        return False
    return not n.endswith(("_slab", "_stairs", "_fence", "_door", "_trapdoor", "_pane", "_carpet", "_bed", "lantern"))
