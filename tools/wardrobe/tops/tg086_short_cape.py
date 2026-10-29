"""Shoulder Cape: a short weathered capelet buttoned across the collarbone, its back falling to the
shoulder blades, over a sleeveless pale tunic belted with rope; bare arms with dark leather arm
guards from elbow to wrist. Light enough to run in."""
from kit import arm_bone, arm_x, neckline
from kit_rugged import cape, rope
from paint import fabric, solid, strip_fabric

META = {
    "name": "Shoulder Cape",
    "gender": "unisex",
    "description": "Short weathered capelet over a sleeveless pale tunic, a rope belt, dark leather arm guards.",
    "tags": ["shinobi", "cloak", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 35060, 2, 0, 10)
    fabric(body.top, "S", "weave", 35060, 3)
    neckline(body.front, "laced", "S")
    body.strip.hline(0, body.strip.w - 1, 10, "S1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "leather", 35061, 3, 5, 10)
        arm.strip.hline(0, arm.strip.w - 1, 5, "K4")
        guard = g.piece(f"{side}_arm_guard", arm_bone(side), (arm_x(side) - .3, 4.6, -2.3), (4, 4, 4), inflate=.1)
        solid(guard, "K", "leather", 35062 + (side == "left"), 3)
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, "K4"), face.set(1, 2, "M3")
    rope(g, "rope_belt", y=9.6, role="L")
    yoke = g.piece("capelet", "TORSO", (-5, -.8, -3), (10, 4, 6))
    solid(yoke, "P", "twill", 35064, 2)
    for face in yoke.sides:
        face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 3, "P1")
    fabric(yoke.top, "P", "twill", 35064, 3)
    yoke.front.vline(4, 0, 3, "P0"), yoke.front.set(4, 1, "M3"), yoke.front.set(5, 1, "M2")
    for side, x in (("right", -5.6), ("left", 5.6)):
        drape = g.piece(f"{side}_drape", "TORSO", (-1, 0, -3), (2, 5, 6), pivot=(x, -.6, 0),
                        rotation=(0, 0, -10 if x < 0 else 10))
        solid(drape, "P", "twill", 35065 + (x > 0), 2)
        for face in drape.sides:
            face.hline(0, face.w - 1, 0, "P3")
    cape(g, "cape_back", 10, 7, 2.4, "P", seed=35067, z=3.0, tear=True)
