"""Medic Coat: the medical corps' ward coat, knee-length and worn open over a plain shirt, piped in
the corps colour down the front, with a standing collar, buttoned cuffs and the cross armband on
the left arm and on the back: the healer who runs the hospital floor between missions."""
from glyphs import stamp
from kit import collar
from kit_specialist import CROSS, coat_skirts, cross_armband, shirt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Medic Coat",
    "gender": "unisex",
    "description": "Knee-length open ward coat piped in green over a shirt, standing collar, cross armband.",
    "tags": ["shinobi", "coat", "chunin"],
    "covers_waist": True,
}


def build(g):
    shirt(g, "S", "weave", 34000)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "smooth", 34002, 2)
    cap(jacket, "P", texture="smooth", seed=34002)
    f = jacket.front
    for y in range(12):
        for x in range(3, 5):
            f.clear(x, y)
        f.set(2, y, "A2"), f.set(5, y, "A2")
    for y in (3, 6, 9):
        f.set(1, y, "M3")
    jacket.back.vline(4, 7, 11, "P1")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "smooth", 34003 + (side == "left"), 2, 0, 11)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "A2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "P1")
    neck = collar(g, "coat_collar", "P", "smooth", height=2, y=-1.4)
    neck.front.vline(4, 0, 1, "A2")
    for i, x in enumerate((-3.4, 1.4)):
        pocket = g.piece(f"chest_pocket_{i}", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(x, 3.0, -2.6))
        solid(pocket, "P", "smooth", 34006 + i, 2)
        pocket.front.hline(0, 1, 0, "A2")
    coat_skirts(g, "coat_skirt", 8, "P", "smooth", 34008, hem="P1", edge="A2")
    cross_armband(g, "left", seed=34015)
    back = g.piece("back_cross", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 1.6, 2.3), scale=(.5, .5, .5))
    for face in back.faces:
        fabric(face, "P", "smooth", 34016, 2)
    stamp(back.back, CROSS, 1, 1, {"#": "A2"})
