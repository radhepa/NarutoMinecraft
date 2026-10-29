"""Ink Smock: a clan artisan's working dress, after Sai's brushwork: an off-white shirt with the
sleeves rolled to the elbow, a dark canvas apron on neck straps with an ink pot and a brush in
its pocket, and a few ink spots on the cloth."""
from kit import roll
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ink Smock",
    "gender": "unisex",
    "description": "Off-white shirt with rolled sleeves, a dark apron with an ink pot and brush, ink spots.",
    "tags": ["shinobi", "civilian"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 13640, 2)
    cap(body, "S", seed=13640)
    body.front.set(3, 0, "S1"), body.front.set(4, 0, "S1"), body.front.set(4, 1, "S1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 13641 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "S", "weave", 13641, 3)
    roll(g, "S", 3.4, prefix="sleeve_roll")
    # The apron: a bib on neck straps, then a skirt to the knee that swings with the stride.
    apron = g.piece("apron_bib", "TORSO", (-3, 0, 0), (6, 9, 1), pivot=(0, 2.0, -2.7))
    solid(apron, "D", "twill", 13643, 2)
    apron.front.hline(0, 5, 0, "D3")
    for x, y in ((1, 5), (4, 2), (2, 7)):
        apron.front.set(x, y, "K1")
    for i, x in enumerate((-2.6, 2.6)):
        strap = g.piece(f"apron_strap_{i}", "TORSO", (-.5, 0, 0), (1, 3, 5), pivot=(x, -.4, -2.5), inflate=.06)
        solid(strap, "D", "twill", 13644 + i, 2, edge=False)
    tie = g.part("jacket")
    tie.strip.hline(0, tie.strip.w - 1, 8, "D2")
    skirt = g.piece("apron_skirt", "TORSO", (-3.5, 0, 0), (7, 7, 1), pivot=(0, 10.8, -2.85), motion="flap_front")
    solid(skirt, "D", "twill", 13646, 2)
    skirt.front.hline(0, 6, 0, "D3"), skirt.front.set(5, 3, "K1")
    pot = g.piece("ink_pot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(.4, 4.2, -3.6))
    solid(pot, "K", "smooth", 13647, 2, edge=False)
    pot.top.fill("K3")
    brush = g.piece("brush", "TORSO", (-.5, -3, -.5), (1, 4, 1), pivot=(-1.4, 5.2, -3.4), rotation=(0, 0, 12))
    solid(brush, "L", "smooth", 13648, 3, edge=False)
    for face in brush.sides:
        face.set(0, 3, "K1")
