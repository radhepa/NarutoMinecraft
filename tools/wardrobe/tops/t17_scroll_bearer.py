"""Scroll Bearer: a short blue wrap top crossed left over right with white trim, short kimono sleeves,
a red obi and a summoning scroll as long as the torso slung across the back on a cord."""
from kit import belt, flaps
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Scroll Bearer",
    "gender": "unisex",
    "description": "Blue wrap top with white trim, red obi, wrapped wrists and a great scroll across the back.",
    "tags": ["shinobi", "genin"],
}

SCROLL = dict(bone="TORSO", pivot=(0, 5.0, 4.1), rotation=(0, 0, 50))


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 321, 2)
    cap(body, "P", texture="weave", seed=321)
    f = body.front
    # The wrap: a white edge running from the right shoulder down to the left hip.
    for y in range(8):
        f.set(y, y, "S3")
        if y + 1 <= 7:
            f.set(y + 1, y, "S2")
        if y + 2 <= 7:
            f.set(y + 2, y, "P1")
    # Short kimono sleeves with a white hem, wrapped wrists below.
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 322 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 322, 3)
        strip_fabric(sleeve, "P", "weave", 324, 2, 0, 4)
        fabric(sleeve.top, "P", "weave", 324, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "S3")
        bandage(arm.strip, 0, 8, arm.strip.w - 1, 10)
    obi = belt(g, "obi", y=7.8, role="A", height=3, buckle=None, inflate=.12)
    obi.front.hline(0, obi.front.w - 1, 1, "K1"), obi.back.hline(0, obi.back.w - 1, 1, "K1")
    for face in flaps(g, "hem", 3, "P", "weave", 325, top=10.6, hem="S3"):
        face.hline(0, face.w - 1, 1, "P1")
    # The cord holding the scroll, crossing the chest from the left shoulder to the right hip.
    cord = g.piece("cord", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 4.8, -2.4), rotation=(0, 0, -40))
    solid(cord, "L", "leather", 326, 2, edge=False)
    # The scroll: cream paper rolled around a dark core, red end caps and a tie band in the middle.
    roll = g.piece("scroll", SCROLL["bone"], (-2, -7, -2), (4, 14, 4), pivot=SCROLL["pivot"], rotation=SCROLL["rotation"])
    solid(roll, "S", "plain", 327, 3, edge=False)
    for face in roll.sides:
        face.hline(0, face.w - 1, 6, "A2"), face.hline(0, face.w - 1, 7, "A1")
        face.vline(face.w // 2, 0, 13, "S2")
    for i, y in enumerate((-8, 7)):
        end = g.piece(f"scroll_cap_{i}", SCROLL["bone"], (-2.5, y, -2.5), (5, 1, 5), pivot=SCROLL["pivot"],
                      rotation=SCROLL["rotation"])
        solid(end, "A", "smooth", 328 + i, 2)
        (end.top if i == 0 else end.bottom).set(2, 2, "L1")
