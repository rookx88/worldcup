# Game Concept

## Status
**Full design complete** — Generation 5. All open design questions resolved. Ready for build.

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

**Hook (one sentence):** Copa asks you five yes-or-no questions about each World Cup match — you answer by gut, the match answers for real, and you get a shareable card showing exactly what you called.

**Why this isn't a prediction game:** There are no stakes, no money, no odds. You're not forecasting outcomes for gain — you're building an instinct *record*. The card is an artifact of what you felt during the match. That's a different psychological frame, and it's what makes the card worth sharing.

---

## Core Mechanic

Before and during each World Cup match, Copa presents **5-6 binary calls** tied to real match events:

- "Does the team that scores first win this match?"
- "Red card in this match — yes or no?"
- "At least one goal from a set piece?"
- "Does this match stay under 3 total goals?"
- "Does this team score before half time?" *(opens at 30', closes at HT whistle)*
- "Does this match go to extra time?" *(knockout rounds only, opens at 75')*

Players tap YES or NO. The call locks. The match decides.

**One Bold Call per match:** Before submitting, the player marks one call as their **Bold Call**. If it hits: 3x points. If it misses: 0 points, no penalty. The Bold Call is displayed prominently on the Copa Card whether it hit or missed — it is the most shareable element of the card.

The Bold Call must be selected before the match kicks off (for pre-match calls) or before the in-match call window closes. It cannot be changed after submission.

---

## What You're Actually Playing

You are building an **instinct record** — a live account of every call you made during the tournament.

After each match, Copa generates your **Copa Card**: a shareable visual showing your call record, your score, and your Bold Call result. The card is designed to be posted. It contains social proof ("I called that") and healthy drama ("my Bold Call landed / missed"). Both emotions drive sharing.

---

## Call Design

### Volume
**5-6 calls per match.** Fewer calls increases each call's weight. More than 6 creates cognitive overhead casual fans won't sustain for 90 minutes.

### Call Types

**Pre-match calls** (submitted before kickoff, resolve during match):
- "Red card in this match — yes or no?"
- "Will this match be decided by a single goal?"
- "Does the team that scores first win?"
- "At least one goal from a set piece — yes or no?"
- "Does a penalty get awarded in this match?" *(replaces 60-second live call in V1)*
- "More or fewer than 2.5 total goals?"

**In-match timed calls** (window opens mid-match, closes at a defined trigger):
- "Does this team score before half time?" (opens at 30', closes at HT whistle — 15+ minute window, feasible via email broadcast)
- "Does this match go to extra time?" (opens at 75', closes at 90' whistle — knockout rounds only)

**One Copa editorial team designs 5-6 calls per match before kickoff.** Calls are selected to be answerable by any fan watching the match — no statistical knowledge required. The goal is that every call feels answerable by instinct alone, while rewarding those with deeper football knowledge.

### Call Selection Principles
- Every call must be resolvable with certainty (no ambiguity in outcome)
- At least one call per match must be "gut-feel accessible" (not dependent on knowing team form)
- At least one call per match must reward football knowledge (team tendency, manager style, tournament context)
- In-match calls must have a minimum 10-minute open window (V1 email delivery constraint)

---

## Scoring System

### Base Points
| Call Result | Points |
|-------------|--------|
| Correct — majority position (≥50% of Copa players agreed with you) | 10 pts |
| Correct — contrarian position (<30% of Copa players agreed with you) | 15 pts |
| Correct **Bold Call** | 30 pts (3x base, regardless of crowd position) |
| Wrong call | 0 pts |
| Bold Call wrong | 0 pts (stamp spent, no penalty) |

### Scoring Notes
- Crowd split is calculated after the match, applied to all correct calls retroactively
- The contrarian bonus rewards Marcus's knowledge advantage without creating a floor that punishes Sofia
- No negative scoring — missed calls cost nothing. This keeps the tone fun rather than punishing.

### Match Score Range
- Typical correct call: 10 pts
- Typical contrarian correct: 15 pts  
- Bold Call correct: 30 pts
- Practical ceiling per match (5 calls, all correct contrarian + Bold Call): ~105 pts
- Realistic engaged player range per match: 30–60 pts
- Copa Card shows: raw score + fraction correct (e.g., "7 / 9 — 52 pts")

### Tournament Score
Running total across all matches played. Shown on leaderboard as both raw points and "calls correct / total calls" (e.g., "143 correct, 182 total — 78.6%").

The fraction is the shareable number. "I finished at 78.6%" works like FPL's Overall Rank — it means something, it can be compared, people want to share it.

### Weekly Hot Streak Bonus (cosmetic only)
- 3 matches in a row with 4+ correct calls → "On Fire 🔥" badge on Copa Card for 48 hours
- No additional points — badge only
- Creates a shareability moment mid-tournament without complexity

---

## The Bold Call Mechanic — Full Specification

**Selection:** On the call submission form, after answering all 5-6 calls, the player designates one as their Bold Call. Radio button UI: "Mark as my Bold Call." Only one may be selected.

**Timing rule:** Bold Call must be selected at submission time. For pre-match calls: before kickoff. For in-match timed calls: before the window closes. The Bold Call cannot be retroactively selected.

**Payout:**
- Bold Call correct → 30 pts (regardless of whether it was a majority or minority position)
- Bold Call wrong → 0 pts
- No Bold Call selected → no Bold Call shown on card (not punished, but the card's most dramatic element is absent)

**Card display:**
- If Bold Call correct: gold band across middle of card — "BOLD CALL ✓ — Called [match going to extra time] before 75'"
- If Bold Call wrong: grey band — "BOLD CALL ✗ — [Call text]"
- If no Bold Call: no band

**Why the Bold Call exists:**
1. It makes one call per match a deliberate commitment, not passive tapping
2. The card's most visually striking element is earned, not automatic
3. It differentiates Marcus (who times his Bold Call strategically) from Sofia (who bets on her gut) — both valid, both rewarded
4. A correct Bold Call on an upset or dramatic moment is the single most shareable content Copa produces

---

## The Copa Card — Full Visual Specification

**Format:** 1080×1080px primary (Instagram square). 1080×1920px secondary (Stories).

**Visual hierarchy (top to bottom):**

1. **Header — full-bleed nation color band** (top 25% of card)
   - Nation flag (large, left-aligned)
   - Player name (large, white, right of flag)
   - Match info (small, below name): "ARG vs FRA · July 18 · Group Stage"

2. **Score band** (bold, centered, large): **"7 / 9 CORRECT"**
   - Below it, smaller: "52 pts · Match rank: Top 12%"

3. **Call list** (middle 40% of card): 5-6 rows
   - Each row: ✓ or ✗ icon · Call text (truncated) · Copa player split (e.g., "61% said YES")
   - Correct contrarian calls get a small "↑ Contrarian" label

4. **Bold Call band** (gold if correct, grey if wrong, absent if not made)
   - Full-width band: "BOLD CALL ✓ — Called [extra time] · +30 pts"

5. **Footer** (bottom 10% of card)
   - Copa wordmark (small, left)
   - `copa.fc/play` (small, right)
   - Current tournament instinct score (e.g., "Tournament: 143 correct · 78.6%")

**Design principle:** Card must communicate in 2 seconds — who, how many right, whether the Bold Call hit. The nation color makes it immediately recognizable as "that person's country" when shared in a group chat.

---

## The Tribal Layer

Every player declares their **nation** at signup. The Copa Card is skinned in that nation's colors. Nation leaderboards aggregate individual scores.

**Nation Leaderboard — full specification (resolved):**
- Metric: **average instinct score per match** across all Copa players who declared that nation
- Formula: sum of all nation players' points ÷ total calls made by nation players
- Minimum qualification: **10 Copa players** must have declared the nation to appear on the main leaderboard
- Nations below 10 players appear on a "Developing Nations" tab — visible, not excluded
- Leaderboard question: "Which nation has the sharpest fans?"
- Updates once per day during group stage; after each match during knockouts

This design is:
- Fair (not dominated by nations with most Copa players)
- Explainable ("the average Copa instinct score for [Nation] fans")
- Interesting (smaller nations can rank above Brazil/Germany if their fans are sharp callers)

---

## Social Layers

### Copa Crews
Groups of up to 20 people. Private leaderboard. Javier creates the Crew (Pro required); friends join free via a single link. Crew leaderboard shows each member's match score and tournament total.

### Rival Mode (V2)
Head-to-head against one specific friend over a single match. Deferred to V2 — requires per-player comparison logic. Copa Crews solve the social competition need for V1.

---

## Join Flow — From Shared Card to Playing in 60 Seconds

**Scenario:** Sofia shares her Copa Card on Instagram Stories. Her cousin Valentina sees it.

**The card shows:** `copa.fc/play` in the footer.

**Valentina opens `copa.fc/play`:**
1. Sees the Copa homepage — current/next match displayed, top Copa Cards from most recent match
2. "Play Copa →" button — prominent
3. Join form: **Name** (text) · **Nation** (flag grid, single tap) · **Email** (text)
4. "Start playing →" button
5. Current open call form appears immediately — she's playing

**No password. No account verification. No email confirmation before first play.**

**If Valentina came from a Crew link** (`copa.fc/crew/javiers-squad`):
1. Lands on Crew page showing: Crew name, current leaderboard (names + scores visible)
2. "Join this Crew →" button
3. Same 3-field form (Name · Nation · Email)
4. Lands on Crew leaderboard with her row added
5. Current call form available immediately

**V1.5 addition:** QR code in Copa Card footer linking directly to join flow.

---

## V1 Scope — Minimum Playable Product

### What V1 includes
- Pre-match call form (Typeform, opens 24hrs before kickoff, closes at kickoff)
- One in-match timed call per match (email broadcast via Beehiiv at the trigger time — e.g., 30' mark; window closes at half-time)
- Post-match Copa Card generation (Canva template; manually produced for each match within 30 minutes of final whistle)
- Copa Card delivered to player's email
- Copa Crews via shared Airtable-backed leaderboard link
- Nation selection at signup
- Bold Call designation in call form (radio button: "This is my Bold Call")
- Scoring in Airtable with crowd-split contrarian multiplier applied post-match

### What V1 defers
- **Live event calls (60-second window):** Not feasible via email. Replaced by pre-match calls covering the same territory ("Does a penalty get awarded?"). Reinstated in V1.5 with push notifications.
- **Automated live call triggering:** V1.5 after tournament proves the model
- **Native app:** V1.5
- **Real-time leaderboard:** V1 uses end-of-day updates
- **QR code on Copa Card:** V1.5
- **Rival (1v1) mode:** V2
- **Referral link automation:** V1 is manual (email referral code post-purchase, tracked in spreadsheet)

### What V1 does not compromise
- **Copa Card quality.** Must look good enough to post on Instagram. Non-negotiable. The card is the growth engine.
- **Crew join flow friction.** Must be under 60 seconds. No account creation before first play.
- **Bold Call on every card.** Even in V1, every card shows the Bold Call outcome. This is the card's hero element.

### V1 Technical Stack
| Function | Tool |
|----------|------|
| Call submission | Typeform |
| Data / scoring / leaderboards | Airtable |
| Card design | Canva (template-based) |
| Email delivery | Beehiiv |
| Payment | Stripe |
| Landing page + join flow | Carrd |
| Crew leaderboard pages | Airtable (shared view) |

### V1 Operator Load
One person. Copa operator:
- Sets call form before each match (5 min)
- Sends in-match email broadcast at trigger time (2 min — watching match, one button)
- Scores calls in Airtable post-match (10 min — automated with formulas once set up)
- Generates Copa Cards in Canva (15 min per match — template, fill in scores, export)
- Sends Copa Cards via Beehiiv (5 min)

**Group Stage load:** Up to 3 matches/day × ~30 min/match = ~90 min/day. Manageable solo.
**Knockout Stage:** 1-2 matches/day — lighter load, more time for card quality.

---

## What Makes This Genuinely New

| Property | DFS | Bracket | Prediction Market | Copa Calls |
|----------|-----|---------|-------------------|------------|
| Requires player knowledge | Yes | No | Partial | **No** |
| Plays during the match | No | No | Partial | **Yes** |
| Generates shareable identity artifact | No | No | No | **Yes** |
| Tribal/national identity | No | Partial | No | **Yes** |
| Bold commitment mechanic | No | No | No | **Yes** |
| Accessible to casual fans | No | Yes | No | **Yes** |
| Novel enough to be press-worthy | No | No | No | **Yes** |

Copa Calls is the only game where the match itself is the game engine and the output is an identity artifact, not a score or a ranking. The Copa Card says something about who you are as a fan — not how much you know about statistics.

---

## Monetization

### Model: Copa Pro — $6.99/tournament (one-time)

### Free Tier (must remain excellent)
- Play all calls for every match
- Receive standard Copa Card after each match (nation skin, full Bold Call display)
- Join one Copa Crew (cannot create)
- Tournament leaderboard access (read-only)

### Pro Tier — $6.99/tournament
**Identity expression (Sofia):**
- Animated Copa Card skin (nation colors, animated elements)
- Nation-exclusive visual frames for milestone moments
- "Copa Pro" badge on public leaderboard

**Organizer power (Javier):**
- Create up to 3 Copa Crews
- Crew admin tools
- Early call access (form opens 30 min before free players)
- Crew vs. Crew challenge mode

**Knowledge proof (Marcus):**
- Extended analytics: call-type percentile breakdown ("You called set-piece goals at 78% — top 3%")
- Best call of tournament highlight with social share
- Full Copa record exported as PDF at tournament end

### Conversion Triggers
| Archetype | Trigger Moment | Message |
|-----------|---------------|---------|
| Sofia | After first Copa Card received + shared | "Your card, but animated — Copa Pro" |
| Javier | At Crew creation wall | "Create your Crew → upgrade takes 30 seconds" |
| Marcus | After 5th Copa Card, blur the analytics | "You're calling set pieces better than most Copa players. See your full breakdown." |

**Rule:** Never upsell before first Copa Card is delivered.

---

## Open Questions (Resolved This Cycle)
- ✅ Copa Card visual hierarchy — fully specified above
- ✅ Nation leaderboard aggregation — average per-player score, min 10 players
- ✅ Rival mode in V1 — deferred to V2; Crews solve the social need
- ✅ Live call (60-second) feasibility in Beehiiv — not feasible; replaced by pre-match calls covering same territory
- ✅ Bold Call as deliberate mechanic — designed as player-designated, not algorithmically assigned
- ✅ Join flow from shared card — fully specified above

## Remaining Open Questions
- None blocking V1 build.
- Nation leaderboard UI: how are ties broken? (Tiebreaker: total calls made — nations with more engaged players break ties upward. To be specified at build time.)
