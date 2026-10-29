"""Tenugui and Undershirt: high summer on the veranda, a ribbed white undershirt with bare arms
and a striped cotton tenugui towel slung round the neck, its ends hanging down the chest."""
from kit_household import stripes
from paint import cap, solid, strip_fabric

META = {
    "name": "Tenugui and Undershirt",
    "gender": "unisex",
    "description": "Ribbed white sleeveless undershirt with a striped tenugui towel slung round the neck.",
    "tags": ["civilian", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "rib", 37420, 3)
    cap(body, "S", texture="rib", seed=37420, base=3)
    f = body.front
    for x in (2, 3, 4, 5):
        f.set(x, 0, None)
    f.set(3, 1, None), f.set(4, 1, None)
    for face in (body.right, body.left):
        face.set(0, 0, None), face.set(3, 0, None)
    body.strip.hline(0, body.strip.w - 1, 11, "S2")
    ring = g.piece("towel_neck", "TORSO", (-3, 0, -2.5), (6, 1, 5), pivot=(0, -.4, 0), inflate=.16)
    solid(ring, "S", "plain", 37421, 4, edge=False)
    stripes(ring.strip, "D2", every=2)
    for side, x, rz in (("right", -2.0, 4), ("left", 2.0, -6)):
        end = g.piece(f"towel_{side}", "TORSO", (-1, 0, 0), (2, 6, 1), pivot=(x, 0, -2.7), rotation=(0, 0, rz), motion="sway")
        solid(end, "S", "plain", 37422 + (side == "left"), 4)
        for face in end.sides:
            face.hline(0, face.w - 1, 3, "D2"), face.hline(0, face.w - 1, 5, "D2")
