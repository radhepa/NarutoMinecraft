"""Waist-Wrap Trousers: narrow trousers under a short wrapped cloth that hangs to mid-thigh front and
back, a cord tied over it, the ankles wrapped above open sandals: dust skirt of the desert roads."""
from kit import flaps, legs, side_panels, waistband
from kit_rugged import leg_wraps
from kit_shinobi import sandals
from paint import solid

META = {"name": "Waist-Wrap Trousers", "gender": "unisex",
        "description": "Narrow trousers under a short wrapped waist cloth front and back, a cord, ankle wraps, sandals.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "twill", 35430, 2)
    legs(g, "D", "twill", 35431, 2, rows=(0, 8), crease=False)
    leg_wraps(g, 8, 9)
    sandals(g)
    for face in flaps(g, "waist_wrap", 5, "P", "weave", 35432, width=9, top=10.0):
        face.hline(0, face.w - 1, 4, "P0")
        face.vline(7, 1, 4, "P3")
    side_panels(g, "waist_wrap_side", 4, "P", "weave", hem="P0", top=10.0)
    cord = g.piece("waist_cord", "TORSO", (-4.5, 9.4, -2.5), (9, 1, 5), inflate=.3)
    for face in cord.faces:
        face.fill("A1")
    for face in cord.sides:
        for x in range(0, face.w, 2):
            face.set(x, 0, "A3")
    solid(g.piece("waist_cord_end", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(2.0, 10.2, -3.3), motion="flap_front"),
          "A", "plain", 35434, 2)
