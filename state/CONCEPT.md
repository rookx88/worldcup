# Game Concept

*This file defines the core game mechanic, unique hook, and product positioning.*
*Copa will develop and iterate this across generations.*

## Status
**Generation 3 — Monetization model integrated. Game design complete. Ready for validation and build.**

---

## The Gap (Why This Exists)

Every existing World Cup fantasy product is built for people who already know the players. The mechanic is always the same: build a roster, accumulate points, climb a leaderboard. The experience is individual, numerical, and quiet.

But the most viral World Cup content isn't stat-based — it's prediction-based. "I said Argentina in the final and I was RIGHT." Nobody shares their fantasy points total. They share that they called the upset.

There is no product that captures this. That is the gap.

**Competitive evidence:**
- FIFA Official Fantasy loses casual players after the group stage — no knowledge = no engagement
- DraftKings requires a deposit and a salary cap — three barriers before your first pick
- Sorare requires understanding NFTs — alienating to 95% of the target audience
- FPL is genuinely beloved but built for club football, not World Cup casual fans
- None of them produce a shareable visual artifact. Not one.

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
- 1 Heroic option: a real pick with low probability but genuine chance (e.g., a midfielder known for long shots)

Each name shown with: flag, shirt number, team, and their Boldness Tier icon. Faces/photos if rights allow.

Scoring: base 20 pts × boldness multiplier.
- Chalk scorer correct: 20 pts
- Bold scorer correct: 30 pts
- Daring scorer correct: 40 pts
- Heroic scorer correct: 60 pts

---

**Pick 3: Upset Meter**
A slider from 1–5. The question: *"How much of an upset would it be if your Pick 1 result happens?"*

Scores when an upset is confirmed:
- Slider 1: 6 pts / Slider 2: 12 pts / Slider 3: 18 pts / Slider 4: 24 pts / Slider 5: 30 pts

Zero penalty for calling an upset that doesn't happen. This asymmetry is intentional — it encourages confident calls without punishing them.

---

**Pick 4: One Moment**
Choose ONE thing you think happens in this match:
- 🧤 **Clean Sheet** — the team you picked to win keeps a clean sheet
- 🟥 **Red Card** — at least one red card shown
- ⏱️ **Stoppage Time Drama** — a goal scored in 85th minute or later
- 📺 **VAR Overturns** — at least one VAR decision reverses a call
- ⚽ **Hat Trick** — any player scores 3+ goals

Scoring: 15 pts if correct, 0 if wrong.

---

**Pick 5: Exact Score (Optional Bonus)**
Type the exact final scoreline. Optional — skipping costs nothing.

Scoring: Exact score correct → +25 pts. Wrong → 0 pts.

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

---

### After the Match: The Card

Within 15 minutes of final whistle, the player receives their completed **Copa Card**.

**Card anatomy:**
- Header: match name, flags, final score, date
- Five pick tiles: what you picked / what happened / Green (correct) / Red (wrong) / Gold (correct + Daring or Heroic)
- Score: large number — "87 / 160"
- Narrative label (auto-selected):
  - "You called the upset."
  - "So close. You had the right team."
  - "Perfect card. This doesn't happen often."
  - "Better luck next time."
  - "You saw it coming."
- Percentile stat: "Your card was better than 78% of Copa players today."
- CTA footer: "Make your pick for [next match]" + short URL
- Copa logo

**Pro player cards:** Gold foil visual treatment on the card border and score display. Visually distinct when shared. A passive advertisement for Copa Pro — the shared card shows the viewer what Pro looks like.

**Visual style:**
- Dark navy background — looks premium on Instagram
- Gold accent for Heroic picks and Pro cards
- Team colors in header
- Portrait orientation (Instagram story / phone screenshot optimized)

---

### Group Leagues

Any player can join a group league for free. Creating a private group league costs $2.99 (first 500 are free).

Group view shows:
- All members' pick tiles for current/last match
- Tournament points leaderboard
- "Bold Call of the Round" — highest-multiplier correct pick

Auto-generated group leaderboard card at end of each round — shareable.

---

## Monetization Integration

### Copa Pro ($4.99 — full tournament)
Premium gold card skin, pick-by-pick percentile breakdown, streak tracking, group Pro badge, early form unlock (30 min before public). Core game remains fully free.

### Group League Creator Fee ($2.99)
Javier pays to create his private league. His friends join free. First 500 leagues free to build proof before the fee activates.

**Non-negotiable free tier:** Making picks, receiving cards, joining groups. The viral loop must stay free. Monetization sits above the viral loop.

---

## What Can Be Cut for V1

| Feature | V1 | V2 |
|---------|----|----|
| Prediction form (5 picks) | ✅ Tally.so | Native app |
| Player identification | ✅ Email + nickname | Full account system |
| Shortlist per match (8 names) | ✅ Manually curated | API-driven |
| Card generation | ✅ Canva template, sent via email | Automated |
| Score calculation | ✅ Manual spreadsheet | Automated |
| Group league | ✅ Shared link + spreadsheet view | Live UI |
| Shareable card | ✅ Image file sent to player | In-app share button |
| Copa Pro payment | ✅ Stripe Checkout link in email | In-app purchase |
| Group creator fee | ✅ Stripe Checkout at group creation | In-app purchase |
| Leaderboard | ✅ Static, updated daily | Real-time |
| Account creation | ❌ Optional, post-pick | Required pre-pick |

---

## Guest Play Flow (Zero Barrier)

Shared card → landing page → 5 picks → submit (no account) → email to receive result card.

Email is the lock-in: you give your email to get your card. This builds the list automatically.

After the first card is received: **Pro upsell email** sent automatically. "Your card is ready. Want the gold version next time? Copa Pro — $4.99 for the full tournament."

This is the optimal moment to convert: the player has just experienced the product. The "aha moment" is immediately followed by the upgrade offer.

---

## Open Questions (Next Generation)
1. What does the card actually look like? Need a Canva mockup.
2. Which tool handles the Stripe payment integration in V1? (Likely: Stripe Checkout link in the confirmation email — no backend needed)
3. How do we manually curate the shortlist of 8 per match? (Data source: Transfermarkt, Wikipedia squad lists, official FIFA site)
4. What domain? copacard.com is the primary candidate — register before launch.
5. Draft the landing page copy — what's the headline? What's the call to action?
6. When and where does the community validation post go up?
