"""Scout Cuirass: light armor for the clan's young scouts. A short laced breastplate over a cream
kimono shirt with elbow sleeves, dark fingerless gloves to the forearm and a navy sash."""
from kit import belt
from kit_senju import lames
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Scout Cuirass",
    "gender": "unisex",
    "description": "Short laced breastplate over a cream kimono shirt, elbow sleeves, dark gloves, navy sash.",
    "tags": ["shinobi", "senju", "armor"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 1620, 2)
    cap(body, "S", seed=1620)
    strip_fabric(jacket, "P", "smooth", 1621, 2, 1, 6)
    lames(jacket.strip, "P", 1, 6, step=3, lace="A2")
    jacket.front.clear(3, 1), jacket.front.clear(4, 1)
    # Shoulder straps holding the plate up.
    for x in (1, 6):
        jacket.front.set(x, 0, "K2")
    for x in (1, 6):
        jacket.back.set(x, 0, "K2")
    fabric(jacket.top, "K", "leather", 1622, 2, 1, 0, 1, 4), fabric(jacket.top, "K", "leather", 1622, 2, 6, 0, 1, 4)
    sash = belt(g, "sash", y=8.4, role="D", height=2, buckle=None, inflate=.1)
    sash.front.set(2, 1, "D1")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 1623, 2, 0, 4)
        fabric(arm.top, "S", "weave", 1623, 3)
        strip_fabric(sleeve, "S", "weave", 1624, 2, 0, 4)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "S1")
        strip_fabric(arm, "K", "leather", 1625, 2, 7, 11)
        arm.strip.hline(0, arm.strip.w - 1, 7, "K3")
    edge = g.piece("plate_rim", "TORSO", (-4, 0, -1), (8, 1, 1), pivot=(0, .9, -2.3))
    solid(edge, "P", "smooth", 1626, 3, edge=False)
