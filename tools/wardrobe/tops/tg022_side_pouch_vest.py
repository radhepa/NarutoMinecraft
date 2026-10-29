"""Side-Pouch Vest: a padded vest buckled shut on the wearer's left under a low collar, its pouches
riding on both hips instead of the chest, over a half-sleeved shirt and mesh down the forearms."""
from kit_field import collar, half_sleeves, mesh_arms, pocket, shirt, vest

META = {
    "name": "Side-Pouch Vest",
    "gender": "unisex",
    "description": "Side-buckled padded vest with hip pouches, a low collar, half sleeves over mesh forearms.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "D", 32020, sleeve=-1)
    half_sleeves(g, "D", 32023, length=4)
    mesh_arms(g, (5, 9))
    vest(g, "P", 32026, closure="side", ribs=(3, 6, 9))
    collar(g, "collar", "P", 32027, style="low")
    for side, x, ry in (("right", -4.25, 90), ("left", 4.25, -90)):
        for i, y in enumerate((6.4, 8.4)):
            pocket(g, f"{side}_hip_pouch_{i}", (x, y, 0), (4, 4, 2), "P", 32028 + i, rotation=(0, ry, 0), snap="M3")
    pocket(g, "chest_pouch", (2.2, 2.6, -2.3), (3, 3, 1), "P", 32032)
