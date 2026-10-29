"""Interrogation Shirt: the slate uniform shirt with the sleeves rolled to the elbow for the work
of the room, black braces over the shoulders, black gloves and the oxblood force band."""
from kit import roll
from kit_morino import armband, gloves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Interrogation Shirt",
    "gender": "unisex",
    "description": "Slate shirt with sleeves rolled to the elbow, black braces, black gloves, oxblood force band.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 17311, 2)
    cap(body, "S", seed=17311)
    body.front.vline(3, 1, 11, "S1"), body.front.set(3, 0, "S0"), body.front.set(4, 0, "S0")
    for y in (3, 6, 9):
        body.front.set(4, y, "S4")
    # Braces: two black straps over each shoulder, crossed at the back.
    for x in (1, 6):
        body.front.vline(x, 0, 10, "K2")
    from paint import line
    line(body.back, 1, 0, 6, 10, "K2"), line(body.back, 6, 0, 1, 10, "K2")
    body.top.vline(1, 0, 3, "K2"), body.top.vline(6, 0, 3, "K2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 17312 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "S", "weave", 17312, 3)
    roll(g, "S", 4.6)
    gloves(g, top=9)
    armband(g, "left", y=1.4)
