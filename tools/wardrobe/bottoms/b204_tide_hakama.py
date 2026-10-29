"""Tide Hakama: wide pleated hakama to the ankle, flaring over the shins, with ties at the waist and a
band of waves at the hem, over open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from kit_uzumaki import waves
from paint import fabric, solid, strip_fabric

META = {"name": "Tide Hakama", "gender": "unisex",
        "description": "Wide pleated ankle hakama flaring over the shins, waist ties, wave hem.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 2430, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 2430, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 2431, 2, 0, 9)
        fabric(leg.top, "D", "twill", 2431, 2)
        for face in leg.sides:
            face.vline(1, 0, 9, "D1")
    sandals(g)
    for ring in leg_ring(g, "flare", 4.0, "D", 2, (6, 6, 6), "twill"):
        for face in ring.sides:
            for x in (1, 3, 5):
                face.vline(x, 1, 5, "D1")
            waves(face, 4, "S", 3)
        ring.bottom.fill("D0")
    ties = g.piece("waist_ties", "TORSO", (-4.6, 0, -2.6), (9, 1, 5), pivot=(0, 9.4, 0), inflate=.1)
    solid(ties, "D", "weave", 2432, 3, edge=False)
    knot = g.piece("waist_knot", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(0, 9.4, -3.0))
    solid(knot, "D", "weave", 2433, 3)
