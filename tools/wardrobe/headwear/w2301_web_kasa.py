"""Web Kasa: the mountain pilgrim's conical straw hat, its crown painted with a plum spider web and
tied under the chin. It sits above the hair, hiding only what stands up from the crown."""
from kit_tsuchigumo import web
from paint import k, rnd

META = {"name": "Web Kasa", "gender": "unisex", "hides_hair": ["crown", "knot", "bun_", "leg_"],
        "description": "Conical straw hat with a plum spider web painted over the crown, tied under the chin.",
        "extras_width": 128}


def straw(box, seed: int, base: int = 3):
    for f in box.faces:
        for y in range(f.h):
            for x in range(f.w):
                s = base - (1 if (x + y) % 3 == 0 else 0) + (1 if rnd(x + f.x0, y + f.y0, seed) > .92 else 0)
                f.set(x, y, k("A", s))
    box.bottom.fill(k("A", base - 2))


def build(g):
    for i, (w, y) in enumerate(((14, -8.9), (11, -9.7), (8, -10.5), (5, -11.3), (2, -12.0))):
        tier = g.piece(f"brim_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 1, w), inflate=.62 if i == 0 else .2)
        straw(tier, 23901 + i)
        c = w // 2
        web(tier.top, c, c, "P1", rings=tuple(range(3, w, 3)))
        for f in tier.sides:
            f.hline(0, f.w - 1, 0, "A1")
    for side, x in (("right", -4.65), ("left", 4.05)):
        cord = g.piece(f"cord_{side}", "HEAD", (0, 0, 0), (1, 8, 1), pivot=(x, -8.4, -1.0), scale=(.5, 1, .5))
        for f in cord.faces:
            f.fill("P2")
