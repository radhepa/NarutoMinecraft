"""Warring Armor: young Danzo in the Warring States and under the Second Hokage: a dark high-necked
shirt under laced grey lamellar armor, rounded shoulder guards, short tassets over the hips and
bandaged forearms, the Shimura crest worn small on the back."""
from kit import flaps
from kit_shimura import back_crest
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Warring Armor",
    "gender": "unisex",
    "description": "Dark high-necked shirt under laced grey lamellar armor, round shoulder guards, tassets, bandaged forearms.",
    "tags": ["shinobi", "armor"],
}


def lamellae(face, rows, lace="K1"):
    """Overlapping horizontal plates, each light at its top edge, laced through at every third column."""
    for y in rows:
        face.hline(0, face.w - 1, y, "P3" if y % 2 == 0 else "P1")
    for x in range(1, face.w, 3):
        for y in rows:
            if y % 2 == 1:
                face.set(x, y, lace)


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 13540, 2)
    cap(body, "D", seed=13540)
    strip_fabric(jacket, "P", "plain", 13541, 2, 0, 8)
    cap(jacket, "P", seed=13541)
    lamellae(jacket.strip, range(0, 9))
    jacket.strip.hline(0, jacket.strip.w - 1, 8, "K1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 8, "K2")
    neck = g.piece("high_neck", "TORSO", (-2.5, -1.4, -2.4), (5, 2, 5))
    solid(neck, "D", "weave", 13542, 2)
    for side, bone, x in (("right", "RIGHT_ARM", -3.6), ("left", "LEFT_ARM", -1.4)):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 13543 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "D", "weave", 13543, 3)
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "S1")
        guard = g.piece(f"{side}_shoulder_guard", bone, (x, -2.6, -2.6), (5, 4, 5))
        solid(guard, "P", "plain", 13545 + (side == "left"), 2)
        for face in guard.sides:
            lamellae(face, range(0, 4))
        fabric(guard.top, "P", "plain", 13547, 3)
    for face in flaps(g, "tasset", 3, "P", "plain", 13548, width=9, top=9.0, front_z=-2.9, back_z=1.9):
        face.hline(0, face.w - 1, 1, "P1")
        for x in (2, 6):
            face.vline(x, 0, 2, "K1")
    back_crest(g, "P", ink="A2", y=1.4, z=2.6, texture="plain")
