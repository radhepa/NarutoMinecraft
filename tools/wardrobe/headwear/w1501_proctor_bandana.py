"""Proctor Bandana: Hayate Gekko's forehead protector worn as a bandana, a dark navy cloth tied over
the whole crown with the steel plate across the brow and long ends knotted at the nape."""
from kit_shinobi import forehead_protector
from paint import fabric, solid

META = {"name": "Proctor Bandana", "gender": "unisex", "hides_hair": ["*"],
        "description": "Dark navy cloth over the crown with the protector plate, long ends knotted at the nape."}


def build(g):
    cap = g.piece("bandana", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    solid(cap, "D", "weave", 15600, 2, edge=False)
    fabric(cap.top, "D", "weave", 15600, 3)
    back = g.piece("bandana_back", "HEAD", (-4, -6, 3), (8, 3, 1), inflate=.62)
    solid(back, "D", "weave", 15601, 2)
    back.back.hline(0, 7, 2, "D1")
    for face in (back.right, back.left):
        face.fill("D2")
    forehead_protector(g, "D", seed=15602, ring=False)
    for i, (x, rz) in enumerate(((-1.0, 26), (1.0, -22))):
        end = g.piece(f"bandana_end_{i}", "HEAD", (-.5, 0, 0), (1, 5, 1), pivot=(x, -3.2, 4.7), rotation=(16, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 15610 + i, 2)
