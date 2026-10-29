"""Previews of created characters, in render.py's style: sample players rolled the way Varied's "Roll a life" does,
and one player across the three age stages. The player model is drawn as the player poser will draw it: scaled by
stage, with the child's head 10% larger (render.py draws residents, whose heads never change size).

    python3 tools/creator/creator.py --samples    # docs/renders/creator/samples_N.png and stages.png
"""
from __future__ import annotations

import numpy as np
from PIL import Image, ImageDraw

import creator as C
import render as R
import wardrobe as W

OUT = W.ROOT / "docs/renders/creator"
SS = R.SS


def render_player(canvas: R.Canvas, ch: R.Character, cx, cy, scale, yaw, pitch=10, pose=None, head=1.0):
    """render.render with the player poser's head scale: HEAD-bone geometry (pieces and Living Eyes planes) grows
    about the neck by `head`. Depth uses the scaled geometry, so a bigger head still sorts against the body."""
    pose = pose or {}
    view = R.rot(pitch, 0, 0) @ R.rot(0, yaw, 0)
    bones = {b: (np.array(pivot, float), R.rot(*pose.get(b, (0, 0, 0)))) for b, pivot in W.BONE_PIVOT.items()}
    grow = {b: (head if b == "HEAD" else 1.0) for b in bones}
    items = [(bone, np.zeros(3), np.eye(3), origin, size, uv, inflate, None, ch.skin, False)
             for name, bone, origin, size, uv, inflate in R.PARTS]
    for p, tex, glow in ch.pieces:
        items.append((p.bone, np.array(p.pivot, float), R.rot(*p.rotation), p.origin, p.size, (p.box.u, p.box.v),
                      p.inflate, p.scale, tex, glow))

    def screen(wv):
        v = view @ wv
        return np.array([cx + v[0] * scale, cy + v[1] * scale, v[2]])

    for bone, ppivot, prot, origin, size, uv, inflate, pscale, tex, glow in items:
        bpivot, brot = bones[bone]
        for verts, uvs, normal in R.cube_quads(origin, size, uv, inflate, pscale or (1, 1, 1)):
            world = [bpivot + brot @ ((ppivot + prot @ v) * grow[bone]) for v in verts]
            wn = brot @ (prot @ np.array(normal, float))
            if (view @ wn)[2] >= -1e-6:
                continue
            canvas.quad([screen(wv) for wv in world], uvs, tex, R.light_for(wn, glow))
    for pl in R.LE.planes(blink=0.0, **ch.face):
        bpivot, brot = bones[pl.bone]
        wn = brot @ np.array((0, 0, -1.0))
        if (view @ wn)[2] >= -1e-6:
            continue
        x0, x1, y0, y1 = pl.x - pl.w / 2, pl.x + pl.w / 2, pl.y - pl.h / 2, pl.y + pl.h / 2
        if pl.pattern is not None:
            tex = pl.pattern
            th, tw = tex.shape[:2]
            uvs = (tw, 0, 0, th) if pl.mirror else (0, 0, tw, th)
        else:
            tex, uvs = np.array([[(*pl.rgb, 255)]], np.uint8), (0, 0, 1, 1)
        world = [bpivot + brot @ (np.array((x, y, pl.z)) * grow[pl.bone]) for x, y in ((x1, y0), (x0, y0), (x0, y1), (x1, y1))]
        canvas.quad([screen(wv) for wv in world], uvs, tex, R.light_for(wn, pl.glow))


def stage_scale(data: dict, stage: str) -> tuple[float, float]:
    st = data["stages"][stage]
    return st["scale"], st["head"]


def draw_player(canvas, ch, x, feet, unit, data, stage, yaw=-24, pose=None):
    """A player standing with their feet at `feet`: 32 model pixels tall at full scale, the head added on top."""
    s, head = stage_scale(data, stage)
    scale = unit * s
    render_player(canvas, ch, x, feet - 24 * scale, scale, yaw, 10, pose, head)


def _label(spec: dict, data: dict, origin: str, family: str) -> tuple[str, str]:
    o = data["origins"][origin]
    title = o["name"] if o["clan"] else ("Clanless · " + family if family else "Clanless")
    return title, f"{spec['hair']} · {spec['hair_color'].title().replace('_', ' ')}"


def samples(world: C.World, data: dict, count: int = 10):
    """Ten players: a Roll a life from save seeds 1..N (origin by population weight), so most are clanless."""
    OUT.mkdir(parents=True, exist_ok=True)
    rolled = []
    for seed in range(1, count + 1):
        origin = C.roll_origin(data, seed)
        look = C.roll_look(data, seed, origin)
        rolled.append((origin, look))
    forced = ["uchiha", "hyuga", "inuzuka", "uzumaki", "akimichi"]
    for i, origin in enumerate(forced):
        rolled.append((origin, C.roll_look(data, 100 + i, origin)))
    rolled += [(o, data["origins"][o]["defaults"][b]) for o, b in (("clanless", "male"), ("clanless", "female"),
                                                                   ("nara", "male"), ("yamanaka", "female"), ("haruno", "female"))]
    groups = [rolled[i:i + 5] for i in range(0, len(rolled), 5)]
    subtitles = ["Roll a life, save seeds 1 to 5 (drawn by population: most are clanless)",
                 "Roll a life, save seeds 6 to 10",
                 "Clan-born rolls: Uchiha, Hyuga, Inuzuka, Uzumaki, Akimichi",
                 "The creator's opening looks: clanless (both bodies), Nara, Yamanaka, Haruno"]
    for n, (group, subtitle) in enumerate(zip(groups, subtitles), 1):
        lineup(world, data, group, OUT / f"samples_{n}.png", subtitle)


def lineup(world, data, group, out, subtitle, stage="child"):
    W_, H_ = 340 * len(group) + 120, 820
    w, h = W_ * SS, H_ * SS
    bg = R.backdrop(w, h)
    feet = 700 * SS
    xs = [120 + 340 * i + 110 for i in range(len(group))]
    for x in xs:
        R.ground_shadow(bg, x * SS, feet + 2 * SS, 90 * SS, 15 * SS)
    canvas = R.Canvas(w, h, bg)
    labels = []
    for x, (origin, look) in zip(xs, group):
        spec = C.spec(data, origin, look, stage)
        draw_player(canvas, R.Character(spec, world.garments), x * SS, feet, 17 * SS, data, stage)
        labels.append(_label(spec, data, origin, look.get("family", "")))
    img = Image.fromarray(canvas.img.clip(0, 255).astype(np.uint8)).resize((W_, H_), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    d.text((44, 30), "Character creation", font=R.font(46, True), fill=(62, 38, 28))
    d.text((46, 88), subtitle, font=R.font(20), fill=(120, 92, 70))
    for x, (title, sub) in zip(xs, labels):
        tw = d.textlength(title, font=R.font(22, True))
        d.text((x - tw / 2, 725), title, font=R.font(22, True), fill=(62, 38, 28))
        tw = d.textlength(sub, font=R.font(14))
        d.text((x - tw / 2, 758), sub, font=R.font(14), fill=(120, 92, 70))
    img.save(out)
    print(out)


def grown(data: dict, origin: str, look: dict, stage: str, outfit_id: str) -> dict:
    """The same player at a later stage: the hair the Years Later mirror suggests, a rank outfit of that stage."""
    out = dict(look)
    out["hair"] = data["grows_into"].get(look["hair"], {}).get(stage, look["hair"])
    out["outfit"] = outfit_id
    o = C.view(data, origin, stage)["outfits"][look["body"]]
    chosen = next(x for x in o if x["id"] == outfit_id)
    if look["palette"] not in chosen["palettes"]:
        out["palette"] = chosen["palettes"][0]
    return out


def stages_sheet(world: C.World, data: dict):
    """One clanless player at 11, 15 and 20: scale 0.78 with a larger head, 0.9, then 1.0."""
    base = dict(data["origins"]["clanless"]["defaults"]["female"], hair="hg003_short_twin_tails", hair_color="CHESTNUT",
                eye_color="JADE", complexion=2, palette="ACADEMY_GENIN_SKY")
    rows = [("child", base, "Child, 11 to 12: scale 0.78, head 1.1"),
            ("teen", grown(data, "clanless", base, "teen", "kunoichi.wrap_runner"), "Teen, 13 to 17: scale 0.9"),
            ("adult", grown(data, "clanless", base, "adult", "kunoichi.flak_wrap"), "Adult, 18 and up: scale 1.0")]
    W_, H_ = 1500, 900
    w, h = W_ * SS, H_ * SS
    bg = R.backdrop(w, h)
    feet = 760 * SS
    xs = [300, 750, 1200]
    for x in xs:
        R.ground_shadow(bg, x * SS, feet + 2 * SS, 100 * SS, 16 * SS)
    canvas = R.Canvas(w, h, bg)
    for x, (stage, look, _) in zip(xs, rows):
        spec = C.spec(data, "clanless", look, stage)
        draw_player(canvas, R.Character(spec, world.garments), x * SS, feet, 19 * SS, data, stage)
    img = Image.fromarray(canvas.img.clip(0, 255).astype(np.uint8)).resize((W_, H_), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    d.text((44, 30), "Growing up", font=R.font(46, True), fill=(62, 38, 28))
    d.text((46, 88), "One player across the age stages: the hair grows (the Years Later mirror's suggestion), the outfit follows the rank",
           font=R.font(20), fill=(120, 92, 70))
    # A 1.8 m ruler: the full-scale player is 32 model pixels (2 blocks' worth of pixels at 16 per block is 1.8 m).
    top = feet / SS - 32 * 19
    d.line((80, feet / SS, 80, top), fill=(160, 130, 100), width=2)
    for k in range(5):
        y = feet / SS - k * (32 * 19) / 4
        d.line((72, y, 88, y), fill=(160, 130, 100), width=2)
    d.text((40, top - 30), "1.8 m", font=R.font(16), fill=(120, 92, 70))
    for x, (stage, look, text) in zip(xs, rows):
        tw = d.textlength(text, font=R.font(20, True))
        d.text((x - tw / 2, 790), text, font=R.font(20, True), fill=(62, 38, 28))
        o = next(v for v in C.view(data, "clanless", stage)["outfits"][look["body"]] if v["id"] == look["outfit"])
        sub = f"{look['hair']} · {o['id']} ({o['rank']})"
        tw = d.textlength(sub, font=R.font(14))
        d.text((x - tw / 2, 822), sub, font=R.font(14), fill=(120, 92, 70))
    out = OUT / "stages.png"
    img.save(out)
    print(out)
