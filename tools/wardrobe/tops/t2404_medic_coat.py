"""Lily Medic Coat: the jonin field medic's long porcelain-white coat, worn open over a jade
under-robe with a crossed collar, its tails hanging to the knee and trimmed along the hem with a
running line of white bells on green stems, deep cuffs turned back over long dark gloves and the
clan's bell crest on the back."""
from kit import belt
from kit_suzuran import back_crest, bell_hem, gloves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Lily Medic Coat",
    "gender": "unisex",
    "description": "Long open white coat over a jade under-robe, bell-trimmed knee tails, turned cuffs, gloves, crest.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 24531, 2)
    cap(body, "P", seed=24531)
    for y in range(4):
        body.front.set(3 - y // 2, y, "P3"), body.front.set(4 + y // 2, y, "P1")
    strip_fabric(jacket, "S", "weave", 24532, 3)
    cap(jacket, "S", seed=24532, base=3)
    for x in range(2, 6):
        for y in range(12):
            jacket.front.clear(x, y)
    jacket.front.vline(1, 0, 11, "D2"), jacket.front.vline(6, 0, 11, "D2")
    for face in (jacket.right, jacket.left):
        face.vline(2, 1, 11, "S2")
    belt(g, "sash", y=8.2, role="D", height=1, buckle=None, inflate=.02)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 24533 + (side == "left"), 3, 0, 6)
        fabric(arm.top, "S", "weave", 24533, 4)
        strip_fabric(sleeve, "S", "weave", 24535, 3, 0, 5)
        fabric(sleeve.top, "S", "weave", 24535, 4)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "D2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "S4")
    gloves(g, "K", top=6, cuff="K3")
    tail = g.piece("coat_tail", "TORSO", (-4.5, 0, 0), (9, 8, 1), pivot=(0, 11.4, 2.05), motion="flap_back")
    solid(tail, "S", "weave", 24536, 3)
    tail.back.vline(4, 0, 4, "S2")
    bell_hem(tail.back, 5, step=2)
    for i, x in enumerate((-4.6, 2.6)):
        panel = g.piece(f"coat_front_{i}", "TORSO", (0, 0, 0), (2, 7, 1), pivot=(x, 11.4, -3.05), motion="flap_front")
        solid(panel, "S", "weave", 24537 + i, 3)
        panel.front.vline(1 if i == 0 else 0, 0, 3, "D2")
        bell_hem(panel.front, 4, step=2, start=i)
    back_crest(g, ground="S3", ring="D2", pivot=(0, 1.2, 2.32))
