"""Village Kimono: the everyday kimono of the clan's homes, wrapped left over right with a cream
collar, a wide green obi tied in a flat bow at the back, and broad sleeves hanging below the arms."""
from kit import belt, flaps
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Village Kimono",
    "gender": "unisex",
    "description": "Wrapped kimono to the knee, cream collar, wide obi with a flat bow, broad hanging sleeves.",
    "tags": ["senju", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 1550, 2)
    cap(body, "P", texture="twill", seed=1550)
    f = body.front
    # The collar (eri) runs from the right shoulder down to the left of the obi.
    for i in range(8):
        x = 1 + i * 5 // 8
        f.set(x, i, "S3"), f.set(x + 1, i, "S2")
    f.set(6, 0, "S3"), f.set(7, 0, "S3"), f.set(6, 1, "S2")
    obi = belt(g, "obi", y=7.2, role="A", height=3, buckle=None, inflate=.2)
    obi.front.hline(0, 8, 1, "A1")
    bow = g.piece("obi_bow", "TORSO", (-2.5, 0, 0), (5, 3, 1), pivot=(0, 7.0, 2.6))
    solid(bow, "A", "twill", 1551, 2)
    bow.back.vline(2, 0, 2, "A1")
    for face in flaps(g, "kimono", 7, "P", "twill", 1552, width=9, top=10.6, front_z=-2.6, back_z=1.6):
        face.hline(0, 8, 6, "P1")
    for name, x in (("right", -4.75), ("left", 3.75)):
        side = g.piece(f"kimono_side_{name}", "TORSO", (0, 0, -2.1), (1, 7, 4), pivot=(x, 10.6, 0))
        solid(side, "P", "twill", 1553, 2)
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 1554, 2, 0, 9)
        fabric(arm.top, "P", "twill", 1554, 3)
        strip_fabric(sleeve, "P", "twill", 1555, 2, 0, 9)
        fabric(sleeve.top, "P", "twill", 1555, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "S3")
        # The sleeve's hanging pocket (tamoto) under the forearm.
        pocket = g.piece(f"{side}_tamoto", bone, (ox + .5, 3.5, -2.5), (3, 6, 5), inflate=.05)
        solid(pocket, "P", "twill", 1556, 2)
        pocket.bottom.fill("P1")
