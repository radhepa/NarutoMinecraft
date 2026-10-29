package dev.shinobi.village.look;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class AgeStageTest {
    @Test
    void scalesFollowTheRoadmap() {
        assertEquals(0.78, AgeStage.CHILD.scale);
        assertEquals(1.1, AgeStage.CHILD.head);
        assertEquals(0.9, AgeStage.TEEN.scale);
        assertEquals(1.0, AgeStage.ADULT.scale);
        assertEquals(1.0, AgeStage.TEEN.head);
        assertEquals(1.62 * 0.78, AgeStage.CHILD.eyeHeight(), 1e-9);
        assertEquals(1.8 * 0.9, AgeStage.TEEN.height(), 1e-9);
    }

    @Test
    void timeSkipsMoveOneStageEachAndAdultIsForGood() {
        assertEquals(AgeStage.CHILD, AgeStage.afterTimeSkips(0));
        assertEquals(AgeStage.TEEN, AgeStage.afterTimeSkips(1));
        assertEquals(AgeStage.ADULT, AgeStage.afterTimeSkips(2));
        assertEquals(AgeStage.ADULT, AgeStage.afterTimeSkips(5));
        assertEquals(AgeStage.ADULT, AgeStage.ADULT.next());
        assertEquals(AgeStage.TEEN, AgeStage.CHILD.next());
    }

    @Test
    void theCompiledFileAgreesWithTheEnum() {
        var stages = CreatorRules.map(Data.RULES.data.get("stages"));
        for (var s : AgeStage.values()) {
            var st = CreatorRules.map(stages.get(s.id()));
            assertEquals(s.scale, ((Number) st.get("scale")).doubleValue(), s.id());
            assertEquals(s.head, ((Number) st.get("head")).doubleValue(), s.id());
            assertEquals(s.fromAge, ((Number) ((java.util.List<?>) st.get("ages")).get(0)).intValue(), s.id());
        }
    }
}
