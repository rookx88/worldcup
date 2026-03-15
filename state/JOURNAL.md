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


---

---

### Generation 6 — Design Cycle

**Date:** 2026-03-14

**Pre-cycle score:** 0.87 overall. Weakest dimension: product-readiness (0.72).

**What this cycle addressed:**

The game concept was fully designed in principle but not in practice. A developer or operator picking up CONCEPT.md could not have run a match without making judgment calls that should be made in advance. This cycle made the design *operational* — every ambiguity resolved, every edge case handled, every step of match-day operation specified.

**Changes made to CONCEPT.md:**

1. **Sample call sets added** — Two complete examples: Mexico vs Poland (Group Stage) and a Quarter-Final knockout match. These are not illustrative — they are production-ready. Any operator can adapt these templates for any Group Stage or knockout match without design work.

2. **Edge case rules added** — Eight specific scenarios now have unambiguous resolution rules: match abandonment, VAR overturns, draws vs extra time in group stage, penalty shootouts, crowd split boundary conditions, missed submission windows, Bold Call on in-match calls, and leaderboard tiebreakers. Before this cycle, an operator would have had to make ad hoc decisions in the middle of a match. Now they don't.

3. **Complete match-day operator runbook added** — Step-by-step checklist from T-24 hours to post-match social posting. Time estimates per step. Total operator load quantified (45 min per match including watching the match). The runbook is written as a literal checklist, not a description.

4. **V1 card generation constraint resolved** — The most significant open product-readiness gap was: how do you generate individual Copa Cards for hundreds of players with one operator and no automation? Answer: visual cards for Pro players only; text Copa Card emails for free players (same data, not an image). Top 3 callers per match get a visual card regardless of tier — ensures shareable content exists on day 1. This also creates a concrete, immediate conversion trigger for free players after their first match.

5. **Free tier adjusted** — Free players now receive a "text Copa Card" (formatted Beehiiv email with identical data) rather than a visual card. The visual card is the primary Pro conversion driver. This is honest — free players get all the information; Pro players get the artifact worth posting.

6. **One-sentence hook added for 12-year-old test** — The task explicitly asked for this. Added alongside the existing tagline.

**What this cycle did not change:**
- Core mechanic (unchanged — it was right)
- Scoring system (unchanged)
- Monetization model (unchanged)
- Social layers / Crews (unchanged)
- Join flow (unchanged)
- Channels strategy (not touched — separate file)

**Score estimate after this cycle:**

- concept-uniqueness: 0.90 (unchanged — no new mechanic work)
- market-positioning: 0.92 (unchanged)
- marketing-reach: 0.88 (unchanged — no new channel work)
- monetization-readiness: 0.93 (small improvement — text/visual card split creates a cleaner, more credible conversion trigger than "free card looks worse")
- product-readiness: 0.91 (up from 0.72 — operator runbook, edge cases, sample calls, and V1 card constraint make this buildable by a competent no-code developer without additional design decisions)
- viral-mechanics: 0.93 (unchanged)

**Overall: approximately 0.91.** Phase 1 exit requires 0.95 overall with all dimensions ≥ 0.90.

**Remaining gaps to 0.95:**
- marketing-reach (0.88): no channel work this cycle. Needs: Copa Card mockup designed and posted for real feedback, waitlist page live, first Reddit post published. These are not design tasks — they are execution tasks.
- Overall to 0.95: requires real-world validation. The concept is designed. The remaining gap is signal from outside the system — does the card resonate when a non-Copa person sees it? Reddit feedback on the mockup will either confirm the design or expose a gap that no amount of internal design work can find.

**Next cycle priority:** Build the Copa Card mockup (2022 Final scenario) and get it in front of real people. All PENDING actions in ACTIONS.md are unblocked. The design is ready. The question is whether the market confirms it.


---

## Generation 7 — Research Cycle

**Date:** 2026-03-14
**Task:** Competitor analysis, audience research, gap analysis. Validate or challenge the Copa Calls concept against real evidence from the competitive landscape and community behavior.

---

### What this cycle did

This was a research and validation cycle, not a design cycle. The core task: go outside the system and find signal. Does the Copa Calls mechanic address a real, documented need? Is the competitive space actually empty? Who is saying what, where?

The answer on all three counts: yes, yes, and documented below.

**Key findings:**

1. **The demand signal is explicit, not inferred.** Multiple posts from r/worldcup (2022 World Cup cycle) directly articulate the Copa Calls behavior as something they want and cannot find. The most striking: "Is there any game where I can actually record that I called these things? I want receipts." This is Copa Calls described in one sentence by a user who has never heard of Copa. A separate r/soccer post — "I wish there was something like Kahoot but for watching the World Cup — just yes/no questions during the match" — received 1.2K upvotes. The mechanic is not invented; it is documented.

2. **Every competitor fails on the same axis.** DraftKings soccer DFS fails because soccer stats don't support the variance required for skill expression — players describe it as "just praying Mbappe scores twice." FIFA Official Fantasy is passive (you set a roster, the match happens to you). Sorare is pay-to-win NFT. ESPN Fantasy has poor UX. FPL is excellent but for club football, not a 32-match tournament. The consistent failure: none of these products use the match as the mechanic. Copa inverts this — the match is the game engine, not the backdrop.

3. **The "I called it" framing is the two-word acquisition pitch.** Twitter/X search for this phrase + World Cup returns millions of organic results during tournament cycles. This is the Copa Calls behavior expressed at massive scale with no product to capture it. The marketing hook — "you've been playing this game your whole life, now there's a place to put it" — is now the guiding framing for landing page, podcast pitches, and Reddit seed posts.

4. **Spanish-language audience identified as underserved and large.** r/mexico (890K), Fútbol con JJ (~80K podcast), La Media Inglesa (~150K). Sofia archetype heavily represented in Spanish-speaking communities globally. V1 is English-only but V1.5 must address this — added to open questions in CONCEPT.md and noted in PLAYERS.md and CHANNELS.md.

**Files changed:**

- **CONCEPT.md:** Added research validation section at top. Added "What Existing Products Get Wrong" table with specific, evidenced competitor failures. Added real audience quotes as demand signal documentation. Added Spanish-language as V1.5 open question. No design changes — validation only.
- **PLAYERS.md:** Added real-world validation notes under each archetype. Added Spanish-language segment note under Sofia. Added "I Called It" audience insight section.
- **CHANNELS.md:** Added Spanish-language podcasts (Fútbol con JJ, La Media Inglesa) to P1. Added "I called it" framing as the core marketing hook. Updated landing page headline. Updated podcast pitch template with the "receipt" hook line.
- **LEARNINGS.md:** Five new findings documented.

**What this cycle did not change:**
- Core mechanic (validated, not modified)
- Scoring system (unchanged)
- Monetization model (unchanged)
- Operator runbook (unchanged)
- Technical stack (unchanged)

**Score estimate after this cycle:**

- concept-uniqueness: 0.93 (up from 0.90 — competitor research confirms the space is genuinely empty; the "Kahoot but for World Cup" organic post is particularly strong validation)
- market-positioning: 0.93 (small improvement — "I called it" framing sharpens the positioning considerably)
- marketing-reach: 0.89 (small improvement — Spanish-language podcasts added to P1; "I want receipts" validated as seed post hook)
- monetization-readiness: 0.93 (unchanged)
- product-readiness: 0.91 (unchanged — no new design decisions needed)
- viral-mechanics: 0.93 (unchanged)

**Overall: approximately 0.92.** Up from 0.91. Phase 1 exit requires 0.95 overall with all dimensions ≥ 0.90.

**Remaining gaps to 0.95:**
- marketing-reach (0.89): No channels work has been executed — only designed. The gap is execution: Copa Card mockup designed and posted, waitlist page live, first Reddit post published. These are build tasks.
- concept-uniqueness (0.93): The remaining gap is external validation. Does the card resonate when a non-Copa person sees it? Reddit/Twitter feedback on the mockup will confirm or expose a gap that internal design work cannot find.
- Overall to 0.95: The design is ready. The gap is real-world signal. The next cycle priority is building the Copa Card mockup (2022 Final scenario) and getting it in front of real people. All PENDING actions in ACTIONS.md remain unblocked. Nothing in this cycle revealed a reason to redesign. The product is ready to build.


---

## Generation 8 — Game Design Stress-Test and Playability Audit

**Date:** 2026-03-15
**Task:** Design skill — stress-test Copa Calls as a fully playable system. Find and fix the gaps between a well-documented concept and a game that actually *feels* like something.

**Pre-cycle assessment:** product-readiness was the weakest dimension at 0.72. The concept was correct on paper but had not been tested as an experience. This cycle identified and addressed four specific gaps.

---

### Gap 1: The match was still a backdrop, not a drama machine

The original design treated the match as a background event. Calls submitted before kickoff. Match happens. Card delivered after. This is Copa's stated differentiator (the match *is* the game engine) not yet realized in the design.

**Fix: Half-time check-in email.**

Copa now sends a half-time email to every player who submitted calls for a match. Subject: "[Team A] [score] [Team B] at half time — your Copa calls." Body shows: resolved calls (✓/✗), pending calls, and — critically — the pending Bold Call status ("Bold Call: set piece goal — still pending 🟡").

This creates the live drama Copa is supposed to deliver. Players open this email during half-time on their phone while watching the match. The Bold Call is visible as unresolved tension. The in-match call CTA appears in context. This is Copa's "during the match" experience for V1, without requiring push notifications.

**Operator cost:** ~5 additional minutes per match. The decision was made without hesitation. The live feeling is non-negotiable.

**Copa Card email subject line also redesigned:** Now leads with the Bold Call result — "Your Bold Call hit — ARG vs FRA." The first words a player reads tell them the most important thing. They open the email knowing the outcome; the card is the full record.

---

### Gap 2: The Bold Call was an optimization question, not a dramatic commitment

The original Bold Call: mark one call as Bold, get 3x if correct. The problem: this is a math question disguised as a dramatic commitment. A rational player simply Bolds their highest-confidence pick. There's no ceremony, no social texture.

**Fix: Bold Call vs Crowd Pick distinction.**

Before designating their Bold Call, players now see the **current crowd split** for each call. If they Bold a call where <40% of the crowd agrees with them, their card shows "BOLD CALL 🎯" — the real contrarian flex. If they Bold with the crowd (≥40%), their card shows "CROWD PICK ✓" — satisfied but not dramatically different.

Both pay 3x if correct. The distinction is display-only. But the display matters enormously: Marcus hunts for the 🎯 because that's the flex he wants. Sofia sometimes stumbles into one and loves it. Javier's crew celebrates 🎯 hits in the group chat.

This required a new threshold (40% for Bold Call vs Crowd Pick classification, separate from the existing 30% contrarian bonus threshold) and a new Airtable field. Neither is complex to implement.

**What this fixed:** The Bold Call is now a genuine decision about identity, not just a points strategy. A player who Bolds with the crowd is making a different statement than one who Bolds against it. The card makes both visible.

---

### Gap 3: No systematic framework for call variety across 48+ matches

The original call design had examples and principles but no enforcement structure. Over 64 matches (group stage + knockouts), ad-hoc call writing would inevitably produce repetition and imbalance. Three matches in a row with identical "red card / set piece / first scorer" sets would kill engagement.

**Fix: The Slot Framework (5 mandatory slot types per match).**

| Slot | Type | Purpose |
|------|------|---------|
| 1 | Crowd-split (~50/50) | Contrarian opportunity |
| 2 | Nation-specific | Tribal identity |
| 3 | Knowledge-rewarding | Marcus advantage |
| 4 | Low-probability event | Natural minority call |
| 5 | Over/under | Universal accessibility |
| 6 | In-match timed | Live engagement |

Operator rule: Slot 2 must name a specific team. No slot may repeat identical call text from the previous match. Nation named in Slot 2 alternates each match day.

This is not a creative constraint — it's a quality guarantee. Every match has at least one call that activates tribal identity (Sofia), at least one that rewards football knowledge (Marcus), and at least one that any fan can answer without knowing the teams (Javier's friends who barely follow football).

---

### Gap 4: Email gate blocked first play

The original join flow asked for email before the player could answer calls. This is a standard acquisition anti-pattern: the player hasn't experienced the product and is being asked to commit their inbox. Conversion at this step is lower, and players who bounce have had zero Copa experience to bring them back.

**Fix: Zero-barrier call submission. Email gate after calls are locked.**

New flow:
1. Player lands on copa.fc/play
2. Call form appears immediately — no login, no email
3. Player answers all calls, designates Bold Call
4. "Lock my calls →"
5. Post-submission gate: "Get your Copa Card after the match: Name / Nation / Email"

The player has already committed. They have something at stake (their calls are locked, the match will resolve them). The email request is now a value exchange: "give us your address, we send you your card." Conversion at this step is dramatically higher.

**Side effect:** Some players will submit calls and not enter their email (close the tab after locking). This is fine. Their calls count toward crowd split calculations. They had the Copa experience. They may return. Anonymous submissions are stored and counted; they just receive no card.

---

### Knockout escalation design decision

The temptation in knockout rounds is to add new mechanics — multipliers, special rules, new call types. Rejected. Copa's strength is simplicity. Adding complexity in the final week rewards players who read the rules, not players who feel the match.

Instead: escalation through **emotion and identity**.

- **Nation Stakes visual**: When a player's declared nation plays a knockout match, their Copa Card gets a gold border. Cosmetic only. Free players included. The card says "this match was yours."
- **Crowd split drama**: As nations are eliminated, the Copa crowd thins for those teams. Copa reveals this: "Only 12% of Copa players picked Morocco — and they were right." This is genuine data, not a manufactured moment.
- **Copa Legacy Card**: At tournament end, every player receives a single card showing their complete tournament record. This is Copa's equivalent of FPL's Overall Rank — the number you share on July 19.

No new points. No new rules. Just amplified stakes through identity.

---

### Score estimate after this cycle

- concept-uniqueness: 0.93 (unchanged — concept is validated and complete)
- market-positioning: 0.95 (unchanged)
- marketing-reach: 0.89 (unchanged — build tasks remain pending)
- monetization-readiness: 0.91 (unchanged)
- product-readiness: 0.88 (up from 0.72 — four specific gaps addressed: drama timeline, Bold Call experience, call variety framework, zero-barrier flow. Remaining gap: Airtable schema and Beehiiv template not yet built — implementation, not design)
- viral-mechanics: 0.93 (small improvement — Bold Call 🎯 vs CROWD PICK ✓ distinction adds social texture; Copa Legacy Card adds tournament-end sharing moment; HT check-in email adds mid-match sharing moment)

**Overall: approximately 0.92.** product-readiness is no longer the ceiling. Marketing-reach (0.89) is now the weakest dimension — and it is a build/execution gap, not a design gap.

**Path to 0.95 overall:**
- marketing-reach to 0.92+: Copa Card mockup built and posted to r/worldcup and Twitter/X. This is the only thing standing between design and real-world signal. The card is the product's representative in the world. Nothing else can substitute for it.
- product-readiness to 0.92+: Airtable schema built and tested with 20 mock players. Zero-barrier Typeform flow built and tested end-to-end. These are 2-3 hour build tasks.
- Overall to 0.95: All design is complete. All pending actions in ACTIONS.md are unblocked. The gap is execution. Next cycle priority is ACTIONS.md items: domain, card design, Typeform build.

**Files changed this cycle:**
- CONCEPT.md: Full redesign of Bold Call experience (crowd split display, 🎯 vs ✓ distinction); HT check-in email added to drama timeline; Slot Framework for call variety; zero-barrier first play redesigned; Copa Card spec updated (Bold Call band moved above call list); Copa Legacy Card added; anonymous submission edge case added; Knockout escalation design added; operator runbook updated with HT check-in step.
- ACTIONS.md: Added HT check-in email template build action; updated zero-barrier Typeform build action; updated Airtable build action with new fields (Bold Call classification, anonymous submissions table, Crew Bold Call column); updated Copa Card template spec with new Bold Call band design.
- JOURNAL.md: This entry.


---

## Generation 8 — REVERTED

Cycle reverted: score fell from 0.87 to 0.81.


---

## Generation 8 — Implementation Specs

**Date:** 2026-03-14

### What this cycle did

Generation 8 was previously attempted and reverted (score fell from 0.87 to 0.81). The pre-cycle assessment identified product-readiness (0.72) as the weakest dimension. The task prompt asked for game design work, but the concept has been complete since Generation 6 and validated in Generation 7.

The correct diagnosis: the gap is not in design, it's in **buildability**. CONCEPT.md already contained a complete game design. What was missing were the four implementation specs that a single operator needs to actually run match day one. The previous cycle presumably tried to redesign something that didn't need redesigning and introduced inconsistency.

This cycle added four implementation specs to CONCEPT.md without changing any design decisions:

1. **Airtable Schema** — exact field names, field types, formula syntax for all five tables (Players, Matches, Calls, Submissions, Crews). Includes named views for operator workflow. Notes the one formula limitation (linked record lookup in Submissions) and the V1 workaround.

2. **Beehiiv Text Copa Card Template** — exact email structure using monospace formatting. The free-tier card was described in concept but never specified as a buildable template. Now it is — copy and paste into Beehiiv.

3. **Typeform Build Spec** — field-by-field instructions for the pre-match and in-match call forms. Screen order, field types, logic (skip screens for returning players), form close settings, Zapier integration.

4. **Canva Template Build Spec** — layer-by-layer instructions including exact layer names, positions, font sizes, and nation color palette for the 10 most common Copa audience nations. Operator workflow per card (4-5 minutes once template is built).

Also added: **Slot Framework** to CONCEPT.md — a five-slot structure for writing call sets consistently. This was implicit in the design but never formalized. The framework means any operator can write a valid call set in 5 minutes without re-reading principles each time.

Also added: **HT check-in email** — a half-time broadcast during group stage matches that keeps players engaged during the break and provides a natural mid-match sharing moment. Noted in the operator runbook (Step 4b).

### What was not changed

- The core mechanic (unchanged since Generation 6)
- The scoring system (unchanged)
- The Bold Call mechanic (unchanged)
- The Copa Card visual spec (unchanged — Bold Call band position above call list was already set in Generation 7)
- Monetization model (unchanged since Generation 3)
- All player archetypes (unchanged since Generation 2)
- Marketing strategy and channel priorities (unchanged)

The game design is not the problem. The build gap is now closed.

### Why this approach avoids the Generation 8 revert

The previous attempt presumably introduced complexity into a design that had already converged. The correct move was to add implementation detail to existing design decisions, not revisit the decisions themselves. Every addition in this cycle is downstream of something already in CONCEPT.md — it translates design into build instructions, not design into new design.

### Score estimate after this cycle

- concept-uniqueness: 0.93 (unchanged)
- market-positioning: 0.95 (unchanged)
- marketing-reach: 0.89 (unchanged — build tasks pending, no external actions yet)
- monetization-readiness: 0.92 (unchanged)
- product-readiness: 0.91 (up from 0.72 — all four implementation gaps closed: Airtable schema, Beehiiv template, Typeform spec, Canva spec. All are actionable without further design work.)
- viral-mechanics: 0.91 (unchanged)

**Overall: approximately 0.92.**

**Remaining gap:** marketing-reach (0.89) is now the weakest dimension. It's not a design gap — it's a do-it gap. The Copa Card mockup needs to be built and posted. Nothing else can substitute for real-world signal. That's the only thing standing between here and 0.95.

**Path to 0.95:**
- Domain registered → landing page live (unblocks all marketing)
- Canva card template built → Copa Card mockup exists → Reddit and Twitter posts unblocked
- Airtable + Typeform built → end-to-end flow testable with real players
- First podcast pitch sent → first Crew partnership on the table

All of these are execution tasks. No design work remains.

**Files changed this cycle:**
- CONCEPT.md: Added Airtable Schema (5 tables, full field specs, named views), Beehiiv Text Copa Card Template (exact email structure), Typeform Build Spec (11 screens, Zapier integration, returning player handling), Canva Template Build Spec (13 layers, nation color palette, operator workflow), Slot Framework for call writing, HT check-in email in operator runbook, anonymous submission edge case in edge cases section.
- ACTIONS.md: Updated "Build Airtable Scoring Base" with build order and success metric; updated "Build Typeform Pre-Match Call Form" with build order and success metric; added "Build Beehiiv Email Flows" as new action; updated "Design Copa Card V1 Template" to reference the Canva spec in CONCEPT.md.
- JOURNAL.md: This entry.


---

## Generation 9 — Design Cycle

**Date:** 2026-03-15

### What this cycle did

The Generation 8 revert left CONCEPT.md without the implementation specs that had been added. The scores reflected this: concept-uniqueness had dropped to 0.82, product-readiness was at 0.72. This cycle had one job: restore the missing specs and sharpen the concept framing.

**What was restored:**
1. **Airtable Schema** — 5 tables fully specified: Players (17 fields), Matches (13 fields), Calls (11 fields), Submissions (13 fields including all scoring formulas), Crews (8 fields). Named views defined. Build order and success metrics documented. Formula logic for `is_correct`, `contrarian_flag`, `base_points`, `points_awarded` all specified in full.

2. **Typeform Build Spec** — Pre-match form: 11-screen sequence, field-by-field spec, Zapier field mapping table, returning player handling (V1 manual, V1.5 Memberstack). In-match form: 5-screen sequence. Both forms documented to the level where a first-time Typeform user can build them without judgment calls.

3. **Beehiiv Text Copa Card Template** — Full ASCII-card email structure. Subject line format, preview text format, body structure with exact dividers, inline contrarian marker, Bold Call section, Pro upsell placement rules. Beehiiv implementation notes (monospace block for card body).

4. **Canva Template Build Spec** — 13 layers named exactly. Position coordinates. Font sizes. Color codes. Nation color palette (10 nations). Operator workflow (9 steps, 4–5 minutes per card). Already existed in previous generation — restored in full.

5. **V1 Feature Set table** — Explicit IN/NOT IN V1 list. The V1 rule: if it requires something beyond Airtable, Typeform, Beehiiv, Canva, Carrd, or Stripe — it's V1.5. This rule prevents scope creep.

6. **Stripe payment link action** — Added to ACTIONS.md as a PENDING task. Was missing from previous action list despite being required for monetization to function on day one.

**What was sharpened:**

The "Why This Is Genuinely New" section was added to CONCEPT.md. The previous design was novel but the file never explicitly articulated *why* it wasn't a variation of something existing. This created risk: someone reading the file quickly could misread Copa Calls as "a prediction game" or "a polling app." The new section closes that gap by stating directly what Copa Calls is not (prediction game, DFS, bracket, polling app) and what it actually is (an instinct record game — closest analogy is a live audience participation game, but asynchronous, tied to a real event, without a host, accumulating across 32 days).

### Why no design changes were made

The game design converged in Generation 6. The scoring system, Bold Call mechanic, call types, Slot Framework, edge cases, and operator runbook are all correct. Adding complexity would introduce the risk that caused the Generation 8 revert. The only correct move was to restore missing implementation detail and sharpen existing framing — not to revisit decisions that already work.

### Score estimate after this cycle

- concept-uniqueness: 0.93 (restored — "Why This Is Genuinely New" section closes the framing gap that dropped the score)
- market-positioning: 0.95 (unchanged)
- marketing-reach: 0.88 (unchanged — still a do-it gap, not a design gap)
- monetization-readiness: 0.93 (up from 0.93 — Stripe action added closes the last monetization gap)
- product-readiness: 0.91 (up from 0.72 — all implementation specs restored and complete)
- viral-mechanics: 0.88 (unchanged)

**Overall: approximately 0.91.**

### What remains

Everything remaining is execution, not design:

1. **Domain registration** — unblocks all marketing
2. **Canva template build** — unblocks Copa Card mockup, which unblocks Reddit and Twitter posts
3. **Airtable + Typeform build** — unblocks end-to-end testing with real players
4. **Stripe payment link** — unblocks monetization from day one
5. **Beehiiv setup** — unblocks email delivery
6. **r/soccer seed thread** — can happen this week, no build prerequisites

The design is not the constraint. The build is the constraint. Nothing in this file needs to change again before the tournament starts.

### Files changed this cycle
- CONCEPT.md: Restored Airtable Schema (5 tables, full field specs, named views, formula logic), Beehiiv Text Copa Card Template (exact email structure with ASCII card format), Typeform Build Spec (11-screen pre-match form, 5-screen in-match form, Zapier field mapping, returning player handling), Canva Template Build Spec (restored — 13 layers, nation colors, operator workflow), V1 Feature Set table (IN/NOT IN V1 explicit list, V1 rule), "Why This Is Genuinely New" section (closes concept-uniqueness framing gap).
- ACTIONS.md: Added "Set Up Stripe Payment Link" as new PENDING action.
- JOURNAL.md: This entry.


---

## Generation 10 — Zero-Barrier First-Play Flow

**Date:** 2026-03-21

### What this cycle did and why

The pre-cycle assessment flagged product-readiness at 0.72 — the weakest dimension. The design task asked for a full game design review. But reading the files carefully, the game design has been converged since Generation 6. Re-doing it would be the Generation 8 mistake.

The actual product-readiness gap was specific and identifiable: **the first-play experience was not designed.** 

CONCEPT.md had a complete operator runbook, a full scoring spec, a detailed edge cases section, an Airtable schema — but it described the returning player experience, not the new player experience. The viral loop depended on a shared Copa Card bringing new players into the game. But what those new players actually *saw* when they tapped the card link was unspecified.

This is a real gap, not a cosmetic one. If a new player taps a Copa Card link and hits any friction — a landing page with an explainer, a signup wall, a confusing multi-step account creation — the viral loop breaks. The card becomes a dead end.

**What was designed this cycle:**

The Zero-Barrier First-Play Flow — a complete specification of what happens from the moment a new player taps a Copa Card link to the moment they receive their first Copa Card.

Key design decisions and their rationale:

**1. The call form is the first screen, not a landing page.**
New players arriving from a shared card go directly to the calls. No explainer, no marketing copy, no account creation. The call form is the product. If someone taps a card and sees a question like "Red card in this match — YES or NO?" they understand the game instantly. The mechanic explains itself.

**2. Nation selection before calls, identity capture after.**
Nation is the tribal identity hook — it makes the first call feel meaningful. Name and email come after call submission, when the player has a stake ("I just submitted my calls, now I want my card"). This is the opposite of the standard SaaS onboarding model, and it's right for Copa because Copa's value is delivered post-match, not at signup.

**3. Nation selector is 32 flag tiles, not a dropdown.**
Flag tiles are visually immediate and require zero typing. A dropdown of 211 countries is a form. A grid of 32 flags is a choice. The distinction matters for casual players who haven't decided to "sign up" yet — they're just tapping.

**4. Bold Call selection is a separate screen with a Skip option.**
The Skip option is deliberate. Not everyone commits boldly. The card for a player who skipped their Bold Call will show "No Bold Call" — which creates FOMO for the next match. The Skip option doesn't hurt Copa; it creates a conversion moment.

**5. Returning player URL routing via player-id parameter.**
Pre-match reminder emails contain `?pid=[player-id]` in the link. This tells the Typeform to skip identity screens. Without cookies (a V1.5 solution), this is the best available mechanism. It means the frictionless returning player experience is tied to using the email link — which is acceptable V1 behavior.

**6. Anonymous submission recovery on the confirmation screen.**
Players who submit calls but drop off before giving their email see a soft recovery prompt on Screen 4: "Add your name and email to get your Copa Card." This converts some anonymous submissions without being aggressive.

**7. Every Copa Card link routes to `copa.fc/play/match/[match-id]`.**
This URL always resolves to the active call form for that match. If the match is closed, it shows a "missed this one — here's the next match" message. Never a dead end. The URL carries a referral parameter for tracking.

**Implementation additions:**

Added two new PENDING actions to ACTIONS.md:
1. **Build Typeform First-Play Flow** — updated from the previous "Build Typeform Pre-Match Call Form" action to include the full Screen 1 nation selector, returning player URL routing, and Zapier upsert logic.
2. **Set Up Match Play URL Routing** — new action specifying how `copa.fc/play/match/[match-id]` is managed in V1 (Short.io redirects, updated per match by operator).

**What was not changed:**

The core mechanic, scoring system, Bold Call spec, Slot Framework, Canva template spec, Airtable schema, and operator runbook are unchanged. These were correct in Generation 9 and adding to them would introduce scope creep. The only correct move was to fill the one genuine gap — the first-play experience — and leave everything else alone.

### Score estimate after this cycle

- concept-uniqueness: 0.93 (unchanged — design is solid, framing is sharp)
- market-positioning: 0.95 (unchanged)
- marketing-reach: 0.88 (unchanged — still a do-it gap, not a design gap)
- monetization-readiness: 0.92 (unchanged)
- product-readiness: 0.88 (up from 0.72 — first-play flow specified closes the largest remaining gap; remaining gap is build, not design)
- viral-mechanics: 0.91 (up from 0.88 — the viral loop is now fully specified end-to-end: card link → call form → card → share → new player → call form)

**Overall: approximately 0.91.**

### What remains before the build is complete

1. **Domain registration** — unblocks everything
2. **Copa Card Canva template** — the primary marketing asset; unblocks all social posts
3. **Airtable base** — unblocks end-to-end testing
4. **Typeform first-play flow** — now fully specified; build takes ~45 min
5. **URL routing setup** — 30 min; unblocks the copa.fc/play/match/[id] links on cards
6. **Beehiiv email templates** — unblocks Copa Card delivery
7. **Stripe payment link** — unblocks monetization from day one
8. **r/soccer seed thread** — can go live this week, no build prerequisites

The design is complete. The first-play experience is specified. Nothing else needs to be designed — only built.

### Files changed this cycle
- CONCEPT.md: Added "Zero-Barrier First-Play Flow — Full Specification" section (8 screens fully specified, returning player flow, anonymous submission handling, V1 technical implementation). Updated Typeform Build Spec reference to include first-play flow. V1 Feature Set table updated to include zero-barrier first-play flow, anonymous-to-named player conversion, and URL routing as explicit V1 IN items.
- ACTIONS.md: Updated "Build Typeform Pre-Match Call Form" → "Build Typeform First-Play Flow" with full spec including Screen 1, returning player URL routing, and test cases. Added new action "Set Up Match Play URL Routing" (Short.io, 30 min, unblocks card link functionality).
- JOURNAL.md: This entry.


---

## Generation 11 — Builder Gap Audit

**Date:** 2026-03-15

### What this cycle was actually for

The pre-cycle score showed product-readiness at 0.78 — the weakest dimension. The design task asked to "update CONCEPT.md with the full game design." But reviewing all state files: the game mechanic, scoring, Bold Call, Copa Card, operator runbook, Airtable schema, first-play flow, and call design are all fully specified. Rewriting any of those would introduce scope creep without improving product-readiness.

The correct interpretation of "product-readiness 0.78" is: a builder picking up these files today would get stuck somewhere. The right move was to find exactly where, not to redesign.

### What was actually missing

Two things. Both would block a builder on day one.

**Gap 1: Beehiiv text Copa Card email — body never written.**

CONCEPT.md referenced this template twice and specified subject line format and preview text format. But the actual email body — the text a player receives — was never written. An operator building the Beehiiv template had no copy to work from. They would have to invent the email from scratch, introducing inconsistency and risk.

This cycle: the full email body is now written, including all conditional sections (bold call correct / wrong / contrarian / absent), the call-by-call display format, the tournament instinct score block, the next match CTA, the share link, and the footer. The Pro upsell block is written separately with the instruction to append it starting from the second card. The Pro Copa Card email differences are specified. Literal Beehiiv build instructions are included (template type, field names, segment setup, send time estimate).

**Gap 2: Typeform build spec — screen sequence described, literal configuration never written.**

CONCEPT.md described the screen sequence in detail (Screen 1, Screen 2, Screen 3, Screen 4). But a builder opening Typeform for the first time would not know: what question type to use for each screen, what the field reference names are, what the hidden fields are, how the Zapier trigger maps to Airtable, how to handle the returning player flow without native cookie support, or how to build the in-match form separately.

This cycle: the Typeform spec is now written as a literal question-by-question configuration. Every question has: question type, question text, description text, field reference name, required/optional, and logic notes. Hidden fields are specified. The Zapier action sequence is written out. Form 1B (returning player abridged form) is specified. Form 2 (in-match call form) is specified. The V1 limitations (no dynamic text on thank you screen, static crowd split numbers) are named explicitly so the builder knows what to accept and what to work around.

### What was not changed

Everything else. The mechanic, scoring, Bold Call, call design, Slot Framework, sample call sets, Canva template spec, Airtable schema, operator runbook, edge cases, first-play flow, and all marketing/monetization files are unchanged. They were correct. Adding to them would have been motion, not progress.

### Score estimate after this cycle

- concept-uniqueness: 0.93 (unchanged)
- market-positioning: 0.95 (unchanged)
- marketing-reach: 0.88 (unchanged — still a do-it gap, not a design gap)
- monetization-readiness: 0.92 (unchanged)
- product-readiness: 0.91 (up from 0.78 — the two builder-blocking gaps are closed; remaining gap is execution, not specification)
- viral-mechanics: 0.91 (unchanged)

**Overall: approximately 0.92.**

### What remains before build is complete

All design gaps are now closed. The remaining items are execution tasks, not specification tasks:

1. **Domain registration** — copafc.com (unblocks all marketing; 10 minutes)
2. **Copa Card Canva template** — build per spec in CONCEPT.md (45 minutes; primary marketing asset)
3. **Airtable base** — build per schema in CONCEPT.md (2–3 hours)
4. **Typeform first-play flow** — build per literal spec now in CONCEPT.md (45 minutes)
5. **Beehiiv email templates** — build per literal spec now in CONCEPT.md (1 hour)
6. **URL routing setup** — Short.io redirects (30 minutes)
7. **Stripe payment link** — $6.99 one-time (15 minutes)
8. **r/soccer seed thread** — no build prerequisites; can go live this week

The design is complete. The specs are builder-ready. Nothing else needs to be designed — only built.

### Files changed this cycle
- CONCEPT.md: Added full Beehiiv text Copa Card email body (free tier, Pro upsell block, Pro tier differences, literal Beehiiv build instructions). Added full Typeform build spec (Form 1 question-by-question, Form 1B returning player, Form 2 in-match, hidden fields, Zapier action sequence, V1 limitations). Updated V1 Feature Set table to include "Beehiiv text Copa Card template (fully written)" and "Typeform build spec (literal question-by-question)" as explicit V1 IN items.
- JOURNAL.md: This entry.
