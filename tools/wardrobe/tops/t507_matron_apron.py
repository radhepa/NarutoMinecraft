"""Matron Apron: the Nara household's at-home wear. A long-sleeved wrap blouse closed by a sash, a
plain work apron tied over it down to the knee, sleeves tied back at the elbow."""
from kit import belt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Matron Apron",
    "gender": "unisex",
    "description": "Wrap blouse with a sash, a plain apron to the knee, sleeves tied back.",
    "tags": ["shinobi", "nara", "work"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 5561, 2)
    cap(body, "P", seed=5561)
    f = body.front
    for y in range(5):
        f.set(1 + y, y, "P3"), f.set(2 + y, y, "P1")
    # The apron bib and its neck strap.
    fabric(f, "S", "weave", 5562, 3, 2, 4, 4, 8)
    f.hline(2, 5, 4, "S4")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 5563 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "weave", 5563, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "K2")
        arm.strip.hline(0, arm.strip.w - 1, 10, "P1")
    sash = belt(g, "sash", y=7.4, role="A", height=2, buckle=None, inflate=.12)
    sash.front.hline(0, sash.front.w - 1, 1, "A1")
    skirt = g.piece("apron", "TORSO", (-3, 0, 0), (6, 8, 1), pivot=(0, 9.4, -2.95), motion="flap_front")
    solid(skirt, "S", "weave", 5565, 3)
    skirt.front.hline(0, 5, 0, "S4"), skirt.front.hline(0, 5, 7, "S2")
    skirt.front.vline(1, 2, 6, "S2")
    for i, (x, rz) in enumerate(((-.6, 10), (.6, -8))):
        tail = g.piece(f"sash_tail_{i}", "TORSO", (-.5, 0, 0), (1, 5, 1), pivot=(x, 9.0, 2.75), rotation=(6, 0, rz),
                       motion="sway")
        solid(tail, "A", "weave", 5566 + i, 2)
