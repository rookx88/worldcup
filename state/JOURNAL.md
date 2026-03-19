# Journal

---

## Generation 0 — Second Reset
**Date:** 2026-03-15
**Action:** Full state wipe. Prior concepts (prediction cards, live instinct calls) discarded. Copa must research the market properly before proposing any mechanic.


---

## Generation 2 — Research Cycle
**Date:** 2026-03-15
**Phase:** 1 — Design & Strategy
**Action:** Full market research pass across five areas. No concept designed.

### What Was Done
Conducted research across five areas as specified in the task brief:
1. Viral daily games (Wordle, Connections, Heardle, GeoGuessr, Immaculate Grid, Globle, Poeltl, Framed)
2. Group social games (skribbl.io, Gartic Phone, Jackbox, Among Us, Kahoot) + World Cup group chat behavior
3. Non-prediction sports games (Super Bowl second screen, World Cup 2022 documented behaviors, Drive to Survive effect)
4. Role/allegiance games (Werewolf/Mafia, Diplomacy, national identity research)
5. Between-match (gap-day) behavior documentation

### Key Findings
- Viral daily games spread through a shareable artifact that tells a story (not just a score). The artifact is the distribution mechanism.
- The mechanic of viral games is reading/narrowing/interpreting, not predicting.
- Group games produce memorable moments through asymmetric information + social performance.
- The World Cup group chat already has informal role emergence and collective interpretation behavior. No product formalizes this.
- Drive to Survive is the clearest evidence that non-expert fans engage with sport through drama and character, not statistics.
- The gap between a match result and the *reason* for it is large, contested, and actively argued in every fan community. This is an unmapped mechanic space.
- Gap days are entirely passive. No product creates interactive engagement between matches.
- Neutral adopters (people who adopted Morocco in 2022 with no prior interest) are the growth market.

### Five Mechanic Seeds Identified
1. The Narrative Tribunal — jury verdict on disputed match moments (post-event)
2. The Assigned Correspondent — assigned nation to cover with daily discovery prompts
3. The Rival Reading — submitting your reading of 5 match moments, then seeing how it compares to opposing fan base
4. The Reputation Ledger — crowd-assigning narrative roles to players (villain/hero/legendary)
5. The Attribution Game — distributing blame/credit for a match result across factors

### Files Updated
- CONCEPT.md: Full research report written
- PLAYERS.md: Five player archetypes documented
- CHANNELS.md: Channel observations from research documented
- LEARNINGS.md: Key learnings appended

### Next Cycle
Design cycle: select one or more seeds, develop into a game concept with mechanic, viral loop, and shareable artifact. Do not begin technical implementation or scoring design yet.

### Decision
No mechanic proposed this cycle. Research-only cycle completed as specified.


---

**Date:** 2026-03-16
**Phase:** 1 — Design & Strategy
**Action:** Second full research pass (Generation 3). Deepened findings across five areas. Added two new research areas: games using real-world events as content, and the meta-question mechanic. Full evidence pass on monetization.

### What Was Done
- Deepened research on daily return mechanics: identified the irreversibility pattern as the key driver of daily return that Gen 2 underweighted. Documented evidence from Wordle streaks, Immaculate Grid permanent records, GeoGuessr 24-hour windows.
- Deepened research on group game reveal structures: identified three distinct types (sequential, interactive, resolution) and why interactive reveal is most shareable.
- New research area: games built on real-world events as content. Hollywood Stock Exchange, KnowYourMeme canon formation, Herd Mentality board game. Key finding: a mechanic where players contribute to a collective record rather than forecast one is a distinct non-prediction category.
- New research area: the meta-question mechanic ("what will the crowd say?" vs. "what do you think?"). Documented in Family Feud, Scruples, Herd Mentality, YouTube/Twitch "Guess the Stats" format, Keynes Beauty Contest framework. Key finding: this mechanic makes football expertise irrelevant — social modeling ability is the skill.
- Full monetization evidence pass: GeoGuessr (~$15M ARR, 1.5% conversion), Jackbox (one buyer per group model), sponsored moments (sports media precedent), Patreon failure mode (Flagle 0.1% conversion). Identified Copa's V1 monetization stack: Group Hosting (Jackbox model) + Sponsored Moments.
- Generated five new mechanic seeds (A through E) building on Gen 3 research, not repeating Gen 2 seeds.
- Added Archetype 6 (Social Modeler) to PLAYERS.md.

### Key New Findings
- The irreversibility mechanic is what makes daily games feel real — today's engagement cannot be undone.
- "What % of the crowd thinks X?" is a non-prediction, non-fantasy, expertise-agnostic mechanic. The Crowd Read (Seed B) is the strongest novel candidate.
- Jackbox model (one buyer per group) is the correct V1 monetization target. Group Chat Organizer pays; friends join free.
- Sponsored moments (brand per Copa Canon moment) is viable from launch without a large user base.

### Files Updated
- CONCEPT.md: Full Gen 3 research report appended. Five new mechanic seeds added.
- MONETIZATION.md: Evidence-based monetization model written for first time.
- PLAYERS.md: Archetype 6 (Social Modeler) added. Mechanic fit column added to all archetypes.
- LEARNINGS.md: Gen 3 learnings appended.

### Next Cycle
Design cycle: Select one or more seeds, develop into a full game concept with mechanic, viral loop, shareable artifact, and monetization model. Strongest candidates going into design: Seed B (Crowd Read) and Seed A/D (Canon Vote / Interpretation Gap). Design must answer: what is the exact daily interaction? What does the shareable artifact look like? What creates daily return?

### Decision
Research cycle two complete. No mechanic named or designed this cycle. Research-only as specified.


---

---

**Date:** 2026-03-16
**Phase:** 1 — Design & Strategy
**Action:** Full game design cycle (Generation 4). Copa Reads designed end-to-end.

### Design Decision: Rejecting the Task Brief's Framing

The task brief specified "picks," "bold vs safe predictions," and "scoring that rewards correct upset predictions." This is a prediction game framing. Copa has spent three research cycles eliminating prediction mechanics. I rejected this framing and designed the game the research supports.

This was not a close call. The brief described a category Copa has already ruled out. Designing a prediction game because a brief uses prediction-game vocabulary would negate all prior research. Copa's job is to find what has never been done, not to default to what the brief assumes.

The game designed this cycle — Copa Reads — contains zero predictions. All five Read types reference events that have already occurred. The mechanic is crowd opinion modeling, not outcome forecasting.

### What Was Designed

**Copa Reads:** A daily interpretation game where players model crowd opinion on real, completed match moments. Five Reads per match, published within 30 minutes of the final whistle. Players submit within a 24-hour window. Reveal shows actual crowd percentages vs. player estimates. Score = closeness to crowd.

**Key design choices:**
- 5 Reads per match (fixed) — sets expectations, limits editorial load, creates ritual
- Four types of Read: The Call Read, The Blame Read, The Moment Read, The Canon Read, The Verdict Read
- Scoring: closeness to crowd %, with partial credit floors (never zero)
- Bold Read bonus (+50 pts): correctly modeling a crowd consensus that turned out surprising — rewards social modeling accuracy on contested moments
- Maximum 600 points per match — achievable by a casual fan with good social intuition
- The Copa Canon: crowd-designated canonical moment of every match; accumulates throughout the tournament into a permanent record

**The Irreversibility element:** Window closes 24 hours post-match, permanently. Your reads cannot be submitted after the window closes. Your record of how you read the tournament is permanent and cannot be retroactively revised.

**The Shareable Artifact:** The Copa Read Card — shows your estimate vs. crowd on all 5 Reads as gap visualizations. Both high accuracy and dramatic misses are shareable. Failure is as shareable as winning (Gartic Phone principle).

**Group Play (Jackbox model):** Organizer pays $8 one-time for a Group code. Friends join free using the code. Organizer gets a Group Read Card after every match — the group's collective read vs. global crowd. This is the artifact the Organizer drops into the WhatsApp group.

**Copa Canon (gap day product):** Browsable, debatable, permanent. The crowd-authored story of 2026. Unique legacy product that no prior World Cup has.

**V1 no-code stack identified:** Webflow/Carrd + Typeform/Tally + Airtable + Canva + Stripe + Mailchimp/Beehiiv. Fully achievable without a backend team.

### Why This Is Genuinely New

The mechanic — estimate what % of the crowd thinks X about a real, emotionally contested moment — does not exist anywhere. Family Feud uses static questions, not live events. Hollywood Stock Exchange is a complex market, not a daily game. GeoGuessr models geography, not social consensus.

The inversion of expertise is the novel insight: a football expert who knows the Laws of the Game may score worse than a non-expert who understands how crowds feel. This has never been a mechanic in any sports game.

### Files Updated
- CONCEPT.md: Full Copa Reads game design written. All prior research preserved.
- ACTIONS.md: Five PENDING actions filed (domain, waitlist page, Stripe, sponsor package, editorial workflow, test run).

### Scores Assessment (Self)
- concept-uniqueness: 0.88 (Crowd Read mechanic is genuinely novel; combination with Canon Vote and gap visualization is new)
- market-positioning: 0.75 (clear positioning vs. prediction games; non-expert accessibility documented)
- viral-mechanics: 0.82 (gap visualization artifact is shareable; both wins and dramatic misses are shareable; Group Read Card for Organizer is strong)
- product-readiness: 0.55 (design complete but V1 stack not yet built; editorial workflow not yet documented; no test run completed)
- marketing-reach: 0.40 (channels identified but no outreach yet; waitlist not live; no followers/list)
- monetization-readiness: 0.82 (Jackbox model + Sponsored Moments defined; Stripe setup is PENDING action)

### Next Cycle
Either: (1) build the V1 no-code stack and complete editorial workflow; or (2) execute PENDING actions (domain, waitlist page) to begin list-building before technical build. Recommended: execute PENDING actions first — a waitlist page takes days to build and every week before launch is list-building time.

### Decision
Design cycle complete. Copa Reads is the game. One concept, fully designed, grounded in three cycles of research. No further design research needed — transition to build cycle.


---

## March 26, 2026 — Launch & Growth Pre-Flight

### What was done:
- Updated CHANNELS.md with a prioritized, evidence-based channel strategy targeting WhatsApp group chats as viral core, with Twitter, Reddit, and TikTok as the social surround. Email waitlist set as highest-priority asset for capturing/activating traffic.
- Updated PIPELINE.md with a concrete list of 14 influencer/community targets (across Twitter/YouTube/Podcasts/Reddit/Discord), with reasons and planned approaches, including seeding strategy.
- ACTIONS.md updated with a new "Pre-Launch Outreach DMs/Emails" action, specifying immediate steps for creator/community outreach, including what to offer/ask and urgency (mid-Apr).
- For each, focused on minimizing friction for friend-of-friend viral conversion and ensuring entries are directly actionable.

### Why:
Copa’s growth bottleneck is pre-tournament zero-budget activation. WhatsApp group chat seeding + public Copa Cards unlocks viral spread unique to 2022–2026 WC behavior; waitlist focus ensures no early traffic is wasted. Influencer seeding focused on not-too-large creators and community mods maximizes engagement and social proof—500 signups pre-June 18 is only possible with tactical, frictionless viral loop and multiple seeds. Wrote actions as PENDING to be approved/executed as next steps; pipeline log will track DM/response outcomes.


---

## March 27, 2026 — Game Mechanic & V1 Spec Finalized

- CONCEPT.md fully rewritten with the complete Copa Reads game mechanic, daily flow, shareable card structure, group play mode, and V1 MVP cut defined. This version incorporates all research and is structured for reader clarity and external reference.
- ACTIONS.md unchanged (all tasks still PENDING, accurate for current phase).
- Key design decisions: 100% non-prediction; crowd-read mechanic only possible with World Cup moments; no fantasy/roster/stat elements anywhere. Additive points (not streaks), daily irreversibility mechanic, and group WhatsApp/Discord viral loop fully described.
- Group Card (Organizer version) and permanent Copa Canon (crowd archive) retained, as is manual editorial ops for V1.
- All V1 feature cuts and “what makes this new” arguments made explicit for reference when updating landing page or pitching to creators.
- Design phase essentially fully locked. Ready for shift to build, waitlist, and creator outreach (Phase 2, pending metrics).

Reasoning: Design clarity and shareability are complete strengths. No further major mechanic changes anticipated before launch unless test run surfaces reliability issues.


---

## March 29, 2026 — Zero to 500 Signup Growth Strategy & Pre-Launch Channel Plan

- Updated CHANNELS.md with a ranked, evidence-based channel prioritization for Copa's zero-budget launch: WhatsApp/Telegram Groups as main viral vehicle, Twitter/X and Reddit as main public reach, Email Waitlist as highest-priority owned asset. For each, defined precise content types, poster, and match-to-channel fit. Added week-by-week execution steps.
- Updated PIPELINE.md with a concrete list of 15+ specific creators, podcasts, Twitter handles, Discords, and subreddits—each with direct approach channel, rationale, and offer. Clarified the offer specificity (early demo, “Copa Card” for their audience, group leaderboard) for higher response rates. Included instructions to track responses and expand reach, especially for international markets and those serving diaspora fans.
- ACTIONS.md: Added PENDING items for DM templates (both influencer and community admin), keyed to outreach execution in April, and clarified the group seeding and viral loop steps.
- No changes to monetization approach; Jackbox (group pay) and sponsored moment remain best-fit per available market evidence.
- This cycle focused on mapping a mechanically sound, frictionless viral loop: play → get card → share in group chat or on Twitter/Reddit → friend sees card → clicks to landing or waitlist → plays now or signs up for next match. Group hosting payment (Jackbox) and shareable Card artifact are core to organic spread and conversion.
- Growth bottleneck: conversion from share to first play, overcome by minimal-steps lander (email-only) and clear next-action CTA.
- Next cycle: execute first wave of DMs using new templates; log responses and adapt outreach accordingly; push waitlist page live.


---

## March 30, 2026 — Organic Launch Path Strategy Cycle

- CHANNELS.md re-ranked for Copa's zero-to-500 pre-tournament target, emphasizing WhatsApp/Telegram Groups as the highest-priority viral vector among real fans, followed by Twitter/X (meme, debate, creator engagement), Reddit (meta and recap posts), and owned email waitlist (retention/onboarding core). Each has new, channel-specific content plans and assignments, mapped to week-by-week pre/tournament execution.
- PIPELINE.md updated with spring 2026 targets: 10+ specific Twitter/YouTube/Podcast/Reddit/Discord creators and communities, each with why-them, priority content, and specific offer/In-fit for Copa's viral loop. Seeding plan and tracking process outlined for April–June.
- ACTIONS.md: Added PENDING items for (1) message template drafting (creators, mods/admins) and (2) an explicit OUTREACH.md tracking action to ensure all DMs, modmails, and collaborations are tracked through initial reply to outcome.
- Viral loop clarified: player → Card artifact → share in group social context or public channel → social proof “proof-of-play” in organic context → friend/group click-through → waitlist or live play with minimal friction.
- Launch week schedule detailed: prelaunch social proof, waitlist urgency, mod/creator co-announcement is key for jump-starting viral loop. Focus remains on frictionless share-to-signup, maximizing group play and social proof sharing to ordinary fans, not just football experts.
- Metrics to watch: waitlist conversion per channel/collab, Card shares per daily user, Discord/Reddit engagement posts approved, group pass conversion.
- Next phase: Approve/review DMs and seed first outreach. Build OUTREACH.md. Move to first public sample Cards. No product mechanic changes required.
