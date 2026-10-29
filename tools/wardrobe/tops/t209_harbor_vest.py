"""Harbor Vest: everyday clothes in the clan's harbor: a white short-sleeved shirt under an open
sleeveless vest with a small whirlpool on the back and sleeves rolled to the shoulder."""
from kit import roll
from kit_uzumaki import crest_patch
from paint import cap, fabric, strip_fabric

META = {
    "name": "Harbor Vest",
    "gender": "unisex",
    "description": "White short-sleeved shirt, open sleeveless vest with a small whirlpool, rolled sleeves.",
    "tags": ["village"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 2292, 3)
    cap(body, "S", seed=2292, base=3)
    body.front.set(3, 0, "S1"), body.front.set(4, 0, "S1")
    strip_fabric(jacket, "P", "twill", 2293, 2, 0, 10)
    cap(jacket, "P", seed=2293)
    for x in range(2, 6):
        for y in range(11):
            jacket.front.clear(x, y)
    jacket.front.vline(1, 0, 10, "P3"), jacket.front.vline(6, 0, 10, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    for face in (jacket.right, jacket.left):
        face.hline(0, face.w - 1, 0, "P3")
    crest_patch(g, "back_crest", "TORSO", (0, 2.0, 2.3), size=6, ground="P2", ink="A2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 2294, 3, 0, 2)
        fabric(arm.top, "S", "weave", 2294, 4)
    roll(g, "S", 1.0, base=3)
