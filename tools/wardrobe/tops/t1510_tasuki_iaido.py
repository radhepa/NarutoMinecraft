"""Tasuki Iaido: a dark kimono top for the quick-draw, the sleeves tied back with a tasuki cord
crossed in an X over the back, the collar edged in silver, a sash with the katana at the left hip."""
from kit import belt
from kit_gekko import hip_katana
from paint import cap, fabric, strip_fabric

META = {
    "name": "Tasuki Iaido",
    "gender": "unisex",
    "description": "Dark kimono top, sleeves tied back by a cord crossed over the back, a katana at the left hip.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 15800, 2)
    cap(body, "P", seed=15800)
    f = body.front
    for i in range(8):
        x = 1 + i
        if x <= 7:
            f.set(x, i, "S3")
            if x + 1 <= 7:
                f.set(x + 1, i, "P1")
    f.set(0, 0, "S3")
    # The tasuki: an X across the back, its ends looping over each shoulder to the armpit.
    b = body.back
    for i in range(9):
        b.set(round(i * 7 / 8), i, "A2"), b.set(7 - round(i * 7 / 8), i, "A2")
    for face in (body.right, body.left):
        face.vline(1, 0, 3, "A2")
    body.top.hline(0, 7, 1, "A3"), body.top.hline(0, 7, 2, "A2")
    belt(g, "sash", y=8.8, role="D", buckle=None, height=2, inflate=.12)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        # Sleeves gathered up above the elbow by the cord.
        strip_fabric(arm, "P", "weave", 15802 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 15802, 3)
        arm.strip.hline(0, arm.strip.w - 1, 3, "A2")
        arm.strip.hline(0, arm.strip.w - 1, 4, "P1")
    hip_katana(g, side="left")
