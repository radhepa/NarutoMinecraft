"""Toolbelt Trousers: straight indigo shinobi trousers bloused over cream shin wraps, a carpenter's
leather tool belt slung on the hips with nail pouches, a chisel and a mallet, and black jika-tabi."""
from kit import waistband
from kit_kinoshita import tabi, tool_belt
from kit_shinobi import wraps
from paint import fabric, solid, strip_fabric

META = {"name": "Toolbelt Trousers", "gender": "unisex",
        "description": "Indigo trousers over cream shin wraps, a leather tool belt with pouches and a mallet, jika-tabi.",
        "tags": ["shinobi", "kinoshita", "work"]}


def build(g):
    waistband(g, "D", "twill", 22661)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 22662 + (side == "left"), 2, 0, 5)
        fabric(leg.top, "D", "twill", 22662, 2)
    wraps(g, top=6, bottom=8)
    tabi(g, top=9)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        puff = g.piece(f"{side}_blouse", bone, (-2.5, 4.6, -2.5), (5, 2, 5))
        solid(puff, "D", "twill", 22664, 2)
        for face in puff.sides:
            face.hline(0, face.w - 1, 0, "D3")
    tool_belt(g, "waist_tool_belt", y=9.6)
