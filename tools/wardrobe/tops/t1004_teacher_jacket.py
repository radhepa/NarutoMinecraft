"""Teacher Jacket: Shino as the Academy's homeroom teacher, a slate jacket worn open over a dark
shirt, its collar turned up behind the neck but open at the front, so the face shows."""
from kit_aburame import high_collar
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Teacher Jacket",
    "gender": "unisex",
    "description": "Open slate jacket over a dark shirt, collar turned up behind the neck.",
    "tags": ["shinobi", "aburame", "coat"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "smooth", 10591, 3)
    cap(body, "K", seed=10591, base=3)
    body.front.hline(2, 5, 0, "K1")
    strip_fabric(jacket, "P", "smooth", 10592, 2)
    cap(jacket, "P", seed=10592)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, k("P", 3)), f.set(6, y, k("P", 1))
    f.hline(0, 1, 7, "P1"), f.hline(6, 7, 7, "P1")
    for face in jacket.sides:
        face.hline(0, face.w - 1, 11, "P1")
    jacket.back.vline(4, 1, 10, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 10593, 2, 0, 11)
        fabric(arm.top, "P", "smooth", 10593, 3)
        strip_fabric(sleeve, "P", "smooth", 10594 + (side == "left"), 2, 0, 10)
        fabric(sleeve.top, "P", "smooth", 10594, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "A2")
    high_collar(g, "P", "smooth", 10600, cover_mouth=False, back_top=-3.4, flare=6)
    for name, x in (("lapel_right", -3.6), ("lapel_left", 2.6)):
        lapel = g.piece(name, "TORSO", (0, 0, 0), (1, 11, 1), pivot=(x, 0, -2.75))
        solid(lapel, "P", "smooth", 10605, 2)
        lapel.front.vline(0, 0, 10, k("A", 2))
