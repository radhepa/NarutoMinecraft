"""Wrap Skirt: a short skirt wrapped and tied at the hip over chain-mesh shorts, mesh down to the knee,
and open-toe sandals: the kunoichi student's field skirt."""
from kit import flaps
from kit_academy import holster, waist
from kit_shinobi import mesh, sandals
from paint import k, solid

META = {"name": "Wrap Skirt", "gender": "female",
        "description": "Short wrap skirt tied at the hip over mesh shorts to the knee, open-toe sandals.",
        "tags": ["shinobi", "genin", "skirt"]}


def build(g):
    waist(g, "P", "weave", 31655)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        mesh(leg.strip, 0, 0, leg.strip.w - 1, 5, "K2")
        mesh(leg.top, 0, 0, leg.top.w - 1, leg.top.h - 1, "K2")
        leg.strip.hline(0, leg.strip.w - 1, 5, "K1")
    sandals(g)
    front, back = flaps(g, "skirt", 4, "P", "weave", 31656, hem=k("A", 2), top=11.0, front_z=-2.95, back_z=1.95)
    front.vline(5, 0, 3, "A2"), front.vline(6, 0, 3, "P1")
    tie = g.piece("skirt_tie", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(1.4, 10.6, -3.1), rotation=(0, 0, -10),
                  motion="flap_front")
    solid(tie, "A", "weave", 31658, 2)
    holster(g, 31659, y=3.6, strap="K")
