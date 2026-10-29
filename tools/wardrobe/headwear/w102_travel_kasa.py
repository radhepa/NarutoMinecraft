"""Travel Kasa: a wide straw hat for the road, shallow cone woven in rings, tied under the chin. It
sits above the hair, hiding only what stands up from the crown."""
from paint import k, rnd

META = {"name": "Travel Kasa", "gender": "unisex", "hides_hair": ["crown"],
        "description": "Wide shallow straw hat woven in rings, tied under the chin.", "extras_width": 128}


def straw(box, seed: int, base: int = 3):
    for f in box.faces:
        for y in range(f.h):
            for x in range(f.w):
                s = base - (1 if (x + y) % 3 == 0 else 0) + (1 if rnd(x + f.x0, y + f.y0, seed) > .92 else 0)
                f.set(x, y, k("L", s))
    box.bottom.fill(k("L", base - 2))


def build(g):
    for i, (w, y) in enumerate(((13, -8.9), (10, -9.6), (7, -10.3), (4, -11.0), (2, -11.6))):
        tier = g.piece(f"brim_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 1, w), inflate=.62 if i == 0 else .2)
        straw(tier, 1810 + i)
        if i == 0:
            for f in tier.sides:
                f.hline(0, f.w - 1, 0, "L1")
    for side, x in (("right", -4.65), ("left", 4.05)):
        cord = g.piece(f"cord_{side}", "HEAD", (0, 0, 0), (1, 8, 1), pivot=(x, -8.4, -1.0), scale=(.5, 1, .5))
        for f in cord.faces:
            f.fill("K3")
