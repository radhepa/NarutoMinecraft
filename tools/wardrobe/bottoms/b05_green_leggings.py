"""Green Leggings: the bodysuit's green legs, bright orange leg warmers bunched over the shins and
navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Green Leggings", "gender": "unisex",
        "description": "Green leggings, orange leg warmers bunched over the shins, navy sandals.",
        "tags": ["shinobi", "taijutsu"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 211, 2, 9, 11)
    fabric(body.bottom, "P", "plain", 211, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "plain", 212 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "P", "plain", 212, 2)
        leg.front.vline(1 if side == "right" else 2, 0, 4, "P1")
        # Leg warmers: knitted orange from below the knee to the ankle.
        strip_fabric(leg, "L", "rib", 214, 3, 6, 9)
        leg.strip.hline(0, leg.strip.w - 1, 9, "L1")
    sandals(g)
    # The warmers' bunched top and their bunching at the ankle.
    for ring in leg_ring(g, "warmer_top", 5.6, "L", 3, size=(5, 2, 5), texture="rib", inflate=.1):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "L4")
    leg_ring(g, "warmer_fold", 8.2, "L", 2, size=(5, 1, 5), texture="rib", inflate=.08)
