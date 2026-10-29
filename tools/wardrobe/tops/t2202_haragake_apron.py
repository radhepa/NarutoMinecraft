"""Haragake Apron: the carpenter's indigo bib apron worn straight over a cream long-sleeved work
shirt, a big cedar-trimmed pocket across the belly with a pencil and a folding rule in it, straps
crossed over the back and the shirt sleeves rolled to the elbow."""
from kit import roll
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Haragake Apron",
    "gender": "unisex",
    "description": "Indigo bib apron with a cedar-trimmed belly pocket over a cream shirt, crossed back straps.",
    "tags": ["shinobi", "kinoshita", "work"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 22321, 3)
    cap(body, "S", base=3, seed=22321)
    f = body.front
    f.set(3, 0, "S1"), f.set(4, 0, "S1")
    # The bib from the collarbone to the hip, its neck straps up over the shoulders.
    fabric(f, "P", "twill", 22322, 2, 1, 2, 6, 10)
    f.vline(1, 0, 1, "P2"), f.vline(6, 0, 1, "P2")
    fabric(body.top, "P", "twill", 22322, 3, 1, 0, 1, 4), fabric(body.top, "P", "twill", 22322, 3, 6, 0, 1, 4)
    f.hline(1, 6, 2, "P3")
    # The belly pocket, trimmed in cedar.
    f.hline(1, 6, 6, "A2"), f.vline(1, 6, 10, "A1"), f.vline(6, 6, 10, "A1")
    f.vline(4, 7, 10, "P1")
    # Back straps crossing between the shoulder blades, down to the waist ties.
    b = body.back
    for y in range(10):
        b.set(min(7, 1 + y * 6 // 9), y, "P2"), b.set(max(0, 6 - y * 6 // 9), y, "P2")
    b.hline(0, 7, 10, "P1"), b.hline(0, 7, 11, "P2")
    for face in (body.right, body.left):
        face.hline(0, face.w - 1, 10, "P1"), face.hline(0, face.w - 1, 11, "P2")
    # A carpenter's pencil and a folding rule standing in the pocket.
    pencil = g.piece("pencil", "TORSO", (-.5, -2, -.5), (1, 3, 1), pivot=(-1.8, 7.2, -2.55), rotation=(0, 0, 10))
    solid(pencil, "A", "smooth", 22323, 3, edge=False)
    pencil.top.fill("K1")
    rule = g.piece("rule", "TORSO", (-.5, -2, -.5), (1, 3, 1), pivot=(2.0, 7.2, -2.55), rotation=(0, 0, -8))
    solid(rule, "S", "smooth", 22324, 4, edge=False)
    for face in rule.sides:
        face.set(0, 1, "K2")
    # The apron runs on below the waist to the upper thigh.
    skirt = g.piece("apron", "TORSO", (-3, 0, 0), (6, 4, 1), pivot=(0, 11.4, -2.85), motion="flap_front")
    solid(skirt, "P", "twill", 22325, 2)
    skirt.front.hline(0, 5, 3, "A2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 22326 + (side == "left"), 3, 0, 4)
        fabric(arm.top, "S", "weave", 22326, 4)
    roll(g, "S", 4.0)
