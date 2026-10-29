"""Narrow Hakama: hakama trousers cut narrow for running, pleated at the front and gathered at the
shin into wraps, the ties crossed at the front of the waist, with tabi boots."""
from kit import legs, waistband
from kit_kunoichi import tabi_boots
from paint import solid

META = {"name": "Narrow Hakama", "gender": "unisex",
        "description": "Narrow pleated hakama trousers gathered into shin wraps, crossed ties, tabi boots.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    waistband(g, "P", "twill", 33720)
    legs(g, "P", "twill", 33721, rows=(0, 9), crease=False)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        leg.front.vline(1, 0, 6, "P1"), leg.front.vline(2, 0, 6, "P3")
        for y in range(6, 8):
            leg.strip.hline(0, 15, y, "S3" if y == 6 else "S2")
    tabi_boots(g, top=8, seed=33722)
    tie = g.piece("waist_himo", "TORSO", (-4.6, 0, -2.6), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.12)
    solid(tie, "S", "weave", 33724, 3, edge=False)
    tie.front.set(4, 0, "S1")
