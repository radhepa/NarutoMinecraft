# Beta dialogue bank

This folder is a developer companion to the approved story briefs. Keep its contents out of player-facing reports.

The beta batch adds 1,373 lines and 280 supplementary questions for 28 roles: the core recurring cast, the four
other senseis, the three other squads and the ramen cook. Each role has ten questions, two answers per question,
a remembered callback for each answer and an answer when the player turns the question back. The batch also
includes 96 combat/command lines, 45 mission-banter lines and 42 public chapter reactions. All use the existing
pool keys, name tokens and condition language. No new plot outcomes or `ans.*` flags are introduced: scripted
story choices keep the flags and options approved in the character files and quest data.

Every role's beta material has an introduction gate and a child-player gate. The Fourth's ordinary beta visits
close at the stadium reveal; the porter's earlier register closes at the later change in that role. Candidates
have the same beta lines in every rotation. Public chapter reactions expose only public events and include a
life beat for each chapter. The `story` tag indexes the relevant gate; `when` is what evaluates it. Multiple
completed story flags never need to be squeezed into one `Context.story` value.

Run `python tools/dialogue/dialogue.py` to compile, then `--check --report`. The real-bank JUnit checks in
`BetaDialogueTest` prove role selection, introduction gates, closed story states, chosen-answer-only callbacks,
the asks-back pools and answer memory after a ledger round trip. Gradle tracks the compiled bank as test input.

shortcut: these beta lines use the briefs' curated character registers; add the full Varied archetype/craft
skins when the Varied cast's role/craft bindings are implemented. Later-arc scenes, their exact story-choice
questions and bond-quest scenes follow DIALOGUE_BRIEFS section 6 after the beta has been played. The in-game
Context/condition/ledger/menu bridge remains the Phase 0 integration listed in DIALOGUE.md section 13; this
batch is compiled content and pure-engine proof, not a replacement for VF's live conversation UI.
