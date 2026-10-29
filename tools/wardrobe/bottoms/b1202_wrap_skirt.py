"""Painter's Wrap Skirt: the light wrap skirt from Yakumo's training days, to mid-thigh over chain-mesh
shorts and leggings to the knee, tied at the hip, with open-toe sandals."""
from kit import flaps, side_panels
from kit_shinobi import mesh, sandals
from paint import fabric, solid, strip_fabric

META = {"name": "Painter's Wrap Skirt", "gender": "female",
        "description": "Light wrap skirt to mid-thigh over mesh leggings to the knee, tied at the hip, sandals.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 12870, 2, 9, 11)
    fabric(body.bottom, "S", "weave", 12870, 1)
    body.strip.hline(0, body.strip.w - 1, 9, "S3")
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 12871, 2, 0, 1)
        fabric(leg.top, "K", "plain", 12871, 2)
        mesh(leg.strip, 0, 2, leg.strip.w - 1, 6, "K2")
        leg.strip.hline(0, leg.strip.w - 1, 6, "K1")
    for face in flaps(g, "skirt", 5, "S", "weave", 12872, width=9, hem="S1", top=11.6, front_z=-2.7, back_z=1.7):
        face.vline(6, 1, 4, "S1")
    side_panels(g, "skirt_side", 5, "S", "weave", hem="S1", top=11.6)
    tie = g.piece("hip_tie", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(3.0, 11.2, -2.9), motion="sway")
    solid(tie, "A", "weave", 12873, 2)
    sandals(g)
