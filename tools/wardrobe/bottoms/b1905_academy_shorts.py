"""Academy Shorts: a student's loose knee shorts with turned-up cream cuffs, white bandage wraps on
the shins for taijutsu class and navy open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals, wraps
from paint import fabric, k, strip_fabric

META = {"name": "Academy Shorts", "gender": "unisex",
        "description": "Loose knee shorts with turned-up cream cuffs, bandaged shins, sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 19750, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 19750, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 19751 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 19751, 2)
    for ring in leg_ring(g, "cuff", 4.0, "S", 3, (5, 2, 5), "weave", inflate=.12):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k("S", 4)), face.hline(0, face.w - 1, 1, k("S", 2))
    wraps(g, top=6, bottom=9)
    sandals(g)
