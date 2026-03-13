# Game Concept

*This file defines the core game mechanic, unique hook, and product positioning.*
*Copa will develop and iterate this across generations.*

## Status
**Generation 5 — Product-ready. Landing page copy written. V1 build spec complete. Edge cases resolved.**

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

**Scoring:** 10 pts × boldness multiplier.
- Chalk result correct: 10 pts
- Bold result correct: 15 pts
- Daring result correct: 20 pts
- Heroic result correct: 30 pts

---

**Pick 2: First Goalscorer**
Select from a **curated shortlist of 8 players** per match. No free text. No knowledge of the full squad required.

Shortlist structure:
- 3 Chalk options: the obvious goal threats (top scorer, main striker) — shown first
- 3 Bold options: attacking midfielders, second strikers, set piece specialists
- 1 Daring option: a defender or backup who occasionally scores
- 1 Heroic option: a real pick with low probability but genuine chance (e.g., a midfielder known for long shots)
- 1 special option: **"None / 0-0"** — selectable if you want to predict a goalless match

Each name shown with: flag, shirt number, team, and their Boldness Tier icon. Faces/photos if rights allow.

Scoring: base 20 pts × boldness multiplier.
- Chalk scorer correct: 20 pts
- Bold scorer correct: 30 pts
- Daring scorer correct: 40 pts
- Heroic scorer correct: 60 pts
- "None / 0-0" correct (no goals in full 90): 25 pts flat

**Edge case — scorer not on shortlist:** If the actual first goalscorer is not among the 8 on the shortlist, all players who selected any goalscorer score 0 pts on Pick 2. The shortlist is curated honestly (no stacking it with obscure players to manufacture 0-point rounds). If this happens more than once per tournament, the shortlist curation process is revisited. Note in the result card: "The first goalscorer wasn't on today's list — Pick 2 scores 0 for everyone."

---

**Pick 3: Upset Meter**
A slider from 1–5. The question: *"How much of an upset would it be if your Pick 1 result happens?"*

Scores when an upset is confirmed:
- Slider 1: 6 pts / Slider 2: 12 pts / Slider 3: 18 pts / Slider 4: 24 pts / Slider 5: 30 pts

Zero penalty for calling an upset that doesn't happen. This asymmetry is intentional — it encourages confident calls without punishing them.

**Edge case — slider 5 on a non-upset:** If a player picks the heavy favorite (Chalk) and sets their Upset Meter to 5, the Upset Meter scores 0 regardless of result. The system checks: if Pick 1 result was Chalk tier, Upset Meter score = 0 regardless of slider setting. This prevents gaming the system with a "5 slider on a sure thing."

---

**Pick 4: One Moment**
Choose ONE thing you think happens in this match:
- 🧤 **Clean Sheet** — the team you picked to win keeps a clean sheet
- 🟥 **Red Card** — at least one red card shown in 90 minutes (not penalty shootout)
- ⏱️ **Stoppage Time Drama** — a goal scored in 85th minute or later (including added time)
- 📺 **VAR Overturns** — at least one VAR decision reverses an on-field call (goal given/disallowed, penalty given/rescinded, red card given/rescinded)
- ⚽ **Hat Trick** — any player scores 3+ goals in the match

Scoring: 15 pts if correct, 0 if wrong.

**Edge case — Clean Sheet with Draw:** If a player picks Draw in Pick 1 and Clean Sheet in Pick 4, Clean Sheet requires BOTH teams to keep a clean sheet (0-0). If the match ends 0-0, the player scores both the Bold pick on Pick 1 AND 15 pts on Pick 4. This is the highest-reward consistent card a cautious player can construct.

---

**Pick 5: Exact Score (Optional Bonus)**
Type the exact final scoreline. Optional — skipping costs nothing.

Scoring: Exact score correct → +25 pts. Wrong → 0 pts.

**Counts 90-minute score only.** Extra time and penalty shootout results do not count toward the exact score. If a match goes to extra time, the 90-minute score is used. This is clearly stated in the form.

---

### Scoring Summary

| Pick | Base Points | Multiplier Range | Max |
|------|------------|-----------------|-----|
| Match Result | 10 pts | 1× – 3× | 30 pts |
| First Goalscorer | 20 pts | 1× – 3× | 60 pts |
| Upset Meter | 0–30 pts | Scales with slider | 30 pts |
| One Moment | 15 pts | 1× or 0 | 15 pts |
| Exact Score (bonus) | 25 pts | — | 25 pts |
| **Maximum per match** | | | **160 pts** |

**Maximum scenario:** Pick underdog to win (Heroic, 3×) → slider 5 → correct. Heroic goalscorer correct. One Moment correct. Exact score correct.
This requires: genuine upset + your obscure striker scored first + one of five moments happened + you knew the exact score. It's achievable. It requires courage and luck simultaneously. That's the story.

---

### Score Drama Curve — When the Score Changes

A Copa Card score isn't just a number you receive at the end. The player experiences it building in real time if they're watching:

**Kickoff:** Card is submitted. Score is 0.
**First goal:** Pick 2 (goalscorer) and Pick 4 (moment) start resolving. If your scorer scores, Pick 2 locks in green. If it's 85+, Pick 4 can lock in.
**Result at 90':** Pick 1 and Pick 3 resolve. This is the biggest single moment — your result prediction pays out or doesn't. The Upset Meter unlocks here.
**Final whistle:** Pick 5 (exact score) resolves. The complete card is assembled.

**The emotional arc:** 
- Watching for your goalscorer to score: immediate, early tension
- Scoreline drama throughout the match
- Result confirmation at 90': peak moment
- The card arrives 15 minutes after final whistle

This arc means Copa players watch matches differently. They're not just watching. They're watching for their picks.

---

### After the Match: The Card

Within 15 minutes of final whistle, the player receives their completed **Copa Card** via email.

**Card anatomy:**
- Header: match name, flags, final score, date
- Five pick tiles: what you picked / what happened / Green (correct) / Red (wrong) / Gold (correct + Daring or Heroic)
- Score: large number — "87 / 160"
- Narrative label (auto-selected from result pattern):
  - "You called the upset." ← Pick 1 Daring or Heroic, correct
  - "So close. You had the right team." ← Pick 1 correct, Pick 2 wrong
  - "Perfect card. This doesn't happen often." ← 140+ pts
  - "Better luck next time." ← Under 30 pts
  - "You saw it coming." ← Upset Meter 4–5, correct result
  - "The bold call paid off." ← Heroic goalscorer correct
  - "Solid card." ← 80–120 pts, no heroic picks
- Percentile stat: "Your card was better than 78% of Copa players today."
- CTA footer: "Make your pick for [next match]" + short URL
- Copa logo

**Pro player cards:** Gold foil visual treatment on the card border and score display. Visually distinct when shared. The shared card shows the viewer what Pro looks like.

**Visual style:**
- Dark navy background (#0D1B2A)
- Gold accent (#C9A84C) for Heroic picks, correct predictions, and Pro cards
- Team colors in header flags
- Portrait orientation 1080×1920 (Instagram Story / phone screenshot optimized)
- Picks displayed as tiles in a 2×3 grid (Pick 5 spans full width as a bonus bar at bottom)

---

### The Shareable Moment — Trigger Design

Players share when:
1. **They called an upset** — the card reads "You called the upset." The narrative is right there.
2. **They're #1 in their group** — "I'm winning the Copa league" is a natural WhatsApp brag.
3. **Their score is in the top 10%** — the percentile stat makes this explicit and social.
4. **They got a Heroic pick right** — the gold tile is visually distinctive; it reads as special even to a viewer who doesn't know the game.
5. **They got a perfect card** — the narrative label "This doesn't happen often" signals rarity.

**What triggers NOT to rely on:**
- High absolute scores (meaningless without context)
- Generic "I played Copa" cards (no emotional hook)

**The card must tell a story, not just show a score.** The narrative label is not decoration — it is the shareability mechanism.

---

### Group Leagues

Any player can join a group league for free. Creating a private group league costs $2.99 (first 500 are free).

**V1 Group League UX:**
1. Javier visits copacard.com/group (or the landing page CTA for groups)
2. He enters his name, email, and group name
3. He receives a unique group code (e.g., COPA-JV4K) and an invite link
4. He shares the link in his WhatsApp group
5. Friends click the link → land on the Copa pick form with the group code pre-filled
6. After each match, Javier (and all members) receive individual cards + a separate group summary email showing the leaderboard
7. The group summary email includes a shareable group card image (the group leaderboard as an image, auto-generated)

**Group view shows (via email, V1):**
- All members' scores for the current match
- Tournament points leaderboard (cumulative)
- "Bold Call of the Round" — highest-multiplier correct pick in the group
- Running rank: "Javier — 1st place, 247 pts"

**Group league creator badge:** Javier's name appears with a ⭐ in all group emails. Small, visible, rewarding.

---

## Monetization Integration

### Copa Pro ($4.99 — full tournament)
Premium gold card skin, pick-by-pick percentile breakdown, streak tracking, group Pro badge, early form unlock (30 min before public). Core game remains fully free.

### Group League Creator Fee ($2.99)
Javier pays to create his private league. His friends join free. First 500 leagues free to build proof before the fee activates.

**Non-negotiable free tier:** Making picks, receiving cards, joining groups. The viral loop must stay free. Monetization sits above the viral loop.

---

## Landing Page Copy (V1 — for Carrd.co)

### Hero Section
**Headline:** Prove you called it.
**Subheadline:** Make five predictions before kickoff. Get a card after the match. Share it if you were right.
**CTA button:** Get my free Copa Card →
**Supporting line:** Free to play. No account needed. World Cup 2026.

---

### How It Works (Three Steps)

**Step 1 — Pick your five things**
Match winner. First goalscorer (we give you a shortlist — no squad knowledge required). One moment you think happens. Takes 90 seconds. Locks at kickoff.

**Step 2 — Watch the match**
Your card builds in real time. Every goal, every red card, every dramatic finish — you're watching for your picks.

**Step 3 — Get your Copa Card**
15 minutes after the final whistle, your card arrives. It shows exactly what you got right. If you called the upset, it looks incredible.

---

### Example Card Section
*[Image: Copa Card mockup — Morocco 2–1 Spain, 2022, showing 5 picks, score 127/160, narrative label "You called the upset." — gold tile on Pick 1]*

"If your card looks like this, you're sharing it."

---

### Social Proof Hook (pre-launch: aspirational copy)
"Made for the fan who sends match predictions in the group chat — and wants something to show for it when they're right."

---

### Group League Section
**Headline:** Play with your crew.
**Copy:** One person creates a league. Everyone else joins free. Best card in the group wins bragging rights. The group leaderboard updates after every match.
**CTA:** Create a free group →

---

### Copa Pro Section (minimal — one callout block)
**Copa Pro — $4.99 for the full tournament**
Gold card treatment. Pick breakdown. Streak tracking. For when you want to be taken seriously.
[Upgrade to Pro →]

---

### Waitlist CTA (below the fold)
**Headline:** World Cup 2026 starts June 18.
**Copy:** Your first Copa Card is free. Drop your email and we'll send your pick form before the opening match.
**Email field placeholder:** your@email.com
**Button:** I'm in →
**Supporting line:** No spam. One email per match day. Unsubscribe anytime.

---

### Footer
Copa · copacard.com · Built for the 2026 World Cup · Free to play
[Instagram] [Twitter/X]

---

## V1 Build Spec — Complete

### What exists at launch (June 18, 2026)

| Component | Tool | Status | Notes |
|-----------|------|--------|-------|
| Pick form | Tally.so | Build needed | New form per match (10 min setup each) |
| Card template | Canva | Build needed | Single template, manually filled per player |
| Card delivery | Email (Gmail/Outlook + BCC list) | Manual V1 | Upgrade to Mailchimp once list > 100 |
| Score calculation | Google Sheets | Build needed | Formula-based, manual data entry |
| Landing page | Carrd.co | Build needed | Copy above, ACTION-005 |
| Group league system | Google Sheets + invite link | Manual V1 | Group code = filter in spreadsheet |
| Group emails | Manual email with card attachment | Manual V1 | Acceptable for < 200 players |
| Payment (Pro) | Stripe Checkout link | Build needed | Link in landing page + upsell email |
| Payment (Group) | Stripe Checkout link | Build needed | Link at group creation |
| Social accounts | Instagram + Twitter/X | Create needed | ACTION-006 |
| Domain | copacard.com | Purchase needed | ACTION-002 |

### Manual workload per match (V1 estimate)
- Update Tally form for match: 10 min
- Watch match (this is the job): 90 min
- Enter results into Google Sheet: 10 min
- Generate cards (Canva, one per player): 3 min/player → 150 players = 7.5 hrs 🚨
- Email cards: 30 min for 150 players

**The card generation bottleneck is the #1 V1 scaling problem.** At 150 players, manual Canva is at the edge of feasibility. At 500 players, it breaks completely.

**Resolution path:**
1. **V1 (< 50 players):** Full manual. Acceptable for beta/test run.
2. **V1.5 (50–200 players):** Use Canva's bulk create feature (CSV data → auto-populated template cards). This is a real Canva feature. One CSV upload generates all cards. Workload drops from 3 min/player to ~20 min total.
3. **V2 (200+ players):** Carrd → Webflow. Card generation via Make.com (Integromat) automation: Google Sheets data → Bannerbear API (card image generation) → email via Mailchimp. Zero manual card work.

**Bannerbear** (bannerbear.com) is the right tool for automated card generation. They have a template system + API that generates images from data. Free tier: 30 images/month. Paid: $49/month for 500 images. This becomes the V1.5 → V2 bridge.

**Action required:** Add ACTION-011: Set up Canva Bulk Create for match card generation (test before tournament).

---

## What Can Be Cut for V1

| Feature | V1 | V2 |
|---------|----|----|
| Prediction form (5 picks) | ✅ Tally.so | Native app |
| Player identification | ✅ Email + nickname | Full account system |
| Shortlist per match (8 names) | ✅ Manually curated | API-driven |
| Card generation | ✅ Canva Bulk Create | Bannerbear API |
| Score calculation | ✅ Google Sheets formula | Automated |
| Group league | ✅ Group code + spreadsheet | Live UI |
| Shareable card | ✅ Image file sent to player via email | In-app share button |
| Copa Pro payment | ✅ Stripe Checkout link in email | In-app purchase |
| Group creator fee | ✅ Stripe Checkout at group creation | In-app purchase |
| Leaderboard | ✅ Static, updated daily via email | Real-time |
| Account creation | ❌ Optional, post-pick | Required pre-pick |
| In-app card sharing | ❌ Player screenshots their email | Native share button |
| Push notifications | ❌ Email only | In-app push |
| Live score updates | ❌ Not in V1 | Match integration |

---

## Guest Play Flow (Zero Barrier)

**Full flow, step by step:**

1. Sofia sees a Copa Card on Instagram (Marcus shared his)
2. She taps the card → goes to copacard.com
3. She reads: "Prove you called it." She sees the example card.
4. She clicks "Get my free Copa Card →"
5. She lands on the Tally.so pick form for today's match
6. She fills in 5 picks (90 seconds). The form requires her email to receive her card.
7. She submits. The form shows: "Picks locked. Your Copa Card arrives 15 minutes after the final whistle."
8. She watches the match.
9. 15 minutes after the final whistle, she receives her card.
10. The email subject: "Your Copa Card is ready — [Match Name]"
11. The email body: The card image + score + one CTA: "Make your pick for [next match] →"
12. Below the card: "Want the gold version? Copa Pro — $4.99 for the full tournament." [Upgrade →]
13. If she calls the upset, she screenshots and posts to Instagram.
14. Her friend sees it. Loop restarts.

**Email is the lock-in:** You give your email to get your card. This builds the list automatically. The waitlist and the product are the same thing.

---

## Canva Card Template — Visual Spec

**Canvas size:** 1080 × 1920 px (Instagram Story)

**Background:** #0D1B2A (dark navy)

**Section 1 — Match Header (top 15% of card)**
- Left: Home team flag + name (white, bold, 36px)
- Center: Final score (white, bold, 72px) + date below (gray, 24px)
- Right: Away team flag + name (white, bold, 36px)
- Thin gold line (#C9A84C) separating header from picks

**Section 2 — Pick Tiles (middle 60% of card)**
Five tiles arranged in 2×2 grid + 1 full-width bonus tile at bottom:

Each pick tile contains:
- Pick label (small, gray): "MATCH RESULT" / "FIRST GOALSCORER" / "UPSET METER" / "ONE MOMENT" / "EXACT SCORE"
- Player's pick (white, medium): e.g., "Morocco Win" / "Youssef En-Nesyri" / "4 / 5" / "🟥 Red Card" / "2–1"
- What happened (light gray, small): "Morocco won 2–1 ✓" or "Spain won 1–0 ✗"
- Tile border color: Green (#22C55E) if correct, Red (#EF4444) if wrong, Gold (#C9A84C) if correct + Daring/Heroic
- Boldness tier badge: Small icon in corner (Chalk / Bold / Daring / Heroic)

**Section 3 — Score + Narrative (bottom 25% of card)**
- Score: "127" large (white, 96px), "/ 160" smaller (gray, 48px)
- Narrative label (gold, italic, 28px): "You called the upset."
- Percentile (gray, 20px): "Better than 83% of Copa players today"
- Divider line
- Footer: "copacard.com" (small, gray) + Copa logo (small wordmark, right-aligned)
- CTA text (white, 22px): "Your next pick → [Next match name]"

**Pro variant:** Add gold foil gradient overlay on card border (4px, animated in V2, static in V1). Add "Copa Pro" badge (small, top-right corner of card). Score display in gold instead of white.

---

## Open Questions (Resolved This Generation)

| Question | Resolution |
|----------|-----------|
| What does the card look like? | Spec written above. Canva template buildable from this spec. |
| Which tool handles Stripe V1? | Stripe Checkout link in email + landing page. No backend needed. |
| How to curate shortlist of 8? | Transfermarkt for squad lists. FIFA.com for form/lineups. 10 min per match. |
| What domain? | copacard.com — register via ACTION-002. |
| Landing page copy? | Written above in full. Ready for Carrd.co build. |
| Card generation scaling? | Canva Bulk Create (V1.5) → Bannerbear API (V2). |
| Scoring edge cases? | Resolved: off-shortlist scorer, Upset Meter gaming, 0-0 prediction, extra time scores. |

## Open Questions (Next Generation)

1. **Bannerbear API test:** Can Bannerbear replicate the Canva card spec at quality? Need a test card generated via API before committing to it as the V2 path.
2. **Tally.so group code logic:** Can a Tally form pre-fill the group code field from a URL parameter? (e.g., copacard.com/pick?group=COPA-JV4K → group code field auto-populated). This is critical for the Javier invite link UX.
3. **Email deliverability:** Gmail bulk sends get flagged as spam above ~100 recipients. Mailchimp free tier (500 contacts, 1000 emails/month) should replace Gmail for card delivery by the time the beta hits 100 players.
4. **Shortlist rights:** Can we show player headshots on the form without licensing issues? Safe default: flag + shirt number + name only. Photos only if sourced from free/open image libraries.
