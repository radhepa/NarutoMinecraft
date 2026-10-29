"""Cipher Coat: the cryptanalysis section's long scholar coat, closed to the knee with toggles down
the front, a collar turned up against the draughts of the archive, the cuffs stained with ink to
the wrist and a writing brush clipped in the breast pocket."""
from kit_aburame import high_collar
from kit_specialist import coat_skirts, ink_stains
from paint import cap, solid, strip_fabric

META = {
    "name": "Cipher Coat",
    "gender": "unisex",
    "description": "Knee-length scholar coat closed with toggles, turned-up collar, ink-stained cuffs, brush in pocket.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 34120, 2)
    cap(body, "P", texture="twill", seed=34120)
    strip_fabric(jacket, "P", "twill", 34121, 2)
    cap(jacket, "P", texture="twill", seed=34121)
    f = jacket.front
    f.vline(3, 0, 11, "P0"), f.vline(4, 0, 11, "P3")
    for y in (1, 4, 7, 10):
        f.set(2, y, "S3"), f.set(3, y, "S2")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 34122, 2)
        strip_fabric(sleeve, "P", "twill", 34123 + (side == "left"), 2, 0, 11)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "P3")
        ink_stains(sleeve.strip, 34125 + (side == "left"), range(9, 12), .25)
        ink_stains(arm.strip, 34127, range(10, 12), .3)
    high_collar(g, "P", "twill", 34130, cover_mouth=False, front_top=-1.6, back_top=-3.0, flare=8)
    pocket = g.piece("breast_pocket", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(1.4, 2.6, -2.75))
    solid(pocket, "P", "twill", 34134, 2)
    pocket.front.hline(0, 1, 0, "P3")
    brush = g.piece("pocket_brush", "TORSO", (-.5, -6, -.5), (1, 6, 1), pivot=(2.0, 3.0, -2.9), rotation=(0, 0, 10),
                    scale=(.5, .5, .5))
    solid(brush, "L", "smooth", 34135, 3, edge=False)
    for face in brush.sides:
        face.set(0, 4, "M3"), face.set(0, 5, "M2")
    brush.top.fill("L1")
    coat_skirts(g, "coat_skirt", 8, "P", "twill", 34136, open_front=False, hem="P1")
