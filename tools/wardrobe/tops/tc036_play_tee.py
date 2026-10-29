"""Play Tee: the children's summer play shirt, cotton jersey in broad bands with a contrasting
neck rib and short sleeves, a patch pocket sewn on crooked and a little star appliqué on the chest,
grass-stained at the hem."""
from kit_household import arm_cloth, bands
from paint import cap, strip_fabric

META = {
    "name": "Play Tee",
    "gender": "unisex",
    "description": "Banded jersey play shirt with a contrasting neck rib, short sleeves, crooked pocket and star appliqué.",
    "tags": ["civilian", "casual"],
}

STAR = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (0, 3), (2, 3)]


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37200, 2)
    cap(body, "P", seed=37200)
    bands(body.strip, "S3", every=3, offset=1)
    f = body.front
    f.hline(2, 5, 0, "A2"), f.set(3, 1, "A2"), f.set(4, 1, "A2")
    for x, y in STAR:
        f.set(5 + x - 1, 3 + y, "A3")
    f.rect(1, 7, 3, 3, "D2"), f.hline(1, 3, 7, "D3"), f.set(3, 9, "D1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for x in (2, 9, 15):
        body.strip.set(x, 11, "L2")
    for arm in arm_cloth(g, "P", "plain", 37201, rows=(0, 3), hem="A2"):
        bands(arm.strip, "S3", every=3, offset=1, rows=range(0, 3))
