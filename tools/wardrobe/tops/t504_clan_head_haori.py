"""Clan Head Haori: a loose knee-length haori worn open over a dark kimono shirt and flak vest
ribbing, the Nara crest large across the back, shadow-black cuffs. The clan head at ease."""
from kit_nara import back_crest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Clan Head Haori",
    "gender": "unisex",
    "description": "Open knee-length haori with the crest across the back over a dark kimono shirt.",
    "tags": ["shinobi", "coat", "nara"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 5531, 2)
    cap(body, "D", seed=5531)
    # The kimono shirt crossed left over right under the haori.
    for y in range(6):
        body.front.set(2 + y // 2 + 1, y, "S3"), body.front.set(5 - y // 2 - 1, y, "D1")
    strip_fabric(jacket, "P", "weave", 5532, 2)
    cap(jacket, "P", seed=5532)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P3")
        jacket.front.set(6, y, "P1")
    back_crest(g, "P", "K1", 5533, y=1.4)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 5534, 2, 0, 10)
        fabric(arm.top, "P", "weave", 5534, 3)
        strip_fabric(sleeve, "P", "weave", 5535 + (side == "left"), 2, 0, 9)
        fabric(sleeve.top, "P", "weave", 5535, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "K2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "K1")
    # Wide lapels down the open front.
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 12, 1), pivot=(x, -.4, -2.75))
        solid(lapel, "P", "weave", 5537, 2)
        lapel.front.vline(0, 0, 11, "K2")
    # The skirts to the knee, open at the front.
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 7, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 5538, 2)
        for face in skirt.sides:
            face.hline(0, face.w - 1, 6, "K2")
    for name, x in (("right", -5.0), ("left", 4.0)):
        side = g.piece(f"skirt_side_{name}", "TORSO", (0, 0, -2), (1, 7, 4), pivot=(x, 11.4, 0))
        solid(side, "P", "weave", 5539, 2)
        for face in side.sides:
            face.hline(0, face.w - 1, 6, "K2")
