"""Onbu Carrier: a parent at the market or the well with the baby on their back, a plain
round-necked smock with rolled sleeves and the cloth carrier's straps crossing the chest, the
little one bundled behind in a quilted wrap with only a knitted bonnet showing."""
from kit_household import arm_cloth
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Onbu Carrier",
    "gender": "unisex",
    "description": "Round-necked smock with rolled sleeves, carrier straps crossed over the chest, a bundled baby behind.",
    "tags": ["civilian", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37400, 2)
    cap(body, "P", seed=37400)
    f = body.front
    f.set(3, 0, None), f.set(4, 0, None), f.set(2, 0, "P1"), f.set(5, 0, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for arm in arm_cloth(g, "P", "plain", 37401, rows=(0, 5)):
        arm.strip.hline(0, arm.strip.w - 1, 5, "P3")
    # The straps cross between the shoulders and the hips.
    for i, rz in enumerate((-34, 34)):
        strap = g.piece(f"strap_{i}", "TORSO", (-.5, -6, -.5), (1, 12, 1), pivot=(0, 5.0, -2.4), rotation=(0, 0, rz))
        solid(strap, "D", "weave", 37404 + i, 2, edge=False)
    belt = g.piece("strap_waist", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.12)
    solid(belt, "D", "weave", 37406, 2, edge=False)
    # The baby: a quilted bundle riding high on the back, a bonnet peeping over the shoulders.
    bundle = g.piece("baby_bundle", "TORSO", (-3, 0, 0), (6, 6, 3), pivot=(0, 2.2, 2.2))
    solid(bundle, "A", "quilt", 37407, 2)
    fabric(bundle.top, "A", "quilt", 37407, 3)
    bonnet = g.piece("baby_bonnet", "TORSO", (-1.5, 0, -1.5), (3, 3, 3), pivot=(0, -.6, 3.6), inflate=.05)
    solid(bonnet, "S", "knit", 37408, 3)
    bonnet.top.set(1, 1, "A3")
    pom = g.piece("baby_pompom", "TORSO", (-.5, 0, -.5), (1, 1, 1), pivot=(0, -1.6, 3.6))
    solid(pom, "A", "knit", 37409, 3, edge=False)
