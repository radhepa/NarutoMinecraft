"""Root Apron: Torune's close black trousers with an apron of dark cloth hanging over the front of the
thighs from the belt, pouches on both hips and black split-toe boots."""
from kit import footwear, legs, pouch, waistband
from paint import k, solid

META = {"name": "Root Apron", "gender": "unisex",
        "description": "Close black trousers, a dark apron over the thighs, hip pouches, split-toe boots.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "K", "twill", 10821, base=3)
    legs(g, "K", "twill", 10822, base=3, rows=(0, 9), crease=False)
    footwear(g, "boot", top=8, role="K", base=2, sole="K0")
    for side in ("right", "left"):
        g.part(f"{side}_pants").front.vline(1, 9, 11, "K0")   # the split toe
    apron = g.piece("waist_apron", "TORSO", (-4, 0, 0), (8, 7, 1), pivot=(0, 10.6, -2.85), motion="flap_front")
    solid(apron, "D", "twill", 10825, 2)
    apron.front.hline(0, 7, 0, k("D", 3))
    apron.front.vline(4, 1, 6, k("D", 1))
    for i, x in enumerate((-4.6, 4.6)):
        pouch(g, f"waist_pouch_{i}", (x, 10.2, 0), size=(1, 2, 2), role="L", flap="M3")
