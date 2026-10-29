#!/usr/bin/env python3
"""Character renders: a small orthographic renderer of the Minecraft player mesh, its overlay
layers and every 3D piece, using Minecraft's box-UV polygon mapping (the Village Friends preview
renderer, supersampled). Renders are for judging the models before they go in game.

    python tools/wardrobe/render.py hokage            # one character sheet
    python tools/wardrobe/render.py --all             # every character, plus the line-up
    python tools/wardrobe/render.py uchiha --out shot.png
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

import living_eyes as LE
import wardrobe as W

BODY = W.ROOT / "src/main/resources/assets/narutominecraft/textures/body"
OUT = W.ROOT / "docs/renders"
SS = 2  # supersampling factor
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(size, bold=False):
    try:
        return ImageFont.truetype(str(FONT_DIR / ("DejaVuSerif-Bold.ttf" if bold else "DejaVuSans.ttf")), size)
    except OSError:
        return ImageFont.load_default()


def rot(rx, ry, rz):
    return np.array(W.rot_matrix(rx, ry, rz))


PARTS = [  # name, bone, box origin, size, uv, inflate
    ("head", "HEAD", (-4, -8, -4), (8, 8, 8), (0, 0), 0), ("hat", "HEAD", (-4, -8, -4), (8, 8, 8), (32, 0), .5),
    ("body", "TORSO", (-4, 0, -2), (8, 12, 4), (16, 16), 0), ("jacket", "TORSO", (-4, 0, -2), (8, 12, 4), (16, 32), .25),
    ("rarm", "RIGHT_ARM", (-3, -2, -2), (4, 12, 4), (40, 16), 0), ("rsl", "RIGHT_ARM", (-3, -2, -2), (4, 12, 4), (40, 32), .25),
    ("larm", "LEFT_ARM", (-1, -2, -2), (4, 12, 4), (32, 48), 0), ("lsl", "LEFT_ARM", (-1, -2, -2), (4, 12, 4), (48, 48), .25),
    ("rleg", "RIGHT_LEG", (-2, 0, -2), (4, 12, 4), (0, 16), 0), ("rpa", "RIGHT_LEG", (-2, 0, -2), (4, 12, 4), (0, 32), .25),
    ("lleg", "LEFT_LEG", (-2, 0, -2), (4, 12, 4), (16, 48), 0), ("lpa", "LEFT_LEG", (-2, 0, -2), (4, 12, 4), (0, 48), .25),
]


def cube_quads(origin, size, uv, inflate, scale=(1, 1, 1)):
    """Minecraft ModelPart.Cube polygons: (four vertices, (u1, v1, u2, v2), outward normal)."""
    x, y, z = origin
    w, h, d = size
    g = inflate
    x0, y0, z0, x1, y1, z1 = x - g, y - g, z - g, x + w + g, y + h + g, z + d + g
    sx, sy, sz = scale
    V = [np.array(v) * (sx, sy, sz) for v in [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0),
                                             (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]]
    u, v = uv
    f, f1, f2, f3, f4, f5 = u, u + d, u + d + w, u + d + 2 * w, u + 2 * d + w, u + 2 * d + 2 * w
    f6, f7, f8 = v, v + d, v + d + h
    return [((V[5], V[4], V[0], V[1]), (f1, f6, f2, f7), (0, -1, 0)),
            ((V[2], V[3], V[7], V[6]), (f2, f7, f3, f6), (0, 1, 0)),
            ((V[0], V[4], V[7], V[3]), (f, f7, f1, f8), (-1, 0, 0)),
            ((V[1], V[0], V[3], V[2]), (f1, f7, f2, f8), (0, 0, -1)),
            ((V[5], V[1], V[2], V[6]), (f2, f7, f4, f8), (1, 0, 0)),
            ((V[4], V[5], V[6], V[7]), (f4, f7, f5, f8), (0, 0, 1))]


class Canvas:
    def __init__(self, w, h, bg):
        self.img = bg.astype(np.float32).copy()
        self.z = np.full((h, w), np.inf, np.float32)
        self.w, self.h = w, h

    def quad(self, pts, uvs, tex, light):
        """pts: 4 screen points (x, y, depth) in polygon order; uvs: (u1, v1, u2, v2)."""
        p0, p1, p2 = pts[0], pts[1], pts[2]
        es, et = p0[:2] - p1[:2], p2[:2] - p1[:2]
        det = es[0] * et[1] - es[1] * et[0]
        if abs(det) < 1e-6:
            return
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        x0, x1 = max(0, int(math.floor(min(xs)))), min(self.w - 1, int(math.ceil(max(xs))))
        y0, y1 = max(0, int(math.floor(min(ys)))), min(self.h - 1, int(math.ceil(max(ys))))
        if x0 > x1 or y0 > y1:
            return
        gx, gy = np.meshgrid(np.arange(x0, x1 + 1) + .5, np.arange(y0, y1 + 1) + .5)
        dx, dy = gx - p1[0], gy - p1[1]
        s = (dx * et[1] - dy * et[0]) / det
        t = (es[0] * dy - es[1] * dx) / det
        inside = (s >= 0) & (s < 1) & (t >= 0) & (t < 1)
        if not inside.any():
            return
        depth = p1[2] + s * (p0[2] - p1[2]) + t * (p2[2] - p1[2])
        u1, v1, u2, v2 = uvs
        tu = np.floor(u1 + s * (u2 - u1) - 1e-4 * np.sign(u2 - u1)).astype(int)
        tv = np.floor(v1 + t * (v2 - v1) - 1e-4 * np.sign(v2 - v1)).astype(int)
        th, tw = tex.shape[:2]
        tu, tv = np.clip(tu, 0, tw - 1), np.clip(tv, 0, th - 1)
        texel = tex[tv, tu]
        zb = self.z[y0:y1 + 1, x0:x1 + 1]
        draw = inside & (texel[..., 3] > 127) & (depth < zb)
        region = self.img[y0:y1 + 1, x0:x1 + 1]
        region[draw] = texel[draw][:, :3] * light
        zb[draw] = depth[draw]


# -- textures ---------------------------------------------------------------------------------
def resolve(layer: W.Layer, palette: dict, hair: list[str], eyes: list[str]) -> np.ndarray:
    out = np.zeros((layer.h, layer.w, 4), np.uint8)
    for y in range(layer.h):
        for x in range(layer.w):
            k = layer.px[y][x]
            if k is None:
                continue
            if k in W.SHADOW_KEYS:
                out[y, x] = (0, 0, 0, W.SHADOW_KEYS[k])
                continue
            table = hair if k[0] == "H" else eyes if k[0] == "E" else palette["ramps"][k[0]]
            out[y, x] = (*W.hex_rgb(table[int(k[1])]), 255)
    return out


def composite(base: np.ndarray, layer: np.ndarray) -> np.ndarray:
    out = base.copy()
    opaque = layer[..., 3] == 255
    out[opaque] = layer[opaque]
    shadow = (layer[..., 3] > 0) & ~opaque
    k = 1 - layer[..., 3:4].astype(np.float32) / 255
    out[..., :3] = np.where(shadow[..., None], (out[..., :3] * k).round(), out[..., :3]).astype(np.uint8)
    return out


class Character:
    """A dressed character: skin texture plus every visible piece with its texture."""

    def __init__(self, spec: dict, garments: dict):
        self.spec = spec
        palette = W.load_palettes()[spec["palette"]]
        hair = W.load_hair_colors()[spec["hair_color"]]["ramp"]
        eye = W.load_eye_colors()[spec["eye_color"]]
        eyes = eye["ramp"]
        top, bottom = garments[spec["top"]], garments[spec["bottom"]]
        face, hairdo = garments[spec["face"]], garments[spec["hair"]]
        hat = garments.get(spec.get("headwear"))
        order = [top, bottom] if top.meta.get("tucked") else [bottom, top]
        order += [face, hairdo] + ([hat] if hat else [])
        skin = np.array(Image.open(BODY / f"{spec['complexion']}.png").convert("RGBA"))
        for g in order:
            skin = composite(skin, resolve(g.skin, palette, hair, eyes))
        self.skin = skin
        hidden = tuple(hat.meta.get("hides_hair", [])) if hat else ()
        self.pieces = []
        for g in order:
            tex = resolve(g.extras, palette, hair, eyes)
            for p in g.pieces:
                if g is bottom and top.meta.get("covers_waist") and p.id.startswith("waist"):
                    continue
                if g is hairdo and hidden and p.id.startswith(hidden):
                    continue
                self.pieces.append((p, tex, bool(g.meta.get("emissive"))))
        # The Living Eyes planes take their colors the way ResidentSkins bakes them: brow and lash
        # from the hair base, lids, lips and neck shade from the complexion's face skin.
        rgb = W.hex_rgb
        pattern = None
        if eye.get("pattern"):
            rows = eye["pattern"]
            pattern = np.zeros((len(rows), len(rows[0]), 4), np.uint8)
            for y, row in enumerate(rows):
                for x, c in enumerate(row):
                    if c != ".":
                        pattern[y, x] = (*rgb(eyes[int(c)]), 255)
        body = np.array(Image.open(BODY / f"{spec['complexion']}.png").convert("RGB"))
        self.face = dict(style=spec["eye_style"], feminine=spec["feminine"], hair=rgb(hair[2]),
                         brows=spec.get("brows", "fine"), marks=tuple(spec.get("marks", [])), masked=bool(hat and hat.meta.get("covers_face")),
                         skin=tuple(int(c) for c in body[12, 12]), iris=rgb(eyes[2]), white=rgb(eyes[4]),
                         pattern=pattern, glow=bool(eye.get("glow")))


# -- drawing ----------------------------------------------------------------------------------
def light_for(w, glow):
    """Minecraft's flat entity shading from the world-space normal: tops full, front and back .85,
    sides .7, undersides .55. Glowing planes ignore it."""
    if glow:
        return 1.0
    x, y, z = w
    return x * x * .70 + z * z * .85 + y * y * (1.0 if y < 0 else .55)


def render(canvas: Canvas, ch: Character, cx, cy, scale, yaw, pitch=-10, pose=None, head_only=False, blink=0.0):
    pose = pose or {}
    view = rot(pitch, 0, 0) @ rot(0, yaw, 0)
    bones = {b: (np.array(pivot, float), rot(*pose.get(b, (0, 0, 0)))) for b, pivot in W.BONE_PIVOT.items()}
    items = [(bone, np.zeros(3), np.eye(3), origin, size, uv, inflate, None, ch.skin, False)
             for name, bone, origin, size, uv, inflate in PARTS]
    leg_r, leg_l = pose.get("RIGHT_LEG", (0, 0, 0))[0], pose.get("LEFT_LEG", (0, 0, 0))[0]
    for p, tex, glow in ch.pieces:
        rx, ry, rz = p.rotation
        if p.motion == "flap_front":
            rx += min(0, leg_r, leg_l)
        elif p.motion == "flap_back":
            rx += max(0, leg_r, leg_l)
        items.append((p.bone, np.array(p.pivot, float), rot(rx, ry, rz), p.origin, p.size, (p.box.u, p.box.v),
                      p.inflate, p.scale, tex, glow))
    for bone, ppivot, prot, origin, size, uv, inflate, pscale, tex, glow in items:
        if head_only and bone != "HEAD":
            continue
        bpivot, brot = bones[bone]
        for verts, uvs, normal in cube_quads(origin, size, uv, inflate, pscale or (1, 1, 1)):
            world = [bpivot + brot @ (ppivot + prot @ v) for v in verts]
            wn = brot @ (prot @ np.array(normal, float))
            if (view @ wn)[2] >= -1e-6:
                continue
            pts = [np.array([cx + (view @ wv)[0] * scale, cy + (view @ wv)[1] * scale, (view @ wv)[2]]) for wv in world]
            canvas.quad(pts, uvs, tex, light_for(wn, glow))
    # Living Eyes face planes: north-facing quads on the head (and the neck shade on the torso).
    for pl in LE.planes(blink=blink, **ch.face):
        if head_only and pl.bone != "HEAD":
            continue
        bpivot, brot = bones[pl.bone]
        wn = brot @ np.array((0, 0, -1.0))
        if (view @ wn)[2] >= -1e-6:
            continue
        x0, x1, y0, y1 = pl.x - pl.w / 2, pl.x + pl.w / 2, pl.y - pl.h / 2, pl.y + pl.h / 2
        corners = [(x1, y0), (x0, y0), (x0, y1), (x1, y1)]
        if pl.pattern is not None:
            tex = pl.pattern
            th, tw = tex.shape[:2]
            uvs = (tw, 0, 0, th) if pl.mirror else (0, 0, tw, th)
        else:
            tex, uvs = np.array([[(*pl.rgb, 255)]], np.uint8), (0, 0, 1, 1)
        world = [bpivot + brot @ np.array((x, y, pl.z)) for x, y in corners]
        pts = [np.array([cx + (view @ wv)[0] * scale, cy + (view @ wv)[1] * scale, (view @ wv)[2]]) for wv in world]
        canvas.quad(pts, uvs, tex, light_for(wn, pl.glow))


def backdrop(w, h, top=(250, 238, 214), bottom=(226, 205, 168)):
    t = np.linspace(0, 1, h)[:, None, None]
    img = np.array(top, np.float32) * (1 - t) + np.array(bottom, np.float32) * t
    return np.repeat(img, w, axis=1)


def ground_shadow(bg, cx, cy, rx, ry, strength=.22):
    h, w = bg.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    d = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
    a = np.clip(1 - d, 0, 1) ** 1.5 * strength
    bg *= (1 - a)[..., None]


WALK = {"RIGHT_LEG": (26, 0, 0), "LEFT_LEG": (-26, 0, 0), "RIGHT_ARM": (-22, 0, 0), "LEFT_ARM": (22, 0, 0)}
VIEWS = [("front", -28, None), ("side", 62, None), ("back", 152, None), ("stride", -28, WALK)]


def sheet(ch: Character, out: Path):
    W_, H_ = 1800, 1000
    w, h = W_ * SS, H_ * SS
    bg = backdrop(w, h)
    scale = ch.spec.get("scale", 15) * SS
    feet = 860 * SS
    xs = [200, 520, 840, 1160]
    for x in xs:
        ground_shadow(bg, x * SS, feet + 2 * SS, 105 * SS, 18 * SS)
    canvas = Canvas(w, h, bg)
    for x, (_, yaw, pose) in zip(xs, VIEWS):
        render(canvas, ch, x * SS, feet - 24 * scale, scale, yaw, 10, pose)
    # Head close-up on the right.
    hs = scale * 1.9
    render(canvas, ch, 1530 * SS, 700 * SS, hs, -22, 8, head_only=True)
    img = Image.fromarray(canvas.img.clip(0, 255).astype(np.uint8)).resize((W_, H_), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    ink, soft = (62, 38, 28), (120, 92, 70)
    d.text((44, 30), ch.spec["name"], font=font(46, True), fill=ink)
    d.text((46, 88), ch.spec.get("tagline", ""), font=font(20), fill=soft)
    d.line((44, 124, W_ - 44, 124), fill=(205, 182, 145), width=2)
    for x, (label, _, _) in zip(xs, VIEWS):
        tw = d.textlength(label, font=font(18))
        d.text((x - tw / 2, 930), label, font=font(18), fill=soft)
    d.text((1530 - d.textlength("close-up", font=font(18)) / 2, 930), "close-up", font=font(18), fill=soft)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(out)


def lineup(chars: list[Character], out: Path):
    W_, H_ = 340 * len(chars) + 120, 900
    w, h = W_ * SS, H_ * SS
    bg = backdrop(w, h)
    feet = 790 * SS
    xs = [120 + 340 * i + 110 for i in range(len(chars))]
    for x in xs:
        ground_shadow(bg, x * SS, feet + 2 * SS, 110 * SS, 18 * SS)
    canvas = Canvas(w, h, bg)
    for x, ch in zip(xs, chars):
        scale = ch.spec.get("scale", 15) * SS
        render(canvas, ch, x * SS, feet - 24 * scale, scale, -24, 10)
    img = Image.fromarray(canvas.img.clip(0, 255).astype(np.uint8)).resize((W_, H_), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    d.text((44, 30), "Naruto Minecraft", font=font(46, True), fill=(62, 38, 28))
    d.text((46, 88), "Shinobi of the Hidden Leaf, built on the Village Friends resident", font=font(20), fill=(120, 92, 70))
    for x, ch in zip(xs, chars):
        tw = d.textlength(ch.spec["name"], font=font(22, True))
        d.text((x - tw / 2, 820), ch.spec["name"], font=font(22, True), fill=(62, 38, 28))
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    specs = {c["id"]: c for c in W.load_characters()}
    wanted = list(specs) if a.all or not a.ids else a.ids
    garments = W.build_all()
    errors = [f"{g.id}: {e}" for g in garments.values() for e in g.validate()]
    errors += W.validate_catalog(garments, W.catalog(garments))
    if errors:
        print("\n".join(errors))
    chars = [Character(specs[i], garments) for i in wanted]
    for ch in chars:
        sheet(ch, Path(a.out) if a.out and len(chars) == 1 else OUT / f"{ch.spec['id']}.png")
    if a.all:
        lineup(chars, OUT / "lineup.png")


if __name__ == "__main__":
    main()
