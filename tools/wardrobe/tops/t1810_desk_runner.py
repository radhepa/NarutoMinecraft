"""Desk Runner: the messenger who runs scrolls between the mission desk and the field, a short-sleeved
navy shirt with a sand-piped placket over mesh forearms, a leather satchel strap across the chest and
a scroll case on the back."""
from kit_nara import net
from kit_umino import scroll
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Desk Runner",
    "gender": "unisex",
    "description": "Short-sleeved navy shirt piped in sand over mesh forearms, a satchel strap and a scroll case.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 18581, 2)
    cap(body, "D", seed=18581)
    f = body.front
    f.set(3, 0, None), f.set(4, 0, None)
    f.vline(3, 1, 4, "S3"), f.vline(4, 1, 4, "S2")
    f.set(4, 2, "M3")
    body.strip.hline(0, body.strip.w - 1, 11, "D1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 18582 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "D", "weave", 18582, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "S3")
        net(arm.strip, 0, 6, arm.strip.w - 1, 10)
    strap = g.piece("strap", "TORSO", (-.5, -7.5, -.5), (1, 15, 1), pivot=(0, 5.0, -2.45), rotation=(0, 0, -36))
    solid(strap, "L", "leather", 18584, 2, edge=False)
    back = g.piece("strap_back", "TORSO", (-.5, -7.5, -.5), (1, 15, 1), pivot=(0, 5.0, 2.45), rotation=(0, 0, 36))
    solid(back, "L", "leather", 18585, 2, edge=False)
    case = g.piece("scroll_case", "TORSO", (-1, -3, -1), (2, 7, 2), pivot=(.6, 4.6, 3.3), rotation=(0, 0, 36))
    solid(case, "L", "leather", 18586, 2)
    for face in case.sides:
        face.hline(0, face.w - 1, 0, "A2")
    scroll(g, "spare_scroll", (2.6, 9.6, -2.8), (0, 0, 90), length=4)
