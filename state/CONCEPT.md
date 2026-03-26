# Copa — Product Concept

## What It Is
Copa is a fantasy sports game built for the 2026 FIFA World Cup, designed to run **inside a betting partner's platform**. It gives bettors a reason to stay engaged across all 104 matches — not just the ones they've wagered on.

**Tournament window:** June 11 – July 19, 2026

---

## How It Works (Player Experience)

1. Player pays a **$10 one-time entry fee** and selects four national teams — one per position slot: GK, DEF, MID, FWD.
2. Every **winning bet placed on the partner platform** earns the player a **spin ticket**.
3. Spins unlock **traits** that strengthen their squad: country kits, position abilities, cleat multipliers, and live match boosts.
4. Squad **locks before the knockouts** — score builds across every remaining fixture.
5. **Leaderboard updates live** during every match. Prize pool pays out at the Final.
6. Partner can **issue free spin bundles** as a promotional tool for any campaign: deposit bonuses, first bets, referrals, seasonal offers.

---

## Key Numbers

| Stat | Value |
|------|-------|
| Total matches | 104 |
| Engagement per squad | 48 days |
| Entry fee | $10 per squad |
| Prize pool | 80% of entry fees |
| Partner revenue share | 20% of entry fees |

---

## The Business Model (Partner Revenue)

Based on players averaging one $25 bet/day from June 1 through the Final (48 days):

| Players | Daily Bet Volume | Total Bet Volume | Entry Fees | Partner Rev Share (20%) | Prize Pool |
|---------|-----------------|-----------------|------------|------------------------|------------|
| 100 | $2,500 | $120,000 | $1,000 | **$200** | $800 |
| 1,000 | $25,000 | $1,200,000 | $10,000 | **$2,000** | $8,000 |
| 10,000 | $250,000 | $12,000,000 | $100,000 | **$20,000** | $80,000 |

*Bet volume figures represent incremental activity driven by Copa engagement. Multiple entries per player are permitted, increasing entry fee revenue.*

---

## What the Partner Gets

- **Retention** — players return to check live scores across all 104 matches, not only ones they bet on
- **Bet frequency** — spin tickets are tied directly to winning bets on their platform
- **Promotional flexibility** — deploy free spins as reward for deposits, referrals, first bets, or any campaign
- **Exclusivity** — Copa is available to one partner platform per market
- **Revenue share** — 20% of all entry fees collected in their market
- **Zero rebuild** — a single webhook is all the integration requires

---

## Integration Requirements

Single webhook integration. No backend rebuild required on the partner's side. Copa handles:
- Squad selection and leaderboard
- Spin logic and trait assignment
- Match score tracking
- Prize pool management

Partner provides:
- Webhook event when a bet resolves as a win (anonymized bet ID, player ID, timestamp)
- Branded placement within their platform (banner/widget/tab)
- Distribution to their player base

---

## Pitch Framing

> Your players bet on matches. Copa gives them a reason to stay for all 104 of them.

Copa only works because of the partner's platform. That is the partnership.
