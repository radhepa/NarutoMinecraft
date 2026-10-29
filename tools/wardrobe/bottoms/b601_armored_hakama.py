"""Armored Hakama: wide pleated hakama trousers in the robe's cloth, lacquered thigh plates (haidate)
strapped over them, the hems tied in above white shin wraps and open-toe sandals."""
from kit_akimichi import lames
from kit_shinobi import sandals, wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Armored Hakama", "gender": "unisex",
        "description": "Wide pleated hakama, lacquered thigh plates, hems tied above white wraps, sandals.",
        "tags": ["shinobi", "akimichi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 6931, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 6931, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 6932 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 6932, 2)
        for x in range(0, leg.strip.w, 2):
            leg.strip.vline(x, 1, 6, "D1")
    wraps(g, 7, 9)
    sandals(g)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        # The wide legs flare out over the knee and are tied in below it.
        flare = g.piece(f"{side}_flare", bone, (-2.5, 3.0, -2.5), (5, 4, 5), inflate=.25)
        solid(flare, "D", "twill", 6934, 2)
        for face in flare.sides:
            for x in range(0, face.w, 2):
                face.vline(x, 0, 3, "D1")
            face.hline(0, face.w - 1, 3, "D0")
        haidate = g.piece(f"{side}_haidate", bone, (-2.5, .2, -2.8), (5, 3, 1), inflate=.15)
        solid(haidate, "P", "smooth", 6936, 2, edge=False)
        haidate.front.hline(0, 4, 0, "P3"), haidate.front.hline(0, 4, 2, "P1")
        for x in (1, 3):
            haidate.front.set(x, 1, "A2")
    belt = g.piece("waist_himo", "TORSO", (-4.5, 9.4, -2.5), (9, 1, 5), inflate=.2)
    solid(belt, "S", "weave", 6938, 3, edge=False)
