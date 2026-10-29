"""Miko Chihaya: the sheer white over-robe a shrine maiden puts on for the festival dance, printed
with pine sprays, open down the front over a red-collared kosode and tied at the chest with a red
cord, its broad sleeves hanging past the wrist."""
from kit_household import overlap, robe_skirt, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Miko Chihaya",
    "gender": "unisex",
    "description": "Sheer white pine-printed over-robe tied with a red chest cord over a red-collared kosode.",
    "tags": ["civilian", "robe"],
    "covers_waist": True,
}


def pines(face, rows=None):
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            gx = (x + face.x0) % 6
            if y % 6 == 2 and gx in (1, 2, 3):
                face.set(x, y, "D2")
            elif y % 6 == 3 and gx in (0, 2, 4):
                face.set(x, y, "D3")


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 37480, 3)
    cap(body, "S", texture="weave", seed=37480, base=3)
    overlap(body.front, "S4", "S1", rows=9, collar="A2", under="A2")
    strip_fabric(jacket, "S", "plain", 37481, 4)
    pines(jacket.strip)
    for x in range(2, 6):
        jacket.front.vline(x, 0, 11, None)
    jacket.front.vline(1, 0, 11, "S2"), jacket.front.vline(6, 0, 11, "S2")
    knot = g.piece("cord_knot", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 4.0, -2.75))
    solid(knot, "A", "weave", 37482, 2, edge=False)
    for i, x in enumerate((-.9, .4)):
        tassel = g.piece(f"cord_tassel_{i}", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(x, 4.8, -2.85), motion="sway")
        solid(tassel, "A", "weave", 37483 + i, 2)
    robe_skirt(g, "chihaya", 4, "S", "plain", 37485, hem="S2", pattern=pines)
    wide_sleeves(g, "sleeve", "S", "plain", 37487, top=1.6, length=9, base=4, hem="A2", pattern=pines, arm_rows=9)
