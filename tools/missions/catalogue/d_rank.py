"""D-rank board missions: the village's daily life, each with twists so no job is only a chore.

Clients are residents picked by a query on their profile (job, district, age, household, pets). Places are
anchor tags the map defines in districts.json (the Konoha build owns them; MISSIONS.md lists every tag).
Twists are rolled per mission from the `missions` stream and switch the graph onto their branch.
"""
from mkit import (S, anchor, buy, chose, choose, collect, count, craft, deliver, end, escort, go, inspect,
                  mission, one_of, outcome, perform, protect, resident, sneak, spawn, talk, twist, twist_if,
                  wait_until, suspect_of)

C = "slot:client"
NIGHT = {"time_between": ["18:00", "23:00"]}

T = []
add = T.append

# --- pets ----------------------------------------------------------------------------------------------

add(mission(
    "mission.d.lost_pet", "d", "pets", minutes=10, pay=0.2, party="squad_or_solo",
    premise="A resident's cat or dog has run off again; find it and bring it home.",
    client=resident(has_pet=True),
    slots={"pet_spot": anchor("pet_hideout"), "second_spot": anchor("pet_hideout"), "claimant": resident()},
    steps=[
        S("ask", talk(C), "find"),
        S("find", collect("slot:client.pet", at="slot:pet_spot"), "return",
          branch=[(twist_if("two_pets"), "second"), (twist_if("new_litter"), "litter"),
                  (twist_if("rival_claims"), "claim")]),
        S("second", collect("stray_pet", at="slot:second_spot"), "return"),
        S("litter", perform("carry_gently", at="slot:pet_spot", count=3), "return"),
        S("claim", talk("slot:claimant"), "evidence"),
        S("evidence", inspect("pet_marks", count=2), "decide"),
        S("decide", choose({"client": None, "claimant": "given_to_claimant"}), "return",
          branch=[(chose("decide", "claimant"), "hand_over")]),
        S("hand_over", deliver("slot:client.pet", "slot:claimant"), None,
          on_done=[end("given_to_claimant")]),
        S("return", deliver("slot:client.pet", C), None),
    ],
    twists=[twist("two_pets", 2), twist("new_litter", 1, harder=True), twist("rival_claims", 1)],
    outcomes={"done": outcome(), "given_to_claimant": outcome(pay=0.6, standing=-1, extra={"other_standing": 2})},
    bonus=["gentle", "fast", "kind_choice"], fast_hours=3,
    anchors=["pet_hideout"], tags=["village", "animal", "search"],
    twist_premises={"two_pets": "It has made a friend: another runaway who needs taking home too.",
                    "new_litter": "It hid to give birth; carry the litter home without frightening them.",
                    "rival_claims": "A neighbour swears the pet is theirs; find out whose it really is."}))

add(mission(
    "mission.d.dog_walking", "d", "pets", minutes=8, pay=0.25, party="squad_or_solo",
    premise="Walk the Inuzuka clinic's boarding ninken around the outer fields and bring every one back.",
    client=resident(job="vet"), slots={"route": anchor("dog_route"), "scent_spot": anchor("forest_edge")},
    steps=[
        S("leash", talk(C), "walk"),
        S("walk", go("slot:route"), "home",
          branch=[(twist_if("scent_chase"), "chase"), (twist_if("shy_pup"), "coax"),
                  (twist_if("lost_collar"), "collar")]),
        S("chase", go("slot:scent_spot"), "round_up"),
        S("round_up", collect("ninken", at="slot:scent_spot", count=4), "home"),
        S("coax", perform("feed_treat", count=3), "home"),
        S("collar", inspect("collar", at="slot:route"), "home"),
        S("home", deliver("ninken", C), None),
    ],
    twists=[twist("scent_chase", 2, harder=True), twist("shy_pup"), twist("lost_collar")],
    bonus=["gentle", "fast"], fast_hours=2, anchors=["dog_route", "forest_edge"],
    unlock={"rank_at_least": "genin"}, tags=["village", "animal", "outdoors"],
    twist_premises={"scent_chase": "The pack catches a scent and bolts for the treeline.",
                    "shy_pup": "One pup will not walk for anyone; win it over.",
                    "lost_collar": "A collar with a clan tag goes missing on the route."}))

add(mission(
    "mission.d.pet_sitting", "d", "pets", minutes=12, pay=0.35, party="solo",
    premise="A family is away for the day; feed, brush and mind their animals at the set hours.",
    client=resident(has_pet=True, household=True), slots={"home": anchor("client_home"),
                                                         "neighbour": resident(district="same:client")},
    steps=[
        S("keys", talk(C), "morning"),
        S("morning", perform("feed_pet", at="slot:home"), "noon",
          branch=[(twist_if("escape_artist"), "escaped")]),
        S("escaped", collect("slot:client.pet", at="slot:home"), "noon"),
        S("noon", wait_until("12:00", at="slot:home"), "evening",
          branch=[(twist_if("neighbour_feud"), "feud")]),
        S("feud", talk("slot:neighbour"), "evening"),
        S("evening", perform("feed_pet", at="slot:home"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("escape_artist", 2), twist("neighbour_feud")],
    bonus=["careful", "extra_mile"], anchors=["client_home"], tags=["village", "animal", "timed"],
    twist_premises={"escape_artist": "The pet has learned to open the latch.",
                    "neighbour_feud": "The neighbour says the pet has been raiding their garden for weeks."}))

# --- children and the Academy ------------------------------------------------------------------------

add(mission(
    "mission.d.babysitting", "d", "childcare", minutes=12, pay=0.4, party="squad_or_solo",
    premise="Mind a family's children for an afternoon while the parents work.",
    client=resident(household_children=True), slots={"home": anchor("client_home"), "hiding": anchor("hiding_spot"),
                                                     "hospital": anchor("hospital.desk")},
    steps=[
        S("arrive", talk(C), "play"),
        S("play", perform("play_with_children", at="slot:home", count=3), "dinner",
          branch=[(twist_if("hide_and_seek"), "seek"), (twist_if("ninja_show"), "show"),
                  (twist_if("sick_child"), "medicine")]),
        S("seek", inspect("hidden_child", at="slot:hiding"), "dinner"),
        S("show", perform("technique:clone"), "dinner"),
        S("medicine", go("slot:hospital"), "back"),
        S("back", deliver("medicine", "slot:home"), "dinner"),
        S("dinner", wait_until("18:00", at="slot:home"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("hide_and_seek", 2), twist("ninja_show", 2), twist("sick_child", 1, harder=True)],
    bonus=["client_unharmed", "extra_mile"], anchors=["client_home", "hiding_spot", "hospital.desk"],
    tags=["village", "children"],
    twist_premises={"hide_and_seek": "The youngest hides so well the others start to worry.",
                    "ninja_show": "The children will not settle until they see a real jutsu.",
                    "sick_child": "One child runs a fever; fetch medicine without leaving the others alone."}))

add(mission(
    "mission.d.academy_assist", "d", "academy", minutes=10, pay=0.35,
    premise="Help an Academy teacher run a target-practice class for the youngest year.",
    client=resident(job="teacher"), slots={"yard": anchor("academy.yard")},
    steps=[
        S("brief", talk(C), "set_up"),
        S("set_up", perform("set_targets", at="slot:yard", count=6), "class",
          branch=[(twist_if("prankster"), "prank")]),
        S("prank", inspect("rigged_target", at="slot:yard", count=3), "class"),
        S("class", perform("coach_throw", at="slot:yard", count=5), "tidy",
          branch=[(twist_if("demonstration"), "demo")]),
        S("demo", perform("combo:three_hit", at="slot:yard"), "tidy"),
        S("tidy", collect("practice_kunai", at="slot:yard", count=12), "report",
          branch=[(twist_if("lost_kunai"), "search")]),
        S("search", collect("practice_kunai", at="place:academy.grounds", count=4), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("prankster", 2), twist("demonstration", 2), twist("lost_kunai")],
    bonus=["all_found", "teamwork"], anchors=["academy.yard"], tags=["village", "academy", "children"],
    twist_premises={"prankster": "Someone has rigged the targets to fall on the first hit.",
                    "demonstration": "The class wants to see a Genin's combo, up close.",
                    "lost_kunai": "Four practice kunai flew over the wall."}))

add(mission(
    "mission.d.tutoring", "d", "academy", minutes=10, pay=0.3, party="solo",
    premise="Tutor an Academy pupil who will fail the next test without help.",
    client=resident(age="child", job="pupil"), slots={"parent": resident(parent_of="client"),
                                                      "bully": resident(age="child"),
                                                      "library": anchor("academy.library")},
    steps=[
        S("meet", talk("slot:parent"), "study"),
        S("study", perform("study_session", at="slot:library", count=2), "quiz",
          branch=[(twist_if("real_problem"), "listen"), (twist_if("cheat_sheet"), "sheet")]),
        S("listen", talk(C), "bully"),
        S("bully", talk("slot:bully"), "quiz"),
        S("sheet", choose({"confiscate": None, "ignore": "looked_away"}), "quiz",
          branch=[(chose("sheet", "ignore"), "quiz_cheat")]),
        S("quiz_cheat", perform("quiz", at="slot:library"), None, on_done=[end("looked_away")]),
        S("quiz", perform("quiz", at="slot:library"), "report"),
        S("report", talk("slot:parent"), None),
    ],
    twists=[twist("real_problem", 2), twist("cheat_sheet")],
    outcomes={"done": outcome(), "looked_away": outcome(pay=1.0, standing=-1, acts=[["slot:parent", "broke_promise"]])},
    bonus=["kind_choice", "extra_mile"], anchors=["academy.library"], tags=["village", "academy", "talk"],
    twist_premises={"real_problem": "The pupil is not slow; an older child takes their lunch every day.",
                    "cheat_sheet": "You find a cheat sheet in the pupil's sleeve."}))

# --- archives and scrolls --------------------------------------------------------------------------------

add(mission(
    "mission.d.scroll_sorting", "d", "inventory", minutes=10, pay=0.3,
    premise="Sort a season of mission reports in the Hokage Residence's records room.",
    client=resident(job="clerk"), slots={"room": anchor("residence.records")},
    steps=[
        S("brief", talk(C), "sort"),
        S("sort", perform("sort_scrolls", at="slot:room", count=5), "report",
          branch=[(twist_if("ink_spill"), "recopy"), (twist_if("paper_moths"), "moths")]),
        S("recopy", craft("copied_report", 2), "report"),
        S("moths", perform("smoke_out", at="slot:room", count=3), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("ink_spill", 2), twist("paper_moths")],
    bonus=["careful", "fast"], fast_hours=2, anchors=["residence.records"], tags=["village", "indoors"],
    twist_premises={"ink_spill": "A jar tips over two reports; copy them again before the clerk notices.",
                    "paper_moths": "Paper moths are eating the bottom shelf."}))

add(mission(
    "mission.d.shop_inventory", "d", "inventory", minutes=10, pay=0.3, party="squad_or_solo",
    premise="Count every item in a shop's storeroom before the quarterly tax visit.",
    client=resident(job="shopkeeper"),
    slots={"store": anchor("shop_storeroom"), "porter": resident(job="porter"), "apprentice": resident(job="apprentice"),
           "culprit": suspect_of("porter", "apprentice")},
    steps=[
        S("brief", talk(C), "count"),
        S("count", inspect("stock_shelf", at="slot:store", count=6), "report",
          branch=[(twist_if("count_mismatch"), "missing"), (twist_if("mislabelled"), "relabel")]),
        S("missing", talk("slot:porter"), "missing2"),
        S("missing2", talk("slot:apprentice"), "accuse"),
        S("accuse", choose({"culprit": None, "say_nothing": "kept_quiet"}), "report"),
        S("relabel", perform("relabel_crate", at="slot:store", count=4), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("count_mismatch", 2, harder=True), twist("mislabelled", 2)],
    outcomes={"done": outcome(), "kept_quiet": outcome(pay=0.8)},
    bonus=["fast", "all_found"], fast_hours=2, anchors=["shop_storeroom"], tags=["village", "market", "indoors"],
    twist_premises={"count_mismatch": "The numbers do not add up: someone has been taking a little at a time.",
                    "mislabelled": "Half the crates are labelled as something else."}))

# --- farms and harvests ----------------------------------------------------------------------------------

add(mission(
    "mission.d.farm_weeding", "d", "farm", minutes=10, pay=0.2, party="squad_or_solo",
    premise="Weed a farmer's field outside the wall before the planting.",
    client=resident(job="farmer"), slots={"field": anchor("farm_field"), "desk": anchor("desk")},
    steps=[
        S("brief", talk(C), "weed"),
        S("weed", perform("pull_weeds", at="slot:field", count=20), "report",
          branch=[(twist_if("crows"), "crows"), (twist_if("boar_tracks"), "tracks"),
                  (twist_if("buried_cache"), "cache")]),
        S("crows", perform("scare_crows", at="slot:field", count=3), "report"),
        S("tracks", inspect("boar_tracks", at="slot:field", count=3), "report",
          on_done=[{"lead": "mission.c.beast_hunt"}]),
        S("cache", choose({"turn_in": None, "keep": "kept_cache"}), "report",
          branch=[(chose("cache", "turn_in"), "turn_in")]),
        S("turn_in", deliver("old_kunai_cache", "slot:desk"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("crows", 2), twist("boar_tracks"), twist("buried_cache")],
    outcomes={"done": outcome(), "kept_cache": outcome(pay=1.0, extra={"item": "old_kunai_cache", "clean_record": False})},
    bonus=["fast", "clean_record"], fast_hours=3, anchors=["farm_field", "desk"],
    tags=["outdoors", "farm"],
    twist_premises={"crows": "The crows have no respect for the scarecrow.",
                    "boar_tracks": "Fresh boar tracks cross the field; the desk will want to know.",
                    "buried_cache": "Your hand closes on an old cache of kunai buried under the rows."}))

add(mission(
    "mission.d.harvest", "d", "harvest", minutes=12, pay=0.45, party="squad",
    premise="Bring a farm's harvest in before the rain.",
    client=resident(job="farmer"), slots={"field": anchor("farm_field"), "barn": anchor("farm_barn"),
                                          "deer_spot": anchor("forest_edge")},
    season=["summer", "autumn"],
    steps=[
        S("brief", talk(C), "pick"),
        S("pick", collect("crop", at="slot:field", count=24), "cart",
          branch=[(twist_if("hungry_deer"), "deer"), (twist_if("storm"), "rush")]),
        S("deer", perform("shoo_gently", at="slot:field", count=4), "cart"),
        S("rush", collect("crop", at="slot:field", count=12), "cart"),
        S("cart", deliver("crop", "slot:barn"), "report",
          branch=[(twist_if("broken_axle"), "axle")]),
        S("axle", craft("cart_axle"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("hungry_deer", 2), twist("storm", 1, harder=True), twist("broken_axle")],
    bonus=["fast", "gentle", "teamwork"], fast_hours=4, anchors=["farm_field", "farm_barn", "forest_edge"],
    tags=["outdoors", "farm", "timed"],
    twist_premises={"hungry_deer": "Deer from the clan forest have found the field first; shoo them gently.",
                    "storm": "The rain comes early; half the field in half the time.",
                    "broken_axle": "The loaded cart's axle snaps on the path."}))

add(mission(
    "mission.d.orchard", "d", "harvest", minutes=10, pay=0.4,
    premise="Pick persimmons from an orchard's tallest trees (tree walking welcome).",
    client=resident(job="farmer"), slots={"orchard": anchor("orchard")},
    unlock={"flag": "story.ch10.done"}, season=["autumn"],
    steps=[
        S("brief", talk(C), "climb"),
        S("climb", collect("persimmon", at="slot:orchard", count=30), "report",
          branch=[(twist_if("wasps"), "wasps"), (twist_if("stuck_child"), "child")]),
        S("wasps", perform("smoke_bomb", at="slot:orchard"), "climb2"),
        S("climb2", collect("persimmon", at="slot:orchard", count=10), "report"),
        S("child", perform("tree_walk_rescue", at="slot:orchard"), "report"),
        S("report", deliver("persimmon", C), None),
    ],
    twists=[twist("wasps", 2), twist("stuck_child")],
    bonus=["careful", "fast"], fast_hours=2, anchors=["orchard"], tags=["outdoors", "farm", "movement"],
    twist_premises={"wasps": "A wasp nest hangs in the best tree.",
                    "stuck_child": "A child climbed after you and cannot get down."}))

add(mission(
    "mission.d.deer_count", "d", "clans", minutes=10, pay=0.35,
    premise="Help the Nara count their deer in the clan forest.",
    client=resident(clan="nara"), slots={"forest": anchor("clan.nara.forest")},
    steps=[
        S("brief", talk(C), "count"),
        S("count", inspect("deer", at="slot:forest", count=12), "report",
          branch=[(twist_if("fawn_stuck"), "fawn"), (twist_if("antler_shed"), "antlers")]),
        S("fawn", perform("free_fawn", at="slot:forest"), "report"),
        S("antlers", collect("shed_antler", at="slot:forest", count=3), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("fawn_stuck", 2), twist("antler_shed")],
    outcomes={"done": outcome(extra={"clan_deed": ["nara", "helped_resident"]})},
    bonus=["gentle", "all_found"], anchors=["clan.nara.forest"], tags=["outdoors", "animal", "clan"],
    twist_premises={"fawn_stuck": "A fawn is caught in a bramble and its mother will not let you near.",
                    "antler_shed": "The clan's medicine-makers want this season's shed antlers too."}))

add(mission(
    "mission.d.insect_garden", "d", "clans", minutes=10, pay=0.35, party="solo",
    premise="Tend the Aburame insect gardens while the keepers are on duty.",
    client=resident(clan="aburame"), slots={"garden": anchor("clan.aburame.garden")},
    steps=[
        S("brief", talk(C), "tend"),
        S("tend", perform("water_beds", at="slot:garden", count=8), "report",
          branch=[(twist_if("escaped_beetles"), "beetles"), (twist_if("night_bloom"), "night")]),
        S("beetles", collect("beetle", at="slot:garden", count=6), "report"),
        S("night", wait_until("21:00", at="slot:garden"), "note"),
        S("note", inspect("night_bloom", at="slot:garden"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("escaped_beetles", 2), twist("night_bloom")],
    outcomes={"done": outcome(extra={"clan_deed": ["aburame", "helped_resident"]})},
    bonus=["gentle", "careful"], anchors=["clan.aburame.garden"], tags=["village", "animal", "clan"],
    twist_premises={"escaped_beetles": "A rare beetle colony has walked out of its box.",
                    "night_bloom": "The keepers need someone to watch a flower that opens only at night."}))

# --- market and shops ------------------------------------------------------------------------------------

add(mission(
    "mission.d.market_stall", "d", "shop", minutes=10, pay=0.35, party="solo",
    premise="Mind a stall on Market Day while the stallholder sees a supplier.",
    client=resident(job="stallholder"), slots={"stall": anchor("market.stall"), "thief": resident(age="child")},
    unlock={"calendar": {"weekday": "market_day"}},
    steps=[
        S("brief", talk(C), "sell"),
        S("sell", perform("serve_customer", at="slot:stall", count=6), "report",
          branch=[(twist_if("haggler"), "haggle"), (twist_if("shoplifter"), "chase"), (twist_if("rush"), "rush")]),
        S("haggle", choose({"hold_price": None, "give_in": "sold_cheap"}), "report"),
        S("chase", collect("stolen_goods", at="slot:thief"), "report"),
        S("rush", perform("serve_customer", at="slot:stall", count=8), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("haggler", 2), twist("shoplifter", 2), twist("rush")],
    outcomes={"done": outcome(), "sold_cheap": outcome(pay=0.85)},
    bonus=["fast", "clean_record"], fast_hours=2, anchors=["market.stall"], tags=["village", "market"],
    twist_premises={"haggler": "A famous haggler wants the best piece for half price.",
                    "shoplifter": "Small hands, quick feet, and a missing purse.",
                    "rush": "A festival crowd arrives all at once."}))

add(mission(
    "mission.d.flower_order", "d", "shop", minutes=8, pay=0.3, party="solo",
    premise="Help the Yamanaka flower shop fill a wedding order, every flower saying the right thing.",
    client=resident(clan="yamanaka", job="florist"), slots={"shop": anchor("clan.yamanaka.shop"),
                                                             "venue": anchor("shrine.hall")},
    steps=[
        S("brief", talk(C), "pick"),
        S("pick", collect("flower", at="slot:shop", count=12), "deliver",
          branch=[(twist_if("wrong_meaning"), "meaning"), (twist_if("wilting"), "wilt")]),
        S("meaning", inspect("flower_language", at="slot:shop", count=3), "deliver"),
        S("wilt", go("slot:venue"), "deliver"),
        S("deliver", deliver("bouquet", "slot:venue"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("wrong_meaning", 2), twist("wilting")],
    bonus=["careful", "fast"], fast_hours=2, anchors=["clan.yamanaka.shop", "shrine.hall"], tags=["village", "market"],
    twist_premises={"wrong_meaning": "Half the order says 'farewell' in the language of flowers.",
                    "wilting": "The heat is wilting the bouquets; get them there now."}))

# --- deliveries and messages ---------------------------------------------------------------------------

add(mission(
    "mission.d.delivery_run", "d", "delivery", minutes=10, pay=0.3, party="squad_or_solo",
    premise="Deliver a sack of parcels across the village before sundown.",
    client=resident(job="porter"),
    slots={"a": resident(), "b": resident(), "c": resident(), "gossip": resident()},
    steps=[
        S("collect", talk(C), "first"),
        S("first", deliver("parcel", "slot:a"), "second",
          branch=[(twist_if("swapped"), "swap")]),
        S("swap", inspect("parcel_label", count=2), "second"),
        S("second", deliver("parcel", "slot:b"), "third",
          branch=[(twist_if("moved_house"), "ask")]),
        S("ask", talk("slot:gossip"), "third"),
        S("third", deliver("parcel", "slot:c"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("swapped", 2), twist("moved_house", 2), twist("fragile", 1, harder=True, modifier=True)],
    bonus=["fast", "careful"], fast_hours=3, tags=["village", "delivery"],
    twist_premises={"swapped": "Two parcels have swapped labels.",
                    "moved_house": "One recipient has moved, and only the neighbours know where.",
                    "fragile": "One parcel rattles; no running and no roof-hopping with it."}))

add(mission(
    "mission.d.catering", "d", "delivery", minutes=8, pay=0.35,
    premise="Carry a restaurant's catering order to a training ground while it is still hot.",
    client=resident(job="cook"), slots={"kitchen": anchor("restaurant"), "ground": anchor("training_ground"),
                                        "genin": resident(group="shinobi", age="child")},
    steps=[
        S("pick_up", collect("catering_box", at="slot:kitchen", count=3), "carry"),
        S("carry", deliver("catering_box", "slot:ground"), "report",
          branch=[(twist_if("hungry_genin"), "hungry"), (twist_if("spill"), "spill")]),
        S("hungry", talk("slot:genin"), "carry2"),
        S("carry2", deliver("catering_box", "slot:ground"), "report"),
        S("spill", collect("catering_box", at="slot:kitchen"), "carry2"),
        S("report", talk(C), None),
    ],
    twists=[twist("hungry_genin", 2), twist("spill")],
    bonus=["fast", "careful"], fast_hours=1, anchors=["restaurant", "training_ground"], tags=["village", "delivery", "timed"],
    twist_premises={"hungry_genin": "Another squad offers to 'inspect' the food for you.",
                    "spill": "A box tips on the stairs; run back for another before it all goes cold."}))

add(mission(
    "mission.d.messenger", "d", "delivery", minutes=8, pay=0.3, party="solo",
    premise="Carry sealed letters between the Residence and three offices before the noon bell.",
    client=resident(job="clerk"), slots={"o1": anchor("office"), "o2": anchor("office"), "o3": anchor("office")},
    contested=True,
    steps=[
        S("collect", talk(C), "o1"),
        S("o1", deliver("sealed_letter", "slot:o1"), "o2"),
        S("o2", deliver("sealed_letter", "slot:o2"), "o3",
          branch=[(twist_if("wait_reply"), "wait")]),
        S("wait", wait_until("+1h", at="slot:o2"), "o3"),
        S("o3", deliver("sealed_letter", "slot:o3"), "report",
          branch=[(twist_if("rival_courier"), "race")]),
        S("race", perform("outrun", at="slot:o3"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("wait_reply", 2), twist("rival_courier", 1, harder=True)],
    bonus=["fast"], fast_hours=1, anchors=["office"], tags=["village", "delivery", "timed", "movement"],
    twist_premises={"wait_reply": "One office insists on sending a reply back with you.",
                    "rival_courier": "Another squad was given the same letters; first one there gets the credit."}))

add(mission(
    "mission.d.posters", "d", "posters", minutes=8, pay=0.2, party="squad_or_solo",
    premise="Put up posters for an upcoming event in every district.",
    client=resident(job="clerk"), slots={"boards": anchor("poster_board"), "rival_shop": resident(job="shopkeeper")},
    steps=[
        S("collect", talk(C), "post"),
        S("post", perform("pin_poster", at="slot:boards", count=8), "report",
          branch=[(twist_if("torn_down"), "watch"), (twist_if("typo"), "reprint"), (twist_if("windy"), "chase")]),
        S("watch", sneak("slot:boards"), "confront"),
        S("confront", talk("slot:rival_shop"), "post2"),
        S("post2", perform("pin_poster", at="slot:boards", count=4), "report"),
        S("reprint", craft("poster", 8), "post"),
        S("chase", collect("poster", count=5), "post2"),
        S("report", talk(C), None),
    ],
    twists=[twist("torn_down", 2), twist("typo"), twist("windy")],
    bonus=["fast", "unseen"], fast_hours=2, anchors=["poster_board"], tags=["village", "movement"],
    twist_premises={"torn_down": "Someone tears the posters down as fast as you put them up.",
                    "typo": "The date on every poster is wrong.",
                    "windy": "A gust takes half the stack over the rooftops."}))

# --- festivals ----------------------------------------------------------------------------------------

add(mission(
    "mission.d.festival_setup", "d", "festival", minutes=12, pay=0.45, party="squad",
    premise="Hang lanterns and raise stalls on the main street for the festival.",
    client=resident(job="organiser"), slots={"street": anchor("main_street"), "store": anchor("festival_store")},
    event={"before": "event.leaf_festival", "days": 3},
    steps=[
        S("brief", talk(C), "stalls"),
        S("stalls", perform("raise_stall", at="slot:street", count=4), "lanterns"),
        S("lanterns", perform("hang_lantern", at="slot:street", count=10), "report",
          branch=[(twist_if("rooftops"), "roofs"), (twist_if("missing_lanterns"), "missing"),
                  (twist_if("fireworks"), "fireworks")]),
        S("roofs", perform("wall_run_string", at="slot:street", count=3), "report"),
        S("missing", inspect("lantern_crate", at="slot:store"), "lanterns2"),
        S("lanterns2", perform("hang_lantern", at="slot:street", count=5), "report"),
        S("fireworks", deliver("fireworks_crate", "slot:store"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("rooftops", 2), twist("missing_lanterns"), twist("fireworks", 1, harder=True)],
    bonus=["careful", "teamwork", "fast"], fast_hours=4, anchors=["main_street", "festival_store"],
    tags=["village", "event", "movement"],
    twist_premises={"rooftops": "The lantern strings go from roof to roof, three storeys up.",
                    "missing_lanterns": "A whole crate of lanterns is missing from the store.",
                    "fireworks": "Carry the fireworks crate across the crowded street. Gently."}))

add(mission(
    "mission.d.night_lamps", "d", "festival", minutes=8, pay=0.25, party="solo",
    premise="Light a district's street lamps at dusk before full dark.",
    client=resident(job="lamplighter"), slots={"lamps": anchor("street_lamp"), "prowler": resident()},
    unlock={"time_between": ["16:00", "20:00"]},
    steps=[
        S("oil", talk(C), "light"),
        S("light", perform("light_lamp", at="slot:lamps", count=10), "report",
          branch=[(twist_if("oil_shortage"), "oil2"), (twist_if("prowler"), "prowl")]),
        S("oil2", buy("lamp_oil", at="place:market.oil", count=2), "light2"),
        S("light2", perform("light_lamp", at="slot:lamps", count=4), "report"),
        S("prowl", collect("stolen_goods", at="slot:prowler"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("oil_shortage", 2), twist("prowler")],
    bonus=["fast"], fast_hours=1, anchors=["street_lamp", "market.oil"], tags=["village", "night", "timed"],
    twist_premises={"oil_shortage": "The oil runs out with half the street still dark.",
                    "prowler": "Someone is using the dark to try the doors."}))

# --- repairs and building -------------------------------------------------------------------------------

add(mission(
    "mission.d.roof_repair", "d", "repairs", minutes=10, pay=0.35, party="squad_or_solo",
    premise="Patch a leaking roof before the evening rain.",
    client=resident(household=True), slots={"roof": anchor("client_roof"), "yard": anchor("carpenters_yard")},
    steps=[
        S("brief", talk(C), "tiles"),
        S("tiles", collect("roof_tile", at="slot:yard", count=8), "patch"),
        S("patch", perform("lay_tile", at="slot:roof", count=8), "report",
          branch=[(twist_if("bird_nest"), "nest"), (twist_if("stuck_cat"), "cat"), (twist_if("rain"), "rain")]),
        S("nest", perform("move_nest", at="slot:roof"), "report"),
        S("cat", collect("cat", at="slot:roof"), "report"),
        S("rain", perform("lay_tile", at="slot:roof", count=4), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("bird_nest", 2), twist("stuck_cat"), twist("rain", 1, harder=True)],
    bonus=["careful", "fast", "gentle"], fast_hours=3, anchors=["client_roof", "carpenters_yard"],
    tags=["village", "movement", "repairs"],
    twist_premises={"bird_nest": "A swallow has nested right over the leak.",
                    "stuck_cat": "The neighbour's cat followed you up and will not come down.",
                    "rain": "The rain arrives with four tiles still to go."}))

add(mission(
    "mission.d.fence_mending", "d", "repairs", minutes=10, pay=0.3, party="squad_or_solo",
    premise="Mend a garden fence between two houses.",
    client=resident(household=True), slots={"fence": anchor("client_garden"), "neighbour": resident(district="same:client"),
                                            "yard": anchor("carpenters_yard")},
    steps=[
        S("brief", talk(C), "posts"),
        S("posts", collect("fence_post", at="slot:yard", count=6), "mend"),
        S("mend", perform("set_post", at="slot:fence", count=6), "report",
          branch=[(twist_if("fence_line"), "line"), (twist_if("termites"), "termites")]),
        S("line", talk("slot:neighbour"), "settle"),
        S("settle", choose({"fair": None, "client": "sided_client", "neighbour": "sided_neighbour"}), "report"),
        S("termites", perform("replace_post", at="slot:fence", count=4), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("fence_line", 2), twist("termites")],
    outcomes={"done": outcome(), "sided_client": outcome(standing=1, extra={"hook": "quarrel_to_mediate"}),
              "sided_neighbour": outcome(pay=0.7, standing=-1)},
    bonus=["kind_choice", "fast"], fast_hours=3, anchors=["client_garden", "carpenters_yard"], tags=["village", "talk", "repairs"],
    twist_premises={"fence_line": "The neighbour says the fence was always a hand's width too far onto their land.",
                    "termites": "The old posts crumble in your hands."},
    choice_premises={"settle": "Measure fairly, take the client's side, or the neighbour's."}))

add(mission(
    "mission.d.timber_haul", "d", "construction", minutes=10, pay=0.4, party="squad",
    premise="Haul timber for the Kinoshita yard from the outer woodlot.",
    client=resident(clan="kinoshita"), slots={"woodlot": anchor("woodlot"), "yard": anchor("carpenters_yard")},
    steps=[
        S("brief", talk(C), "haul"),
        S("haul", deliver("timber", "slot:yard"), "report",
          branch=[(twist_if("log_roll"), "roll"), (twist_if("injured_apprentice"), "carry")]),
        S("roll", collect("timber", at="slot:woodlot", count=3), "haul2"),
        S("haul2", deliver("timber", "slot:yard"), "report"),
        S("carry", escort("apprentice", "place:hospital.desk"), "haul2"),
        S("report", talk(C), None),
    ],
    twists=[twist("log_roll", 2), twist("injured_apprentice")],
    bonus=["teamwork", "fast"], fast_hours=3, anchors=["woodlot", "carpenters_yard", "hospital.desk"],
    tags=["outdoors", "repairs"],
    twist_premises={"log_roll": "The stack gives way and three logs roll for the river.",
                    "injured_apprentice": "An apprentice crushes a foot; get them to the hospital first."}))

add(mission(
    "mission.d.moving_day", "d", "household", minutes=12, pay=0.45, party="squad",
    premise="Help a family move house across the village.",
    client=resident(household=True), slots={"old": anchor("client_home"), "new": anchor("vacant_home")},
    steps=[
        S("brief", talk(C), "pack"),
        S("pack", collect("moving_crate", at="slot:old", count=6), "move"),
        S("move", deliver("moving_crate", "slot:new"), "report",
          branch=[(twist_if("heirloom"), "heirloom"), (twist_if("cat_hides"), "cat"),
                  (twist_if("heavy_chest"), "chest")]),
        S("heirloom", deliver("heirloom", "slot:new"), "report"),
        S("cat", inspect("hiding_cat", at="slot:old"), "report"),
        S("chest", perform("chakra_lift", at="slot:old"), "move2"),
        S("move2", deliver("chest", "slot:new"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("heirloom", 2), twist("cat_hides", 2), twist("heavy_chest")],
    bonus=["careful", "teamwork", "fast"], fast_hours=4, anchors=["client_home", "vacant_home"], tags=["village", "household"],
    twist_premises={"heirloom": "Grandmother's tea set travels by hand, and only by hand.",
                    "cat_hides": "The cat does not want to move and has found the one place nobody looks.",
                    "heavy_chest": "A chest nobody can lift without chakra."}))

# --- clearing, rivers and outdoors -------------------------------------------------------------------------

add(mission(
    "mission.d.drain_clearing", "d", "clearing", minutes=8, pay=0.25, party="squad_or_solo",
    premise="Clear a blocked drain before the street floods.",
    client=resident(household=True), slots={"drain": anchor("street_drain")},
    steps=[
        S("brief", talk(C), "clear"),
        S("clear", collect("drain_muck", at="slot:drain", count=8), "report",
          branch=[(twist_if("lost_ring"), "ring"), (twist_if("frogs"), "frogs")]),
        S("ring", choose({"return": None, "keep": "kept_ring"}), "report",
          branch=[(chose("ring", "return"), "owner")]),
        S("owner", deliver("ring", C), "report"),
        S("frogs", collect("frog", at="slot:drain", count=5), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("lost_ring", 2), twist("frogs")],
    outcomes={"done": outcome(), "kept_ring": outcome(extra={"item": "ring", "clean_record": False})},
    bonus=["fast", "clean_record"], fast_hours=2, anchors=["street_drain"], tags=["village", "clearing"],
    twist_premises={"lost_ring": "A ring glints in the muck; the client lost one last spring.",
                    "frogs": "The drain is a frog kingdom; move them to the river."}))

add(mission(
    "mission.d.lot_clearing", "d", "clearing", minutes=10, pay=0.3, party="squad",
    premise="Clear an overgrown lot for a new training post.",
    client=resident(job="groundskeeper"), slots={"lot": anchor("overgrown_lot")},
    steps=[
        S("brief", talk(C), "clear"),
        S("clear", collect("debris", at="slot:lot", count=16), "report",
          branch=[(twist_if("old_trap"), "trap"), (twist_if("hornets"), "hornets")]),
        S("trap", perform("disarm_wire", at="slot:lot", count=2), "report"),
        S("hornets", perform("smoke_bomb", at="slot:lot"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("old_trap", 2, harder=True), twist("hornets")],
    bonus=["no_knockouts", "fast"], fast_hours=3, anchors=["overgrown_lot"], tags=["outdoors", "clearing"],
    twist_premises={"old_trap": "An old training trap is still armed under the weeds.",
                    "hornets": "Hornets have claimed the woodpile."}))

add(mission(
    "mission.d.river_cleanup", "d", "river", minutes=10, pay=0.3, party="squad_or_solo",
    premise="Fish the rubbish out of the river below the market bridge.",
    client=resident(job="fisher"), slots={"bank": anchor("riverbank"), "addressee": resident()},
    steps=[
        S("brief", talk(C), "clean"),
        S("clean", collect("river_rubbish", at="slot:bank", count=12), "report",
          branch=[(twist_if("bottle"), "bottle"), (twist_if("snagged_net"), "net"),
                  (twist_if("midstream"), "midstream")]),
        S("bottle", deliver("bottled_letter", "slot:addressee"), "report"),
        S("net", perform("free_net", at="slot:bank"), "report"),
        S("midstream", perform("water_walk_collect", at="slot:bank", count=4), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("bottle", 2), twist("snagged_net"), twist("midstream")],
    bonus=["all_found", "fast"], fast_hours=2, anchors=["riverbank"], tags=["outdoors", "river"],
    twist_premises={"bottle": "A bottle with a letter inside, addressed to someone in the village.",
                    "snagged_net": "A fisher's net is snagged on the weir.",
                    "midstream": "The worst of it is out on the water, where only water-walking reaches."}))

add(mission(
    "mission.d.fishing_haul", "d", "river", minutes=10, pay=0.35,
    premise="Help the fish stall's supplier land the morning catch.",
    client=resident(job="fisher"), slots={"boat": anchor("river_jetty"), "stall": anchor("market.fish")},
    unlock={"time_between": ["05:00", "10:00"]},
    steps=[
        S("brief", talk(C), "haul"),
        S("haul", perform("haul_net", at="slot:boat", count=4), "carry",
          branch=[(twist_if("big_one"), "big"), (twist_if("net_tear"), "mend")]),
        S("big", perform("hold_line", at="slot:boat"), "carry"),
        S("mend", craft("net_patch"), "carry"),
        S("carry", deliver("fish_crate", "slot:stall"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("big_one", 2), twist("net_tear")],
    bonus=["fast", "careful"], fast_hours=2, anchors=["river_jetty", "market.fish"], tags=["outdoors", "river", "market"],
    twist_premises={"big_one": "Something enormous takes the line.",
                    "net_tear": "The net tears with the catch half in."}))

add(mission(
    "mission.d.laundry", "d", "household", minutes=8, pay=0.2, party="solo",
    premise="Help the riverside washerwomen with a hotel's laundry.",
    client=resident(job="washer"), slots={"bank": anchor("riverbank"), "inn": anchor("inn")},
    steps=[
        S("brief", talk(C), "wash"),
        S("wash", perform("wash_linen", at="slot:bank", count=8), "deliver",
          branch=[(twist_if("sheet_in_wind"), "sheet"), (twist_if("dye_mixup"), "dye")]),
        S("sheet", collect("sheet", count=1), "deliver"),
        S("dye", inspect("dyed_linen", at="slot:bank", count=3), "deliver"),
        S("deliver", deliver("linen", "slot:inn"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("sheet_in_wind", 2), twist("dye_mixup")],
    bonus=["fast", "careful"], fast_hours=2, anchors=["riverbank", "inn"], tags=["village", "river", "household"],
    twist_premises={"sheet_in_wind": "A sheet takes off across the rooftops like a kite.",
                    "dye_mixup": "Someone washed red with white; find which loads can be saved."}))

add(mission(
    "mission.d.herb_gathering", "d", "hospital", minutes=10, pay=0.35,
    premise="Gather medicinal herbs on the slopes outside the wall for the hospital.",
    client=resident(clan="suzuran"), slots={"slope": anchor("herb_slope"), "hospital": anchor("hospital.desk")},
    steps=[
        S("brief", talk(C), "gather"),
        S("gather", collect("herb", at="slot:slope", count=10), "deliver",
          branch=[(twist_if("lookalike"), "check"), (twist_if("snake"), "snake")]),
        S("check", inspect("herb", count=5), "deliver"),
        S("snake", perform("shoo_gently", at="slot:slope"), "deliver"),
        S("deliver", deliver("herb", "slot:hospital"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("lookalike", 2), twist("snake")],
    bonus=["careful", "gentle"], anchors=["herb_slope", "hospital.desk"], tags=["outdoors", "hospital"],
    twist_premises={"lookalike": "A poisonous lookalike grows among the herbs; check every stem.",
                    "snake": "A snake has made the best patch its home."}))

add(mission(
    "mission.d.hospital_orderly", "d", "hospital", minutes=10, pay=0.4,
    premise="Help on the wards for a day: linens, meals and errands for the medics.",
    client=resident(job="medic"), slots={"ward": anchor("hospital.ward"), "garden": anchor("herb_garden"),
                                         "wanderer": resident(age="elder")},
    steps=[
        S("brief", talk(C), "rounds"),
        S("rounds", deliver("linen", "slot:ward"), "meals",
          branch=[(twist_if("wanderer"), "find"), (twist_if("herb_shortage"), "herbs")]),
        S("find", escort("slot:wanderer", "slot:ward"), "meals"),
        S("herbs", collect("herb", at="slot:garden", count=6), "meals"),
        S("meals", perform("serve_meal", at="slot:ward", count=6), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("wanderer", 2), twist("herb_shortage")],
    bonus=["gentle", "fast"], fast_hours=3, anchors=["hospital.ward", "herb_garden"], tags=["village", "hospital"],
    twist_premises={"wanderer": "A confused old patient has walked out in his slippers.",
                    "herb_shortage": "The medics are out of a herb only the Suzuran gardens grow."}))

# --- elders, shrines and households ------------------------------------------------------------------------

add(mission(
    "mission.d.elder_errands", "d", "elders", minutes=8, pay=0.2, party="solo",
    premise="Run a shopping list of errands for an elderly resident.",
    client=resident(age="elder"), slots={"shop1": anchor("market.grocer"), "shop2": anchor("market.tea")},
    steps=[
        S("list", talk(C), "grocer"),
        S("grocer", buy("groceries", at="slot:shop1"), "tea"),
        S("tea", buy("tea_leaves", at="slot:shop2"), "home",
          branch=[(twist_if("forgot_one"), "again")]),
        S("again", buy("lamp_oil", at="place:market.oil"), "home"),
        S("home", deliver("groceries", C), None,
          branch=[(twist_if("story_time"), "story")]),
        S("story", perform("listen", at="slot:client"), None,
          on_done=[{"bond_event": ["slot:client", "heart_to_heart"]}]),
    ],
    twists=[twist("forgot_one", 2), twist("story_time", 2)],
    bonus=["fast", "extra_mile"], fast_hours=2, anchors=["market.grocer", "market.tea", "market.oil"],
    tags=["village", "talk", "market"],
    twist_premises={"forgot_one": "They remember one more thing, and then another.",
                    "story_time": "They want you to stay for tea and a story of the old days."}))

add(mission(
    "mission.d.shrine_cleaning", "d", "shrine", minutes=8, pay=0.25, party="squad_or_solo",
    premise="Sweep the shrine steps and re-tie the weathered charms.",
    client=resident(job="priest"), slots={"steps": anchor("shrine.steps"), "crow_roost": anchor("shrine.roof")},
    steps=[
        S("brief", talk(C), "sweep"),
        S("sweep", perform("sweep", at="slot:steps", count=6), "charms"),
        S("charms", perform("tie_charm", at="slot:steps", count=8), "report",
          branch=[(twist_if("crows"), "crows"), (twist_if("fox_offering"), "fox")]),
        S("crows", collect("offering", at="slot:crow_roost", count=4), "report"),
        S("fox", inspect("fox_statue", at="slot:steps"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("crows", 2), twist("fox_offering")],
    bonus=["careful", "fast"], fast_hours=2, anchors=["shrine.steps", "shrine.roof"], tags=["village", "shrine"],
    twist_premises={"crows": "The crows have been stealing offerings and hoarding them on the roof.",
                    "fox_offering": "Someone leaves fried tofu at the fox statue every night; the priest wants to know who."}))

add(mission(
    "mission.d.bathhouse", "d", "bathhouse", minutes=10, pay=0.3, party="solo",
    premise="Scrub the bath house and stoke its fires before the evening rush.",
    client=resident(job="bath_keeper"), slots={"bath": anchor("bathhouse"), "boiler": anchor("bathhouse.boiler")},
    steps=[
        S("brief", talk(C), "scrub"),
        S("scrub", perform("scrub_tiles", at="slot:bath", count=8), "stoke"),
        S("stoke", perform("stoke_fire", at="slot:boiler", count=3), "report",
          branch=[(twist_if("boiler_trouble"), "fix"), (twist_if("locker_key"), "key")]),
        S("fix", perform("technique:nature", at="slot:boiler"), "report"),
        S("key", inspect("locker_key", at="slot:bath"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("boiler_trouble", 2), twist("locker_key")],
    bonus=["fast"], fast_hours=2, anchors=["bathhouse", "bathhouse.boiler"], tags=["village", "indoors"],
    twist_premises={"boiler_trouble": "The boiler will not catch; a fire or wind technique would help.",
                    "locker_key": "A regular lost their locker key in the big bath."}))

add(mission(
    "mission.d.kitchen_help", "d", "cooking", minutes=10, pay=0.35,
    premise="Help the barbecue house's kitchen through a big party's order.",
    client=resident(clan="akimichi"), slots={"kitchen": anchor("barbecue_house"), "grocer": anchor("market.grocer")},
    steps=[
        S("brief", talk(C), "prep"),
        S("prep", perform("prep_ingredients", at="slot:kitchen", count=6), "serve",
          branch=[(twist_if("missing_spice"), "spice"), (twist_if("taste_test"), "taste")]),
        S("spice", buy("spice", at="slot:grocer"), "serve"),
        S("taste", choose({"honest": None, "polite": None}), "serve"),
        S("serve", perform("serve_table", at="slot:kitchen", count=5), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("missing_spice", 2), twist("taste_test")],
    outcomes={"done": outcome(extra={"clan_deed": ["akimichi", "helped_resident"]})},
    bonus=["fast", "extra_mile"], fast_hours=2, anchors=["barbecue_house", "market.grocer"], tags=["village", "cooking"],
    twist_premises={"missing_spice": "The house spice ran out mid-service.",
                    "taste_test": "The chef wants your honest opinion of a new sauce. It is not good."}))

# --- training grounds, the gate, seasons ------------------------------------------------------------------

add(mission(
    "mission.d.training_upkeep", "d", "training", minutes=8, pay=0.25,
    premise="Repair the dummies and posts at a training ground and rake the field.",
    client=resident(job="groundskeeper"), slots={"ground": anchor("training_ground"), "challenger": resident(group="shinobi", age="child")},
    steps=[
        S("brief", talk(C), "repair"),
        S("repair", perform("repair_dummy", at="slot:ground", count=4), "rake",
          branch=[(twist_if("stray_shuriken"), "shuriken"), (twist_if("challenge"), "spar")]),
        S("shuriken", collect("stray_shuriken", at="slot:ground", count=10), "rake"),
        S("spar", perform("spar", at="slot:ground"), "rake",
          on_done=[{"bond_event": ["slot:challenger", "spar_won"]}]),
        S("rake", perform("rake", at="slot:ground", count=6), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("stray_shuriken", 2), twist("challenge", 2)],
    bonus=["all_found", "fast"], fast_hours=2, anchors=["training_ground"], tags=["outdoors", "training"],
    twist_premises={"stray_shuriken": "Last week's class left the grass full of shuriken.",
                    "challenge": "A Genin from another squad wants a spar before you go."}))

add(mission(
    "mission.d.gate_logbook", "d", "gate", minutes=8, pay=0.3, party="solo",
    premise="Help the gate guards log the day's travellers through the main gate.",
    client=resident(clan="hagane"), slots={"gate": anchor("gate.main"), "farmer": resident(job="farmer")},
    steps=[
        S("brief", talk(C), "log"),
        S("log", inspect("traveller_pass", at="slot:gate", count=6), "report",
          branch=[(twist_if("odd_cart"), "cart"), (twist_if("lost_traveller"), "guide")]),
        S("cart", inspect("cart", at="slot:gate"), "decide"),
        S("decide", choose({"pass": None, "hold": "held_cart"}), "report"),
        S("guide", escort("traveller", "place:inn"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("odd_cart", 2), twist("lost_traveller")],
    outcomes={"done": outcome(), "held_cart": outcome(pay=1.0, extra={"lead": "district.b2.contraband"})},
    bonus=["fast", "kind_choice"], fast_hours=2, anchors=["gate.main", "inn"], tags=["village", "gate", "talk"],
    twist_premises={"odd_cart": "A cart's papers are in order, but it sits too low on its wheels.",
                    "lost_traveller": "A traveller has no idea where the inn they booked is."},
    choice_premises={"decide": "Let the cart through or hold it for the guard captain."}))

add(mission(
    "mission.d.snow_clearing", "d", "seasonal", minutes=10, pay=0.3, party="squad",
    premise="Clear snow from roofs and lanes before it brings a roof down.",
    client=resident(job="clerk"), slots={"roofs": anchor("client_roof"), "lane": anchor("residential_lane"),
                                         "kids": resident(age="child")},
    season=["winter"],
    steps=[
        S("brief", talk(C), "roofs"),
        S("roofs", perform("shovel_roof", at="slot:roofs", count=6), "lane",
          branch=[(twist_if("slide"), "slide"), (twist_if("snowball_ambush"), "ambush")]),
        S("slide", perform("dodge", at="slot:lane"), "lane"),
        S("ambush", perform("snowball_fight", at="slot:lane"), "lane",
          on_done=[{"bond_event": ["slot:kids", "favor"]}]),
        S("lane", perform("shovel_lane", at="slot:lane", count=8), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("slide", 2), twist("snowball_ambush", 2)],
    bonus=["teamwork", "fast"], fast_hours=3, anchors=["client_roof", "residential_lane"], tags=["village", "seasonal"],
    twist_premises={"slide": "A whole roof of snow lets go at once.",
                    "snowball_ambush": "The street's children declare war."}))

add(mission(
    "mission.d.leaf_raking", "d", "seasonal", minutes=8, pay=0.2, party="squad_or_solo",
    premise="Rake the leaves in the park by the Academy.",
    client=resident(job="groundskeeper"), slots={"park": anchor("park")},
    season=["autumn"],
    steps=[
        S("brief", talk(C), "rake"),
        S("rake", perform("rake", at="slot:park", count=10), "report",
          branch=[(twist_if("hidden_treasure"), "treasure"), (twist_if("bonfire"), "bonfire")]),
        S("treasure", choose({"return": None, "keep": "kept_find"}), "report"),
        S("bonfire", perform("roast_sweet_potato", at="slot:park"), "report",
          on_done=[{"bond_event": ["role:squad", "meal_together"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("hidden_treasure"), twist("bonfire", 2)],
    outcomes={"done": outcome(), "kept_find": outcome(extra={"clean_record": False})},
    bonus=["fast", "clean_record"], fast_hours=2, anchors=["park"], tags=["outdoors", "seasonal"],
    twist_premises={"hidden_treasure": "Under the leaves, a purse someone lost weeks ago.",
                    "bonfire": "The groundskeeper says the pile is perfect for roasting sweet potatoes."}))

# --- recurring clients ------------------------------------------------------------------------------------

add(mission(
    "mission.d.kiln_firing", "d", "chain", minutes=12, pay=0.45, chain="chain.kiln",
    premise="Keep the kiln family's fire at the right heat through a night's firing.",
    client={"pick": "role", "role": "role:client.kiln_grandmother"},
    slots={"kiln": anchor("kiln_yard"), "woodlot": anchor("woodlot")},
    unlock={"time_between": ["16:00", "22:00"]},
    steps=[
        S("brief", talk(C), "wood"),
        S("wood", collect("firewood", at="slot:woodlot", count=12), "fire"),
        S("fire", perform("stoke_fire", at="slot:kiln", count=6), "dawn",
          branch=[(twist_if("crack"), "crack"), (twist_if("rain_night"), "cover")]),
        S("crack", inspect("cracked_pot", at="slot:kiln", count=2), "dawn"),
        S("cover", perform("hold_tarp", at="slot:kiln", count=3), "dawn"),
        S("dawn", wait_until("06:00", at="slot:kiln"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("crack", 2), twist("rain_night", 1, harder=True)],
    bonus=["careful", "extra_mile"], tags=["village", "night", "chain"],
    twist_premises={"crack": "A pot cracks in the heat; find which shelf is too close to the flame.",
                    "rain_night": "Rain on the kiln roof; hold the tarp until it passes."}))
