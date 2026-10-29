"""Nightshade Robe: the poison master's long dark robe, closed at the throat and falling in narrow
front panels to the knee, edged in toxic violet, bound with a white sash hung with a single vial
of something no one should drink, and dark gloves."""
from kit import belt, collar
from kit_suzuran import bell_hem, gloves, vial
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Nightshade Robe",
    "gender": "unisex",
    "description": "Long dark robe edged in violet, narrow front panels to the knee, a white sash and one vial.",
    "tags": ["shinobi", "robe", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "velvet", 24571, 2)
    cap(body, "P", seed=24571)
    strip_fabric(jacket, "P", "velvet", 24572, 2)
    cap(jacket, "P", texture="velvet", seed=24572)
    f = jacket.front
    for y in range(12):
        x = 4 - min(3, y // 3)
        f.set(x, y, "A2")
        if y < 3:
            f.set(x - 1, y, "A3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "A2")
    neck = collar(g, "collar", "P", "velvet", height=1, y=-.8)
    neck.front.hline(2, 5, 0, "A2")
    belt(g, "sash", y=8.0, role="S", height=2, buckle=None, inflate=.14)
    vial(g, "poison", (2.6, 9.6, -3.0), liquid="A2", height=4)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 24573 + (side == "left"), 2, 0, 8)
        fabric(arm.top, "P", "velvet", 24573, 3)
        strip_fabric(sleeve, "P", "velvet", 24575, 2, 0, 8)
        fabric(sleeve.top, "P", "velvet", 24575, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "A2")
    gloves(g, "K", top=9)
    for i, (x, w) in enumerate(((-4.6, 4), (.6, 4))):
        panel = g.piece(f"robe_front_{i}", "TORSO", (0, 0, 0), (w, 8, 1), pivot=(x, 11.4, -2.95), motion="flap_front")
        solid(panel, "P", "velvet", 24576 + i, 2)
        panel.front.vline(w - 1 if i == 0 else 0, 0, 7, "A2")
        bell_hem(panel.front, 5, stem="A1", bell="S3", shade="P1", step=2, start=i)
    back = g.piece("robe_back", "TORSO", (-4.5, 0, 0), (9, 8, 1), pivot=(0, 11.4, 1.95), motion="flap_back")
    solid(back, "P", "velvet", 24578, 2)
    bell_hem(back.back, 5, stem="A1", bell="S3", shade="P1", step=2)
