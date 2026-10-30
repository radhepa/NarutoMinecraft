package dev.shinobi.village;

import com.google.gson.JsonObject;
import dev.shinobi.core.SaveSeed;
import dev.shinobi.village.look.ResidentNames;
import dev.villagefriends.VillageFriends;
import dev.villagefriends.VillageSettlements;
import dev.villagefriends.outfit.ResidentLook;
import net.minecraft.network.chat.Component;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.npc.villager.Villager;

/** Names belong to the save, even when Classic reuses the same cast UUIDs and looks. */
public final class LeafNames {
    private static final String NAMED = "narutominecraft.named", CLAN = "narutominecraft.clan:";
    private static final ResidentNames POOLS = new ResidentNames(LeafWardrobe.read("/data/narutominecraft/names/given.json").toString());

    private LeafNames() {}

    /** Called before a marker's resident enters the world; accepts clan ids with or without the clan: prefix. */
    public static void marker(Villager resident, JsonObject marker) {
        if (!marker.has("clan")) return;
        String clan = marker.get("clan").getAsString().replaceFirst("^clan:", "");
        if (!clan.equals("clanless") && !clan.equals("civilian") && !PlayerLooks.rules.isClan(clan))
            throw new IllegalArgumentException("Unknown resident clan: " + clan);
        resident.addTag(CLAN + clan);
    }

    /** VF calls this after making a profile. The vanilla custom name and entity tags survive save/reopen. */
    public static void ensure(Villager resident) {
        if (!(resident.level() instanceof ServerLevel level) || resident.entityTags().contains(NAMED)) return;
        var profile = VillageFriends.target(resident).getAttached(VillageFriends.PROFILE);
        if (profile == null) return;
        var look = ResidentLook.parse(profile.look());
        if (look == null) return;
        String clan = resident.entityTags().stream().filter(t -> t.startsWith(CLAN)).map(t -> t.substring(CLAN.length())).findFirst().orElse("clanless");
        String gender = switch (look.gender()) {
            case MALE -> "male";
            case FEMALE -> "female";
            case NON_BINARY -> "unisex";
        };
        var name = POOLS.roll(SaveSeed.of(level.getServer()).seed(), "resident:" + resident.getUUID(), gender, clan, PlayerLooks.rules);
        if (VillageFriends.target(resident).getAttached(VillageFriends.HOME) != null)
            VillageSettlements.rename(resident, name.full());
        else resident.setCustomName(Component.literal(name.full()));
        resident.addTag(NAMED);
    }
}
