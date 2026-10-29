"""Sealer Haori: the sealing specialist's short haori over a dark inner kimono, worn open, its hem
and cuffs sewn with paper seal tags, a braided cord tying the fronts at the chest and a roll of
blank tags at the hip."""
from kit_hyuga import wrap_front
from kit_specialist import coat_skirts, scroll_tube, seal_trim, shirt
from paint import cap, solid, strip_fabric

META = {
    "name": "Sealer Haori",
    "gender": "unisex",
    "description": "Open short haori over a dark inner kimono, seal tags at hem and cuffs, chest cord, tag roll.",
    "tags": ["shinobi", "haori", "jonin"],
}


def build(g):
    body = shirt(g, "K", "weave", 34080)
    wrap_front(body.front, "K", "S3", rows=6, start=1)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "weave", 34082, 2)
    cap(jacket, "P", texture="weave", seed=34082)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "P3"), f.set(6, y, "P1")
    seal_trim(jacket.strip, 9, 3, every=3, seed=34083)
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "weave", 34084 + (side == "left"), 2, 0, 9)
        seal_trim(sleeve.strip, 7, 3, every=4, seed=34086)
    cord = g.piece("haori_cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 4.0, -2.75))
    solid(cord, "A", "weave", 34087, 2, edge=False)
    knot = g.piece("haori_knot", "TORSO", (-.5, 0, 0), (1, 2, 1), pivot=(0, 4.0, -2.95))
    solid(knot, "A", "weave", 34088, 3, edge=False)
    coat_skirts(g, "haori_skirt", 3, "P", "weave", 34090)
    for p in g.pieces:
        if p.id.startswith("haori_skirt"):
            seal_trim(p.box.strip, p.box.h - 2, 2, every=3, seed=34097)
    scroll_tube(g, "tag_roll", (4.3, 8.6, .5), (90, 0, 0), length=3, role="S", end="A2", seed=34099)
