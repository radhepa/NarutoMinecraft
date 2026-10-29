"""Festival Momohiki: the close-fitting white leggings of the float bearers, worn with a dark
loincloth sash at the waist and black split-toe jika-tabi to mid-shin."""
from kit_household import jika_tabi, trouser_legs, waist
from paint import solid

META = {"name": "Festival Momohiki", "gender": "unisex",
        "description": "Close-fitting white leggings, a dark waist sash, black split-toe jika-tabi.",
        "tags": ["civilian", "trousers"]}


def build(g):
    waist(g, "S", "plain", 37724, base=3)
    trouser_legs(g, "S", "plain", 37725, rows=(0, 9), base=3)
    for side in ("right", "left"):
        g.part(f"{side}_leg").front.vline(1 if side == "right" else 2, 0, 6, "S2")
    jika_tabi(g, "K", top=7)
    band = g.piece("waist_sash", "TORSO", (-4.5, 0, -2.5), (9, 2, 5), pivot=(0, 9.4, 0), inflate=.16)
    solid(band, "K", "weave", 37727, 2, edge=False)
    band.front.hline(0, 8, 0, "K3")
