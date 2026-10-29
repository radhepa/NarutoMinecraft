"""Shopkeeper's Cardigan: the older shopkeeper's knitted cardigan over a collared shirt, buttoned
halfway, two patch pockets sagging with keys and receipts, the cuffs turned back."""
from kit_market import pocket, sleeves
from paint import cap, k, strip_fabric

META = {
    "name": "Shopkeeper's Cardigan",
    "gender": "unisex",
    "description": "Knitted cardigan buttoned halfway over a collared shirt, two sagging pockets, turned-back cuffs.",
    "tags": ["civilian", "casual", "jacket"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 36360, 3)
    cap(body, "S", seed=36360, base=3)
    body.front.set(2, 0, "S4"), body.front.set(5, 0, "S4"), body.front.set(3, 1, "S1"), body.front.set(4, 1, "S1")
    strip_fabric(jacket, "P", "knit", 36361, 2)
    jacket.top.fill(k("P", 3))
    for y in range(0, 5):
        for x in range(3 - min(y, 1), 5 + min(y, 1)):
            jacket.front.clear(x, y)
    for y in range(12):
        jacket.front.set(3 if y >= 4 else 2, y, k("P", 3))
    for y in (5, 7, 9):
        jacket.front.set(4, y, "M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 36362, 3, 0, 9)
    sleeves(g, "P", "knit", 36363, rows=(0, 9), cuff=k("P", 3))
    for i, x in enumerate((-2.2, 2.2)):
        p = pocket(g, f"pocket_{i}", "P", (x, 7.6, -2.6), size=(3, 3), seed=36365 + i, base=2)
        p.front.hline(0, 2, 0, k("P", 3))
