"""Prodigy Shirt: Kakashi as the Academy's youngest graduate, a navy short-sleeved shirt with a high
neck that meets the mask, a kunai pouch at the back of the hip and the White Fang's tanto, too long
for him, across his back."""
from kit_hatake import white_fang_tanto
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Prodigy Shirt",
    "gender": "unisex",
    "description": "Navy short-sleeved high-neck shirt, a kunai pouch at the hip, a white-hilted tanto across the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 11301, 2)
    cap(body, "D", seed=11301)
    f = body.front
    f.vline(2, 2, 9, "D1"), f.vline(5, 3, 9, "D1")
    strip_fabric(jacket, "D", "weave", 11302, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "D3"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "D1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 11303, 2, 0, 3)
        fabric(arm.top, "D", "weave", 11303, 3)
        strip_fabric(sleeve, "D", "weave", 11304, 2, 0, 3)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 3, "D1")
    # The high neck standing up round the throat.
    neck = g.piece("high_neck", "TORSO", (-4.4, -1.4, -2.5), (9, 2, 5), inflate=.05)
    solid(neck, "D", "rib", 11305, 2)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "D3")
    pouch = g.piece("kunai_pouch", "TORSO", (0, 0, 0), (3, 2, 2), pivot=(-3.8, 9.0, .6))
    solid(pouch, "L", "leather", 11306, 2)
    pouch.right.hline(0, 1, 0, "L3"), pouch.right.set(0, 1, "M3")
    white_fang_tanto(g, "tanto", pivot=(-2.4, 2.0, 2.6), rotation=(0, 0, 38), length=9)
