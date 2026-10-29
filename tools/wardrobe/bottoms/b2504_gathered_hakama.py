"""Gathered Hakama: full trousers in the clan's dark cloth, wide through the thigh and gathered tight
at the calf into the split-toe boots like a field hakama, a stitched waist panel and dark ties."""
from kit import leg_ring, legs, waistband
from kit_tobari import split_toe_boots
from paint import k, solid

META = {"name": "Gathered Hakama", "gender": "unisex",
        "description": "Full trousers wide at the thigh and gathered at the calf, split-toe boots, a stitched waist panel.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    waistband(g, "D", "twill", 25690)
    legs(g, "D", "twill", 25691, rows=(0, 8), crease=False)
    split_toe_boots(g, top=8, role="K", tie=None)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        full = g.piece(f"{side}_fullness", bone, (-2.5, 0, -2.5), (5, 6, 5), inflate=.1)
        solid(full, "D", "twill", 25693 + (side == "left"), 2)
        for face in full.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 1, face.h - 1, k("D", 1))
        full.bottom.fill("D0")
    for ring in leg_ring(g, "gather", 6.0, "D", base=2, size=(5, 2, 5), inflate=-0.0):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "D1"), face.hline(0, face.w - 1, 1, "K2")
    panel = g.piece("waist_panel", "TORSO", (-2, 0, 0), (4, 3, 1), pivot=(0, 9.2, -2.7))
    solid(panel, "D", "twill", 25697, 3)
    panel.front.hline(0, 3, 1, "D1")
