"""Straw Rain Coat: a mino of layered straw-colored thatch over the shoulders and down the back past
the hips, tied at the chest with cord, over a long-sleeved work shirt with leather hand guards: the
oldest rain gear on the road, still worn by mountain shinobi."""
from kit import arm_bone, arm_x, sleeves
from paint import fabric, k, rnd, solid, strip_fabric

META = {
    "name": "Straw Rain Coat",
    "gender": "unisex",
    "description": "Layered straw-colored thatch coat over the shoulders and back, cord ties, leather hand guards.",
    "tags": ["shinobi", "cloak", "coat", "jonin"],
    "covers_waist": True,
}


def thatch(face, seed, tier=3, base=2):
    """Shingled straw: fine vertical strands, each tier staggered by a texel and ending in a dark
    ragged fringe over the tier below."""
    for y in range(face.h):
        t = y // tier
        for x in range(face.w):
            c = (x + t) % 4
            s = base + (1 if c == 0 else -1 if c == 3 else 0)
            if t == 0 and y == 0 and c != 3:
                s = base + 1
            if y % tier == tier - 1:
                s = base - 1 if (x + t) % 2 else base - 2
                if rnd(x, y, seed) < .2:
                    s = base
            face.set(x, y, k("P", s))


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 35070, 2)
    fabric(body.top, "D", "weave", 35070, 3)
    body.front.vline(3, 0, 11, "D1")
    sleeves(g, "D", "weave", 35071, 2, rows=(0, 9))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "L", "leather", 35072, 2, 8, 10)
        arm.strip.hline(0, arm.strip.w - 1, 8, "L3")
        drape = g.piece(f"{side}_thatch", arm_bone(side), (arm_x(side) - .6, -2.6, -2.6), (5, 5, 5))
        solid(drape, "P", "plain", 35073, 2)
        for face in drape.sides:
            thatch(face, 35074 + (side == "left"))
        drape.top.fill("P3")
    yoke = g.piece("thatch_yoke", "TORSO", (-5, -1, -3), (10, 4, 6))
    solid(yoke, "P", "plain", 35076, 2)
    for face in yoke.sides:
        thatch(face, 35076)
    fabric(yoke.top, "P", "weave", 35076, 3)
    back = g.piece("thatch_back", "TORSO", (-5, 0, 0), (10, 15, 1), pivot=(0, 2.0, 2.6), motion="flap_back")
    solid(back, "P", "plain", 35077, 2)
    thatch(back.back, 35077)
    thatch(back.front, 35078)
    for side, x in (("right", -3.4), ("left", 3.4)):
        panel = g.piece(f"thatch_front_{side}", "TORSO", (-1.5, 0, 0), (3, 10, 1), pivot=(x, 2.0, -3.0), motion="flap_front")
        solid(panel, "P", "plain", 35079, 2)
        thatch(panel.front, 35079 + (x > 0))
        thatch(panel.back, 35079)
    tie = g.piece("chest_cord", "TORSO", (-2, 0, 0), (4, 1, 1), pivot=(0, 2.4, -3.2))
    for face in tie.faces:
        face.fill("L1")
