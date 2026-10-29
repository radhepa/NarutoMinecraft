"""Wave Skirt: a navy wrap skirt to the calf over dark leggings, its hem printed with a band of
sea-blue waves and a sand stripe, the overlap at the front, with open-toe sandals."""
from kit import flaps
from kit_shinobi import sandals
from kit_umino import waves
from paint import fabric, strip_fabric

META = {"name": "Wave Skirt", "gender": "female",
        "description": "Calf-length navy wrap skirt hemmed with sea-blue waves and a sand stripe, leggings, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 18641, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "weave", 18641, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 18642 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "K", "smooth", 18642, 2)
    sandals(g)
    front, back = flaps(g, "skirt", 9, "D", "weave", 18643, hem="S3", top=11.2)
    for face in (front, back):
        waves(face, 5, "A3")
    front.vline(6, 1, 7, "D0")
    for name, x in (("right", -5.0), ("left", 4.0)):
        panel = g.piece(f"skirt_{name}", "TORSO", (0, 0, -2), (1, 9, 4), pivot=(x, 11.2, 0))
        strip_fabric(panel, "D", "weave", 18644, 2)
        fabric(panel.top, "D", "weave", 18644, 3), fabric(panel.bottom, "D", "weave", 18644, 1)
        for face in panel.sides:
            waves(face, 5, "A3")
        panel.strip.hline(0, panel.strip.w - 1, 8, "S3")
