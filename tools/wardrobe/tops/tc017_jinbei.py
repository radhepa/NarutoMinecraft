"""Jinbei: the summer house-and-stall top, loose kasuri cotton with short split sleeves, the front
panels tied at the side with paired cords, worn open and easy in the heat."""
from kit_market import kasuri, sleeves
from paint import cap, k, strip_fabric

META = {
    "name": "Jinbei",
    "gender": "unisex",
    "description": "Loose kasuri-print summer top with short split sleeves, the front tied at the side with cords.",
    "tags": ["civilian", "casual", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36340, 2)
    cap(body, "P", seed=36340)
    for face in body.sides:
        kasuri(face, k("S", 2), 36341 + face.x0)
    f = body.front
    for y in range(6):
        x = min(6, 2 + y)
        f.set(x, y, k("P", 4))
    f.hline(0, 1, 0, k("P", 4))
    f.vline(6, 6, 11, k("P", 4))
    # The cord ties at the side: two pairs of short dark cords.
    for y in (5, 8):
        f.set(7, y, k("K", 3)), f.set(7, y + 1, k("K", 2)), body.left.set(0, y, k("K", 3))
    sleeves(g, "P", "weave", 36342, rows=(0, 3))
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        kasuri(sleeve.strip, k("S", 2), 36344, rows=range(0, 3))
        # The split under the arm, a gap of shade where the sleeve opens.
        sleeve.front.set(0 if side == "right" else 3, 3, None)
        sleeve.back.set(3 if side == "right" else 0, 3, None)
