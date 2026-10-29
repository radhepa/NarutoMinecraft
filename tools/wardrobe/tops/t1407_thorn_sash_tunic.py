"""Thorn Sash Tunic: a practical high-collared tunic for the clan's field ninja, crossed from the
left shoulder to the right hip by an ivory sash printed with a thorn stem, short sleeves over
bandaged forearms and a leather belt with a pouch."""
from kit import belt, collar, pouch
from kit_yuhi import bandage_turns, thorn_vine
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Thorn Sash Tunic",
    "gender": "unisex",
    "description": "High-collared tunic, thorn-printed ivory sash across the chest, short sleeves, bandaged forearms.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 14780, 2)
    cap(body, "P", texture="twill", seed=14780)
    jacket = g.part("jacket")
    # The sash: two texels wide, from the left shoulder down across the chest to the right hip and up the back.
    for i in range(9):
        x = 7 - (i * 7) // 8
        for dx in (0, -1):
            if 0 <= x + dx < 8:
                jacket.front.set(x + dx, i, "S3" if dx == 0 else "S2")
        if 0 <= x - 1 < 8 and i % 3 == 1:
            jacket.front.set(x - 1 if x - 1 >= 0 else 0, i, "A2")
        bx = (i * 7) // 8
        jacket.back.set(bx, i, "S3"), jacket.back.set(min(7, bx + 1), i, "S2")
    belt(g, "belt", y=9.6, role="L", height=1, buckle="M")
    pouch(g, "pouch", (2.6, 10.6, -2.6), (2, 2, 1))
    neck = collar(g, "collar", "P", "twill", height=2, y=-1.4)
    neck.front.vline(4, 0, 1, "P0")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 14781 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "twill", 14783, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "P1")
        bandage_turns(arm.strip, 0, 6, arm.strip.w - 1, 10, "S", 3)
    thorn_vine(g.part("right_arm").right, 1, 0, 3, "A")
