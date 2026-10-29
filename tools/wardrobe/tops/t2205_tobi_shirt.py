"""Tobi Shirt: the high-collared work shirt of the scaffold crews, closed down the front with a row
of brass hook clasps, the long sleeves shoved up to the forearm and bunched there, and a twisted
cream towel slung round the neck with its ends hanging down the chest."""
from kit import collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Tobi Shirt",
    "gender": "unisex",
    "description": "High-collared work shirt with brass hook clasps, shoved-up sleeves and a towel round the neck.",
    "tags": ["shinobi", "kinoshita", "work"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 22381, 2)
    cap(body, "P", texture="twill", seed=22381)
    f = body.front
    f.vline(4, 0, 11, "P1")
    for y in range(1, 11, 2):
        f.set(3, y, "M3")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    c = collar(g, "stand_collar", "P", "twill", height=2, y=-1.4)
    c.front.vline(4, 0, 1, "P0")
    # The towel: twisted round the neck, both ends down the chest.
    towel = g.piece("towel", "TORSO", (-4.5, 0, -2.6), (9, 1, 5), pivot=(0, .3, 0), inflate=.16)
    for face in towel.faces:
        face.paint(lambda x, y, cur: "S4" if x % 2 else "S3")
    for i, (x, rz) in enumerate(((-1.8, 6), (1.8, -6))):
        end = g.piece(f"towel_end_{i}", "TORSO", (-.5, 0, -.5), (1, 5, 1), pivot=(x, 1.2, -2.8), rotation=(0, 0, rz))
        solid(end, "S", "weave", 22382 + i, 3)
        end.front.hline(0, 0, 3, "D2")
    # Sleeves shoved up and bunched below the elbow over bare forearms.
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 22384 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "P", "twill", 22384, 3)
        for i, (y, h) in enumerate(((4.6, 1), (5.6, 1))):
            bunch = g.piece(f"{side}_bunch_{i}", bone, (ox - .45 - i * .1, y, -2.45 - i * .1), (5, h, 5))
            solid(bunch, "P", "twill", 22386 + i, 3 - i, edge=False)
