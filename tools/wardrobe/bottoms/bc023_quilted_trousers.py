"""Quilted Trousers: padded winter trousers for the early market and the night stalls, quilted
through and tied at the ankle over white tabi and wooden geta."""
from kit_market import gathered_ankles, geta
from paint import fabric, strip_fabric

META = {"name": "Quilted Trousers", "gender": "unisex",
        "description": "Padded quilted winter trousers tied at the ankle, white tabi and wooden geta.",
        "tags": ["civilian", "trousers"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "quilt", 36845, 2, 9, 11)
    fabric(body.bottom, "D", "quilt", 36845, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "quilt", 36846 + (side == "left"), 2, 0, 8)
        fabric(leg.top, "D", "quilt", 36846, 2)
        strip_fabric(pants, "D", "quilt", 36848 + (side == "left"), 2, 0, 7)
    gathered_ankles(g, "ankle", "D", 36850, y=8.0)
    geta(g, sock="S3")
