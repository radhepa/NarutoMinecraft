"""Split Apron Skirt: Sakura's Shippuden skirt, a rose wrap open at the front and sides over fitted
dark shorts, a medical pouch at the back of the belt and black knee boots."""
from kit import belt, flaps, footwear, pouch, side_panels
from paint import fabric, k, strip_fabric

META = {"name": "Split Apron Skirt", "gender": "unisex",
        "description": "Rose wrap skirt split at the front and sides over dark shorts, back pouch, black knee boots.",
        "tags": ["shinobi", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "smooth", 19720, 2, 9, 11)
    fabric(body.bottom, "K", "smooth", 19720, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "smooth", 19721, 2, 0, 3)
        fabric(leg.top, "K", "smooth", 19721, 2)
    footwear(g, "boot", top=5, role="K", base=2, sole="K0")
    for side in ("right", "left"):
        g.part(f"{side}_pants").front.hline(0, 3, 5, k("K", 4))
    belt(g, "waist_band", y=9.2, role="P", height=1, buckle=None, inflate=.2)
    for face in flaps(g, "waist_skirt", 5, "P", "smooth", 19722, width=9, hem=k("P", 3), top=10.2, front_z=-2.9,
                      back_z=1.9, slit=True):
        face.vline(0, 1, 4, k("P", 1)), face.vline(8, 1, 4, k("P", 1))
    side_panels(g, "waist_skirt_side", 5, "P", "smooth", hem=k("P", 3), top=10.2)
    pouch(g, "waist_pouch", (0, 9.4, 2.6), size=(3, 2, 1), role="S", flap=k("A", 3))
