"""Tide Hakama: wide navy hakama for the senior teachers, pleated and flaring a little, a band of sand
waves near the hem, tied at the waist over pale tabi and straw sandals."""
from kit_hyuga import hakama_legs, tabi
from kit_umino import waves
from paint import fabric, solid, strip_fabric

META = {"name": "Tide Hakama", "gender": "unisex",
        "description": "Wide pleated navy hakama with a band of sand waves near the hem, pale tabi and sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 18661, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 18661, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 18662, 2, 0, 8)
    for box in hakama_legs(g, "hakama", "D", 18663, flare=4, length=10, top=0.0):
        for face in box.sides:
            waves(face, 7, "S3")
    tabi(g)
    band = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.2)
    solid(band, "S", "weave", 18665, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "S3")
