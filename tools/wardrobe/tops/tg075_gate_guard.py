"""Gate Guard: the flak vest of the chunin on duty at the great gate, over a long-sleeved shirt
with steel bracers buckled on the forearms and a signal whistle on a cord round the neck: the
pair who sign every traveller in and out of the village."""
from kit_shinobi import flak_vest
from kit_specialist import shirt
from paint import solid, strip_fabric

META = {
    "name": "Gate Guard",
    "gender": "unisex",
    "description": "Flak vest over a long-sleeved shirt, steel bracers on the forearms, whistle on a neck cord.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "D", "weave", 34280)
    flak_vest(g, shoulder_swirls=True, seed=34282)
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "M", "plain", 34290 + (side == "left"), 2, 6, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "M4"), sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "M1")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "L2")
    cord = g.piece("whistle_cord", "TORSO", (-2.5, 0, 0), (5, 1, 1), pivot=(0, .4, -2.85), rotation=(0, 0, 0))
    solid(cord, "A", "weave", 34292, 2, edge=False)
    whistle = g.piece("whistle", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(0, 1.2, -3.2))
    solid(whistle, "M", "plain", 34293, 3, edge=False)
