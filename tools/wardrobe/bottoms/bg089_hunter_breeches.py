"""Hunter's Breeches: sturdy trousers with leather chaps strapped over the front of the thighs and
knees, tucked into soft boots, a skinning knife on the belt: for crawling through brush."""
from kit import belt, legs, waistband
from kit_rugged import soft_boots
from paint import solid

META = {"name": "Hunter's Breeches", "gender": "unisex",
        "description": "Sturdy trousers with leather chaps over the thighs and knees, soft boots, a belt knife.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "twill", 35390, 2)
    legs(g, "P", "twill", 35391, 2, rows=(0, 8), crease=False)
    soft_boots(g, top=8, role="L")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        chap = g.piece(f"{side}_chap", bone, (-2.2, .4, -2.6), (4, 7, 1), inflate=.05)
        solid(chap, "L", "leather", 35392 + (side == "left"), 2)
        chap.front.vline(0, 0, 6, "L1"), chap.front.vline(3, 0, 6, "L1")
        chap.front.hline(0, 3, 5, "L3")
        for y in (1.2, 5.6):
            strap = g.piece(f"{side}_chap_strap_{int(y)}", bone, (-2, y, -2), (4, 1, 4), inflate=.32)
            for face in strap.faces:
                face.fill("K2")
    belt(g, "waist_belt", y=9.4, role="L", height=1, buckle="M")
    knife = g.piece("waist_knife", "TORSO", (0, 0, 0), (1, 4, 1), pivot=(-3.8, 10.0, 0), rotation=(0, 0, 10))
    solid(knife, "K", "leather", 35395, 2)
    knife.top.fill("M3")
