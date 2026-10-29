"""Chest Rig: a sleeveless undershirt with a padded rig buckled across the chest, three pouches along
its front and straps over the shoulders, bare arms taped from elbow to wrist."""
from kit_field import pocket, shirt, tape
from paint import fabric, k, strip_fabric

META = {
    "name": "Chest Rig",
    "gender": "unisex",
    "description": "Sleeveless undershirt with a padded chest rig, three front pouches and taped forearms.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "D", 32100, sleeve=-1, texture="rib")
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "plain", 32102, 2, 2, 6)
    jacket.strip.hline(0, jacket.strip.w - 1, 2, "P3"), jacket.strip.hline(0, jacket.strip.w - 1, 6, "P0")
    # Shoulder straps from the rig over the top of the shoulders.
    for face in (jacket.front, jacket.back):
        for x in (1, 6):
            fabric(face, "P", "plain", 32103, 2, x, 0, 1, 2)
    for x in (1, 6):
        jacket.top.vline(x, 0, 3, k("P", 3))
    for face in (jacket.right, jacket.left):
        face.hline(0, 3, 4, "L2")
    for i, x in enumerate((-2.4, 0, 2.4)):
        pocket(g, f"rig_pouch_{i}", (x, 3.0, -2.3), (4, 5, 2), "P", 32104 + i, snap="M3" if i != 1 else None)
    for side in ("right", "left"):
        tape(g.part(f"{side}_arm"), range(5, 10))
