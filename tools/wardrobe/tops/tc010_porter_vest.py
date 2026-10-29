"""Porter's Vest: the carrier's short sleeveless vest open over a sarashi chest wrap, a quilted pad
on the right shoulder where the carrying pole rides, a coil of rope at the hip and a sash."""
from kit_market import open_front, sash
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Porter's Vest",
    "gender": "unisex",
    "description": "Short open sleeveless vest over a chest wrap, a quilted shoulder pad, rope coil at the hip.",
    "tags": ["civilian", "vest", "work"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    for face in body.sides:
        for y in range(2, 8):
            for x in range(face.w):
                face.set(x, y, "S3" if (x + y) % 4 else "S2")
    strip_fabric(jacket, "P", "twill", 36200, 2, 0, 9)
    fabric(jacket.top, "P", "twill", 36200, 3)
    for y in range(10):
        for x in range(2, 6):
            jacket.front.clear(x, y)
    open_front(jacket.front, k("P", 3), None, range(0, 10), left=1, right=6)
    pad = g.piece("shoulder_pad", "RIGHT_ARM", (-3.5, -2.6, -2.5), (5, 2, 5), inflate=.1)
    solid(pad, "S", "quilt", 36202, 2)
    pad.top.fill("S3")
    sash(g, "sash", "A", 36204, y=8.8, height=2, knot="front")
    coil = g.piece("rope_coil", "TORSO", (-.5, -1.5, -1.5), (1, 3, 3), pivot=(4.9, 10.4, .4), motion="sway")
    solid(coil, "L", "weave", 36206, 3)
    for face in coil.faces:
        face.paint(lambda x, y, cur: "L2" if (x + y) % 2 else "L3")
    coil.left.set(1, 1, "L0")
