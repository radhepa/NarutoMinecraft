"""Elder's Chanchanko: the grandparent's padded sleeveless vest over a plain kimono, warm quilted
cotton with a soft dark collar band, worn sitting at the shop front all winter."""
from kit_kurama import wrap_front
from kit_market import sleeves
from paint import cap, k, strip_fabric

META = {
    "name": "Elder's Chanchanko",
    "gender": "unisex",
    "description": "Padded sleeveless vest with a dark collar band over a plain long-sleeved kimono.",
    "tags": ["civilian", "vest", "kimono", "wrap"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 36500, 2)
    cap(body, "S", seed=36500)
    wrap_front(body.front, "S4", "S1", rows=8, start=2)
    sleeves(g, "S", "weave", 36501, rows=(0, 10), overlay=False)
    strip_fabric(jacket, "A", "quilt", 36502, 2, 0, 10)
    jacket.top.fill(k("A", 3))
    for y in range(11):
        for x in (3, 4):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "K3"), jacket.front.set(5, y, "K3")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "A", "quilt", 36503, 2, 0, 2)
        sleeve.top.fill(k("A", 3))
