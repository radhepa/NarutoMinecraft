"""Florist Apron: the flower shop's working wear, a lavender shirt with sleeves rolled to the elbow
under a cream bib apron with a pocket of blossoms, crossed straps behind and long apron ties."""
from kit import roll
from kit_yamanaka import floral_trim, flower
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Florist Apron",
    "gender": "unisex",
    "description": "Lavender shirt with rolled sleeves under a cream bib apron with a pocket of blossoms.",
    "tags": ["yamanaka", "florist"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 7450, 3)
    cap(body, "P", texture="weave", seed=7450, base=3)
    body.front.hline(2, 5, 0, "P1"), body.front.set(3, 1, "P1")
    # Crossed apron straps on the back.
    for y in range(9):
        body.back.set(1 + y * 6 // 9, y, "S2"), body.back.set(6 - y * 6 // 9, y, "S2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 7451 + (side == "left"), 3, 0, 4)
        fabric(arm.top, "P", "weave", 7451, 4)
    roll(g, "P", 4.0, base=3, accent="A3")
    # The bib and skirt of the apron, one panel standing proud of the shirt.
    bib = g.piece("apron_bib", "TORSO", (-3, 0, 0), (6, 9, 1), pivot=(0, 1.6, -2.75))
    solid(bib, "S", "weave", 7453, 3)
    floral_trim(bib.front, 0, "A", step=2)
    skirt = g.piece("apron_skirt", "TORSO", (-3.5, 0, 0), (7, 6, 1), pivot=(0, 10.4, -2.95), motion="flap_front")
    solid(skirt, "S", "weave", 7454, 3)
    floral_trim(skirt.front, 5, "A", ground="S2", step=3, start=1)
    pocket = g.piece("pocket", "TORSO", (-1.5, 0, 0), (3, 2, 1), pivot=(-1.0, 5.0, -3.5))
    solid(pocket, "S", "weave", 7455, 2)
    pocket.front.hline(0, 2, 0, "S4")
    flower(g, "bloom_0", (-1.6, 4.8, -3.9), bone="TORSO")
    flower(g, "bloom_1", (-.5, 4.4, -3.9), bone="TORSO", petal="P", base=4)
    for i, x in enumerate((-1.0, .8)):
        tie = g.piece(f"apron_tie_{i}", "TORSO", (-.5, 0, 0), (1, 5, 1), pivot=(x, 9.6, 2.1), rotation=(10, 0, 14 - 28 * i),
                      motion="sway")
        solid(tie, "S", "weave", 7456 + i, 3)
