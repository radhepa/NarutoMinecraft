"""Kunoichi Qipao: a sleeveless red qipao dress to mid-thigh with a mandarin collar, a zip down the
front, open side slits for kicking and the white circle crest on the back."""
from glyphs import stamp
from kit import collar, flaps
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Kunoichi Qipao",
    "gender": "female",
    "description": "Sleeveless red qipao dress with side slits, mandarin collar and a white circle crest.",
    "tags": ["shinobi", "dress"],
    "covers_waist": True,
}

CIRCLE = ["...####...",
          ".##....##.",
          ".#......#.",
          "#........#",
          "#........#",
          "#........#",
          "#........#",
          ".#......#.",
          ".##....##.",
          "...####..."]


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 101, 2)
    cap(body, "P", seed=101)
    f = body.front
    f.vline(4, 1, 8, "P1"), f.set(4, 1, "M4")
    # Darts shaping the waist and the bust.
    f.set(2, 4, "P1"), f.set(5, 4, "P1"), f.vline(1, 6, 8, "P1"), f.vline(6, 6, 8, "P3")
    # Bare arms: only the shoulder seam is painted, as a narrow cap of the dress.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "P", "plain", 102, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
    # Skirt panels front and back; the open sides are the slits.
    for face in flaps(g, "dress", 5, "P", "plain", 104, width=9, hem="P1", top=11.0, front_z=-2.7, back_z=1.7):
        face.vline(4, 1, 3, "P1")
    back = g.piece("back_crest", "TORSO", (-5, 0, 0), (10, 10, 1), pivot=(0, 2.0, 2.05), scale=(.5, .5, .5))
    for face in back.faces:
        fabric(face, "P", "plain", 105, 2)
    stamp(back.back, CIRCLE, 0, 0, {"#": "S3"})
    neck = collar(g, "collar", "P", "plain", height=1, y=-.9)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S3")
    neck.front.set(4, 0, "M3")
