"""Fume Jacket: the poison workshop's close-fitting jacket, zipped to a tall white collar that a
half mask tucks into, a white medic's armband on each sleeve, long gloves to the elbow and a belt
of corked vials across the hips."""
from kit import belt, collar
from kit_suzuran import armband, gloves, vial
from paint import cap, fabric, strip_fabric

META = {
    "name": "Fume Jacket",
    "gender": "unisex",
    "description": "Fitted jacket zipped to a tall white collar, medic armbands, elbow gloves, a belt of vials.",
    "tags": ["shinobi", "jacket"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 24561, 2)
    cap(body, "P", seed=24561)
    strip_fabric(jacket, "P", "twill", 24562, 2, 0, 10)
    cap(jacket, "P", texture="twill", seed=24562)
    jacket.front.vline(3, 0, 10, "M3"), jacket.front.vline(4, 0, 10, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "S3")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 9, "D2")
    neck = collar(g, "collar", "S", height=2, y=-1.8, inflate=.1)
    neck.front.vline(4, 0, 1, "M3")
    for face in neck.sides:
        face.hline(0, face.w - 1, 1, "S2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 24563 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "P", "twill", 24563, 3)
    gloves(g, "D", top=6, cuff="S3")
    armband(g, "armband", y=1.2)
    belt(g, "vial_belt", y=9.8, role="L", height=1, buckle="M")
    for i, (x, liquid) in enumerate(((-3.0, "A2"), (-1.8, "D3"), (2.2, "A3"), (3.4, "S3"))):
        vial(g, f"vial_{i}", (x, 10.0, -2.85), liquid=liquid, height=3)
