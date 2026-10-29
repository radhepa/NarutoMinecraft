"""Danzo Robe: Danzo Shimura as a council elder: an off-white high-collared kosode under a long
grey robe draped over the right shoulder, so the right arm is hidden inside it, crossing the chest
to pass under the left arm and falling to the knee; the bare white left sleeve holds a plain cane."""
from kit import collar, flaps
from kit_shimura import cane
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Danzo Robe",
    "gender": "unisex",
    "description": "Grey robe draped over the right shoulder hiding the arm, an off-white high collar and sleeve, a cane.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 13500, 2)
    cap(body, "S", seed=13500)
    # The robe: grey everywhere but the white kosode showing over the left breast, above the
    # diagonal edge that runs from the right shoulder down under the left arm.
    strip_fabric(jacket, "P", "twill", 13501, 2)
    cap(jacket, "P", texture="twill", seed=13501)
    f = jacket.front
    for y in range(7):
        for x in range(8):
            if x > 2 + y:
                f.clear(x, y)
        edge = 2 + y
        if edge <= 7:
            f.set(edge, y, "P3")
            if edge - 1 >= 0:
                f.set(edge - 1, y, "P1")
    for y in range(3):
        jacket.left.clear(0, y), jacket.left.clear(1, y)
    jacket.top.rect(4, 0, 4, 4, None)
    # Folds where the robe hangs from the hidden right shoulder.
    for x in (1, 5):
        jacket.back.vline(x, 2, 11, "P1")
    # The right arm is wrapped inside the robe: a draped sleeve with no hand showing.
    drape = g.piece("right_drape", "RIGHT_ARM", (-3.6, -2.6, -2.6), (5, 13, 5))
    solid(drape, "P", "twill", 13502, 2)
    for face in drape.sides:
        face.vline(1, 2, 12, "P1"), face.vline(3, 4, 12, "P1")
        face.hline(0, face.w - 1, 12, "P0")
    fabric(drape.top, "P", "twill", 13503, 3)
    # The left arm: the kosode's white sleeve to the wrist.
    arm = g.part("left_arm")
    strip_fabric(arm, "S", "weave", 13504, 2, 0, 9)
    fabric(arm.top, "S", "weave", 13504, 3)
    arm.strip.hline(0, arm.strip.w - 1, 9, "S1")
    sleeve = g.part("left_sleeve")
    strip_fabric(sleeve, "S", "weave", 13505, 2, 0, 8)
    fabric(sleeve.top, "S", "weave", 13505, 3)
    sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "S1")
    # The high standing collar of the kosode.
    neck = collar(g, "collar", "S", "weave", height=2, y=-1.7, inflate=.1)
    neck.front.vline(4, 0, 1, "S1")
    # The robe's length to the knee, front and back.
    for face in flaps(g, "robe", 7, "P", "twill", 13506, width=9, top=11.0, front_z=-2.85, back_z=1.85):
        face.vline(2, 1, 6, "P1"), face.vline(6, 1, 6, "P1")
        face.hline(0, face.w - 1, 6, "P1")
    cane(g)
