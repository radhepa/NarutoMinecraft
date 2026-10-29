"""Elder Haori: an elder's dark, mid-thigh haori worn open over a pale wrap kimono, with wide
sleeves, a lavender cord tied across the chest and the clan crest between the shoulders."""
from kit_hyuga import crest, wrap_front
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Elder Haori",
    "gender": "unisex",
    "description": "Dark mid-thigh haori open over a pale wrap kimono, lavender cord, crest on the back.",
    "tags": ["hyuga", "robe", "wrap", "haori"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # The kimono beneath: pale, wrapped, with a dark sash at the waist.
    strip_fabric(body, "S", "velvet", 4691, 2)
    cap(body, "S", texture="velvet", seed=4691)
    wrap_front(body.front, role="S", trim="A1", rows=7, start=2)
    body.strip.hline(0, body.strip.w - 1, 8, "D1"), body.strip.hline(0, body.strip.w - 1, 9, "D2")
    # The haori: everywhere but the open front.
    strip_fabric(jacket, "P", "velvet", 4692, 2)
    cap(jacket, "P", texture="velvet", seed=4692)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P3"), jacket.front.set(6, y, "P1")
    jacket.back.vline(3, 6, 11, "P1")
    crest(g, "back_crest", "P", "S3", pivot=(0, 1.4, 2.3), seed=4693)
    # Lapels, the cord and its two tassels.
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 11, 1), pivot=(x, .1, -2.8))
        solid(lapel, "P", "velvet", 4694, 2)
        lapel.front.vline(0, 0, 10, "P3")
    cord = g.piece("cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 5.0, -2.95), scale=(1, .5, .5))
    solid(cord, "A", "weave", 4695, 2, edge=False)
    knot = g.piece("cord_knot", "TORSO", (-.5, 0, 0), (1, 2, 1), pivot=(0, 5.0, -3.0), scale=(1, 1, .5))
    solid(knot, "A", "weave", 4696, 3, edge=False)
    # Wide sleeves to the wrist over the kimono's pale cuffs.
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "velvet", 4697, 2, 0, 10)
        strip_fabric(sleeve, "P", "velvet", 4698, 2, 0, 3)
        fabric(sleeve.top, "P", "velvet", 4698, 3)
        ox = -3.0 if side == "right" else -1.0
        cuff = g.piece(f"{side}_wide_sleeve", bone, (ox - .6, 2.0, -2.6), (5, 7, 5), inflate=.15)
        solid(cuff, "P", "velvet", 4699 + (side == "left"), 2)
        cuff.bottom.fill("S1")
        for face in cuff.sides:
            face.hline(0, face.w - 1, 6, "P1")
    # Skirts: two open front halves and the back, to mid-thigh.
    for name, x0, w, z, motion, face in (("skirt_front_right", -4.7, 3, -3.0, "flap_front", "front"),
                                          ("skirt_front_left", 1.7, 3, -3.0, "flap_front", "front"),
                                          ("skirt_back", -4.7, 9, 2.0, "flap_back", "back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 6, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "velvet", 4701 + w, 2)
        getattr(skirt, face).hline(0, w - 1, 5, "P1")
    for name, x in (("skirt_right", -5.1), ("skirt_left", 4.1)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 5, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "velvet", 4705, 2)
