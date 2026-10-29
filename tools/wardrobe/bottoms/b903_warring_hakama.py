"""Warring Hakama: Warring States battle dress, after Sasuke Sarutobi. Wide pleated hakama of thick
dark cloth gathered at the shin, steel-plated shin guards laced over it and straw sandals."""
from kit import flaps
from paint import fabric, k, solid, strip_fabric

META = {"name": "Warring Hakama", "gender": "unisex",
        "description": "Wide pleated dark hakama gathered at the shin, laced steel shin guards, straw sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 9620, 1, 9, 11)
    fabric(body.bottom, "P", "twill", 9620, 0)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "twill", 9621 + (side == "left"), 1, 0, 9)
        fabric(leg.top, "P", "twill", 9621, 1)
        for x in range(0, leg.strip.w, 2):
            leg.strip.vline(x, 0, 6, "P0")
        pants = g.part(f"{side}_pants")
        strip_fabric(pants, "P", "twill", 9623, 1, 0, 6)
        for x in range(1, pants.strip.w, 3):
            pants.strip.vline(x, 0, 6, "P0")
        pants.strip.hline(0, pants.strip.w - 1, 6, "P2")
        # Straw sandals with dark ties.
        strip_fabric(leg, "S", "weave", 9624, 2, 10, 11)
        leg.strip.hline(0, leg.strip.w - 1, 10, "K1")
        leg.bottom.fill("S1")
    # The front and back panels of the hakama over the hips.
    for face in flaps(g, "waist_hakama", 4, "P", "twill", 9625, width=9, base=1, top=10.6, front_z=-2.8, back_z=1.8):
        for x in (2, 4, 6):
            face.vline(x, 1, 3, "P0")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_suneate", bone, (-2.2, 6.6, -2.6), (4, 4, 1), inflate=.05)
        solid(guard, "M", "smooth", 9627, 2)
        for x in (0, 3):
            guard.front.vline(x, 0, 3, "M1")
        guard.front.hline(0, 3, 0, "M3")
        for y in (1, 3):
            guard.front.set(1, y, k("L", 2)), guard.front.set(2, y, k("L", 2))
        tie = g.piece(f"{side}_suneate_tie", bone, (-2.45, 7.4, -2.45), (5, 1, 5))
        solid(tie, "L", "leather", 9628, 2, edge=False)
