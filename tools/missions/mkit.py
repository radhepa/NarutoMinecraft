"""The mission authoring kit: small helpers that build board-mission templates in the quest format.

A template is ROADMAP section 5's quest format with `kind: mission` plus the board's own fields (rank,
category, slots, twists, outcomes, bonuses, places). The catalogue modules call `mission(...)` once per
template; `missions.py` compiles every template to one JSON file in the Adventure datapack and checks it.
MISSIONS.md explains every field.

Text is never written here: titles, briefings, twist premises and choices are dialogue keys derived from
the id (`mission.d.lost_pet.title`), and the dialogue session writes the lines. Premises in English are
for MISSIONS.md and the generated catalogue only.
"""

RANKS = ("d", "c", "b", "a", "s")
PARTIES = ("squad", "solo", "squad_or_solo", "lead", "anbu_cell")
STATUSES = ("beta", "later")

# Bonus objectives that lift a mission's grade (MISSIONS.md, "Grades"). Each names what the engine measures.
BONUSES = {
    "fast": "Finished within the template's fast time",
    "unseen": "Never spotted during sneak steps",
    "no_knockouts": "Nobody in the party was knocked out",
    "client_unharmed": "The client or cargo took no harm",
    "all_found": "Every optional find was found",
    "gentle": "The animal or person was brought in unhurt",
    "kind_choice": "The choice the client hoped for",
    "no_alarm": "No alarm was raised",
    "spared": "Enemies defeated without a finishing blow (captured or routed)",
    "teamwork": "Every teammate's role was used (squad missions)",
    "careful": "Nothing fragile was dropped or broken",
    "extra_mile": "An optional step done for the client",
    "clean_record": "Nothing taken that was not yours",
}


def _key(mid, *parts):
    """A dialogue key in the dialogue session's scheme: dlg:<template id>.<part>."""
    return "dlg:" + ".".join((mid,) + parts)


# The dialogue parts every template has (the dialogue session's pools).
PARTS = ("brief", "accept", "decline", "progress", "success", "fail", "report")


# --- objectives ---------------------------------------------------------------------------------------

def go(place):
    return {"type": "go", "place": place}


def talk(who, dialogue=None):
    o = {"type": "talk", "who": who}
    if dialogue:
        o["dialogue"] = dialogue
    return o


def inspect(target, at=None, count=None):
    o = {"type": "inspect", "target": target}
    if at:
        o["at"] = at
    if count:
        o["count"] = count
    return o


def collect(target, at=None, count=None):
    o = {"type": "collect", "target": target}
    if at:
        o["at"] = at
    if count:
        o["count"] = count
    return o


def deliver(item, to):
    return {"type": "deliver", "item": item, "to": to}


def craft(item, count=1):
    return {"type": "craft", "item": item, "count": count}


def buy(item, at, count=1):
    return {"type": "buy", "item": item, "at": at, "count": count}


def perform(what, at=None, count=None):
    o = {"type": "perform", "what": what}
    if at:
        o["at"] = at
    if count:
        o["count"] = count
    return o


def defeat(group, at=None):
    o = {"type": "defeat", "group": group}
    if at:
        o["at"] = at
    return o


def escort(who, to):
    return {"type": "escort", "who": who, "to": to}


def protect(who, until=None, at=None):
    o = {"type": "protect", "who": who}
    if until:
        o["until"] = until
    if at:
        o["at"] = at
    return o


def survive(until, at=None):
    o = {"type": "survive", "until": until}
    if at:
        o["at"] = at
    return o


def sneak(to):
    return {"type": "sneak", "to": to}


def wait_until(time, at=None):
    o = {"type": "wait_until", "time": time}
    if at:
        o["at"] = at
    return o


def sleep(at):
    return {"type": "sleep", "at": at}


def choose(options):
    """A dialogue choice. `options` maps an option id to the outcome it leads to (or None to keep going)."""
    return {"type": "choose", "options": dict(options)}


# --- slots --------------------------------------------------------------------------------------------

def resident(**where):
    return {"pick": "resident", "where": where} if where else {"pick": "resident"}


def anchor(tag):
    return {"pick": "anchor", "tag": tag}


def region(*ids):
    return {"pick": "region", "from": list(ids)}


def one_of(*values):
    return {"pick": "one_of", "from": list(values)}


def count(lo, hi):
    return {"pick": "count", "range": [lo, hi]}


def role(r):
    return {"pick": "role", "role": r}


def enemy_group(*ids):
    return {"pick": "enemy_group", "from": list(ids)}


def suspect_of(*slots):
    """The culprit: one of the named resident slots, rolled per mission (who it is goes in the twist roll)."""
    return {"pick": "suspect", "from": list(slots)}


# --- steps --------------------------------------------------------------------------------------------

class S:
    """One step: an objective, the step after it, and optional branches and actions."""

    def __init__(self, name, objective, nxt=None, branch=(), on_enter=(), on_done=(), optional=None):
        self.name, self.objective, self.nxt = name, objective, nxt
        self.branch, self.on_enter, self.on_done, self.optional = list(branch), list(on_enter), list(on_done), optional

    def json(self):
        j = {"objective": self.objective}
        if self.on_enter:
            j["on_enter"] = self.on_enter
        if self.on_done:
            j["on_done"] = self.on_done
        if self.branch:
            j["branch"] = [{"if": c, "next": n} for c, n in self.branch]
        if self.optional:
            j["bonus"] = self.optional
        j["next"] = self.nxt
        return j


def twist_if(tid):
    return {"twist": tid}


def chose(step, option):
    return {"chose": [step, option]}


def spawn(group, at):
    return {"spawn_group": [group, at]}


def end(outcome):
    return {"mission_outcome": outcome}


# --- the template ---------------------------------------------------------------------------------------

def outcome(pay=1.0, standing=0, acts=(), flags=(), news=None, extra=None):
    """What an ending does: pay multiplier, client standing change, bond acts (`[who, act]`), flags."""
    o = {"pay": pay, "standing": standing}
    if acts:
        o["acts"] = [list(a) for a in acts]
    if flags:
        o["flags"] = [list(f) for f in flags]
    if news:
        o["news"] = news
    if extra:
        o.update(extra)
    return o


def twist(tid, weight=1, harder=False, modifier=False):
    """A rolled variant. Most switch the graph onto their branch; a `modifier` changes the rules instead
    (no running with a fragile parcel) and needs no branch."""
    t = {"id": tid, "weight": weight, "harder": harder}
    if modifier:
        t["modifier"] = True
    return t


def mission(mid, rank, category, *, premise, minutes, steps, client=None, slots=None, party="squad",
            twists=(), outcomes=None, bonus=(), enemies=(), anchors=(), regions=(), unlock=None, pay=0.5,
            tags=(), fail=None, season=None, event=None, contested=False, chain=None, status=None,
            classic=True, fast_hours=None, days=None, twist_premises=None, choice_premises=None):
    assert rank in RANKS, mid
    assert party in PARTIES, mid
    status = status or ("beta" if rank in ("d", "c") else "later")
    t = {
        "format": 1,
        "id": mid,
        "kind": "mission",
        "rank": rank,
        "category": category,
        "status": status,
        "title": _key(mid, "title"),
        "brief": _key(mid, "brief"),
        "dialogue": {p: _key(mid, p) for p in PARTS},
        "minutes": minutes,
        "party": party,
    }
    if days:
        t["days"] = days
    if unlock:
        t["unlock"] = unlock
    if season:
        t["season"] = season
    if event:
        t["event"] = event
    slot_map = {}
    if client:
        slot_map["client"] = client
    slot_map.update(slots or {})
    t["slots"] = slot_map
    t["start"] = steps[0].name
    t["steps"] = {s.name: s.json() for s in steps}
    t["twists"] = [dict(tw, premise=_key(mid, "twist", tw["id"])) for tw in twists]
    for s in steps:
        if s.objective["type"] == "choose":
            s.objective["dialogue"] = _key(mid, "choice", s.name)
    t["outcomes"] = outcomes or {"done": outcome()}
    t["bonus"] = list(bonus)
    if fast_hours:
        t["fast_hours"] = fast_hours
    t["fail"] = fail or {"on_death": True, "timeout_days": 1 if rank == "d" else 3}
    t["enemies"] = list(enemies)
    t["places"] = {"anchors": list(anchors), "regions": list(regions)}
    t["pay"] = {"band": rank, "xp_band": rank, "weight": pay}
    t["tags"] = list(tags)
    t["contested"] = contested
    if chain:
        t["chain"] = chain
    t["classic"] = classic
    t["banter"] = "dlg:mission.banter." + category
    # English premises for the docs only; the game reads the keys above.
    t["_premise"] = premise
    if twist_premises:
        t["_twists"] = twist_premises
    if choice_premises:
        t["_choices"] = choice_premises
    return t
