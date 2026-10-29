"""Ceremonial Kimono: the formal kimono of a clan rite, pale and wrapped, with long swinging
sleeves edged in the accent colour, a wide obi bound with a cord and the clan crest at the back."""
from kit_hyuga import crest, kimono_sleeves, obi, wrap_front
from paint import cap, solid, strip_fabric

META = {
    "name": "Ceremonial Kimono",
    "gender": "unisex",
    "description": "Formal pale wrap kimono, long swinging sleeves, a corded obi, the clan crest on the back.",
    "tags": ["hyuga", "wrap", "kimono"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 4821, 3)
    cap(body, "P", texture="velvet", seed=4821, base=3)
    wrap_front(body.front, role="P", trim="A2", rows=6, start=2)
    body.front.set(1, 0, "A2"), body.front.set(1, 1, "S4")
    sash = obi(g, "obi", "A", y=6.6, height=3, knot="back", accent="M3", seed=4823)
    crest(g, "back_crest", "P", "A2", pivot=(0, 1.2, 2.05), seed=4825)
    sleeves = kimono_sleeves(g, "sleeve", "P", "velvet", 4826, top=2.6, length=8, trim="A2", depth=5, hand_rows=10)
    for box in sleeves:
        for face in box.sides:
            face.hline(0, face.w - 1, 6, "A1")
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "S", "velvet", 4831, 3)
    for face in collar.sides:
        face.hline(0, face.w - 1, 0, "A2")
