package dev.shinobi.life.home;

import java.util.List;

/**
 * A photo taken at a milestone, hung in a wall frame. {@code people} are roles ({@code role:teammate_a}), so the
 * photo shows whoever the save bound to them; {@code stage} is the player's age stage when it was taken. After a time
 * skip the same milestone can be retaken ({@code version} 2, 3...): the newest hangs, the older ones go in the album.
 */
public record Photo(String id, long day, List<String> people, String stage, int version) {

    public Photo {
        people = List.copyOf(people);
    }

    /** The milestones that take a photo, by slice. The story session may add its own under {@code photo.story.<hook>}. */
    public static final List<String[]> MILESTONES = List.of(
            new String[]{"photo.class", "b1", "Ch 2: the Academy class"},
            new String[]{"photo.graduation", "b1", "Ch 7: graduation day"},
            new String[]{"photo.squad", "b2", "Ch 8: the new squad with its sensei"},
            new String[]{"photo.first_c_rank", "b2", "Ch 11: the squad on the road"},
            new String[]{"photo.leaf_festival", "b2", "The Leaf Festival, with whoever came along"},
            new String[]{"photo.chunin_exams", "b3", "Ch 20: after the results"},
            new String[]{"photo.squad.teen", "later", "The squad retaken after the first time skip"},
            new String[]{"photo.squad.adult", "later", "The squad retaken after the second time skip"},
            new String[]{"photo.jonin", "later", "Promotion to Jonin"},
            new String[]{"photo.wedding", "later", "Your wedding at the shrine"},
            new String[]{"photo.family", "later", "Your household, once you have one"},
            new String[]{"photo.hokage", "later", "The day your face goes on the Rock"});
}
