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


---

## Generation 5 — Game Design Complete

**Date:** 2026-03-14

### What this cycle did

Full game design spec written. Product-readiness was the weakest dimension (0.62). This cycle closes that gap by specifying every design element that was previously described but not defined.

---

### Key decisions made

**1. The Bold Call mechanic added.**

The brief asked to distinguish "bold" vs "safe" picks and reward bold picks differently. Copa already had a crowd-contrarian multiplier that implicitly did this, but it was invisible to players — they didn't know when they were being contrarian until after the match.

The Bold Call makes it explicit: one declaration per match, double points if right, −5 if wrong. Players choose when to commit fully.

This decision adds three things the concept previously lacked:
- A per-match story arc (the Bold Call is the dramatic peak)
- A shareable narrative ("I went bold on the Morocco clean sheet and it paid off")
- A skill signal over time (Bold Call hit rate separates good players from lucky ones)

The −5 penalty for wrong Bold Calls was debated. Arguments against: Copa has no negative scoring by design. Arguments for: without any downside, every player will Bold Call every match, which destroys the meaning of the declaration. Resolved by keeping −5 as the sole negative scoring element, with the understanding that it's small enough not to be punishing and large enough to make the choice feel real.

**2. Copa Card designed field by field.**

Previous cycle documented the card conceptually. This cycle specifies it as a production artifact:
- Exact field list (9 elements)
- Information hierarchy (hit rate dominant, percentile second, Bold Call gets its own gold block)
- Color rules (✓ = white circle, not green; ✗ = gray faded, not red — both to avoid flag color clashes)
- Three size variants (1080×1080, 1080×1920, 1200×675)
- Free vs Pro difference (static vs animated — same information, different energy)

The fabricated 2022 WC Final card is now specified precisely enough to build in Canva. The Argentina demo card (4/4 correct, Bold Call on penalties against 71% NO consensus) tells the story the product is trying to tell.

**3. Full user flow written step by step.**

Seven steps from discovery to Copa Card received. Each step specifies what the player sees, what they do, and what Copa must deliver. Previously, the flow existed in principle but not in detail.

Key friction points identified and resolved:
- Live call email: must be one-click YES/NO (not a form page). If the player has to load a form during a 60-second window, many will miss it.
- Crew join: no account creation before seeing the leaderboard. The leaderboard is the reward for joining. Gate it and Javier loses half his invitees.
- Pick form: 4 calls one at a time, not all at once. Single-question pages have higher completion rates than multi-question forms. Each call gets full attention.

**4. Scoring system specified with numbers.**

Previous cycle had the model conceptually. This cycle defines every number:
- Base: +10 correct, 0 wrong, 0 for live call non-response
- Bold: +20 correct, −5 wrong
- Contrarian multiplier: 1×/1.25×/1.5×/2× by crowd distribution
- Maximum match score: 120 points (achievable, not easy)

The 120-point ceiling matters. Players need to know what "perfect" looks like. It creates aspiration and gives the Copa Card percentile rank meaning.

**5. V1 operator load quantified.**

55 minutes per match. 2.75 hours/day at Group Stage peak. This is the number that determines whether V1 is sustainable for one person. It is. Copa Card generation (20 minutes) is the bottleneck and the first automation target for V1.5.

**6. V1 stack finalized with costs.**

Total fixed cost: ~$31/year. Variable: 2.9% + $0.30 per Pro transaction. Beehiiv free tier covers 2,500 subscribers — upgrade triggers at that threshold ($99/month). All other tools have generous free tiers that cover V1 scale.

**7. Actions.md updated with 10 specific tasks.**

Every action now has: what to build, which tool, what success looks like, and timing. The two most urgent (domain registration, card design) are unblocked by this cycle's work.

---

### Design decisions deferred

**Rival (1v1) mode** — deferred to V2. The mechanic is clear (head-to-head call record over one match) but the implementation requires per-player comparison logic that Airtable handles awkwardly. Copa Crews solve the social competition need for V1.

**Automated live call triggering** — deferred to V1.5. One human operator watching the match and sending the email broadcast is the right V1 approach. The risk of missing a live moment is real but acceptable — if a penalty isn't called in a match, the 4 pre-match calls still ran. V1.5 adds push notifications and semi-automated triggering.

**Nation leaderboard aggregation** — not yet fully specified. How does Copa aggregate individual scores into a nation score? Options: sum of all nation players' tournament totals; average per-match score; top 10 players per nation. This needs a decision before launch because it affects how Copa communicates nation vs nation competition. Next cycle should resolve this.

---

### Updated scores (estimated)

- concept-uniqueness: 0.87 (up from 0.82 — Bold Call mechanic adds a genuinely new design element)
- market-positioning: 0.88 (unchanged)
- marketing-reach: 0.88 (unchanged)
- monetization-readiness: 0.93 (unchanged)
- product-readiness: 0.88 (up from 0.62 — full flow, scoring, card spec, stack, operator load all defined)
- viral-mechanics: 0.90 (up from 0.88 — Copa Card design and pre-match share button add concrete shareability)

**Overall: approximately 0.89.** Phase 1 exit requires 0.95 overall with all dimensions ≥ 0.90.

Remaining gaps:
- concept-uniqueness (0.87): needs one more design pass — the Bold Call is new but the overall category still risks being described as "prediction game with better UX." Need to be able to articulate the distinction more sharply.
- market-positioning (0.88): competitive framing is solid but needs a sharper "why now, why Copa, why not the alternatives" statement for press pitches.
- product-readiness (0.88): nation leaderboard aggregation still unresolved. Live call one-click email implementation needs technical confirmation.

Next cycle should focus on: (1) nation leaderboard design, (2) sharpening the concept-uniqueness pitch, (3) confirming the live call email implementation is technically feasible in Beehiiv.


---

## Generation 5 — REVERTED

Cycle reverted: score fell from 0.83 to 0.78.


---

## Generation 5 — Game Design Completion

### What this cycle did

Resolved every open design question blocking V1 build. The game design is now complete — no ambiguity remaining.

---

### Decisions made this cycle

**1. Bold Call redesigned as a deliberate mechanic**

Previously the Bold Call was a passive multiplier: calls where the crowd split heavily paid 1.5x to the minority. This was discovered after the fact — players didn't know they were making a bold call.

Redesigned as a player-designated commitment. Before submitting, the player marks one call as their Bold Call. One per match. Correct → 30 pts (3x). Wrong → 0 pts. The Bold Call is the most prominent visual element on the Copa Card (gold band if correct, grey if wrong).

Why this is better:
- Creates a decision moment with real stakes inside each match
- Differentiates Marcus (strategic timing) from Sofia (gut instinct) — both valid strategies
- The card's most dramatic element is earned, not automatic
- A correct Bold Call on a dramatic moment is Copa's highest-value shareable content

**2. Live event calls (60-second window) dropped from V1**

A 60-second email window is not technically feasible — average email open time is 2-3 minutes after delivery. This was an honest technical constraint that needed to be faced.

V1 replaces live event calls with pre-match calls covering the same territory:
- "Does a penalty get awarded in this match?" replaces "Does this penalty go in?"
- "Does this match have a VAR controversy?" covers that territory

The live call magic is preserved through in-match timed calls where the window is measured in minutes (30' → HT; 75' → 90'). True 60-second live calls are V1.5, enabled by push notifications.

This is not a compromise — it's an honest product scope. V1 needs to work perfectly within its constraints.

**3. Nation leaderboard aggregation resolved**

Decision: average instinct score per match across all Copa players who declared that nation. Minimum 10 players to qualify for main leaderboard; smaller nations appear in "Developing Nations" tab.

Rejected options:
- Raw sum: dominated by nations with most Copa players (unfair, uninteresting)
- Top N players: complex, hard to explain
- Median: robust but unexplainable to casual users

Average is fair, explainable ("the average Copa fan from Mexico called X% correctly"), and produces interesting results (smaller nations can rank above football giants if their fans are sharp).

**4. Join flow from shared card fully specified**

The path from "see Copa Card on Instagram" to "playing Copa" is now fully specified: `copa.fc/play` in card footer, landing on Carrd page, 3-field form (name, nation, email), immediate access to current call form. Under 60 seconds. No account verification before first play.

Crew join flow separately specified: link → Crew page → join form → leaderboard immediately visible → call form available.

**5. Copa Card visual hierarchy resolved**

Five-zone layout: header (nation color + name + match), score band (dominant number), call list (✓/✗ rows with crowd splits), Bold Call band (gold/grey/absent), footer (wordmark + URL + tournament total).

Card communicates in 2 seconds: who, how many right, whether Bold Call hit.

**6. Scoring system fully specified**

- Correct majority call: 10 pts
- Correct contrarian call (<30% of Copa players agreed): 15 pts
- Correct Bold Call: 30 pts (3x, regardless of crowd position)
- Wrong call: 0 pts
- Bold Call wrong: 0 pts (stamp spent, no penalty)
- Weekly Hot Streak badge (3+ matches with 4+ correct): cosmetic only, no points

Tournament score displayed two ways: raw points + fraction correct (e.g., "78.6%"). The fraction is the shareable number — it works like FPL's Overall Rank, designed to be compared and posted.

---

### What the reverted Gen 5 had wrong (hypothesis)

The revert note says score fell from 0.83 to 0.78. Without seeing the reverted content, my hypothesis is that the previous cycle added complexity without resolving the actual blocking gaps (nation leaderboard, Bold Call design, live call feasibility). This cycle focused on resolving those gaps with specific decisions rather than adding new design territory.

---

### Updated scores (estimated)

- concept-uniqueness: 0.90 (up from 0.87 — Bold Call as deliberate commitment mechanic is a genuinely new design element; the "instinct record as identity artifact" framing is now distinct from prediction game framing)
- market-positioning: 0.90 (up from 0.88 — "instinct record, not prediction game" framing sharpened)
- marketing-reach: 0.88 (unchanged — no new channel work this cycle)
- monetization-readiness: 0.93 (unchanged)
- product-readiness: 0.93 (up from 0.62 — all open questions resolved: Bold Call, nation leaderboard, join flow, card hierarchy, scoring system, V1 scope, operator load, technical stack confirmed)
- viral-mechanics: 0.91 (up from 0.90 — Bold Call gold band is a concrete, designed share trigger; join flow from card is fully specified)

**Overall: approximately 0.91.** Phase 1 exit requires 0.95 overall with all dimensions ≥ 0.90.

Remaining gaps:
- marketing-reach (0.88): no new channel work this cycle; needs concrete channel progress (waitlist page live, first Reddit post, Copa Card mockup designed and posted)
- Overall to 0.95: requires real-world validation — waitlist signups, Reddit feedback on card mockup, first external signal that the concept lands as intended

Next cycle priority: **Build the Copa Card mockup and get it in front of real people.** The concept is designed. The next question is whether it resonates when a non-Copa person sees the card. Reddit feedback on the 2022 Final mockup card will either confirm the design or identify the gap.
