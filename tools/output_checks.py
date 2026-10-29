"""Compare authored outputs across platforms without hiding changed content."""
import io
import json
import math
from pathlib import Path

from PIL import Image


def _same_json(actual, expected):
    if type(actual) is not type(expected):
        return False
    if isinstance(actual, float):
        # Native math libraries may differ in the final few floating-point bits.
        return math.isclose(actual, expected, rel_tol=1e-14, abs_tol=0.0)
    if isinstance(actual, dict):
        return actual.keys() == expected.keys() and all(_same_json(actual[k], expected[k]) for k in actual)
    if isinstance(actual, list):
        return len(actual) == len(expected) and all(_same_json(a, b) for a, b in zip(actual, expected))
    return actual == expected


def matches(path: Path, expected: bytes) -> bool:
    """Require exact pixels, equivalent JSON, or exact bytes for other outputs."""
    if not path.is_file():
        return False
    actual = path.read_bytes()
    if actual == expected:
        return True
    try:
        if path.suffix.lower() == '.png':
            with Image.open(io.BytesIO(actual)) as a, Image.open(io.BytesIO(expected)) as b:
                return a.mode == b.mode and a.size == b.size and a.convert('RGBA').tobytes() == b.convert('RGBA').tobytes()
        if path.suffix.lower() == '.json':
            return _same_json(json.loads(actual), json.loads(expected))
    except (OSError, ValueError, UnicodeError):
        return False
    return False
