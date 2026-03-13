# Game Concept

*This file defines the core game mechanic, unique hook, and product positioning.*
*Copa will develop and iterate this across generations.*

## Status
**Generation 1 — Initial hypothesis established. Awaiting validation.**

---

## The Gap (Why This Exists)

Every existing World Cup fantasy product is built for people who already know the players. The core mechanic is always the same: build a roster, accumulate points, climb a leaderboard. The experience is individual, numerical, and quiet.

But the most viral World Cup content isn't stat-based — it's prediction-based. "I said Argentina in the final and I was RIGHT." Nobody shares their fantasy points total. They share that they called the upset.

There is no product that captures this. That is the gap.

---

## Mechanic Hypothesis: Prediction Cards

### The Core Loop
Before each match, a player fills out a **Prediction Card** — 5 bold calls about that match:

1. **Winner** (or draw) — basic, but the foundation
2. **First goalscorer** — chosen from a shortlist of 6–8 names (no need to know the full squad)
3. **Upset confidence** — a slider: "how upset would this result be?" 1–5. If an upset happens, high-confidence upset-callers score big.
4. **One moment** — pick one: "clean sheet," "red card," "extra time," "VAR controversy" — things that happen in matches that non-stat fans notice
5. **Score exactly** — optional bonus: guess the exact scoreline for multiplier points

### Why This Is Different
- **No roster building.** No salary cap. No knowledge of player stats required.
- **The shortlist solves the knowledge problem.** You don't need to know the full squad — you pick from 6–8 curated names for goalscorer. Casual fans can make an informed guess; hardcore fans can show off by picking the obscure one.
- **The Upset Confidence mechanic rewards drama-watchers**, not stat-optimizers. Someone who "just watches the games" has just as good a read on upset potential as a DFS grinder.
- **The card is a visual artifact.** After the match, your card shows what you got right and wrong — green/red, with the actual result overlaid. It's designed to be shared. The shareable unit is the card, not a leaderboard position.

### What Happens Match Day
- Predictions lock at kickoff
- During the match: no interaction required (passive engagement is fine)
- After final whistle: card resolves, turns into shareable graphic
- Notification: "Your card is ready" — shows your result visually

### What Happens Off-Days
- Group chat / league view: see how your friends' cards scored across recent matches
- "Bold call of the day" feed: surface the best/most surprising correct predictions from all users
- Tournament bracket view: running score of who's called the most matches correctly

### Scoring Philosophy
Points are secondary to narrative. The primary output is: **your card tells a story**. Points exist to create a leaderboard for the competitive players, but the shareable moment is "I called the Morocco upset" not "I have 847 points."

---

## Unique Hook (One Sentence)
**Copa turns your World Cup predictions into a shareable card — so you can prove you called it.**

---

## What Can Be Skipped for V1
- Live in-match interaction (no live scoring needed — resolves after match)
- Complex scoring formulas (simple: correct winner = 1pt, correct scorer = 3pts, exact score = 5pts, upset bonus = variable)
- Custom avatars / cosmetics
- Native mobile app (web-first, mobile-optimized)
- Monetization layer
- Real-time leaderboard (daily batch update is fine)

---

## Open Questions (Next Generation)
1. Does the shortlist for goalscorer need to be manually curated per match, or can it pull from a public API?
2. What does the shareable card actually look like — what visual style resonates with casual fans?
3. Is the game individual + group leagues, or purely group-based?
4. How does this handle the group stage (multiple matches per day) vs knockout rounds?
