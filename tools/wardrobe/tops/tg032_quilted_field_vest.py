"""Quilted Field Vest: a diamond-quilted vest for cold postings, zipped to a tall funnel collar, two
slanted hand pockets, over a dark undershirt with chain mesh sleeves to the wrist."""
from kit_field import chain, collar, pocket, shirt, vest

META = {
    "name": "Quilted Field Vest",
    "gender": "unisex",
    "description": "Diamond-quilted zip vest with a funnel collar and slanted pockets over mesh sleeves.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "K", 32220, sleeve=-1)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        chain(arm.strip, 0, 0, arm.strip.w - 1, 9)
        arm.strip.hline(0, arm.strip.w - 1, 9, "K2")
        arm.top.fill("K2")
    vest(g, "P", 32222, ribs=(), texture="quilt")
    collar(g, "collar", "P", 32223, style="funnel")
    for i, (x, rz) in enumerate(((-2.4, -14), (2.4, 14))):
        pocket(g, f"hand_pocket_{i}", (x, 7.0, -2.3), (4, 4, 1), "P", 32224 + i, rotation=(0, 0, rz))
