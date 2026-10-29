"""Combat barks: the events combat fires and the speaker kinds. The dialogue session owns the pools and
the lines (VF's dialogue format, name tokens only); combat only picks a key."""

SPEAKERS = ["player_ally", "rival", "bandit", "rogue", "cell", "exam_genin", "spar_partner", "resident_bystander", "beast_none"]

EVENTS = ["fight_start", "taunt", "low_health", "ally_down", "knocked_out", "yield", "surrender", "flee", "victory", "defeat",
          "parry_landed", "got_parried", "combo_finisher_landed", "jutsu_cast", "jutsu_countered", "genjutsu_caught", "genjutsu_broken",
          "smoke_bomb", "substitution", "command_ack", "combo_call", "nature_combo", "heal_given"]

HABIT_TIPS = ["spam_same_jutsu", "never_guards", "never_dodges", "out_of_chakra", "too_far", "too_close", "ignores_tells", "good_parry_streak"]

BARKS = {
    "owner": "the dialogue session (pools and lines); combat fires the keys",
    "key": "dlg:combat.<event>.<speaker>",
    "boss_key": "dlg:combat.boss.<boss id>.phase_<n> and dlg:combat.boss.<boss id>.<event>",
    "sensei_tip": "dlg:combat.sensei_tip.<habit>",
    "tokens": "{technique} (the technique's name key), {name:<role>}, {given:<role>}, {player}",
    "rate": "at most one bark per speaker every 6 s and three per fight per speaker kind; never during a finisher cinematic",
    "speakers": SPEAKERS,
    "events": EVENTS,
    "habit_tips": HABIT_TIPS,
}
