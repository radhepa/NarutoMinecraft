package dev.shinobi.village.dialogue;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

/**
 * The compiled dialogue bank: every line by pool, the questions, and the rules. Loaded from the files
 * {@code tools/dialogue/dialogue.py} writes into {@code data/narutominecraft/dialogue/} (the manifest lists them);
 * {@code story.json} (story-gated pools) is loaded the same way and kept apart only in the sources.
 */
public final class Bank {
    private final Map<String, List<Line>> pools;
    private final Map<String, Question> questions;
    private final Rules rules;
    private final int maxId;

    private Bank(Map<String, List<Line>> pools, Map<String, Question> questions, Rules rules, int maxId) {
        this.pools = pools; this.questions = questions; this.rules = rules; this.maxId = maxId;
    }

    /** Loads a compiled bank from a directory. */
    public static Bank load(Path dir) {
        return load(name -> {
            try { return Files.readString(dir.resolve(name), StandardCharsets.UTF_8); }
            catch (IOException e) { throw new UncheckedIOException(e); }
        });
    }
    /** Loads a compiled bank through a reader of its files by name (the glue reads them as resources). */
    public static Bank load(Function<String, String> files) {
        var manifest = Json.map(Json.parse(files.apply("manifest.json")));
        var pools = new LinkedHashMap<String, List<Line>>();
        var questions = new LinkedHashMap<String, Question>();
        Rules rules = null;
        for (var f : Json.list(manifest.get("files"))) {
            String name = f.toString();
            var data = Json.map(Json.parse(files.apply(name)));
            if (name.equals("rules.json")) { rules = Rules.read(data); continue; }
            for (var l : Json.list(data.get("lines"))) {
                var line = Line.read(l);
                pools.computeIfAbsent(line.pool(), k -> new ArrayList<>()).add(line);
            }
            for (var q : Json.list(data.get("questions"))) {
                var question = Question.read(q);
                questions.put(question.id(), question);
            }
        }
        if (rules == null) throw new IllegalStateException("the bank has no rules.json");
        return of(pools, questions, rules, Json.integer(manifest.get("max_id"), 0));
    }
    /** A bank from lines and questions in memory (tests). */
    public static Bank of(Map<String, List<Line>> pools, Map<String, Question> questions, Rules rules, int maxId) {
        var frozen = new HashMap<String, List<Line>>();
        int max = maxId;
        for (var e : pools.entrySet()) {
            frozen.put(e.getKey(), List.copyOf(e.getValue()));
            for (var l : e.getValue()) max = Math.max(max, l.id());
        }
        for (var q : questions.values()) max = Math.max(max, q.num());
        return new Bank(Collections.unmodifiableMap(frozen), Collections.unmodifiableMap(new LinkedHashMap<>(questions)), rules, max);
    }

    public List<Line> pool(String key) { return pools.getOrDefault(key, List.of()); }
    public boolean has(String key) { return pools.containsKey(key); }
    public java.util.Set<String> poolKeys() { return pools.keySet(); }
    public java.util.Collection<Question> questions() { return questions.values(); }
    public Question question(String id) { return questions.get(id); }
    public Rules rules() { return rules; }
    /** The highest line or question id: the heard ledger needs one bit per id up to it. */
    public int maxId() { return maxId; }
    public int lineCount() {
        int n = 0;
        for (var p : pools.values()) n += p.size();
        return n;
    }
}
