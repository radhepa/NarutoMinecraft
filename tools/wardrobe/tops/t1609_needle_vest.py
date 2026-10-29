"""Needle Vest: a quilted steel-grey vest with rows of narrow needle pockets, the senbon heads
showing at the top of each, worn over a dusky turtleneck: the chunin's answer to the flak vest."""
from kit import collar
from paint import cap, fabric, strip_fabric

META = {
    "name": "Needle Vest",
    "gender": "unisex",
    "description": "Quilted steel vest with rows of senbon pockets over a dusky turtleneck.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "knit", 16840, 2)
    cap(body, "D", texture="knit", seed=16840)
    strip_fabric(jacket, "P", "quilt", 16841, 2, 0, 10)
    cap(jacket, "P", texture="quilt", seed=16841)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    for y in range(11):
        jacket.front.set(3, y, "P0"), jacket.front.set(4, y, "P3")
    for x0 in (0, 5):
        for x in range(x0, x0 + 3):
            jacket.front.set(x, 3, "M4" if x % 2 == 0 else "P3")
            jacket.front.set(x, 7, "M4" if x % 2 == 1 else "P3")
            jacket.front.set(x, 4, "P1"), jacket.front.set(x, 8, "P1")
    collar(g, "collar", "D", texture="knit", height=2, y=-1.6)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "knit", 16843 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "quilt", 16843, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
        arm.strip.hline(0, arm.strip.w - 1, 11, "D3")
