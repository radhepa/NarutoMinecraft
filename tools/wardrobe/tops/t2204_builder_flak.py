"""Builder's Flak Vest: the Konoha flak vest of a field engineer over an indigo shirt with the sleeves
rolled up, a leather tool belt with nail pouches and a mallet slung low on the hips, and a pull saw
hung from the vest's right shoulder."""
from kit import roll
from kit_kinoshita import saw, tool_belt
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Builder's Flak Vest",
    "gender": "unisex",
    "description": "Konoha flak vest over a rolled-sleeve indigo shirt, a tool belt with pouches and a mallet.",
    "tags": ["shinobi", "kinoshita", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 22361, 2)
    cap(body, "D", seed=22361)
    flak_vest(g, seed=22362)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 22363 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "D", "weave", 22363, 3)
    roll(g, "D", 4.0)
    tool_belt(g, "tool_belt", y=10.2)
    saw(g, "saw", (-3.6, 1.0, 2.7), (0, 0, 14), length=10)
