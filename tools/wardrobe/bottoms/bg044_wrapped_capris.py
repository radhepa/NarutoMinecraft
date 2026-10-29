"""Wrapped Capris: slim cropped trousers to mid-calf, the hems bound tight with cloth wraps, a
sash with hanging ends at the hip and open-toe sandals."""
from kit import legs, waistband
from kit_kunoichi import obi
from kit_shinobi import sandals
from paint import strip_fabric

META = {"name": "Wrapped Capris", "gender": "unisex",
        "description": "Slim mid-calf trousers bound at the hem with wraps, a hip sash, sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 33460)
    legs(g, "P", "twill", 33461, rows=(0, 6))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for y in range(6, 9):
            for x in range(16):
                leg.strip.set(x, y, "S3" if (x + y) % 3 else "S2")
        leg.strip.hline(0, 15, 6, "S4")
        strip_fabric(leg, "P", "twill", 33462, 1, 5, 5)
    sandals(g)
    obi(g, "waist_sash", y=9.2, role="A", height=1, knot="side", seed=33463)
