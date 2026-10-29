"""ANBU Cloak: a long dusk-grey travelling cloak over the ANBU armor, draped over both shoulders,
clasped at the throat and open down the front so the plates show, falling to the knee behind."""
from kit import arm_bone, arm_x
from kit_shinobi import anbu_arms, anbu_plates
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "ANBU Cloak",
    "gender": "unisex",
    "description": "Long grey cloak over the plated armor: shoulder drapes, a clasp, open front, knee-length back.",
    "tags": ["shinobi", "armor", "cloak"],
}

LENGTH = 18   # from the shoulders to the knee


def cloth(face, seed, folds=3, base=2):
    """Cloak cloth: soft vertical folds, a light top edge and a dark hem."""
    fabric(face, "L", "twill", seed, base)
    for x in range(1, face.w - 1, folds):
        face.vline(x, 1, face.h - 1, k("L", base - 1))
    face.hline(0, face.w - 1, 0, k("L", base + 1))
    face.hline(0, face.w - 1, face.h - 1, k("L", base - 1))


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 151, 2)
    cap(body, "D", seed=151)
    anbu_plates(g)
    anbu_arms(g, tattoo=False)
    # Shoulder drapes ride on the arms so they swing with them.
    for side in ("right", "left"):
        drape = g.piece(f"{side}_drape", arm_bone(side), (arm_x(side) - .5, -2.5, -2.5), (5, 6, 5))
        solid(drape, "L", "twill", 181 + (side == "left"), 2)
        for face in drape.sides:
            cloth(face, 183 + (side == "left"))
    # Yoke over the shoulders and the clasp at the throat.
    yoke = g.piece("yoke", "TORSO", (-4.5, -.6, -2.6), (9, 3, 5))
    solid(yoke, "L", "twill", 185, 2)
    for face in yoke.sides:
        face.hline(0, face.w - 1, 0, "L3")
    yoke.front.vline(4, 0, 2, "L0")
    yoke.front.set(3, 1, "M3"), yoke.front.set(5, 1, "M3"), yoke.front.set(4, 1, "M4")
    # The long back panel follows the stride.
    back = g.piece("cape_back", "TORSO", (-5, 0, 0), (10, LENGTH, 1), pivot=(0, 1.6, 2.5), motion="flap_back")
    solid(back, "L", "twill", 186, 2)
    cloth(back.back, 187)
    # Open front: one narrow panel on each side of the chest.
    for side, x in (("right", -3.1), ("left", 3.1)):
        panel = g.piece(f"cape_front_{side}", "TORSO", (-1.5, 0, -.5), (3, LENGTH - 2, 1), pivot=(x, 2.2, -2.75),
                        motion="flap_front")
        solid(panel, "L", "twill", 188 + (x > 0), 2)
        cloth(panel.front, 190 + (x > 0))
