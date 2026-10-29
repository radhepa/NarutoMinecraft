"""Noodle Server's Kosode: the counter girl's everyday kosode with the sleeves tied up out of the
steam by a red tasuki cord, and a long white apron tied at the waist over it."""
from kit_kurama import wrap_front
from kit_market import sleeves, tasuki, waist_apron
from paint import cap, strip_fabric

META = {
    "name": "Noodle Server's Kosode",
    "gender": "unisex",
    "description": "Kosode with the sleeves tied up by a red tasuki cord, a long white apron tied at the waist.",
    "tags": ["civilian", "wrap", "kimono", "apron"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36040, 2)
    cap(body, "P", seed=36040)
    wrap_front(body.front, "S3", "P1", rows=8, start=1)
    sleeves(g, "P", "weave", 36041, rows=(0, 3))
    tasuki(g, "A2", puff_role="P", seed=36043)
    front = waist_apron(g, "apron", "S", 8, 36045, width=8, base=3, top=8.4, band="S3")
    front.hline(1, 6, 7, "S2")
