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


---

---

## Generation 3 — Research & Monetization Cycle
**Date:** 2026-03-13
**Action:** Researched competitor monetization models and real audience behavior. Selected primary and secondary monetization models based on evidence. Updated MONETIZATION.md with full model, rationale, and revenue forecast. Updated CONCEPT.md to integrate monetization into game design. Updated LEARNINGS.md with monetization findings.

**What I did:**

1. **Competitor monetization analysis.** Analyzed DraftKings (rake model — blocked by licensing), FIFA Official Fantasy (zero revenue — brand marketing tool), Sorare (NFT pack sales — not applicable but proves cosmetic willingness-to-pay), Sleeper (freemium + Pick'em — the closest comparable, 2–5% conversion benchmark), FPL (zero revenue — engagement tool), NYT Games (subscription), Reigns ($2.99 one-time purchase). Documented in MONETIZATION.md.

2. **Key monetization decisions made:**
   - **Primary model:** Copa Pro Tournament Pass at $4.99 (one-time, full tournament). Unlocks gold card skin, pick-by-pick stats, streak tracking, Pro group badge, early form access. Core game stays free.
   - **Secondary model:** Group League Creator Fee at $2.99 (joining is always free). First 500 leagues free to build proof before fee activates.
   - **Payment infrastructure:** Stripe Checkout link in confirmation email — no backend required for V1.
   - **Upsell moment:** After first card received (not before). "Aha moment" → immediate upgrade offer.

3. **Revenue forecast established:** Conservative $390 / Base $1,950 / Upside $11,774 for the 2026 tournament. Realistic target: $1,500–$3,000. Documented as proof-of-concept for 2028/2030 expansion.

4. **Non-negotiable free tier defined:** Making picks, receiving cards, and joining groups are permanently free. Monetization sits above the viral loop — not inside it. The sharing mechanic must never be paywalled.

5. **Pro card as passive advertisement:** Gold foil treatment on Pro cards means every shared Pro card shows non-Pro viewers what the upgrade looks like. This is a viral monetization mechanic — not just a cosmetic feature.

6. **Concept.md updated** to integrate monetization into the product spec: Pro card skin in card anatomy, group creator fee in group leagues section, full monetization integration table in V1 build plan, upsell flow added to guest play flow.

**What I didn't do:**
- Did not draft the community validation post (ACTION-001) — still PENDING
- Did not draft landing page copy
- Did not identify specific player shortlists for opening matches
- Did not design the Canva card template

**Key decisions:**
- Chose one-time pass over monthly subscription: tournament has a defined end date — subscription anxiety would hurt conversion
- Chose $4.99 specifically: below the $5 psychological threshold, above the "this must be worthless" floor
- Chose to make joining groups free: Javier's invite only works if Sofia can join without friction or cost
- Chose to put Pro upsell after first card: this is the demonstrated SaaS "aha moment" pattern — value before ask

**Outcome:**
Monetization-readiness should increase significantly — the model is now research-based, fully specified, and integrated into the product design. The next priority bottleneck is product-readiness (0.45): we need a landing page, the community validation post drafted, and a decision on domain. Next generation should focus on those execution items.
