package dev.shinobi.life.bond;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * A sample question bank in the dialogue data's format, for tests and the simulation: a few of each kind, at several
 * levels and depths, with follow-ups, public opinions and a cast-only question. The real bank is the dialogue
 * session's; these show the shape and give the pacing check something to ask.
 */
public final class SampleQuestions {
    static Map<String, Object> a(String id, String stance, String... tags) { return Map.of("id", id, "stance", stance, "tags", List.of(tags)); }
    static Map<String, Object> a(String id, String stance, Map<String, Object> extra, String... tags) {
        var m = new java.util.HashMap<String, Object>(Map.of("id", id, "stance", stance, "tags", List.of(tags)));
        m.putAll(extra);
        return m;
    }
    static Map<String, Object> q(String id, String kind, int level, int depth, String about, boolean pub, List<Map<String, Object>> answers) {
        return q(id, kind, level, depth, about, pub, answers, "", 0, Map.of());
    }
    static Map<String, Object> q(String id, String kind, int level, int depth, String about, boolean pub, List<Map<String, Object>> answers,
            String followUpOf, int gap, Map<String, Object> audience) {
        var m = new java.util.HashMap<String, Object>();
        m.put("format", 1); m.put("id", id); m.put("kind", kind); m.put("level", level); m.put("depth", depth); m.put("about", about);
        m.put("public", pub); m.put("answers", answers); m.put("follow_up_of", followUpOf); m.put("min_gap_days", gap); m.put("audience", audience);
        return m;
    }

    public static List<Map<String, Object>> raw() {
        var list = new ArrayList<Map<String, Object>>();
        // Preferences: light, early.
        list.add(q("q.pref.ramen_or_dango", "preference", 1, 1, "pref:food", false, List.of(a("ramen", "ramen", "playful"), a("dango", "dango", "kind"), a("either", "either", "humble"))));
        list.add(q("q.pref.morning_or_night", "preference", 1, 1, "pref:time", false, List.of(a("dawn", "dawn", "dutiful"), a("night", "night", "free"))));
        list.add(q("q.pref.rain", "preference", 2, 1, "pref:weather", false, List.of(a("love_it", "rain", "curious"), a("hate_it", "sun", "blunt"), a("training_weather", "rain", "ambitious"))));
        list.add(q("q.pref.festival_game", "preference", 2, 1, "pref:games", false, List.of(a("goldfish", "goldfish", "playful"), a("targets", "targets", "ambitious", "bold"))));
        // Opinions: some about the village, which travel.
        list.add(q("q.opinion.instructor", "opinion", 2, 1, "person:role:instructor", true, List.of(a("great", "likes", "kind", "loyal"), a("strict", "dislikes", "blunt"), a("dont_know", "neutral", "evasive"))));
        list.add(q("q.opinion.uchiha", "opinion", 3, 1, "clan:uchiha", true, List.of(a("respect_them", "respects", "humble", "kind"),
                a("stuck_up", "dislikes", Map.of("deed", "insulted_clan"), "rude", "blunt"), a("never_met", "neutral", "honest"))));
        list.add(q("q.opinion.hokage_rock", "opinion", 3, 1, "plan:hokage", false, List.of(a("my_face_there", "hokage", "ambitious", "bold"), a("not_for_me", "not_hokage", "humble"), a("joke", "joke", "playful"))));
        list.add(q("q.opinion.rules", "opinion", 4, 2, "value:rules", false, List.of(a("rules_keep_us_alive", "rules", "dutiful"), a("rules_are_guides", "free", "free", "honest"))));
        list.add(q("q.opinion.clans_vs_clanless", "opinion", 5, 2, "value:blood", true, List.of(a("blood_doesnt_matter", "merit", "kind", "honest"),
                a("clans_keep_traditions", "tradition", "loyal", "dutiful"), a("whatever", "neutral", "evasive"))));
        // Dilemmas: values in conflict.
        list.add(q("q.dilemma.found_wallet", "dilemma", 3, 1, "value:honesty", false, List.of(a("return_it", "honest", "honest", "kind"), a("keep_it", "self", "ambitious", "blunt"),
                a("give_to_guard", "honest", "dutiful"))));
        list.add(q("q.dilemma.friend_cheats", "dilemma", 4, 1, "value:honesty", false, List.of(a("tell_teacher", "honest", "dutiful", "honest"),
                a("talk_to_friend", "honest", "loyal", "kind"), a("let_it_go", "self", "loyal", "evasive"))));
        list.add(q("q.dilemma.orders_or_friend", "dilemma", 6, 2, "value:duty", false, List.of(a("orders", "duty", "dutiful", "cautious"),
                a("friend", "loyalty", Map.of("sets", "growth.chose_friends"), "loyal", "bold"), a("find_a_third_way", "both", "curious", "bold"))));
        list.add(q("q.dilemma.save_one", "dilemma", 8, 3, "value:duty", false, List.of(a("the_mission", "duty", "dutiful", "blunt"), a("the_person", "loyalty", "loyal", "kind"))));
        // Advice they ask for: it can shape them.
        list.add(q("q.advice.first_mission", "advice", 2, 1, "advice:nerves", false, List.of(
                a("be_careful", "careful", Map.of("nudge", Map.of("trait", "boldness", "amount", -0.05)), "cautious", "kind"),
                a("go_for_it", "bold", Map.of("nudge", Map.of("trait", "boldness", "amount", 0.05)), "bold", "ambitious"),
                a("stick_together", "together", "loyal"))));
        list.add(q("q.advice.first_mission.after", "advice", 3, 1, "advice:nerves", false, List.of(a("you_did_well", "praise", "kind"), a("next_time_better", "push", "blunt", "ambitious")),
                "q.advice.first_mission", 5, Map.of()));
        list.add(q("q.advice.quit_or_not", "advice", 5, 2, "advice:persevere", false, List.of(
                a("keep_going", "persevere", Map.of("sets", "growth.kept_going", "nudge", Map.of("trait", "discipline", "amount", 0.08)), "ambitious", "kind"),
                a("rest_a_while", "rest", "kind", "cautious"), a("do_what_you_love", "free", Map.of("sets", "growth.followed_heart"), "free", "honest"))));
        list.add(q("q.advice.apologize", "advice", 4, 1, "advice:pride", false, List.of(a("say_sorry", "humble", "humble", "honest"), a("let_them_come", "proud", "proud"))));
        list.add(q("q.advice.family_expectations", "advice", 6, 2, "advice:family", false, List.of(a("talk_to_them", "honest", "honest", "family"), a("your_life", "free", "free", "bold"),
                a("make_them_proud", "duty", "dutiful", "family")), "", 0, Map.of("values", List.of("family"))));
        // About the player.
        list.add(q("q.past.before_the_leaf", "player_past", 3, 1, "past:origin", false, List.of(a("tell_them", "open", "honest"), a("dont_remember", "closed", "evasive"), a("joke_it_off", "closed", "playful"))));
        list.add(q("q.past.before_the_leaf.deeper", "player_past", 6, 2, "past:origin", false, List.of(a("the_whole_story", "open", "honest", "loyal"), a("not_yet", "closed", "cautious")),
                "q.past.before_the_leaf", 10, Map.of()));
        list.add(q("q.past.scariest_moment", "player_past", 5, 2, "past:fear", false, List.of(a("admit_it", "open", "honest", "humble"), a("never_scared", "brave", "proud", "bold"))));
        list.add(q("q.plans.after_academy", "player_plans", 1, 1, "plan:career", false, List.of(a("strongest_ninja", "power", "ambitious", "bold"), a("protect_everyone", "protect", "kind", "loyal"),
                a("no_idea", "unsure", "honest"))));
        list.add(q("q.plans.ten_years", "player_plans", 6, 2, "plan:career", false, List.of(a("hokage", "power", "ambitious"), a("with_my_friends", "protect", "loyal", "kind"), a("a_quiet_life", "quiet", "free"))));
        list.add(q("q.plans.family", "player_plans", 7, 3, "plan:family", false, List.of(a("someday", "family", "family", "honest"), a("the_village_is_my_family", "village", "loyal")),
                "", 0, Map.of("min_stage", "teen")));
        // Their small confessions.
        list.add(q("q.confess.afraid_of_heights", "confession", 3, 1, "", false, List.of(a("me_too", "", "honest", "kind"), a("tease", "", "playful", "rude"), a("ill_help", "", "loyal", "kind"))));
        list.add(q("q.confess.failed_test", "confession", 4, 1, "", false, List.of(a("happens", "", "kind"), a("study_with_me", "", "loyal", "dutiful"), a("you_should_have_studied", "", "blunt"))));
        list.add(q("q.confess.lonely", "confession", 6, 2, "", false, List.of(a("youre_not_alone", "", "kind", "loyal"), a("me_too_sometimes", "", "honest", "humble"), a("change_subject", "", "evasive"))));
        list.add(q("q.confess.jealous", "confession", 7, 3, "", false, List.of(a("thank_you_for_telling_me", "", "honest", "kind"), a("nothing_to_be_jealous_of", "", "humble"), a("get_over_it", "", "blunt", "rude"))));
        // Personality-specific.
        list.add(q("q.pref.paint_me", "preference", 3, 1, "", false, List.of(a("yes_please", "", "kind", "curious"), a("im_shy", "", "humble")), "", 0, Map.of("archetypes", List.of("shy", "imaginative"))));
        list.add(q("q.opinion.strength", "opinion", 3, 1, "value:strength", false, List.of(a("strength_is_everything", "strength", "ambitious", "proud"), a("strength_is_for_others", "kindness", "kind")),
                "", 0, Map.of("values", List.of("strength"))));
        list.add(q("q.dilemma.bend_the_rules", "dilemma", 4, 1, "value:rules", false, List.of(a("never", "rules", "dutiful"), a("for_a_friend", "free", "loyal", "free")), "", 0,
                Map.of("archetypes", List.of("stern", "meticulous", "steadfast"))));
        // One for a particular role (the story's briefs add these per character).
        list.add(q("q.role.sensei.why_shinobi", "player_plans", 4, 2, "plan:career", false, List.of(a("to_protect", "protect", "loyal", "dutiful"), a("to_be_strong", "power", "ambitious")),
                "", 0, Map.of("roles", List.of("role:sensei"))));
        return list;
    }
    public static List<Question> bank() { return raw().stream().map(Question::parse).toList(); }
    private SampleQuestions() {}
}
