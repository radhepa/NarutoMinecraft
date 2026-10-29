"""Commander Coat: a long navy field coat worn open over the jonin flak vest, trimmed in red, with
the Hidden Leaf crest in white across the back: the jonin who leads the village's squads."""
from glyphs import LEAF, stamp
from kit import collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Commander Coat",
    "gender": "unisex",
    "description": "Long navy coat with red trim and a white leaf crest, open over a green flak vest.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # Under-layer: the flak vest's ribbing and zip.
    strip_fabric(body, "P", "rib", 421, 2)
    cap(body, "P", seed=421)
    for y in (3, 6, 9):
        body.strip.hline(0, body.strip.w - 1, y, "P1")
    body.front.vline(3, 0, 11, "P0"), body.front.vline(4, 0, 11, "P3")
    # The coat: navy everywhere but the open front, red piping down both edges.
    strip_fabric(jacket, "D", "weave", 422, 2)
    cap(jacket, "D", seed=422)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "A2"), f.set(6, y, "A2")
    crest = g.piece("back_crest", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 2.0, 2.3))
    fabric(crest.back, "D", "weave", 423, 2)
    stamp(crest.back, LEAF, 0, 0, {"#": "S3"})
    crest.back.hline(0, 7, 7, "A2")
    for face in (crest.top, crest.bottom, crest.right, crest.left, crest.front):
        face.fill("D2")
    # Coat sleeves to the wrist with red cuffs.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 424, 2, 0, 10)
        fabric(arm.top, "D", "weave", 424, 3)
        strip_fabric(sleeve, "D", "weave", 425 + (side == "left"), 2, 0, 9)
        fabric(sleeve.top, "D", "weave", 425, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "A2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "A1")
    neck = collar(g, "vest_collar", "P", "rib", height=2, y=-1.4)
    neck.front.hline(3, 5, 0, "P0")
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 12, 1), pivot=(x, -.4, -2.75))
        solid(lapel, "D", "weave", 427, 2)
        lapel.front.vline(0, 0, 11, "A2")
    for i, x in enumerate((-3.5, 1.5)):
        pocket = g.piece(f"scroll_pocket_{i}", "TORSO", (0, 0, 0), (2, 3, 1), pivot=(x, 4.5, -2.6))
        solid(pocket, "P", "rib", 428 + i, 2)
        pocket.front.hline(0, 1, 0, "P3")
    # Long skirts to the knee: the two open front halves, the back and the sides, hemmed in red.
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 9, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "D", "weave", 430 + len(name), 2)
        skirt.strip.hline(0, skirt.strip.w - 1, 8, "A2")
        skirt.bottom.fill("A1")
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 8, 4), pivot=(x, 11.4, 0))
        solid(panel, "D", "weave", 450, 2)
        panel.strip.hline(0, panel.strip.w - 1, 7, "A2")
        panel.bottom.fill("A1")
