"""Bandaged Tunic: a sleeveless high-necked tunic for training in the herb gardens, the forearms
wound in white bandages from wrist to elbow, a violet cord belt knotted at the front with a sprig
of white bells hanging from it."""
from kit_shinobi import bandage
from kit_suzuran import bell_charm
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Bandaged Tunic",
    "gender": "unisex",
    "description": "Sleeveless high-necked tunic, bandaged forearms, a violet cord belt with a hanging bell sprig.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 24591, 2)
    cap(body, "P", seed=24591)
    body.front.hline(2, 5, 0, "P3"), body.front.vline(1, 1, 7, "P1")
    for x in (2, 3):
        body.front.set(x, 2 + x, "S3")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for face in (body.right, body.left):
        face.vline(0, 0, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 5, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 5, "S4")
    cord = g.piece("cord", "TORSO", (-4.5, 8.4, -2.5), (9, 1, 5), inflate=.05)
    solid(cord, "A", "smooth", 24592, 2, edge=False)
    for face in cord.sides:
        for x in range(0, face.w, 2):
            face.set(x, 0, "A3")
    knot = g.piece("cord_knot", "TORSO", (-1, -.5, -.5), (2, 1, 1), pivot=(-1.4, 8.9, -2.9))
    solid(knot, "A", "smooth", 24593, 3, edge=False)
    for i, rz in enumerate((6, -10)):
        end = g.piece(f"cord_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(-1.6 + i * .6, 9.2, -2.9),
                      rotation=(0, 0, rz), motion="sway", scale=(.6, 1, .6))
        solid(end, "A", "smooth", 24594, 2, edge=False)
    bell_charm(g, "sprig", (-1.0, 11.6, -3.1), rotation=(0, 0, 70), bone="TORSO")
