"""Wave Wrap Blouse: a kunoichi teacher's wrap blouse in the clan color closed left over right under
a sand collar, a sea-blue obi with a flat bow at the back and elbow sleeves printed with waves."""
from kit import belt
from kit_umino import waves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Wave Wrap Blouse",
    "gender": "female",
    "description": "Wrap blouse under a sand collar, a sea-blue obi with a flat bow, elbow sleeves printed with waves.",
    "tags": ["shinobi", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 18561, 2)
    cap(body, "P", seed=18561)
    f = body.front
    for i in range(6):
        f.set(1 + i, i, "S3")
        if i < 5:
            f.set(2 + i, i, "P1")
    f.set(0, 0, "S3")
    obi = belt(g, "obi", y=7.0, role="A", height=3, buckle=None, inflate=.1)
    for face in obi.sides:
        face.hline(0, face.w - 1, 1, "S3")
    bow = g.piece("obi_bow", "TORSO", (-2.5, -1, 0), (5, 2, 1), pivot=(0, 8.4, 2.7))
    solid(bow, "A", "weave", 18562, 2)
    bow.back.set(2, 0, "A1"), bow.back.set(2, 1, "A1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 18563 + (side == "left"), 2, 0, 6)
        fabric(arm.top, "P", "weave", 18563, 3)
        waves(arm.strip, 3, "S3")
        arm.strip.hline(0, arm.strip.w - 1, 6, "S2")
