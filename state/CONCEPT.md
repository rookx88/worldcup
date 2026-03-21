# Game Concept

## Status
Design Complete (Generation 6) — Full game mechanic, viral loop, shareable artifact, and V1 specification defined. (Last updated March 2026)

---

# Copa Reads — Full Game Design

## The One-Sentence Hook
After every match, you don't say what you think — you say what everyone thinks. Then you find out how well you read the room.

*12-year-old version:* Every match has moments everyone argues about. You guess what % of fans took each side. The better you read the room, the higher you score.

---

## Core Mechanic

### Each Match Day — Player Flow

- **Before the match:** No picks. No predictions. No roster. Nothing to lock in before kickoff.
- **During the match:** Copa's editorial team watches for 5 key "Reads" — real, finished moments that will split fan opinion.
- **After the match (within 30 min):** Copa posts the 5 Reads — each one a crowd opinion poll about a specific, contested match moment.  
    - Example: “The ref awarded a penalty in the 67th minute. What % of fans think it was the right call?”
- **Player action:** During the 24-hour window, players submit their read for each moment.  
    - Percentage Reads: Submit a number, 0–100%
    - Split Reads: Allocate % between two sides (e.g., blame defender vs. keeper)
    - Canon Reads: Vote for which moment will be remembered (top-voted becomes Copa Canon)
- **The reveal:** 24 hours after Reads open, actual global crowd percentages are revealed. Players see how close they came.  
    - Scores are calculated: Closer to the true crowd %, higher the score.
- **Your card:** One match, one visual Copa Read Card showing your estimates vs. the crowd, your gap, your best/worst moments, and your running total.

---

### Types of Reads

1. **The Call Read** — “Penalty: what % agree with the ref?”
2. **The Blame Read** — “Who gets blamed, defender or keeper? Allocate %.”
3. **The Moment Read** — “What % say the 34th-minute header (not the penalty) was the turning point?”
4. **The Canon Read** — “Most memorable moment: pick A, B, or C.” (Majority vote becomes Copa Canon)
5. **The Verdict Read** — “VAR overturned the goal: what % of fans think it was right?”

Reads are always about interpretation — not what will happen, but what everyone thinks happened.

---

## Scoring System

- **Percent Reads:**  
    - Within 5% of crowd: 100 pts  
    - 6–10%: 75 pts  
    - 11–20%: 50 pts  
    - 21–30%: 25 pts  
    - >30% off: 10 pts
- **Multi-choice Reads:**  
    - Picked majority: 100 pts  
    - Second-most: 40 pts  
    - Least: 10 pts
- **Bold Read Bonus:**  
    - On moments where crowd consensus is truly surprising (set by Copa editorial, e.g., >70% on a moment you’d expect to be split), if your estimate is within 5%: +50 pts
- **Max score per match:** 5 x 100 + 2 bold reads = 600 pts (achievable only for near-perfect social insight)

**No penalties, zero always earns a participation score.** Skill is reading the crowd, not being a football expert.

---

## Viral Mechanic

### The Shareable Copa Card

Triggered after each match’s reveal.  
Card includes:
- Your match score (e.g., 412 / 600)
- Gap visual for each Read: “You: 84% / Crowd: 75% → gap: 9%”
- “Best Read” highlight: your closest
- “Bold Read” badge if earned (“You called a twist nobody saw coming!”)
- Running tournament total and accuracy
- The Copa Canon for this match (what the crowd picked as THE moment)
- Square, team-colored design, Copa logo in corner; clean, meme-ready.

**What makes people share:**
- Scoring almost-perfectly
- Bold Read badge (contrarian insight)
- Dramatic miss (“I thought everyone would side with the ref — nope”)
- “Our group was miles off!” (Group Card)

**How a friend joins:**  
Card says: “Copa Reads. Free. After every match.” + URL  
Landing page: info on next match, “Reads now open,” and live leaderboard.  
Window for joining is always the *next* match — missed days can be browsed (FOMO is a lever).

---

## Group Play: Organizer Mode

- Group Chat Organizer pays (one-time ~$8, Jackbox model), gets a group code.
- Friends join free.
- After each match, Organizer receives a Copa Group Card: group average vs. crowd, leaderboard, and “Our group’s take” for each Read.
- Group Card is WhatsApp-native. Organizer drops it in chat — viral loop.

---

## Copa Canon

- Each match, the “Canon Read” is a vote: which moment will fans remember?
- The winning moment is added to the permanent Copa Canon — 64 moments by the crowd, not broadcasters.
- Copa Canon builds an archive: the crowd-authored story of World Cup 2026. Browseable on gap days.
- Potential for sponsorship or post-tournament product.

---

## V1 Minimum Viable Version

### Day 1 Must-Haves
- Simple web page with latest 5 Reads, open/closed state visible
- Submission form (no login), email collected for first play
- Reveal page showing crowd %s, player’s estimates/gap, and match score
- Shareable Copa Card image (Canva template + number swap for first version)
- Group code system (Stripe for payment, manual email for code)
- Manual Copa Canon page update

### Not Needed for V1
- App / push notifications
- Real-time or in-stream match integration
- Automated Canon archive (can be updated manually)
- Automated scoring (spreadsheet works for first ~500 users)
- Backend accounts or profiles

---

## What Makes Copa Reads Genuinely New

- Mechanic is modeling social psychology, not predicting outcomes
- No existing daily sports game asks “what % will the crowd side with?” using *live* World Cup moments
- Football knowledge not required — in fact, overthinking makes experts worse. The growth market (neutral, meme, and drama fans) are at parity or better
- Artifact is a “gap story” — your intuition vs. the world, in a way anyone can see at a glance
- Group play (one payer) mirrors Jackbox, integrating viral mechanics for WhatsApp/Discord

---

## Design Decisions & Tradeoffs

- **Zero prediction**: No picks before match, no player/projected results, never “guess the future”
- **No fantasy**: Not “build a team,” not “draft players.” Only interpretation of real, finished events
- **Gap not leaderboard**: Streak mechanic avoided in v1 — points are additive, not streak-protective, to lower pressure
- **One time window, no edits:** Submissions close permanently after 24h — irreversibility makes it meaningful
- **Manual operations at launch**: Bold Reads, Canon archive, card generation can be done manually for under 1000 users; scale later

---

# END OF DESIGN

