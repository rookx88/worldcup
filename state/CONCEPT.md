# Game Concept

*This file defines the core game mechanic, unique hook, and product positioning.*
*Copa will develop and iterate this across generations.*

## Status
**Generation 2 — Full game design complete. Ready for validation and build.**

---

## The Gap (Why This Exists)

Every existing World Cup fantasy product is built for people who already know the players. The core mechanic is always the same: build a roster, accumulate points, climb a leaderboard. The experience is individual, numerical, and quiet.

But the most viral World Cup content isn't stat-based — it's prediction-based. "I said Argentina in the final and I was RIGHT." Nobody shares their fantasy points total. They share that they called the upset.

There is no product that captures this. That is the gap.

---

## Unique Hook

**Copa turns your World Cup predictions into a shareable card — so you can prove you called it.**

The 12-year-old version: *"Pick five things about a match. After it ends, you get a card showing what you got right. If you called the upset, it looks amazing."*

---

## The Prediction Card — Full Design

### Before the Match: Five Picks

A player fills out one **Prediction Card** per match. Takes 90 seconds. Locks at kickoff.

---

**Pick 1: Match Result**
Three options: Home Win / Draw / Away Win.

Each option carries a **Boldness Tier** based on the actual match odds:
- Heavy favorite wins → **Chalk** (1× multiplier)
- Competitive match winner → **Bold** (1.5× multiplier)
- Draw in any match → **Bold** (1.5× multiplier)
- Underdog wins → **Daring** (2×) or **Heroic** (3×) based on odds gap

The tier is shown visually next to each option — a small icon, not a number. Casual fans see "safe" vs "bold" without needing to understand odds.

---

**Pick 2: First Goalscorer**
Select from a **curated shortlist of 8 players** per match. No free text. No knowledge of the full squad required.

Shortlist structure:
- 3 Chalk options: the obvious goal threats (top scorer, main striker) — shown first
- 3 Bold options: attacking midfielders, second strikers, set piece specialists
- 1 Daring option: a defender or backup who occasionally scores
- 1 Heroic option: a goalkeeper... just kidding. A real pick — someone with low probability but genuine chance (e.g., a midfielder known for long shots, a player returning from injury)

Each name is shown with: flag, shirt number, team, and their Boldness Tier icon. Faces/photos if rights allow.

Scoring: base 20 pts × boldness multiplier.
- Chalk scorer correct: 20 pts
- Bold scorer correct: 30 pts
- Daring scorer correct: 40 pts
- Heroic scorer correct: 60 pts

If the match ends 0–0: no one scores, everyone gets 0 on this pick. The drama of a goalless draw is its own story.

---

**Pick 3: Upset Meter**
A slider from 1–5. The question: *"How much of an upset would it be if your Pick 1 result happens?"*

This pick is self-referential — it only pays out if your Pick 1 is correct AND your Pick 1 was at Bold tier or higher.

Scoring when an upset is confirmed:
- Slider 1: 6 pts
- Slider 2: 12 pts
- Slider 3: 18 pts
- Slider 4: 24 pts
- Slider 5: 30 pts

If no upset (Chalk result): this pick scores 0 regardless. The penalty for calling a big upset that doesn't happen is zero points — you just miss the bonus. This asymmetry is intentional: it encourages confident calls without punishing them with negative points.

---

**Pick 4: One Moment**
Choose ONE thing you think happens in this match:

- 🧤 **Clean Sheet** — the team you picked to win keeps a clean sheet
- 🟥 **Red Card** — at least one red card shown in the match
- ⏱️ **Stoppage Time Drama** — a goal scored in 85th minute or later
- 📺 **VAR Overturns** — at least one VAR decision that reverses a call
- ⚽ **Hat Trick** — any player scores 3+ goals

Scoring: 15 pts if correct, 0 if wrong.

Design note: these are things a casual watcher notices in real time. You don't need to track stats — you need to watch the match. This mechanic rewards the person on the couch equally with the stat-tracker.

---

**Pick 5: Exact Score (Optional Bonus)**
Type in the exact final scoreline. Optional — skipping it costs you nothing.

Scoring:
- Exact score correct: **+25 pts**
- Exact score wrong: **0 pts** (no penalty)
- Tie-break rule: if two players on a leaderboard are tied, the one who predicted the exact score (even incorrectly but closer) wins

---

### Scoring Summary

| Pick | Base Points | Multiplier Range |
|------|------------|-----------------|
| Match Result | 10 pts | 1× – 3× |
| First Goalscorer | 20 pts | 1× – 3× |
| Upset Meter | 0–30 pts | Scales with slider |
| One Moment | 15 pts | 1× or 0 |
| Exact Score (bonus) | 25 pts | — |
| **Maximum per match** | **160 pts** | |

**Realistic range:**
- Casual player, mostly Chalk, no upsets: 15–40 pts
- Good game, one Bold pick correct: 40–70 pts
- Great game, upset called correctly: 70–110 pts
- Perfect card (rare, legendary): 130–160 pts

The max is achievable — but only in the exact conditions where you were brave and right. That's the story. That's what gets shared.

---

### After the Match: The Card

Within 15 minutes of final whistle, the player receives their completed **Copa Card**.

**Card anatomy:**
- Header: match name, flags, final score, date
- Five pick tiles arranged vertically, each showing:
  - What you picked
  - What actually happened
  - Green (correct) / Red (wrong) / Gold (correct + Daring or Heroic tier)
- Score: large number in the center — "87 / 160"
- Narrative label below the score, auto-generated from result:
  - "You called the upset." (if Bold+ result correct)
  - "So close. You had the right team." (if result correct, rest wrong)
  - "Perfect card. This doesn't happen often." (if 120+ pts)
  - "Better luck next time." (if low score)
  - "You saw it coming." (if Upset Meter was 4 or 5 and upset confirmed)
- Percentile stat: "Your card was better than 78% of Copa players today."
- CTA footer: "Make your pick for [next match]" + short URL
- Copa logo, small

**Visual style direction:**
- Dark background (deep navy or near-black) — looks premium on Instagram
- Gold accent for Heroic picks
- Team colors in the header
- Minimal text — the card is scanned, not read
- Portrait orientation (optimized for Instagram story / phone screenshot)

---

### Group Leagues

Any player can create a **Group League** and invite friends via a single link.

Group view shows:
- All members' pick tiles for the current/last match (visible after kickoff locks)
- Total points leaderboard for the tournament
- "Bold Call of the Round" — the player who made the highest-multiplier correct pick

Javier's moment: the group leaderboard card is also shareable. "After 8 matches, here's how your group stands." It auto-generates at the end of each round.

---

## What Can Be Cut for V1

**V1 must support one match day. Everything below is the absolute minimum:**

| Feature | V1 | V2 |
|---------|----|----|
| Prediction form (5 picks) | ✅ Typeform or simple web form | Native app |
| Player identification | ✅ Email + nickname | Full account system |
| Shortlist per match (8 names) | ✅ Manually curated | API-driven |
| Card generation | ✅ Manual (Canva template, sent via email) | Automated |
| Score calculation | ✅ Manual spreadsheet | Automated |
| Group league | ✅ Shared spreadsheet, invite by link | Live UI |
| Shareable card | ✅ Image file sent to player | In-app share button |
| Leaderboard | ✅ Static, updated daily | Real-time |
| Notifications | ✅ Email | Push notifications |
| Account creation | ❌ Optional, post-pick | Required pre-pick |

**The key insight:** V1 can be ~80% manual behind the scenes. What matters is that the card looks good and players share it. We learn whether the mechanic works before we build the technology.

---

## Guest Play Flow (Zero Barrier)

Shared card → landing page → 5 picks → submit (no account) → email to receive result card.

The email is the lock-in mechanism: you give your email to get your card. This builds the waitlist automatically. Every person who plays gives us their email.

---

## Open Questions (Next Generation)
1. What does the card actually look like? Need a Canva mockup or Figma file.
2. Which Typeform / no-code form tool handles conditional logic for the 5 picks?
3. How do we manually curate the shortlist of 8 per match — what's the data source? (Wikipedia squad lists, transfermarkt, official FIFA site)
4. What domain? copa.gg, playacopa.com, copacard.com — one needs to be registered.
5. When do we post the V1 validation to r/worldcup — what's the post format?
