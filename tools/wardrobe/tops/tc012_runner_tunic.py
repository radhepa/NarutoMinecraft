"""Runner's Tunic: the delivery runner's short close tunic, cut for speed with the sleeves above the
elbow, a sash pulled tight, and the day's parcels bound in a dotted furoshiki on the back."""
from kit_kurama import wrap_front
from kit_market import furoshiki, sash, sleeves
from paint import cap, strip_fabric

META = {
    "name": "Runner's Tunic",
    "gender": "unisex",
    "description": "Short close tunic with sleeves above the elbow, tight sash, parcels in a furoshiki on the back.",
    "tags": ["civilian", "wrap", "casual"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 36240, 2)
    cap(body, "P", texture="twill", seed=36240)
    wrap_front(body.front, "P4", "P1", rows=7, start=1)
    sleeves(g, "P", "twill", 36241, rows=(0, 3))
    sash(g, "sash", "A", 36243, y=8.6, height=2, knot="front")
    furoshiki(g, "parcel", "D", 36245, pivot=(0, 4.0, 3.9), size=(6, 5, 3), knot_key="D3", print_key="S3")
