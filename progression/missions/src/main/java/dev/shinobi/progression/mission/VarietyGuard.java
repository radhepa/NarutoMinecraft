package dev.shinobi.progression.mission;

import java.util.HashMap;
import java.util.Map;

import static dev.shinobi.progression.mission.Json.*;

/**
 * Keeps the board from repeating itself (MISSIONS.md section 7). Hard rule: a template the player took is not offered
 * again within its rank's {@code template_gap_days}. Soft rules, which the slot filler and the board prefer but
 * break when nothing else fits: a client is not cast again within {@code client_gap_days} of a mission taken for
 * them, an anchor not within {@code anchor_gap_days}, and a repeated template does not repeat its last twist within
 * {@code twist_gap_days}.
 */
public final class VarietyGuard {
    final Map<String, Integer> templateDay = new HashMap<>(), clientDay = new HashMap<>(), anchorDay = new HashMap<>(),
            offeredDay = new HashMap<>();
    final Map<String, String> lastTwist = new HashMap<>();
    final Map<String, Integer> twistDay = new HashMap<>();
    final Map<String, Object> rules;

    public VarietyGuard(Map<String, Object> deskVariety) { this.rules = deskVariety; }

    public int templateGap(Rank r) { return (int) num(map(rules.get("template_gap_days")).get(r.id()), 7); }

    /** Hard: may this template be offered today? */
    public boolean templateFree(Template t, int day) {
        Integer last = templateDay.get(t.id());
        return last == null || day - last >= templateGap(t.rank());
    }
    /** Soft: was it on the board in the last few days without being taken? Its weight drops. */
    public boolean recentlyOffered(Template t, int day) {
        Integer last = offeredDay.get(t.id());
        return last != null && day - last < 3;
    }
    public boolean clientFresh(String resident, int day) {
        Integer last = clientDay.get(resident);
        return last == null || day - last >= num(rules.get("client_gap_days"), 4);
    }
    public boolean anchorFresh(String anchor, int day) {
        Integer last = anchorDay.get(anchor);
        return last == null || day - last >= num(rules.get("anchor_gap_days"), 2);
    }
    /** The twist this template must not repeat today, or null. */
    public String avoidTwist(Template t, int day) {
        Integer last = twistDay.get(t.id());
        return last != null && day - last < num(rules.get("twist_gap_days"), 10) ? lastTwist.get(t.id()) : null;
    }
    public int maxSameCategory() { return (int) num(rules.get("max_same_category"), 1); }

    public void offered(Offer o, int day) { offered(o.template(), day); }
    public void offered(String template, int day) { offeredDay.put(template, day); }

    public void taken(Offer o, Template t, int day) {
        templateDay.put(o.template(), day);
        if (o.client() != null) clientDay.put(o.client(), day);
        for (var e : o.slots().entrySet())
            if (t.slots().get(e.getKey()) != null && "anchor".equals(t.slots().get(e.getKey()).get("pick"))) anchorDay.put(e.getValue(), day);
        if (o.twist() != null) { lastTwist.put(o.template(), o.twist()); twistDay.put(o.template(), day); }
    }

    public Integer lastTaken(String template) { return templateDay.get(template); }
}
