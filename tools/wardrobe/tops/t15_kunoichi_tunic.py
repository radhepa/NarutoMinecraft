"""Kunoichi Tunic: a sleeveless violet tunic with a stand-up collar and gold piping, a short split
skirt over the shorts, chain-mesh sleeves and violet arm warmers: the genin kunoichi's field kit."""
from kit import belt, collar, flaps, pouch
from kit_shinobi import mesh
from paint import cap, fabric, strip_fabric

META = {
    "name": "Kunoichi Tunic",
    "gender": "unisex",
    "description": "Sleeveless violet tunic with gold piping, a split skirt, mesh sleeves and arm warmers.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 291, 2)
    cap(body, "P", seed=291)
    f = body.front
    # A wrap closure crossing from the collar to the right hip, piped in gold.
    for y in range(9):
        x = 5 - y // 2
        f.set(x, y, "A2"), f.set(x - 1, y, "P1")
    for face in (body.right, body.left):
        face.hline(0, face.w - 1, 0, "A2")
    # Mesh sleeves over the arm, violet warmers on the forearm with a gold band.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 7, "K3")
        mesh(arm.top, 0, 0, arm.top.w - 1, arm.top.h - 1, "K3")
        strip_fabric(arm, "P", "plain", 292, 2, 7, 10)
        strip_fabric(sleeve, "P", "plain", 293, 2, 6, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "A2")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P1")
    neck = collar(g, "collar", "P", "plain", height=2, y=-1.4)
    neck.front.hline(0, 8, 0, "A3"), neck.front.vline(5, 0, 1, "A2")
    for face in (neck.right, neck.left, neck.back):
        face.hline(0, face.w - 1, 0, "A3")
    sash = belt(g, "sash", y=8.8, role="K", height=1, buckle=None)
    sash.front.set(5, 0, "A3")
    pouch(g, "hip_pouch", (2.6, 9.6, 2.2), size=(2, 2, 1), role="L", flap="L3")
    for face in flaps(g, "skirt", 4, "P", "plain", 294, hem="A2", top=9.8, slit=True):
        face.hline(0, face.w - 1, 1, "P1")
