"""Mesh Tank: a tank top over a long-sleeved chain-mesh shirt, the mesh showing at the neck and down
both arms to the wrist, with a leaf printed on the back: the genin who trains like a chunin."""
from kit_academy import back_crest
from kit_shinobi import mesh
from paint import cap, strip_fabric

META = {
    "name": "Mesh Tank",
    "gender": "unisex",
    "description": "Tank top over a long-sleeved mesh shirt showing at the neck and arms, a leaf on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 31255, 2)
    cap(body, "P", seed=31255)
    f = body.front
    for x in (2, 3, 4, 5):
        f.set(x, 0, "K2")
    f.set(3, 1, "K2"), f.set(4, 1, "K1")
    for face in (body.front, body.back):
        face.set(0, 0, "K2"), face.set(7, 0, "K2")
        face.set(1, 0, "A2"), face.set(6, 0, "A2")
    for face in (body.right, body.left):
        face.hline(0, face.w - 1, 0, "K2"), face.hline(0, face.w - 1, 1, "A2")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 10, "K2")
        mesh(arm.top, 0, 0, arm.top.w - 1, arm.top.h - 1, "K2")
        arm.strip.hline(0, arm.strip.w - 1, 10, "K1")
    back_crest(g, "P", "A2", 31256, y=2.6)
