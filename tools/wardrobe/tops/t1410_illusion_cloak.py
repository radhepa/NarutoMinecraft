"""Illusion Cloak: the dark field cloak of the clan's genjutsu hunters, a short cape over both
shoulders lined in crimson and drifting with mist spirals, fastened at the throat with a rose clasp,
over a fitted dark tunic with bandaged forearms."""
from kit_yuhi import bandage_turns, mist_swirls, rose
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Illusion Cloak",
    "gender": "unisex",
    "description": "Short dark cape lined in crimson with mist spirals, rose clasp, fitted tunic, bandaged forearms.",
    "tags": ["shinobi", "cloak"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 14870, 2)
    cap(body, "P", texture="twill", seed=14870)
    body.front.vline(4, 1, 11, "P1")
    body.strip.hline(0, body.strip.w - 1, 9, "L2"), body.front.set(4, 9, "M3")
    # The cape: a back panel to mid-back and a front panel over each shoulder, open down the chest.
    cape = g.piece("cape_back", "TORSO", (-5, 0, 0), (10, 8, 1), pivot=(0, -.4, 2.6), rotation=(6, 0, 0), motion="flap_back")
    solid(cape, "K", "velvet", 14871, 2)
    mist_swirls(cape.back, 0, 2, 9, 7, "P", 3)
    cape.back.hline(0, 9, 7, "A2"), cape.front.fill("A1")
    for side, x in (("right", -3.25), ("left", 3.25)):
        front = g.piece(f"cape_{side}", "TORSO", (-1.75, 0, 0), (4, 5, 1), pivot=(x, -.4, -3.4), rotation=(-4, 0, 0))
        solid(front, "K", "velvet", 14872 + (side == "left"), 2)
        mist_swirls(front.front, 0, 1, 3, 4, "P", 3)
        front.front.hline(0, 3, 4, "A2"), front.back.fill("A1")
        front.front.vline(3 if side == "right" else 0, 0, 4, "A2")
        shoulder = g.piece(f"cape_{side}_shoulder", "TORSO", (-2.5, 0, -3), (5, 1, 6), pivot=(x * 1.2, -.9, 0))
        solid(shoulder, "K", "velvet", 14874 + (side == "left"), 2)
    rose(g, "clasp", (0, .4, -3.6), bone="TORSO", petal="A", base=2)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 14876 + (side == "left"), 2, 0, 6)
        fabric(arm.top, "P", "twill", 14878, 3)
        bandage_turns(arm.strip, 0, 7, arm.strip.w - 1, 11, "S", 3)
