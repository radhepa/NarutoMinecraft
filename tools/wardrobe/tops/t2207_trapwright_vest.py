"""Trapwright Vest: the trap-builder's long sleeveless work vest to mid-thigh, quilted with sashiko
and hung with pockets for wire and pegs, a coil of steel trip wire on the left hip, worn over an
indigo shirt with tekko hand guards and a cedar cord belt."""
from kit_kinoshita import sashiko
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Trapwright Vest",
    "gender": "unisex",
    "description": "Long sashiko-quilted work vest with pockets, a coil of trip wire, indigo shirt and hand guards.",
    "tags": ["shinobi", "kinoshita", "work"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 22421, 2)
    cap(body, "D", seed=22421)
    # The vest: sawdust cloth quilted all over, closed at the chest and open below.
    strip_fabric(jacket, "S", "weave", 22422, 2)
    cap(jacket, "S", seed=22422)
    for face in jacket.sides:
        sashiko(face, "S1", 0, 1, face.w, 11, step=3)
    jacket.front.vline(3, 0, 11, "S0"), jacket.front.set(3, 0, None), jacket.front.set(4, 0, None)
    for y in range(7, 12):
        jacket.front.clear(3, y), jacket.front.clear(4, y)
    jacket.front.vline(2, 7, 11, "S1"), jacket.front.vline(5, 7, 11, "S1")
    # Two breast pockets and two hip pockets.
    for i, (x, y) in enumerate(((-3.6, 2.8), (1.4, 2.8), (-3.8, 8.6), (1.8, 8.6))):
        pocket = g.piece(f"pocket_{i}", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(x, y, -2.85))
        solid(pocket, "S", "weave", 22423 + i, 2, edge=False)
        pocket.front.hline(0, 1, 0, "S0")
    cord = g.piece("cord_belt", "TORSO", (-4.6, 7.4, -2.6), (9, 1, 5), inflate=.32)
    for face in cord.faces:
        face.paint(lambda x, y, cur: "A3" if x % 2 else "A1")
    # The skirts of the vest, split at the front.
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 4, -2.95, "flap_front"),
                                   ("skirt_front_left", .6, 4, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 5, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "S", "weave", 22427, 2)
        face = skirt.front if z < 0 else skirt.back
        sashiko(face, "S1", 0, 1, w, 4, step=3)
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 4, 4), pivot=(x, 11.4, 0))
        solid(panel, "S", "weave", 22428, 2)
    # The coil of trip wire on the left hip.
    coil = g.piece("wire_coil", "TORSO", (-1.5, -1.5, -.5), (3, 3, 1), pivot=(4.9, 10.4, 0), rotation=(0, 90, 0))
    solid(coil, "M", "plain", 22429, 3, edge=False)
    for face in coil.faces:
        face.paint(lambda x, y, cur: "M1" if (x + y) % 2 else cur)
    coil.left.set(1, 1, "K0"), coil.right.set(1, 1, "K0")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 22430 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "weave", 22430, 3)
        fabric(arm.strip, "S", "weave", 22432, 3, 0, 9, arm.strip.w, 2)
        arm.strip.hline(0, arm.strip.w - 1, 9, "S1")
