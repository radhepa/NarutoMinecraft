"""Bandage Bodice: a young Yuhi's training top, a sleeveless chain-mesh shirt with the body bound in
broad bandage turns from the chest to the hips, a thorn-printed strip tied round the waist and both
forearms wrapped."""
from kit import belt
from kit_shinobi import mesh
from kit_yuhi import bandage_turns, thorn_band
from paint import fabric, solid

META = {
    "name": "Bandage Bodice",
    "gender": "unisex",
    "description": "Sleeveless mesh shirt bound in bandage turns, thorn-print waist tie, wrapped forearms.",
    "tags": ["shinobi", "genin", "wrap"],
}


def build(g):
    body = g.part("body")
    for f in body.sides:
        f.fill("K2")
        mesh(f, 0, 0, f.w - 1, 2, "K1")
        bandage_turns(f, 0, 3, f.w - 1, f.h - 1, "S", 3)
    fabric(body.top, "K", "plain", 14720, 2), fabric(body.bottom, "S", "plain", 14720, 2)
    sash = belt(g, "waist_tie", y=9.0, role="P", height=2, buckle=None, inflate=.1)
    for face in sash.sides:
        thorn_band(face, 1, "A")
    for i, rz in enumerate((10, -6)):
        end = g.piece(f"tie_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(-3.2 + i * .7, 10.4, -2.75),
                      rotation=(0, 0, rz), motion="sway")
        solid(end, "P", "weave", 14721 + i, 2)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "K", "plain", 14723, 2)
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 1, "K1")
        bandage_turns(arm.strip, 0, 6, arm.strip.w - 1, 11, "S", 3)
        fabric(arm.bottom, "S", "plain", 14724, 2)
