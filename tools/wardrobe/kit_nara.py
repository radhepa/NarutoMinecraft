"""Nara clan building blocks: the spiky 'pineapple' tail tied high on the crown, the slicked-back
crown it is gathered from, and the deer-and-leaf crest the clan wears on its cloth."""
from anime import cel_box, ring_shell, spike, tie
from glyphs import stamp
from paint import k, scalp


def pulled_back(g, seed: int, side_rows: int = 5, back_rows: int = 7, sideburn: int = 2):
    """Hair combed straight back from the brow toward a tie: painted scalp, a tight hat-layer shell
    and streak lines running back over the crown."""
    scalp(g, seed, side_rows=side_rows, back_rows=back_rows, sideburn=sideburn)
    hat = ring_shell(g, seed + 1, side_rows=side_rows, back_rows=back_rows, ring_row=1)
    for x in (1, 3, 4, 6):
        hat.top.vline(x, 0, 7, k("H", 1 if x in (3, 6) else 3))
    return hat


def pineapple(g, prefix: str, pivot, spikes, seed: int = 0, tie_key: str | None = None, tie_rx: float = -30,
              depth: int = 2):
    """A short spiky tail bursting from a tie: `spikes` lists (segments, rx, rz) for each spike,
    rx negative tilts it back and up from the crown. The tie is hair-dark or a cloth key."""
    tie(g, f"{prefix}_tie", pivot, (tie_rx, 0, 0), (3, 1, 3), y=0, key=tie_key)
    root = g.piece(f"{prefix}_root", "HEAD", (-2, 1, -2), (4, 2, 4), pivot=pivot, rotation=(tie_rx, 0, 0))
    cel_box(root, seed - 1, base=2)
    for i, (segs, rx, rz) in enumerate(spikes):
        spike(g, f"{prefix}_{i}", pivot, (rx, 0, rz), segs, depth, seed + i * 7)


def tuft(g, pid: str, pivot, rotation, size=(3, 2, 3), seed: int = 0):
    """A small rounded knot of hair, the root a tail springs from."""
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, -h / 2, -d / 2), size, pivot=pivot, rotation=rotation)
    cel_box(box, seed, base=2)
    return box


# The Nara crest: a ring round a leaf, with two antler tines rising from its top.
CREST = [".#....#.",
         "#.#..#.#",
         "..####..",
         ".#....#.",
         "#..##..#",
         "#.####.#",
         ".#.##.#.",
         "..####.."]


def crest(face, x0: int, y0: int, key: str, ground: str | None = None):
    if ground:
        for y in range(8):
            for x in range(8):
                face.set(x0 + x, y0 + y, ground)
    stamp(face, CREST, x0, y0, {"#": key})
