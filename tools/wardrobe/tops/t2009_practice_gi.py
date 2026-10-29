"""Practice Gi: the sword-hall gi in pale grey, sleeveless for drills, teal lapels edged in the
wave, a dark belt, bound forearms and a wooden practice sword slung across the back."""
from kit import belt
from kit_namiashi import wave_band
from kit_shinobi import bandage
from paint import cap, fabric, line, solid, strip_fabric

META = {
    "name": "Practice Gi",
    "gender": "unisex",
    "description": "Sleeveless pale grey gi, teal wave-edged lapels, dark belt, bound forearms, a wooden sword on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 20281, 3)
    cap(body, "S", seed=20281)
    line(body.front, 0, 0, 4, 7, "P2"), line(body.front, 1, 0, 5, 7, "P3")
    line(body.front, 7, 0, 4, 5, "P2")
    wave_band(body.strip, 0, "P", 2, ground="S3")
    belt(g, "belt", y=8.8, role="K", buckle=None, inflate=.1)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "S", "weave", 20282, 4)
        arm.strip.hline(0, arm.strip.w - 1, 0, "S3"), arm.strip.hline(0, arm.strip.w - 1, 1, "P2")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
    sword = g.piece("bokken", "TORSO", (-.5, -4, -.5), (1, 14, 1), pivot=(0, 5.0, 2.8), rotation=(0, 0, -32))
    solid(sword, "L", "smooth", 20283, 3)
    for face in sword.sides:
        face.vline(0, 0, 3, "L1")
    guard = g.piece("bokken_guard", "TORSO", (-1, 0, -1), (2, 1, 2), pivot=(0, 5.0, 2.8), rotation=(0, 0, -32))
    solid(guard, "K", "plain", 20284, 2)
    guard.top.fill("K3")
