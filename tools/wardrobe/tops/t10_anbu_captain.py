"""ANBU Captain: the plated armor with riveted steel pauldrons, black lacquer pauldrons, the captain's blue scarf
wrapped at the throat, a blue armband and a long ninjato across the back, hilt over the right shoulder."""
from kit import arm_bone, arm_x
from kit_shinobi import anbu_arms, anbu_plates, tanto
from paint import cap, solid, strip_fabric

META = {
    "name": "ANBU Captain",
    "gender": "unisex",
    "description": "Plated armor with black lacquer pauldrons, a blue scarf, a captain's armband and a ninjato.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 201, 2)
    cap(body, "D", seed=201)
    anbu_plates(g, seed=202)
    anbu_arms(g)
    for side in ("right", "left"):
        # Two-tier black lacquer pauldron: a cap and a lame below it, both riveted.
        upper = g.piece(f"{side}_pauldron", arm_bone(side), (arm_x(side) - .5, -2.7, -2.5), (5, 2, 5), inflate=.15)
        solid(upper, "K", "smooth", 203, 2, edge=False)
        lame = g.piece(f"{side}_pauldron_lame", arm_bone(side), (arm_x(side) - .5, -.9, -2.5), (5, 2, 5))
        solid(lame, "K", "smooth", 204, 2, edge=False)
        for box in (upper, lame):
            for face in box.sides:
                face.hline(0, face.w - 1, 0, "K3"), face.hline(0, face.w - 1, 1, "K1")
                face.set(face.w // 2, 0, "M3")
        band = g.part(f"{side}_sleeve")
        if side == "left":
            strip_fabric(band, "A", "weave", 205, 2, 2, 3)
            band.strip.hline(0, band.strip.w - 1, 2, "A3")
    # The captain's scarf, wrapped at the throat.
    wrap = g.piece("scarf", "TORSO", (-4.5, -1.2, -2.7), (9, 2, 5), inflate=.1)
    solid(wrap, "A", "weave", 206, 2, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 0, "A3")
    tanto(g, "ninjato", pivot=(-1.4, 1.2, 2.9), rotation=(0, 0, -40), length=12)
