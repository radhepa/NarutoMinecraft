"""Sharingan Face: the shinobi face with glowing Sharingan eyes. Each eye is a decal at quarter
resolution in front of the face: lash line, white, a red iris with a black ring, pupil and three
tomoe. The pieces glow (they are drawn fullbright, like a spider's eyes)."""
from importlib import util
from pathlib import Path

_spec = util.spec_from_file_location("f01_shinobi", Path(__file__).with_name("f01_shinobi.py"))
_f01 = util.module_from_spec(_spec)
_spec.loader.exec_module(_f01)

META = {"name": "Sharingan Face", "gender": "unisex", "emissive": True,
        "description": "Straight brows, small mouth and three-tomoe Sharingan eyes that glow."}

W, H, Q = 12, 12, 1 / 6   # eye decal: 12 x 12 texels = 2 x 2 face pixels from the lash row down


# One eye, looking straight out: two rows of lash over a red iris with
# a black rim, a dark inner ring, the pupil and three tomoe at twelve, four and eight o'clock.
# 0-3 are eye shades (0 black, 1 dark red, 2 red, 3 bright red), w the eye white.
EYE = ["000000000000",
       "000000000000",
       "www000000www",
       "ww03000220ww",
       "w0331001220w",
       "w0313222120w",
       "w0312002120w",
       "w0312002100w",
       "w0200220020w",
       "w0200110020w",
       "ww00222220ww",
       "www000000www"]
KEY = {"0": "E0", "1": "E1", "2": "E2", "3": "E3", "w": "E4"}


def build(g):
    _f01.paint(g, eyes=False)
    # Face columns 1-2 and 5-6, rows 3-5; head front is z = -4, face x 0 is model x -4.
    for name, x0, inner_right in (("right_eye", -3.0, True), ("left_eye", 1.0, False)):
        eye = g.piece(name, "HEAD", (0, 0, -1), (W, H, 1), pivot=(x0, -5.0, -4.01), scale=(Q, Q, Q))
        for face in eye.faces:
            face.fill("E0")
        for y, row in enumerate(EYE):
            for x, ch in enumerate(row if inner_right else row[::-1]):   # mirrored, so the tomoe turn alike
                eye.front.set(x, y, KEY[ch])
