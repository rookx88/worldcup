# Game Concept

## Status
**Full design in progress** — Generation 3 research complete. Monetization model and V1 scope now defined.

---

## The Gap This Fills

Existing World Cup fantasy products serve one of two audiences:
1. **Stat-literate hardcore fans** — DFS, FPL-style games requiring deep player knowledge
2. **Passive bracket participants** — pick match winners, forget about it until knockout stage

Nobody has built for the third and largest audience: **casual fans who watch every match, feel everything in real time, and have nowhere to put that energy.**

These players don't know Ecuador's left back. But they *know* when a team is about to score. They feel the referee is wrong before the replay confirms it. They have instincts — and no product rewards those instincts.

The demand signal is visible without a product to capture it: post-match threads on r/worldcup and r/soccer are full of "I knew Morocco was going to win," "I said Spain looked nervous all second half," "Anyone else feel the penalty was coming?" Copa Calls formalizes a behavior that already exists.

---

## The Concept: Copa Calls

**Tagline:** *Trust your instincts. Prove you felt it first.*

### Core Mechanic

Before and during each World Cup match, Copa presents a sequence of **live narrative questions** — binary calls tied to real match moments:

- "Does this penalty go in?" (60-second live window when penalty is awarded)
- "Does this team score before half time?" (opens at 30', closes at HT)
- "Red card in this match — yes or no?" (opens at kickoff)
- "Next goal scored by the attacking team — yes or no?" (after each corner/freekick)

Players tap YES or NO. The call locks. The match decides.

**This is not prediction markets.** No money rides on individual calls. No odds. No liquidity pools. The financial frame is completely absent.

**This is not DFS.** No rosters. No salary cap. No statistical optimization. You need to know nothing about players to play.

**This is not a bracket game.** The unit of play is a *moment inside a match*, not a match result.

### What You're Actually Playing

You are building an **instinct record** — a live account of every call you made during the tournament, hit or miss.

After each match, Copa generates your **Copa Card**: a shareable visual showing:
- Your calls this match
- Your hit rate (e.g., "7 of 9 correct")
- Your best call ("called the 94th-minute equalizer with 2 minutes left")
- Your tournament-wide instinct score

The card is designed to be posted. It contains social proof ("I called that") and healthy shame ("I missed 4 in a row"). Both emotions drive sharing.

### The Tribal Layer

Every player declares their **nation** at signup. Your Copa Card is skinned in your nation's colors. Leaderboards are nation vs. nation. When your nation scores, your Copa Card gets a special visual.

This is the World Cup's unique property — national tribal identity — fully activated in the game mechanic.

### The Social Layer

**Copa Crews:** Groups of up to 20 friends. Private leaderboard. The crew's collective hit rate vs. other crews. Javier invites his group chat; everyone joins free.

**Rival mode:** Challenge a specific friend. Head-to-head instinct record over a single match. Winner earns a "Copa Edge" badge on their card for 48 hours.

---

## What Makes This Genuinely New

| Property | DFS | Bracket | Prediction Market | Copa Calls |
|----------|-----|---------|-------------------|------------|
| Requires player knowledge | Yes | No | Partial | **No** |
| Plays during the match | No | No | Partial | **Yes** |
| Generates shareable content | No | No | No | **Yes** |
| Tribal/national identity | No | Partial | No | **Yes** |
| Accessible to casual fans | No | Yes | No | **Yes** |
| Novel enough to be press-worthy | No | No | No | **Yes** |

Copa Calls is the only game where the match itself is the game engine. The referee, the VAR decision, the goalkeeper's dive — every moment is a game mechanic.

---

## Call Design

### Volume
**5-8 curated calls per match.** Fewer calls increases each call's weight and drama. More than 8 creates cognitive overhead that casual fans won't sustain for 90 minutes.

### Call Types (Three Categories)

**Pre-match calls** (submit before kickoff, resolve during match):
- "Red card in this match — yes or no?"
- "Will this match be decided by a single goal?"
- "Does the team that scores first win?"
- "At least one goal from a set piece — yes or no?"

**In-match calls** (open during the match, close at specific trigger):
- "Does this team score before half time?" (opens at 30', closes at half-time whistle)
- "Does this match go to extra time?" (opens at 75', closes at 90' whistle in knockout rounds)
- "Next goal in this half — yes or no?" (opens after a key attack sequence)

**Live event calls** (60-second window, manually triggered by Copa operator):
- "Does this penalty go in?"
- "Red card upheld after VAR review — yes or no?"
- "Goal or no goal — is this VAR review going to stand?"

### Who Sets the Calls
**Copa editorial** sets pre-match and in-match calls before kickoff. Calls are designed to be answerable by any fan watching the match — no stat knowledge required. Live event calls are triggered manually by one Copa operator watching the match.

### Scoring Model
**Base:** 10 points per correct call.

**Difficulty multiplier:** Calls where the crowd leans heavily one way pay out more for the contrarian call.
- If 80%+ of Copa players say YES and NO wins: 1.5x points for the NO callers
- If 50/50 split: standard 10 points either way

This rewards Marcus's knowledge advantage (he knows which penalty takers are nervous, which teams collapse late) while keeping the game accessible to Sofia (she can still score well by following her instincts).

**No negative scoring.** Missed calls cost nothing. This keeps the tone fun rather than punishing.

---

## V1 Scope (Minimum Playable Product)

**What V1 includes:**
- Pre-match call submission form (Typeform or Google Forms)
- One manual live call per match (triggered by Copa operator, delivered via email/SMS)
- Post-match Copa Card generation (Canva template + manual customization for top plays)
- Email delivery of Copa Card
- Copa Crews via shared leaderboard link (Airtable-backed)
- Nation selection at signup

**What V1 defers:**
- Automated live call triggering (V1.5)
- Native app (V1.5)
- Real-time leaderboard (V1 uses end-of-day updates)
- Referral link automation (V1 is manual)

**What V1 does not compromise:**
- Copa Card quality. The card must look good enough to post on Instagram. This is non-negotiable because the card is the growth engine.
- Crew join flow. Must be frictionless. No account creation before seeing the game.

**Stack (no-code):**
- Typeform → Airtable (call submission + scoring)
- Canva (Copa Card template generation)
- Beehiiv or Mailchimp (card delivery + live call notifications)
- Stripe (Pro tier payment)
- Notion or Airtable (Crew leaderboards)

**Who operates V1:** One person. Copa operator watches each match, triggers the live call, scores calls post-match, generates and sends Copa Cards.

**Group Stage load:** Up to 3 matches/day × 8 calls = 24 calls/day to score. Manageable manually. Copa Cards generated for each match within 30 minutes of final whistle.

---

## Open Design Questions (Next Cycle)
- Exact Copa Card visual design — what information hierarchy, what dimensions, what sharing format?
- Nation leaderboard mechanics — how does collective nation score aggregate?
- Rival mode implementation in V1 — can this be done with Airtable or does it require custom logic?
- Pre-launch waitlist strategy — when to open, what to offer waitlist members

---

## Monetization

### Model: Copa Pro — $6.99/tournament (one-time)

Evidence base: Comparable zero-budget viral products (Kahoot Pro $9.99/month, Discord Nitro $9.99/month, fantasy sports Pro tiers $5-$20/season) suggest $6.99 one-time is below-market but appropriate for a first-tournament product maximizing adoption over revenue. Tournament-length products should not be subscription-priced — the tournament has a hard end date.

### Free Tier (must remain excellent)
- Play all calls for every match
- Receive Copa Card after each match (standard nation skin)
- Join one Copa Crew (cannot create)
- Tournament leaderboard access (read-only)

### Pro Tier — $6.99/tournament
**Identity expression (Sofia motivation):**
- Animated Copa Card skin (nation colors, animated elements)
- Nation-exclusive visual frames for milestone moments (your team scores, advances, wins)
- "Copa Pro" badge visible on public leaderboard

**Organizer power (Javier motivation):**
- Create up to 3 Copa Crews
- Crew admin tools: rename, invite management, remove members
- Early call access: pre-match calls unlock 30 minutes before free players
- Crew vs. Crew challenge mode

**Knowledge proof (Marcus motivation):**
- Extended analytics: call-type breakdown ("you called penalties at 71% — top 3% of Copa")
- Percentile rank by call category (set pieces, late-match calls, first-half goals)
- "Best call of the tournament" highlight with social share
- Historical record exported as PDF at tournament end

### Conversion Timing
**Do not upsell before first Copa Card is delivered.**

Conversion window by archetype:
- **Sofia:** After first Copa Card received + shared. She's seen the product work. Show her the animated Pro version. "Your card, but animated."
- **Javier:** At Crew creation wall. When he tries to create a Crew, show him Pro. One tap to upgrade, then his crew link is ready.
- **Marcus:** After 5th Copa Card. Show him his percentile stats — but blur the detailed breakdown. "You're calling penalties better than most Copa players. See exactly where you rank → Pro."

### Projected Conversion Rate
Based on Kahoot/Discord comparable data: 5-10% of engaged users (users who have shared at least one Copa Card) will convert to Pro. For planning purposes, model at 7%.

### Revenue Model (Conservative)
- 10,000 engaged users by tournament start → 700 Pro conversions → $4,893 revenue
- 50,000 engaged users → 3,500 Pro conversions → $24,465 revenue
- 200,000 engaged users → 14,000 Pro conversions → $97,860 revenue

These numbers are not the goal — they're the proof that the model works at scale. The 2026 World Cup has 5+ billion viewers. Even capturing 0.001% of that as engaged users produces meaningful revenue.
