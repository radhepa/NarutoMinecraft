"""Split Hakama Trousers: loose split hakama-trousers flaring from the hip and cut off below the knee,
the shins bound in pale wraps over open-toe sandals: easy to run and kneel in."""
from kit_field import trousers
from kit_hyuga import hakama_legs
from kit_shinobi import sandals, wraps
from paint import solid

META = {"name": "Split Hakama Trousers", "gender": "unisex",
        "description": "Loose hakama-trousers flaring to below the knee over pale shin wraps and sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    trousers(g, "D", 32520, length=6)
    hakama_legs(g, "hakama", "D", 32523, flare=3, length=7, top=0.0)
    wraps(g, 7, 9)
    sandals(g)
    tie = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.3, 0), inflate=.2)
    solid(tie, "A", "weave", 32525, 2, edge=False)
