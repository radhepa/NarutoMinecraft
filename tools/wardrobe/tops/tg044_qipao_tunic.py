"""Qipao Tunic: a sleeveless tunic cut like a qipao, a mandarin collar, a diagonal closure from the
throat to the right armpit fastened with knot buttons, and split panels front and back to mid-thigh
over whatever is worn beneath."""
from kit import flaps
from kit_kunoichi import frog_buttons, mandarin_collar
from paint import cap, strip_fabric

META = {
    "name": "Qipao Tunic",
    "gender": "female",
    "description": "Sleeveless qipao-cut tunic, mandarin collar, knot buttons, split panels to mid-thigh.",
    "tags": ["shinobi", "chunin", "tunic"],
    "rejects": ["skirt"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "smooth", 33060, 2)
    cap(body, "P", texture="smooth", seed=33060)
    f = body.front
    for y in range(4):
        f.set(4 - y, y + 1, "A2")
    frog_buttons(f, [(4, 1), (2, 3), (0, 4)])
    f.vline(2, 6, 10, "P1"), f.vline(5, 6, 10, "P3")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "P1")
    for side in ("right", "left"):
        g.part(f"{side}_arm").strip.hline(0, 15, 0, "A2")
    mandarin_collar(g, "collar", "P", 33061, trim="A2")
    for face in flaps(g, "panel", 6, "P", "smooth", 33062, width=7, hem="A2", top=10.6):
        face.vline(0, 1, 5, "P1"), face.vline(6, 1, 5, "P3")
