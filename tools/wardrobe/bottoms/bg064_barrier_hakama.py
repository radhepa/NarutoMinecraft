"""Barrier Hakama: full pleated hakama in the robe's colour, edged at the hem in the corps accent,
over bandaged ankles and open-toe sandals."""
from kit import flaps
from kit_hyuga import hakama_legs
from kit_shinobi import sandals, wraps
from paint import fabric, k, strip_fabric

META = {"name": "Barrier Hakama", "gender": "unisex",
        "description": "Full pleated hakama with an accent hem, bandaged ankles and sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 34460, 2, 9, 11)
    fabric(body.bottom, "P", "twill", 34460, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "twill", 34461, 2, 0, 7)
        fabric(leg.top, "P", "twill", 34461, 2)
    wraps(g, 8, 9)
    sandals(g)
    for box in hakama_legs(g, "hakama", "P", 34462, flare=6, length=9, top=.4):
        for face in box.sides:
            face.hline(0, face.w - 1, face.h - 1, "A2")
    for face in flaps(g, "waist_hakama", 4, "P", "twill", 34464, width=9, top=10.8, front_z=-2.8, back_z=1.8):
        for x in range(1, 9, 2):
            face.vline(x, 1, 3, k("P", 1))
