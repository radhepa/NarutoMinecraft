"""Apothecary Vest: the clan's chunin field wear, a sleeveless padded vest over a dark leaf-green
undershirt, a leather apothecary sash across the chest slotted with three stoppered vials (toxin,
antidote, salve), a herb pouch on the hip and long medic gloves."""
from kit import belt, collar
from kit_suzuran import apothecary_sash, gloves, herb_pouch, sash_vials
from paint import cap, fabric, strip_fabric

META = {
    "name": "Apothecary Vest",
    "gender": "unisex",
    "description": "Padded sleeveless vest over a green undershirt, a vial sash across the chest, herb pouch, gloves.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 24521, 2)
    fabric(body.top, "D", "weave", 24521, 3)
    strip_fabric(jacket, "P", "quilt", 24522, 2, 0, 10)
    cap(jacket, "P", texture="quilt", seed=24522)
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    jacket.front.vline(3, 0, 10, "S3"), jacket.front.vline(4, 0, 10, "S2")
    apothecary_sash(jacket.front, jacket.back)
    sash_vials(g, "vial", start=(-2.4, 1.8), step=(1.27, 2.0), z=-2.85)
    neck = collar(g, "collar", "S", height=1, y=-.8)
    neck.front.hline(3, 5, 0, "S1")
    belt(g, "belt", y=9.6, role="L", height=1, buckle="M")
    herb_pouch(g, "pouch", (3.4, 9.0, -2.6))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 24523 + (side == "left"), 2, 0, 6)
        fabric(arm.top, "D", "weave", 24523, 3)
    gloves(g, "K", top=5, cuff="S3")
