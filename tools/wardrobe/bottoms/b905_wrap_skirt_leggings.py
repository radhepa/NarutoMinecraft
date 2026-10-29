"""Wrap Skirt Leggings: a kunoichi's field wear. A short wrapped skirt crossing at the left hip over
close dark leggings to mid-shin, bandaged ankles and navy open-toe sandals."""
from kit import flaps
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "Wrap Skirt Leggings", "gender": "female",
        "description": "Short wrapped skirt over dark leggings to mid-shin, bandaged ankles, navy sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 9640, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "P3")
    fabric(body.bottom, "P", "weave", 9640, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 9641 + (side == "left"), 2, 0, 7)
        fabric(leg.top, "K", "plain", 9641, 2)
        leg.strip.hline(0, leg.strip.w - 1, 7, "K3")
        for y in (8, 9):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, "S2" if (x + y) % 3 == 0 else "S3")
    sandals(g)
    front, back = flaps(g, "skirt", 4, "P", "weave", 9643, width=9, hem="A2", top=10.8, front_z=-2.8, back_z=1.8)
    for y in range(4):
        front.set(5 + y // 2, y, "P1")
    front.vline(6, 0, 3, "P3")
