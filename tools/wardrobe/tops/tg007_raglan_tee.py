"""Raglan Tee: a baseball-cut tee whose three-quarter sleeves run in one contrast piece right up to the
collar, the seam slanting across the chest and back, with a small chest pocket."""
from kit_academy import shirt
from paint import k

META = {
    "name": "Raglan Tee",
    "gender": "unisex",
    "description": "Baseball tee with contrast three-quarter raglan sleeves, slanted seams and a chest pocket.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "S", "plain", 31090, sleeve=7, sleeve_role="A")
    for face in (body.front, body.back):
        for y in range(4):
            for x in range(0, 3 - y):
                face.set(x, y, "A2")
                face.set(7 - x, y, "A2")
            if 3 - y >= 0:
                face.set(3 - y, y, "A1"), face.set(4 + y, y, "A1")
        face.hline(3, 4, 0, k("A", 1))
    for face in (body.right, body.left):
        for y in range(4):
            face.hline(0, face.w - 1, y, "A2")
        face.hline(0, face.w - 1, 4, "A1")
    body.top.fill("A3")
    for arm in arms:
        arm.strip.hline(0, arm.strip.w - 1, 7, "A1")
    f = body.front
    f.rect(5, 4, 2, 2, "S3"), f.hline(5, 6, 4, "A2"), f.vline(4, 5, 5, "S1")
    body.strip.hline(0, body.strip.w - 1, 11, "S1")
