"""Checked Skirt: a knee-length A-line skirt in a woven check for school days and errands, with
short white socks and soft cloth shoes."""
from kit_household import checks, cloth_shoes, skirt, socks, waist

META = {"name": "Checked Skirt", "gender": "female",
        "description": "Knee-length A-line skirt in a woven check, short white socks, cloth shoes.",
        "tags": ["civilian", "skirt"]}


def build(g):
    waist(g, "D", "plain", 37660, band="D1")
    socks(g, "S3", rows=(8, 9))
    cloth_shoes(g, "K", 2, strap="K3")
    skirt(g, "skirt", 6, "D", "plain", 37662, hem="D1",
          pattern=lambda f, rows=None: checks(f, "D3", every=3, cross="A2", rows=rows))
