#!/usr/bin/env python3
"""Naruto Minecraft wardrobe compiler (the Village Friends resident wardrobe, extended for shinobi).

Every hairstyle, top and bottom is one Python module under tools/wardrobe/{hair,tops,bottoms}/.
A module paints pixel art in *key colors* (role + shade) and declares 3D cuboid pieces. The
compiler writes one PNG + JSON per piece of clothing to
src/main/resources/assets/narutominecraft/wardrobe/, plus palettes.json, hair_colors.json and
catalog.json. The game resolves key colors through the one palette an outfit owns, so the art
is palette-locked: no garment carries its own RGB.

    python tools/wardrobe/wardrobe.py            # compile everything
    python tools/wardrobe/wardrobe.py --check    # validate and confirm outputs are current
    python tools/wardrobe/wardrobe.py --only t03_arcanist_longcoat
    python tools/wardrobe/wardrobe.py --only tf bf          # every id starting with tf or bf
    python tools/wardrobe/render.py --all        # character sheets in docs/renders/
"""
from __future__ import annotations

import argparse
import colorsys
import importlib.util
import io
import json
import math
import re
import sys
from pathlib import Path

from PIL import Image

TOOL = Path(__file__).resolve().parent
ROOT = TOOL.parents[1]
OUT = ROOT / "src/main/resources/assets/narutominecraft/wardrobe"
KINDS = ("faces", "hair", "headwear", "tops", "bottoms")
KIND_NAME = {"faces": "face", "hair": "hair", "headwear": "headwear", "tops": "top", "bottoms": "bottom"}
GENDERS = ("male", "female", "unisex")

# --------------------------------------------------------------------------------------------
# Key colors. Each opaque authoring pixel names a palette role and one of five shades:
# 0 deep crease/outline, 1 shadow, 2 base, 3 light, 4 highlight. The authoring RGB values only
# make the PNGs readable in an image editor; the game maps them back to (role, shade).
# P primary 60%, S secondary 30%, A accent 10%, L leather, M metal, K ink, D denim, H natural hair,
# E eyes (0 pupil/outline, 1 iris shadow, 2 iris, 3 iris light, 4 eye white), resolved through eye_colors.json.
# Leather, metal, ink and denim are material roles: every palette has its own tone of each.
# X1/X2 are translucent shadows that darken whatever is beneath them.
# --------------------------------------------------------------------------------------------
ROLES = "PSALMKDHE"
PALETTE_ROLES = "PSALMKD"
KEY_RGB = {
    "P": ["1f2d4d", "2f4673", "44619a", "6585bd", "93b0dc"],
    "S": ["6b5d47", "968566", "c4b28c", "e0d0ab", "f5ebcf"],
    "A": ["4d1519", "78232b", "a8363c", "cc5d57", "eb958e"],
    "L": ["2c1c13", "4a2f20", "6b4630", "8f6444", "b38962"],
    "M": ["39342f", "655b4d", "968870", "c4b594", "eee2c0"],
    "K": ["14100c", "221a14", "2f251d", "3c3026", "4a3c30"],
    "D": ["162640", "243a5f", "355280", "5578a7", "8ba7d0"],
    "H": ["3a2213", "5c381f", "80522d", "a86f3c", "d09655"],
    "E": ["0b0a10", "2a3d5c", "3f6aa0", "7aa6d6", "f2efe6"],
}
SHADOW_KEYS = {"X1": 46, "X2": 84}  # alpha of a black multiply
KEYS = {f"{r}{i}": KEY_RGB[r][i] for r in ROLES for i in range(5)}


def key_rgba(key: str) -> tuple[int, int, int, int]:
    if key in SHADOW_KEYS:
        return (0, 0, 0, SHADOW_KEYS[key])
    h = KEYS[key]
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)


RGBA_KEY = {key_rgba(k): k for k in list(KEYS) + list(SHADOW_KEYS)}
if len(RGBA_KEY) != len(KEYS) + len(SHADOW_KEYS):
    raise SystemExit("Key colors must be unique")


def shade(key: str, delta: int) -> str:
    """Same role, clamped shade offset: shade('P2', -1) == 'P1'."""
    if key in SHADOW_KEYS:
        return key
    return f"{key[0]}{max(0, min(4, int(key[1]) + delta))}"


# --------------------------------------------------------------------------------------------
# Palette ramps. Shadows cool and saturate, highlights warm and soften (classic pixel-art
# hue shifting). The compiler bakes the ramps into JSON so Java and the preview agree exactly.
# --------------------------------------------------------------------------------------------
def hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_hex(rgb) -> str:
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(c))) for c in rgb)


def _toward(h: float, target: float, amount: float) -> float:
    d = (target - h + 0.5) % 1.0 - 0.5
    return (h + max(-amount, min(amount, d))) % 1.0


def ramp(base: str, dark: float = 1.0, light: float = 1.0) -> list[str]:
    r, g, b = (c / 255 for c in hex_rgb(base))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    tint = min(1.0, s * 4)
    out = []
    for n in (-2, -1, 0, 1, 2):
        if n < 0:
            k = -n
            vv = v * (1 - 0.19 * k * dark)
            ss = min(1.0, s * (1 + 0.14 * k) + (0.035 * k if s > 0.04 else 0))
            hh = _toward(h, 0.68, 0.024 * k * tint)
        elif n > 0:
            vv = min(1.0, v + (1 - v) * 0.30 * n * light + 0.045 * n * light)
            ss = s * (1 - 0.15 * n * light)
            hh = _toward(h, 0.13, 0.016 * n * tint)
        else:
            hh, ss, vv = h, s, v
        out.append(rgb_hex(c * 255 for c in colorsys.hsv_to_rgb(hh, ss, vv)))
    return out


def load_palettes() -> dict:
    src = json.loads((TOOL / "palettes.json").read_text())
    result = {}
    for pid, p in src.items():
        ramps = {}
        for role in PALETTE_ROLES:
            spec = p[role]
            if isinstance(spec, list):
                ramps[role] = spec
            else:
                ramps[role] = ramp(spec, **p.get("tuning", {}).get(role, {}))
        result[pid] = {"name": p["name"], "ramps": ramps}
    return result


def load_hair_colors() -> dict:
    src = json.loads((TOOL / "hair_colors.json").read_text())
    return {cid: {"name": c["name"], "ramp": c["ramp"] if "ramp" in c else ramp(c["base"], **c.get("tuning", {}))}
            for cid, c in src.items()}


# --------------------------------------------------------------------------------------------
# Painting surfaces. Every cuboid uses Minecraft's box UV net: top/bottom above, then the four
# sides as one continuous strip (right, front, left, back). Face-local x always runs from the
# viewer's left to right while looking at that face from outside; y runs downward.
# --------------------------------------------------------------------------------------------
class Layer:
    def __init__(self, w: int, h: int):
        self.w, self.h = w, h
        self.px: list[list[str | None]] = [[None] * w for _ in range(h)]

    def set(self, x: int, y: int, key: str | None):
        if key is not None and key not in KEYS and key not in SHADOW_KEYS:
            raise ValueError(f"Unknown key color {key}")
        self.px[y][x] = key

    def get(self, x: int, y: int):
        return self.px[y][x]


class Face:
    def __init__(self, layer: Layer, x0: int, y0: int, w: int, h: int, name: str):
        self.layer, self.x0, self.y0, self.w, self.h, self.name = layer, x0, y0, w, h, name

    def inside(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h

    def set(self, x: int, y: int, key: str | None):
        if self.inside(x, y):
            self.layer.set(self.x0 + x, self.y0 + y, key)

    def get(self, x: int, y: int):
        return self.layer.get(self.x0 + x, self.y0 + y) if self.inside(x, y) else None

    def fill(self, key):
        self.rect(0, 0, self.w, self.h, key)

    def rect(self, x, y, w, h, key):
        for yy in range(y, y + h):
            for xx in range(x, x + w):
                self.set(xx, yy, key)

    def hline(self, x0, x1, y, key):
        for x in range(x0, x1 + 1):
            self.set(x, y, key)

    def vline(self, x, y0, y1, key):
        for y in range(y0, y1 + 1):
            self.set(x, y, key)

    def paint(self, fn):
        """fn(x, y, current) -> key or None (None leaves the pixel unchanged)."""
        for y in range(self.h):
            for x in range(self.w):
                k = fn(x, y, self.get(x, y))
                if k is not None:
                    self.set(x, y, k)

    def recolor(self, fn):
        """fn(key) -> key for every painted pixel."""
        for y in range(self.h):
            for x in range(self.w):
                k = self.get(x, y)
                if k is not None:
                    self.set(x, y, fn(k, x, y))

    def clear(self, x, y):
        self.set(x, y, None)


class Box:
    """Box-UV net of one cuboid of size w*h*d at (u, v) in a layer."""

    def __init__(self, layer: Layer, u: int, v: int, w: int, h: int, d: int):
        self.layer, self.u, self.v, self.w, self.h, self.d = layer, u, v, w, h, d
        self.top = Face(layer, u + d, v, w, d, "top")          # last row touches the front
        self.bottom = Face(layer, u + d + w, v, w, d, "bottom")  # last row touches the front
        self.right = Face(layer, u, v + d, d, h, "right")      # character's right; x: back -> front
        self.front = Face(layer, u + d, v + d, w, h, "front")  # x: character's right -> left
        self.left = Face(layer, u + d + w, v + d, d, h, "left")  # x: front -> back
        self.back = Face(layer, u + 2 * d + w, v + d, w, h, "back")  # x: character's left -> right
        self.strip = Face(layer, u, v + d, 2 * (w + d), h, "strip")
        self.faces = [self.top, self.bottom, self.right, self.front, self.left, self.back]
        self.sides = [self.right, self.front, self.left, self.back]

    @property
    def width(self):  # unfolded net size
        return 2 * (self.w + self.d)

    @property
    def height(self):
        return self.d + self.h

    # Strip coordinates of each side's first column.
    @property
    def sx_front(self):
        return self.d

    @property
    def sx_left(self):
        return self.d + self.w

    @property
    def sx_back(self):
        return 2 * self.d + self.w

    def fill(self, key):
        for f in self.faces:
            f.fill(key)

    def paint(self, fn):
        for f in self.faces:
            f.paint(lambda x, y, cur, f=f: fn(f, x, y, cur))


# Steve (wide-arm) player skin layout: (u, v, w, h, d). Overlays are inflated by the game model.
SKIN_PARTS = {
    "head": (0, 0, 8, 8, 8), "hat": (32, 0, 8, 8, 8),
    "body": (16, 16, 8, 12, 4), "jacket": (16, 32, 8, 12, 4),
    "right_arm": (40, 16, 4, 12, 4), "right_sleeve": (40, 32, 4, 12, 4),
    "left_arm": (32, 48, 4, 12, 4), "left_sleeve": (48, 48, 4, 12, 4),
    "right_leg": (0, 16, 4, 12, 4), "right_pants": (0, 32, 4, 12, 4),
    "left_leg": (16, 48, 4, 12, 4), "left_pants": (0, 48, 4, 12, 4),
}
ALLOWED_PARTS = {
    "face": {"head"},
    "hair": {"head", "hat"},
    "headwear": {"hat"},
    "top": {"body", "jacket", "right_arm", "right_sleeve", "left_arm", "left_sleeve"},
    "bottom": {"body", "jacket", "right_leg", "right_pants", "left_leg", "left_pants"},
}
BONES = ("HEAD", "TORSO", "LEFT_ARM", "RIGHT_ARM", "LEFT_LEG", "RIGHT_LEG")
ALLOWED_BONES = {"face": {"HEAD"}, "hair": {"HEAD"}, "headwear": {"HEAD"}, "top": {"TORSO", "LEFT_ARM", "RIGHT_ARM"},
                 "bottom": {"TORSO", "LEFT_LEG", "RIGHT_LEG"}}
MOTIONS = ("none", "flap_front", "flap_back", "sway")
# Player model bone pivots (model pixels, y down, +x is the character's left).
BONE_PIVOT = {"HEAD": (0, 0, 0), "TORSO": (0, 0, 0), "RIGHT_ARM": (-5, 2, 0), "LEFT_ARM": (5, 2, 0),
              "RIGHT_LEG": (-1.9, 12, 0), "LEFT_LEG": (1.9, 12, 0)}

# Base-face pixels the Living Eyes model samples for eye whites, irises and skin: never paint them.
EYE_ROW = {(x, 12) for x in range(8, 16)}


class Piece:
    def __init__(self, box: Box, pid, bone, origin, size, pivot, rotation, inflate, motion, scale):
        self.box, self.id, self.bone = box, pid, bone
        self.origin, self.size, self.pivot = origin, size, pivot
        self.rotation, self.inflate, self.motion, self.scale = rotation, inflate, motion, scale

    def json(self):
        data = {"id": self.id, "bone": self.bone, "pivot": list(self.pivot), "rotation": list(self.rotation),
                "origin": list(self.origin), "size": list(self.size), "uv": [self.box.u, self.box.v]}
        if self.inflate:
            data["inflate"] = self.inflate
        if self.motion != "none":
            data["motion"] = self.motion
        if self.scale:
            data["scale"] = list(self.scale)
        return data


class Garment:
    EXTRAS_W = 64

    def __init__(self, kind: str, gid: str, meta: dict):
        self.kind, self.id, self.meta = kind, gid, meta
        self.skin = Layer(64, 64)
        self.extras = Layer(meta.get("extras_width", self.EXTRAS_W), meta.get("extras_height", 160))
        self.pieces: list[Piece] = []
        self._shelf_x = self._shelf_y = self._shelf_h = 0
        self._parts = {name: Box(self.skin, *spec) for name, spec in SKIN_PARTS.items()}

    def part(self, name: str) -> Box:
        if name not in ALLOWED_PARTS[KIND_NAME[self.kind]]:
            raise ValueError(f"{self.id}: a {self.kind} may not paint {name}")
        return self._parts[name]

    def piece(self, pid: str, bone: str, origin, size, pivot=(0, 0, 0), rotation=(0, 0, 0),
              inflate=0.0, motion="none", scale=None) -> Box:
        if bone not in ALLOWED_BONES[KIND_NAME[self.kind]]:
            raise ValueError(f"{self.id}:{pid} may not attach to {bone}")
        if motion not in MOTIONS:
            raise ValueError(f"{self.id}:{pid} has unknown motion {motion}")
        w, h, d = size
        if min(w, h, d) < 1 or any(int(s) != s for s in size):
            raise ValueError(f"{self.id}:{pid} needs positive integer texture size")
        if inflate < 0:
            raise ValueError(f"{self.id}:{pid} cannot shrink (negative inflate)")
        tw, th = 2 * (w + d), d + h
        if self._shelf_x + tw > self.extras.w:
            self._shelf_x, self._shelf_y, self._shelf_h = 0, self._shelf_y + self._shelf_h + 1, 0
        if tw > self.extras.w or self._shelf_y + th > self.extras.h:
            raise ValueError(f"{self.id}: extras region full at {pid}; raise extras_height")
        box = Box(self.extras, self._shelf_x, self._shelf_y, w, h, d)
        self._shelf_x += tw + 1
        self._shelf_h = max(self._shelf_h, th)
        if any(p.id == pid for p in self.pieces):
            raise ValueError(f"{self.id}: duplicate piece {pid}")
        self.pieces.append(Piece(box, pid, bone, tuple(origin), tuple(size), tuple(pivot), tuple(rotation),
                                 float(inflate), motion, tuple(scale) if scale else None))
        return box

    # -- output -------------------------------------------------------------------------------
    def used_extras_height(self):
        rows = [y for y in range(self.extras.h) if any(self.extras.px[y])]
        return 0 if not rows else ((max(rows) + 16) // 16) * 16

    def image(self) -> Image.Image:
        eh = self.used_extras_height()
        img = Image.new("RGBA", (max(64, self.extras.w), 64 + eh), (0, 0, 0, 0))
        for layer, oy, h in ((self.skin, 0, 64), (self.extras, 64, eh)):
            for y in range(h):
                for x in range(layer.w):
                    k = layer.px[y][x]
                    if k is not None:
                        img.putpixel((x, oy + y), key_rgba(k))
        return img

    @property
    def gender(self) -> str:
        return self.meta["gender"]

    @property
    def locked_to(self) -> str | None:
        return self.meta.get("locked_to")

    def fits(self, gender: str) -> bool:
        return self.gender in (gender, "unisex")

    def definition(self) -> dict:
        m = self.meta
        data = {"id": self.id, "kind": KIND_NAME[self.kind], "name": m["name"], "gender": m["gender"],
                "texture": f"{self.kind}/{self.id}.png", "extrasHeight": self.used_extras_height(),
                "tags": sorted(m.get("tags", [])), "requires": sorted(m.get("requires", [])),
                "rejects": sorted(m.get("rejects", [])), "pieces": [p.json() for p in self.pieces]}
        if self.locked_to:
            data["lockedTo"] = self.locked_to
        if self.kind == "tops":
            data["tucked"] = bool(m.get("tucked", False))
            data["coversWaist"] = bool(m.get("covers_waist", False))
        if "description" in m:
            data["description"] = m["description"]
        return data

    # -- validation ---------------------------------------------------------------------------
    def validate(self):
        errors = []
        kind = KIND_NAME[self.kind]
        if self.meta.get("gender") not in GENDERS:
            errors.append(f"META gender must be one of {GENDERS}")
        if self.locked_to is not None and (kind not in ("top", "bottom") or not isinstance(self.locked_to, str)):
            errors.append("only tops and bottoms may set locked_to (the id of their partner)")
        allowed = set()
        for name in ALLOWED_PARTS[kind]:
            u, v, w, h, d = SKIN_PARTS[name]
            b = Box(self.skin, u, v, w, h, d)
            for f in b.faces:
                allowed |= {(f.x0 + x, f.y0 + y) for y in range(f.h) for x in range(f.w)}
        for y in range(64):
            for x in range(64):
                k = self.skin.px[y][x]
                if k is None:
                    continue
                if (x, y) not in allowed:
                    errors.append(f"skin pixel outside {kind} regions at {x},{y}")
                if kind not in ("hair", "face") and k[0] == "H":
                    errors.append(f"natural hair key on a garment at {x},{y}")
                if kind != "face" and k[0] == "E":
                    errors.append(f"eye key outside a face at {x},{y}")
                if kind in ("hair", "headwear"):
                    if (x, y) in EYE_ROW:
                        errors.append(f"hair paints the protected eye row at {x},{y}")
                    if 8 <= x < 16 and 8 <= y < 16 and y > 8 and 9 <= x <= 14 and k not in SHADOW_KEYS:
                        errors.append(f"hair paints opaque face pixel {x},{y}")
                    # The hat layer sits in front of the animated lash/eye planes: a fringe may
                    # reach the brows (rows 0-2) but only the outer columns may fall lower.
                    if 40 <= x < 48 and 11 <= y < 16 and 1 <= x - 40 <= 6:
                        errors.append(f"hair hat-layer covers eyes/nose/mouth at {x},{y}")
        for p in self.pieces:
            if kind in ("hair", "headwear"):
                lo, hi = world_bounds(p)
                if lo[2] < -4.1 and lo[0] < 3 and hi[0] > -3 and hi[1] > -5.02 and lo[1] < 0:
                    errors.append(f"piece {p.id} hangs over the eyes/nose/mouth")
            for f in p.box.faces:
                for y in range(f.h):
                    for x in range(f.w):
                        k = f.get(x, y)
                        if k is None:
                            errors.append(f"piece {p.id} has an unpainted {f.name} texel {x},{y}")
                            break
                        if kind not in ("hair", "face") and k[0] == "H":
                            errors.append(f"piece {p.id} uses hair keys")
                        if kind != "face" and k[0] == "E":
                            errors.append(f"piece {p.id} uses eye keys")
                    else:
                        continue
                    break
        if kind == "hair" and not any(p.size for p in self.pieces):
            errors.append("hair needs volumetric pieces")
        limit = 504 if kind == "hair" else 512   # the kind's shared slot in the game's 256x512 atlas
        if self.used_extras_height() > limit:
            errors.append(f"3D pieces need {self.used_extras_height()} rows; the {kind} slot holds {limit}")
        return errors


def rot_matrix(rx, ry, rz):
    """Minecraft PartPose rotation order: Z * Y * X applied to a column vector (ZYX intrinsic)."""
    ax, ay, az = (math.radians(a) for a in (rx, ry, rz))
    cx, sx, cy, sy, cz, sz = math.cos(ax), math.sin(ax), math.cos(ay), math.sin(ay), math.cos(az), math.sin(az)
    X = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    Y = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    Z = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]

    def mul(a, b):
        return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return mul(mul(Z, Y), X)


def piece_corners(p: Piece):
    """Bone-local corners of a piece, including pivot, rotation, scale and inflation."""
    w, h, d = p.size
    sx, sy, sz = p.scale or (1, 1, 1)
    ox, oy, oz = p.origin
    g = p.inflate
    m = rot_matrix(*p.rotation)
    corners = []
    for cx in (ox - g, ox + w + g):
        for cy in (oy - g, oy + h + g):
            for cz in (oz - g, oz + d + g):
                v = (cx * sx, cy * sy, cz * sz)
                r = [sum(m[i][k] * v[k] for k in range(3)) for i in range(3)]
                corners.append((r[0] + p.pivot[0], r[1] + p.pivot[1], r[2] + p.pivot[2]))
    return corners


def world_bounds(p: Piece):
    c = piece_corners(p)
    return [min(v[i] for v in c) for i in range(3)], [max(v[i] for v in c) for i in range(3)]


# --------------------------------------------------------------------------------------------
# Module loading and compilation.
# --------------------------------------------------------------------------------------------
def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(f"wardrobe_{path.parent.name}_{path.stem}", path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(TOOL))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(TOOL))
    return module


def build(kind: str, path: Path) -> Garment:
    module = load_module(path)
    g = Garment(kind, path.stem, dict(module.META))
    module.build(g)
    return g


def natural(path: Path):
    """t2 < t10 < t100 < tf001: letters first, then the number, then the name."""
    m = re.match(r"([a-z]+)(\d+)_(.*)", path.stem)
    return (m.group(1), int(m.group(2)), m.group(3)) if m else (path.stem, 0, "")


def sources(kind: str):
    return sorted((p for p in (TOOL / kind).glob("*.py") if not p.name.startswith("_")), key=natural)


def build_all(only=None):
    """only: ids or id prefixes ("tf" builds every female top)."""
    out = {}
    for kind in KINDS:
        for path in sources(kind):
            if only and not any(path.stem.startswith(o) for o in only):
                continue
            out[path.stem] = build(kind, path)
    return out


def png_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def json_text(data) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def load_characters() -> list[dict]:
    """Every tools/wardrobe/characters/*.json: one dressed character per file, in name order.

    A character names one piece of each kind plus the palette, hair color, eye color and
    complexion it is shown in. Characters are the showcase roster for render.py and the game.
    """
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((TOOL / "characters").glob("*.json"))]


def load_eye_colors() -> dict:
    src = json.loads((TOOL / "eye_colors.json").read_text())
    return {cid: {"name": c["name"], "ramp": c["ramp"]} for cid, c in src.items()}


def catalog(garments: dict) -> dict:
    data = {"schemaVersion": 1, "keys": {k: "#" + v for k, v in KEYS.items()}, "shadowKeys": SHADOW_KEYS}
    for kind in KINDS:
        data[kind] = [g.id for g in garments.values() if g.kind == kind]
    data["characters"] = load_characters()
    return data


def compatible(top: Garment, bottom: Garment) -> bool:
    """Sims-style mixing with tag rules; a locked set only ever pairs with its own partner."""
    if top.locked_to or bottom.locked_to:
        return top.locked_to == bottom.id and bottom.locked_to == top.id
    t, b = top.meta, bottom.meta
    tt, bt = set(t.get("tags", [])), set(b.get("tags", []))
    if set(t.get("rejects", [])) & bt or set(b.get("rejects", [])) & tt:
        return False
    if t.get("requires") and not set(t["requires"]) & bt:
        return False
    if b.get("requires") and not set(b["requires"]) & tt:
        return False
    return True


CHARACTER_SLOTS = {"face": "faces", "hair": "hair", "headwear": "headwear", "top": "tops", "bottom": "bottoms"}


def validate_catalog(garments: dict, data: dict) -> list[str]:
    errors = []
    palettes, hairs, eyes = load_palettes(), load_hair_colors(), load_eye_colors()
    ids = set()
    for c in data["characters"]:
        cid = c.get("id", "?")
        if cid in ids:
            errors.append(f"duplicate character {cid}")
        ids.add(cid)
        for slot, kind in CHARACTER_SLOTS.items():
            gid = c.get(slot)
            if gid is None and slot == "headwear":
                continue
            if gid not in garments or garments[gid].kind != kind:
                errors.append(f"character {cid} names unknown {slot} {gid}")
        if c.get("top") in garments and c.get("bottom") in garments and not compatible(garments[c["top"]], garments[c["bottom"]]):
            errors.append(f"character {cid} pairs incompatible pieces")
        for field, table in (("palette", palettes), ("hair_color", hairs), ("eye_color", eyes)):
            if c.get(field) not in table:
                errors.append(f"character {cid} names unknown {field} {c.get(field)}")
        if c.get("complexion") not in range(6):
            errors.append(f"character {cid} needs a complexion 0-5")
    for g in garments.values():
        if g.locked_to and (g.locked_to not in garments or garments[g.locked_to].locked_to != g.id):
            errors.append(f"{g.id} is locked to {g.locked_to}, which must lock back")
    return errors


def outputs(garments: dict, full: bool) -> dict[Path, bytes]:
    files = {}
    for g in garments.values():
        files[OUT / g.kind / f"{g.id}.png"] = png_bytes(g.image())
        files[OUT / g.kind / f"{g.id}.json"] = json_text(g.definition()).encode()
    if full:
        files[OUT / "palettes.json"] = json_text({"schemaVersion": 1, "palettes": load_palettes()}).encode()
        files[OUT / "hair_colors.json"] = json_text({"schemaVersion": 1, "colors": load_hair_colors()}).encode()
        files[OUT / "eye_colors.json"] = json_text({"schemaVersion": 1, "colors": load_eye_colors()}).encode()
        files[OUT / "catalog.json"] = json_text(catalog(garments)).encode()
    return files


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate and fail if outputs are stale")
    ap.add_argument("--only", nargs="*", help="compile only these ids")
    args = ap.parse_args(argv)
    garments = build_all(set(args.only) if args.only else None)
    errors = []
    for g in garments.values():
        errors += [f"{g.id}: {e}" for e in g.validate()]
    full = not args.only
    if full:
        errors += validate_catalog(garments, catalog(garments))
    if errors:
        print("\n".join(errors))
        return 1
    files = outputs(garments, full)
    if args.check:
        stale = [p for p, data in files.items() if not p.exists() or p.read_bytes() != data]
        if full:
            known = set(files)
            stale += [p for kind in KINDS for p in (OUT / kind).glob("*") if p not in known]
        if stale:
            print("Stale wardrobe outputs:\n" + "\n".join(str(p.relative_to(ROOT)) for p in stale))
            return 1
        print(f"Wardrobe current: {len(garments)} pieces")
        return 0
    for path, data in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
    if full:
        known = set(files)
        for kind in KINDS:
            for p in (OUT / kind).glob("*"):
                if p not in known:
                    p.unlink()
    print(f"Compiled {len(garments)} wardrobe pieces")
    return 0


if __name__ == "__main__":
    sys.exit(main())
