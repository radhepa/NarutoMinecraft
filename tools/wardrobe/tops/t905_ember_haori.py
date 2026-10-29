"""Ember Haori: the clan head at a festival or a council. A thigh-length haori over a dark kimono,
flame tongues rising from its hem and sleeve ends, the Sarutobi crest on the back and a cord
tying the fronts across the chest."""
from kit import flaps
from kit_sarutobi import crest_patch, flame_hem
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Ember Haori",
    "gender": "unisex",
    "description": "Thigh-length haori with flames at the hem and sleeves, the crest on the back, over a dark kimono.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 9790, 2)
    cap(body, "K", seed=9790)
    # The kimono's crossed collar in the gap between the haori fronts.
    for i in range(5):
        body.front.set(2 + i // 2 if i < 4 else 4, i, "S3")
    strip_fabric(jacket, "P", "velvet", 9791, 2)
    cap(jacket, "P", texture="velvet", seed=9791)
    fr = jacket.front
    for y in range(12):
        fr.set(3, y, None), fr.set(4, y, None)
        fr.set(2, y, "S3"), fr.set(5, y, "S3")
    # The cord across the chest.
    fr.set(2, 4, "A3"), fr.set(5, 4, "A3")
    knot = g.piece("cord_knot", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 4.0, -2.75))
    solid(knot, "A", "weave", 9792, 3)
    for face in flaps(g, "haori", 5, "P", "velvet", 9793, width=9, hem=None, top=11.4, front_z=-2.85, back_z=1.85):
        flame_hem(face, 0, k("A", 2), k("A", 4))
        if face.name == "front":
            face.vline(4, 0, 4, k("K", 1))
    for face in (jacket.right, jacket.left, jacket.back, jacket.front):
        for x in range(face.w):
            face.set(x, 11, k("P", 1))
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "weave", 9794, 2, 0, 10)
        fabric(arm.top, "K", "weave", 9794, 3)
        strip_fabric(sleeve, "P", "velvet", 9795 + (side == "left"), 2, 0, 7)
        fabric(sleeve.top, "P", "velvet", 9795, 3)
        flame_hem(sleeve.strip, 3, k("A", 2), k("A", 4))
        sleeve.strip.hline(0, sleeve.strip.w - 1, 7, k("A", 1))
    crest_patch(g, "back_crest", "TORSO", (0, 1.2, 2.33), "P", "S3", 9797, ground="A2")
