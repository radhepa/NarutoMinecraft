"""Sash Kimono: Chocho's genin outfit, a sleeveless white kimono crossed over a chain-mesh shirt, a
broad sash tied at the back in a ribbon bow with long trailing ends, a short split skirt and long
black arm warmers."""
from kit import belt, flaps
from kit_shinobi import mesh
from paint import fabric, solid, strip_fabric

META = {
    "name": "Sash Kimono",
    "gender": "unisex",
    "description": "Sleeveless white kimono over a mesh shirt, a sash with a ribbon bow, long black arm warmers.",
    "tags": ["shinobi", "genin", "akimichi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    mesh(body.strip, 0, 0, body.strip.w - 1, 11)
    mesh(body.top, 0, 0, body.top.w - 1, body.top.h - 1)
    strip_fabric(jacket, "S", "velvet", 6806, 2, 0, 11)
    fabric(jacket.top, "S", "velvet", 6806, 3)
    f = jacket.front
    # The kimono crosses left over right, leaving a V of mesh at the throat, its edge trimmed.
    for y in range(4):
        for x in range(3 - y // 2, 5):
            f.set(x, y, None)
    for y in range(8):
        f.set(min(7, 5 + y // 3), y, "S1")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 1, 10, "S1")
    sash = belt(g, "sash", y=7.8, role="A", height=3, buckle=None, inflate=.3)
    sash.front.hline(0, sash.front.w - 1, 1, "A1")
    for i, (x, rz) in enumerate(((-1.7, 28), (1.7, -28))):
        loop = g.piece(f"bow_loop_{i}", "TORSO", (-1.5, -1, 0), (3, 2, 1), pivot=(x, 8.8, 2.9), rotation=(0, 0, rz))
        solid(loop, "A", "weave", 6807 + i, 1, edge=False)
    knot = g.piece("bow_knot", "TORSO", (-.5, -.5, 0), (1, 2, 1), pivot=(0, 8.6, 3.0))
    solid(knot, "A", "weave", 6809, 1, edge=False)
    for i, (x, rz) in enumerate(((-.8, 8), (.8, -8))):
        end = g.piece(f"bow_end_{i}", "TORSO", (-.5, 0, 0), (1, 6, 1), pivot=(x, 9.4, 2.9), rotation=(6, 0, rz),
                      motion="flap_back")
        solid(end, "A", "weave", 6810 + i, 1)
    for face in flaps(g, "skirt", 3, "S", "velvet", 6812, width=9, top=10.8, front_z=-2.75, back_z=1.75, slit=True):
        face.hline(0, face.w - 1, 2, "S1")
    # Mesh on the shoulders, long black arm warmers from above the elbow to the knuckles.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 3)
        mesh(arm.top, 0, 0, arm.top.w - 1, arm.top.h - 1)
        strip_fabric(arm, "K", "rib", 6814 + (side == "left"), 2, 4, 11)
        arm.strip.hline(0, arm.strip.w - 1, 4, "K3")
