"""Plated Vest: the clan head's flak vest reinforced with riveted steel plates over the chest
pockets and on both shoulders, gunmetal sleeves under plated bracers, and the heavy family mace
on its baldric across the back."""
from kit import sleeves
from kit_hagane import bracers, harness, mace, plate
from kit_shinobi import flak_vest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Plated Vest",
    "gender": "unisex",
    "description": "Flak vest with riveted steel chest and shoulder plates, gunmetal sleeves, bracers, the family mace.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 21970, 2)
    cap(body, "D", seed=21970)
    flak_vest(g, shoulder_swirls=False, seed=21971)
    for arm in sleeves(g, "D", "weave", 21976, 2, rows=(0, 11)):
        arm.strip.hline(0, arm.strip.w - 1, 11, "D1")
    for i, x in enumerate((-3.8, 1.0)):
        chest = g.piece(f"chest_plate_{i}", "TORSO", (0, 0, 0), (3, 3, 1), pivot=(x, 3.0, -3.0))
        solid(chest, "M", "plain", 21977, 2, edge=False)
        plate(chest.front, 0, 0, 3, 3)
    for side, bone, x in (("right", "RIGHT_ARM", -3.6), ("left", "LEFT_ARM", -1.4)):
        guard = g.piece(f"{side}_pauldron", bone, (x, -1.2, -2.6), (5, 3, 5))
        solid(guard, "M", "plain", 21978, 2)
        for face in guard.sides:
            plate(face, 0, 0, face.w, 3)
        fabric(guard.top, "M", "plain", 21978, 3)
    bracers(g, top=7.0, height=4, seed=21979, inflate=.1)
    harness(g, seed=21915)
    mace(g, seed=21917)
