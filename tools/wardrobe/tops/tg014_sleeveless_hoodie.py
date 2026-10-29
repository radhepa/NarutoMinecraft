"""Sleeveless Hoodie: a cut-off hoodie with the hood down and a zip pocket on the chest, worn with
ribbed arm warmers pulled up to the elbow: the genin who never stops moving."""
from kit_academy import drawstrings, hood_down, ribbed
from paint import cap, strip_fabric

META = {
    "name": "Sleeveless Hoodie",
    "gender": "unisex",
    "description": "Cut-off hoodie with the hood down, a chest zip pocket and ribbed arm warmers.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 31195, 2)
    cap(body, "P", seed=31195)
    for face in (body.right, body.left):
        face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 1, "P1")
    ribbed(body, (11,), "P")
    f = body.front
    f.hline(1, 3, 3, "M3"), f.hline(1, 3, 4, "P1")
    f.vline(5, 6, 9, "P1"), f.vline(2, 6, 9, "P1"), f.hline(2, 5, 6, "P3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "rib", 31196, 2, 5, 10)
        strip_fabric(sleeve, "K", "rib", 31197, 2, 4, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "S3")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "K1")
    hood_down(g, "P", "S", 31198, depth=2.9, tilt=18)
    drawstrings(g, "S3", 31200, length=3)
