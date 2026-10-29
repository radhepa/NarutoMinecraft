package dev.shinobi.village.dialogue.sim;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/**
 * Writes every dialogue pool the bond engine asks for ({@code dev.shinobi.life.bond.DialogueKeys.required()}) to a
 * file, one per line, for {@code dialogue.py --report}. Read by reflection so the dialogue engine never depends on
 * the bond engine.
 */
public final class BondKeys {
    public static void main(String[] args) throws Exception {
        @SuppressWarnings("unchecked")
        var keys = (List<String>) Class.forName("dev.shinobi.life.bond.DialogueKeys").getMethod("required").invoke(null);
        Files.write(Path.of(args[0]), keys);
        System.out.println(keys.size() + " bond engine pools written to " + args[0]);
    }
    private BondKeys() {}
}
