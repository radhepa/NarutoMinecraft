"""Block and building previews for the Konoha kit. It draws with the wardrobe's rasterizer
(tools/wardrobe/render.py's Canvas, the Village Friends preview renderer), so blocks come out with
the same shading and supersampling as the character renders.

Custom blocks are drawn from the compiled blockstates, models and textures under
src/main/resources/assets/narutominecraft/, so a render tests what the game will load. Vanilla
blocks have no textures in this repository: they are drawn as procedural stand-ins in their average
colours (VANILLA below), which is enough to judge massing, palette and rhythm, not texture detail.
"""
from __future__ import annotations

import json
import math
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "wardrobe"))
from render import Canvas, backdrop, font  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "src/main/resources/assets/narutominecraft"
SS = 2


# -- block states -----------------------------------------------------------------------------
def parse_state(s: str) -> tuple[str, dict]:
    if "[" in s:
        name, props = s[:-1].split("[", 1)
        return name, dict(p.split("=") for p in props.split(","))
    return s, {}


@lru_cache(None)
def texture(name: str) -> np.ndarray:
    ns, path = name.split(":")
    return np.array(Image.open(ROOT / f"src/main/resources/assets/{ns}/textures/{path}.png").convert("RGBA"))


@lru_cache(None)
def model(name: str) -> dict:
    ns, path = name.split(":")
    return json.loads((ROOT / f"src/main/resources/assets/{ns}/models/{path}.json").read_text())


@lru_cache(None)
def blockstate(block_id: str) -> dict:
    return json.loads((ASSETS / "blockstates" / f"{block_id}.json").read_text())


def custom_variant(block_id: str, props: dict) -> dict:
    variants = blockstate(block_id)["variants"]
    for key, v in variants.items():
        if not key:
            return v
        want = dict(p.split("=") for p in key.split(","))
        if all(props.get(k) == val for k, val in want.items()):
            return v
    raise KeyError(f"{block_id}{props}: no blockstate variant")


# -- geometry ---------------------------------------------------------------------------------
# Each face: (corner order TL, TR, BL in texture space as functions of from/to), normal.
def face_corners(face, f, t):
    x1, y1, z1 = f
    x2, y2, z2 = t
    return {"north": ((x2, y2, z1), (x1, y2, z1), (x2, y1, z1), (0, 0, -1)),
            "south": ((x1, y2, z2), (x2, y2, z2), (x1, y1, z2), (0, 0, 1)),
            "east": ((x2, y2, z2), (x2, y2, z1), (x2, y1, z2), (1, 0, 0)),
            "west": ((x1, y2, z1), (x1, y2, z2), (x1, y1, z1), (-1, 0, 0)),
            "up": ((x1, y2, z1), (x2, y2, z1), (x1, y2, z2), (0, 1, 0)),
            "down": ((x1, y1, z2), (x2, y1, z2), (x1, y1, z1), (0, -1, 0))}[face]


def axis_rot(axis, deg):
    a = math.radians(deg)
    c, s = math.cos(a), math.sin(a)
    if axis == "x":
        return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    if axis == "y":
        return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def model_quads(model_name: str, yrot: int = 0, xrot: int = 0):
    """World-space quads of a block model in block units (0..1): (TL, TR, BL, BR, normal, uv, tex, light)."""
    m = model(model_name)
    keys = m.get("textures", {})
    out = []
    # Blockstate y rotation turns the model clockwise seen from above, about the block centre.
    ry = axis_rot("y", -yrot) @ axis_rot("x", -xrot)
    for el in m["elements"]:
        f, t = el["from"], el["to"]
        rot = el.get("rotation")
        if rot:
            er = axis_rot(rot["axis"], rot["angle"])
            origin = np.array(rot["origin"], float)
        for face, spec in el["faces"].items():
            tl, tr, bl, n = face_corners(face, f, t)
            pts = [np.array(p, float) for p in (tl, tr, bl)]
            pts.append(pts[1] + pts[2] - pts[0])
            n = np.array(n, float)
            if rot:
                pts = [origin + er @ (p - origin) for p in pts]
                n = er @ n
            pts = [ry @ (p - 8) + 8 for p in pts]
            n = ry @ n
            key = spec["texture"].lstrip("#")
            while key in keys and keys[key].startswith("#"):
                key = keys[key][1:]
            tex = texture(keys[key])
            u1, v1, u2, v2 = spec.get("uv", [0, 0, 16, 16])
            th, tw = tex.shape[:2]
            uv = (u1 * tw / 16, v1 * th / 16, u2 * tw / 16, v2 * th / 16)
            glow = el.get("light_emission", 0) > 0 or el.get("shade") is False
            out.append(([p / 16 for p in pts], n, uv, tex, glow))
    return out


# -- vanilla stand-ins ------------------------------------------------------------------------
# id -> (colour, pattern). Patterns: plain, planks, log, bricks, tiles, grid, stone, wool, glass,
# leaves, path. Colours are the blocks' average texture colours (approximate).
VANILLA = {
    "smooth_sandstone": ("#e0d5a6", "plain"), "cut_sandstone": ("#dccf9d", "grid"), "sandstone": ("#d8cb97", "stone"),
    "smooth_quartz": ("#ece6dc", "plain"), "calcite": ("#e0e0db", "stone"), "bone_block": ("#e2dcc6", "plain"),
    "white_terracotta": ("#d2b2a1", "plain"), "terracotta": ("#985e43", "plain"), "orange_terracotta": ("#a15426", "plain"),
    "red_terracotta": ("#8f3d2e", "plain"), "brown_terracotta": ("#4d3324", "plain"), "light_gray_terracotta": ("#876b62", "plain"),
    "smooth_red_sandstone": ("#b5621f", "plain"), "cut_red_sandstone": ("#b5621f", "grid"),
    "white_concrete": ("#d0d6d7", "plain"), "red_concrete": ("#8e2121", "plain"), "black_concrete": ("#0a0c10", "plain"),
    "oak_planks": ("#a2834f", "planks"), "spruce_planks": ("#735531", "planks"), "dark_oak_planks": ("#432b14", "planks"),
    "birch_planks": ("#c0af79", "planks"), "cherry_planks": ("#e2b2ab", "planks"), "bamboo_planks": ("#c2ad50", "planks"),
    "stripped_spruce_log": ("#745a36", "log"), "stripped_oak_log": ("#b29157", "log"), "stripped_dark_oak_log": ("#4a3a26", "log"),
    "spruce_log": ("#3a2a16", "log"), "oak_log": ("#6d5533", "log"), "dark_oak_log": ("#3c2e1a", "log"),
    "deepslate_tiles": ("#36363a", "tiles"), "deepslate_tile_stairs": ("#36363a", "tiles"), "deepslate_tile_slab": ("#36363a", "tiles"),
    "waxed_oxidized_cut_copper": ("#4f9a80", "grid"), "waxed_oxidized_cut_copper_stairs": ("#4f9a80", "grid"),
    "waxed_oxidized_cut_copper_slab": ("#4f9a80", "grid"), "waxed_cut_copper": ("#c06c50", "grid"),
    "waxed_cut_copper_stairs": ("#c06c50", "grid"), "waxed_cut_copper_slab": ("#c06c50", "grid"),
    "stone_bricks": ("#7b7a7a", "bricks"), "stone_brick_slab": ("#7b7a7a", "bricks"), "stone_brick_stairs": ("#7b7a7a", "bricks"),
    "andesite": ("#888888", "stone"), "polished_andesite": ("#848685", "plain"), "smooth_stone": ("#9e9e9e", "plain"),
    "smooth_stone_slab": ("#9e9e9e", "plain"), "cobblestone": ("#7f7f7f", "stone"), "gravel": ("#837f7e", "stone"),
    "mud_bricks": ("#89684f", "bricks"), "packed_mud": ("#8e6b50", "plain"), "dirt_path": ("#947a41", "path"),
    "coarse_dirt": ("#77553b", "stone"), "grass_block": ("#6f9d47", "grass"), "moss_block": ("#596e2d", "wool"),
    "spruce_slab": ("#735531", "planks"), "spruce_stairs": ("#735531", "planks"), "dark_oak_slab": ("#432b14", "planks"),
    "dark_oak_stairs": ("#432b14", "planks"), "oak_slab": ("#a2834f", "planks"), "birch_slab": ("#c0af79", "planks"),
    "spruce_fence": ("#735531", "planks"), "oak_fence": ("#a2834f", "planks"), "dark_oak_fence": ("#432b14", "planks"), "iron_bars": ("#8a8b8b", "plain"),
    "spruce_trapdoor": ("#6a4d2c", "planks"), "dark_oak_trapdoor": ("#40291a", "planks"),
    "glass_pane": ("#c6dde3", "glass"), "glass": ("#c6dde3", "glass"), "white_stained_glass_pane": ("#efeae0", "glass"),
    "spruce_door": ("#6a4d2c", "planks"), "dark_oak_door": ("#40291a", "planks"),
    "white_wool": ("#e9ecec", "wool"), "red_wool": ("#a02722", "wool"), "blue_wool": ("#35399d", "wool"),
    "white_carpet": ("#e9ecec", "wool"), "red_carpet": ("#a02722", "wool"), "hay_block": ("#a68a22", "plain"), "target": ("#d9c3a9", "plain"), "bookshelf": ("#6b5132", "planks"), "crafting_table": ("#7a5a35", "planks"), "grindstone": ("#8a8a8a", "plain"), "lectern": ("#a2834f", "planks"), "lightning_rod": ("#c56d4f", "plain"), "green_terracotta": ("#4c532a", "plain"), "red_bed": ("#a02722", "wool"), "blue_bed": ("#35399d", "wool"),
    "oak_leaves": ("#4d8a2b", "leaves"), "cherry_leaves": ("#e8a8c0", "leaves"), "azalea_leaves": ("#5a7a2c", "leaves"),
    "flower_pot": ("#7c4536", "plain"), "potted_azalea_bush": ("#5a7a2c", "leaves"), "barrel": ("#86643a", "planks"),
    "chest": ("#a37628", "planks"), "lantern": ("#ffd27a", "plain"), "water": ("#3f76e4", "plain"),
    "bamboo_block": ("#7d8a27", "log"), "bamboo_fence": ("#c2ad50", "planks"), "light_gray_wool": ("#8e8e86", "wool"),
    "stone_brick_wall": ("#7b7a7a", "bricks"), "cauldron": ("#4a4a4f", "plain"), "smoker": ("#5b5a58", "bricks"),
    "red_nether_bricks": ("#460709", "bricks"), "quartz_slab": ("#ece6dc", "plain"), "gray_stained_glass_pane": ("#4c4c4c", "glass"),
    "lime_terracotta": ("#677534", "plain"),
}

THIN = {"glass_pane", "white_stained_glass_pane", "gray_stained_glass_pane", "iron_bars"}
FENCE = {"spruce_fence", "oak_fence", "dark_oak_fence", "bamboo_fence"}
DOORS = {"spruce_door", "dark_oak_door"}
TRAPDOORS = {"spruce_trapdoor", "dark_oak_trapdoor"}
CARPET = {"white_carpet", "red_carpet"}
BEDS = {"red_bed", "blue_bed"}


@lru_cache(None)
def stand_in(name: str, face: str) -> np.ndarray:
    colour, pattern = VANILLA[name]
    c = np.array([int(colour[i:i + 2], 16) for i in (1, 3, 5)], np.float32)
    rng = np.random.default_rng(abs(hash((name, face))) % 2 ** 32)
    k = 1 + rng.normal(0, .035, (16, 16))
    if pattern == "planks":
        for y in (3, 7, 11, 15):
            k[y] *= .78
        k[0:4, 7] *= .85
        k[4:8, 13] *= .85
        k[8:12, 4] *= .85
        k[12:16, 10] *= .85
    elif pattern == "log":
        k *= 1 + np.repeat(rng.normal(0, .06, (1, 16)), 16, 0)
        if face in ("up", "down"):
            k = 1 + rng.normal(0, .03, (16, 16))
            k[[0, 15], :] *= .7
            k[:, [0, 15]] *= .7
    elif pattern == "bricks":
        for y in (3, 7, 11, 15):
            k[y] *= .8
        for y0, xs in ((0, (7, 15)), (4, (3, 11)), (8, (7, 15)), (12, (3, 11))):
            for x in xs:
                k[y0:y0 + 3, x] *= .8
    elif pattern == "tiles":
        for y in (3, 7, 11, 15):
            k[y] *= .7
        for y0, xs in ((0, (7, 15)), (4, (3, 11)), (8, (7, 15)), (12, (3, 11))):
            for x in xs:
                k[y0:y0 + 3, x] *= .75
        k[0::4] *= 1.12
    elif pattern == "grid":
        k[[7, 15], :] *= .8
        k[:, [7, 15]] *= .8
        k[[0, 8], :] *= 1.1
    elif pattern == "stone":
        k = 1 + rng.normal(0, .07, (16, 16))
    elif pattern == "wool":
        k = 1 + rng.normal(0, .05, (16, 16))
    elif pattern == "path":
        k = 1 + rng.normal(0, .08, (16, 16))
    elif pattern == "grass":
        if face == "up":
            k = 1 + rng.normal(0, .09, (16, 16))
        else:
            c = np.array([134, 96, 67], np.float32)
            k = 1 + rng.normal(0, .07, (16, 16))
    elif pattern == "leaves":
        k = 1 + rng.normal(0, .14, (16, 16))
    rgb = np.clip(c[None, None] * k[..., None], 0, 255)
    if pattern == "grass" and face != "up":
        rgb[0:3] = np.array([111, 157, 71]) * (1 + rng.normal(0, .06, (3, 16, 1)))
    alpha = np.full((16, 16, 1), 255, np.float32)
    if pattern == "glass":
        rgb[1:15, 1:15] = rgb[1:15, 1:15] * .2 + np.array([214, 232, 236]) * .8
        rgb[[0, 15], :] *= .85
        rgb[:, [0, 15]] *= .85
    return np.concatenate([np.clip(rgb, 0, 255), alpha], -1).astype(np.uint8)


FACING_Y = {"north": 0, "east": 90, "south": 180, "west": 270}


def vanilla_boxes(name: str, props: dict) -> list[tuple]:
    """(from, to) boxes in pixels, unrotated, plus a y rotation."""
    b = name.replace("minecraft:", "")
    half = props.get("half", "bottom")
    facing = props.get("facing", "north")
    if b.endswith("_slab"):
        typ = props.get("type", "bottom")
        return [((0, 8 if typ == "top" else 0, 0), (16, 16 if typ in ("top", "double") else 8, 16))], 0
    if b.endswith("_stairs"):
        y0, y1 = (8, 16) if half == "bottom" else (0, 8)
        base = ((0, 0 if half == "bottom" else 8, 0), (16, 8 if half == "bottom" else 16, 16))
        return [base, ((0, y0, 0), (16, y1, 8))], FACING_Y[facing]  # the step's back is on the facing side
    if b in THIN:
        axis = props.get("axis", "x")
        return [((0, 0, 7), (16, 16, 9))], 0 if axis == "x" else 90
    if b in FENCE:
        boxes = [((6, 0, 6), (10, 16, 10))]
        for d, ((x0, z0), (x1, z1)) in {"north": ((7, 0), (9, 6)), "south": ((7, 10), (9, 16)),
                                        "east": ((10, 7), (16, 9)), "west": ((0, 7), (6, 9))}.items():
            if props.get(d) == "true":
                boxes += [((x0, 6, z0), (x1, 9, z1)), ((x0, 12, z0), (x1, 15, z1))]
        return boxes, 0
    if b in DOORS:
        return [((0, 0, 0), (16, 16, 3))], FACING_Y[facing] + 180
    if b in TRAPDOORS:
        if props.get("open") == "true":
            return [((0, 0, 13), (16, 16, 16))], FACING_Y[facing]
        return [((0, 0 if half == "bottom" else 13, 0), (16, 3 if half == "bottom" else 16, 16))], 0
    if b in CARPET:
        return [((0, 0, 0), (16, 1, 16))], 0
    if b in BEDS:
        return [((0, 3, 0), (16, 9, 16))], 0
    if b == "lantern":
        return [((5, 1, 5), (11, 8, 11)), ((6, 8, 6), (10, 10, 10))], 0
    if b in ("flower_pot", "potted_azalea_bush"):
        out = [((5, 0, 5), (11, 6, 11))]
        if b == "potted_azalea_bush":
            out.append(((3, 6, 3), (13, 14, 13)))
        return out, 0
    return [((0, 0, 0), (16, 16, 16))], 0


def is_full(state: str) -> bool:
    name, props = parse_state(state)
    if not name.startswith("minecraft:"):
        return False
    b = name[10:]
    if b.endswith(("_slab", "_stairs")) or b in THIN | FENCE | DOORS | TRAPDOORS | CARPET | BEDS:
        return name.endswith("_slab") and props.get("type") == "double"
    if b in ("lantern", "flower_pot", "potted_azalea_bush", "glass", "water") or "leaves" in b:
        return False
    return True


def block_quads(state: str):
    """Quads of one block in block units, for a custom or a vanilla block."""
    name, props = parse_state(state)
    if not name.startswith("minecraft:"):
        v = custom_variant(name.split(":")[1], props)
        return model_quads(v["model"], v.get("y", 0), v.get("x", 0))
    b = name[10:]
    boxes, yrot = vanilla_boxes(name, props)
    ry = axis_rot("y", -yrot)
    out = []
    for f, t in boxes:
        for face in ("north", "south", "east", "west", "up", "down"):
            tl, tr, bl, n = face_corners(face, f, t)
            pts = [np.array(p, float) for p in (tl, tr, bl)]
            pts.append(pts[1] + pts[2] - pts[0])
            pts = [ry @ (p - 8) + 8 for p in pts]
            n = ry @ np.array(n, float)
            tex = stand_in(b, face)
            # stand-in textures sample the face's own area, like Minecraft's auto UVs
            x1, y1, z1 = f
            x2, y2, z2 = t
            uv = {"north": (16 - x2, 16 - y2, 16 - x1, 16 - y1), "south": (x1, 16 - y2, x2, 16 - y1),
                  "west": (z1, 16 - y2, z2, 16 - y1), "east": (16 - z2, 16 - y2, 16 - z1, 16 - y1),
                  "up": (x1, z1, x2, z2), "down": (x1, 16 - z2, x2, 16 - z1)}[face]
            out.append(([p / 16 for p in pts], n, uv, tex, b == "lantern"))
    return out


# -- scenes -----------------------------------------------------------------------------------
def light_for(n):
    """Minecraft's block shading: tops 1.0, north/south .8, east/west .6, bottoms .5."""
    x, y, z = n
    return x * x * .62 + z * z * .82 + y * y * (1.0 if y > 0 else .5)


class Scene:
    """Blocks at integer positions; draws only faces not hidden by a full neighbour."""

    def __init__(self):
        self.blocks: dict[tuple, str] = {}

    def put(self, pos, state):
        self.blocks[tuple(pos)] = state if ":" in state else "minecraft:" + state

    def bounds(self):
        xs, ys, zs = zip(*self.blocks)
        return (min(xs), min(ys), min(zs)), (max(xs) + 1, max(ys) + 1, max(zs) + 1)

    def draw(self, canvas: Canvas, cx, cy, scale, yaw, pitch, cut_y=None, centre=None):
        view = axis_rot("x", pitch) @ axis_rot("y", yaw)
        lo, hi = self.bounds()
        centre = np.array(centre if centre is not None else [(lo[i] + hi[i]) / 2 for i in range(3)], float)
        full = {p for p, s in self.blocks.items() if is_full(s)}
        for pos, state in self.blocks.items():
            if cut_y is not None and pos[1] >= cut_y:
                continue
            p = np.array(pos, float)
            for pts, n, uv, tex, glow in block_quads(state):
                nb = tuple(int(v) for v in np.array(pos) + np.round(n).astype(int))
                if pos in full and nb in full and (cut_y is None or nb[1] < cut_y):
                    continue
                world = [p + q - centre for q in pts]
                scr = [view @ w for w in world]
                wn = view @ n
                if wn[2] <= 1e-6:  # the camera looks down -z in view space
                    continue
                # y is up in the world and down on screen; nearer is smaller depth
                quad = [np.array([cx + s[0] * scale, cy - s[1] * scale, -s[2]]) for s in scr]
                # Canvas.quad wants (p0, p1, p2) = (TR, TL, BL): s runs TL->TR, t runs TL->BL
                canvas.quad([quad[1], quad[0], quad[2], quad[3]], uv, tex, 1.0 if glow else light_for(n))


def save_canvas(canvas: Canvas, out: Path, label: str | None = None, sub: str | None = None):
    img = Image.fromarray(np.clip(canvas.img, 0, 255).astype(np.uint8), "RGB")
    img = img.resize((canvas.w // SS, canvas.h // SS), Image.LANCZOS)
    if label:
        d = ImageDraw.Draw(img)
        d.text((24, 16), label, fill=(60, 40, 28), font=font(30, True))
        if sub:
            d.text((24, 54), sub, fill=(90, 70, 55), font=font(17))
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return img


def new_canvas(w, h, top=(236, 228, 212), bottom=(205, 196, 178)):
    return Canvas(w * SS, h * SS, backdrop(w * SS, h * SS, top, bottom))
