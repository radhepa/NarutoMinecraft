"""Homestead Dress: the plain village dress of an Uzumaki at home, after Kushina's: a long, loose
sleeveless dress over a white high-collared sleeveless blouse, a cloth tie at the waist, a wave band
at the hem and a wristband on the left wrist."""
from kit import collar, flaps, neckline
from kit_uzumaki import waves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Homestead Dress",
    "gender": "unisex",
    "description": "Long loose sleeveless dress over a high-collared blouse, waist tie, wave hem, left wristband.",
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
    # Bare arms below the blouse's cap shoulders, and a wristband on the left wrist.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 2231 + (side == "left"), 3, 0, 1)
        fabric(arm.top, "S", "weave", 2231, 4)
    wrist = g.part("left_arm")
    wrist.strip.hline(0, wrist.strip.w - 1, 8, "D2"), wrist.strip.hline(0, wrist.strip.w - 1, 9, "D3")
    neck = collar(g, "blouse_collar", "S", "weave", base=3, height=2, y=-1.4)
    neck.front.vline(4, 0, 1, "S1")
    tie = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 7.6, 0), inflate=.12)
    solid(tie, "S", "weave", 2233, 3, edge=False)
    for i, (x, rz) in enumerate(((2.8, 8), (3.6, -6))):
        end = g.piece(f"tie_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 8.4, 2.8), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 2234 + i, 3)
    for face in flaps(g, "dress", 8, "P", "plain", 2236, width=9, hem="P1", top=10.6):
        waves(face, 5, "S", 3)
