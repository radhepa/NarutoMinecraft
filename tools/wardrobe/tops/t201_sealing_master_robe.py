"""Sealing Master Robe: the clan's long working robe, wrapped left over right with a collar trimmed in
seal tags, wide kimono sleeves inked round the openings, a red obi hung with paper tags, the
whirlpool crest across the back and a knee-length skirt edged in rolling waves."""
from kit import belt, flaps
from kit_uzumaki import crest_patch, seal_tags, waves, wide_sleeves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Sealing Master Robe",
    "gender": "unisex",
    "description": "Long wrapped robe, seal-tag collar, wide inked sleeves, red obi with tags, whirlpool crest.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 2210, 2)
    cap(body, "P", texture="weave", seed=2210)
    f = body.front
    # The wrap: a collar band of seal tags from the right shoulder to the left hip.
    for y in range(8):
        f.set(y, y, "S3"), f.set(min(7, y + 1), y, "S2")
        if y % 2:
            f.set(min(7, y + 1), y, "K1")
        if y + 2 <= 7:
            f.set(y + 2, y, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 2211, 3, 0, 9)
        fabric(arm.top, "P", "weave", 2211, 3)
    wide_sleeves(g, "P", "weave", 2212, top=1.0, length=7, drop=3, trim="A2", tags=True)
    obi = belt(g, "obi", y=7.4, role="A", height=3, buckle=None, inflate=.14)
    obi.front.hline(0, obi.front.w - 1, 1, "K1"), obi.back.hline(0, obi.back.w - 1, 1, "K1")
    for i, (x, rz) in enumerate(((2.4, 4), (3.4, -6), (-3.0, 8))):
        tag = g.piece(f"obi_tag_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 10.2, -2.8), rotation=(0, 0, rz),
                      motion="sway")
        solid(tag, "S", "plain", 2213 + i, 3, edge=False)
        tag.front.set(0, 1, "K1"), tag.front.set(0, 3, "A2")
    for face in flaps(g, "robe", 7, "P", "weave", 2216, width=9, hem="P1", top=10.4, front_z=-2.8, back_z=1.8):
        waves(face, 4, "S", 3)
        face.vline(0, 1, 6, "P1"), face.vline(8, 1, 6, "P1")
    crest_patch(g, "back_crest", "TORSO", (0, .6, 2.05), ground="P2", ink="A2")
    collar = g.piece("collar", "TORSO", (-4.5, -.9, -2.6), (9, 1, 5), inflate=.06)
    solid(collar, "S", "plain", 2217, 3)
    seal_tags(collar.back, 0, 1, every=2, seed=2218)
