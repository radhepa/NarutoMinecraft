"""Battle Helmet: the Third Hokage's war helmet. A dark steel cap over the whole crown with the
Hidden Leaf plate on the brow, riveted cheek guards down the sides and a flared neck guard; a
beard grown along the jaw still shows beneath it."""
from kit_sarutobi import HAIR_PREFIXES
from kit_shinobi import forehead_protector
from paint import fabric, k, solid

META = {"name": "Battle Helmet", "gender": "unisex", "hides_hair": HAIR_PREFIXES,
        "description": "Dark steel cap with the leaf plate, riveted cheek guards and a flared neck guard."}


def build(g):
    cap = g.piece("helmet", "HEAD", (-4, -8.4, -4), (8, 2, 8), inflate=.68)
    solid(cap, "P", "smooth", 9901, 2, edge=False)
    fabric(cap.top, "P", "smooth", 9901, 3)
    for f in cap.sides:
        f.hline(0, f.w - 1, 0, k("P", 3))
        for x in (1, 4, 6):
            f.set(x, 1, k("M", 3))
    # The lower rim round the sides and back, set back from the brow so the eyes stay clear.
    rim = g.piece("helmet_rim", "HEAD", (-4, -6.4, -3), (8, 2, 7), inflate=.66)
    solid(rim, "P", "smooth", 9905, 2, edge=False)
    for f in rim.sides:
        f.hline(0, f.w - 1, 1, k("P", 1))
    crest = g.piece("helmet_ridge", "HEAD", (-.5, -1, -4), (1, 1, 8), pivot=(0, -8.6, 0), inflate=.2)
    solid(crest, "A", "smooth", 9902, 2)
    for side, sign in (("right", -1), ("left", 1)):
        guard = g.piece(f"cheek_guard_{side}", "HEAD", (3.9 if sign > 0 else -4.9, -5.6, -3.2), (1, 4, 4), inflate=.1,
                        rotation=(0, 0, 0))
        solid(guard, "P", "smooth", 9903, 2)
        outer = guard.left if sign > 0 else guard.right
        outer.set(1, 1, k("M", 3)), outer.set(2, 1, k("M", 3))
        outer.hline(0, 3, 3, k("P", 1))
    neck = g.piece("neck_guard", "HEAD", (-4.5, 0, 0), (9, 4, 1), pivot=(0, -5.8, 4.4), rotation=(28, 0, 0))
    solid(neck, "P", "smooth", 9904, 2)
    for y in (1, 3):
        neck.back.hline(0, 8, y, k("P", 1))
    forehead_protector(g, "K", ring=False)
