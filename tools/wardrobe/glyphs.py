"""Kanji and crests drawn at double or triple resolution for decal pieces (scale 1/2 or 1/3)."""
from __future__ import annotations

FIRE = ["............",
        ".....##.....",
        ".....##.....",
        ".#...##...#.",
        ".##..##..##.",
        "..#..##..#..",
        ".....##.....",
        ".....##.....",
        "....####....",
        "...##..##...",
        "..##....##..",
        ".##......##.",
        "##........##",
        "............"]


def stamp(face, rows, x0: int, y0: int, legend: dict):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in legend:
                face.set(x0 + x, y0 + y, legend[ch])


# The Uzumaki swirl worn on Konoha flak vests: a ring with a spiral curling into its centre.
SWIRL = ["....####....",
         "..##....##..",
         ".##.......#.",
         ".#...###..#.",
         "##..#...#..#",
         "#...#...##.#",
         "#...###..#.#",
         "#.......##.#",
         ".##.....#.#.",
         ".#.#####..#.",
         "..##....##..",
         "....####...."]

SWIRL_SMALL = [".####.",
               "#....#",
               "#.##.#",
               "#.#.##",
               "#..#.#",
               ".####."]


# The Hidden Leaf mark engraved on a forehead protector: a spiral with a pointed leaf tip at the
# upper left and a stem trailing off to the lower right.
LEAF = ["#.......",
        ".#####..",
        ".#...#..",
        ".#.#.#..",
        ".#.###..",
        "..#.....",
        "...####.",
        "........"]
