"""Training Kimono: the top Yakumo trained in with Kurenai. A short wrapped kimono top cut
asymmetrically, one long sleeve to the wrist and one short to the shoulder, the bare arm under
chain mesh; a wide sash bound high round the waist."""
from kit import belt
from kit_kurama import wrap_front
from kit_shinobi import mesh
from paint import cap, fabric, strip_fabric

META = {
    "name": "Training Kimono",
    "gender": "female",
    "description": "Short wrapped kimono top, one long sleeve and one short, mesh on the bare arm, a wide sash.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 12625, 2, 0, 9)
    cap(body, "P", seed=12625)
    f = body.front
    for x, y in [(2, 0), (3, 0), (3, 1)]:
        f.clear(x, y)
    mesh(f, 2, 0, 3, 1, "K2")
    wrap_front(f, "S3", "P1", rows=6, start=3)
    # The body below the sash: the mesh undershirt at the hips.
    for face in body.sides:
        mesh(face, 0, 10, face.w - 1, 11, "K2")
    # The wide sash, two layers of the accent with a light cord between them.
    sash = belt(g, "sash", y=6.8, role="A", height=3, buckle=None, inflate=.12)
    for face in sash.sides:
        face.hline(0, face.w - 1, 1, "S3")
    strip_fabric(jacket, "A", "weave", 12626, 2, 9, 9)
    # Right: the long sleeve. Left: a short cap sleeve over a mesh arm.
    right, rs = g.part("right_arm"), g.part("right_sleeve")
    strip_fabric(right, "P", "weave", 12627, 2, 0, 10)
    fabric(right.top, "P", "weave", 12627, 3)
    strip_fabric(rs, "P", "weave", 12628, 2, 0, 9)
    fabric(rs.top, "P", "weave", 12628, 3)
    rs.strip.hline(0, rs.strip.w - 1, 9, "S3")
    left, ls = g.part("left_arm"), g.part("left_sleeve")
    strip_fabric(left, "P", "weave", 12629, 2, 0, 2)
    fabric(left.top, "P", "weave", 12629, 3)
    mesh(left.strip, 0, 3, left.strip.w - 1, 8, "K2")
    strip_fabric(ls, "P", "weave", 12630, 2, 0, 2)
    fabric(ls.top, "P", "weave", 12630, 3)
    ls.strip.hline(0, ls.strip.w - 1, 2, "S3")
