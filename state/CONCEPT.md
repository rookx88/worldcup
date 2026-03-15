# Game Concept

## Status
Design Complete (Generation 4) — Full game mechanic, viral loop, shareable artifact, and V1 specification defined.

---

# Design Note — Generation 4

The task brief for this cycle specified "picks," "bold vs safe predictions," and "scoring that rewards correct upset predictions." This framing describes a prediction game — the category Copa's research has already eliminated.

Copa's three research cycles identified the strongest non-prediction, non-fantasy, genuinely novel mechanic: the **Crowd Read** — asking players to model crowd opinion on completed match events, not forecast future outcomes. This design builds from that research finding.

The game designed below is not a prediction game. It is an interpretation and social modeling game. This is the mechanic the research supports.

---

# Copa Reads — Full Game Design

## The One-Sentence Hook
**After the match, you don't say what you think — you say what everyone thinks. Then we find out how well you read the room.**

Or, for a 12-year-old: **Every match creates moments everyone argues about. You guess what % of fans took each side. The better you read the room, the higher you score.**

---

## Core Mechanic

### What Happens Each Match Day

**Before the match:** Nothing. No picks. No predictions. No stakes set in advance.

**During the match:** Copa's editorial team (initially: one person, the founder) watches the match and identifies 5 "reads" — contested moments that the crowd will have a genuine opinion split on.

**After the match (within 30 minutes of final whistle):** Copa publishes the 5 Reads for that match. Players have a **24-hour window** to submit their reads before results are revealed. This window closes permanently.

**The reveal (24 hours later, or next match day):** Actual crowd percentages are shown. Players see how close their reads were. Scores are calculated and shareable artifacts are generated.

---

### The Five Reads (Match Day Structure)

Each match produces exactly 5 Reads. Each Read is a crowd opinion question about a real, completed moment from that match. Examples:

**Format:** A moment description + a sliding spectrum or percentage question.

**Type 1 — The Call Read**
*"The referee awarded a penalty in the 67th minute. What % of fans think it was the right call?"*
Player submits a number 0–100. Score = closeness to actual crowd %.

**Type 2 — The Blame Read**
*"After the own goal, what % of fans will blame the defender (vs. the goalkeeper)?"*
Player submits a split. Score = closeness to actual crowd split.

**Type 3 — The Moment Read**
*"What % of fans will say the 34th minute header (not the 78th minute penalty) was the true turning point?"*
Player picks the option they think the crowd will pick. Score = 100 if correct, 0 if wrong, with partial credit for the right order.

**Type 4 — The Canon Read**
*"Which moment from today will fans remember in 10 years? A: Mbappé's red card. B: The goalkeeper's triple save. C: The 94th minute equalizer."*
Player picks the option they think the majority will pick. Copa's Canon: whichever option gets the most votes becomes the officially crowd-designated canonical moment of that match. It is added to the Copa Canon, permanently.

**Type 5 — The Verdict Read**
*"VAR overturned the goal. What % of fans think VAR made the right call?"*
Player submits a number 0–100.

**Why 5?** Enough to reward attention to the match without requiring comprehensive knowledge. A fan who watched casually can still submit all 5. Missing a Read is allowed — skipped Reads score 0 but don't break the game.

---

### Scoring System

**Base score per Read:** Reads are scored on closeness to actual crowd percentage.

For percentage-estimate reads (Types 1, 5):
- Within 5% of actual crowd: **100 points**
- Within 10%: **75 points**
- Within 20%: **50 points**
- Within 30%: **25 points**
- Outside 30%: **10 points** (participation, not zero — the game should never feel punishing)

For multi-choice reads (Types 3, 4):
- Picked the majority option: **100 points**
- Picked second-most-popular option: **40 points**
- Picked least-popular option: **10 points**

**Bold Read bonus:** If the majority crowd opinion is outside the "expected" range (determined by pre-reveal Copa algorithm based on how contested the moment was), and a player's estimate was within 5% of the actual crowd result, they earn a **Bold Read bonus: +50 points**. This rewards players who correctly read a genuinely surprising crowd consensus — not players who predicted a match outcome, but players who correctly identified that the crowd would have an unexpected reaction.

The Bold Read bonus is the only "risk/reward" element in the game. It is always about crowd psychology, never about match outcomes.

**Maximum score per match:** 5 Reads × 100 points + up to 2 Bold Read bonuses × 50 = **600 points maximum.**

This is achievable. It requires reading the crowd correctly on all 5 moments, with 2 of them being "surprising" crowd consensus moments the player correctly identified. A player who watches casually and has good social intuition can achieve this. A football expert who over-indexes on "correct" analysis and misses crowd psychology cannot.

**Tournament score:** Accumulates across all matches the player participates in. Not average — sum. Missing a match day doesn't wreck your tournament score, it just doesn't add to it. This is psychologically different from streak mechanics — participation is additive, not protective.

---

### Daily Return Mechanic

**The window:** Reads open within 30 minutes of the final whistle. They close 24 hours later, permanently. Submitting after the window is impossible. This is the irreversibility element.

**The pending state:** After submitting, your reads are locked but results haven't been revealed yet. This creates a 24-hour anticipation window — you know you submitted but don't know how you did. The reveal is an event.

**The reveal:** Copa reveals actual crowd percentages at window close. The reveal shows:
- What % of the crowd said (the actual answer)
- Your estimate
- Your gap
- Your score for that match

This is the shareable moment. The reveal, not the submission.

**Gap day behavior:** On days between matches, the Copa Canon grows. Players can see the accumulating Canon — the crowd-designated defining moments of the tournament so far. This is readable, browsable, and debatable. Gap days have content without requiring player action.

---

## Viral Mechanic

### The Shareable Artifact: The Copa Read Card

Triggered at: reveal completion.

**What it shows:**
- Your crowd-read accuracy score for the match (e.g., "78/100")
- A visual showing your estimate vs. the actual crowd on each of the 5 reads — depicted as a gap: "You said 34%. Crowd said 31%. Gap: 3%."
- Your tournament accuracy running score (e.g., "Tournament: 4.2 matches, 71% average accuracy")
- One highlighted "Best Read" — your closest estimate of the match
- If you earned a Bold Read bonus: "Bold Read: You called it when almost nobody else did."
- The Copa Canon moment from this match — the crowd-designated canonical moment

**Visual design principle:** The card must communicate a story, not just a number. The gap visualization is the key — it shows the shape of how you read the match, not just a score. It is immediately legible to non-players: "Oh, you said 34% and the crowd said 31% — that's pretty close."

**What makes someone share unprompted:**
1. They scored near-maximum (achievement signal)
2. They earned a Bold Read bonus (contrarian insight signal — "I saw what the crowd was going to do before the crowd did")
3. Their Best Read gap was very small (specific precision signal — "I said 34%, crowd said 31%")
4. Their gap on a major moment was dramatically wrong in an interesting direction ("I thought 80% would approve the red card. Only 22% did.")

Both extreme accuracy AND extreme miss are shareable. The dramatic miss tells a story too — "I was completely out of step with the crowd on that one" is interesting. This is the Gartic Phone principle: failure is as shareable as winning.

**The card format:**
- Square format (Instagram/WhatsApp native)
- Bold team colors from the match
- Minimal text — visual gap bars dominate
- Copa logo small, bottom right
- No Copa website on the card (URL is for the Organizer to add; the card is clean)

**How a friend joins from seeing the card:**
Card includes one line: "Copa Reads. Free. After every match." + a URL.
That URL leads to a page showing: the 5 Reads for the most recent match (with window closed — viewable but not submittable) and a prompt to join for the next match.

The window-closed preview is intentional. The friend sees what they missed. The next match window is visible. They join because they can see the game already happened and want to be in for the next one.

---

### Group Play: The Organizer Loop

**The Group Chat Organizer receives a Copa Group code** (paid — Jackbox model).

When their friends submit their Reads using the group code, the Organizer gets a Group Read Card after the reveal — showing the group's average estimate vs. the crowd on each Read, and a group leaderboard.

The Group Read Card is different from the personal card — it encodes everyone's reads together, showing "your group was more skeptical of the referee than the global crowd" or "your group's crowd-read accuracy: 68% — better than 71% of Copa groups."

This is the shareable artifact the Organizer drops into the WhatsApp group after every match. It maintains the group chat without requiring everyone to coordinate in real time.

**Why the Organizer pays:** The Group Read Card and group leaderboard are Organizer features only. Everyone else plays free but sees only their personal card. The Organizer pays once ($8 for the tournament) and has the Group Read Card for every match.

---

## Copa Canon

**What it is:** The crowd-designated canonical moment of every match in the 2026 World Cup. Built one match at a time, permanently.

**How it's built:** Type 4 Reads (The Canon Read) let players pick which moment they think the crowd will designate as the match's canonical memory. The majority-voted moment becomes canon. It is added to the Copa Canon archive with the date, match, and crowd vote breakdown.

**Why it matters:** By the end of the tournament, the Copa Canon is a crowd-authored story of 2026 — 64 moments designated by millions of fans, not by journalists or broadcasters. This is genuinely new. No such record exists for any prior World Cup.

**Gap day use:** The Copa Canon is browsable and shareable at all times. On gap days, fans can browse the Canon, debate the designations, and see which early Copa Canon calls were prescient ("Match 3 canon was decided by only 52% of voters — still contested").

**Legacy value:** After the tournament, the Copa Canon is the permanent crowd record of 2026. This is the product that could be licensed to sports media, used in anniversary coverage, and reactivated for future tournaments.

---

## V1 Minimum Viable Version

### What V1 Must Have

**Day 1 of the tournament:**
1. A web page (no app) where a user can see the 5 Reads for the current/most recent match
2. A submission form (no account required for first submission — email collected here)
3. A reveal page showing actual crowd percentages and the user's score
4. A shareable image generated from the reveal (can be a pre-designed template with numbers filled in — no custom image generation required at V1)
5. A Group code system (basic — Organizer pays via Stripe, gets a code, shares it with friends who enter it on submission)

**What V1 does NOT need:**
- Native app
- Real-time updates
- Live score tracking during matches
- Complex user accounts (email is sufficient)
- Automated Copa Canon archive page (can be manually updated daily)
- Bold Read bonus automation (can be manually designated at V1)

**No-code V1 stack:**
- **Webflow or Carrd** — web pages
- **Typeform or Tally** — submission forms
- **Airtable** — data collection and scoring calculation (spreadsheet-native)
- **Canva** — shareable card template with manual number entry for V1
- **Stripe** — Group code payments
- **Mailchimp or Beehiiv** — email delivery of reveal notifications

**Timeline to V1 launch:** 10 weeks from decision (Copa needs to be live for the first matches, June 18, 2026. Design complete March 2026 → 12 weeks to build, test, and launch.)

**Editorial load:** Copa's editorial team (one person at launch) watches each match and selects 5 Reads within 30 minutes of final whistle. This is the only ongoing labor requirement. The Reads must be good — contested, legible to non-experts, and genuinely uncertain in outcome.

---

## What Makes This Genuinely New

### The mechanic that does not exist

No existing game asks: "What % of fans agree with this controversial call?" and scores you on accuracy of crowd modeling — not on your personal opinion, not on the match outcome.

The closest analogies:
- **Family Feud:** "Survey says" — but applied to a static question bank, not real-world events with genuine emotional stakes.
- **Hollywood Stock Exchange:** Collective market on real events — but complex, and not a simple daily game.
- **GeoGuessr:** Read the environment and narrow to the right answer — but geographic, not social.

Copa Reads combines: **real match events** (World Cup specific) + **crowd opinion modeling** (not prediction) + **daily reveal with irreversibility** (return mechanic) + **gap visual artifact** (shareable).

This combination does not exist.

### Why football expertise is not the skill

A football expert who watches the Argentina–Brazil match and says "87% of fans will approve the VAR call — it was clearly offside, the laws are clear" is likely to score worse than a non-expert who says "55% will approve — it looks like a call most people will have mixed feelings about."

The skill Copa Reads rewards: correctly modeling how emotionally invested, tribally divided, non-expert fans will feel about an ambiguous moment.

Football experts systematically over-index on "correct" technical analysis. Social modelers who understand how crowds feel outperform them. This inverts every existing sports game's expertise premium. It is why Drive to Survive worked — the non-expert brings the right frame.

---

## Design Decisions and Tradeoffs

**Decision: No predictions whatsoever, including in-match**
The task brief suggested in-match or pre-match "bold picks." These are prediction mechanics, regardless of timing. Copa Reads contains zero predictions. This was not a compromise — it is the mechanic.

**Decision: Post-match only**
All 5 Reads reference events that have already happened. This means: no stakes during the match itself. Players are watching the match without Copa running in the background. This is a feature. Copa doesn't interrupt watching — it starts when the match ends.

**Decision: 5 Reads per match (fixed)**
Fixed at 5 to: (a) set player expectations, (b) create a consistent ritual, (c) limit editorial load. Could be 3 in V1 if editorial capacity is constrained.

**Decision: Participation score (never zero)**
A Read that's far from the crowd still earns 10 points. This keeps the game non-punishing. The score spread between excellent and poor performance is enough to be meaningful (600 vs ~50) without making poor performance feel humiliating.

**Decision: The Copa Canon is a community product, not a Copa editorial product**
Copa does not choose which moment is canonical. The crowd designates it. This is intentional — Copa is a container for collective intelligence, not a broadcaster making editorial choices. This distinction matters for brand trust and for the product's long-term claim to be the authentic crowd record.

**Decision: Email collection at submission (no account creation)**
Wordle's early spread was account-free. The first submission requires only an email — used to deliver the reveal card. Account creation is V2. This removes the #1 signup abandonment point.

**Tradeoff accepted: Manual operations at V1**
The Bold Read bonus requires someone to manually assess whether a moment was "surprising" consensus. The Copa Canon archive page requires manual daily updates. The shareable cards require manual number entry at V1. These are all acceptable V1 tradeoffs for a zero-budget launch.

---

# Research Reports

[All Generation 2 and Generation 3 research reports preserved below — unchanged]

---

# Research Report — Generation 2

*Completed: Generation 2*
*This is a research document only. No concept has been named or designed.*

---

## Area 1: Viral Daily Games — Findings

### Games Researched
- Wordle, NYT Connections, Heardle, GeoGuessr (daily), Immaculate Grid, Globle, Worldle, Poeltl, Framed

### Key Findings

**Wordle** (NYT, ~40M daily users at peak)
- Mechanic: One 5-letter word per day. Six guesses with color-coded feedback. Same word globally.
- Spread mechanism: The emoji grid output — shareable, spoiler-free, legible as a social signal.
- Daily return driver: Scarcity. One puzzle per day, non-bingeable.
- Core hook: Shared constraint. The communal element is not a feature — it IS the product.

**NYT Connections** (NYT, fastest-growing game post-Wordle)
- Mechanic: 16 words grouped into 4 hidden categories of 4. Difficulty tiered by color.
- Spread mechanism: Colored square output encoding difficulty tier → you can see that someone cracked purple first, instantly legible.
- Core hook: The categories are designed to be deceptively tricky — "things that can precede HOT." The 'aha' moment is explainable in conversation, which drives talk.

**Heardle** (Spotify, ~18 months of massive play)
- Mechanic: Identify a song from progressively longer audio clips. 1 second → 16 seconds.
- Core hook: Cultural identity signal. Getting it in 1 second is proof of who you are, not just skill.

**GeoGuessr** (~40M registered users)
- Mechanic: Dropped into Street View. Read visual cues to identify location. Click on world map.
- Spread mechanism: The map screenshot showing your pin vs. actual location. The *gap* is the shareable.
- Core hook: Reading and narrowing, not predicting. The answer exists. You're finding your way to it through observation.

**Immaculate Grid**
- Mechanic: 3×3 grid. Each cell requires a player who satisfies two intersecting criteria (played for both teams, met two stats). One guess per cell.
- Core hook: Constraint satisfaction. You're not picking a winner — you're navigating a puzzle with a right answer that may surprise you.

**Globle / Worldle**
- Mechanic: Guess a mystery country. Wrong guesses yield distance/direction feedback.
- Core hook: Iterative narrowing under live feedback. You improve in real time, not locked in advance.

**Poeltl**
- Mechanic: Guess an NBA player via attribute matching (team, position, height, age).
- Core hook: Deductive inference. Building a mental model and revising it.

**Framed**
- Mechanic: Identify a movie from a single still frame. Wrong guess reveals next frame.
- Core hook: Cultural identity signal. Obscure knowledge has social value.

### Pattern: What Viral Daily Games Share

1. **One thing per day, same for everyone.** Scarcity + simultaneity creates shared experience.
2. **The share encodes a story, not just a result.** Wordle grid = outcome + struggle. GeoGuessr screenshot = outcome + geographic gap.
3. **No expertise required to participate; expertise creates a different quality of experience.**
4. **The mechanic is READING or NARROWING, not PREDICTING.**
5. **Failure is as shareable as winning.**

---

## Area 2: Group Social Games — Findings

### Games Researched
- skribbl.io, Gartic Phone, Jackbox (Quiplash, Drawful), Among Us, Kahoot

### Key Findings

**skribbl.io**
- Group dynamic: The drawing is public and evolving. The comedy lives in the gap between intended drawing and actual drawing.

**Gartic Phone**
- Group dynamic: Telephone + drawing. A phrase corrupts through multiple individual interpretations.
- Core insight: **Collective misinterpretation IS the entertainment.**

**Jackbox / Quiplash**
- Core insight: **Being evaluated by known people raises stakes enormously vs. anonymous leaderboards.**

**Among Us**
- Core insight: **Asymmetric information + social performance = memorable group moments.**

**Kahoot**
- Core insight: Being 0.2 seconds slower than a friend on the same question you both knew is surprisingly activating.

### World Cup Group Chat Behaviors (Documented)
- The meme drop, the hot take cascade, the role emergence, the villain designation, the "I called it" energy.

### Key Insight
Group games create memorable moments through **asymmetric information + social performance**.

---

## Area 3: Non-Prediction Sports Games — Findings

- Twitter/X spikes during Super Bowl ads. Squares pools survive gambling legalization.
- 2022 World Cup: Morocco's narrative (African nation, incredible run, diaspora emotion) became the product.
- Drive to Survive doubled F1 US viewership among under-35 by making sport a vehicle for human storylines.

### Key Insight
Non-prediction sports entertainment works via **characters, drama, and belonging to a story**.

---

## Area 4: Role / Allegiance Games — Findings

- Werewolf / Diplomacy: assigned roles create different psychology than chosen roles.
- **Assigned allegiance creates different psychology than chosen allegiance.** You defend something you didn't ask for more fiercely.

---

## Area 5: Between-Match Behavior (Gap Days) — Findings

Gap-day behaviors: YouTube highlights, meme production, argument maintenance, player discovery, table watching, anticipation content.

**The Unnamed Gap-Day Work:** Fans are performing tournament narrative construction between matches. No formal container exists.

---

## Cross-Area Synthesis: Five Convergent Patterns

1. The shareable artifact must tell a story, not just a score.
2. Collective constraint is more powerful than individual achievement.
3. Assigned roles beat chosen ones for engagement depth.
4. The gap between intention and outcome is the entertainment.
5. Non-experts are the growth market; the mechanic must not penalize them.

---

## Mechanic Seeds — Generation 2

**SEED 1: The Narrative Tribunal** — jury verdict on disputed moments
**SEED 2: The Assigned Correspondent** — cover an assigned nation
**SEED 3: The Rival Reading** — your reading vs. opposing fan bases
**SEED 4: The Reputation Ledger** — crowd-assigned narrative roles for players
**SEED 5: The Attribution Game** — distribute blame/credit for match outcomes

---

# Research Report — Generation 3

*Completed: Generation 3*

---

## Deepening Area 1: Daily Return Mechanics

- Streak maintenance is #1 retention driver in Wordle (NYT internal data).
- Irreversibility mechanic: something about today's engagement that cannot be undone.
- GeoGuessr daily: 24-hour comparison window. After 24 hours, score can't be compared to friends'.
- Immaculate Grid: one attempt per cell, ever. Permanent record.

**New Pattern:** Best daily games incorporate irreversibility. Today feels real because it cannot be repeated.

---

## Deepening Area 2: Reveal Structures in Group Games

Three types: Sequential (Gartic Phone), Interactive (Quiplash — voting during reveal), Resolution (Among Us).

**Key insight:** Interactive reveals are most shareable — the reaction to the reveal is itself content.

---

## New Area: Games Built on Real-World Events as Content

**Herd Mentality:** Match the majority — social modeling, not correctness.
**Hollywood Stock Exchange:** Virtual market on real events. Your action changes the price. Collective intelligence production, not forecasting.
**KnowYourMeme:** Multiple interpretations compete; the dominant one becomes canon. Canon formation is competitive.

---

## New Area: The "What Does the Crowd Think?" Mechanic

**Family Feud:** Survey says — second-order social modeling.
**Scruples:** What would most people do?
**"Guess the Stats" format:** Most engaging variant is "what do you think the crowd will say?" not "what do you think?"
**Keynes Beauty Contest:** Winning strategy is modeling other judges, not expressing personal preference.

**Core Insight:** Football expertise may be a disadvantage when the question is crowd psychology, not technical correctness.

---

## Monetization Evidence (Deep Pass)

- GeoGuessr: ~$15M ARR, 1.5% conversion of 40M users to $24/year Pro tier.
- Jackbox: One buyer per group. Group Chat Organizer pays. Everyone else free.
- Sponsored moments: sports media precedent (MLB Statcast, Sky Sports sponsored segments).
- Patreon failure: Flagle 0.1% conversion = hobby, not business.

**V1 monetization: Group Hosting + Sponsored Moments only.**

---

## Gap-Day Behavior (Quantified Pass)

- Post-match highlight videos: 80%+ of views within first 24 hours.
- "Can X still qualify?" content peaks on gap days.
- Player discovery content peaks immediately after breakout performances, decays within 48 hours.
- Reddit post-match threads active 12-24 hours after match.
- "Was [controversial call] correct?" threads run 48-72 hours.

**The Unnamed Gap-Day Work:** Tournament narrative construction — deciding heroes, villains, turning points. Happens everywhere informally, has no formal container.

---

## New Mechanic Seeds — Generation 3

**SEED A: Canon Vote** — select defining moments per match; accumulates into crowd-authored tournament record
**SEED B: Crowd Read** — estimate what % of crowd agrees with a call; social modeling score
**SEED C: Reputation Market** — early narrative calls on players earn more than late consensus
**SEED D: Interpretation Gap** — read moments on spectrums; see gap vs. fan camps
**SEED E: Streak Correspondent** — assigned nation, daily observations, permanent dispatch log

---

## Seed Assessment

| Seed | Prediction? | Fantasy? | World Cup Specific? | Expert Advantage? | Viral Strength |
|------|------------|---------|-------------------|-----------------|----------------|
| A: Canon Vote | No | No | Yes | No | High |
| B: Crowd Read | No | No | Yes | Reversed | High |
| C: Reputation Market | No | No | Yes | No | Med-High |
| D: Interpretation Gap | No | No | Yes | No | High |
| E: Correspondent | No | No | Yes | No | Medium |

**Strongest:** B (Crowd Read) for viral + accessibility. A (Canon Vote) for World Cup specificity + legacy.

Copa Reads combines B + A + elements of D into a single daily game.
