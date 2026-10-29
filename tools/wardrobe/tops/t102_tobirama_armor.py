"""Tobirama Armor: the Second's blue armor. A smooth cuirass with laced lames only over the belly, a
thick white fur collar round the neck and shoulders, short laced shoulder guards and dark sleeves
bound at the forearm."""
from kit import belt, sleeves
from kit_senju import crest, lames, shoulder_guards
from paint import cap, fabric, k, rnd, strip_fabric

META = {
    "name": "Tobirama Armor",
    "gender": "unisex",
    "description": "Blue cuirass with a white fur collar, laced belly lames, short shoulder guards, bound forearms.",
    "tags": ["shinobi", "senju", "armor"],
}


def fur(box, seed: int):
    """White fur: soft tufts with shaded roots and a ragged lower edge."""
    for f in box.faces:
        for y in range(f.h):
            for x in range(f.w):
                r = rnd(x + f.x0, y + f.y0, seed)
                f.set(x, y, k("S", 4 if r > .7 else 3 if r > .25 else 2))
    for f in box.sides:
        for x in range(f.w):
            f.set(x, f.h - 1, k("S", 1 if rnd(x, f.x0, seed) < .5 else 2))


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 1520, 2)
    cap(body, "D", seed=1520)
    strip_fabric(jacket, "P", "smooth", 1521, 2, 0, 8)
    fabric(jacket.top, "P", "smooth", 1521, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 0, "P3")
    lames(jacket.strip, "P", 3, 8, step=3, lace="P0")
    jacket.front.vline(3, 1, 3, "P1"), jacket.front.vline(4, 1, 3, "P3")
    belt(g, "obi", y=8.9, role="K", height=2, buckle=None, inflate=.32)
    back = g.piece("back_crest", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, 1.6, 2.3), scale=(.5, .5, .5))
    for face in back.faces:
        fabric(face, "P", "smooth", 1522, 2)
    crest(back.back, 2, 2, "S3", bar="P0")
    sleeves(g, "D", "weave", 1523, 2, rows=(0, 10))
    for side in ("right", "left"):
        guard = g.part(f"{side}_sleeve")
        for y in range(5, 10):
            for x in range(guard.strip.w):
                guard.strip.set(x, y, "K2" if (x + y * 2) % 4 == 0 else "K3")
        guard.strip.hline(0, guard.strip.w - 1, 5, "P2"), guard.strip.hline(0, guard.strip.w - 1, 9, "P1")
    shoulder_guards(g, length=4, seed=1525, lace="P0", flare=20)
    # The fur collar: a thick ring round the neck with a ruff over each shoulder.
    ruff = g.piece("fur_collar", "TORSO", (-5.5, -.6, -3.2), (11, 3, 7))
    fur(ruff, 1527)
    for side, x in (("right", -6.4), ("left", 4.4)):
        tuft = g.piece(f"fur_{side}", "TORSO", (0, 0, -2.5), (2, 3, 5), pivot=(x, .2, 0))
        fur(tuft, 1528 + (x > 0))
