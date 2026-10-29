"""Snack Bandolier: a quilted vest over a dark shirt, a leather bandolier across the chest hung
with crinkled snack bags, a sake gourd on a cord at the hip and padded shoulders."""
from kit import arm_bone, arm_x, belt
from kit_akimichi import gourd, quilt, snack_pouch
from paint import fabric, line, solid, strip_fabric

META = {
    "name": "Snack Bandolier",
    "gender": "unisex",
    "description": "Quilted vest, a bandolier of snack bags across the chest, a sake gourd at the hip.",
    "tags": ["shinobi", "genin", "akimichi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 6781, 2)
    fabric(body.top, "K", "weave", 6781, 3)
    for face in jacket.sides:
        quilt(face, "P", 6782, 2, 0, 0, face.w, 11)
    fabric(jacket.top, "P", "weave", 6782, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P0")
    jacket.front.vline(3, 0, 10, "P0"), jacket.front.vline(4, 0, 10, "P1")
    for x in (3, 4):
        jacket.front.set(x, 0, "K2")
    # The bandolier, painted from the right shoulder to the left hip and round the back.
    for face, pts in ((jacket.front, ((0, 0), (7, 9))), (jacket.back, ((7, 0), (0, 9)))):
        line(face, *pts[0], *pts[1], "L2")
        line(face, pts[0][0], pts[0][1] + 1, pts[1][0], pts[1][1] + 1, "L1")
    for i, (x, y) in enumerate(((-2.8, 1.4), (-.3, 4.4), (2.2, 7.2))):
        snack_pouch(g, f"snack_{i}", (x, y, -2.75), role="A" if i % 2 == 0 else "S", size=(2, 3, 1), seed=6783 + i)
    belt(g, "belt", y=10.0, role="L", height=2, inflate=.3)
    gourd(g, "gourd", (-4.4, 10.6, -.6), rotation=(0, 0, 14), motion="flap_front")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "weave", 6790 + (side == "left"), 2, 0, 6)
        fabric(arm.top, "K", "weave", 6790, 3)
        arm.strip.hline(0, arm.strip.w - 1, 6, "K1")
        pad = g.piece(f"{side}_pad", arm_bone(side), (arm_x(side) - .5, -2.4, -2.5), (5, 3, 5), inflate=.12)
        solid(pad, "P", "weave", 6792, 2, edge=False)
        for face in pad.sides:
            quilt(face, "P", 6793, 2)
