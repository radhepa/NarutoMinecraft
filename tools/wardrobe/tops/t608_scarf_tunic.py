"""Scarf Tunic: a warm wrap tunic with a contrasting hem, a long white muffler wound twice round the
neck with one end thrown back over the shoulder, a broad belt with two snack pouches and rolled
sleeves."""
from kit import belt, roll
from kit_akimichi import snack_pouch
from paint import fabric, solid, strip_fabric

META = {
    "name": "Scarf Tunic",
    "gender": "unisex",
    "description": "Wrap tunic, a long white muffler with one end over the shoulder, belt with snack pouches.",
    "tags": ["shinobi", "genin", "akimichi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "velvet", 6856, 2)
    fabric(body.top, "P", "velvet", 6856, 3)
    # The wrap: a contrasting edge from the right shoulder down to the left hip, side seams.
    for y in range(9):
        x = min(7, 1 + (y * 2) // 3)
        body.front.set(x, y, "A2"), body.front.set(min(7, x + 1), y, "P0")
    for face in (body.right, body.left):
        face.vline(face.w // 2, 2, 10, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "A2"), body.strip.hline(0, body.strip.w - 1, 10, "A3")
    # The muffler: two wound turns and the long end over the right shoulder down the back.
    for i, (y, inflate) in enumerate(((-1.6, .3), (-.2, .4))):
        turn = g.piece(f"muffler_{i}", "TORSO", (-4.5, y, -2.6), (9, 2, 5), inflate=inflate)
        solid(turn, "S", "knit", 6857 + i, 3, edge=False)
        for face in turn.sides:
            face.hline(0, face.w - 1, 1, "S2")
    end = g.piece("muffler_end", "TORSO", (-1, 0, 0), (3, 9, 1), pivot=(-2.4, -.4, 2.4), rotation=(8, 0, 4), motion="sway")
    solid(end, "S", "knit", 6859, 3)
    for face in end.sides:
        face.hline(0, face.w - 1, end.h - 2, "A2"), face.hline(0, face.w - 1, end.h - 1, "S2")
    front = g.piece("muffler_front", "TORSO", (-1, 0, -1), (2, 7, 1), pivot=(2.4, 1.0, -2.7), rotation=(0, 0, -6),
                    motion="sway")
    solid(front, "S", "knit", 6860, 3)
    for face in front.sides:
        face.hline(0, face.w - 1, front.h - 2, "A2")
    belt(g, "belt", y=8.6, role="L", height=2, inflate=.3)
    for i, x in enumerate((-2.8, 2.8)):
        snack_pouch(g, f"snack_{i}", (x, 10.2, -3.0), role="A" if i else "S", size=(2, 2, 1), seed=6861 + i)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "velvet", 6863 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "P", "velvet", 6863, 3)
    roll(g, "P", 5.2, base=2, accent="A2")
