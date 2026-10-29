"""Courtyard Yukata: a light summer yukata to the knee, cream with fine lavender-flecked pinstripes,
short wide sleeves and a narrow obi knotted at the side."""
from kit_hyuga import obi, wrap_front
from kit import flaps, side_panels
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Courtyard Yukata",
    "gender": "unisex",
    "description": "Knee-length cream yukata with fine lavender-flecked pinstripes, short wide sleeves, a side-knotted obi.",
    "tags": ["hyuga", "robe", "wrap"],
    "covers_waist": True,
}


def stripes(face, seed: int = 0):
    """Fine pinstripes on the cream cloth, a lavender fleck where every other stripe crosses a row."""
    for y in range(face.h):
        for x in range(face.w):
            if (x + seed) % 3 == 0:
                face.set(x, y, "A3" if (x + seed) % 6 == 0 and y % 3 == 1 else "P2")


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 4841, 3)
    cap(body, "P", texture="plain", seed=4841, base=3)
    stripes(body.strip, 1)
    wrap_front(body.front, role="P", trim="D2", rows=8, start=1)
    obi(g, "obi", "D", y=7.2, height=2, knot="side", seed=4843)
    for face in flaps(g, "skirt", 7, "P", "plain", 4845, width=9, hem="D2", top=10.6, front_z=-2.75, back_z=1.75, base=3):
        stripes(face, 2)
        face.hline(0, face.w - 1, 6, "D2")
    side_panels(g, "skirt_side", 6, "P", "plain", hem="D2", top=10.6)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "plain", 4847, 3, 0, 4)
        fabric(arm.top, "P", "plain", 4847, 4)
        ox = -3.0 if side == "right" else -1.0
        wide = g.piece(f"{side}_wide_sleeve", bone, (ox - .5, -2.0, -2.5), (5, 6, 5), inflate=.12)
        solid(wide, "P", "plain", 4848 + (side == "left"), 3)
        for face in wide.sides:
            stripes(face, 3)
            face.hline(0, face.w - 1, 5, "D2")
        wide.bottom.fill("P1")
