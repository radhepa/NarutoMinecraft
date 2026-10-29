"""Ranger Vest: a forest scout's leather jerkin over a long-sleeved shirt, green vine stitching
climbing both front edges, a strap across the chest with two pouches, sleeves pushed to the elbow."""
from kit import pouch, roll
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Ranger Vest",
    "gender": "unisex",
    "description": "Leather jerkin with vine stitching over a shirt, chest strap with pouches, rolled sleeves.",
    "tags": ["shinobi", "senju", "vest"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 1590, 2)
    cap(body, "P", seed=1590)
    strip_fabric(jacket, "L", "leather", 1591, 2, 0, 10)
    cap(jacket, "L", texture="leather", seed=1591)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "L1")
    # Open at the throat, laced lower down; vines climb the edges.
    for y in range(4):
        jacket.front.clear(3, y), jacket.front.clear(4, y)
    for y in range(11):
        for x in (2, 5):
            jacket.front.set(x, y, k("A", 2 if (y + x) % 3 else 3) if y % 2 == 0 else k("L", 1))
    for y in (5, 7, 9):
        jacket.front.set(3, y, "S3"), jacket.front.set(4, y, "S3")
    strap = g.piece("chest_strap", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 6, -2.5), rotation=(0, 0, 38))
    solid(strap, "K", "leather", 1592, 3)
    for i, (x, y) in enumerate(((-2.8, 2.0), (1.2, 7.0))):
        pouch(g, f"strap_pouch_{i}", (x, y, -3.1), size=(2, 2, 1), role="L", flap="M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 1593, 2, 0, 5)
        fabric(arm.top, "P", "weave", 1593, 3)
    roll(g, "P", 4.0, prefix="sleeve_roll")
