"""Long Split Skirt: a long skirt to the ankle, split up both sides to the hip for movement, over
close trousers, bandaged ankles and open-toe sandals."""
from kit import belt
from kit_shinobi import sandals, wraps
from paint import fabric, k, solid, strip_fabric

META = {"name": "Long Split Skirt", "gender": "unisex",
        "description": "Ankle-length skirt split up both sides over close trousers, bandaged ankles, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 34680, 2, 9, 11)
    fabric(body.bottom, "P", "twill", 34680, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 34681, 2, 0, 7)
        fabric(leg.top, "D", "twill", 34681, 2)
    wraps(g, 8, 9)
    sandals(g)
    belt(g, "waist_band", y=9.0, role="P", height=1, buckle=None, inflate=.15)
    for name, z, motion, face in (("waist_skirt_front", -2.9, "flap_front", "front"),
                                  ("waist_skirt_back", 1.9, "flap_back", "back")):
        panel = g.piece(name, "TORSO", (-4.5, 0, 0), (9, 12, 1), pivot=(0, 10.0, z), motion=motion)
        solid(panel, "P", "twill", 34683 + (z > 0), 2)
        f = getattr(panel, face)
        f.hline(0, 8, 0, k("P", 3))
        f.vline(0, 1, 11, k("P", 1)), f.vline(8, 1, 11, k("P", 1))
        for x in (2, 6):
            f.vline(x, 2, 10, k("P", 1))
        f.hline(0, 8, 11, k("A", 2))
