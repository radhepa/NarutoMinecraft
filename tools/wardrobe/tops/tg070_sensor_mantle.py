"""Sensor Mantle: the sensor corps' hooded mantle, a short cape over the shoulders with the deep
hood thrown back, clasped at the throat with a metal disc, over a quiet long-sleeved tunic belted
at the waist: the shinobi who feels chakra across the valley before anyone sees a thing."""
from kit import belt
from kit_aburame import hood_down
from kit_specialist import shirt
from paint import k, solid

META = {
    "name": "Sensor Mantle",
    "gender": "unisex",
    "description": "Short hooded mantle over the shoulders with a metal clasp, hood down, over a belted tunic.",
    "tags": ["shinobi", "mantle", "chunin"],
}


def build(g):
    body = shirt(g, "S", "weave", 34180, cuff="S1")
    body.front.vline(4, 1, 11, "S1")
    belt(g, "tunic_belt", y=9.2, height=2)
    mantle = g.piece("mantle", "TORSO", (-8.6, -.5, -3.0), (17, 5, 6), inflate=.12)
    solid(mantle, "P", "twill", 34182, 2)
    mantle.top.fill("P3")
    for face in mantle.sides:
        face.hline(0, face.w - 1, 0, "P3")
        for x in range(1, face.w, 3):
            face.vline(x, 1, face.h - 2, "P1")
        face.hline(0, face.w - 1, face.h - 1, "A2")
    mantle.bottom.fill(k("P", 0))
    front = g.piece("mantle_front", "TORSO", (-3, 0, 0), (6, 3, 1), pivot=(0, 4.4, -3.15))
    solid(front, "P", "twill", 34183, 2)
    front.front.vline(2, 0, 2, "P0"), front.front.vline(3, 0, 2, "P0")
    front.front.hline(0, 5, 2, "A2")
    clasp = g.piece("mantle_clasp", "TORSO", (-1, -1, 0), (2, 2, 1), pivot=(0, .6, -3.4))
    solid(clasp, "M", "plain", 34184, 3, edge=False)
    clasp.front.set(0, 0, "M4")
    hood_down(g, "P", "twill", 34185)
