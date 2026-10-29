"""Cropped Mesh Jacket: a short open jacket ending above the ribs with elbow-length sleeves and a
turned-back collar, worn over a chain-mesh undershirt that runs down to the waistband."""
from kit import collar, sleeves
from kit_shinobi import mesh
from paint import fabric, strip_fabric

META = {
    "name": "Cropped Mesh Jacket",
    "gender": "unisex",
    "description": "Short open jacket to the ribs, elbow sleeves, over a chain-mesh undershirt.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "plain", 33020, 1, 0, 11)
    mesh(body.strip, 0, 0, body.strip.w - 1, 11, "K3")
    fabric(body.top, "K", "plain", 33020, 2)
    strip_fabric(jacket, "P", "plain", 33021, 2, 0, 5)
    fabric(jacket.top, "P", "plain", 33021, 3)
    # Open front: the mesh shows between the lapels, which are lit on their edges.
    for y in range(6):
        for x in range(3, 5):
            jacket.front.clear(x, y)
        jacket.front.set(2, y, "P3"), jacket.front.set(5, y, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 5, "P1")
    jacket.front.set(2, 5, "A2"), jacket.front.set(5, 5, "A2")
    sleeves(g, "P", "plain", 33022, rows=(0, 5), layer="sleeve", cuff="A2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        mesh(arm.strip, 0, 6, arm.strip.w - 1, 9, "K3")
        strip_fabric(arm, "K", "smooth", 33024, 2, 10, 11)
    neck = collar(g, "collar", "P", "plain", height=1, y=-.9)
    neck.front.hline(3, 5, 0, "P0")
