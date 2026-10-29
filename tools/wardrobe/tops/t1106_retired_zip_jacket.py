"""Retired Zip Jacket: Kakashi after the Hokage years, a plain grey zip-up jacket with a high collar
over the mask, two slash pockets and ribbed cuffs, the look of a man who finally gets to read in peace."""
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Retired Zip Jacket",
    "gender": "unisex",
    "description": "Grey zip-up jacket with a high collar, slash pockets and ribbed cuffs and hem.",
    "tags": ["shinobi", "casual"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 11501, 2)
    cap(body, "D", seed=11501)
    strip_fabric(jacket, "P", "plain", 11502, 2)
    cap(jacket, "P", texture="plain", seed=11502)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1"), jacket.strip.hline(0, jacket.strip.w - 1, 10, "P3")
    f = jacket.front
    f.vline(3, 0, 11, "M2"), f.vline(4, 0, 11, "P1")
    f.set(3, 0, "M3")
    # Slash pockets and the side seams.
    f.hline(0, 2, 7, "P1"), f.hline(5, 7, 7, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "plain", 11503 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "plain", 11503, 3)
        arm.strip.hline(0, arm.strip.w - 1, 5, "P1")
        arm.strip.hline(0, arm.strip.w - 1, 9, "P3"), arm.strip.hline(0, arm.strip.w - 1, 10, "P1")
    neck = g.piece("collar", "TORSO", (-4.5, -2.0, -2.6), (9, 3, 5), inflate=.08)
    solid(neck, "P", "plain", 11506, 2)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "P3")
    neck.front.vline(4, 0, 2, "M2")
    neck.top.fill("D1")
