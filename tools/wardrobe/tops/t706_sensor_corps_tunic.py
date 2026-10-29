"""Sensor Corps Tunic: the sensing unit's dark fitted tunic, long-sleeved with a high collar, aqua
piping traced down the front like the lines of a barrier map, a single lavender shoulder guard and
a chest strap carrying an aqua sensor stone."""
from kit import arm_x, collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Sensor Corps Tunic",
    "gender": "unisex",
    "description": "Dark high-collared tunic with aqua piping, one shoulder guard, a chest strap with a sensor stone.",
    "tags": ["shinobi", "yamanaka", "sensor"],
}

# Piping on the front: two lines that branch from the collar and step down to the hem.
PIPING = [(2, 0), (2, 1), (2, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11),
          (5, 0), (5, 1), (5, 2), (6, 3), (6, 4), (6, 5), (6, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 7650, 2)
    cap(body, "P", texture="twill", seed=7650)
    for x, y in PIPING:
        body.front.set(x, y, "A2")
    body.back.vline(3, 0, 11, "A1"), body.back.vline(4, 0, 11, "A2")
    strip_fabric(jacket, "P", "twill", 7651, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "A2"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 7652 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "twill", 7652, 3)
        strip_fabric(arm, "K", "smooth", 7654, 2, 11, 11)
        strip_fabric(sleeve, "P", "twill", 7655, 2, 8, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "A2")
    guard = g.piece("shoulder_guard", "LEFT_ARM", (arm_x("left") - .4, -2.4, -2.4), (5, 3, 5), rotation=(0, 0, -10))
    solid(guard, "S", "smooth", 7656, 2)
    for face in guard.sides:
        face.hline(0, face.w - 1, 2, "A2")
    strap = g.piece("chest_strap", "TORSO", (-.5, -6.5, -.5), (1, 13, 1), pivot=(0, 5.0, -2.35), rotation=(0, 0, 40))
    solid(strap, "K", "leather", 7657, 2)
    stone = g.piece("sensor_stone", "TORSO", (-1, -1, -1), (2, 2, 1), pivot=(0, 5.0, -2.95))
    solid(stone, "M", "plain", 7658, 3)
    stone.front.fill("A3"), stone.front.set(0, 0, "A4")
    neck = collar(g, "collar", "P", "twill", height=2, y=-1.6)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A2")
