"""Stand-Collar Shirt: a short-sleeved shirt fastened down the side with cloth toggles, a high stand
collar, and a chain-mesh undershirt showing on the forearms: the genin who studies the old manuals."""
from kit import collar
from kit_academy import shirt
from kit_shinobi import mesh

META = {
    "name": "Stand-Collar Shirt",
    "gender": "unisex",
    "description": "Short-sleeved shirt fastened at the side with toggles, a high collar, mesh forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "P", "weave", 31105, sleeve=4, trim="P1")
    f = body.front
    # The placket: an edge from the collar over to the right side seam, three toggles along it.
    f.vline(5, 0, 11, "P3"), f.vline(6, 0, 11, "P1")
    for y in (1, 4, 7):
        f.set(5, y, "A2"), f.set(6, y, "A1")
    for face in (body.right, body.left):
        face.vline(1, 2, 10, "P1")
    for arm in arms:
        mesh(arm.strip, 0, 5, arm.strip.w - 1, 10, "K2")
        arm.strip.hline(0, arm.strip.w - 1, 10, "K1")
    neck = collar(g, "collar", "P", "weave", height=2, y=-1.8)
    neck.front.vline(5, 0, 1, "A2")
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "P3")
