"""Dyer's Trousers: pale undyed work trousers rolled at the shin, stained blue from the vats
creeping up from the ankle, bare feet in wooden geta."""
from kit_kurama import splatter
from kit_market import geta, rolled_cuffs
from paint import fabric, k, strip_fabric

META = {"name": "Dyer's Trousers", "gender": "unisex",
        "description": "Pale undyed work trousers rolled at the shin, stained indigo from the ankle, wooden geta.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36710, 2, 9, 11)
    fabric(body.bottom, "S", "weave", 36710, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "S", "weave", 36711 + (side == "left"), 2, 0, 6)
        fabric(leg.top, "S", "weave", 36711, 2)
        for y in range(3, 7):
            for x in range(leg.strip.w):
                if y >= 5 or (x * 3 + y) % 4 == 0:
                    leg.strip.set(x, y, k("D", 2 if y < 6 else 1))
        splatter(leg.strip, 36713 + (side == "left"), keys=(k("D", 2), k("D", 3)), density=.07, rows=range(0, 3))
        leg.strip.hline(0, leg.strip.w - 1, 9, k("D", 1))
    for ring in rolled_cuffs(g, "cuff", 6.0, "S", 36715):
        for face in ring.sides:
            face.hline(0, face.w - 1, 1, k("D", 2))
    geta(g)
