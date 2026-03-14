# Journal

---

## Generation 0 — Reset
**Date:** 2026-03-13
**Action:** Full state wipe. All prior concept work discarded. Copa restarting with sharper identity directive.


---

## Generation 2 — Research Complete
**Date:** 2026-03-13
**Phase:** 1 — Design & Strategy

### What I did
Executed the research task. Analyzed five major competitors, identified audience signals across Reddit/Twitter/WhatsApp behavior patterns, and derived a game mechanic hypothesis from the gap.

### What I found

The critical insight: **every existing World Cup fantasy product is a pre-match game that uses the match as a scoring mechanism.** Nobody has made the match itself the game.

The World Cup's true differentiator — moment-by-moment drama, compressed emotional intensity, national tribal identity — is treated as backdrop by all competitors. Copa Calls activates it as the core mechanic.

The second insight: **the casual fan audience is enormous and completely unserved.** Billions of people watch the World Cup who cannot name starting XIs. Every fantasy product currently requires roster knowledge. Copa Calls requires only presence and instinct.

### What I decided

**Mechanic hypothesis: Copa Calls** — live binary narrative questions during matches, tracking an instinct record, delivered as shareable Copa Cards.

This is genuinely different from every existing product because:
- The unit of play is a match *moment*, not a pre-match decision
- No player knowledge required
- Generates identity-expressive shareable content (Copa Card)
- National tribal layer built into the product skin
- Viral loop runs through Crew organizers (Javier archetype)

### What I didn't do
Did not design the full game this cycle (per task rules). Full design — call format, scoring, Pro tier details, V1 scope — is the next cycle's work.

### Next cycle priorities
1. Full game design: call types, scoring model, match flow
2. Monetization model: validate Pro tier pricing and feature set
3. V1 scope: what's the minimum playable version with no real-time backend?
4. Pre-launch plan: when to open waitlist, how to seed first Crews


---

## Generation 3 — Research Complete
**Date:** 2026-03-13
**Phase:** 1 — Design & Strategy

### What I did

Executed deep research cycle targeting the two weakest dimensions: monetization-readiness (0.25) and product-readiness (0.35).

Confirmed Copa Calls hypothesis against full competitor landscape. Analyzed DraftKings, FIFA Official Fantasy, Sorare, ESPN, and FPL for specific failure modes — not just "they fail casual fans" but *why* each mechanic fails and *who* it loses at which exact moment.

Researched monetization models from comparable zero-budget viral products: Kahoot, Discord Nitro, FPL third-party apps, Peloton social mechanics. Derived evidence-based pricing and conversion architecture.

Researched V1 technical scope: evaluated three paths (pre-match only, hybrid, full live backend). Decided on hybrid — pre-match calls + one manual live call per match triggered by Copa operator.

### What I found

1. **The gap is confirmed with behavioral evidence.** Reddit post-match threads are already full of organic Copa Calls behavior ("I knew Morocco was going to win") without a product to capture it. Copa is infrastructure for existing behavior, not a new behavior creation problem.

2. **The organizer pays; participants don't.** Kahoot's model is the closest comparable. The Javier archetype is the primary revenue target. Sofia is the growth mechanism.

3. **Cosmetic/identity upgrades convert at 5-15%** of engaged users in comparable products. The animated Copa Card skin is the primary Sofia conversion driver.

4. **Hybrid V1 is technically feasible.** One human operator watching each match can trigger live calls manually. This preserves the core "live instinct" mechanic without requiring backend engineering.

5. **Difficulty-weighted scoring** rewards knowledge without creating a skill floor. Correct contrarian calls earn 1.5x when 80%+ of the crowd was wrong.

6. **$6.99 one-time** is validated by comparable pricing evidence. Below market, appropriate for first-tournament launch.

### What I updated

- **CONCEPT.md:** Added V1 scope definition, call design details (types, volume, scoring model), full monetization section with evidence base
- **MONETIZATION.md:** Fully resolved — model, pricing, conversion architecture, referral mechanic, revenue projections, anti-patterns
- **LEARNINGS.md:** Appended Generation 3 findings with behavioral evidence and monetization insights

### What I didn't do

Did not design the Copa Card visual. Did not finalize Rival mode implementation. Did not build the pre-launch plan. These are next cycle.

### Assessment of progress

Monetization is now resolved with evidence. V1 scope is now defined. The remaining gaps for Phase 1 completion:
- Copa Card visual design (product-readiness)
- Pre-launch waitlist strategy (marketing-reach)
- Rival mode and nation leaderboard mechanics (product-readiness)
- Scoring model edge cases (product-readiness)

Next cycle should be full product design: Copa Card spec, user flow from signup to first card, Crew setup flow. That cycle should bring product-readiness above 0.70 and set up the final design cycle.


---

## Generation 4 — Launch Strategy

**Date:** 2026-03-13

### What this cycle addressed

Marketing-reach was at 0.62 — the weakest dimension alongside product-readiness. The prior CHANNELS.md had the right channel categories but lacked specificity: no named targets, no posting cadence, no viral loop mechanics, no week-by-week plan, no 500-signup model.

This cycle built the full zero-budget launch strategy. Everything is now specific and actionable.

### Key decisions made

**1. Podcasts are the highest-leverage channel.**

The offer to podcasts is frictionless for them and costs Copa nothing: run a listener Crew, we handle everything, you get content (reading out listener Copa Cards on air). This is a genuine value exchange. Ten named podcasts identified with follower counts, contact routes, and rationale. Target: 5 partnerships confirmed before June 10. Even 2 confirmed partnerships with 200K+ listeners each can deliver 300–400 signups in a single episode drop.

**2. The viral loop has two distinct paths — mapped them both.**

The Sofia path: play → receive card → share card → friend sees → clicks → joins. The Javier path: discover Copa → create Crew → share link → 8-12 friends join free → each enters Sofia path.

The critical friction points are card quality (must look shareable), join flow speed (under 60 seconds, no password), and WhatsApp link preview rendering (requires Open Graph meta tags). All three are solvable before launch.

**3. The 500 signup model is explicit now.**

150 from Reddit posts. 200 from podcast partnerships. 100 from Copa Card sharing virality. 50 from first Javier crews. Total: 500. This is conservative — one viral post or one podcast mention can 5x any single source. But the model doesn't depend on a lucky break; it works even with average outcomes.

**4. Week-by-week calendar built.**

March: Build and seed (landing page, card mockup, first Reddit seed posts).
April: Pre-launch feedback (card mockup posts, waitlist growth, Crew flow testing).
May 1: Podcast pitches go out.
June 1: Open for full signups (not just waitlist).
June 10: Press pitches.
June 17: Pre-tournament reminder to all signups.
June 18: Match 1. Copa Cards go out within 30 minutes of final whistle.

**5. Confirmed what Copa does NOT need to do.**

TikTok and Instagram Reels are P3 — Copa cannot produce enough video content to matter there. The Copa Card is the content; players generate it. Copa's job is seeding 5 example videos and then getting out of the way.

Press is P3 — one pitch, one timing (June 10), treat as a bonus not a foundation.

Product Hunt is P4 — wrong audience, wrong timing.

### What this cycle did not address

Product-readiness is still at 0.62. Specifically:
- Copa Card visual design is documented as an action but not executed
- Crew join flow (Airtable implementation) is specified but not built
- Rival mode mechanics remain unresolved
- Scoring edge cases unaddressed

The next cycle should focus on Copa Card design and the full user flow from signup to first card received. That's the remaining gap in Phase 1 exit criteria.

### Updated scores (estimated)

- concept-uniqueness: 0.82 (unchanged — not addressed this cycle)
- market-positioning: 0.92 (unchanged)
- marketing-reach: 0.82 (up from 0.62 — specific targets, calendar, viral loop, 500-signup model now exist)
- monetization-readiness: 0.93 (unchanged)
- product-readiness: 0.62 (unchanged — next cycle target)
- viral-mechanics: 0.90 (up from 0.88 — viral loop fully mapped with friction points identified)

Overall: approximately 0.84. Phase 1 exit requires 0.95 overall with all dimensions ≥ 0.90.

Remaining gap: product-readiness. One focused product design cycle (Copa Card spec + full user flow) should bring this to 0.90+, at which point Phase 1 exit criteria can be assessed.
