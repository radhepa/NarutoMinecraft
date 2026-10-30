"""Shared helpers for the combat authoring tools (COMBAT.md).

Every data file is a Python module under tools/combat/ that builds plain dicts; build.py writes them
to data/combat/ as JSON with a "format" field, and --check validates every cross reference.
"""

import json
import os

FORMAT = 1
ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "data", "combat")

RANKS = ["e", "d", "c", "b", "a", "s"]
NATURES = ["fire", "wind", "lightning", "earth", "water"]
SLICES = ["beta1", "beta2", "beta2_5", "beta3", "chunin", "jonin", "anbu", "road", "post"]
SIGNS = ["rat", "ox", "tiger", "hare", "dragon", "snake", "horse", "ram", "monkey", "bird", "dog", "boar"]

# Rank defaults: the level a technique of that rank asks for, its chakra cost, its single-target
# power (base damage before level, pillar and nature scaling) and its cooldown in ticks.
RANK_LEVEL = {"e": 1, "d": 5, "c": 10, "b": 18, "a": 30, "s": 42}
RANK_COST = {"e": 5, "d": 10, "c": 16, "b": 30, "a": 50, "s": 80}
RANK_POWER = {"e": 0, "d": 5, "c": 10, "b": 14, "a": 21, "s": 32}
RANK_COOLDOWN = {"e": 40, "d": 60, "c": 120, "b": 200, "a": 360, "s": 800}
TICKS_PER_SIGN = 4


def cid(name):
    """A combat id: every id other sessions see is namespaced combat:."""
    return name if name.startswith("combat:") else "combat:" + name


# --check sets this to a dict: outputs are collected here (path -> text) instead of written.
PENDING = None


def emit(path, text):
    if PENDING is not None:
        PENDING[os.path.normpath(path)] = text
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def write(rel, payload):
    path = os.path.join(OUT, rel)
    body = {"format": FORMAT}
    body.update(payload)
    emit(path, json.dumps(body, indent=1, ensure_ascii=False) + "\n")
    return path
