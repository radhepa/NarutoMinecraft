"""Mountain Hakama: wide pleated hakama in deep plum, the hem edged in an ochre web line, tied with
crossed bands at the front, over pale tabi and straw sandals for the shrine stairs."""
from kit_hyuga import hakama_legs, tabi
from kit_tsuchigumo import web_hem
from paint import fabric, solid, strip_fabric

META = {"name": "Mountain Hakama", "gender": "unisex",
        "description": "Wide pleated plum hakama with an ochre web-line hem, pale tabi and straw sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 23751, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "A2")
    fabric(body.bottom, "D", "twill", 23751, 1)
    for side in ("right", "left"):
        strip_fabric(g.part(f"{side}_leg"), "D", "twill", 23752, 2, 0, 8)
    for box in hakama_legs(g, "hakama", "D", 23753, flare=4, length=10, top=0.0):
        for face in box.sides:
            web_hem(face, 9, "A2", "A1")
    tabi(g)
    band = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.2)
    solid(band, "A", "weave", 23756, 2, edge=False)
