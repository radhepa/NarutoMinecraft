"""Field Medic Vest: the flak vest of a medic attached to a combat squad, over a long-sleeved shirt
pushed to the elbow, the cross armband on the left arm and a medical kit on the belt at the hip."""
from glyphs import stamp
from kit import belt, roll
from kit_shinobi import flak_vest
from kit_specialist import CROSS, cross_armband, shirt
from paint import fabric, solid

META = {
    "name": "Field Medic Vest",
    "gender": "unisex",
    "description": "Flak vest over a shirt pushed to the elbow, cross armband, medical kit on the belt.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    shirt(g, "S", "weave", 34020, arm_rows=(0, 5))
    roll(g, "S", 3.6)
    flak_vest(g, shoulder_swirls=False, seed=34022)
    cross_armband(g, "left", y=-.6, seed=34030)
    belt(g, "kit_belt", y=10.0, height=1, buckle=None)
    kit = g.piece("medical_kit", "TORSO", (-1.5, 0, -1), (3, 3, 2), pivot=(3.4, 9.6, -.4))
    solid(kit, "P", "plain", 34031, 3)
    kit.top.fill("P4")
    lid = g.piece("medical_kit_mark", "TORSO", (0, 0, 0), (1, 6, 6), pivot=(4.95, 9.8, -1.9), scale=(.5, .5, .5))
    for face in lid.faces:
        fabric(face, "P", "plain", 34032, 3)
    stamp(lid.left, CROSS, 0, 0, {"#": "A2"})
