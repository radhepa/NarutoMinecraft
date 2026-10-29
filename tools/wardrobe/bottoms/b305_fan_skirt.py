"""Fan Skirt: a short wrap skirt over dark mesh-hemmed shorts, a white thigh wrap and holster on the
right leg and navy sandals."""
from kit import flaps
from kit_shinobi import sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Fan Skirt", "gender": "female",
        "description": "Short wrap skirt over dark shorts, white thigh wrap with a holster, navy sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 3982, 2, 9, 11)
    fabric(body.bottom, "K", "plain", 3982, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 3983 + (side == "left"), 2, 0, 2)
        fabric(leg.top, "K", "plain", 3983, 2)
        leg.strip.hline(0, leg.strip.w - 1, 2, "K1")
    sandals(g)
    for face in flaps(g, "skirt", 4, "D", "weave", 3985, width=9, hem="D1", top=10.4, front_z=-2.8, back_z=1.8):
        face.vline(6, 1, 3, "D1")
    for name, x in (("right", -5.0), ("left", 4.0)):
        panel = g.piece(f"skirt_{name}", "TORSO", (0, 0, -2), (1, 4, 4), pivot=(x, 10.4, 0))
        solid(panel, "D", "weave", 3987, 2)
    wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.4, 3.4, -2.4), (5, 2, 5))
    solid(wrap, "S", "weave", 3988, 3, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 1, "S2")
    holster = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, 3.2, -1.0))
    solid(holster, "K", "leather", 3989, 3)
    holster.right.set(0, 0, "M3"), holster.right.set(1, 0, "M2")
