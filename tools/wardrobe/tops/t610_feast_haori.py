"""Feast Haori: the clan's formal wear, a long dark haori to the knee with the 食 crest in a white
disc across the back, worn over a kimono with a white collar, a broad red obi and white haori
cords tied at the chest."""
from kit import belt
from kit_akimichi import shoku_disc
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Feast Haori",
    "gender": "unisex",
    "description": "Long dark haori with the food crest on the back, white kimono collar, red obi, white cords.",
    "tags": ["shinobi", "robe", "akimichi"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 6906, 2)
    cap(body, "D", seed=6906)
    strip_fabric(jacket, "P", "velvet", 6907, 2)
    cap(jacket, "P", texture="velvet", seed=6907)
    f = jacket.front
    for y in range(12):
        for x in (3, 4):
            f.set(x, y, None)
    f.vline(2, 0, 11, "P1"), f.vline(5, 0, 11, "P0")
    # The kimono's white collar crossing at the throat.
    for i, (x, y) in enumerate(((3, 0), (4, 0), (3, 1), (4, 2))):
        body.front.set(x, y, "S3" if i % 2 == 0 else "S2")
    obi = belt(g, "obi", y=8.0, role="A", height=3, buckle=None, inflate=.15)
    obi.front.hline(0, obi.front.w - 1, 1, "A1")
    # The haori cords: two white tassels tied across the opening.
    cords = g.piece("cords", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 4.0, -2.75))
    solid(cords, "S", "plain", 6908, 3, edge=False)
    for i, x in enumerate((-.6, .6)):
        tassel = g.piece(f"tassel_{i}", "TORSO", (-.5, 0, 0), (1, 2, 1), pivot=(x, 5.0, -2.8), motion="sway")
        solid(tassel, "S", "plain", 6909 + i, 3, edge=False)
    shoku_disc(g, "back_crest", (0, 3.6, 2.3), ground="P2", disc="S", ink="P1", side="back")
    # The skirts: the two fronts hang open over the kimono, the back is one panel.
    for i, x in enumerate((-4.5, 1.5)):
        panel = g.piece(f"haori_front_{i}", "TORSO", (0, 0, 0), (3, 7, 1), pivot=(x, 11.0, -2.75), motion="flap_front")
        solid(panel, "P", "velvet", 6911 + i, 2)
        panel.front.vline(2 if i == 0 else 0, 0, 6, "P1")
    back = g.piece("haori_back", "TORSO", (-4.5, 0, 0), (9, 7, 1), pivot=(0, 11.0, 1.75), motion="flap_back")
    solid(back, "P", "velvet", 6914, 2)
    for side, x in (("right", -5.0), ("left", 4.0)):
        panel = g.piece(f"haori_{side}", "TORSO", (0, 0, -2), (1, 6, 4), pivot=(x, 11.0, 0))
        solid(panel, "P", "velvet", 6913, 2)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "velvet", 6915 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "P", "velvet", 6915, 3)
        strip_fabric(sleeve, "P", "velvet", 6917, 2, 0, 8)
        fabric(sleeve.top, "P", "velvet", 6917, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "P1")
