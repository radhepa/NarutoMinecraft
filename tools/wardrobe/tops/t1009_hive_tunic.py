"""Hive Tunic: a sleeveless tunic quilted in a honeycomb of cells, a low standing collar that leaves
the face open, a moss sash and dark wraps from the elbow to the knuckles."""
from kit import belt, collar
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Hive Tunic",
    "gender": "unisex",
    "description": "Sleeveless honeycomb-quilted tunic, low standing collar, sash and dark arm wraps.",
    "tags": ["shinobi", "aburame"],
}


def comb(face, seed, base=2):
    """Honeycomb cells: rows of cells three texels tall, each row's walls offset from the last."""
    fabric(face, "P", "plain", seed, base)
    for y in range(face.h):
        row = y // 3
        for x in range(face.w):
            if y % 3 == 2:
                face.set(x, y, k("P", base - 1))
            elif (x + row * 2) % 4 == 0:
                face.set(x, y, k("P", base - 1))
            elif y % 3 == 0 and (x + row * 2) % 4 == 2:
                face.set(x, y, k("P", base + 1))


def build(g):
    body = g.part("body")
    for face in body.sides:
        comb(face, 10681 + face.x0)
    cap(body, "P", seed=10681)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for face in arm.sides:
            for y in range(5, 12):
                for x in range(face.w):
                    face.set(x, y, "D0" if (x + y) % 3 == 0 else "D1")
        arm.strip.hline(0, arm.strip.w - 1, 5, "A2")
    neck = collar(g, "collar", "P", "plain", height=2, y=-1.6)
    neck.front.hline(3, 5, 0, "P0"), neck.front.set(4, 1, "P0")
    sash = belt(g, "sash", y=8.8, role="A", height=2, buckle=None)
    sash.front.vline(2, 0, 1, "A1")
