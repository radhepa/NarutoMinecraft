"""Field Flak Vest: the chunin's padded vest zipped to a stand collar, a pair of chest pockets on the
left and a stacked pair low on the right, over a long-sleeved shirt taped at the wrists."""
from kit_field import collar, pocket, shirt, tape, vest

META = {
    "name": "Field Flak Vest",
    "gender": "unisex",
    "description": "Padded zip vest, stand collar, offset pocket layout, long-sleeved shirt taped at the wrists.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "D", 32000)
    vest(g, "P", 32005)
    collar(g, "collar", "P", 32006)
    for i, (x, y) in enumerate(((1.3, 2.4), (3.0, 2.4), (-2.4, 5.2), (-2.4, 7.4))):
        pocket(g, f"pocket_{i}", (x, y, -2.3), role="P", seed=32007 + i)
    for side in ("right", "left"):
        tape(g.part(f"{side}_arm"), (8, 9))
