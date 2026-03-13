# Monetization

*How Copa makes money. First-class concern — not a Phase 2 afterthought.*

## Status
**Resolved** — Generation 3 research complete. Model defined with evidence base.

---

## The Model: Copa Pro — $6.99/tournament (one-time)

### Why One-Time, Not Subscription
The tournament runs 32 days. Subscription pricing implies ongoing value. Copa Pro is a one-time purchase for tournament access — this framing is honest, matches how fans think about World Cup (a finite event), and removes the "I'll cancel after" friction that lowers subscription conversion.

### Why $6.99, Not $4.99 or $9.99
Evidence from comparable zero-budget viral products:
- Kahoot Pro: $9.99/month
- Discord Nitro: $9.99/month
- Fantasy sports Pro tiers: $5-$20/season
- Wordle/NYT Games: $5/month

$4.99 is below the psychological floor for "real product." $9.99 is above the "impulse buy" threshold for a first-time product without brand equity. $6.99 sits in the zone where the purchase feels considered but not costly. One-time framing makes it feel smaller than a monthly subscription at the same price.

---

## Free vs. Pro Feature Split

### Free Tier (must remain excellent)
- Play all calls for every match
- Receive standard Copa Card after each match (nation skin)
- Join one Copa Crew (cannot create)
- Tournament leaderboard access (read-only)

**Rule:** The free card must look good enough to post. This is not generosity — it's the growth mechanism. A bad free card kills sharing, kills virality, kills the paid funnel.

### Pro Tier — $6.99/tournament
Designed to serve three distinct psychological motivations:

**Identity Expression (Sofia — largest segment):**
- Animated Copa Card skin
- Nation-exclusive visual frames for milestone moments
- "Copa Pro" badge on public leaderboard

**Organizer Power (Javier — viral vector):**
- Create up to 3 Copa Crews
- Crew admin tools (rename, invite, remove)
- Early call access (30 minutes before free players)
- Crew vs. Crew challenge mode

**Knowledge Proof (Marcus — retention anchor):**
- Extended analytics: call-type percentile breakdown
- "You called penalties at 71% — top 3% of Copa" stat cards
- Best call of tournament highlight with social share
- Full Copa record exported as PDF

---

## Conversion Architecture

### The Paywall Rule
**Never gate participation. Gate creation and depth.**

- Joining a Crew: free (Sofia joins Javier's Crew without paying)
- Creating a Crew: Pro (Javier pays to be the organizer)
- Playing calls: free
- Seeing your own detailed analytics: Pro

This preserves the viral loop (Javier brings 15 friends free) while creating a real reason for Javier to pay.

### Conversion Triggers by Archetype

| Archetype | Trigger Moment | Upsell Message |
|-----------|---------------|----------------|
| Sofia | After first Copa Card received + shared | "Your card, but animated — Copa Pro" |
| Javier | At Crew creation wall | "Create your Copa Crew → upgrade takes 30 seconds" |
| Marcus | After 5th Copa Card, blur the analytics | "You're calling set pieces better than most Copa players. See your full breakdown." |

### What Not to Do
1. Don't upsell before first Copa Card delivered — players haven't experienced the product
2. Don't make free cards look bad to make Pro look good — free cards drive sharing, sharing drives the paid funnel
3. Don't paywall Crew joining — every gate on the invite link breaks the Javier viral loop
4. Don't subscription-price — the tournament ends, the product ends, one-time is honest

---

## Referral Mechanic

**Trigger:** After Pro purchase
**Mechanic:** Pro purchaser gets a unique referral link. Friend goes Pro via their link → referrer earns "Copa Legend" badge for rest of tournament.

**Why a badge, not cash:** Cash referrals require backend infrastructure. A badge is free to implement and hits the same identity nerve that drove the Pro purchase.

**V1 implementation:** Manual. Send referral code by email post-purchase. Track in spreadsheet.
**V1.5:** Referral link with UTM tracking → Stripe webhook → automatic badge grant.

---

## Revenue Projections (Conservative)

| Engaged Users | Pro Conversion (7%) | Revenue |
|--------------|---------------------|---------|
| 10,000 | 700 | $4,893 |
| 50,000 | 3,500 | $24,465 |
| 100,000 | 7,000 | $48,930 |
| 200,000 | 14,000 | $97,860 |

**Conversion rate basis:** Kahoot/Discord comparable data suggests 5-15% of engaged users convert to paid. Modeling at 7% (conservative). "Engaged" means has shared at least one Copa Card.

**The 2026 World Cup context:** 5+ billion viewers globally. Capturing 0.002% of that as engaged Copa users = 100,000 users. This is not an optimistic target — it's a realistic ceiling for a zero-budget first-tournament product.

---

## Future Monetization Surfaces (Post-V1)

These are not V1 — they are options to evaluate after the tournament proves the model:

1. **Copa Crew Pro** — Teams/organizations buy Crew Pro for entire group (one payment, 20 seats). Enterprise angle for office pools.
2. **Sponsored call series** — A brand sponsors the "First Goal" call series. Every Copa Card for that match shows the brand frame. Non-intrusive, high-impression.
3. **Copa Archive** — After tournament ends, pay $1.99 to download your complete Copa record as a tournament keepsake. Low-priority but zero-cost to add.
4. **Copa 2028** — If the product proves out for World Cup 2026, the brand and mechanics port directly to Euro 2028, Copa América, Olympics. The model repeats.
