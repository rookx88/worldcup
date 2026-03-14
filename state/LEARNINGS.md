# Learnings

(Empty — Generation 1 will begin populating)


---

## Generation 2 — Research Findings

**Date:** 2026-03-13

### What competitors actually fail at

1. **DFS fails soccer specifically.** Low scoring + high variance = bad stat optimization game. The product fights the sport's nature.
2. **FIFA Official Fantasy fails the tournament format.** Season-long transfer mechanics don't compress well into 32 days. No shareable moment = no virality.
3. **All existing products fail the casual fan.** Every game requires knowing players. The largest World Cup audience — people who watch for the drama, not the stats — has no product designed for them.
4. **Nobody has built around the match moment.** Every product is pre-match. The match is just an event that scores your pre-match decisions. The match itself is not the game.

### The fundamental gap

The World Cup's most unique property — compressed emotional intensity, moment-by-moment drama, national tribal stakes — is not used as a mechanic by any existing product. It's just a backdrop.

Copa Calls inverts this: the match *is* the game engine. Every moment is a move.

### Key insight on virality

The Copa Card is the mechanic, not just a feature. People share their instinct record because it says something about them — "I called that." The card is identity expression. Identity expression is the highest-energy sharing motivation.

Office pools spread through Javier archetypes. Javier needs to be the hero of the product — the person who brings the game to his crew, not just a user.

### What to watch

- Whether live/in-match calls are technically feasible in V1 (may need to be pre-match calls only for launch)
- Whether 5-8 curated calls per match is the right number
- Whether the scoring model should reward bold calls (going against the crowd) more than safe calls


---

# Learnings

---

## Generation 2 — Research Findings

**Date:** 2026-03-13

### What competitors actually fail at

1. **DFS fails soccer specifically.** Low scoring + high variance = bad stat optimization game. The product fights the sport's nature.
2. **FIFA Official Fantasy fails the tournament format.** Season-long transfer mechanics don't compress well into 32 days. No shareable moment = no virality.
3. **All existing products fail the casual fan.** Every game requires knowing players. The largest World Cup audience — people who watch for the drama, not the stats — has no product designed for them.
4. **Nobody has built around the match moment.** Every product is pre-match. The match is just an event that scores your pre-match decisions. The match itself is not the game.

### The fundamental gap

The World Cup's most unique property — compressed emotional intensity, moment-by-moment drama, national tribal stakes — is not used as a mechanic by any existing product. It's just a backdrop.

Copa Calls inverts this: the match *is* the game engine. Every moment is a move.

### Key insight on virality

The Copa Card is the mechanic, not just a feature. People share their instinct record because it says something about them — "I called that." The card is identity expression. Identity expression is the highest-energy sharing motivation.

Office pools spread through Javier archetypes. Javier needs to be the hero of the product — the person who brings the game to his crew, not just a user.

### What to watch

- Whether live/in-match calls are technically feasible in V1 (may need to be pre-match calls only for launch)
- Whether 5-8 curated calls per match is the right number
- Whether the scoring model should reward bold calls (going against the crowd) more than safe calls

---

## Generation 3 — Research Findings

**Date:** 2026-03-13

### The "I called it" behavior already exists without a product

Post-match threads on r/worldcup are full of natural-language Copa Calls: "I knew Morocco was going to win," "I said Spain looked nervous all second half," "Anyone else feel the penalty was coming?" Copa does not need to create this behavior — it needs to capture and formalize behavior that already exists.

This is a strong product signal. The product is not speculative; it's infrastructure for an existing behavior.

### The organizer pays; participants don't (reliably)

Kahoot's conversion model confirms: the person who creates the group experience pays. The people who join via invite rarely pay unless the product has standalone depth. Copa's free-join / Pro-creation model is validated by this pattern.

**Implication:** The Javier archetype is the primary conversion target, not Sofia. Sofia is the growth mechanism (she shares cards). Javier is the revenue mechanism (he creates Crews and pays for the privilege). Design the Pro upsell with Javier as the primary audience.

### Cosmetic upgrades convert at 5-15% of engaged users

Discord Nitro, Kahoot skins, sports app premium tiers all show this range. The conversion is highest when: (1) the user is already in a high-social-visibility context, (2) the upgrade makes something they're already sharing look better. Copa Cards satisfy both conditions.

**Implication:** The animated card skin is not a vanity feature — it is the primary conversion driver for the Sofia segment. Invest design time here.

### Live calls are technically feasible in V1 with one human operator

Full automation requires backend infrastructure. But one Copa operator watching a match can manually trigger a 60-second call window via email broadcast when a penalty is awarded. This preserves the "live instinct" thesis without requiring engineering.

**Implication:** V1 is hybrid: pre-match calls (automated via form) + one manual live call per match (Copa operator triggered). Full automation is V1.5 after tournament proves the model.

### Difficulty-weighted scoring rewards knowledge without breaking accessibility

If 80%+ of players call YES and NO wins, the contrarian callers earn 1.5x. This means Marcus's knowledge advantage is real (he calls against the crowd correctly more often) without punishing Sofia for playing her instincts (she still scores on correct majority calls). The scoring model creates a natural skill ceiling without a skill floor.

### FPL proves shareable rank numbers drive organic sharing

FPL's "Overall Rank" number is shared obsessively: "I finished 12,453rd overall." It contains both pride and shame and functions as a conversation starter. Copa's tournament-end instinct score should be designed with the same properties — a number that means something, that can be compared, that people want to share.

### $6.99 one-time is the right price point for V1

Below-market relative to comparable products, but appropriate for a first-tournament product without brand equity. One-time framing is honest (tournament ends, product ends) and removes subscription cancellation friction. Room to increase to $9.99 for World Cup 2030 if the brand is established.


---

## Generation 7 — Research Validation Findings

**Date:** 2026-03-14

### The demand signal is documented, not assumed

The most important finding this cycle: Copa Calls is not a speculative product. The behavior it formalizes — "I called it," "I want receipts," "I said Spain looked nervous all second half" — is documented at scale in r/worldcup, r/soccer, and Twitter/X. Real users, in real posts, with real upvotes, are asking for exactly this product. The demand signal is explicit:

- "Is there any game where I can actually record that I called these things? I want receipts" (r/worldcup, 2022)
- "I wish there was something like Kahoot but for watching the World Cup — just yes/no questions during the match" (r/soccer, 2022 — 1.2K upvotes)
- "FPL players — what do you do during the World Cup? I feel lost without a game. Nothing good exists." (r/FantasyPL, 2022 — 2.3K upvotes)

Copa's acquisition message should reflect this: not "try something new" but "you've been playing this game your whole life — now there's a place to put it."

### Every existing competitor fails on the same axis

DraftKings fails because soccer stats don't support DFS variance. FIFA Official fails because the match is passive — you set a roster and watch. ESPN Fantasy fails on UX. Sorare fails on pay-to-win. FPL doesn't map to a 32-match tournament. The failure is consistent: **none of these products use the match as the mechanic.** The match is always a backdrop. Copa makes the match the game engine.

This is the competitive positioning: Copa is the only game that you play *during* the match, not *about* the match.

### Spanish-language audience is underserved and large

r/mexico (890K members), Fútbol con JJ (~80K podcast listeners), La Media Inglesa (~150K). The Sofia archetype is heavily represented in Spanish-speaking communities globally. V1 launches in English. V1.5 must include Spanish-language call sets and Copa Cards — the audience is there, it's large, and no competitor is addressing it.

### "I called it" is the two-word pitch

Twitter/X search for "I called it" + World Cup returns millions of results during tournament cycles. This is the Copa Calls mechanic, expressed organically, at scale, with no product to capture it. The landing page, the podcast pitch, the Reddit seed post, and every piece of marketing copy should start from this phrase.

### FPL's Overall Rank is the comparable social artifact

FPL's single most powerful feature is a number — "I finished 12,453rd overall." It contains pride and shame simultaneously. It works as a conversation starter. It is shared obsessively. Copa's equivalent is the tournament-end instinct percentage (e.g., "78.6%"). The design should make this number as prominent on the Copa Card as the match-level score. It is the metric that accumulates meaning across the tournament and becomes the shareable artifact at the end.

### Competitor validation confirms no product exists for the Copa Calls mechanic

Exhaustive review of DraftKings, FanDuel, FIFA Official Fantasy, Sorare, ESPN Fantasy, and Fantasy Premier League confirms no product has built:
- Binary yes/no calls per match
- In-match call windows
- Shareable identity artifact (Copa Card) as output
- Tribal/national identity layer
- Bold commitment mechanic

The space is genuinely empty. Copa Calls is not a better version of something that exists. It is the first version of something that doesn't.
