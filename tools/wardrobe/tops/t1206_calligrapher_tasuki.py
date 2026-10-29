"""Calligrapher's Kosode: a plain kosode with its long sleeves tied back by a tasuki cord crossed over
the back, so the cuffs stay clear of the ink. Ink stains the right cuff, and a lacquered brush case
hangs at the hip."""
from kit import belt
from kit_kurama import wrap_front
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Calligrapher's Kosode",
    "gender": "unisex",
    "description": "Kosode with the sleeves tied back by a crossed tasuki cord, ink-stained cuff, brush case at the hip.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 12725, 2)
    cap(body, "P", seed=12725)
    wrap_front(body.front, "S3", "P1", rows=7, start=1)
    body.front.set(0, 0, "S3")
    belt(g, "obi", y=8.0, role="D", height=2, buckle=None, inflate=.12)
    # The tasuki: a cord in an X across the back and over each shoulder.
    for i in range(9):
        jacket.back.set(i - 0, i + 1, "A2"), jacket.back.set(7 - i, i + 1, "A2")
    jacket.top.hline(0, 7, 1, "A2")
    jacket.front.set(0, 0, "A2"), jacket.front.set(7, 0, "A2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 12726, 2, 0, 6)
        fabric(arm.top, "P", "weave", 12726, 3)
        # The sleeve gathered up into a puff above the elbow by the cord.
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        ox = -3.0 if side == "right" else -1.0
        puff = g.piece(f"{side}_gathered_sleeve", bone, (ox - .6, -2.2, -2.6), (5, 6, 5), inflate=.12)
        solid(puff, "P", "weave", 12727 + (side == "left"), 2)
        for face in puff.sides:
            for x in range(0, face.w, 2):
                face.vline(x, 1, 4, "P1")
            face.hline(0, face.w - 1, 5, "S3")
            face.hline(0, face.w - 1, 2, "A2")
        if side == "right":
            for x in range(arm.strip.w):
                if (x * 7) % 3:
                    arm.strip.set(x, 6, "K2")
            arm.front.set(1, 7, "K1")
    case = g.piece("brush_case", "TORSO", (-.5, 0, -.5), (1, 6, 1), pivot=(3.6, 8.6, -2.4), rotation=(0, 0, -14),
                   motion="sway")
    solid(case, "K", "smooth", 12730, 3)
    for face in case.sides:
        face.set(0, 0, "A2"), face.set(0, 5, "M3")
