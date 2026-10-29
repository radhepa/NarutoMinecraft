"""Academy Shorts: a pupil's loose navy knee shorts turned up in a sand cuff, a sea-blue drawstring
at the waist, bare shins and open-toe sandals."""
from kit import leg_ring
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Academy Shorts", "gender": "unisex",
        "description": "Loose navy knee shorts with sand turn-ups and a sea-blue drawstring, sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 18621, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    body.front.set(3, 10, "A3"), body.front.set(4, 10, "A3"), body.front.set(4, 11, "A2")
    fabric(body.bottom, "D", "twill", 18621, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 18622 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 18622, 2)
    for ring in leg_ring(g, "cuff", 4.0, "S", 3, (5, 1, 5), "weave", inflate=.12):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "S3")
    sandals(g)
