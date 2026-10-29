"""Sealer Coat: a long coat worn open over a dark shirt, its lapels lined with seal tags, a belt hung
with paper tags and an ink scroll, long tails edged in tags, and the whirlpool on the back."""
from kit import belt
from kit_uzumaki import crest_patch, seal_tags
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Sealer Coat",
    "gender": "unisex",
    "description": "Long open coat with seal-tag lapels and hem, tag-hung belt, ink scroll, whirlpool crest.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 2280, 2)
    cap(body, "D", seed=2280)
    strip_fabric(jacket, "P", "twill", 2281, 2)
    cap(jacket, "P", seed=2281)
    for x in range(2, 6):
        for y in range(12):
            jacket.front.clear(x, y)
    seal_tags(jacket.front, 0, 12, every=5, seed=2282, start=1)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 2283, 2, 0, 10)
        fabric(arm.top, "P", "twill", 2283, 3)
        strip_fabric(sleeve, "P", "twill", 2284, 2, 0, 9)
        fabric(sleeve.top, "P", "twill", 2284, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "A2")
    crest_patch(g, "back_crest", "TORSO", (0, 1.2, 2.3), ground="P2", ink="A2")
    belt(g, "belt", y=8.6, role="L", height=1, buckle="M", inflate=.6)
    for i, (x, rz) in enumerate(((-3.6, 6), (-2.7, -4), (3.2, 5))):
        tag = g.piece(f"belt_tag_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 9.6, -3.15), rotation=(0, 0, rz),
                      motion="sway")
        solid(tag, "S", "plain", 2285 + i, 3, edge=False)
        tag.front.set(0, 1, "K1"), tag.front.set(0, 3, "A2")
    scroll = g.piece("ink_scroll", "TORSO", (-.5, -3, -.5), (2, 6, 2), pivot=(4.2, 9.0, 1.2), rotation=(0, 0, -30))
    solid(scroll, "S", "plain", 2288, 3, edge=False)
    for face in scroll.sides:
        face.hline(0, face.w - 1, 0, "A2"), face.hline(0, face.w - 1, 5, "A2")
    # Long tails: the open front halves and the back, each edged in a row of seal tags.
    for name, x0, w, z, motion, face_name in (("tail_front_right", -4.6, 3, -3.05, "flap_front", "front"),
                                               ("tail_front_left", 1.6, 3, -3.05, "flap_front", "front"),
                                               ("tail_back", -4.6, 9, 2.05, "flap_back", "back")):
        tail = g.piece(name, "TORSO", (0, 0, 0), (w, 8, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(tail, "P", "twill", 2289 + len(name), 2)
        face = getattr(tail, face_name)
        face.hline(0, w - 1, 0, "P3")
        seal_tags(face, 5, 3, every=3, seed=2290, start=1)
