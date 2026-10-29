"""Long Scarf Tee: Konohamaru at the Academy. A loose short-sleeved tee with the Sarutobi crest on
the back and on the left sleeve, and his very long blue scarf wound round the neck, one end
trailing down his back to the knees."""
from kit_sarutobi import crest_patch, scarf
from paint import cap, fabric, strip_fabric

META = {
    "name": "Long Scarf Tee",
    "gender": "unisex",
    "description": "Loose short-sleeved tee with the Sarutobi crest, and a very long blue scarf to the knees.",
    "tags": ["shinobi", "genin", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 9750, 2)
    cap(body, "P", seed=9750)
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    f = body.front
    f.vline(2, 3, 10, "P1"), f.vline(6, 5, 10, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "plain", 9751, 2, 0, 3)
        fabric(arm.top, "P", "plain", 9751, 3)
        strip_fabric(sleeve, "P", "plain", 9752, 2, 0, 4)
        fabric(sleeve.top, "P", "plain", 9752, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "P1")
    crest_patch(g, "back_crest", "TORSO", (0, 3.0, 2.08), "P", "A2", 9753)
    crest_patch(g, "sleeve_crest", "LEFT_ARM", (3.33, 0.0, 0), "P", "A2", 9754, face="left")
    scarf(g, "D", 9760, tail=15)
