"""Armored Hakama: dark hakama trousers under a skirt of laced tassets that hang from the waist, plate
shin guards strapped over the shins and dark sandals: the lower half of the clan's war armor."""
from kit_senju import lames, plate
from kit_shinobi import sandals
from paint import fabric, k, strip_fabric

META = {"name": "Armored Hakama", "gender": "unisex",
        "description": "Dark hakama trousers, laced plate tassets at the waist, plate shin guards, dark sandals.",
        "tags": ["shinobi", "hakama", "armor"], "rejects": ["formal"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 1700, 2, 9, 11)
    fabric(body.bottom, "D", "weave", 1700, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "weave", 1701 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "weave", 1701, 2)
        # Loose pleats on the overlay down to the shin.
        strip_fabric(pants, "D", "weave", 1703, 2, 0, 4)
        for x in range(0, pants.strip.w, 3):
            pants.strip.vline(x, 1, 4, "D1")
        # Shin guards: laced plates from below the knee to the ankle.
        strip_fabric(pants, "P", "smooth", 1704, 2, 5, 9)
        lames(pants.strip, "P", 5, 9, step=5, lace=None)
        for x in range(1, pants.strip.w, 4):
            pants.strip.set(x, 7, "M3")
        pants.strip.hline(0, pants.strip.w - 1, 9, "K2")
    sandals(g)
    # Tassets (kusazuri): four laced plates round the hips. Long coats hide them ("waist").
    for name, pivot, size, rz in (("waist_tasset_front", (0, 10.2, -2.8), (8, 5, 1), 0),
                                  ("waist_tasset_back", (0, 10.2, 2.0), (8, 5, 1), 0),
                                  ("waist_tasset_right", (-4.7, 10.2, -.2), (1, 5, 4), 6),
                                  ("waist_tasset_left", (4.7, 10.2, -.2), (1, 5, 4), -6)):
        w, h, d = size
        plate(g, name, "TORSO", (-w / 2, 0, -d / 2 + (.5 if d == 1 else 0)), size, "P", 1705 + rz,
              pivot=pivot, rotation=(0, 0, rz), step=3, lace="A2")
    belt = g.piece("waist_cord", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.6, 0), inflate=.35)
    for face in belt.faces:
        face.fill(k("A", 2))
