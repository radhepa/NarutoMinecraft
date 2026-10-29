"""Shogi Sweater: a slouchy knit sweater, sleeves shoved up past the elbow, with a band knitted
like a shogi board round the hem and a single shogi piece knitted on the chest."""
from paint import cap, fabric, grid, k, strip_fabric

META = {
    "name": "Shogi Sweater",
    "gender": "unisex",
    "description": "Slouchy knit sweater with a shogi-board band at the hem and a shogi piece on the chest.",
    "tags": ["shinobi", "nara"],
}

PIECE = [".s.",
         "sss",
         "sss"]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "rib", 5571, 2)
    cap(body, "P", texture="rib", seed=5571)
    strip_fabric(jacket, "P", "rib", 5572, 2, 0, 1)
    jacket.strip.hline(0, jacket.strip.w - 1, 1, "P1")
    # The board: a cream band ruled into squares by dark lines, then a ribbed hem.
    for face in body.sides:
        for y in (8, 9, 10):
            for x in range(face.w):
                face.set(x, y, "K1" if x % 3 == 0 or y == 8 else "S2")
        face.hline(0, face.w - 1, 11, "P1")
    grid(body.front, 4, 3, PIECE, {"s": "S3"})
    body.front.set(5, 5, "K2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "rib", 5573 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "P", "rib", 5573, 3)
        strip_fabric(sleeve, "P", "rib", 5575, 2, 4, 6)
        for x in range(sleeve.strip.w):
            sleeve.strip.set(x, 5, k("P", 3 if x % 2 else 1))
