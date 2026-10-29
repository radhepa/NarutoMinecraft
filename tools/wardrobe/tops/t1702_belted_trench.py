"""Belted Trench: a black double-breasted trench coat buttoned to the throat, two rows of steel
buttons, a leather belt cinched hard, shoulder straps and skirts to the knee split behind."""
from kit import belt, collar
from kit_morino import coat_skirts
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Belted Trench",
    "gender": "unisex",
    "description": "Black double-breasted trench buttoned to the throat, steel buttons, cinched belt, skirts to the knee.",
    "tags": ["shinobi", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 17221, 2)
    cap(body, "P", texture="twill", seed=17221)
    strip_fabric(jacket, "P", "twill", 17222, 2)
    cap(jacket, "P", texture="twill", seed=17222)
    f = jacket.front
    for y in range(12):
        f.set(5 - min(y, 2), y, "P0") if y < 3 else f.set(5, y, "P0")
    for y in (1, 4, 7):
        f.set(2, y, "M3"), f.set(6, y, "M3")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    belt(g, "belt", y=8.4, role="L", height=2, buckle="M", inflate=.3)
    neck = collar(g, "collar", "P", "twill", height=2, y=-1.6, inflate=.12)
    neck.front.set(4, 1, "A2"), neck.front.set(3, 1, "A2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 17223 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 17223, 3)
        strip_fabric(sleeve, "P", "twill", 17225, 2, 0, 9)
        fabric(sleeve.top, "P", "twill", 17225, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "L2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "P1")
    for name, x in (("right", -4.6), ("left", 2.6)):
        strap = g.piece(f"epaulette_{name}", "TORSO", (0, 0, -2.5), (2, 1, 5), pivot=(x, -.6, 0), inflate=.1)
        solid(strap, "P", "twill", 17226, 3)
        strap.top.set(1, 1, "M3")
    coat_skirts(g, "skirt", 7, "P", 17230, hem="P0", top=10.6, open_front=False)
