"""Field Bandana: a dark cloth bandana pulled over the whole crown with the protector's plate sewn on
the front, knotted at the nape with two long ends: the working chunin's way to keep hair down."""
from kit_shinobi import forehead_protector
from paint import fabric, k, solid

META = {"name": "Field Bandana", "gender": "unisex", "hides_hair": ["*"],
        "description": "Dark bandana over the crown with a protector plate, knotted at the nape with long ends."}


def build(g):
    cap = g.piece("bandana", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    solid(cap, "D", "weave", 32965, 2, edge=False)
    fabric(cap.top, "D", "weave", 32965, 3)
    for face in cap.sides:
        face.hline(0, face.w - 1, 1, k("D", 1))
    back = g.piece("bandana_back", "HEAD", (-4, -6, 3), (8, 4, 1), inflate=.62)
    solid(back, "D", "weave", 32966, 2)
    back.back.vline(4, 0, 3, k("D", 1))
    forehead_protector(g, "D", seed=32967, ring=False)
    for i, (x, rz) in enumerate(((-1.0, 22), (1.0, -16))):
        end = g.piece(f"bandana_end_{i}", "HEAD", (-.5, 0, 0), (1, 6, 1), pivot=(x, -2.4, 4.7), rotation=(18, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 32973 + i, 2)
