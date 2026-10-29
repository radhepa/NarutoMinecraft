"""Shop Happi: the short straight coat the stallholders wear on market and festival days, open
over a white undershirt, the collar bands printed with the shop's name, a big round shop mark on
the back and a sash tied low at the front."""
from kit import flaps
from kit_market import mark, open_front, sash, sleeves, stripes
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Shop Happi",
    "gender": "unisex",
    "description": "Short straight happi coat over a white undershirt, printed collar bands, shop mark on the back, low sash.",
    "tags": ["civilian", "jacket", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 36060, 3)
    cap(body, "S", seed=36060, base=3)
    strip_fabric(jacket, "P", "weave", 36061, 2)
    fabric(jacket.top, "P", "weave", 36061, 3)
    fabric(jacket.bottom, "P", "weave", 36061, 1)
    for y in range(12):
        for x in range(3, 5):
            jacket.front.clear(x, y)
    open_front(jacket.front, "S3", None, range(0, 12), left=2, right=5)
    for y in range(1, 12, 2):
        jacket.front.set(2, y, "K2"), jacket.front.set(5, y, "K2")
    mark(jacket.back, "maru", 1, 2, "S3")
    jacket.back.hline(0, 7, 9, "S3"), jacket.back.hline(0, 7, 10, "A2")
    sleeves(g, "P", "weave", 36062, rows=(0, 5), cuff="S3")
    for face in flaps(g, "happi_hem", 3, "P", "weave", 36064, width=9, top=11.0, front_z=-3.0, back_z=2.0, slit=True):
        face.hline(0, 8, 0, "S3"), face.hline(0, 8, 1, "A2")
        stripes(face, k("P", 1), 3, rows=[2])
    sash(g, "sash", "A", 36066, y=8.8, height=2, knot="front")
