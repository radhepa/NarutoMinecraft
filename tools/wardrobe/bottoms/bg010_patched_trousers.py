"""Patched Trousers: sturdy denim trousers rolled up to mid-shin, a square patch sewn over the right
knee and open-toe sandals: worn through at the knee on the training field and mended at home."""
from kit_academy import leg_cloth, turned_hem, waist
from kit_shinobi import sandals
from paint import fabric

META = {"name": "Patched Trousers", "gender": "unisex",
        "description": "Denim trousers rolled to mid-shin, a patch over the right knee, open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = waist(g, "D", "twill", 31535, band="L2")
    body.front.set(3, 9, "M3")
    legs = leg_cloth(g, "D", "twill", 31536, (0, 8))
    for side, leg in zip(("right", "left"), legs):
        leg.front.vline(1 if side == "right" else 2, 1, 7, "D3")
        for face in (leg.right, leg.left):
            face.vline(1, 0, 8, "S2")
    knee = legs[0].front
    fabric(knee, "A", "plain", 31538, 2, 0, 4, 3, 3)
    for x, y in ((0, 4), (2, 4), (0, 6), (2, 6)):
        knee.set(x, y, "A1")
    turned_hem(g, "roll", 7.6, "D", 31539, height=2, base=3)
    sandals(g)
