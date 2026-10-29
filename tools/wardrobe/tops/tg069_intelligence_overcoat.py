"""Intelligence Overcoat: the long dark overcoat of the intelligence division, worn closed over a
grey shirt with a short shoulder cape buttoned at the throat, a high back collar, and a slim case
of ciphers carried on a strap: the field analyst who reads a village from its paperwork."""
from kit import collar
from kit_specialist import coat_skirts, ink_stains, shirt
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Intelligence Overcoat",
    "gender": "unisex",
    "description": "Long closed overcoat with a short buttoned shoulder cape, high collar, inked cuffs.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    shirt(g, "S", "weave", 34160)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "smooth", 34162, 2)
    cap(jacket, "P", texture="smooth", seed=34162)
    jacket.front.vline(4, 3, 11, "P0")
    for y in (5, 8, 11):
        jacket.front.set(3, y, "M3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 34163, 2)
        strip_fabric(sleeve, "P", "smooth", 34164 + (side == "left"), 2, 0, 11)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "P0")
        ink_stains(arm.strip, 34166 + (side == "left"), range(10, 12), .2)
    neck = collar(g, "coat_collar", "P", "smooth", height=2, y=-1.6)
    neck.front.vline(4, 0, 1, "P0")
    # The shoulder cape: a short wide yoke over the shoulders and the tops of the arms.
    cape = g.piece("shoulder_cape", "TORSO", (-8.4, -.4, -2.8), (17, 3, 6), inflate=.1)
    solid(cape, "P", "smooth", 34168, 2)
    cape.top.fill("P3")
    for face in cape.sides:
        face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, face.h - 1, "P0")
        for x in range(2, face.w - 1, 4):
            face.set(x, 1, "P1")
    cape.front.vline(8, 0, 2, "P0"), cape.front.set(7, 1, "M3")
    cape.bottom.fill(k("P", 0))
    coat_skirts(g, "coat_skirt", 9, "P", "smooth", 34170, open_front=False, hem="P1")
