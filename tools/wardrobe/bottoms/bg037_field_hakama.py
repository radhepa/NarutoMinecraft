"""Field Hakama: a full hakama cut for work rather than ceremony, the wide legs falling to the ankle
and tied at the hip with an accent cord, worn over split-toe socks and straw sandals."""
from kit_field import trousers
from kit_hyuga import hakama_legs, tabi
from paint import k, solid

META = {"name": "Field Hakama", "gender": "unisex",
        "description": "Full working hakama to the ankle, tied at the hip with an accent cord, tabi and sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    trousers(g, "D", 32720, length=8)
    hakama_legs(g, "hakama", "D", 32723, flare=4, length=10, top=0.0)
    tabi(g)
    tie = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.3, 0), inflate=.22)
    solid(tie, "D", "weave", 32725, 3, edge=False)
    knot = g.piece("waist_knot", "TORSO", (-1, 0, -1), (2, 2, 1), pivot=(-2.0, 9.2, -2.7))
    solid(knot, "A", "weave", 32726, 2)
    knot.front.set(0, 0, k("A", 3))
