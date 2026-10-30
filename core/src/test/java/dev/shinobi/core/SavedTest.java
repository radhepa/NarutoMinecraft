package dev.shinobi.core;

import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.mojang.serialization.Codec;
import com.mojang.serialization.JsonOps;
import net.minecraft.nbt.NbtOps;
import org.junit.jupiter.api.Test;

import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.*;

class SavedTest {
    static <A> A read(Codec<A> codec, String json) {
        return codec.parse(JsonOps.INSTANCE, JsonParser.parseString(json)).getOrThrow();
    }

    static JsonElement fixture(String name) throws Exception {
        try (var in = SavedTest.class.getResourceAsStream("/saves/v1/" + name)) {
            return JsonParser.parseReader(new InputStreamReader(in, StandardCharsets.UTF_8));
        }
    }

    @Test void theVersionOneTestSaveStillReads() throws Exception {
        assertEquals(new PlayerRecord(1, "genin", 7, "teen", "nara", "hard"),
                PlayerRecord.CODEC.parse(JsonOps.INSTANCE, fixture("player_record.json")).getOrThrow());
        assertEquals(new SaveSeed(-42, "varied"), SaveSeed.CODEC.parse(JsonOps.INSTANCE, fixture("save_seed.json")).getOrThrow());
    }

    @Test void aRecordWritesAndReadsBackTheSame() {
        var r = new PlayerRecord(1, "chunin", 30, "adult", "uchiha", "story");
        assertEquals(r, PlayerRecord.CODEC.parse(JsonOps.INSTANCE, PlayerRecord.CODEC.encodeStart(JsonOps.INSTANCE, r).getOrThrow()).getOrThrow());
    }

    @Test void missingAndDamagedFieldsDefaultAndTheRestIsKept() {
        assertEquals(new PlayerRecord(1, "genin", 1, "teen", "", "shinobi"),
                read(PlayerRecord.CODEC, "{\"version\": 1, \"rank\": \"genin\", \"level\": \"seven\", \"age_stage\": \"teen\"}"));
    }

    @Test void aRecordFromANewerPackKeepsTheKnownFieldsAndStillSaves() {
        var r = read(PlayerRecord.CODEC, "{\"version\": 2, \"rank\": \"genin\", \"level\": 7, \"age_stage\": \"teen\", \"clan\": \"nara\", \"difficulty\": \"hard\", \"new\": 1}");
        assertEquals(new PlayerRecord(2, "genin", 7, "teen", "nara", "hard"), r);
        assertTrue(PlayerRecord.CODEC.encodeStart(JsonOps.INSTANCE, r).isSuccess());
    }

    @Test void theRecordRoundTripsThroughNbtAsFabricSavesIt() {
        var r = new PlayerRecord(1, "genin", 3, "child", "", "story");
        assertEquals(r, PlayerRecord.CODEC.parse(NbtOps.INSTANCE, PlayerRecord.CODEC.encodeStart(NbtOps.INSTANCE, r).getOrThrow()).getOrThrow());
        var s = new SaveSeed(Long.MIN_VALUE, "varied");
        assertEquals(s, SaveSeed.CODEC.parse(NbtOps.INSTANCE, SaveSeed.CODEC.encodeStart(NbtOps.INSTANCE, s).getOrThrow()).getOrThrow());
    }

    @Test void anUnknownModeIsClassicButAnUnreadableSeedIsNotGuessed() {
        assertEquals(new SaveSeed(5, "classic"), read(SaveSeed.CODEC, "{\"seed\": 5, \"mode\": \"chaos\"}"));
        assertEquals(new SaveSeed(5, "classic"), read(SaveSeed.CODEC, "{\"seed\": 5}"));
        assertTrue(SaveSeed.CODEC.parse(JsonOps.INSTANCE, JsonParser.parseString("{\"mode\": \"varied\"}")).isError());
    }
}
