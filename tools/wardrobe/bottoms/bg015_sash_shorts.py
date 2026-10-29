"""Sash Shorts: loose knee shorts belted with a broad cloth sash knotted at the hip, its long tail
hanging to the knee, white shin wraps and open-toe sandals."""
from kit_academy import leg_cloth, turned_hem, waist
from kit_shinobi import sandals, wraps
from paint import k, solid

META = {"name": "Sash Shorts", "gender": "unisex",
        "description": "Loose knee shorts with a broad knotted sash, shin wraps and open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "K", "weave", 31610)
    leg_cloth(g, "K", "weave", 31611, (0, 5))
    turned_hem(g, "hem", 5.0, "K", 31613, height=1)
    wraps(g, 6, 9)
    sandals(g)
    band = g.piece("waist_sash", "TORSO", (-4.6, 9.0, -2.6), (9, 2, 5), inflate=.08)
    solid(band, "A", "weave", 31614, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "A3")
    knot = g.piece("waist_sash_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(2.0, 9.0, -3.1))
    solid(knot, "A", "weave", 31615, 3, edge=False)
    tail = g.piece("waist_sash_tail", "TORSO", (0, 0, 0), (2, 6, 1), pivot=(2.2, 10.8, -3.0), rotation=(0, 0, -6),
                   motion="flap_front")
    solid(tail, "A", "weave", 31616, 2)
    tail.front.hline(0, 1, 5, k("A", 1))
