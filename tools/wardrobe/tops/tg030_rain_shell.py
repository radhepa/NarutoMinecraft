"""Rain Shell: a hip-length hooded shell for weather on the road, toggled down the front, the hood
folded down the back, a drawcord in the accent colour at the hem and cuffed sleeves."""
from kit_field import shirt
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Rain Shell",
    "gender": "unisex",
    "description": "Hooded hip-length shell with toggles, the hood down, an accent drawcord and cuffed sleeves.",
    "tags": ["shinobi", "coat", "chunin"],
    "covers_waist": True,
}


def build(g):
    shirt(g, "P", 32180, texture="smooth")
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "smooth", 32182, 2)
    cap(jacket, "P", texture="smooth", seed=32182)
    f = jacket.front
    f.vline(4, 0, 11, "P0"), f.vline(3, 0, 11, "P3")
    for y in (2, 5, 8):
        f.set(4, y, "S3")
    for face in (jacket.right, jacket.left):
        face.vline(2, 0, 11, "P1")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "smooth", 32184, 2, 8, 9)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "P3"), sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "P1")
    hem = g.piece("hem", "TORSO", (-4.5, 0, -2.5), (9, 3, 5), pivot=(0, 10.2, 0), inflate=.32)
    solid(hem, "P", "smooth", 32185, 2)
    for face in hem.sides:
        face.hline(0, face.w - 1, 1, k("A", 2))
    hem.front.set(4, 1, "P0"), hem.front.set(4, 0, "P0"), hem.front.set(4, 2, "P0")
    for i, x in enumerate((-1.2, 1.2)):
        cord = g.piece(f"cord_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 11.0, -3.1), scale=(.5, 1, .5),
                       motion="sway")
        solid(cord, "A", "plain", 32186 + i, 2)
    hood = g.piece("hood", "TORSO", (-3.5, 0, 0), (7, 5, 2), pivot=(0, -.8, 2.2), rotation=(-12, 0, 0))
    solid(hood, "P", "smooth", 32188, 2)
    hood.back.hline(0, 6, 0, "P3"), hood.back.vline(3, 1, 4, "P1")
    hood.front.hline(0, 6, 0, "A2")
    collar = g.piece("collar", "TORSO", (-4.5, -1.2, -2.7), (9, 2, 5), inflate=.08)
    solid(collar, "P", "smooth", 32189, 2, edge=False)
    collar.front.vline(4, 0, 1, "P0")
    fabric(collar.top, "P", "smooth", 32189, 3)
