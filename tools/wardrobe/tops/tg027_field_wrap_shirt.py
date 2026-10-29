"""Field Wrap Shirt: a crossed wrap shirt with elbow sleeves, a cloth sash knotted at the hip with its
ends hanging, and forearms bandaged against brush and blade."""
from kit import belt
from kit_field import shirt
from kit_shinobi import bandage
from paint import solid

META = {
    "name": "Field Wrap Shirt",
    "gender": "unisex",
    "description": "Crossed wrap shirt with elbow sleeves, a knotted sash with hanging ends, bandaged forearms.",
    "tags": ["shinobi", "wrap", "chunin"],
}


def build(g):
    body = shirt(g, "P", 32120, sleeve=5, texture="twill")
    f = body.front
    for y in range(8):
        x = 1 + y * 6 // 7
        f.set(x, y, "P0"), f.set(min(7, x + 1), y, "P3")
    f.set(0, 0, "P3"), f.set(1, 0, "S3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "P1"), sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "P3")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    belt(g, "sash", y=8.8, role="A", height=2, buckle=None, inflate=.12)
    knot = g.piece("sash_knot", "TORSO", (-1, -1, -1), (2, 2, 1), pivot=(2.4, 9.8, -2.75))
    solid(knot, "A", "weave", 32124, 2)
    for i, (x, rz) in enumerate(((2.0, 8), (2.9, -10))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 10.4, -2.9), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "A", "weave", 32125 + i, 2)
