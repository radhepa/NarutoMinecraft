"""Wrap Work Skirt: a short koshimaki wrap skirt tied over monpe for the market stall, keeping the
trousers clean, the trousers gathered at the ankle over straw sandals."""
from kit import flaps
from kit_market import checks, gathered_ankles, straw_sandals
from paint import fabric, k, strip_fabric

META = {"name": "Wrap Work Skirt", "gender": "unisex",
        "description": "Short checked wrap skirt tied over monpe gathered at the ankle, straw sandals.",
        "tags": ["civilian", "skirt", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "A", "weave", 36740, 2, 9, 11)
    fabric(body.bottom, "A", "weave", 36740, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "weave", 36741 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "weave", 36741, 2)
    for face in flaps(g, "wrap", 5, "A", "weave", 36743, width=9, hem=k("A", 1), top=11.2, front_z=-2.9, back_z=1.9):
        checks(face, k("A", 3), 2, rows=range(1, 4))
    gathered_ankles(g, "ankle", "D", 36745, y=8.0)
    straw_sandals(g)
