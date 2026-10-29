"""Guard Bandana: Raido's way of wearing the forehead protector, the cloth drawn down over the whole
head and knotted behind, the plate across the brow, a pale wave trim along the lower edge and two
short ends lying flat on the nape."""
from kit_namiashi import wave_band
from kit_shinobi import forehead_protector
from paint import fabric, solid

META = {"name": "Guard Bandana", "gender": "unisex", "hides_hair": ["*"],
        "description": "Cloth drawn down over the whole head, the protector plate on the brow, a wave-trimmed edge."}


def build(g):
    cap = g.piece("bandana", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.64)
    solid(cap, "D", "weave", 20801, 2, edge=False)
    fabric(cap.top, "D", "weave", 20801, 3)
    back = g.piece("bandana_back", "HEAD", (-4, -6, -1), (8, 5, 5), inflate=.64)
    solid(back, "D", "weave", 20802, 2, edge=False)
    for face in (back.right, back.left, back.back):
        wave_band(face, 3, "S", 2, ground="D2")
    for face in (back.right, back.left):
        face.set(0, 4, "D1")
    back.front.fill("D1")
    forehead_protector(g, "D", seed=20803, ring=False)
    knot = g.piece("bandana_knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -4.4, 4.7))
    solid(knot, "D", "weave", 20804, 1)
    for i, (x, rz) in enumerate(((-.8, 8), (.8, -8))):
        end = g.piece(f"bandana_end_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -3.6, 4.8), rotation=(8, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 20805 + i, 2)
