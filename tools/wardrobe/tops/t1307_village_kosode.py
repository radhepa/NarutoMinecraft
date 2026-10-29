"""Village Kosode: the clan's everyday wear in the village: a plain wrapped kosode with elbow
sleeves and a narrow dark-red obi knotted at the back, tucked into the trousers."""
from kit import belt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Village Kosode",
    "gender": "unisex",
    "description": "Plain wrapped kosode with elbow sleeves and a narrow dark-red obi knotted at the back.",
    "tags": ["shinobi", "civilian"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 13620, 2)
    cap(body, "P", seed=13620)
    f = body.front
    for y in range(9):
        x = min(7, 2 + y * 2 // 3)
        f.set(x, y, "S2")
        if x + 1 <= 7:
            f.set(x + 1, y, "P1")
    f.set(1, 0, "S2"), f.set(1, 1, "S3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 13621, 2, 0, 4)
        fabric(arm.top, "P", "weave", 13621, 3)
        strip_fabric(sleeve, "P", "weave", 13622 + (side == "left"), 2, 0, 4)
        fabric(sleeve.top, "P", "weave", 13622, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "P1")
    obi = belt(g, "obi", y=8.0, role="A", height=2, buckle=None, inflate=.1)
    obi.front.hline(0, 7, 1, "A1")
    knot = g.piece("obi_knot", "TORSO", (-1.5, 0, 0), (3, 2, 1), pivot=(0, 8.0, 2.6))
    solid(knot, "A", "weave", 13624, 3, edge=False)
    for i, rz in enumerate((10, -10)):
        end = g.piece(f"obi_end_{i}", "TORSO", (-.5, 0, 0), (1, 3, 1), pivot=(-.6 + 1.2 * i, 9.6, 2.7), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "A", "weave", 13625 + i, 2)
