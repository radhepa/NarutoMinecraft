#!/usr/bin/env python3
"""Training yard: the street's practice ground, a packed-earth yard inside a low fence with a line of
target posts and hay bales to throw at, and the village notice board on the street front.

The first of the training-ground prop sets (target lines, post rows, log circles). The notice board is
Village Friends' working board (notices, the quest log) until the Konoha board model replaces it.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import Plan  # noqa: E402


def build() -> Plan:
    p = Plan("training_yard", "Training yard with the notice board", (13, 4, 11), "training",
             "Target posts and hay bales to practise on; Village Friends' notice board on the street front")
    p.fill(0, 0, 0, 12, 0, 10, "grass_block")
    p.fill(1, 0, 1, 11, 0, 8, "coarse_dirt")
    p.fill(0, 0, 9, 12, 0, 10, "dirt_path")
    # a low fence round the yard, open to the street in the middle
    for x in range(0, 13):
        p.set(x, 1, 0, "spruce_fence")
        if not 5 <= x <= 7:
            p.set(x, 1, 8, "spruce_fence")
    for z in range(0, 9):
        p.set(0, 1, z, "spruce_fence")
        p.set(12, 1, z, "spruce_fence")
    # the target line along the back, hay bales at the ends
    for x in (3, 6, 9):
        p.set(x, 1, 2, "stripped_spruce_log[axis=y]")
        p.set(x, 2, 2, "target")
        p.marker("training_target", (x, 2, 2))
    for x in (1, 11):
        p.set(x, 1, 1, "hay_block[axis=y]")
        p.set(x, 2, 1, "hay_block[axis=y]")
    p.set(10, 1, 1, "hay_block[axis=x]")
    p.set(2, 1, 1, "hay_block[axis=x]")
    p.set(2, 1, 9, "villagefriends:notice_board[facing=south]")
    p.marker("notice_board", (2, 1, 9))
    p.marker("anchor:training", (6, 1, 5))
    p.marker("door_anchor", (6, 1, 8))
    return p


if __name__ == "__main__":
    build().write()
