"""Scale Vest: a short sleeveless vest of small lacquered scales laced at the sides, over a
long-sleeved dark shirt, the vest's edges bound in the accent: a jonin's close-guard armor."""
from kit import sleeves
from paint import cap, strip_fabric

META = {
    "name": "Scale Vest",
    "gender": "unisex",
    "description": "Short vest of lacquered scales bound in the accent over a dark long-sleeved shirt.",
    "tags": ["shinobi", "jonin", "armor", "vest"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "plain", 33360, 2)
    cap(body, "K", seed=33360)
    sleeves(g, "K", "plain", 33361, rows=(0, 10), cuff="K1")
    for y in range(9):
        for x in range(jacket.strip.w):
            jacket.strip.set(x, y, "P3" if (x + (y % 2)) % 2 == 0 and y % 2 == 0 else ("P1" if y % 2 else "P2"))
    jacket.top.fill("P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 0, "A2"), jacket.strip.hline(0, jacket.strip.w - 1, 8, "A2")
    for y in range(9):
        jacket.front.set(3, y, "A2"), jacket.front.set(4, y, "A1")
    for face in (jacket.right, jacket.left):
        for y in range(1, 8, 2):
            face.set(1, y, "L3"), face.set(2, y, "L1")
