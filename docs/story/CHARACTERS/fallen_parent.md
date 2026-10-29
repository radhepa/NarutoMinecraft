# `role:fallen_parent`

> **SPOILERS: for developers only.** Part of the [story bible](../STORY_BIBLE.md). In lineage B
> (`twist.lineage = fallen`) they are the player's parent; in lineage A they are not
> ([ROTATIONS.md](../ROTATIONS.md) §2).

## At a glance

| | |
|---|---|
| Role | The sensei's dead teammate, a Leaf Jonin, killed in the Ash Road ambush (~Y-8) |
| Look | None in the world: a painted portrait drawn in shadow (Ch 41 mural, the sensei's box); never a resident |
| Gender | Rolled per save from the `names` stream; dialogue about them uses `{they:fallen_parent}` |
| Name | Given Family, both rolled (an ordinary family name, **no clan**: the renamed grandmother's adoptive family was clanless). On the memorial stone at Ch 10, just beside the chiselled gap; moved beside the Kagari names in Ch 41 |
| Line | Grandchild of one of the twenty-seven renamed Kagari children; sealed flame that flickered |
| Habits | Hummed the watch-fire song on missions; loved persimmons; laughed at their own jokes |
| Appears | Only through others: the sensei (Ch 10, 13, 18, 21, 25, 36, 48), the stone, the archive (Ch 36 to 37), the box (lineage B) |

## Who they were

Warm, a little reckless, the team's morale. On their old team's campfires the fire leaned toward
the team; they laughed it off ("The fire likes us"). They did not know what they were; the seal
kept the flame from waking fully. Yūgure found them with chakra paper and ambushed the team on the
Ash Road to test them. The team was three: the sensei, `fallen_parent` and `sensei_3` (Classic:
a Yuhi genjutsu user), whom the sensei sent back to signal for help. They died; the sensei was
burned pulling them out; `sensei_3` came back with help too late.

**Lineage B only.** They married a civilian of a border village and kept the child there, far from
the village's eyes. They were the one who carved the pair of watch-fire charms (they didn't know
the custom's meaning, only that their grandmother did it). After the ambush the spouse fled with
the child to a sister's house with a persimmon tree.

**Lineage A.** No child. The persimmons were only their favourite fruit; the song only a song their
grandmother sang.

## What remains of them

| Thing | Where | Lineage |
|---|---|---|
| Their name on the memorial stone | Training Ground 3 | Both |
| A persimmon left every year by the sensei | The stone, Ch 21 | Both |
| The sealed Ash Road report | The archive, Ch 36 | Both |
| Their grandmother's line on the renaming list | The archive, Ch 37 | Both |
| Their forehead protector | The sensei's box | Both (the box exists in both saves; seen only in B) |
| Half a watch-fire charm | The sensei's box | **B only** |
| A letter, never sent, to "the little one" ("If the fire ever leans toward you, it means someone loves you. Let it.") | The box | **B only**, read at Ch 48 |
| A team letter to the sensei ("If I'm late, eat my share") | The sensei keeps it in a pocket | Both; the sensei shows it at level 7 |

## Brief for lines about them

Others speak of them; they never speak. Rules:

- **The sensei** speaks of them in fragments until Ch 25 ("A teammate. The best of us."), then more.
  Never "your parent" before Ch 48 in either lineage.
- **`sensei_3`** remembers them as the one who made the team laugh, and blames the sensei a little
  for sending her back; her lines live in the ensemble files.
- **The keeper** knew of them as a name on a sealed report; his line in Ch 36 is guilt, not memory.
- **The memorial** (Ch 41) and teammate_a's mural show them in shadow; the mural never shows a face
  (no fixed look exists).
- **Lineage B, Ch 48:** the sensei tells the story of the ambush in full and reads the unsent letter.
  The player's answer is `ans.player.parent_meet` ("You found me anyway" / "You should have looked" /
  say their teammate's name).
- **Lineage A:** at Ch 48 to 49 the sensei says, of the second: "They'd have liked her. They liked
  anyone who fought for kids."
- **Never reveal before:** that they were Kagari (Ch 25 for the flame, Ch 37 for the line); that
  Yūgure killed them (Ch 36); the box's charm (B, Ch 48).

## Questions

They ask none. One question about them is asked of the player:

| Id | When | Asker | Question | Options | Remembered |
|---|---|---|---|---|---|
| `ans.sensei.fallen_name` | Ch 41, at the re-carved stone (level 5 with the sensei) | the sensei | "Should their name stand with the Leaf's dead, or with the Kagari?" | Leaf / Kagari / both, side by side | Ch 41.1 carving; Ch 55 speech in lineage B |

## New flags

- `ans.sensei.fallen_name` (leaf, kagari, both)
