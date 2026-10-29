"""Seal Tabard: a sleeveless tabard of the sealing corps over a long-sleeved shirt, open at the
sides, its edges bound with seal tags and the long panels belted with a twisted rope at the waist."""
from kit_specialist import seal_trim, shirt
from paint import fabric, solid

META = {
    "name": "Seal Tabard",
    "gender": "unisex",
    "description": "Tag-edged tabard over a long-sleeved shirt, rope belt, long front and back panels.",
    "tags": ["shinobi", "tunic", "chunin"],
}


def build(g):
    shirt(g, "S", "weave", 34100, cuff="S1")
    jacket = g.part("jacket")
    for face in (jacket.front, jacket.back):
        fabric(face, "P", "twill", 34101, 2)
        face.hline(0, 7, 0, "P3")
        seal_trim(face, 0, 12, every=7, seed=34102)
    fabric(jacket.top, "P", "twill", 34101, 3)
    jacket.front.clear(3, 0), jacket.front.clear(4, 0)
    rope = g.piece("rope_belt", "TORSO", (-4.6, 9.0, -2.6), (9, 1, 5), inflate=.18)
    solid(rope, "A", "weave", 34103, 2, edge=False)
    for face in rope.sides:
        for x in range(0, face.w, 2):
            face.set(x, 0, "A3")
    for name, z, motion in (("tabard_front", -2.85, "flap_front"), ("tabard_back", 1.85, "flap_back")):
        panel = g.piece(name, "TORSO", (-3, 0, 0), (6, 6, 1), pivot=(0, 11.4, z), motion=motion)
        solid(panel, "P", "twill", 34104 + (z > 0), 2)
        seal_trim(panel.strip, 4, 2, every=3, seed=34106)
        panel.bottom.fill("S3")
    for i, x in enumerate((-.9, .1)):
        end = g.piece(f"rope_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 9.8, -3.2), rotation=(0, 0, 8 - 16 * i),
                      motion="sway")
        solid(end, "A", "weave", 34108 + i, 2)
