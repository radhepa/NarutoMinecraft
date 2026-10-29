"""Combination play: nature combos between allies, squad combo techniques, team commands,
formations and cohesion bonuses (BONDS.md section 7), plus PvP rules for later multiplayer."""

NATURE_COMBOS = [
    {"id": "combat:combo.firestorm", "natures": ["wind", "fire"], "name": "Firestorm", "slice": "beta2",
     "how": "A fire jutsu passing through an ally's wind gust (within 20 ticks) grows: x1.5 power, x1.5 radius, burning doubled",
     "player_role": "either side"},
    {"id": "combat:combo.storm_surge", "natures": ["water", "lightning"], "name": "Storm Surge", "slice": "beta2",
     "how": "Lightning into soaked targets or a water jutsu's area: shocks everyone in it (stun 10 ticks, chains 4)"},
    {"id": "combat:combo.lava_bullets", "natures": ["earth", "fire"], "name": "Lava Bullets", "slice": "chunin",
     "how": "Fire through Earth Dragon Bullet's mud: lava bullets (x1.4, burning)"},
    {"id": "combat:combo.mudslide", "natures": ["earth", "water"], "name": "Mudslide", "slice": "chunin",
     "how": "Water over Mud River: twice as long, enemies stuck (bound 30)"},
    {"id": "combat:combo.gale_rain", "natures": ["wind", "water"], "name": "Gale Rain", "slice": "chunin",
     "how": "Wind through a water wave: needles of rain at long range (x1.3, soaked, chilled)"},
    {"id": "combat:combo.thunder_gust", "natures": ["wind", "lightning"], "name": "Thunder Gust", "slice": "jonin",
     "how": "Even natures that oppose each other combine with timing: a perfect-timed (5 ticks) lightning through wind spreads into a 6-block arc"},
    {"id": "combat:combo.magma_wall", "natures": ["earth", "fire"], "name": "Magma Wall", "slice": "jonin",
     "how": "Fire into an earth wall: the wall glows and burns anyone touching it"},
]

SQUAD_COMBOS = [
    {"id": "combat:squad.launcher_relay", "name": "Launcher relay", "slice": "beta2", "needs": "any two squadmates",
     "how": "A teammate's launcher sends the target up; your jump within 20 ticks starts an air combo with +1 hit and x1.2 damage"},
    {"id": "combat:squad.clone_feint", "name": "Clone feint", "slice": "beta2", "needs": "Clone Technique",
     "how": "Your clones run in; the enemy turns to them; your teammate's next hit from behind is a crit"},
    {"id": "combat:squad.bomb_line", "name": "Bomb line", "slice": "beta2", "needs": "wire and paper bombs",
     "how": "A teammate strings wire, you tag it: the tripwire bursts along its length"},
    {"id": "combat:squad.pincer", "name": "Pincer", "slice": "beta2", "needs": "the Pincer formation",
     "how": "Two squadmates on opposite sides of a target: both get +20% damage and the target cannot guard both"},
    {"id": "combat:squad.bell_grab", "name": "Distract and take", "slice": "beta2", "needs": "the cord test's lesson",
     "how": "One distracts (any hit), the other takes: a stagger window of 30 ticks on the target. Taught by the cord test"},
    {"id": "combat:squad.shadow_and_strike", "name": "Shadow and strike", "slice": "beta2", "needs": "a Nara in the squad",
     "how": "While a target is possessed, every squadmate's hit is a crit"},
    {"id": "combat:squad.fang_and_swarm", "name": "Fang and swarm", "slice": "beta2", "needs": "an Inuzuka and an Aburame",
     "how": "Fang over Fang homes on a target marked by insects; insects slow anyone the fang knocks down"},
    {"id": "combat:squad.triad", "name": "The triad formation", "slice": "chunin", "needs": "a Nara, an Akimichi and a Yamanaka",
     "how": "Possession, then Mind Body Disturbance, then a Human Boulder: a three-step squad finisher (cinematic)"},
    {"id": "combat:squad.barrier_and_fire", "name": "Barrier and fire", "slice": "chunin", "needs": "a four-tag barrier",
     "how": "Fire jutsu cast inside your own barrier fill it: x2 burning for everyone trapped"},
    {"id": "combat:squad.cover_fire", "name": "Cover fire", "slice": "beta2", "needs": "a thrower and a close fighter",
     "how": "Thrown weapons at a target your teammate is fighting interrupt its guard (poise x1.5)"},
    {"id": "combat:squad.final_watch", "name": "Squad finisher", "slice": "chunin", "needs": "cohesion 80",
     "how": "With full momentum on two squadmates: each does their style's finisher on the same target in turn (cinematic)"},
]

COMMANDS = {
    "key": "hold Command (H) for a wheel, or tap for the last command; a teammate's name token shows who answers",
    "list": [
        {"id": "attack", "what": "attack my target (the crosshair or lock-on)"},
        {"id": "defend", "what": "stay near me and intercept"},
        {"id": "follow", "what": "follow me, fight only what attacks us"},
        {"id": "hold", "what": "hold this spot"},
        {"id": "spread", "what": "spread out (against area jutsu)"},
        {"id": "regroup", "what": "come back to me now"},
        {"id": "combo", "what": "start a squad or nature combo on my target (picks one you can do)"},
        {"id": "retreat", "what": "fall back and heal"},
        {"id": "heal", "what": "the medic heals the most hurt"},
    ],
    "response": "a command is obeyed after 4 ticks at cohesion 60+, 10 ticks at 30 to 59, 16 ticks under 30; under 30 a teammate ignores 1 in 10 (except Umino's Steady Voice)",
    "slice": "beta2 (Ch 8, the cord test)",
}

FORMATIONS = [
    {"id": "line", "what": "side by side, facing the threat: guard +10% for all", "slice": "beta2"},
    {"id": "arrowhead", "what": "a wedge with you at the front: your dash attacks +15%; teammates follow your target", "slice": "beta2"},
    {"id": "ring", "what": "back to back around a protect target: no back attacks on anyone", "slice": "beta3"},
    {"id": "pincer", "what": "split around the target (opens the pincer squad combo)", "slice": "beta2"},
    {"id": "hidden", "what": "spread in cover, silent: first strikes are crits (stealth objectives)", "slice": "beta3"},
]

COHESION = {
    "source": "BONDS.md section 7: the squad's cohesion (0 to 100) from Shinobi Life (squad_cohesion)",
    "bands": [
        {"from": 0, "to": 29, "effects": {"command_delay_ticks": 16, "ignore_chance": 0.1, "combo_damage": -0.1}},
        {"from": 30, "to": 59, "effects": {"command_delay_ticks": 10}},
        {"from": 60, "to": 79, "effects": {"command_delay_ticks": 4, "combo_damage": 0.1, "nature_combo_window_bonus_ticks": 10}},
        {"from": 80, "to": 100, "effects": {"command_delay_ticks": 4, "combo_damage": 0.2, "squad_finisher": True,
                                              "cover": "once per fight a teammate intercepts a hit that would down you"}},
    ],
    "friendship": "a teammate at friendship 6+ joins nature combos with you without a command; at 8+ they call combos themselves (bark: combo_call)",
    "experiences": "every squad combo landed is a shared experience for the bond engine (kind: spar or mission)",
}

TEAMMATE_AI = {
    "roles": "Progression's squad roles drive the AI: vanguard (close), support (mid, throws and jutsu), sensor (far, reveals), medic (heals)",
    "loadouts": "teammates have loadout files like enemies (combat:ally.<role id>), growing with the story",
    "never_killed": "squadmates are knocked out, never killed (ROADMAP); downed teammates can be revived",
    "friendly_fire": "off for direct hits; area jutsu push allies but never hurt them (Hard: 25% damage)",
}

PVP = {
    "status": "later (multiplayer after the single-player story)",
    "rules": [
        "Level and gear normalised to a chosen band (default: everyone at level 30, ranks equalised)",
        "Shinobi difficulty timings, no aim assist, no habit adaptation",
        "Diminishing returns on stun, bind, seal and mind: second within 15 s at half, third at a quarter, then immune",
        "Genjutsu on a player: a screen effect for at most 3 s and never control of the camera; Mind Transfer cannot target players",
        "Substitution: once per 25 s; Palm Rotation and barriers have a 10 s cooldown in PvP",
        "S-rank jutsu disabled by default (a server rule can allow them)",
        "Lag compensation: 2 ticks; hits are confirmed by the server sweep",
        "Duels by invitation (/shinobi duel <player>) to 30% health; squad battles 3v3 in arenas; no PvP in the village outside arenas",
    ],
}
