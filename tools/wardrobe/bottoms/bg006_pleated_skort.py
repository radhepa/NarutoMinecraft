"""Pleated Skort: a short pleated skirt panel over snug shorts, striped knee socks and canvas shoes:
the Academy girl who still does cartwheels at break."""
from kit import flaps, footwear
from kit_academy import leg_cloth, stripes, waist

META = {"name": "Pleated Skort", "gender": "female",
        "description": "Short pleated skirt over snug shorts, striped knee socks and canvas shoes.",
        "tags": ["shinobi", "genin", "skirt"]}


def build(g):
    waist(g, "D", "plain", 31475)
    leg_cloth(g, "D", "plain", 31476, (0, 2))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        stripes(leg, range(5, 10), "S3")
        stripes(leg, (5, 7), "A2")
    footwear(g, "shoe", 10, "K", 2, toe="S3", sole="S2")
    for face in flaps(g, "skirt", 4, "D", "plain", 31478, hem="D1", top=11.0, front_z=-2.95, back_z=1.95):
        for x in (1, 3, 5, 7):
            face.vline(x, 1, 3, "D1")
        face.hline(0, face.w - 1, 0, "D3")
