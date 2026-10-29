"""Bandaged Shorts: plain shorts above the knee and both legs bandaged from the thigh to the ankle the
way the taijutsu instructors teach, with open-toe sandals."""
from kit_academy import leg_cloth, turned_hem, waist
from kit_shinobi import bandage, sandals

META = {"name": "Bandaged Shorts", "gender": "unisex",
        "description": "Above-knee shorts with both legs bandaged from thigh to ankle, open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "P", "twill", 31640)
    leg_cloth(g, "P", "twill", 31641, (0, 2))
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        bandage(leg.strip, 0, 3, leg.strip.w - 1, 9)
        leg.strip.hline(0, leg.strip.w - 1, 3, "S2")
    turned_hem(g, "hem", 2.2, "P", 31643, height=1)
    sandals(g)
