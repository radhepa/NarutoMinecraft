# Development workflow

The controller for Shinobi Modpack development sessions. A fresh session reads the project
instructions, [STATE.md](STATE.md), the active card in [phases/](phases/) and only the sources its task
needs. Phase order: P00 baseline, P01 boot, P02 state, P03 street, P04 quest loop, P05 daily life,
P06 Academy combat, P07 Beta 1, P08 Genin systems, P09 Beta 2 and 2.5, P10 Beta 3, P11 release
candidate. Story integration (P07 onward) waits for the private story gate.

## Controller

```text
Continue the Shinobi Modpack using the approved phase card below.
Follow repository instructions and the existing roadmap. Apply Ponytail 5
in full mode: reuse working code and tools; implement the smallest complete
change. Do not reinstall the prepared environment or redesign settled systems.

Read the short development checkpoint if present. Inspect branch and worktree
state without changing or discarding unfinished work. For repository questions,
use one narrow Graphify query, normally --budget 1200, then inspect only the
relevant source passages. Treat the graph as navigation, not ground truth.
If a query fails or stalls, record that once and use bounded source searches;
do not loop on it or claim it succeeded. Never dump the graph or whole repo.

Choose the next uncompleted, dependency-ready task in this phase. State its
goal, owned paths and observable done condition briefly, then implement it.
Reuse the eight pure engines and Village Friends. Keep client rendering/input
separate from common/server logic. Preserve the documented one-way mod
dependencies; shared lower-level contracts live in Shinobi Core.

One session should deliver one reviewable increment. Split large phase work
into a short queue; do not stop after writing the queue. Execute its first
bounded task. Do not widen scope into later phases or speculative features.
Do not add dependencies unless existing facilities cannot meet the requirement.
Introduce runtime assemblies and shared interfaces when the current slice has
a real caller. Reach the ten-minute M2 play session before finishing all daily-
life and combat content or expanding districts. Player clarity, input feedback,
world activity, recovery and measured performance are part of done.

Use a worker only for genuinely separate work with explicit path ownership,
shared contracts and acceptance checks. Tell workers others are editing and
they must preserve those edits. At most two implementation workers. Review
high-risk save, reward, authority and integration changes after implementation;
do not repeat broad independent reviews for routine assets or small edits.

Test changed behavior at the responsible layer. Add focused tests for new
nontrivial behavior and regressions; do not test only that code mirrors itself.
Run related checks during work, full required checks at integration milestones,
and in-game proof for runtime behavior. Reuse passing evidence only while its
relevant inputs are unchanged. Never label a build-only result playable.
Refresh affected graph data using the installed documented update workflow
after a coherent batch. Do not force paid semantic regeneration on every edit.

All plot details, clues and private review findings stay under docs/story/.
Owner-facing output gives progress and checks without story details. Public
plans, screenshots, graphs and logs must not expose private content. Before
story approval use noncanonical fixtures, never silently lock the story.

Preserve settled beta choices: child stage, clanless start, single-player first,
server-authoritative state, vanilla storage, fixed canonical plot with role-bound
cast, seeded Classic/Varied appearance. No post-beta romance or power systems.
Use existing balance and progression data instead of inventing replacements.

On completion, update the short checkpoint with actual checks and the exact
next task. Normally keep replies within 120 words: result, verification and
next action, with a launch instruction for a playable milestone. Expand only
to explain a material blocker or decision. No invented scores or savings.
Do not push, merge to the default branch or publish release assets under this
prompt. Prepare a concrete reviewable result and retain all unfinished work.
```

## Player milestones

| Milestone | When | What the owner can actually try |
|---|---|---|
| M0: real launch | First P01 increment | Open Minecraft with Shinobi Core loaded; see launch evidence |
| M1: living street | P03–P04 | Meet residents, accept a fixture errand, earn ryo, buy an item and reload |
| M2: ten-minute play session | Early P05 + P06 | Create a character, follow a training objective, spar, see clear success feedback, buy/place one furnishing, sleep and reload |
| M3: complete Academy slice | P07 | Play from the approved opening to graduation without commands |
| M4: Genin loop | P08–P09 | Choose a mission, travel with the squad, use movement/combat and return for rewards |
| M5: complete beta | P10–P11 | Play through the exams, retain the save and install the candidate cleanly |

**M2 comes before completing the rest of P05/P06 or mass-producing districts and quests.** Use a noncanonical training fixture until the story gate passes. Implement just the creator, home and combat behavior needed for this play session, then complete the remaining required Beta 1 features. Pets, extra stock and full technique coverage are still required for the slice; they do not delay the first playable combat feedback.

At every player milestone check these observable qualities:

- **Understandable:** the player can identify the next action, its location, costs and completion/failure state without developer explanation. Use clear text, legible UI and input hints; vital feedback must not depend only on color or sound.
- **Responsive:** attacks, signs, movement and interaction produce coherent animation and hit/target feedback. Verify relevant controls can be rebound and do not conflict with normal Minecraft controls. Use existing settings before adding new ones.
- **Alive:** the street has readable routes, named residents with varied greetings, routine activity and deliberate visual treatment. Complete one representative street/building to the intended art standard before copying it across Konoha.
- **Recoverable:** quitting, reloading, losing a fight or retrying a quest preserves progress and avoids duplicate rewards or softlocks. Keep a small set of versioned test-save fixtures for these boundaries.
- **Measured:** record the machine, relevant settings, resident count and a repeatable route when checking performance. Profile a representative busy scene before multiplying districts. Change only demonstrated bottlenecks.

Give the owner a launch instruction and at most three specific things to judge. Fix a blocking issue in the tested slice before adding more content. Preserve clear user feedback in the checkpoint; do not invent a fun score, pretend to have watched a playtest or add unrelated features under the label of polish.

## Continuation

```text
Continue the current phase from its short checkpoint. Execute the next bounded
dependency-ready task, verify it, update the checkpoint, and give the concise
result. Reuse current context; do not repeat completed discovery or expand scope.
```

## Worker contract

```text
Task: [one observable result]. Base: [verified revision].
Own only: [explicit paths]. Inputs: [a few source links].
Required contract: [existing interface/data fields].
Done when: [focused test and/or runtime evidence].
Others are editing this project. Preserve their changes; request a contract
adjustment instead of rewriting their files. Do not spawn further workers.
Return changed paths, actual checks, integration notes and blockers in at most
200 words. Never include story details outside the private story boundary.
```

## Risk review

```text
Review this bounded diff against [acceptance conditions]. Focus on [save/reward/
authority/interface risk]. Read only necessary callers and tests. Do not modify
unrelated code. Return actionable findings with file locations and a concrete
failure case, or say none found and state any missing runtime evidence. Maximum
250 words. Do not certify behavior that has only been compiled.
```
