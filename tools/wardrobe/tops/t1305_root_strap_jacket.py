"""Root Strap Jacket: the Foundation's field wear, after Torune and Fu: a black bodysuit with long
sleeves into black gloves, a short dark jacket cropped at the ribs, and the dark-red straps every
Root member wears over both shoulders, crossed by a steel-ringed belt."""
from kit import belt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Root Strap Jacket",
    "gender": "unisex",
    "description": "Black bodysuit and gloves, a short dark jacket, dark-red straps over both shoulders, a ringed belt.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "smooth", 13580, 2)
    cap(body, "K", texture="smooth", seed=13580)
    strip_fabric(jacket, "P", "weave", 13581, 2, 0, 6)
    fabric(jacket.top, "P", "weave", 13581, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 6, "P0")
    jacket.front.vline(4, 1, 6, "P1")
    # The red straps: down the front and back over each shoulder.
    for face in (jacket.front, jacket.back):
        for x in (1, 6):
            face.vline(x, 0, 6, "A2")
            face.set(x, 6, "A1")
    for x in (1, 6):
        jacket.top.vline(x, 0, 3, "A3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "smooth", 13582, 2)
        fabric(arm.top, "K", "smooth", 13582, 3)
        fabric(arm.bottom, "K", "smooth", 13582, 1)
        strip_fabric(sleeve, "P", "weave", 13583 + (side == "left"), 2, 0, 3)
        fabric(sleeve.top, "P", "weave", 13583, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P0")
        arm.strip.hline(0, arm.strip.w - 1, 8, "K3")
    belt(g, "belt", y=9.2, role="K", buckle=None, height=1, inflate=.12)
    ring = g.piece("belt_ring", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(0, 9.7, -2.95))
    solid(ring, "M", "plain", 13585, 3, edge=False)
    ring.front.set(0, 0, "M4")
