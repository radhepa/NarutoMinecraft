"""Night Muffler: the clan's thick knitted muffler pulled up over the mouth and nose to just under the
eyes, wound twice so it sits fat round the jaw, a fold down the front and both ends hanging behind."""
from paint import k, solid

META = {"name": "Night Muffler", "gender": "unisex", "covers_mouth": True,
        "description": "A thick knitted muffler pulled up over mouth and nose, wound twice, its ends hanging behind."}


def build(g):
    wrap = g.piece("muffler", "HEAD", (-4, -1.6, -4), (8, 2, 8), inflate=.4)
    solid(wrap, "S", "knit", 25800, 2, edge=False)
    wrap.front.vline(2, 0, 1, "S1"), wrap.front.hline(0, 7, 0, "S3")
    for face in wrap.sides:
        face.hline(0, face.w - 1, 0, "S3")
    lower = g.piece("muffler_lower", "HEAD", (-4, .4, -4), (8, 1, 8), inflate=.6)
    solid(lower, "S", "knit", 25801, 1, edge=False)
    for face in lower.sides:
        face.hline(0, face.w - 1, 0, k("S", 2))
    for i, (x, rz, n) in enumerate(((-1.2, 8, 6), (.8, -6, 5))):
        end = g.piece(f"muffler_end_{i}", "HEAD", (-1, 0, -.5), (2, n, 1), pivot=(x, -.4, 4.9), rotation=(14, 0, rz),
                      motion="sway")
        solid(end, "S", "knit", 25802 + i, 2)
        for face in end.sides:
            face.hline(0, face.w - 1, n - 1, "S1")
