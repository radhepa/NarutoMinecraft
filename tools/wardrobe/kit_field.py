"""Field gear for the field collection, the everyday kit of working chunin and jonin: padded vests
with their own closures, collars and pocket layouts, harness straps, half-sleeves over mesh, arm
guards, and for the legs trousers with blousing, tape, knee guards, holsters and cargo pockets.
Seeds come from the field block (32000-32999); every helper takes the piece's own."""
from __future__ import annotations

from kit import SIDES, arm_bone, arm_x, leg_bone
from paint import cap, fabric, k, solid, strip_fabric


# -- tops ------------------------------------------------------------------------------------
def vest(g, role: str = "P", seed: int = 32000, hem: int = 11, closure: str = "zip", ribs=(2, 5, 8),
         texture: str = "plain"):
    """A padded vest on the jacket layer down to row `hem`: stitched ribs (dark seam, puffed row
    above), shaded side seams and a closure: 'zip' down the middle, 'open' (worn unzipped over the
    shirt), 'side' (closed on the wearer's left with two buckles) or 'cross' (a diagonal flap)."""
    jacket = g.part("jacket")
    strip_fabric(jacket, role, texture, seed, 2, 0, hem)
    cap(jacket, role, texture=texture, seed=seed)
    w = jacket.strip.w
    for y in ribs:
        if 0 < y < hem:
            jacket.strip.hline(0, w - 1, y, k(role, 1)), jacket.strip.hline(0, w - 1, y - 1, k(role, 3))
    jacket.strip.hline(0, w - 1, hem, k(role, 0))
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, hem, k(role, 1))
    f = jacket.front
    if closure == "zip":
        f.vline(3, 0, hem - 1, k(role, 0)), f.vline(4, 0, hem - 1, k(role, 1))
    elif closure == "open":
        for y in range(hem + 1):
            f.clear(3, y), f.clear(4, y)
        f.vline(2, 0, hem, k(role, 3)), f.vline(5, 0, hem, k(role, 1))
    elif closure == "side":
        f.vline(5, 0, hem - 1, k(role, 0)), f.vline(6, 0, hem - 1, k(role, 1))
        for y in (2, hem - 3):
            f.set(6, y, "M3"), f.set(7, y, "L2")
    elif closure == "cross":
        for y in range(hem):
            x = 1 + y * 5 // max(1, hem - 1)
            f.set(x, y, k(role, 0)), f.set(min(7, x + 1), y, k(role, 3))
    return jacket


def collar(g, pid: str, role: str = "P", seed: int = 32000, style: str = "stand"):
    """Collars for vests and jackets: 'stand' (the high padded collar), 'low' (a single padded roll),
    'funnel' (tall, split at the front) or 'notch' (folded flat, notched at the throat)."""
    height, y = {"stand": (2, -1.6), "low": (1, -.8), "funnel": (3, -2.4), "notch": (1, -.3)}[style]
    box = g.piece(pid, "TORSO", (-4.5, y, -2.7), (9, height, 5), inflate=.08 if style != "notch" else .14)
    solid(box, role, "plain", seed, 2, edge=False)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, 3))
    if style in ("stand", "funnel"):
        box.front.vline(4, 0, height - 1, k(role, 0))
        box.front.hline(3, 5, height - 1, k(role, 1))
    elif style == "notch":
        box.front.set(3, 0, k(role, 0)), box.front.set(4, 0, k(role, 0)), box.front.set(5, 0, k(role, 1))
    return box


def pocket(g, pid: str, pivot, size=(3, 4, 1), role: str = "P", seed: int = 32000, bone: str = "TORSO",
           rotation=(0, 0, 0), scale: float = .5, snap: str | None = None, texture: str = "plain"):
    """A flapped pocket standing out from its pivot toward the front (or wherever `rotation` turns
    it), at half scale by default so a 3 x 4 texture reads as a 1.5 x 2 pouch."""
    w, h, d = size
    box = g.piece(pid, bone, (-w / 2, 0, -d), size, pivot=pivot, rotation=rotation,
                  scale=(scale, scale, scale) if scale != 1 else None)
    solid(box, role, texture, seed, 2)
    box.front.hline(0, w - 1, 0, k(role, 3)), box.front.hline(0, w - 1, 1, k(role, 1))
    if snap:
        box.front.set(w // 2, 1, snap)
    return box


def strap(g, pid: str, pivot, rotation=(0, 0, 0), length: int = 14, role: str = "L", seed: int = 32000, width: int = 1,
          bone: str = "TORSO", base: int = 2):
    """A strap centred on its pivot: slant it with `rotation` to cross the chest or the back."""
    box = g.piece(pid, bone, (-width / 2, -length / 2, -.5), (width, length, 1), pivot=pivot, rotation=rotation)
    solid(box, role, "leather" if role == "L" else "weave", seed, base, edge=False)
    return box


def shirt(g, role: str = "D", seed: int = 32000, texture: str = "weave", sleeve: int = 11):
    """The shirt under the gear: body cloth and sleeves down to arm row `sleeve` (11 is wrist-long,
    -1 leaves the arms bare), a darker cuff row at the end of the sleeve."""
    body = g.part("body")
    strip_fabric(body, role, texture, seed, 2)
    fabric(body.top, role, texture, seed, 3), fabric(body.bottom, role, texture, seed + 1, 1)
    if sleeve < 0:
        return body
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, role, texture, seed + 2 + (side == "left"), 2, 0, sleeve)
        fabric(arm.top, role, texture, seed + 2, 3)
        arm.strip.hline(0, arm.strip.w - 1, sleeve, k(role, 1))
        if sleeve == 11:
            fabric(arm.bottom, role, texture, seed + 4, 1)
    return body


def half_sleeves(g, role: str = "D", seed: int = 32000, length: int = 4, texture: str = "weave"):
    """Short sleeves to arm row `length`, finished with a raised hem ring on the sleeve overlay."""
    for side in SIDES:
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, role, texture, seed + (side == "left"), 2, 0, length)
        fabric(arm.top, role, texture, seed, 3)
        strip_fabric(sleeve, role, texture, seed + 2, 2, length - 1, length)
        sleeve.strip.hline(0, sleeve.strip.w - 1, length - 1, k(role, 3))
        sleeve.strip.hline(0, sleeve.strip.w - 1, length, k(role, 1))


def chain(face, x0: int, y0: int, x1: int, y1: int, ground: str = "K1", link: str = "K2"):
    """Chain mesh read from a step back: a dark ground crossed by a lighter diamond lattice."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            face.set(x, y, link if (x + y) % 3 == 0 or (x - y) % 3 == 0 else ground)


def mesh_arms(g, rows=(5, 10)):
    """Chain mesh down the forearms to the wrist."""
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        chain(arm.strip, 0, rows[0], arm.strip.w - 1, rows[1])


def tape(box, rows, role: str = "S"):
    """Flat tape wound in bands round a limb's strip, each band lit at the top, a seam every fourth texel."""
    for i, y in enumerate(rows):
        for x in range(box.strip.w):
            box.strip.set(x, y, k(role, 3 if (x + i) % 4 else 2))


def arm_guards(g, seed: int = 32000, role: str = "K", plate: str = "M", y: float = 4.6, height: int = 4):
    """Forearm guards strapped over the sleeve: a cloth sleeve ring with a steel plate on the outer face."""
    out = []
    for side in SIDES:
        guard = g.piece(f"{side}_guard", arm_bone(side), (arm_x(side) - .5, y, -2.5), (5, height, 5))
        solid(guard, role, "smooth", seed + (side == "left"), 2)
        outer = guard.right if side == "right" else guard.left
        fabric(outer, plate, "plain", seed + 2, 3, 1, 1, 3, height - 2)
        outer.hline(1, 3, 1, k(plate, 4))
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, k(role, 3))
        out.append(guard)
    return out


def gloves(g, role: str = "K", seed: int = 32000, top: int = 9):
    """Fingerless gloves from arm row `top` to the knuckles, the fingertips bare below."""
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, role, "smooth", seed + (side == "left"), 2, top, 10)
        arm.strip.hline(0, arm.strip.w - 1, top, k(role, 3))
        arm.bottom.fill(k(role, 1))


# -- bottoms ---------------------------------------------------------------------------------
def trousers(g, role: str = "D", seed: int = 32400, texture: str = "twill", length: int = 5, crease: bool = False):
    """Waistband (body rows 9-11) and legs down to leg row `length`, a belt row at the top."""
    body = g.part("body")
    strip_fabric(body, role, texture, seed, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, k(role, 1))
    fabric(body.bottom, role, texture, seed, 1)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, role, texture, seed + 1 + (side == "left"), 2, 0, length)
        fabric(leg.top, role, texture, seed + 1, 2)
        if crease:
            leg.front.vline(1 if side == "right" else 2, 1, length, k(role, 3))
    return body


def blouse(g, role: str = "D", seed: int = 32400, y: float = 4.6, texture: str = "twill"):
    """Trouser legs bloused over whatever binds the shin: a puffed ring at leg height y."""
    out = []
    for side in SIDES:
        puff = g.piece(f"{side}_blouse", leg_bone(side), (-2.5, y, -2.5), (5, 2, 5))
        solid(puff, role, texture, seed + (side == "left"), 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, k(role, 3))
        out.append(puff)
    return out


def knee_guards(g, seed: int = 32400, role: str = "K", plate: str = "M", y: float = 4.2):
    """A padded guard strapped over each knee, a steel plate riveted to its face."""
    for side in SIDES:
        bone = leg_bone(side)
        band = g.piece(f"{side}_knee_strap", bone, (-2.45, y + 1.4, -2.45), (5, 1, 5))
        solid(band, "L", "leather", seed, 2, edge=False)
        pad = g.piece(f"{side}_knee_pad", bone, (-1.5, 0, -1), (3, 3, 1), pivot=(0, y, -2.4))
        solid(pad, role, "smooth", seed + 1 + (side == "left"), 2)
        pad.front.hline(0, 2, 0, k(plate, 3)), pad.front.set(1, 1, k(plate, 2))
        pad.front.hline(0, 2, 2, k(role, 1))


def holster(g, side: str = "right", seed: int = 32400, role: str = "K", strap_role: str = "L", y: float = 1.0,
            tied: bool = False):
    """A kunai holster strapped to the outer thigh; `tied` adds a second strap below it."""
    bone, x = leg_bone(side), -3.0 if side == "right" else 2.0
    for i, yy in enumerate((y, y + 2.4) if tied else (y,)):
        band = g.piece(f"{side}_holster_strap_{i}", bone, (-2.45, yy, -2.45), (5, 1, 5))
        solid(band, strap_role, "leather", seed + i, 2, edge=False)
    case = g.piece(f"{side}_holster", bone, (0, 0, 0), (1, 3, 2), pivot=(x, y - .2, -1.0))
    solid(case, role, "leather", seed + 3, 3)
    outer = case.right if side == "right" else case.left
    outer.set(0, 0, "M3"), outer.set(1, 0, "M2")


def cargo(g, side: str, seed: int = 32400, role: str = "D", y: float = 1.6, size=(3, 3, 1), scale: float = 1):
    """A flapped cargo pocket on the outer face of the thigh."""
    x, ry = (-2.25, 90) if side == "right" else (2.25, -90)
    return pocket(g, f"{side}_cargo", (x, y, 0), size, role, seed, bone=leg_bone(side), rotation=(0, ry, 0), scale=scale,
                  snap="M3", texture="twill")
