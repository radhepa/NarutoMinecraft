"""Handler Jerkin: a ninken handler's leather jerkin laced over a shirt with sleeves pushed up, a
crossed harness of straps on the back, a coiled lead hooked at the hip and a pouch of treats."""
from kit import belt, pouch, roll, sleeves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Handler Jerkin",
    "gender": "unisex",
    "description": "Laced leather jerkin over a shirt, a crossed back harness, a coiled lead and a treat pouch.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 8720, 2)
    cap(body, "P", seed=8720)
    strip_fabric(jacket, "L", "leather", 8721, 2, 0, 10)
    fabric(jacket.top, "L", "leather", 8721, 3)
    f = jacket.front
    for y in range(0, 10):
        f.set(3, y, None), f.set(4, y, None)
    for y in range(1, 9, 2):
        f.set(3, y, "K2"), f.set(4, y + 1, "K2")
    f.vline(2, 0, 10, "L1"), f.vline(5, 0, 10, "L1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "L1")
    b = jacket.back
    for i in range(8):
        b.set(i, 1 + i, "K2"), b.set(7 - i, 1 + i, "K2")
    b.set(3, 4, "M3"), b.set(4, 4, "M3")
    for arm in sleeves(g, "P", "weave", 8722, 2, rows=(0, 4)):
        fabric(arm.top, "P", "weave", 8722, 3)
    roll(g, "P", 4.0, base=3)
    belt(g, "belt", y=9.6, role="K", buckle="M", inflate=.12)
    pouch(g, "treat_pouch", (2.6, 11.0, -2.9), (2, 2, 1), flap="M3")
    # The coiled lead hooked on the right hip.
    for i, (y, w) in enumerate(((10.6, 3), (11.6, 3), (12.6, 2))):
        coil = g.piece(f"lead_coil_{i}", "TORSO", (-w / 2, 0, -1), (w, 1, 2), pivot=(-4.6, y, -.4), motion="sway")
        solid(coil, "A", "leather", 8724 + i, 2, edge=False)
