package dev.shinobi.progression.mission;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * A sample Leaf for tests and the simulation: about 300 residents by the population weights (about 45% civilians,
 * 28% clanless shinobi, the rest clan members), with every job, age and household the templates ask for, plus
 * travellers for far regions; anchors for every tag the catalogue names (several for common tags, one for a named
 * place); and the save's bound roles. Built from the seed, so it is the same village every time.
 */
public final class SampleVillage implements World {
    static final String[] DISTRICTS = {"market", "residential", "riverside", "academy", "gate", "clans", "hospital"};
    static final String[] CLANS = {"uchiha", "hyuga", "nara", "akimichi", "yamanaka", "inuzuka", "aburame", "sarutobi",
            "shimura", "yuhi", "gekko", "senju", "uzumaki", "kurama", "hatake", "shiranui", "morino", "umino", "haruno",
            "namiashi", "hagane", "kinoshita", "tsuchigumo", "suzuran", "tobari"};
    static final String[] CIVILIAN_JOBS = {"farmer", "shopkeeper", "porter", "stallholder", "cook", "fisher", "washer",
            "clerk", "groundskeeper", "lamplighter", "organiser", "bath_keeper", "priest", "florist", "apprentice",
            "builder", "innkeeper", "trader", "medic", "teacher", "vet", "guard", "scholar"};
    static final String[] TRAVELLER_JOBS = {"trader", "scholar", "noble_guest", "innkeeper", "headman", "magistrate",
            "envoy", "daimyo", "priest", "builder"};

    final List<Resident> residents = new ArrayList<>();
    final Map<String, List<String>> anchors = new HashMap<>();
    final Map<String, String> roles = new HashMap<>();
    final List<String> squad = new ArrayList<>();

    public SampleVillage(long seed, Catalogue cat) {
        var rng = Seeds.stream(seed, "sample_village", "residents");
        int n = 0;
        for (int i = 0; i < 300; i++) {
            double g = rng.unit();
            String id = "resident:" + (n++);
            String district = DISTRICTS[rng.below(DISTRICTS.length)];
            String age = rng.chance(0.18) ? "child" : rng.chance(0.15) ? "elder" : "adult";
            boolean pet = rng.chance(0.25), household = rng.chance(0.7), kids = household && age.equals("adult") && rng.chance(0.4);
            if (g < 0.45) {
                String job = age.equals("child") ? "pupil" : CIVILIAN_JOBS[rng.below(CIVILIAN_JOBS.length)];
                residents.add(new Resident(id, job, district, age, "civilian", "", "civilian", pet, household, kids, false, null));
            } else {
                String clan = g < 0.73 ? "" : CLANS[rng.below(CLANS.length)];
                String rank = age.equals("child") ? (rng.chance(0.5) ? "academy" : "genin") : rng.chance(0.5) ? "chunin" : rng.chance(0.5) ? "genin" : "jonin";
                String job = age.equals("child") ? "pupil" : rng.chance(0.3) ? CIVILIAN_JOBS[rng.below(CIVILIAN_JOBS.length)] : "shinobi";
                residents.add(new Resident(id, job, district, age, "shinobi", clan, rank, pet, household, kids, false, null));
            }
        }
        // Every child has a parent among the adults (VF households), most in the same district.
        for (int c = 0; c < residents.size(); c++) {
            Resident child = residents.get(c);
            if (!child.age().equals("child")) continue;
            for (int tries = 0; tries < 40; tries++) {
                int k = rng.below(residents.size());
                Resident a = residents.get(k);
                if (!a.age().equals("adult") || a.parentOf() != null) continue;
                residents.set(k, new Resident(a.id(), a.job(), a.district(), a.age(), a.group(), a.clan(), a.rank(), a.hasPet(),
                        true, true, false, child.id()));
                break;
            }
        }
        // Every clan and job at least twice, and parents for some Academy pupils.
        for (String clan : CLANS) for (int k = 0; k < 2; k++)
            residents.add(new Resident("resident:" + (n++), k == 0 ? "shinobi" : clan.equals("yamanaka") ? "florist" : "shopkeeper",
                    "clans", "adult", "shinobi", clan, "chunin", false, true, false, false, null));
        for (String job : CIVILIAN_JOBS) for (int k = 0; k < 2; k++)
            residents.add(new Resident("resident:" + (n++), job, DISTRICTS[k % DISTRICTS.length], "adult", "civilian", "", "civilian",
                    k == 0, true, k == 0, false, null));
        for (int k = 0; k < 8; k++) {
            String child = "resident:" + (n++);
            residents.add(new Resident(child, "pupil", "academy", "child", "civilian", "", "academy", false, true, false, false, null));
            residents.add(new Resident("resident:" + (n++), "farmer", "residential", "adult", "civilian", "", "civilian", false, true, true, false, child));
        }
        for (String grp : List.of("council", "anbu")) for (int k = 0; k < 3; k++)
            residents.add(new Resident("resident:" + (n++), grp, "residence", "adult", grp, "", "jonin", false, true, false, false, null));
        for (int k = 0; k < 4; k++)
            residents.add(new Resident("resident:" + (n++), "shinobi", "gate", "adult", "shinobi", "", "jonin", false, true, false, false, null));
        for (String job : TRAVELLER_JOBS) for (int k = 0; k < 3; k++)
            residents.add(new Resident("traveller:" + (n++), job, "far", "adult", "civilian", "", "civilian", false, false, false, true, null));
        for (int k = 0; k < 6; k++)
            residents.add(new Resident("traveller:" + (n++), "traveller", "far", "adult", "civilian", "", "civilian", false, false, false, true, null));

        Set<String> tags = new LinkedHashSet<>();
        for (Template t : cat.all()) {
            for (var slot : t.slots().values()) if ("anchor".equals(slot.get("pick"))) tags.add((String) slot.get("tag"));
            tags.addAll(t.anchors());
        }
        for (String tag : tags) {
            boolean named = tag.contains(".");
            int count = named ? 1 : 6;
            var list = new ArrayList<String>();
            for (int k = 0; k < count; k++) list.add("anchor:" + tag + (count > 1 ? "." + k : ""));
            anchors.put(tag, list);
        }
        for (String r : List.of("role:merchant", "role:client.kiln_grandmother", "role:client.kiln_parent", "role:client.kiln_heir",
                "role:rival_squad", "role:npc_genin_squad", "role:target.warlord", "role:target.minister", "role:target.deserter",
                "role:target.legend", "role:target.official", "role:target.missing_nin"))
            roles.put(r, r.replace("role:", "cast:"));
        squad.addAll(List.of("resident:0", "resident:1", "resident:2"));
    }

    @Override public List<Resident> residents() { return residents; }
    @Override public List<String> anchors(String tag) { return anchors.getOrDefault(tag, List.of()); }
    @Override public String role(String role) { return roles.get(role); }
    @Override public List<String> squad() { return squad; }
}
