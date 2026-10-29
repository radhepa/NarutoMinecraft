"""Senior Vest: the jonin flak vest over a navy long-sleeved shirt, a long sand scarf with a sea-blue
stripe looped once round the neck and hanging down the front, the sleeves taped at the wrist."""
from kit_shinobi import flak_vest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Senior Vest",
    "gender": "unisex",
    "description": "Jonin flak vest over a navy shirt, a long sand scarf with a sea-blue stripe, taped wrists.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 18541, 2)
    cap(body, "D", seed=18541)
    flak_vest(g, seed=18542)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 18543 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "weave", 18543, 3)
        for y in (9, 10):
            arm.strip.hline(0, arm.strip.w - 1, y, "S3" if y == 9 else "S2")
    ring = g.piece("scarf", "TORSO", (-4.5, -1.6, -2.6), (9, 2, 5), inflate=.2)
    solid(ring, "S", "weave", 18545, 3, edge=False)
    for face in ring.sides:
        face.hline(0, face.w - 1, 1, "A2")
    for i, (x, length) in enumerate(((-2.2, 7), (-1.0, 5))):
        tail = g.piece(f"scarf_tail_{i}", "TORSO", (-.5, 0, -.5), (1, length, 1), pivot=(x, .4, -3.0), rotation=(0, 0, 4 - i * 6),
                       motion="sway")
        solid(tail, "S", "weave", 18546 + i, 3)
        for face in tail.sides:
            face.hline(0, face.w - 1, length - 2, "A2")
