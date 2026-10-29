"""Travel Gaiters: narrow trousers with pale kyahan gaiters buttoned over the shins from knee to
ankle, tied at the top with cord, over straw sandals: the old road-walker's leggings."""
from kit import legs, leg_ring, waistband
from kit_rugged import straw_sandals
from paint import solid

META = {"name": "Travel Gaiters", "gender": "unisex",
        "description": "Narrow trousers with pale gaiters from knee to ankle tied with cord, over straw sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 35380, 2)
    legs(g, "P", "twill", 35381, 2, rows=(0, 9), crease=False)
    straw_sandals(g)
    for ring in leg_ring(g, "gaiter", 4.6, "S", 2, (5, 5, 5), "weave"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "L1")
            face.hline(0, face.w - 1, 4, "S1")
        outer = ring.right
        for y in (1, 2, 3):
            outer.set(2, y, "K2")
        outer2 = ring.left
        for y in (1, 2, 3):
            outer2.set(2, y, "K2")
    tie = g.piece("waist_tie", "TORSO", (-4.5, 9.4, -2.5), (9, 1, 5), inflate=.12)
    solid(tie, "D", "weave", 35383, 2, edge=False)
