"""B, A and S-rank templates and ANBU operations: laid out now, authored after the beta.

Every template here is `status: later`. The graphs are complete and valid so the formats, the desk and the
generator hold them today; regions, enemy loadouts and dialogue arrive with the Chunin, Jonin and ANBU
arcs. Targets are roles (`role:target.*`), bound when the mission is rolled, never named.
"""
from mkit import (S, anchor, chose, choose, collect, defeat, deliver, end, enemy_group, escort, go, inspect,
                  mission, outcome, perform, protect, region, resident, role, sleep, sneak, survive, talk, twist,
                  twist_if, wait_until)

C = "slot:client"
CHUNIN = {"rank_at_least": "chunin"}
JONIN = {"rank_at_least": "jonin"}
ANBU = {"rank_at_least": "anbu"}
S_RANK = {"all": [{"rank_at_least": "jonin"}, {"level_at_least": 42}]}

T = []
add = T.append


def travel(nxt):
    return S("travel", go("place:gate.travel_desk"), nxt)


# --- B rank (Chunin) -----------------------------------------------------------------------------------

add(mission(
    "mission.b.fortress_infiltration", "b", "infiltration", minutes=40, days=2, pay=0.5, unlock=CHUNIN,
    premise="Slip into a bandit warlord's hill fort and bring out the ledger of who pays him.",
    client=resident(job="magistrate", resident_of="any"),
    slots={"fort": region("region:hill_fort"), "wall": anchor("fort.wall"), "keep": anchor("fort.keep"),
           "guards": enemy_group("bandit.fort_guard"), "gate": anchor("fort.gate")},
    steps=[
        travel("approach"),
        S("approach", sneak("slot:wall"), "keep", optional=["unseen"]),
        S("keep", sneak("slot:keep"), "ledger",
          branch=[(twist_if("prisoner"), "prisoner")]),
        S("prisoner", choose({"free": None, "leave": None}), "ledger",
          branch=[(chose("prisoner", "free"), "free")]),
        S("free", escort("prisoner", "slot:gate"), "ledger"),
        S("ledger", collect("ledger", at="slot:keep"), "out"),
        S("out", sneak("slot:gate"), "report",
          branch=[(twist_if("alarm"), "fight")]),
        S("fight", defeat("slot:guards", at="slot:gate"), "report", on_enter=[{"spawn_group": ["slot:guards", "slot:gate"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("prisoner", 2), twist("alarm", 2, harder=True)],
    bonus=["unseen", "no_alarm", "no_knockouts"], enemies=["bandit.fort_guard"], regions=["region:hill_fort"],
    tags=["stealth", "infiltration", "travel"],
    twist_premises={"prisoner": "A prisoner in the cellar begs to be taken along.",
                    "alarm": "A dog catches your scent on the way out."}))

add(mission(
    "mission.b.scroll_recovery", "b", "recovery", minutes=40, pay=0.55, unlock=CHUNIN,
    premise="Two missing-nin stole a sealed technique scroll from a temple; get it back before they sell it.",
    client=resident(job="priest", resident_of="any"),
    slots={"trail": anchor("forest.trail"), "camp": anchor("forest.camp"), "pair": enemy_group("missing_nin.pair")},
    steps=[
        travel("trail"),
        S("trail", inspect("tracks", at="slot:trail", count=4), "camp"),
        S("camp", defeat("slot:pair", at="slot:camp"), "scroll", on_enter=[{"spawn_group": ["slot:pair", "slot:camp"]}]),
        S("scroll", collect("sealed_scroll", at="slot:camp"), "report",
          branch=[(twist_if("buyer"), "buyer")]),
        S("buyer", defeat("missing_nin.chunin", at="slot:camp"), "report",
          on_enter=[{"spawn_group": ["missing_nin.chunin", "slot:camp"]}]),
        S("report", deliver("sealed_scroll", C), None),
    ],
    twists=[twist("buyer", 2, harder=True), twist("decoy_scroll", 1, modifier=True)],
    fast_hours=24, bonus=["fast", "no_knockouts", "clean_record"], enemies=["missing_nin.pair", "missing_nin.chunin"],
    regions=["region:northern_forest"], tags=["travel", "fight", "recovery", "tracking"],
    twist_premises={"buyer": "The buyer arrives as you take the scroll back.",
                    "decoy_scroll": "The scroll they carry is a decoy; the real one is buried at their camp."}))

add(mission(
    "mission.b.village_defence", "b", "defence", minutes=45, days=2, pay=0.6, unlock=CHUNIN,
    premise="A border village expects a raid by a mercenary band; prepare its defences and hold.",
    client=resident(job="headman", resident_of="any"),
    slots={"square": anchor("border.square"), "walls": anchor("border.palisade"), "band": enemy_group("mercenary.band")},
    steps=[
        travel("prepare"),
        S("prepare", perform("set_trap", at="slot:walls", count=6), "train"),
        S("train", perform("drill_villagers", at="slot:square", count=3), "hold"),
        S("hold", survive("06:00", at="slot:walls"), "report", on_enter=[{"spawn_group": ["slot:band", "slot:walls"]}],
          branch=[(twist_if("second_wave"), "wave")]),
        S("wave", defeat("mercenary.captain", at="slot:square"), "report",
          on_enter=[{"spawn_group": ["mercenary.captain", "slot:square"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("second_wave", 2, harder=True), twist("traitor_villager", 1, modifier=True)],
    bonus=["client_unharmed", "no_knockouts", "teamwork"], enemies=["mercenary.band", "mercenary.captain"],
    regions=["region:border_village"], tags=["travel", "defence", "fight"],
    twist_premises={"second_wave": "Their captain comes himself at dawn.",
                    "traitor_villager": "Someone in the village opened a gate last time."}))

add(mission(
    "mission.b.warlord", "b", "elimination", minutes=40, days=2, pay=0.6, unlock=CHUNIN,
    premise="A bandit warlord holds a valley to ransom; end his hold on it (capture or eliminate, by the client's terms).",
    client=resident(job="magistrate", resident_of="any"),
    slots={"target": role("role:target.warlord"), "camp": anchor("valley.camp"), "guard": enemy_group("bandit.fort_guard")},
    steps=[
        travel("scout"),
        S("scout", sneak("slot:camp"), "strike", optional=["unseen"]),
        S("strike", defeat("slot:guard", at="slot:camp"), "target", on_enter=[{"spawn_group": ["slot:guard", "slot:camp"]}]),
        S("target", defeat("slot:target", at="slot:camp"), "terms"),
        S("terms", choose({"capture": None, "finish": "eliminated"}), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("body_double", 2, modifier=True), twist("hostage_valley", 1, harder=True, modifier=True)],
    outcomes={"done": outcome(extra={"deed": "defended_village"}), "eliminated": outcome(pay=1.0)},
    bonus=["unseen", "spared", "no_knockouts"], enemies=["bandit.fort_guard", "bandit.warlord"],
    regions=["region:valley"], tags=["travel", "fight", "target"],
    twist_premises={"body_double": "The man in the warlord's armour is a double.",
                    "hostage_valley": "He holds the valley's headmen as hostages in his camp."}))

add(mission(
    "mission.b.envoy_escort", "b", "escort", minutes=40, days=3, pay=0.55, unlock=CHUNIN,
    premise="Escort a daimyo's envoy to a neighbouring land's court and back.",
    client=resident(job="envoy", resident_of="any"),
    slots={"court": anchor("capital.court"), "road": anchor("capital.road"), "attackers": enemy_group("assassin.team")},
    steps=[
        travel("road"),
        S("road", escort(C, "slot:road"), "court", on_enter=[{"spawn_group": ["slot:attackers", "slot:road"]}]),
        S("court", protect(C, until="+6h", at="slot:court"), "home",
          branch=[(twist_if("poison"), "poison")]),
        S("poison", inspect("cup", at="slot:court", count=3), "home"),
        S("home", escort(C, "place:gate.main"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("poison", 2), twist("envoy_defects", 1, harder=True, modifier=True)],
    bonus=["client_unharmed", "no_alarm"], enemies=["assassin.team"], regions=["region:capital"],
    tags=["travel", "escort", "politics", "fight"],
    twist_premises={"poison": "The welcome tea is not what it seems.",
                    "envoy_defects": "The envoy wants to stay, and asks you not to stop them."}))

add(mission(
    "mission.b.hostage_rescue", "b", "rescue", minutes=40, pay=0.6, unlock=CHUNIN,
    premise="Kidnappers hold a merchant family's child in a river mill; get the child out alive.",
    client=resident(job="trader"),
    slots={"mill": anchor("river.mill"), "kidnappers": enemy_group("thug.kidnappers")},
    steps=[
        travel("approach"),
        S("approach", sneak("slot:mill"), "rescue", optional=["unseen"]),
        S("rescue", escort("hostage", "place:gate.main"), "report",
          branch=[(twist_if("discovered"), "fight")]),
        S("fight", protect("hostage", at="slot:mill"), "rescue2", on_enter=[{"spawn_group": ["slot:kidnappers", "slot:mill"]}]),
        S("rescue2", escort("hostage", "place:gate.main"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("discovered", 2, harder=True), twist("two_hostages", 1, modifier=True)],
    bonus=["unseen", "client_unharmed", "no_alarm"], enemies=["thug.kidnappers"], regions=["region:river_crossing"],
    tags=["travel", "rescue", "stealth"],
    twist_premises={"discovered": "A kidnapper comes down for water at the worst moment.",
                    "two_hostages": "There are two children, not one."}))

add(mission(
    "mission.b.missing_nin_hunt", "b", "hunt", minutes=40, days=2, pay=0.6, unlock=CHUNIN,
    premise="Hunt down a pair of missing-nin seen on the Fire Country's roads.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"town": anchor("town.inn"), "ambush": anchor("forest.trail"), "pair": enemy_group("missing_nin.pair")},
    steps=[
        travel("ask"),
        S("ask", inspect("rumour", at="slot:town", count=3), "trail"),
        S("trail", inspect("tracks", at="slot:ambush", count=3), "fight"),
        S("fight", defeat("slot:pair", at="slot:ambush"), "report", on_enter=[{"spawn_group": ["slot:pair", "slot:ambush"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("they_ambush_first", 2, harder=True, modifier=True), twist("one_surrenders", 1, modifier=True)],
    fast_hours=36, bonus=["fast", "no_knockouts", "spared"], enemies=["missing_nin.pair"], regions=["region:post_town"],
    tags=["travel", "hunt", "fight"],
    twist_premises={"they_ambush_first": "They knew you were coming.",
                    "one_surrenders": "One of them throws down their kunai and asks for a trial at home."}))

add(mission(
    "mission.b.supply_sabotage", "b", "sabotage", minutes=40, pay=0.55, unlock=CHUNIN,
    premise="A foreign band is stockpiling weapons at a border depot; spoil the stockpile without starting a war.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"depot": anchor("border.depot"), "guards": enemy_group("enemy.squad")},
    steps=[
        travel("approach"),
        S("approach", sneak("slot:depot"), "spoil", optional=["unseen"]),
        S("spoil", perform("paper_bomb_set", at="slot:depot", count=4), "out"),
        S("out", sneak("place:gate.travel_desk"), "report",
          branch=[(twist_if("patrol"), "fight")]),
        S("fight", defeat("slot:guards", at="slot:depot"), "report", on_enter=[{"spawn_group": ["slot:guards", "slot:depot"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("patrol", 2, harder=True), twist("civilian_workers", 1, modifier=True)],
    bonus=["unseen", "no_alarm", "spared"], enemies=["enemy.squad"], regions=["region:border_depot"],
    tags=["travel", "stealth", "sabotage"],
    twist_premises={"patrol": "A patrol changes its route tonight.",
                    "civilian_workers": "Hired civilians sleep in the depot; get them out first."}))

add(mission(
    "mission.b.spy_in_town", "b", "investigation", minutes=40, days=2, pay=0.55, unlock=CHUNIN,
    premise="Find the spy who sells the post town's caravan schedules to raiders.",
    client=resident(job="magistrate", resident_of="any"),
    slots={"town": anchor("town.square"), "a": resident(resident_of="any"), "b": resident(resident_of="any"),
           "c": resident(resident_of="any"), "dead_drop": anchor("town.shrine")},
    steps=[
        travel("talk_a"),
        S("talk_a", talk("slot:a"), "talk_b"),
        S("talk_b", talk("slot:b"), "talk_c"),
        S("talk_c", talk("slot:c"), "drop"),
        S("drop", wait_until("02:00", at="slot:dead_drop"), "accuse"),
        S("accuse", choose({"a": None, "b": None, "c": None}), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("spy_a", 1, modifier=True), twist("spy_b", 1, modifier=True), twist("spy_c", 1, modifier=True)],
    bonus=["unseen", "kind_choice"], regions=["region:post_town"], tags=["travel", "investigation", "talk"],
    twist_premises={"spy_a": "The rolled spy is the first suspect.", "spy_b": "The rolled spy is the second.",
                    "spy_c": "The rolled spy is the third."}))

add(mission(
    "mission.b.bridge_builders", "b", "guard", minutes=45, days=3, pay=0.6, unlock=CHUNIN,
    premise="Guard a bridge-builder whose bridge will free a poor town from a shipping boss's grip.",
    client=resident(job="builder", resident_of="any"),
    slots={"bridge": anchor("coast.bridge"), "thugs": enemy_group("thug.hired"), "enforcer": enemy_group("missing_nin.chunin")},
    steps=[
        travel("work"),
        S("work", protect(C, until="18:00", at="slot:bridge"), "night",
          on_enter=[{"spawn_group": ["slot:thugs", "slot:bridge"]}]),
        S("night", sleep("place:coast.house"), "enforcer"),
        S("enforcer", defeat("slot:enforcer", at="slot:bridge"), "report",
          on_enter=[{"spawn_group": ["slot:enforcer", "slot:bridge"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("town_stands_up", 2, modifier=True), twist("builder_lied", 1, modifier=True)],
    bonus=["client_unharmed", "no_knockouts", "teamwork"], enemies=["thug.hired", "missing_nin.chunin"],
    regions=["region:coast_town"], tags=["travel", "guard", "fight"],
    twist_premises={"town_stands_up": "The town comes out with tools to stand by the builder.",
                    "builder_lied": "The builder said C-rank; the danger is far beyond it."}))

add(mission(
    "mission.b.quarantine", "b", "medical", minutes=40, days=2, pay=0.5, unlock=CHUNIN,
    premise="A fever has closed a hill village; bring medicine in, keep order, and find the source.",
    client=resident(job="medic"),
    slots={"village": anchor("hills.village"), "well": anchor("hills.well")},
    steps=[
        travel("deliver"),
        S("deliver", deliver("medicine_crate", "slot:village"), "order"),
        S("order", perform("calm_crowd", at="slot:village", count=3), "source"),
        S("source", inspect("water_sample", at="slot:well", count=3), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("looters", 2, harder=True, modifier=True), twist("poisoned_well", 1, modifier=True)],
    fast_hours=24, bonus=["kind_choice", "fast"], regions=["region:hill_village"], tags=["travel", "medical", "investigation"],
    twist_premises={"looters": "Looters move in on the empty houses.",
                    "poisoned_well": "The fever is no fever: someone poisoned the well."}))

add(mission(
    "mission.b.allied_courier", "b", "courier", minutes=35, pay=0.5, unlock=CHUNIN,
    premise="Carry a treaty draft to an allied village, through land where others would like to read it.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"gate": anchor("allied.gate"), "hunters": enemy_group("enemy.hunter_squad")},
    steps=[
        travel("road"),
        S("road", sneak("slot:gate"), "deliver", optional=["unseen"],
          branch=[(twist_if("hunters"), "fight")]),
        S("fight", defeat("slot:hunters", at="slot:gate"), "deliver", on_enter=[{"spawn_group": ["slot:hunters", "slot:gate"]}]),
        S("deliver", deliver("treaty_draft", "slot:gate"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("hunters", 2, harder=True), twist("cipher", 1, modifier=True)],
    bonus=["unseen", "fast"], fast_hours=24, enemies=["enemy.hunter_squad"], regions=["region:allied_village"],
    tags=["travel", "courier", "stealth"],
    twist_premises={"hunters": "A hunter squad has been sent to take it from you.",
                    "cipher": "The allies want the draft read aloud in cipher at the gate."}))

add(mission(
    "mission.b.capture_rogue", "b", "capture", minutes=40, pay=0.6, unlock=CHUNIN,
    premise="Bring a deserter of the Leaf home alive to face judgement.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"target": role("role:target.deserter"), "hideout": anchor("forest.hollow")},
    steps=[
        travel("find"),
        S("find", inspect("tracks", at="slot:hideout", count=4), "fight"),
        S("fight", defeat("slot:target", at="slot:hideout"), "talk"),
        S("talk", choose({"bring_home": None, "hear_them_out": None}), "home"),
        S("home", escort("slot:target", "place:gate.main"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("reason", 2, modifier=True), twist("rescuers", 1, harder=True, modifier=True)],
    bonus=["spared", "no_knockouts"], enemies=["missing_nin.chunin"], regions=["region:northern_forest"],
    tags=["travel", "capture", "fight", "target"],
    twist_premises={"reason": "The deserter left for a reason the council should hear.",
                    "rescuers": "Someone wants the deserter free and is willing to fight for it."}))

add(mission(
    "mission.b.kiln_glaze", "b", "recovery", minutes=40, pay=0.55, unlock=CHUNIN, chain="chain.kiln",
    premise="The kiln family's secret glaze recipe was stolen by a workshop across the border; get it back quietly.",
    client=role("role:client.kiln_parent"),
    slots={"workshop": anchor("border.workshop"), "guards": enemy_group("thug.hired")},
    steps=[
        travel("workshop"),
        S("workshop", sneak("slot:workshop"), "recipe", optional=["unseen"]),
        S("recipe", collect("glaze_recipe", at="slot:workshop"), "report",
          branch=[(twist_if("copied"), "copies")]),
        S("copies", collect("recipe_copy", at="slot:workshop", count=3), "report"),
        S("report", deliver("glaze_recipe", C), None),
    ],
    twists=[twist("copied", 2), twist("rival_is_family", 1, modifier=True)],
    bonus=["unseen", "no_alarm", "clean_record"], enemies=["thug.hired"], regions=["region:border_village"],
    tags=["travel", "stealth", "recovery", "chain"],
    twist_premises={"copied": "They have already made copies.",
                    "rival_is_family": "The rival workshop belongs to an estranged branch of the same family."}))

# --- A rank (Jonin) ----------------------------------------------------------------------------------

add(mission(
    "mission.a.border_skirmish", "a", "war", minutes=50, days=2, pay=0.5, unlock=JONIN,
    premise="An enemy platoon has crossed the border; hold the line at a river crossing until reinforcements come.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"crossing": anchor("front.crossing"), "platoon": enemy_group("enemy.platoon"), "jonin": enemy_group("enemy.jonin")},
    steps=[
        travel("dig_in"),
        S("dig_in", perform("set_trap", at="slot:crossing", count=6), "hold"),
        S("hold", survive("+12h", at="slot:crossing"), "commander", on_enter=[{"spawn_group": ["slot:platoon", "slot:crossing"]}]),
        S("commander", defeat("slot:jonin", at="slot:crossing"), "report", on_enter=[{"spawn_group": ["slot:jonin", "slot:crossing"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("flanked", 2, harder=True, modifier=True), twist("wounded_ally", 1, modifier=True)],
    bonus=["no_knockouts", "teamwork"], enemies=["enemy.platoon", "enemy.jonin"], regions=["region:front"],
    tags=["travel", "war", "defence", "fight"],
    twist_premises={"flanked": "A second squad comes around through the reeds.",
                    "wounded_ally": "An allied squad is pinned on the far bank."}))

add(mission(
    "mission.a.assassination", "a", "elimination", minutes=50, days=2, pay=0.6, unlock=JONIN,
    premise="A foreign lord's war minister plans an invasion; remove him from the board before it begins.",
    client=resident(group="council"),
    slots={"target": role("role:target.minister"), "palace": anchor("foreign.palace"), "guard": enemy_group("enemy.jonin")},
    steps=[
        travel("infiltrate"),
        S("infiltrate", sneak("slot:palace"), "strike", optional=["unseen"]),
        S("strike", defeat("slot:target", at="slot:palace"), "escape",
          branch=[(twist_if("guarded"), "guard")]),
        S("guard", defeat("slot:guard", at="slot:palace"), "escape", on_enter=[{"spawn_group": ["slot:guard", "slot:palace"]}]),
        S("escape", sneak("place:gate.travel_desk"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("guarded", 2, harder=True), twist("change_of_heart", 1, modifier=True)],
    bonus=["unseen", "no_alarm"], enemies=["enemy.jonin"], regions=["region:foreign_capital"],
    tags=["travel", "stealth", "target"],
    twist_premises={"guarded": "A Jonin bodyguard never leaves his side.",
                    "change_of_heart": "The minister offers proof he was forced into the plan."}))

add(mission(
    "mission.a.agent_extraction", "a", "extraction", minutes=50, pay=0.6, unlock=JONIN,
    premise="Bring home a Leaf agent whose cover in a foreign village has been blown.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"safehouse": anchor("foreign.safehouse"), "hunters": enemy_group("enemy.hunter_squad")},
    steps=[
        travel("contact"),
        S("contact", sneak("slot:safehouse"), "extract"),
        S("extract", escort("agent", "place:gate.travel_desk"), "report", on_enter=[{"spawn_group": ["slot:hunters", "slot:safehouse"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("agent_wounded", 2, modifier=True), twist("agent_turned", 1, harder=True, modifier=True)],
    bonus=["unseen", "client_unharmed"], enemies=["enemy.hunter_squad"], regions=["region:foreign_village"],
    tags=["travel", "stealth", "extraction"],
    twist_premises={"agent_wounded": "The agent cannot walk.",
                    "agent_turned": "The agent is not sure they want to come home."}))

add(mission(
    "mission.a.outpost_defence", "a", "defence", minutes=45, pay=0.55, unlock=JONIN,
    premise="Hold a Leaf outpost against an enemy squad until the night is over.",
    client=resident(group="shinobi", rank="jonin"),
    slots={"outpost": anchor("border.outpost"), "squad": enemy_group("enemy.squad"), "jonin": enemy_group("enemy.jonin")},
    steps=[
        travel("ready"),
        S("ready", perform("set_trap", at="slot:outpost", count=4), "hold"),
        S("hold", survive("06:00", at="slot:outpost"), "report", on_enter=[{"spawn_group": ["slot:squad", "slot:outpost"]}],
          branch=[(twist_if("their_jonin"), "jonin")]),
        S("jonin", defeat("slot:jonin", at="slot:outpost"), "report", on_enter=[{"spawn_group": ["slot:jonin", "slot:outpost"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("their_jonin", 2, harder=True), twist("fog", 1, modifier=True)],
    bonus=["no_knockouts", "teamwork"], enemies=["enemy.squad", "enemy.jonin"], regions=["region:border_village"],
    tags=["travel", "defence", "night", "fight"],
    twist_premises={"their_jonin": "Their Jonin leads the last assault himself.",
                    "fog": "A thick fog rolls in; the sensors are blind."}))

add(mission(
    "mission.a.forbidden_scroll", "a", "recovery", minutes=50, days=2, pay=0.6, unlock=JONIN,
    premise="A forbidden scroll stolen generations ago has surfaced in a ruined fortress; recover it before anyone else.",
    client=resident(group="council"),
    slots={"ruin": anchor("ruin.vault"), "rivals": enemy_group("enemy.squad"), "guardian": enemy_group("beast.great_serpent")},
    steps=[
        travel("ruin"),
        S("ruin", inspect("seal", at="slot:ruin", count=3), "vault"),
        S("vault", defeat("slot:guardian", at="slot:ruin"), "scroll", on_enter=[{"spawn_group": ["slot:guardian", "slot:ruin"]}]),
        S("scroll", collect("forbidden_scroll", at="slot:ruin"), "report",
          branch=[(twist_if("rivals"), "rivals")]),
        S("rivals", defeat("slot:rivals", at="slot:ruin"), "report", on_enter=[{"spawn_group": ["slot:rivals", "slot:ruin"]}]),
        S("report", deliver("forbidden_scroll", C), None),
    ],
    twists=[twist("rivals", 2, harder=True), twist("seal_trap", 1, modifier=True)],
    bonus=["no_knockouts", "clean_record"], enemies=["enemy.squad", "beast.great_serpent"], regions=["region:ruins"],
    tags=["travel", "recovery", "fight"],
    twist_premises={"rivals": "Another village's team arrives on the same night.",
                    "seal_trap": "The scroll's seal is a trap for anyone who breaks it."}))

add(mission(
    "mission.a.daimyo_escort", "a", "escort", minutes=50, days=3, pay=0.6, unlock=JONIN,
    premise="Escort the Fire Country's daimyo on a pilgrimage through contested land.",
    client=resident(job="daimyo", resident_of="any"),
    slots={"temple": anchor("pilgrim.temple"), "road": anchor("pilgrim.road"), "assassins": enemy_group("assassin.team")},
    steps=[
        travel("road"),
        S("road", escort(C, "slot:road"), "temple", on_enter=[{"spawn_group": ["slot:assassins", "slot:road"]}]),
        S("temple", protect(C, until="+8h", at="slot:temple"), "home"),
        S("home", escort(C, "place:gate.main"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("inside_guard", 2, modifier=True), twist("storm", 1, modifier=True)],
    bonus=["client_unharmed", "no_alarm"], enemies=["assassin.team"], regions=["region:pilgrim_road"],
    tags=["travel", "escort", "politics", "fight"],
    twist_premises={"inside_guard": "One of the daimyo's own guards is paid by the other side.",
                    "storm": "A typhoon strands the procession at the temple."}))

add(mission(
    "mission.a.cell_hunt", "a", "hunt", minutes=50, days=2, pay=0.6, unlock=JONIN,
    premise="Track an enemy cell through a far region and bring it down.",
    client=resident(group="council"),
    slots={"trail": anchor("far.trail"), "lair": anchor("far.lair"), "cell": enemy_group("enemy.cell")},
    steps=[
        travel("trail"),
        S("trail", inspect("tracks", at="slot:trail", count=5), "lair"),
        S("lair", defeat("slot:cell", at="slot:lair"), "report", on_enter=[{"spawn_group": ["slot:cell", "slot:lair"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("trap_lair", 2, harder=True, modifier=True), twist("prisoners", 1, modifier=True)],
    fast_hours=36, bonus=["no_knockouts", "fast"], enemies=["enemy.cell"], regions=["region:far_lands"],
    tags=["travel", "hunt", "fight", "tracking"],
    twist_premises={"trap_lair": "The lair is bait.", "prisoners": "They are holding travellers."}))

add(mission(
    "mission.a.siege_relief", "a", "war", minutes=55, days=3, pay=0.6, unlock=JONIN,
    premise="Break the siege of an allied castle town before its stores run out.",
    client=resident(job="envoy", resident_of="any"),
    slots={"lines": anchor("siege.lines"), "gate": anchor("siege.gate"), "army": enemy_group("enemy.platoon"),
           "general": enemy_group("enemy.jonin")},
    steps=[
        travel("scout"),
        S("scout", sneak("slot:lines"), "stores", optional=["unseen"]),
        S("stores", deliver("supply_crate", "slot:gate"), "break"),
        S("break", defeat("slot:army", at="slot:lines"), "general", on_enter=[{"spawn_group": ["slot:army", "slot:lines"]}]),
        S("general", defeat("slot:general", at="slot:lines"), "report", on_enter=[{"spawn_group": ["slot:general", "slot:lines"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("sortie", 2, modifier=True), twist("tunnel", 1, modifier=True)],
    bonus=["no_knockouts", "teamwork", "unseen"], enemies=["enemy.platoon", "enemy.jonin"], regions=["region:castle_town"],
    tags=["travel", "war", "fight"],
    twist_premises={"sortie": "The town's own soldiers want to ride out with you.",
                    "tunnel": "An old smugglers' tunnel runs under the lines."}))

add(mission(
    "mission.a.listening_post", "a", "investigation", minutes=45, pay=0.55, unlock=JONIN,
    premise="A foreign spy ring keeps a listening post somewhere in the Leaf's market district; find it and close it quietly.",
    client=resident(group="council"),
    slots={"market": anchor("market.rooftops"), "drop": anchor("village.dead_drop"), "suspect_a": resident(job="trader", resident_of="any"),
           "suspect_b": resident(job="innkeeper", resident_of="any"), "suspect_c": resident(job="porter", resident_of="any"),
           "ring": enemy_group("enemy.cell")},
    steps=[
        S("watch", inspect("signal", at="slot:market", count=4), "drop"),
        S("drop", wait_until("01:00", at="slot:drop"), "follow"),
        S("follow", sneak("slot:drop"), "accuse", optional=["unseen"]),
        S("accuse", choose({"a": None, "b": None, "c": None}), "close"),
        S("close", defeat("slot:ring", at="slot:drop"), "report", on_enter=[{"spawn_group": ["slot:ring", "slot:drop"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("post_a", 1, modifier=True), twist("post_b", 1, modifier=True), twist("post_c", 1, modifier=True)],
    bonus=["unseen", "no_alarm", "spared"], enemies=["enemy.cell"], tags=["village", "investigation", "stealth"],
    twist_premises={"post_a": "The rolled listening post is the first suspect's.", "post_b": "The second's.", "post_c": "The third's."}))

add(mission(
    "mission.a.kiln_court", "a", "bodyguard", minutes=45, days=2, pay=0.55, unlock=JONIN, chain="chain.kiln",
    premise="The kiln family's eldest is named court potter; guard them through a court that does not want a commoner there.",
    client=role("role:client.kiln_heir"),
    slots={"court": anchor("capital.court"), "assassins": enemy_group("assassin.team")},
    steps=[
        travel("court"),
        S("court", protect(C, until="+12h", at="slot:court"), "report", on_enter=[{"spawn_group": ["slot:assassins", "slot:court"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("sabotaged_kiln", 2, modifier=True), twist("noble_ally", 1, modifier=True)],
    bonus=["client_unharmed", "no_alarm"], enemies=["assassin.team"], regions=["region:capital"],
    tags=["travel", "guard", "politics", "chain"],
    twist_premises={"sabotaged_kiln": "Someone has cracked the court kiln before the first firing.",
                    "noble_ally": "One noble quietly offers help."}))

# --- S rank -----------------------------------------------------------------------------------------------

add(mission(
    "mission.s.rogue_legend", "s", "elimination", minutes=60, days=3, pay=0.5, unlock=S_RANK,
    premise="A missing-nin of legendary strength has surfaced near the border; stop them.",
    client=resident(group="council"),
    slots={"target": role("role:target.legend"), "arena": anchor("far.battlefield")},
    steps=[
        travel("find"),
        S("find", inspect("destruction", at="slot:arena", count=3), "fight"),
        S("fight", defeat("slot:target", at="slot:arena"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("second_phase", 2, harder=True, modifier=True), twist("parley", 1, modifier=True)],
    bonus=["no_knockouts", "teamwork"], enemies=["missing_nin.legend"], regions=["region:far_lands"],
    tags=["travel", "fight", "target", "boss"],
    twist_premises={"second_phase": "They were holding back.", "parley": "They ask to talk first."}))

add(mission(
    "mission.s.coup", "s", "protection", minutes=60, days=2, pay=0.6, unlock=S_RANK,
    premise="A coup is planned against the Fire Country's daimyo during a festival at the capital.",
    client=resident(job="daimyo", resident_of="any"),
    slots={"palace": anchor("capital.palace"), "plotters": enemy_group("assassin.team", "enemy.jonin")},
    steps=[
        travel("intel"),
        S("intel", inspect("plotter_sign", at="slot:palace", count=4), "night"),
        S("night", protect(C, until="06:00", at="slot:palace"), "report", on_enter=[{"spawn_group": ["slot:plotters", "slot:palace"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("council_involved", 2, modifier=True), twist("fire", 1, harder=True, modifier=True)],
    bonus=["client_unharmed", "no_alarm", "unseen"], enemies=["assassin.team", "enemy.jonin"], regions=["region:capital"],
    tags=["travel", "politics", "defence", "fight"],
    twist_premises={"council_involved": "A minister of the court is behind it.",
                    "fire": "They set the palace alight as a distraction."}))

add(mission(
    "mission.s.stronghold", "s", "infiltration", minutes=60, days=3, pay=0.6, unlock=S_RANK,
    premise="Retrieve a stolen forbidden technique from a foreign stronghold no one has left alive.",
    client=resident(group="council"),
    slots={"stronghold": anchor("foreign.stronghold"), "vault": anchor("foreign.vault"), "guard": enemy_group("enemy.jonin")},
    steps=[
        travel("in"),
        S("in", sneak("slot:stronghold"), "vault", optional=["unseen"]),
        S("vault", collect("forbidden_scroll", at="slot:vault"), "out"),
        S("out", sneak("place:gate.travel_desk"), "report",
          branch=[(twist_if("sealed_in"), "fight")]),
        S("fight", defeat("slot:guard", at="slot:stronghold"), "report", on_enter=[{"spawn_group": ["slot:guard", "slot:stronghold"]}]),
        S("report", deliver("forbidden_scroll", C), None),
    ],
    twists=[twist("sealed_in", 2, harder=True), twist("inside_help", 1, modifier=True)],
    bonus=["unseen", "no_alarm", "no_knockouts"], enemies=["enemy.jonin"], regions=["region:foreign_stronghold"],
    tags=["travel", "stealth", "infiltration"],
    twist_premises={"sealed_in": "The stronghold seals itself when the vault opens.",
                    "inside_help": "A prisoner inside has been waiting years for someone like you."}))

add(mission(
    "mission.s.peace_summit", "s", "protection", minutes=60, days=3, pay=0.6, unlock=S_RANK,
    premise="Guard the five lands' peace summit; three sides would like it to fail.",
    client=resident(group="council"),
    slots={"hall": anchor("summit.hall"), "spoilers": enemy_group("assassin.team", "enemy.cell")},
    steps=[
        travel("sweep"),
        S("sweep", inspect("trap", at="slot:hall", count=5), "summit"),
        S("summit", protect("delegates", until="+12h", at="slot:hall"), "report", on_enter=[{"spawn_group": ["slot:spoilers", "slot:hall"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("delegate_plot", 2, modifier=True), twist("walkout", 1, modifier=True)],
    bonus=["client_unharmed", "no_alarm"], enemies=["assassin.team", "enemy.cell"], regions=["region:summit"],
    tags=["travel", "politics", "guard"],
    twist_premises={"delegate_plot": "One of the delegates hired the assassins.",
                    "walkout": "A delegation storms out; talk them back in."}))

# --- ANBU operations (the optional branch) ----------------------------------------------------------------

add(mission(
    "mission.anbu.night_watch", "b", "anbu", minutes=35, pay=0.6, unlock=ANBU, party="anbu_cell",
    premise="Watch a house in the Leaf from the rooftops for three nights and report everyone who comes and goes.",
    client=resident(group="anbu"),
    slots={"house": anchor("village.rooftop_watch"), "visitor": resident()},
    steps=[
        S("n1", wait_until("04:00", at="slot:house"), "n2"),
        S("n2", wait_until("04:00", at="slot:house"), "n3"),
        S("n3", inspect("visitor", at="slot:house", count=3), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("spotted", 2, harder=True, modifier=True), twist("innocent", 1, modifier=True)],
    bonus=["unseen"], tags=["village", "anbu", "stealth", "night"],
    twist_premises={"spotted": "A child in the house sees your mask on the second night.",
                    "innocent": "It is a love affair, not a conspiracy."}))

add(mission(
    "mission.anbu.silent_extraction", "a", "anbu", minutes=50, pay=0.6, unlock=ANBU, party="anbu_cell",
    premise="Take a prisoner out of an enemy camp without anyone knowing the Leaf was there.",
    client=resident(group="anbu"),
    slots={"camp": anchor("far.camp"), "guards": enemy_group("enemy.squad")},
    steps=[
        travel("in"),
        S("in", sneak("slot:camp"), "take"),
        S("take", escort("prisoner", "place:gate.travel_desk"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("drugged", 2, modifier=True), twist("trap", 1, harder=True, modifier=True)],
    bonus=["unseen", "no_alarm"], enemies=["enemy.squad"], regions=["region:far_lands"], tags=["travel", "anbu", "stealth"],
    twist_premises={"drugged": "The prisoner is drugged and must be carried.",
                    "trap": "The prisoner is bait."}))

add(mission(
    "mission.anbu.corrupt_official", "a", "anbu", minutes=45, pay=0.6, unlock=ANBU, party="anbu_cell",
    premise="Gather proof against an official of the daimyo's court who sells border passes.",
    client=resident(group="anbu"),
    slots={"office": anchor("capital.office"), "official": role("role:target.official")},
    steps=[
        travel("office"),
        S("office", sneak("slot:office"), "proof"),
        S("proof", collect("pass_ledger", at="slot:office"), "decide"),
        S("decide", choose({"expose": None, "leverage": "kept_leverage"}), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("blackmailed", 2, modifier=True), twist("rival_agent", 1, modifier=True)],
    outcomes={"done": outcome(), "kept_leverage": outcome(pay=1.0, extra={"flag": "anbu.leverage"})},
    bonus=["unseen", "no_alarm"], regions=["region:capital"], tags=["travel", "anbu", "stealth", "politics"],
    twist_premises={"blackmailed": "The official is being blackmailed into it.",
                    "rival_agent": "Another land's agent is after the same ledger."}))

add(mission(
    "mission.anbu.hunter_nin", "a", "anbu", minutes=50, days=2, pay=0.6, unlock=ANBU, party="anbu_cell",
    premise="Hunt a missing-nin who carries the Leaf's secrets in their head, before another village catches them.",
    client=resident(group="anbu"),
    slots={"target": role("role:target.missing_nin"), "trail": anchor("far.trail")},
    steps=[
        travel("trail"),
        S("trail", inspect("tracks", at="slot:trail", count=5), "fight"),
        S("fight", defeat("slot:target", at="slot:trail"), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("other_hunters", 2, harder=True, modifier=True), twist("plea", 1, modifier=True)],
    fast_hours=36, bonus=["fast", "unseen"], enemies=["missing_nin.jonin"], regions=["region:far_lands"],
    tags=["travel", "anbu", "hunt", "target"],
    twist_premises={"other_hunters": "Another village's hunters got there first.",
                    "plea": "The target begs to be taken home instead."}))

add(mission(
    "mission.anbu.deep_cover", "s", "anbu", minutes=60, days=5, pay=0.6, unlock=ANBU, party="solo",
    premise="Live under a false name in a foreign town for five days and learn what its lord is building.",
    client=resident(group="anbu"),
    slots={"town": anchor("foreign.town"), "works": anchor("foreign.works")},
    steps=[
        travel("settle"),
        S("settle", perform("transformation_hold", at="slot:town", count=3), "learn"),
        S("learn", inspect("works", at="slot:works", count=4), "report"),
        S("report", talk(C), None),
    ],
    twists=[twist("friend_made", 2, modifier=True), twist("cover_blown", 1, harder=True, modifier=True)],
    bonus=["unseen", "no_alarm"], regions=["region:foreign_town"], tags=["travel", "anbu", "stealth", "talk"],
    twist_premises={"friend_made": "Someone in the town becomes a real friend to your false self.",
                    "cover_blown": "A visitor from the Leaf recognises you on the street."}))

add(mission(
    "mission.anbu.village_shadow", "s", "anbu", minutes=60, pay=0.6, unlock=ANBU, party="anbu_cell",
    premise="On the night of a great festival, guard the Leaf from the rooftops against what the festival hides.",
    client=resident(group="anbu"),
    slots={"roofs": anchor("village.rooftop_watch"), "intruders": enemy_group("enemy.cell")},
    event={"during": "event.leaf_festival"},
    steps=[
        S("post", go("slot:roofs"), "watch"),
        S("watch", survive("02:00", at="slot:roofs"), "report", on_enter=[{"spawn_group": ["slot:intruders", "slot:roofs"]}]),
        S("report", talk(C), None),
    ],
    twists=[twist("quiet_night", 1, modifier=True), twist("two_cells", 2, harder=True, modifier=True)],
    bonus=["no_alarm", "unseen"], enemies=["enemy.cell"], tags=["village", "anbu", "night", "defence"],
    twist_premises={"quiet_night": "Nothing comes, and you watch the fireworks alone.",
                    "two_cells": "Two cells come from opposite sides of the village."}))
