"""Rolled Work Trousers: sturdy trousers rolled to mid-calf for kneeling at the easel, flecked with
paint, a rag tucked at the waist, bare shins and open-toe sandals."""
from kit import leg_ring
from kit_kurama import splatter
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Rolled Work Trousers", "gender": "unisex",
        "description": "Sturdy trousers rolled to mid-calf, flecked with paint, a rag at the waist, sandals.",
        "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 12910, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D1")
    fabric(body.bottom, "D", "twill", 12910, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 12911 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "D", "twill", 12911, 2)
        leg.front.vline(1 if side == "right" else 2, 1, 6, "D3")
        splatter(leg.strip, 12913 + (side == "left"), keys=("A2", "S3", "P2"), density=.05, rows=range(0, 6))
    for ring in leg_ring(g, "roll", 5.6, "D", 3, (5, 2, 5), "twill"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "D4"), face.hline(0, face.w - 1, 1, "D2")
    rag = g.piece("waist_rag", "TORSO", (-.5, 0, -.5), (1, 3, 2), pivot=(-3.6, 10.0, -1.2), motion="sway")
    solid(rag, "S", "weave", 12915, 3)
    rag.right.set(0, 1, "A2"), rag.right.set(1, 2, "D3")
    sandals(g)
