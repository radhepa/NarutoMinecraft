"""Scout Mantle: a lookout's short cream mantle over a fitted dark shirt, falling over the
shoulders to the chest, its hood down at the back and its front closed with a lavender toggle."""
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Scout Mantle",
    "gender": "unisex",
    "description": "Short cream hooded mantle over the shoulders, a fitted dark shirt, a lavender toggle.",
    "tags": ["shinobi", "hyuga", "mantle"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "plain", 4801, 2)
    cap(body, "D", texture="plain", seed=4801)
    body.front.vline(2, 5, 10, "D1"), body.front.vline(5, 6, 10, "D3")
    body.front.vline(4, 5, 11, "D1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "plain", 4802, 2, 0, 10)
        fabric(arm.top, "D", "plain", 4802, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    # The mantle: a cape round the chest and back, and a capelet over each shoulder.
    cape = g.piece("mantle", "TORSO", (-4.5, 0, -2.5), (9, 5, 5), pivot=(0, -.2, 0), inflate=.3)
    solid(cape, "P", "velvet", 4803, 2)
    fabric(cape.top, "P", "velvet", 4803, 3)
    for face in cape.sides:
        face.hline(0, face.w - 1, 4, "A2")
    cape.front.vline(4, 0, 4, "P1")
    cape.bottom.fill("P0")
    for side, bone, x in (("right", "RIGHT_ARM", -3.6), ("left", "LEFT_ARM", -.4)):
        cap_ = g.piece(f"{side}_capelet", bone, (x, -2.4, -2.6), (4, 4, 5), inflate=.3)
        solid(cap_, "P", "velvet", 4805 + (side == "left"), 2)
        for face in cap_.sides:
            face.hline(0, face.w - 1, 3, "A2")
        cap_.bottom.fill("P0")
    toggle = g.piece("toggle", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 2.0, -3.0))
    solid(toggle, "A", "plain", 4807, 3, edge=False)
    hood = g.piece("hood", "TORSO", (-4, 0, -1), (8, 3, 2), pivot=(0, -1.0, 3.2), rotation=(20, 0, 0))
    solid(hood, "P", "velvet", 4808, 2)
    fabric(hood.top, "A", "plain", 4809, 1)
    hood.top.hline(0, 7, 0, "P3")
