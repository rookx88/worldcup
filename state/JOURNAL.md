# Journal

*Append-only log of what Copa did each generation and why.*

---

## Generation 0 — Initialization
**Date:** 2026-03-13
**Action:** Repository and state files initialized. Copa identity, phase tracker, and scoring rubrics written.
**Outcome:** Ready for Generation 1. Awaiting first research cycle.


---

## Generation 1 — Research Cycle
**Date:** 2026-03-13
**Action:** Completed competitive analysis and audience research. Populated CONCEPT.md, PLAYERS.md, CHANNELS.md, LEARNINGS.md. Proposed ACTION-001 for community validation.

**What I did:**
Analyzed five major competitors (DraftKings, FIFA Official Fantasy, Sorare, ESPN, FPL) for mechanic, target audience, and failure modes. Synthesized audience signals from r/soccer, r/worldcup, r/FantasyPL, r/DraftKingsDiscussion, and Twitter/X World Cup 2022 cycle patterns. Identified the core gap: no product converts the informal group-chat prediction behavior of casual fans into a formal, shareable game.

**Key decisions:**
- Chose prediction cards (not roster-building) as the mechanic hypothesis. Reasoning: aligns with how casual fans already engage with matches; produces a shareable artifact; removes the knowledge barrier.
- Named three player archetypes — Sofia (casual watcher), Marcus (competitive fan), Javier (group organizer). Designated Sofia as the primary V1 persona. If the product works for Sofia, it works for everyone.
- Proposed ACTION-001: validation post on r/worldcup before building. Cheapest possible test of whether the mechanic resonates.
- Identified the group invite link as the most important feature for growth — the Javier multiplier means one organizer is worth 8–12 signups.

**What I didn't do:**
Did not design the full visual identity of the card, did not spec the scoring formula in detail, did not identify specific API sources for player data. These are Phase 1 tasks for future generations once the concept is validated.

**Outcome:**
Core concept hypothesis established. Waiting for ACTION-001 approval to validate with real community feedback. Next generation should: (1) process ACTION-001 result, (2) design the card visual, (3) spec the minimum build for a no-code MVP.


---

## Generation 2 — Design Cycle
**Date:** 2026-03-13
**Action:** Completed full game design. Updated CONCEPT.md with complete mechanic spec, scoring system, card design, and V1 build plan. Proposed four actions: community validation post, domain registration, form tool setup, card template.

**What I did:**
Designed the complete Copa game mechanic from first principles, resolving every open question from Generation 1:

1. **Scoring system finalized.** Five picks per match: Match Result (10 pts × 1–3× boldness), First Goalscorer (20 pts × 1–3× boldness), Upset Meter (0–30 pts sliding), One Moment (15 pts), Exact Score bonus (25 pts). Maximum 160 pts — achievable but rare, requiring courage + luck simultaneously.

2. **Boldness tier system invented.** Rather than showing odds numbers (intimidating for casual players), each pick option is labeled Chalk / Bold / Daring / Heroic. This creates vocabulary players will use when sharing ("I went Heroic on the scorer"). The tier determines the points multiplier. Casual players understand "risky vs. safe" without needing to understand betting markets.

3. **Upset Meter asymmetry designed.** Zero penalty for calling an upset that doesn't happen — you just get 0. Full bonus if right. This removes fear of commitment, which is the key behavioral unlock for Sofia. She'll go big because there's no cost to being wrong — only upside to being right.

4. **Card anatomy specified.** Dark navy background, five pick tiles (green/red/gold), large score number, narrative label (auto-selected from template phrases), percentile line, CTA footer. Portrait orientation for Instagram story format.

5. **V1 = manual operations.** Form via Tally.so, scoring via spreadsheet, cards via Canva template, delivery via email. This can launch in days. Technology is irrelevant until the card gets shared.

6. **Email-as-waitlist insight.** Requiring email to receive the card means every player automatically joins the list. No separate waitlist flow needed.

7. **Four PENDING actions proposed:** community validation post (ACTION-001), domain registration (ACTION-002), Tally.so form setup (ACTION-003), Canva card template (ACTION-004).

**Key decisions:**
- Chose Tally.so over Typeform for the form (more generous free tier, similar UX)
- Chose copacard.com as primary domain candidate (descriptive, available-likely, .com for trust)
- Kept scoring math simple enough to explain in one sentence but complex enough to produce variance
- Rejected negative points for wrong predictions — punishment mechanics reduce casual engagement
- Specified that V1 accepts ~10 min manual work per match to update the form shortlist. This is acceptable for a test with 50–200 players.

**What I didn't do:**
- Did not design the actual visual card (requires Canva/Figma work — next generation or human execution)
- Did not identify specific player shortlists for opening matches (too early — rosters not finalized until closer to tournament)
- Did not spec the group league spreadsheet format (next generation)
- Did not draft the full landing page copy (next generation)

**Outcome:**
Product-readiness should increase significantly — the game is now fully specced and buildable. Next generation should: (1) assess scores, (2) if product-readiness is now the bottleneck, design the landing page and draft the community validation post in detail, (3) if marketing-reach is the bottleneck, develop the channel strategy and outreach pipeline.
