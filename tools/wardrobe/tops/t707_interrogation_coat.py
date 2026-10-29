"""Interrogation Coat: the long slate greatcoat of the Torture and Interrogation force, buttoned to
a high collar with accent trim, belted in leather, the skirts split to the knee, long sleeves with
turned-back cuffs."""
from kit import arm_x, belt, collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Interrogation Coat",
    "gender": "unisex",
    "description": "Long dark greatcoat to the knee with a high collar, leather belt, split skirts, turned cuffs.",
    "tags": ["shinobi", "yamanaka", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 7750, 2)
    cap(body, "P", texture="twill", seed=7750)
    strip_fabric(jacket, "P", "twill", 7751, 2)
    cap(jacket, "P", texture="twill", seed=7751)
    f = jacket.front
    f.vline(3, 0, 11, "A2"), f.vline(4, 0, 11, "P0")
    for y in (2, 5):
        f.set(5, y, "M3"), f.set(2, y, "M3")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    belt(g, "belt", y=8.6, role="L", height=1, buckle="M", inflate=.3)
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 7752 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 7752, 3)
        strip_fabric(sleeve, "P", "twill", 7754, 2, 0, 3)
        fabric(sleeve.top, "P", "twill", 7754, 3)
        cuff = g.piece(f"{side}_cuff", bone, (arm_x(side) - .4, 8.6, -2.4), (5, 2, 5), inflate=.08)
        solid(cuff, "P", "twill", 7755, 3)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 0, "A2")
    for name, z, motion in (("front", -3.0, "flap_front"), ("back", 2.0, "flap_back")):
        for i, (x, w) in enumerate(((-4.5, 4), (.5, 4))):
            panel = g.piece(f"skirt_{name}_{i}", "TORSO", (0, 0, 0), (w, 8, 1), pivot=(x, 11.2, z), motion=motion)
            solid(panel, "P", "twill", 7756 + i, 2)
            getattr(panel, name).hline(0, w - 1, 7, "A2")
    neck = collar(g, "collar", "P", "twill", height=2, y=-1.6)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A2")
