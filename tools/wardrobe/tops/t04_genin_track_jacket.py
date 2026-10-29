"""Genin Track Jacket: the loud orange zip-up of a genin who wants to be noticed: navy across the
shoulders, a white stand-up collar, an elastic hem and the red swirl on the back."""
from glyphs import SWIRL, stamp
from kit import collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Genin Track Jacket",
    "gender": "unisex",
    "description": "Orange zip-up with navy shoulders, white collar and the red swirl on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 81, 2)
    cap(body, "K", seed=81)
    # Navy yoke over the shoulders, dipping lower on the back.
    strip_fabric(body, "K", "plain", 82, 2, 0, 1)
    body.back.hline(0, 7, 2, "K2")
    # Zip down the front and a fold either side of it.
    f = body.front
    f.vline(4, 2, 11, "S3"), f.vline(3, 2, 11, "P1")
    f.set(4, 2, "M4"), f.set(4, 3, "M2")
    f.vline(1, 4, 9, "P1"), f.vline(6, 5, 9, "P3")
    # Loose elastic hem on the jacket layer.
    strip_fabric(jacket, "P", "plain", 83, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "plain", 84 + (side == "left"), 2, 0, 10)
        strip_fabric(arm, "K", "plain", 86, 2, 0, 2)
        fabric(arm.top, "K", "plain", 86, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "P1")
        # Slightly baggy forearm folds on the sleeve layer.
        strip_fabric(sleeve, "P", "plain", 87, 2, 8, 10)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 10, "K2")
    back = g.piece("back_swirl", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, 2.6, 2.05), scale=(.5, .5, .5))
    fabric(back.back, "P", "plain", 88, 2)
    stamp(back.back, SWIRL, 0, 0, {"#": "A2"})
    for face in (back.top, back.bottom, back.right, back.left, back.front):
        face.fill("P2")
    neck = collar(g, "collar", "S", height=2, y=-1.6)
    neck.front.vline(4, 0, 1, "M2"), neck.front.set(3, 1, "S1")
    pull = g.piece("zip_pull", "TORSO", (0, 0, -1), (1, 2, 1), pivot=(.1, 1.2, -2.05), scale=(.5, .5, .5))
    solid(pull, "M", "plain", 89, 3, edge=False)
