package dev.shinobi.life.economy;

import java.nio.file.Path;

/** The compiled item data the tests read (build.gradle passes data/items as the items.data property). */
public final class Data {
    public static final Path DIR = Path.of(System.getProperty("items.data", "../../data/items"));
    private static Catalogue catalogue;

    public static synchronized Catalogue catalogue() {
        if (catalogue == null) catalogue = Catalogue.load(DIR);
        return catalogue;
    }

    private Data() {}
}
