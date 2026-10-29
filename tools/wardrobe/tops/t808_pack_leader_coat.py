"""Pack Leader Coat: a long dark coat to the knee with broad fur lapels, fur-trimmed cuffs, a leather
belt over the waist and the skirts split for running, a red fang on the back between the shoulders."""
from kit import belt, flaps, sleeves
from kit_inuzuka import fang, fur_box, fur_edge
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Pack Leader Coat",
    "gender": "unisex",
    "description": "Long dark coat with fur lapels and cuffs, belted, split skirts, a red fang on the back.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 8660, 3)
    cap(body, "S", seed=8660)
    strip_fabric(jacket, "P", "twill", 8661, 2)
    fabric(jacket.top, "P", "twill", 8661, 3)
    f = jacket.front
    for y in range(8):
        f.set(3, y, None), f.set(4, y, None)
    f.vline(2, 0, 11, "P0"), f.vline(5, 0, 11, "P0")
    fang(jacket.back, 4, 2, "A2", h=3)
    for arm in sleeves(g, "P", "twill", 8662, 2, rows=(0, 9)):
        arm.strip.hline(0, arm.strip.w - 1, 5, "P1")
    for side, bone, x in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        cuff = g.piece(f"{side}_fur_cuff", bone, (x - .5, 8.2, -2.5), (5, 2, 5))
        fur_box(cuff, "S", 8663 + (side == "left"), 2)
    # Broad fur lapels down the opening and a fur collar standing round the neck.
    for side, x in (("right", -2.4), ("left", 1.4)):
        lapel = g.piece(f"fur_lapel_{side}", "TORSO", (0, 0, 0), (1, 8, 1), pivot=(x, -.4, -3.1), inflate=.15)
        fur_box(lapel, "S", 8665 + (side == "left"), 2)
    collar = g.piece("fur_collar", "TORSO", (-5, -1.6, -2.4), (10, 2, 5), inflate=.1)
    fur_box(collar, "S", 8667, 2)
    belt(g, "belt", y=8.6, role="L", buckle="M", inflate=.2)
    front, back = flaps(g, "coat", 8, "P", "twill", 8668, width=9, hem="P1", top=11.0, front_z=-2.85, back_z=1.85, slit=True)
    for face in (front, back):
        fur_edge(face, 6, "S", 8669, 2, 2)
