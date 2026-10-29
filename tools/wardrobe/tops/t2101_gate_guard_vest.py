"""Gate Guard Vest: the chunin flak vest as the clan wears it on the Leaf's front gate, over a
gunmetal shirt, with steel-plated bracers on the forearms and a rust-orange duty band round the left
arm: the two guards at the gate desk, always on watch."""
from kit import sleeves
from kit_hagane import bracers
from kit_shinobi import flak_vest
from paint import cap, strip_fabric

META = {
    "name": "Gate Guard Vest",
    "gender": "unisex",
    "description": "Chunin flak vest over a gunmetal shirt, steel-plated bracers, a rust duty band on the left arm.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 21880, 2)
    cap(body, "D", seed=21880)
    flak_vest(g, seed=21881)
    for arm in sleeves(g, "D", "weave", 21886, 2, rows=(0, 10)):
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    band = g.part("left_sleeve")
    strip_fabric(band, "A", "weave", 21888, 2, 3, 4)
    band.strip.hline(0, band.strip.w - 1, 3, "A3")
    bracers(g, top=6.0, height=4, seed=21889)
