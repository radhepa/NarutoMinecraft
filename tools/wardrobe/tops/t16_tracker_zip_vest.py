"""Tracker Zip Vest: a padded sleeveless khaki vest zipped up to a high collar, rust trim, ribbed black
arm warmers and a satchel slung from the left shoulder to the right hip: the genin who reads the trail."""
from kit import collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Tracker Zip Vest",
    "gender": "unisex",
    "description": "Padded sleeveless zip vest with a high collar, black arm warmers and a slung satchel.",
    "tags": ["shinobi", "genin"],
}

SLING = dict(pivot=(0, 5.0, -2.55), rotation=(0, 0, -36))


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 311, 2)
    cap(body, "P", seed=311)
    # Padding stitched in horizontal channels, puffed just below each seam.
    for y in (3, 6, 9):
        body.strip.hline(0, body.strip.w - 1, y, "P1")
        body.strip.hline(0, body.strip.w - 1, y + 1, "P3")
    f = body.front
    f.vline(4, 0, 11, "M3"), f.vline(3, 0, 11, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "A1")
    for face in (body.right, body.left):
        face.hline(0, face.w - 1, 0, "A2")
    # Bare upper arms, ribbed black warmers from the elbow down with a rust band at the top.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "rib", 312, 2, 5, 10)
        strip_fabric(sleeve, "K", "rib", 313, 2, 4, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "A2")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "K1")
    neck = collar(g, "collar", "P", "plain", height=2, y=-1.6)
    neck.front.vline(4, 0, 1, "M3"), neck.front.set(4, 0, "M4")
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A3")
    pull = g.piece("zip_pull", "TORSO", (0, 0, -1), (1, 2, 1), pivot=(.1, 1.0, -2.05), scale=(.5, .5, .5))
    solid(pull, "M", "plain", 314, 3, edge=False)
    # The satchel strap across the chest and the satchel riding on the right hip.
    strap = g.piece("sling", "TORSO", (-.5, -7, -.5), (1, 14, 1), **SLING)
    solid(strap, "L", "leather", 315, 2, edge=False)
    bag = g.piece("satchel", "TORSO", (-1.5, 0, -1), (3, 3, 2), pivot=(-3.0, 8.6, -3.1))
    solid(bag, "L", "leather", 316, 2)
    bag.front.hline(0, 2, 0, "L3"), bag.front.hline(0, 2, 1, "L1")
    bag.front.set(1, 1, "M3")
