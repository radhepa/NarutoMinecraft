"""Umino building blocks: hair combed up to a high tie, Iruka's short brush of a ponytail, the wave
band and the leaping dolphin the family of Academy teachers wears on its cloth ("sea field")."""
from anime import cel_box, lock, ring_shell, spike, tie
from glyphs import stamp
from paint import fabric, k, scalp, solid


def combed_up(g, seed: int, side_rows: int = 5, back_rows: int = 7, sideburn: int = 2, streaks: bool = True):
    """Hair combed up and back from the brow toward a high tie: painted scalp, a hat-layer shell and
    fine streak lines running back over the crown."""
    scalp(g, seed, side_rows=side_rows, back_rows=back_rows, sideburn=sideburn)
    hat = ring_shell(g, seed + 1, side_rows=side_rows, back_rows=back_rows, ring_row=1)
    if streaks:
        for x in (2, 5):
            hat.top.vline(x, 1, 7, k("H", 1))
        for x in (1, 6):
            hat.back.vline(x, 0, 2, k("H", 1))
    return hat


def knot(g, prefix: str, pivot, rx: float = 0, key: str | None = None, size=(3, 2, 3)):
    """The tie at the top of a tail and the rounded knob of hair it gathers."""
    tie(g, f"{prefix}_tie", pivot, (rx, 0, 0), size, y=-1, key=key)
    root = g.piece(f"{prefix}_root", "HEAD", (-2, -1.5, -1.5), (4, 3, 3), pivot=pivot, rotation=(rx + 20, 0, 0))
    cel_box(root, 18901, base=2)
    return root


def brush_tail(g, prefix: str, pivot, locks, seed: int = 0, up=()):
    """Iruka's tail: a short brush of stiff pointed locks standing out behind a high tie. `locks` are
    (segments, rx, rz) for locks that hang back from the tie (rx near 90 points straight back), `up`
    the same for the odd spike flicking up off the top of the brush."""
    for i, (segs, rx, rz) in enumerate(locks):
        lock(g, f"{prefix}_{i}", pivot, (rx, 0, rz), segs, 2, seed + i * 7, ring=None)
    for i, (segs, rx, rz) in enumerate(up):
        spike(g, f"{prefix}_up_{i}", pivot, (rx, 0, rz), segs, 2, seed + 50 + i * 5)


def falling_tail(g, prefix: str, pivot, segments, rx: float = 16, seed: int = 0, depth: int = 3, rz: float = 0):
    """A long swinging tail falling from a high tie."""
    return lock(g, prefix, pivot, (rx, 0, rz), segments, depth, seed, ring=None, motion="sway")


# A rolling wave drawn at double resolution: repeat it along a band, two waves per 12 texels.
WAVE = [".##....##...",
        "#..#..#..#..",
        "....##....##"]

# The leaping dolphin (iruka) the family takes its given names from, at double resolution.
DOLPHIN = ["....#.......",
           "...##.......",
           ".#######....",
           "#.########..",
           ".##########.",
           "......#####.",
           ".........###",
           "........#..#"]


def wave_band(g, pid: str, bone: str, pivot, width: int, key: str, ground: str, face: str = "front", rows: int = 4,
              rotation=(0, 0, 0)):
    """A thin double-resolution plate printed with a run of waves on one face, ground everywhere else."""
    box = g.piece(pid, bone, (-width / 2, 0, 0 if face == "back" else -1), (width, rows, 1), pivot=pivot,
                  rotation=rotation, scale=(.5, .5, .5))
    for f in box.faces:
        f.fill(ground)
    target = getattr(box, face)
    for x0 in range(0, width, 12):
        stamp(target, [r[:width - x0] for r in WAVE], x0, (rows - 3) // 2, {"#": key})
    return box


def waves(face, y: int, key: str, x0: int = 0, x1: int | None = None, phase: int = 0):
    """A one-texel wave line across a face: crests on row y, troughs on y + 1."""
    x1 = face.w - 1 if x1 is None else x1
    for x in range(x0, x1 + 1):
        face.set(x, y + (0 if (x + phase) % 4 in (0, 1) else 1), key)


def surf(face, y: int, crest: str, water: str, rows: int = 2, x0: int = 0, x1: int | None = None, phase: int = 0):
    """A band of water `rows` deep under a line of breaking crests on row y: reads as a wave from a step back."""
    x1 = face.w - 1 if x1 is None else x1
    for x in range(x0, x1 + 1):
        if (x + phase) % 4 in (0, 1):
            face.set(x, y, crest)
        for r in range(1, rows + 1):
            face.set(x, y + r, water)
        if (x + phase) % 4 == 1:
            face.set(x, y + 1, crest)


def dolphin(g, pid: str, role: str, key: str, pivot, bone: str = "TORSO", face: str = "back", seed: int = 18950):
    """The dolphin crest on a cloth patch: 14 x 10 texels at double resolution."""
    box = g.piece(pid, bone, (-7, 0, 0 if face == "back" else -1), (14, 10, 1), pivot=pivot, scale=(.5, .5, .5))
    for f in box.faces:
        fabric(f, role, "weave", seed, 2)
    rows = [r[::-1] for r in DOLPHIN] if face == "back" else DOLPHIN
    stamp(getattr(box, face), rows, 1, 1, {"#": key})
    return box


def scroll(g, pid: str, pivot, rotation=(0, 0, 0), bone: str = "TORSO", length: int = 5, role: str = "S", cord: str = "A2"):
    """A rolled lesson scroll: paper in `role`, capped ends and a tie cord round its middle."""
    box = g.piece(pid, bone, (-1, -length / 2, -1), (2, length, 2), pivot=pivot, rotation=rotation, scale=(.75, .75, .75))
    solid(box, role, "plain", 18960, 3, edge=False)
    for f in box.sides:
        f.hline(0, f.w - 1, 0, "L2"), f.hline(0, f.w - 1, length - 1, "L2")
        f.hline(0, f.w - 1, length // 2, cord)
    return box
