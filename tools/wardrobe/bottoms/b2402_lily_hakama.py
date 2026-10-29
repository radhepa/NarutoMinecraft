"""Lily Hakama: full pleated hakama in the house colour, flaring wide to the ankle, the hem trimmed
with a running line of white bells on green stems, tied with white himo at the waist."""
from kit import belt, flaps, leg_ring, legs
from kit_suzuran import bell_hem
from paint import fabric, strip_fabric

META = {"name": "Lily Hakama", "gender": "unisex",
        "description": "Full pleated hakama flaring to the ankle, a bell-trimmed hem, white himo at the waist.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 24711, 2, 9, 11)
    fabric(body.bottom, "P", "weave", 24711, 1)
    for leg in legs(g, "P", "weave", 24712, 2, rows=(0, 11), crease=False):
        for face in leg.sides:
            face.vline(1, 0, 11, "P1")
        leg.bottom.fill("K1")
    for ring in leg_ring(g, "flare", 6, "P", base=2, size=(5, 6, 5), inflate=.1):
        for face in ring.sides:
            for x in range(0, face.w, 2):
                face.vline(x, 0, 2, "P1")
            bell_hem(face, 3, step=3, start=1)
    for face in flaps(g, "pleat", 3, "P", "weave", 24713, top=11.6):
        face.vline(2, 1, 2, "P1"), face.vline(6, 1, 2, "P1")
    belt(g, "waist_himo", y=9.0, role="S", height=1, buckle=None, inflate=.15)
