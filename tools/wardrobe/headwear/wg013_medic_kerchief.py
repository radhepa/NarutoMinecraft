"""Medic Kerchief: the ward's cloth kerchief tied over the crown to keep hair out of a wound, the
corps' cross on the brow and the ends knotted at the nape."""
from glyphs import stamp
from kit_specialist import CROSS
from paint import fabric, solid

META = {"name": "Medic Kerchief", "gender": "unisex", "hides_hair": ["*"],
        "description": "Cloth kerchief tied over the crown with the medical cross on the brow, knotted at the nape."}


def build(g):
    cap = g.piece("kerchief", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.64)
    solid(cap, "P", "weave", 34950, 3, edge=False)
    fabric(cap.top, "P", "weave", 34950, 4)
    for f in cap.sides:
        f.hline(0, f.w - 1, 1, "P2")
    back = g.piece("kerchief_back", "HEAD", (-4, -6.4, 3), (8, 3, 1), inflate=.64)
    solid(back, "P", "weave", 34951, 3)
    mark = g.piece("kerchief_cross", "HEAD", (-3, 0, 0), (6, 6, 1), pivot=(0, -8.2, -4.75), scale=(1 / 3, 1 / 3, 1 / 3))
    for f in mark.faces:
        fabric(f, "P", "weave", 34952, 3)
    stamp(mark.front, CROSS, 0, 0, {"#": "A2"})
    for i, (x, rz) in enumerate(((-.9, 22), (.9, -18))):
        end = g.piece(f"kerchief_end_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -3.0, 4.75), rotation=(14, 0, rz),
                      motion="sway")
        solid(end, "P", "weave", 34953 + i, 3)
