"""Shimura clan building blocks: the clan crest, Danzo's cane, bandaged arms with steel shackles and
the back crest panel the clan's formal coats carry."""
from glyphs import stamp
from kit_shinobi import bandage
from paint import fabric, k, solid

# The Shimura crest: a ring round a crossbar and a trunk that splits into three roots, for the
# clan that grew the village's hidden Root. Drawn at double resolution (scale 1/2).
CREST = ["....####....",
         "..##....##..",
         ".#........#.",
         ".#.######.#.",
         "#....##....#",
         "#....##....#",
         "#...#..#...#",
         "#..#.##.#..#",
         ".#.#.##.#.#.",
         ".#...##...#.",
         "..##....##..",
         "....####...."]


def back_crest(g, role: str, ink: str = "S3", y: float = 1.6, z: float = 2.3, pid: str = "back_crest", texture: str = "weave"):
    """The crest in `ink` on a half-scale panel of the coat's own cloth, centred on the back."""
    panel = g.piece(pid, "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, y, z), scale=(.5, .5, .5))
    fabric(panel.back, role, texture, 13990, 2)
    stamp(panel.back, CREST, 0, 0, {"#": ink})
    for face in (panel.top, panel.bottom, panel.right, panel.left, panel.front):
        face.fill(k(role, 2))
    return panel


def cane(g, seed: int = 13980, pivot=(1.0, 8.6, -1.2), length: int = 13):
    """Danzo's plain walking cane held in the left hand: a dark shaft to the ground under a
    rounded grip, a steel ferrule at the foot."""
    shaft = g.piece("cane", "LEFT_ARM", (-.5, 0, -.5), (1, length, 1), pivot=pivot, rotation=(-6, 0, 0))
    solid(shaft, "L", "smooth", seed, 1, edge=False)
    for face in shaft.sides:
        face.set(0, length - 1, "M2")
        face.vline(0, 1, length - 3, "L2")
    grip = g.piece("cane_grip", "LEFT_ARM", (-1, -1, -1), (2, 1, 2), pivot=pivot, rotation=(-6, 0, 0))
    solid(grip, "L", "smooth", seed + 1, 2, edge=False)


def bandaged_arm(g, side: str, rows=(0, 11), shackles=(), seed: int = 13970):
    """An arm wound in bandages from rows[0] to rows[1], with steel shackle bands at the given rows."""
    arm = g.part(f"{side}_arm")
    bandage(arm.strip, 0, rows[0], arm.strip.w - 1, rows[1])
    if rows[0] == 0:
        bandage(arm.top, 0, 0, arm.top.w - 1, arm.top.h - 1)
    if rows[1] == 11:
        bandage(arm.bottom, 0, 0, arm.bottom.w - 1, arm.bottom.h - 1)
    bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
    x = -3.5 if side == "right" else -1.5
    for i, y in enumerate(shackles):
        band = g.piece(f"{side}_shackle_{i}", bone, (x, y, -2.5), (5, 1, 5))
        solid(band, "M", "plain", seed + i, 3, edge=False)
        for face in band.sides:
            face.set(face.w // 2, 0, "M4")
    return arm
