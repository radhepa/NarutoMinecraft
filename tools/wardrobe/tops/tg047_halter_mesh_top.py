"""Halter Mesh Top: a halter-neck top tied behind the neck, bare shoulders under a chain-mesh yoke,
a wide waistband and wrapped wrists."""
from kit_kunoichi import arm_warmers
from kit_shinobi import mesh
from paint import cap, fabric, strip_fabric

META = {
    "name": "Halter Mesh Top",
    "gender": "female",
    "description": "Halter-neck top with a mesh yoke over bare shoulders, wide waistband, wrapped wrists.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 33120, 2, 2, 11)
    mesh(body.strip, 0, 0, body.strip.w - 1, 1, "K3")
    fabric(body.top, "K", "plain", 33120, 3)
    f = body.front
    # The halter: a narrowing front panel up to the neck tie.
    for y in range(3):
        f.set(2 - y // 2, y + 1, "P3"), f.set(5 + y // 2, y + 1, "P1")
    f.hline(2, 5, 0, "P2"), f.hline(3, 4, 1, "P2")
    body.back.hline(3, 4, 0, "P2"), body.back.set(3, 1, "P1")
    for y in (8, 9):
        body.strip.hline(0, body.strip.w - 1, y, "S2" if y == 8 else "S1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    arm_warmers(g, "S", 33121, rows=(8, 10), band="P2")
