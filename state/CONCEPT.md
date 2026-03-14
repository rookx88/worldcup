# Game Concept

## Status
**Full design complete** — Generation 6. Match-day flow, call writing rules, edge cases, and V1 operator runbook fully specified. Ready for build.

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

**Version a 12-year-old can understand:** Before each game, answer five yes/no questions about what's going to happen. After the game, you get a card showing how many you got right. One answer per game is your "Bold Call" — if that one hits, you get way more points.

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
- "Does a penalty get awarded in this match?"
- "More or fewer than 2.5 total goals?"

**In-match timed calls** (window opens mid-match, closes at a defined trigger):
- "Does [Team X] score before half time?" (opens at 30', closes at HT whistle — 15+ minute window, feasible via email broadcast)
- "Does this match go to extra time?" (opens at 75', closes at 90' whistle — knockout rounds only)

**One Copa editorial team designs 5-6 calls per match before kickoff.** Calls are selected to be answerable by any fan watching the match — no statistical knowledge required. The goal is that every call feels answerable by instinct alone, while rewarding those with deeper football knowledge.

### Call Selection Principles
- Every call must be resolvable with certainty (no ambiguity in outcome)
- At least one call per match must be "gut-feel accessible" (not dependent on knowing team form)
- At least one call per match must reward football knowledge (team tendency, manager style, tournament context)
- In-match calls must have a minimum 10-minute open window (V1 email delivery constraint)

### Sample Call Set — Match 1: Mexico vs Poland (Group Stage)

This is a real example of what Copa would publish for a Group Stage match. Used as the template for all Group Stage call writing.

**Pre-match calls (form opens 24hrs before kickoff, closes at kickoff):**

1. "Red card in this match?" — YES / NO
   *(Gut accessible. Poland's physical defensive style means cards are possible. Mexico games tend to be heated.)*

2. "More or fewer than 2.5 total goals?" — MORE / FEWER
   *(Classic over/under. Both teams play tactically in Group Stage openers — FEWER is defensible gut call.)*

3. "Does the first team to score win this match?" — YES / NO
   *(Tests intuition about match control. Mexico historically vulnerable to leads slipping. YES is ~60% in World Cup Group Stage history.)*

4. "Does Mexico score from open play in the first half?" — YES / NO
   *(Nation-specific call activates tribal identity. Mexico fans will feel this viscerally.)*

5. "At least one set piece goal in this match?" — YES / NO
   *(Rewards knowledge — Poland's Lewandowski is a set piece threat, Mexico's corners are dangerous. Crowd will split roughly 50/50.)*

**In-match call (email sent at 30', window closes at HT whistle):**

6. "Does this match reach half time goalless?" — YES / NO
   *(Opens at 30' with score visible — players use live match state to answer. A 0-0 at 30' makes YES credible; a goal already scored makes NO obvious. Crowd split is real-time information.)*

**Bold Call instruction on form:** "Before submitting, mark one answer as your Bold Call. If it hits, you earn 3x points. Choose wisely — or choose boldly."

### Sample Call Set — Knockout Round: Quarter-Final

**Pre-match calls:**

1. "Does this match go to extra time?" — YES / NO
   *(Higher stakes = more draws. More credible as a pre-match call in knockouts.)*

2. "Clean sheet for either team?" — YES / NO
   *(Simple, resolves at final whistle. Rewards knowledge of defensive records.)*

3. "Both teams score in the first half?" — YES / NO
   *(Harder to predict. Crowd tends to say NO. Contrarian bonus if YES hits.)*

4. "Red card in this match?" — YES / NO
   *(Knockout nerves increase cards. More credible in knockouts than group stage.)*

5. "Does the match winner score first?" — YES / NO
   *(Replaces "first scorer wins" with a slightly different framing for variety.)*

**In-match call (opens at 75', closes at 90' whistle):**

6. "Does this match go to extra time?" — YES / NO
   *(Same call as #1, but now players have 90 minutes of evidence. A player who called YES pre-match might lock in YES again with high confidence. A player who called NO might reconsider.)*

   *Note: #1 and #6 can be the same question. They are independent calls — pre-match intuition vs. late-match read. Players who called YES pre-match and then YES again at 75' are rewarded twice if ET occurs. This is intentional: rewarding conviction.*

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

## Edge Cases and Resolution Rules

These rules exist so the Copa operator can score every match without judgment calls.

### Match Abandonment
- If a match is abandoned before 90' (or 120' in extra time), all calls for that match are voided.
- Players receive 0 points and the match is excluded from their tournament record.
- Copa Card is not generated for that match.
- If the match is replayed, Copa generates a new call set for the rescheduled fixture.

### VAR Overturns
- Copa scores calls on the **official final result** as confirmed at the final whistle, including all VAR decisions.
- A penalty awarded then overturned by VAR: call scored as NO penalty awarded.
- A red card rescinded by VAR: call scored as NO red card.
- Copa does not issue corrections after the Copa Card has been sent. The final whistle state is final.

### Draws and Extra Time (Group Stage)
- "Does this match go to extra time?" is only offered in knockout rounds.
- In group stage, a draw is a draw. "Does the first team to score win?" scores NO if the match ends in a draw.
- "Will this match be decided by a single goal?" scores as per the final group stage score (e.g., 1-0 = YES, 1-1 = NO, 2-1 = NO).

### Penalty Shootouts
- Shootout results do not affect Copa calls. Copa calls resolve at the end of 90' regulation (or 120' extra time if applicable).
- "Does this match go to extra time?" resolves YES if the match reaches extra time (regardless of shootout outcome).
- "Clean sheet for either team?" resolves based on regulation + extra time goals only.

### Crowd Split Edge Case
- If crowd split lands exactly at 30% (boundary for contrarian bonus), the call is scored as majority (10 pts, not 15 pts). The threshold is **strictly less than** 30%.
- If fewer than 50 players have submitted the call, contrarian bonus is suspended for that call (not enough data to compute a meaningful crowd split). All correct calls score 10 pts regardless of position.

### Player Misses the Submission Window
- If a player does not submit before the pre-match deadline, they receive 0 pts for that match.
- No retroactive submissions. No exceptions.
- In-match call: if the player does not submit the in-match call within the window, the in-match call is scored as a miss (0 pts, does not count toward their "calls total").
- A missed in-match call does not appear on the Copa Card (does not show ✗ — it is simply absent).

### Bold Call on In-Match Call
- A player may designate the in-match call as their Bold Call.
- The timing rule applies: they must select Bold Call before the in-match window closes.
- If they already submitted pre-match calls without a Bold Call designation, they may still designate the in-match call as Bold Call (one Bold Call per match total — not one per call type).

### Ties on Leaderboard
- Tournament leaderboard ties broken by: (1) higher percentage correct (calls correct ÷ total calls), (2) more total calls made, (3) earlier account creation.
- Nation leaderboard ties broken by: more total calls made by nation's Copa players. Nations with more engaged fans break ties upward.

### Call Ambiguity (Pre-Match)
- If Copa publishes a call that becomes unanswerable (e.g., "Does [Player] score?" and player is injured in warmup), the call is voided for all players. Voided calls do not appear on Copa Cards.
- Copa reserves the right to void a call up to kickoff. After kickoff, all calls stand.

---

## Complete Match-Day Operator Flow

This is the full checklist for one Copa operator to run a single match. Written as a literal runbook.

### T-24 hours (day before match)

**Step 1: Write the call set (5 min)**
- Open Call Writing Template (Airtable form)
- Write 5 pre-match calls using Call Selection Principles
- Write 1 in-match call (note: trigger time = 30' for group stage, 75' for knockouts)
- Confirm all 5-6 calls are unambiguous and resolvable
- Enter calls into Airtable Calls table (match, call text, call type, trigger time)
- Save correct answers column as blank (fill post-match)

**Step 2: Publish pre-match Typeform (5 min)**
- Open Typeform template for pre-match calls
- Copy call text from Airtable into form fields
- Set Bold Call radio button field (appears after all 5 calls)
- Set form close time = kickoff time (Typeform scheduled close)
- Copy form URL
- Send pre-match reminder email via Beehiiv (subject: "[Team A vs Team B] — your Copa calls are open")

### T-0 (kickoff)

**Step 3: Confirm pre-match form is closed (1 min)**
- Verify Typeform is showing "closed" to new submissions
- Export submissions to Airtable via Typeform → Airtable Zap (or manual export if Zap is not set up)

### During match (live watch required)

**Step 4: Trigger in-match call (2 min)**
- At the designated trigger time (30' or 75'), send Beehiiv broadcast
- Subject: "[LIVE] Copa in-match call — [Team A vs Team B]"
- Body: Call text + YES/NO Typeform link (separate in-match form)
- Window closes: at half-time whistle (30' call) or 90' whistle (75' call)
- Operator sets reminder on phone for window close time

**Step 5: Note key match events (ongoing)**
- Track: goals (scorer, time, type — open play / set piece / penalty), cards, penalties awarded, substitutions that affect calls
- This takes 2 minutes post-match to finalize — worth noting during match so nothing is missed

### T+0 (final whistle)

**Step 6: Score the calls (10 min)**
- In Airtable, enter correct answers for all calls (YES or NO)
- Airtable formula: for each submission, compare player answer to correct answer → calculate base points (10 or 0)
- Run crowd split calculation: for each call, count YES submissions ÷ total submissions
- Identify contrarian callers (<30% position, correct): update their points to 15
- Identify Bold Call submissions: if Bold Call answer = correct answer → 30 pts. If wrong → 0 pts.
- Spot-check 3 random player scores manually to confirm formula is working
- Estimated time once Airtable is set up: 10 min

**Step 7: Update leaderboards (5 min)**
- Airtable Players table auto-updates running totals via rollup fields
- Nation leaderboard: check average score per nation updates
- Crew leaderboards: check all active Crews show updated scores
- Verify "On Fire" badge logic (3+ consecutive matches with 4+ correct) — manual check for now

### T+15 to T+30 (post-match)

**Step 8: Generate Copa Cards (15 min)**
- Open Canva Copa Card template
- For each player: populate name, nation, match, score, call list, Bold Call result
- V1 workflow: generate top 5 cards manually (top 3 scorers + any Bold Call highlights)
  - Mass card generation is not feasible manually — see V1 constraint below
- Export all cards as PNG (1080×1080)

**V1 Copa Card generation constraint:** Generating individual cards for every player manually is not feasible at scale. V1 solution:
  - Auto-generate cards for top 3 players per match (manually, ~5 min each)
  - All other players receive a **text-format Copa Card via email**: formatted email with their score, call results, and Bold Call outcome, designed to look like the card
  - Text Copa Card has the same information; it is less visually shareable
  - Players who want the visual card: upgrade to Pro (Pro players get visual card generated within 30 min of final whistle)
  - This creates a natural Pro conversion trigger: "I want my card to look like that"

**Step 9: Send Copa Cards via Beehiiv (5 min)**
- Beehiiv broadcast to all match players
- Subject: "Your Copa Card — [Team A] vs [Team B]"
- Preview text: "[X/Y correct]. [Bold Call hit/missed]."
- Body: visual card (for Pro) or text card (for free) + link to leaderboard
- Include: "Your tournament instinct score: [X correct / Y total — Z%]"
- Include: one-tap link to tomorrow's call form (if a match is scheduled)

**Step 10: Post to social (5 min)**
- Twitter/X: post top Copa Card image + "Yesterday's top caller went [X/Y] in [Match]. They called [Bold Call]. [Card image]"
- If notable crowd split data: "Copa players were split [X%/Y%] on [call]. They were [right/wrong]."
- Reddit match thread: post crowd call aggregate as a comment (not a new post)

**Total operator time per match: ~45 minutes (including match watch)**
**Group Stage peak: 3 matches/day × 45 min = ~2.25 hours/day**

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

**V1 Card generation tiers:**
- **Pro players:** Full visual card (Canva-generated, exported PNG, emailed within 30 min of final whistle)
- **Free players:** Text Copa Card email (same data, formatted for email — not a PNG image, but not ugly)
- **Top 3 callers per match:** Visual card generated and posted publicly on Copa social (free players included — being top 3 earns a visual card regardless of tier)

---

## The Tribal Layer

Every player declares their **nation** at signup. The Copa Card is skinned in that nation's colors. Nation leaderboards aggregate individual scores.

**Nation Leaderboard — full specification:**
- Metric: **average instinct score per match** across all Copa players who declared that nation
- Formula: sum of all nation players' points ÷ total calls made by nation players
- Minimum qualification: **10 Copa players** must have declared the nation to appear on the main leaderboard
- Nations below 10 players appear on a "Developing Nations" tab — visible, not excluded
- Leaderboard question: "Which nation has the sharpest fans?"
- Updates once per day during group stage; after each match during knockouts
- Ties broken by: total calls made by nation's players (more engaged fans win the tiebreak)

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
- One in-match timed call per match (email broadcast via Beehiiv at the trigger time; window closes at half-time or 90' whistle)
- Post-match Copa Card: **visual card for Pro players** (Canva, within 30 min of final whistle); **text Copa Card for free players** (formatted email with identical data)
- Top 3 callers per match receive a visual card regardless of Pro status — posted publicly on Copa social
- Copa Crews via shared Airtable-backed leaderboard link
- Nation selection at signup
- Bold Call designation in call form (radio button: "This is my Bold Call")
- Scoring in Airtable with crowd-split contrarian multiplier applied post-match

### What V1 defers
- **Mass visual card generation for free players:** V1 uses text Copa Card email for free players. V1.5 automates card generation for all players.
- **Live event calls (60-second window):** Not feasible via email. Replaced by pre-match calls covering the same territory ("Does a penalty get awarded?"). Reinstated in V1.5 with push notifications.
- **Automated live call triggering:** V1.5 after tournament proves the model
- **Native app:** V1.5
- **Real-time leaderboard:** V1 uses end-of-day updates
- **QR code on Copa Card:** V1.5
- **Rival (1v1) mode:** V2
- **Referral link automation:** V1 is manual (email referral code post-purchase, tracked in spreadsheet)

### What V1 does not compromise
- **Copa Card visual quality for Pro players.** Must look good enough to post on Instagram. Non-negotiable. The Pro card is the conversion trigger.
- **Text Copa Card data completeness.** Free players must see their full score, all call results, and Bold Call outcome. The format is text; the information is not degraded.
- **Top 3 public cards.** The top 3 callers per match always get a visual card posted publicly. This ensures shareable content exists even with zero Pro players on day 1.
- **Crew join flow friction.** Must be under 60 seconds. No account creation before first play.
- **Bold Call on every card.** Even in V1, every card (visual and text) shows the Bold Call outcome. This is the card's hero element.

### V1 Technical Stack
| Function | Tool |
|----------|------|
| Call submission | Typeform |
| Data / scoring / leaderboards | Airtable |
| Card design (Pro) | Canva (template-based) |
| Text Copa Card (free) | Beehiiv (formatted email template) |
| Email delivery | Beehiiv |
| Payment | Stripe |
| Landing page + join flow | Carrd |
| Crew leaderboard pages | Airtable (shared view) |

### V1 Operator Load
One person. Copa operator:
- Writes call set before each match (5 min)
- Sets call form and schedules close time (5 min)
- Sends in-match email broadcast at trigger time (2 min — watching match, one button)
- Scores calls in Airtable post-match (10 min — automated with formulas once set up)
- Generates visual Copa Cards in Canva for Pro players + top 3 (15 min per match)
- Sends Copa Cards via Beehiiv (5 min)
- Posts to social (5 min)

**Group Stage load:** Up to 3 matches/day × ~45 min/match = ~2.25 hours/day. Manageable solo.
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
- Receive text Copa Card after each match (full data: score, call results, Bold Call — text format)
- Join one Copa Crew (cannot create)
- Tournament leaderboard access (read-only)

### Pro Tier — $6.99/tournament
**Identity expression (Sofia):**
- **Visual Copa Card** (1080×1080 PNG, delivered within 30 min of final whistle) — primary conversion driver
- Animated Copa Card skin (V1.5)
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
| Sofia | After first text Copa Card received | "Get the visual card — Copa Pro ($6.99 for the whole tournament)" |
| Javier | At Crew creation wall | "Create your Crew → upgrade takes 30 seconds" |
| Marcus | After 5th Copa Card, blur the analytics | "You're calling set pieces better than most Copa players. See your full breakdown." |

**Rule:** Never upsell before first Copa Card (text or visual) is delivered.

---

## Open Questions (Resolved This Cycle)
- ✅ Copa Card visual hierarchy — fully specified above
- ✅ Nation leaderboard aggregation — average per-player score, min 10 players, ties by engagement
- ✅ Rival mode in V1 — deferred to V2; Crews solve the social need
- ✅ Live call (60-second) feasibility in Beehiiv — not feasible; replaced by pre-match calls covering same territory
- ✅ Bold Call as deliberate mechanic — designed as player-designated, not algorithmically assigned
- ✅ Join flow from shared card — fully specified above
- ✅ Edge cases — abandoned matches, VAR overturns, missed windows, crowd split thresholds — all resolved
- ✅ V1 card generation constraint — text Copa Card for free players; visual card for Pro; top 3 callers get visual regardless
- ✅ Match-day operator runbook — step-by-step checklist with time estimates
- ✅ Sample call sets — two complete examples (Group Stage + Knockout Quarter-Final)

## Remaining Open Questions
- None blocking V1 build.
- **Airtable schema:** Exact field types and formula syntax to be confirmed at build time (not a design question — an implementation detail).
- **Beehiiv text Copa Card template:** HTML/CSS formatting to be designed at build time.
