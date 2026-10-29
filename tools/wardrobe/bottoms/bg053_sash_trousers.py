"""Sash Trousers: slim straight trousers with a long sash knotted at the left hip whose ends hang
to the knee, tucked at the ankle into wrapped sandals."""
from kit import legs, waistband
from kit_kunoichi import obi
from kit_shinobi import sandals, wraps

META = {"name": "Sash Trousers", "gender": "unisex",
        "description": "Slim trousers, a long sash knotted at the left hip to the knee, wrapped ankles.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "K", "twill", 33640)
    legs(g, "K", "twill", 33641, rows=(0, 9))
    sandals(g)
    wraps(g, 8, 9)
    obi(g, "waist_sash", y=9.1, role="P", height=1, knot="side", seed=33643)
