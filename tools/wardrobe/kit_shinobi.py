"""Shinobi building blocks shared by bottoms: open-toe sandals and bandage wraps."""
from paint import strip_fabric


def sandals(g):
    """Open-toe shinobi sandals: navy straps and heel, toes showing at the front."""
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "smooth", 41, 2, 10, 11)
        leg.front.set(1, 11, None), leg.front.set(2, 11, None)
        leg.front.hline(0, 3, 10, "D3")
        leg.bottom.fill("K1")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "K1")
        pants.front.set(1, 11, None), pants.front.set(2, 11, None)
        pants.bottom.fill("K0")


def wraps(g, top: int = 6, bottom: int = 9):
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for y in range(top, bottom + 1):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, "S2" if (x + y * 2) % 5 == 0 else "S3")
