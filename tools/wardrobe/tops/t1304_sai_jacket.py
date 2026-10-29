"""Ink Jacket: after Sai: a cropped dark jacket that stops above the navel, a single long sleeve on
the right arm and the left arm bare, a grey-trimmed collar, a short zip, the tanto across the
back and a small pack for brushes, ink and scrolls."""
from kit_shinobi import tanto
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ink Jacket",
    "gender": "unisex",
    "description": "Cropped one-sleeved dark jacket, bare midriff and left arm, grey collar, tanto and an ink pack on the back.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 13560, 2, 0, 6)
    fabric(body.top, "P", "weave", 13560, 3)
    strip_fabric(jacket, "P", "weave", 13561, 2, 0, 6)
    fabric(jacket.top, "P", "weave", 13561, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 6, "P0")
    jacket.front.vline(3, 1, 5, "P1"), jacket.front.vline(4, 1, 3, "M3")
    jacket.front.hline(0, 7, 0, "D3")
    for face in (jacket.right, jacket.left):
        face.vline(2, 0, 6, "P1")
    # One sleeve: the right arm covered to the wrist, the left left bare to the shoulder seam.
    arm, sleeve = g.part("right_arm"), g.part("right_sleeve")
    strip_fabric(arm, "P", "weave", 13562, 2, 0, 10)
    fabric(arm.top, "P", "weave", 13562, 3)
    strip_fabric(sleeve, "P", "weave", 13563, 2, 0, 9)
    fabric(sleeve.top, "P", "weave", 13563, 3)
    sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "D2")
    left = g.part("left_arm")
    left.strip.hline(0, left.strip.w - 1, 0, "P1")
    fabric(left.top, "P", "weave", 13564, 2)
    collar = g.piece("collar", "TORSO", (-4.5, -1.2, -2.6), (9, 1, 5), inflate=.1)
    solid(collar, "D", "weave", 13565, 2)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "D3")
    pack = g.piece("ink_pack", "TORSO", (-2, 0, 0), (4, 3, 2), pivot=(1.0, 5.4, 2.1))
    solid(pack, "L", "leather", 13566, 2)
    pack.back.hline(0, 3, 0, "L3"), pack.back.set(2, 1, "M3")
    tanto(g, pivot=(-1.2, 2.6, 2.95), rotation=(0, 0, -62), length=8, wrap="D3")
