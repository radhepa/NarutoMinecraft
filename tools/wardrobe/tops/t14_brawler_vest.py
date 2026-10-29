"""Brawler Vest: an open sleeveless vest in deep red over a chain-mesh shirt, a mustard sash knotted
at the hip and bandaged forearms: the genin who settles things with taijutsu."""
from glyphs import LEAF, stamp
from kit import belt
from kit_shinobi import bandage, mesh
from paint import fabric, solid, strip_fabric

META = {
    "name": "Brawler Vest",
    "gender": "unisex",
    "description": "Open red vest over a mesh shirt, a knotted mustard sash and bandaged forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # Chain mesh over bare skin, with a dark band at the neck.
    mesh(body.strip, 0, 0, body.strip.w - 1, 9)
    mesh(body.top, 0, 0, body.top.w - 1, body.top.h - 1)
    body.front.hline(2, 5, 0, "K1")
    # The vest hangs open down the middle, its edges trimmed in mustard.
    strip_fabric(jacket, "P", "weave", 281, 2, 0, 9)
    fabric(jacket.top, "P", "weave", 281, 3)
    f = jacket.front
    for y in range(10):
        for x in range(3, 5):
            f.set(x, y, None)
    f.vline(2, 0, 9, "A2"), f.vline(5, 0, 9, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "P1")
    f.set(2, 9, "A1"), f.set(5, 9, "A1")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 2, 8, "P1")
    # Mesh short sleeves and bandaged forearms.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 2)
        mesh(arm.top, 0, 0, arm.top.w - 1, arm.top.h - 1)
        arm.strip.hline(0, arm.strip.w - 1, 3, "K1")
        bandage(arm.strip, 0, 7, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 7, "S2")
    # Mustard sash with a knot on the left hip and two hanging tails.
    sash = belt(g, "sash", y=9.4, role="A", buckle=None)
    sash.front.hline(0, sash.front.w - 1, 1, "A1")
    knot = g.piece("sash_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(1.6, 9.4, -3.1))
    solid(knot, "A", "weave", 282, 3, edge=False)
    for i, x in enumerate((1.7, 2.7)):
        tail = g.piece(f"sash_tail_{i}", "TORSO", (0, 0, 0), (1, 4 - i, 1), pivot=(x, 11.2, -3.0),
                       rotation=(0, 0, 8 - 16 * i), motion="flap_front")
        solid(tail, "A", "weave", 283 + i, 2)
    # The leaf in mustard across the back of the vest.
    crest = g.piece("back_leaf", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 2.4, 2.55), scale=(.5, .5, .5))
    fabric(crest.back, "P", "weave", 285, 2)
    stamp(crest.back, LEAF, 0, 0, {"#": "A2"})
    for face in (crest.top, crest.bottom, crest.right, crest.left, crest.front):
        face.fill("P2")
