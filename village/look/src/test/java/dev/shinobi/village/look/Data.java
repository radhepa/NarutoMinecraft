package dev.shinobi.village.look;

import java.nio.file.Path;

/** The compiled creator file, loaded once for every test (the path comes from build.gradle). */
final class Data {
    static final CreatorRules RULES;
    static {
        try {
            RULES = CreatorRules.load(Path.of(System.getProperty("creator.json", "../../src/main/resources/data/narutominecraft/creator/creator.json")));
        } catch (Exception e) {
            throw new ExceptionInInitializerError(e);
        }
    }
    private Data() {}
}
