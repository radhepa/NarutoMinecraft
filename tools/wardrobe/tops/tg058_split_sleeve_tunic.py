"""Split Sleeve Tunic: a high-necked tunic whose long sleeves are open from shoulder to cuff and
caught at the wrist with a ribbon, the bare arm showing through the split; a slim sash."""
from kit import belt
from paint import cap, strip_fabric

META = {
    "name": "Split Sleeve Tunic",
    "gender": "female",
    "description": "High-necked tunic, long sleeves split open to the wrist ribbons, a slim sash.",
    "tags": ["shinobi", "chunin", "tunic"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 33340, 2)
    cap(body, "P", texture="smooth", seed=33340)
    body.front.hline(2, 5, 0, "P3")
    for side in ("right", "left"):
        sleeve, arm = g.part(f"{side}_sleeve"), g.part(f"{side}_arm")
        strip_fabric(sleeve, "P", "smooth", 33341, 2, 0, 9)
        # The split runs down the outer face, one column of bare arm.
        outer = sleeve.right if side == "right" else sleeve.left
        for y in range(1, 8):
            outer.clear(1, y), outer.clear(2, y)
        outer.set(0, 8, "A3"), outer.set(3, 8, "A3")
        sleeve.strip.hline(0, 15, 9, "A2")
        sleeve.top.fill("P3")
        arm.strip.hline(0, 15, 0, "P2")
    sash = belt(g, "sash", y=8.8, role="A", height=1, buckle=None, inflate=.1)
    sash.front.set(6, 0, "A4")
