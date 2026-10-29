"""Green Jumpsuit: the taijutsu specialist's skin-tight green bodysuit with a zip up the front, the
forehead protector worn as a red belt with its steel plate at the front, and bandaged hands."""
from glyphs import LEAF, stamp
from kit import belt
from paint import cap, fabric, strip_fabric

META = {
    "name": "Green Jumpsuit",
    "gender": "unisex",
    "description": "Tight green bodysuit, the forehead protector as a red belt, bandaged hands.",
    "tags": ["shinobi", "taijutsu"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 201, 2)
    cap(body, "P", texture="plain", seed=201)
    f = body.front
    f.vline(4, 0, 8, "P1"), f.set(4, 0, "M3")
    # Soft shading down the sides of the chest.
    f.vline(1, 2, 8, "P3"), f.vline(6, 2, 8, "P1")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "plain", 202 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "P", "plain", 202, 3)
        # Bandaged hands, wound in diagonal turns.
        for y in (10, 11):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "S2" if (x + y) % 3 == 0 else "S3")
        fabric(arm.bottom, "S", "plain", 204, 2)
    # The protector as a belt: red cloth with the leaf plate over the navel.
    belt(g, "protector_belt", y=8.6, role="A", height=1, buckle=None, inflate=.12)
    plate = g.piece("belt_plate", "TORSO", (-9, -4, -1), (18, 8, 2), pivot=(0, 9.1, -2.75), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", 205, 2)
    pf = plate.front
    fabric(pf, "M", "plain", 206, 3)
    pf.hline(0, 17, 0, "M4"), pf.hline(0, 17, 7, "M1")
    pf.vline(0, 0, 7, "M2"), pf.vline(17, 0, 7, "M1")
    for x in (2, 15):
        pf.set(x, 2, "M1"), pf.set(x, 5, "M1")
    stamp(pf, LEAF, 5, 0, {"#": "M0"})
