"""Bandana Protector: a pale cloth bandana tied over the whole crown with the protector's plate sewn
on the front and the ends knotted at the nape: the field jonin's way of keeping hair out of the way."""
from kit_shinobi import forehead_protector
from paint import fabric, solid

META = {"name": "Bandana Protector", "gender": "unisex", "hides_hair": ["*"],
        "description": "Pale bandana over the crown with a protector plate, knotted at the nape."}


def build(g):
    cap = g.piece("bandana", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    solid(cap, "S", "weave", 371, 2, edge=False)
    fabric(cap.top, "S", "weave", 371, 3)
    back = g.piece("bandana_back", "HEAD", (-4, -6, 3), (8, 3, 1), inflate=.62)
    solid(back, "S", "weave", 372, 2)
    forehead_protector(g, "S", ring=False)
    for i, (x, rz) in enumerate(((-1.0, 24), (1.0, -20))):
        end = g.piece(f"bandana_end_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -3.0, 4.6), rotation=(14, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 373 + i, 2)
