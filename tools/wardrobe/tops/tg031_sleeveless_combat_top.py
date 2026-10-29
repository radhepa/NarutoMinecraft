"""Sleeveless Combat Top: a fitted sleeveless top with a short mock neck and darker side panels, bare
shoulders, plated forearm guards over fingerless gloves and a plain belt: built for taijutsu."""
from kit import belt
from kit_field import arm_guards, collar, gloves, shirt

META = {
    "name": "Sleeveless Combat Top",
    "gender": "unisex",
    "description": "Fitted sleeveless top with a mock neck and side panels, plated forearm guards and gloves.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = shirt(g, "P", 32200, sleeve=-1, texture="knit")
    for face in (body.right, body.left):
        face.rect(0, 2, 4, 9, "D2")
        face.vline(0, 2, 10, "D1")
    for face in (body.front, body.back):
        face.vline(0, 2, 10, "P1"), face.vline(7, 2, 10, "P1")
    neck = collar(g, "mock_neck", "P", 32202, style="low")
    neck.front.set(4, 0, "P1")
    gloves(g, "K", 32203)
    arm_guards(g, 32205, role="D", y=5.2, height=3)
    belt(g, "belt", y=9.6, role="K")
