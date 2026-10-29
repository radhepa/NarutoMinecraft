"""Open Field Vest: a worn quilted vest hanging open over a short-sleeved undershirt, two deep hip
pockets with buttoned flaps, the sleeves turned up once and a pouch on the belt: the travelling
chunin's kit after a season on the roads."""
from kit import belt, neckline, pouch, roll
from paint import fabric, solid, strip_fabric

META = {
    "name": "Open Field Vest",
    "gender": "unisex",
    "description": "Worn quilted vest hanging open over a short-sleeved undershirt, deep hip pockets, a belt pouch.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 35030, 2, 0, 10)
    fabric(body.top, "S", "weave", 35030, 3)
    neckline(body.front, "round", "S")
    strip_fabric(jacket, "P", "quilt", 35031, 2, 0, 10)
    fabric(jacket.top, "P", "quilt", 35031, 3)
    f = jacket.front
    for y in range(11):
        f.set(3, y, None), f.set(4, y, None)
    f.vline(2, 0, 10, "P3"), f.vline(5, 0, 10, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    jacket.back.hline(0, 7, 4, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 35032, 2, 0, 3)
        fabric(arm.top, "S", "weave", 35032, 3)
    roll(g, "S", 1.6, base=2)
    for side, x in (("right", -3.0), ("left", 1.0)):
        p = g.piece(f"hip_pocket_{side}", "TORSO", (0, 0, 0), (2, 3, 1), pivot=(x, 6.4, -2.85))
        solid(p, "P", "quilt", 35033, 2)
        p.front.hline(0, 1, 0, "P3"), p.front.set(0, 1, "M3")
    belt(g, "vest_belt", y=10.0, role="L", height=1, buckle="M")
    pouch(g, "belt_pouch", (2.6, 10.6, 2.6), size=(2, 2, 1), flap="M3")
