"""Rivet Gambeson: a padded gunmetal jacket stitched in channels against blows, a short stand collar, rows of
steel rivets down the front closure and rust cord ties at the side, sleeves to the wrist under
plated bracers."""
from kit import collar, sleeves
from kit_hagane import bracers
from paint import cap, strip_fabric

META = {
    "name": "Rivet Gambeson",
    "gender": "unisex",
    "description": "Padded gunmetal jacket with a stand collar, steel rivets down the front, rust side ties, bracers.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 21950, 2)
    cap(body, "P", seed=21950)
    strip_fabric(jacket, "P", "weave", 21951, 2, 0, 11)
    cap(jacket, "P", seed=21951)
    # Padded channels stitched across the body and down the sleeves.
    for y in (2, 5, 8):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P1")
        jacket.strip.hline(0, jacket.strip.w - 1, y + 1, "P3")
    jacket.front.vline(3, 0, 11, "P1")
    for y in range(1, 11, 2):
        jacket.front.set(4, y, "M4"), jacket.front.set(2, y, "M3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P0")
    for face in (jacket.right, jacket.left):
        face.set(1, 5, "A3"), face.set(2, 5, "A2"), face.set(1, 8, "A3"), face.set(2, 8, "A2")
    for arm in sleeves(g, "P", "weave", 21952, 2, rows=(0, 11)):
        arm.strip.hline(0, arm.strip.w - 1, 11, "P1")
        for y in (2, 5):
            arm.strip.hline(0, arm.strip.w - 1, y, "P1")
    c = collar(g, "collar", "P", "plain", base=2, height=2, y=-1.6, inflate=.08)
    c.front.hline(3, 5, 0, "P0"), c.front.set(4, 1, "M3")
    bracers(g, top=7.0, height=4, seed=21953, inflate=.1)
