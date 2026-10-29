"""Homestead Dress: the plain village dress of an Uzumaki at home: a sleeveless dress to the knee
over a white long-sleeved blouse, a cloth tie at the waist and a single wave band at the hem."""
from kit import flaps, neckline
from kit_uzumaki import waves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Homestead Dress",
    "gender": "unisex",
    "description": "Sleeveless knee dress over a white long-sleeved blouse, waist tie, one wave band at the hem.",
    "tags": ["village", "dress"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 2230, 2)
    cap(body, "P", seed=2230)
    neckline(body.front, "square", "P")
    body.front.hline(2, 5, 0, "S3")
    for face in (body.front, body.back):
        face.vline(2, 2, 7, "P1"), face.vline(5, 2, 7, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 2231 + (side == "left"), 3, 0, 9)
        fabric(arm.top, "S", "weave", 2231, 4)
        arm.strip.hline(0, arm.strip.w - 1, 9, "S2")
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
    tie = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 7.6, 0), inflate=.12)
    solid(tie, "S", "weave", 2233, 3, edge=False)
    for i, (x, rz) in enumerate(((2.8, 8), (3.6, -6))):
        end = g.piece(f"tie_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 8.4, 2.8), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 2234 + i, 3)
    for face in flaps(g, "dress", 6, "P", "plain", 2236, width=9, hem="P1", top=10.6):
        waves(face, 3, "S", 3)
