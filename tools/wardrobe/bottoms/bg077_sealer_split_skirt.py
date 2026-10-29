"""Sealer Split Skirt: a long dark wrap skirt split up the side, its hem sewn with a row of paper
seal tags, over close trousers and open-toe sandals."""
from kit import belt
from kit_shinobi import sandals
from kit_specialist import seal_trim
from paint import fabric, k, solid, strip_fabric

META = {"name": "Sealer Split Skirt", "gender": "unisex",
        "description": "Long dark wrap skirt split at the side, seal tags round the hem, close trousers, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 34720, 2, 9, 11)
    fabric(body.bottom, "K", "twill", 34720, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34721, 2, 0, 9)
        fabric(leg.top, "D", "twill", 34721, 2)
    sandals(g)
    belt(g, "waist_obi", y=9.0, role="A", height=1, buckle=None, inflate=.15)
    for name, z, motion, face in (("waist_skirt_front", -2.9, "flap_front", "front"),
                                  ("waist_skirt_back", 1.9, "flap_back", "back")):
        panel = g.piece(name, "TORSO", (-4.5, 0, 0), (9, 11, 1), pivot=(0, 10.0, z), motion=motion)
        solid(panel, "K", "twill", 34723 + (z > 0), 2)
        f = getattr(panel, face)
        f.hline(0, 8, 0, k("K", 3))
        f.vline(6, 1, 10, k("K", 0))
        seal_trim(panel.strip, 8, 3, every=3, seed=34726)
    side = g.piece("waist_skirt_left", "TORSO", (0, 0, -2), (1, 10, 4), pivot=(4.0, 10.0, 0))
    solid(side, "K", "twill", 34727, 2)
