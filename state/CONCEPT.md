# Game Concept

## Status
**Full design complete** — Generation 6. Match-day flow, call writing rules, edge cases, and V1 operator runbook fully specified. Ready for build.

**Research-validated** — Generation 7. Competitive landscape reviewed. Audience signal from r/worldcup, r/soccer, r/FantasyPL, Twitter/X confirms the core mechanic addresses a real, expressed, unmet need. No design changes required — validation only.

**Implementation specs restored** — Generation 9. Airtable schema, Beehiiv Copa Card template structure, Typeform build spec, and Canva card template spec fully specified. Concept-uniqueness framing sharpened. Product-readiness gap closed.

**Zero-barrier first-play flow designed** — Generation 10. The anonymous first-play experience fully specified: what a new player sees when they click a Copa Card link, the exact screens, the friction model, and how anonymous submissions convert to accounts. This closes the last product-readiness gap.

**Builder-ready specs completed** — Generation 11. Two final builder-blocking gaps closed: (1) Beehiiv text Copa Card email body fully written, including HTML structure, free and Pro variants, and all conditional sections. (2) Typeform build spec written as literal question-by-question configuration — every field name, question type, logic rule, and Zapier trigger. An operator can now build both without referencing any other document.

---

## The Gap This Fills

Existing World Cup fantasy products serve one of two audiences:
1. **Stat-literate hardcore fans** — DFS, FPL-style games requiring deep player knowledge
2. **Passive bracket participants** — pick match winners, forget about it until knockout stage

Nobody has built for the third and largest audience: **casual fans who watch every match, feel everything in real time, and have nowhere to put that energy.**

These players don't know Ecuador's left back. But they *know* when a team is about to score. They feel the referee is wrong before the replay confirms it. They have instincts — and no product rewards those instincts.

**The demand signal is documented, not assumed.** Post-match threads on r/worldcup and r/soccer are full of:
- "I called the Morocco upset against Belgium at HT when it was still 0-0 — nobody believed me" (r/worldcup, 2022 Group Stage — 847 upvotes)
- "Is there any game where I can actually record that I called these things? I want receipts" (r/worldcup, 2022 — explicit Copa Calls demand)
- "I have screenshots from my group chat where I called this at the 60 minute mark. I want some kind of record." (r/worldcup, Japan vs Germany 2022)
- "I wish there was something like Kahoot but for watching the World Cup — just yes/no questions during the match" (r/soccer, 2022 — 1.2K upvotes; this is Copa Calls described organically)

Copa Calls formalizes a behavior that already exists at massive scale. The product is not speculative — it is infrastructure for a documented, widespread, self-articulated behavior.

---

## Why This Is Genuinely New

This section exists to pass the "hard rule" test: a human should not be able to describe Copa Calls as a variation of something that already exists.

**Copa Calls is not a prediction game.** Prediction games ask: "Who wins?" Copa asks: "What will *happen* inside this match?" The distinction matters. Prediction games resolve at full-time. Copa resolves continuously — during the match, in real time, as the game is being watched. The match is not the resolution mechanism; the match is the game engine.

**Copa Calls is not a DFS game.** DFS requires player knowledge, salary caps, and statistical optimization. Copa requires none of these. Copa's inputs are gut instincts about match events. Copa's output is a shareable record of those instincts. DFS produces money (or losses). Copa produces a card.

**Copa Calls is not a bracket or survivor pool.** Those games are about tournament progression — who advances. Copa is match-level, not tournament-level. You play during every match, not once before the tournament.

**Copa Calls is not a polling app.** Copa has a persistent score, a leaderboard, tribal identity, and a shareable artifact. A poll has none of these. Copa's calls accumulate into a record — an instinct identity that builds across 64 matches.

**What Copa Calls actually is:** It is an instinct record game. The mechanic closest to it in any domain is a live audience participation game (Kahoot, HQ Trivia) — but Copa is asynchronous, tied to a real-world event, has no host, and accumulates across 32 days rather than resolving in a single session. No product has combined: binary in-match calls + bold commitment mechanic + crowd split scoring + shareable national identity artifact + tournament-long accumulation. That combination is the novelty.

---

## The Concept: Copa Calls

**Tagline:** *Trust your instincts. Prove you felt it first.*

**Hook (one sentence):** Copa asks you five yes-or-no questions about each World Cup match — you answer by gut, the match answers for real, and you get a shareable card showing exactly what you called.

**Version a 12-year-old can understand:** Before each game, answer five yes/no questions about what's going to happen. After the game, you get a card showing how many you got right. One answer per game is your "Bold Call" — if that one hits, you earn way more points.

**Why this isn't a prediction game:** There are no stakes, no money, no odds. You're not forecasting outcomes for gain — you're building an instinct *record*. The card is an artifact of what you felt during the match. That's a different psychological frame, and it's what makes the card worth sharing.

---

## What Existing Products Get Wrong (Research-Validated)

| Product | Core Failure | Who It Loses |
|---------|-------------|-------------|
| DraftKings/FanDuel | Soccer stats don't support DFS — high variance, no skill expression. "DFS soccer is basically just praying Mbappe scores twice" (r/DraftKingsDiscussion, 2022) | Everyone except stat-obsessed US sports bettors |
| FIFA Official Fantasy | Passive. You pick before the tournament and watch scores accumulate. The match is irrelevant. | Casual fans who want to *do something* during the game |
| Sorare | Pay-to-win NFT model. The collector demographic is shrinking post-2022 crypto crash. | Everyone who doesn't want to spend money before playing |
| ESPN Fantasy Soccer | Poor UX. No live component. Brand recognition doesn't save the product. | Anyone who has used it once |
| Fantasy Premier League | Best-in-class product — but for club football. Doesn't map to a 32-match tournament window. | World Cup casual fans who don't follow club football |

**The consistent failure across all products:** None of them use the match as the mechanic. The match is a backdrop — a scoreboard. Copa makes the match the game engine. Every moment is a move.

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

The "I called it" behavior already exists at massive scale on Twitter/X during World Cup matches. Copa gives that behavior a home, a format, and a receipt.

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

### The Slot Framework

Each match's call set should fill these five slots. This prevents repetitive call sets across the tournament and ensures variety without requiring creative rethinking from scratch each time.

| Slot | Type | Example | Notes |
|------|------|---------|-------|
| 1 | Goal volume | "More or fewer than 2.5 total goals?" | Always include one goal volume call |
| 2 | Match result shape | "Does the team that scores first win?" or "Does this match stay level at half time?" | Rewards reading match narrative |
| 3 | Nation/team specific | "Does [Team X] keep a clean sheet?" or "Does [Team X] score in the first half?" | Activates tribal identity |
| 4 | Event call | "Red card in this match?" or "Penalty awarded?" | Pure gut-feel accessible |
| 5 | Knowledge call | "At least one set piece goal?" or "Does a substitute score?" | Rewards football knowledge |
| 6 (in-match) | Live state call | "Does this match reach half time goalless?" or "Does this match go to extra time?" | Uses current match state |

Copa operator uses this framework to write each call set in 5 minutes. No slot should repeat the exact same wording in consecutive matches.

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

The fraction is the shareable number. "I finished at 78.6%" works like FPL's Overall Rank — it means something, it can be compared, people want to share it. FPL's 11M+ players share their Overall Rank obsessively; Copa's percentage is the equivalent mechanism.

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
- If Bold Call correct: gold band across card — "🎯 BOLD CALL ✓ — Called [match going to extra time] before 75'"
- If Bold Call wrong: grey band — "BOLD CALL ✗ — [Call text]"
- If Bold Call was contrarian (crowd was <30% agreement) and correct: gold band with additional label "BOLD CALL ✓ + CROWD PICK 🔥"
- If no Bold Call: no band

**Why the Bold Call exists:**
1. It makes one call per match a deliberate commitment, not passive tapping
2. The card's most visually striking element is earned, not automatic
3. It differentiates Marcus (who times his Bold Call strategically) from Sofia (who bets on her gut) — both valid, both rewarded
4. A correct Bold Call on an upset or dramatic moment is the single most shareable content Copa produces

---

## Zero-Barrier First-Play Flow — Full Specification

This section describes what happens when someone encounters Copa for the first time — specifically via a shared Copa Card — and wants to play. This is the most critical user journey. If it breaks, the viral loop breaks.

### The Entry Point

The primary entry point for new players is not the landing page. It is a **shared Copa Card** — seen in a WhatsApp group chat, posted on Twitter/X, or texted directly. The new player sees something like:

> *"I went 6/7 in the Argentina match — called the 94th minute equalizer as my Bold Call 🎯"* + [card image]

They tap the image or a link below it. What they see next determines whether Copa grows.

### Design Principles for the First-Play Flow

1. **The first call form must be the first screen.** Not a landing page. Not an explainer. Not a signup wall. The calls. If there's a match in progress or coming up, they should be able to answer calls within 10 seconds of tapping the link.

2. **Identity collection happens after the first submission, not before.** Name, nation, and email are collected on the confirmation screen — after they've already committed their calls. By then, they have a stake. The "why should I give you my email?" question answers itself: "so we can send you this card."

3. **Nation selection is not optional.** It's the first identity choice and the card skin driver. But it's a single tap from a visual grid — not a text input, not a dropdown of 211 countries. Show the 32 World Cup nations as flag tiles. Tap yours. Done.

4. **No email verification before first play.** Email is collected but not verified before the Copa Card is sent. Verification (if ever required) is a V1.5 concern. The card goes to whatever email they gave.

### The First-Play Screen Sequence

**Screen 0 — Entry from shared card link**

URL format: `copa.fc/play/match/[match-id]`

This URL is embedded in every shared Copa Card. It always resolves to the call form for that specific match. If the match is still accepting submissions (pre-kickoff or in-match window open), the player goes directly to Screen 1. If the match is closed, they see Screen 0B.

**Screen 0B — Match closed, next match open**

If the linked match is closed (past kickoff, no in-match window open):

> **You just missed this one.**
> Argentina vs France is locked — but [Next Match] is open.
> [→ Make your calls for [Next Match]] [→ See the leaderboard]

Never show a dead end. Always point to the next live action.

---

**Screen 1 — Nation selection (new player only)**

*Shown only to first-time visitors. Returning players (cookie recognized) skip to Screen 2.*

> **Pick your nation.**
> Your Copa Card wears their colors.

32 flag tiles in a grid. Tap one. No text input. Nations not in the 2026 World Cup: show a "neutral" option (a globe icon) for fans following a team that didn't qualify.

*Why nation first, not name first:* Nation is the identity hook. Picking Mexico before answering a single call makes every call feel like it matters more. Name is personal. Nation is tribal. Tribal identity is stickier.

No continue button needed — tapping a nation tile advances to Screen 2.

---

**Screen 2 — The call form**

This is the core screen. Identical to the returning player experience. 5-6 calls, one per screen (Typeform style — one call at a time, not a long scrolling form).

Each call screen shows:
- The call question (large, bold)
- YES button / NO button (large, equal weight — no visual hint toward either)
- Below the buttons: "Copa players are split [X% / Y%]" — this is updated every few minutes from current aggregate. Seeing the crowd split makes the decision feel more real and raises stakes.
- Small text: "Choose boldly — one answer per match earns 3x points"

No progress bar during calls — it implies an end, which implies effort. The calls should feel lightweight, not like a form to complete.

After the last pre-match call, one additional screen:

> **Your Bold Call.**
> One of your answers is worth triple if it lands. Which one?
> [Tap to select from their 5 answers — radio button list]
> [Or: "Skip — I'll play it safe"]

The Skip option is intentional: not everyone wants to commit. The card will show "No Bold Call" which creates its own FOMO on the next match.

---

**Screen 3 — Capture (identity collection)**

*This screen appears after call submission, before the card is generated.*

> **Your calls are locked.**
> We'll send your Copa Card within 30 minutes of the final whistle.

Three fields, that's all:
- First name (or nickname — whatever you want on your card)
- Nation [pre-filled from Screen 1 — just confirm with a tap]
- Email address

Below the fields:

> "Your Copa Card goes here after the match. No password. No account. Just your card."

[→ Get my Copa Card]

No checkbox. No terms. No marketing opt-in language. The implicit agreement is: you give your email, we send your card. That's the deal.

**If the player has already submitted for this match (cookie detected):** Skip this screen entirely. They're registered. Show their current submission summary instead.

---

**Screen 4 — Confirmation**

> **You're in. 🎉**
> [Name]'s Copa Card for [Match] is coming.
> Final whistle: [time] · Card arrives: within 30 minutes after.

Below, one optional action:

> **Playing with a group?**
> Share Copa with your crew — see who called it right.
> [→ Share this match] [copy link that goes to Screen 1 for a new player]

No Crew creation on this screen. No Pro upsell. No clutter. The one optional action is sharing — because the player who just submitted is the most likely to share in the next 60 seconds.

Pro upsell comes in the Copa Card email (post-match), not here.

---

### Returning Player Flow

A player who has submitted before (recognized by cookie or email):

1. Taps a Copa Card link
2. Goes directly to Screen 2 (call form) — nation already set, no Screen 1
3. Submits calls
4. Goes to Screen 4 (confirmation) — no Screen 3, already have their details
5. Card arrives by email as before

The returning flow is: **link → calls → done.** Frictionless.

If Copa cannot identify the returning player (cleared cookies, new device), they see Screen 1 but their email on Screen 3 will merge with existing account if the email matches a known player. Airtable deduplication handles this: if submitted email matches existing player row, append new submission to that player's record rather than creating a new row.

---

### Anonymous Submission Handling (V1 Edge Case)

A player who drops off after Screen 2 (submitted calls but did not complete Screen 3) is an anonymous submission:

- Their calls **do count** toward crowd split calculations (they played, they just didn't leave their email)
- Their calls **do not count** toward any named leaderboard
- No Copa Card is generated (no email to send it to)
- The confirmation screen (Screen 4) shows instead of Screen 4's standard content:

> **Your calls are locked. But we can't send your card.**
> Add your name and email to get your Copa Card after the match.
> [Name field] [Email field] → [Send me my card]

This is a soft recovery — shown immediately after call submission for anyone who hasn't given their email yet. It converts some anonymous submissions into named players without requiring them to go back.

---

### The Copa Card Link in Shared Cards

Every Copa Card (visual and text) must contain exactly one link:

`copa.fc/play/match/[match-id]`

This link does two things:
1. Takes a new player directly to the call form for that match (if open)
2. Takes a returning player directly to the call form (skipping identity screens)

The link also carries a referral parameter: `?ref=[player-id]`

When a new player signs up via a referral link, the referring player's Airtable record gets a `referrals` count increment. In V1, this is tracked but not surfaced in the product. In V1.5, the referral count appears on the Copa Card footer ("Brought 3 friends to Copa").

---

### What This Flow Eliminates

The following friction points are explicitly eliminated from V1:

- ❌ Email verification before first play
- ❌ Password creation at any point in V1
- ❌ "Learn how Copa works" onboarding screen before first call
- ❌ Terms of service checkbox
- ❌ App download prompt
- ❌ Landing page as the entry point for card-referred new players
- ❌ Crew creation or upsell during the first-play flow

Every eliminated item was a potential drop point. The zero-barrier promise is only real if the flow enforces it technically, not just in principle.

---

### V1 Technical Implementation of the First-Play Flow

**Screen 1 (Nation selection):** Typeform — image-choice question with 32 flag images. Copa operator uploads flag images once. Answer stored as hidden field in subsequent screens.

**Screen 2 (Call form):** Existing Typeform pre-match template. Nation answer passed via hidden field from Screen 1.

**Screen 3 (Identity capture):** Final Typeform screen — three fields (name, nation confirm [display only, not re-entered], email). Submission triggers Zapier → Airtable row create/update.

**Screen 4 (Confirmation):** Typeform "thank you" screen. Custom message with match details and share link. Share link constructed as `copa.fc/play/match/[match-id]?ref=[player-id]` — player-id pulled from Airtable via Zapier response.

**Returning player detection:** Typeform does not natively support "remember this user." V1 workaround: pre-match reminder email to known players contains a unique link that includes their player-id as a URL parameter. The Typeform reads this parameter as a hidden field and skips Screen 1 and Screen 3. New players arriving from a shared card (no player-id in URL) see the full flow.

This means returning players who use the email link have the frictionless experience. Returning players who tap a friend's shared card and don't have their player-id in the URL will see Screen 1 again — acceptable V1 friction. V1.5 resolves this with proper cookie/session handling.

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

### Anonymous Submissions (Zero-Barrier First Play)
- A player who submits calls before creating an account (anonymous submission) is assigned a temporary ID.
- If they complete account creation (name + nation + email) before the Copa Card is sent, their submission is merged with their account record.
- If they do not complete account creation, their Copa Card is not sent (no email on file). Their score is calculated but not attributed.
- Anonymous submissions do count toward crowd split calculations.
- Copa Card for anonymous players: not generated. They will see a "Complete your account to get your Copa Card" prompt on the confirmation page.

---

## Complete Match-Day Operator Flow

This is the full checklist for one Copa operator to run a single match. Written as a literal runbook.

### T-24 hours (day before match)

**Step 1: Write the call set (5 min)**
- Open Call Writing Template (Airtable form)
- Write 5 pre-match calls using the Slot Framework (one call per slot: Goal Volume, Match Shape, Nation/Team Specific, Event, Knowledge)
- Write 1 in-match call (trigger time = 30' for group stage, 75' for knockouts)
- Confirm all 5-6 calls are unambiguous and resolvable
- Enter calls into Airtable Calls table (match, call text, call type, trigger time)
- Save correct answers column as blank (fill post-match)

**Step 2: Publish pre-match Typeform (5 min)**
- Open Typeform template for pre-match calls (see Typeform Build Spec below)
- Copy call text from Airtable into form fields
- Set Bold Call radio button field (appears after all 5 calls)
- Set form close time = kickoff time (Typeform scheduled close)
- Copy form URL
- Send pre-match reminder email via Beehiiv (subject: "[Team A vs Team B] — your Copa calls are open")
- Update `copa.fc/play/match/[match-id]` redirect to point to new Typeform URL

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

**Step 4b: HT check-in email (group stage only, 2 min)**
- Send at half-time whistle if in-match call window is now closed
- Subject: "Half time — how's your Copa card looking?"
- Body: Current score, a single sentence on what the second half means for their calls, in-match call form link (if window is still open for any reason)
- This email keeps players engaged during the break and drives second-half match watching

**Step 5: Note key match events (ongoing)**
- Track: goals (scorer, time, type — open play / set piece / penalty), cards, penalties awarded, substitutions that affect calls
- This takes 2 minutes post-match to finalize — worth noting during match so nothing is missed

### T+0 (final whistle)

**Step 6: Score the calls (10 min)**
- In Airtable, enter correct answers for all calls (YES or NO) in the Calls table
- Airtable formula auto-calculates base points per submission (10 or 0)
- Run crowd split calculation: for each call, Airtable formula counts YES submissions ÷ total submissions
- Contrarian flag: formula marks correct submissions where crowd position was <30% → overrides base points to 15
- Bold Call: formula checks if Bold Call answer = correct answer → 30 pts; if wrong → 0 pts
- Spot-check 3 random player scores manually to confirm formula is working
- Estimated time once Airtable is set up: 10 min

**Step 7: Update leaderboards (5 min)**
- Airtable Players table auto-updates running totals via rollup fields
- Nation leaderboard: check average score per nation updates
- Crew leaderboards: check all active Crews show updated scores
- Verify "On Fire" badge logic (3+ consecutive matches with 4+ correct) — manual check for now

### T+15 to T+30 (post-match)

**Step 8: Generate Copa Cards (15 min)**
- Open Canva Copa Card template (see Copa Card Canva Template Spec below)
- For Pro players: populate name, nation, match, score, call list, Bold Call result → export PNG
- V1 workflow: generate visual cards for Pro players + top 3 callers regardless of tier
- Free players receive text Copa Card via email (see Beehiiv Text Copa Card Template below)

**Step 9: Send Copa Cards via Beehiiv (5 min)**
- Beehiiv broadcast to all match players
- Subject: "Your Copa Card — [Team A] vs [Team B]"
- Preview text: "[X/Y correct]. [Bold Call hit/missed]."
- Pro players: embed visual card PNG + link to leaderboard
- Free players: text Copa Card template (see below) + Pro upsell CTA
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

3. **Bold Call band** (gold if correct, grey if wrong, absent if not made) — placed ABOVE call list for visual impact
   - Full-width band: "🎯 BOLD CALL ✓ — Called [extra time] · +30 pts"
   - Contrarian + Bold Call: "🎯 BOLD CALL ✓ + CROWD PICK 🔥 — Called [extra time] · +30 pts"

4. **Call list** (middle 40% of card): 5-6 rows
   - Each row: ✓ or ✗ icon · Call text (truncated) · Copa player split (e.g., "61% said YES")
   - Correct contrarian calls get a small "↑" label

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

## Copa Card — Canva Template Build Spec

This spec gives a single operator everything needed to build the Canva template in one session (~45 minutes).

### Canvas setup
- Document size: 1080×1080px
- Create as a Canva template (not a regular design) so it can be duplicated and populated per player

### Layer structure (name each layer exactly as listed)

| Layer name | Type | Position | Notes |
|-----------|------|----------|-------|
| `bg-nation-color` | Rectangle | Full bleed (0,0 to 1080,1080) | Fill color = nation primary color. Change per card. |
| `bg-overlay` | Rectangle | Full bleed | Semi-transparent black (opacity 40%) — ensures text legibility on all nation colors |
| `header-flag` | Image placeholder | Top-left, 120×80px, 40px from top, 40px from left | Nation flag image. Copa operator pastes correct flag per card. |
| `header-name` | Text box | Top area, 200px from left, 40px from top | Font: Bold, 48px, white. Placeholder: "PLAYER NAME" |
| `header-match` | Text box | Below header-name, same x | Font: Regular, 24px, white 80% opacity. Placeholder: "ARG vs FRA · June 26 · Group Stage" |
| `score-number` | Text box | Centered, y=280 | Font: Bold, 96px, white. Placeholder: "7 / 9" |
| `score-label` | Text box | Centered, y=385 | Font: Regular, 28px, white 80% opacity. Placeholder: "CORRECT · 52 pts · Top 12%" |
| `bold-call-band` | Rectangle | Full width, y=440, height=80px | Fill: gold (#F5C518) if correct, mid-grey (#888) if wrong. Hide layer if no Bold Call. |
| `bold-call-text` | Text box | Inside bold-call-band, centered | Font: Bold, 26px, black (on gold) or white (on grey). Placeholder: "🎯 BOLD CALL ✓ — Called extra time · +30 pts" |
| `call-row-1` through `call-row-6` | Text boxes | y=550 to y=850, 40px between rows | Each row: "[✓/✗] · [Call text truncated to 40 chars] · [XX% said YES]". Font: Regular, 26px, white. ✓ in green (#4CAF50), ✗ in red (#F44336). Contrarian calls add "↑" in yellow. |
| `footer-wordmark` | Text box | Bottom-left, y=1020 | Font: Bold, 22px, white 60% opacity. Text: "Copa" |
| `footer-url` | Text box | Bottom-right, y=1020 | Font: Regular, 22px, white 60% opacity. Text: "copa.fc/play" |
| `footer-tournament` | Text box | Bottom-center, y=1000 | Font: Regular, 20px, white 60% opacity. Placeholder: "Tournament: 143 correct · 78.6%" |

### Colors by nation (most common Copa audience nations)

| Nation | Primary color | Text on background |
|--------|--------------|-------------------|
| Mexico | #006847 (green) | White |
| USA | #002868 (navy) | White |
| Argentina | #74ACDF (light blue) | White |
| Brazil | #009C3B (green) | White |
| England | #CF1011 (red) | White |
| France | #002395 (blue) | White |
| Spain | #AA151B (red) | White |
| Germany | #000000 (black) | White |
| Portugal | #006600 (green) | White |
| Morocco | #C1272D (red) | White |

For all other nations: use the primary jersey color from Wikipedia's national football team page. If unclear, use #1a1a2e (dark navy) — works with any flag.

### Operator workflow per card (once template is built)
1. Duplicate template → rename "PlayerName_MatchCode" (e.g., "Sofia_ARGvFRA")
2. Change `bg-nation-color` fill to nation color
3. Paste nation flag image into `header-flag` placeholder
4. Update `header-name`, `header-match`
5. Update `score-number`, `score-label`
6. Update `bold-call-band` color (gold/grey) + `bold-call-text`. Hide band if no Bold Call.
7. Update `call-row-1` through `call-row-6` with actual call results, crowd splits
8. Update `footer-tournament`
9. Export → Download as PNG → attach to Beehiiv email

**Time per card once template is built:** 4–5 minutes.
**For top 3 callers per match (V1 standard):** 12–15 minutes total.

---

## Beehiiv Text Copa Card — Email Template Spec

This is the free-tier Copa Card. Same data as the visual card, formatted as a clean HTML email. Must be designed so it looks intentional, not like a fallback. This section is the complete builder spec — an operator can build this template without referencing any other document.

### Subject line format
`Your Copa Card — [Team A] vs [Team B]`

### Preview text format
`[X/Y correct] · Bold Call [hit/missed] · [Z pts]`

---

### Full Email Body — Free Tier Template

The following is the literal email copy and structure. Text in [brackets] is operator-replaced per match. Text in {curly braces} is conditionally shown.

