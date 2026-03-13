# Monetization

*How Copa makes money. This is a first-class concern — not a Phase 2 afterthought.*

## Constraint
- Zero budget for paid acquisition — monetization must work organically
- Must be live before or at tournament start (June 18, 2026)
- Must not break the core experience for free players — growth depends on free users sharing

## Status
**Resolved — primary and secondary models selected based on competitive research.**

---

## Research Summary

### What comparable products actually earn

| Product | Model | Notes |
|---------|-------|-------|
| DraftKings | Rake on entry fees (10–15%) | Requires gambling license — not available to Copa |
| FIFA Official Fantasy | $0 — brand marketing tool | Proves free works for engagement; proves nothing about revenue |
| Sorare | NFT pack sales + resale fees | Collectible instinct is real; NFT mechanism is not the answer |
| Sleeper | Freemium (Sleeper+, $5/mo or $40/yr) + Pick'em rake | Best comparable — social fantasy, free core, premium upgrade |
| FPL | $0 — engagement tool for Sky ecosystem | No native monetization |
| NYT Games | $5/month subscription (Connections, Wordle, etc.) | Casual players will pay for a good daily game experience |
| Reigns | $2.99 one-time purchase | Simple novel mechanic, 1M+ sales |

### Key findings
1. **Freemium works** — Sleeper demonstrates 2–5% free-to-paid conversion in social sports apps. At 10,000 players, that's 200–500 paying users.
2. **One-time purchases beat subscriptions for tournament-format products** — a defined end date reduces subscription commitment anxiety.
3. **The group organizer (Javier) is the motivated buyer** — he's already spending on the group experience (food, bracket entry). A small fee to create a private league is below conscious spending threshold.
4. **Cosmetic differentiation has real willingness-to-pay** — Sorare proved this (even without the NFT model). Premium card treatment = identity expression.
5. **Entry fee contests are blocked** — gambling license required; zero-budget path is not available.
6. **Advertising doesn't work at launch scale** — requires volume Copa won't have in V1.

---

## Primary Model: Copa Pro Tournament Pass

**Price:** $4.99 (one-time, covers full tournament: June 18 – July 19, 2026)

**What Pro unlocks:**

| Feature | Free | Pro |
|---------|------|-----|
| Make picks for every match | ✅ | ✅ |
| Receive Copa Card after each match | ✅ | ✅ |
| Join a group league | ✅ | ✅ |
| Standard card skin (dark navy) | ✅ | ✅ |
| **Premium card skin (gold foil treatment)** | ❌ | ✅ |
| **Full percentile breakdown** (pick-by-pick, not just overall) | ❌ | ✅ |
| **Streak tracking** (consecutive correct results) | ❌ | ✅ |
| **Group league Pro badge** (name appears with crown icon) | ❌ | ✅ |
| **Early form unlock** (30 min before public) | ❌ | ✅ |

**Why $4.99:**
- Below the $5 psychological threshold
- One coffee — low decision friction
- Less than any DFS deposit minimum
- One-time for a 32-day tournament = high perceived value vs. $5/month recurring

**Why these features:**
- Gold card skin = identity expression. Pro players look different in group leagues. This drives visible status distinction within the social layer.
- Streak tracking = retention mechanic. Gives Marcus something to optimize for beyond a single match.
- Early form unlock = minor but feels elite. Creates a moment of "I'm in before everyone else."

---

## Secondary Model: Group League Creator Fee

**Price:** $2.99 (one-time, per league created)

**Joining a league is always free.**

**Who pays:** Javier — the group organizer. He creates the league, shares the link. His friends join for free.

**Why Javier pays:**
- He's already invested in the group experience (organizing, tracking, bragging)
- $2.99 is below conscious deliberation — it's the cost of parking, not a decision
- He gets a "Group Organizer" badge in the league view (visible status)
- He gets a shareable group report card auto-generated at end of each round (exclusive to paid leagues)

**Beta exception:** First 500 group leagues created are free — reward early adopters, generate proof-of-sharing before introducing the fee. Once the tournament is live and the product is demonstrated, the creator fee activates.

---

## Revenue Forecast

| Scenario | Players | Pro conversion | Pro revenue | Groups paid | Group revenue | Total |
|----------|---------|---------------|-------------|-------------|---------------|-------|
| Conservative | 2,000 | 3% | $299 | 30 | $90 | ~$390 |
| Base | 10,000 | 3% | $1,497 | 150 | $449 | ~$1,950 |
| Upside | 50,000 | 4% | $9,980 | 600 | $1,794 | ~$11,774 |

**Realistic target:** $1,500–$3,000 for the 2026 tournament.

This is not the end state. It's the proof of concept. The data from this tournament answers: what do players pay for? That determines the 2028 (Euro) and 2030 (WC) model.

---

## What Stays Free Forever (Non-Negotiable)

- Making picks before every match
- Receiving your Copa Card after every match
- Joining a group league
- Appearing on group leaderboards

**Rationale:** The free product is the growth engine. Sofia sharing her card is how new players find Copa. If the card is paywalled, the viral loop breaks. Monetization must sit *above* the viral loop, not inside it.

---

## Payment Infrastructure

**V1:** Stripe Checkout — simplest integration, no backend needed for basic payment flows. Copa Pro purchase generates a confirmation email with a "Pro code" the player enters in their next form submission. Manual validation for V1.

**V2:** Account system with Stripe-linked Pro status. Auto-applied to cards and group view.

**Stripe fees:** 2.9% + $0.30 per transaction. At $4.99, net revenue per sale = ~$4.54. At $2.99, net = ~$2.60.

---

## Open Questions (Next Generation)
1. Should Copa Pro be purchasable before any picks are made, or only after the first free card is received? (Post-first-card purchase is higher-converting based on SaaS "aha moment" research — but requires more infrastructure)
2. Is there a referral incentive — e.g., "share this link, if a friend goes Pro you get a free upgrade"? This could accelerate paid conversion without paid ads.
3. Should the gold card skin be visible to non-Pro players who receive a shared card? (Yes — this is a passive ad for Pro. The shared card should say "Copa Pro" somewhere subtle.)
