"""Shinobi building blocks: open-toe sandals, bandage wraps, chain mesh, the Konoha flak vest, ANBU
chest plates, a tanto and the steel plate of a forehead protector."""
from glyphs import LEAF, SWIRL, SWIRL_SMALL, stamp
from paint import cap, fabric, solid, strip_fabric


def sandals(g):
    """Open-toe shinobi sandals: navy straps and heel, toes showing at the front."""
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "smooth", 41, 2, 10, 11)
        leg.front.set(1, 11, None), leg.front.set(2, 11, None)
        leg.front.hline(0, 3, 10, "D3")
        leg.bottom.fill("K1")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "K1")
        pants.front.set(1, 11, None), pants.front.set(2, 11, None)
        pants.bottom.fill("K0")


def wraps(g, top: int = 6, bottom: int = 9):
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for y in range(top, bottom + 1):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, "S2" if (x + y * 2) % 5 == 0 else "S3")


def bandage(face, x0: int, y0: int, x1: int, y1: int):
    """Bandage turns wound on a slant over a face rectangle."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            face.set(x, y, "S2" if (x + y) % 3 == 0 else "S3")


def mesh(face, x0: int, y0: int, x1: int, y1: int, key: str = "K2"):
    """Chain mesh: a dark net over the skin, one texel in four left open so the skin shows through."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if x % 2 == 0 or y % 2 == 0:
                face.set(x, y, key)


def protector_plate(face, x0: int = 0):
    """The steel plate of a forehead protector, 18 x 8 texels drawn at triple resolution."""
    fabric(face, "M", "plain", 63, 3, x0, 0, 18, 8)
    face.hline(x0, x0 + 17, 0, "M4"), face.hline(x0, x0 + 17, 7, "M1")
    face.vline(x0, 0, 7, "M2"), face.vline(x0 + 17, 0, 7, "M1")
    for x in (2, 15):
        face.set(x0 + x, 2, "M1"), face.set(x0 + x, 5, "M1")
    stamp(face, LEAF, x0 + 5, 0, {"#": "M0"})


def flak_vest(g, shoulder_swirls: bool = True, seed: int = 52):
    """The Konoha flak vest in P: padded ribs, a zip, the red swirl on the back, a high collar and
    four scroll pockets. Shoulder swirl patches sit on the sleeves, so only tops with sleeves add them."""
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "plain", seed, 2, 0, 11)
    cap(jacket, "P", texture="plain", seed=seed)
    for y in (2, 5, 8):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P1")
    for y in (1, 4, 7):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P0")
    jacket.front.vline(3, 0, 10, "P0"), jacket.front.vline(4, 0, 10, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    back = g.piece("back_swirl", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, 2.2, 2.3), scale=(.5, .5, .5))
    fabric(back.back, "P", "plain", seed + 1, 2)
    stamp(back.back, SWIRL, 0, 0, {"#": "A2"})
    for face in (back.top, back.bottom, back.right, back.left, back.front):
        face.fill("P2")
    if shoulder_swirls:
        for side, bone, x in (("right", "RIGHT_ARM", -3.05), ("left", "LEFT_ARM", 3.05)):
            patch = g.piece(f"{side}_swirl", bone, (0, 0, -3), (1, 6, 6), pivot=(x - (.5 if side == "right" else 0), .6, 0),
                            scale=(.5, .5, .5))
            outer = patch.right if side == "right" else patch.left
            for face in patch.faces:
                face.fill("D2")
            rows = SWIRL_SMALL if side == "left" else [r[::-1] for r in SWIRL_SMALL]
            stamp(outer, rows, 0, 0, {"#": "A2"})
    collar = g.piece("collar", "TORSO", (-4.5, -1.6, -2.7), (9, 2, 5), inflate=.08)
    solid(collar, "P", "plain", seed + 4, 2)
    collar.front.hline(3, 5, 0, "P0"), collar.front.set(4, 1, "P0")
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "P3")
    for i, x in enumerate((-3.7, -2.1, .6, 2.2)):
        pocket = g.piece(f"scroll_pocket_{i}", "TORSO", (0, 0, -1), (3, 6, 1), pivot=(x, 3.4, -2.3), scale=(.5, .5, .5))
        solid(pocket, "P", "plain", seed + 5 + i, 2)
        pocket.front.hline(0, 2, 0, "P3"), pocket.front.hline(0, 2, 1, "P1")
        pocket.front.vline(2, 2, 5, "P1")


def anbu_plates(g, seed: int = 152, belt: bool = True):
    """ANBU chest armor in P on the jacket layer: plates split by seams, open below the ribs, black
    side straps, and a black belt with a steel buckle on the body layer."""
    jacket, body = g.part("jacket"), g.part("body")
    strip_fabric(jacket, "P", "plain", seed, 2, 0, 8)
    cap(jacket, "P", texture="plain", seed=seed)
    for y in (3, 6):
        jacket.strip.hline(0, jacket.strip.w - 1, y - 1, "P1")
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 0, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 8, "P0")
    jacket.front.vline(4, 0, 8, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 8, "K1"), face.vline(2, 0, 8, "K2")
    if belt:
        body.strip.hline(0, body.strip.w - 1, 9, "K1"), body.strip.hline(0, body.strip.w - 1, 10, "K2")
        body.front.set(3, 9, "M3"), body.front.set(4, 9, "M3"), body.front.set(3, 10, "M2"), body.front.set(4, 10, "M2")


def tanto(g, prefix: str = "tanto", pivot=(-1.0, 4.6, 2.9), rotation=(0, 0, -38), bone: str = "TORSO", length: int = 8,
          wrap: str = "S3"):
    """A short blade in its sheath: wrapped hilt above the pivot, steel guard, black sheath below."""
    hilt = g.piece(f"{prefix}_hilt", bone, (-.5, -4, -.5), (1, 4, 1), pivot=pivot, rotation=rotation)
    solid(hilt, "K", "smooth", 157, 2)
    for face in hilt.sides:
        for y in (0, 2):
            face.set(0, y, wrap)
    guard = g.piece(f"{prefix}_guard", bone, (-1, 0, -1), (2, 1, 2), pivot=pivot, rotation=rotation)
    solid(guard, "M", "plain", 158, 3)
    sheath = g.piece(f"{prefix}_sheath", bone, (-.5, 1, -.5), (1, length, 1), pivot=pivot, rotation=rotation)
    solid(sheath, "K", "smooth", 159, 2)
    for face in sheath.sides:
        face.set(0, length - 1, "M2")


# The ANBU spiral, one texel per pixel on the outer face of the left upper arm.
TATTOO = ["AAA.",
          "A.A.",
          "A.AA"]


def anbu_arms(g, top: int = 4, guards: bool = True, tattoo: bool = True, shirt: str = "D"):
    """Black gloves from row `top` to the hand, long white guards from elbow to wrist with a seam
    and a steel stud, a shirt edge on the shoulder and the red spiral on the bare left upper arm."""
    for side in ("right", "left"):
        arm, guard = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        if shirt:
            fabric(arm.top, shirt, "weave", 153, 2)
            arm.strip.hline(0, arm.strip.w - 1, 0, f"{shirt}2")
        strip_fabric(arm, "K", "smooth", 154, 2, top, 11)
        fabric(arm.bottom, "K", "smooth", 154, 1)
        if guards:
            strip_fabric(guard, "S", "plain", 155 + (side == "left"), 2, 4, 9)
            guard.strip.hline(0, guard.strip.w - 1, 4, "S4")
            guard.strip.hline(0, guard.strip.w - 1, 7, "S1")
            guard.strip.hline(0, guard.strip.w - 1, 9, "S1")
            outer = guard.right if side == "right" else guard.left
            outer.set(1, 7, "M3"), outer.set(2, 7, "M3")
    if tattoo:
        left = g.part("left_arm").left
        for y, row in enumerate(TATTOO):
            for x, ch in enumerate(row):
                if ch == "A":
                    left.set(x, 1 + y, "A2")
