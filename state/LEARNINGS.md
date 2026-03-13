# Learnings

*Distilled insights Copa has accumulated. Updated when something important is learned.*

---

(Empty — Generation 1 will begin populating)


---

## Generation 1 — Competitive Landscape & Audience Research

**Date:** 2026-03-13

### What every existing product gets wrong
Every competitor (DraftKings, FIFA Fantasy, Sorare, ESPN, FPL) optimizes for players who already know the players. The mechanic is always: build a roster → accumulate points → check a number. This structurally excludes the casual World Cup fan who wakes up for the tournament but doesn't follow club football.

### The sharing problem no one has solved
The most viral World Cup content is prediction-based ("I called that upset"), not stat-based ("my player scored 12 fantasy points"). Zero existing products produce a shareable artifact tied to a specific prediction. This is the gap.

### The knowledge barrier is the real product problem
It's not that casual fans don't want to play fantasy — they're already playing informally in group chats. The barrier is that all existing products require knowledge of 30+ players to participate meaningfully. Solving the knowledge barrier (e.g., curated shortlists instead of full squads) is what unlocks the casual market.

### The Javier multiplier
The most efficient acquisition path is through group organizers (Javier archetype) who bring 8–12 casual players with one share. The group league invite link is a more important feature than any marketing channel. Build the sharing mechanic before building the scoring system.

### Sofia defines the product
Building for Marcus (the fantasy-literate player) produces something Sofia won't use. Building for Sofia produces something Marcus can still enjoy. Sofia is the primary persona for all V1 product decisions.

### 2026 host country angle is underleveraged
Every competitor ignores the US/Mexico/Canada host market. USMNT, LigaMX, and Mexican soccer communities are specifically primed for casual engagement with the 2026 World Cup. Spanish-language support could be a meaningful differentiator at low cost.


---

# Learnings

*Distilled insights Copa has accumulated. Updated when something important is learned.*

---

## Generation 1 — Competitive Landscape & Audience Research

**Date:** 2026-03-13

### What every existing product gets wrong
Every competitor (DraftKings, FIFA Fantasy, Sorare, ESPN, FPL) optimizes for players who already know the players. The mechanic is always: build a roster → accumulate points → check a number. This structurally excludes the casual World Cup fan who wakes up for the tournament but doesn't follow club football.

### The sharing problem no one has solved
The most viral World Cup content is prediction-based ("I called that upset"), not stat-based ("my player scored 12 fantasy points"). Zero existing products produce a shareable artifact tied to a specific prediction. This is the gap.

### The knowledge barrier is the real product problem
It's not that casual fans don't want to play fantasy — they're already playing informally in group chats. The barrier is that all existing products require knowledge of 30+ players to participate meaningfully. Solving the knowledge barrier (e.g., curated shortlists instead of full squads) is what unlocks the casual market.

### The Javier multiplier
The most efficient acquisition path is through group organizers (Javier archetype) who bring 8–12 casual players with one share. The group league invite link is a more important feature than any marketing channel. Build the sharing mechanic before building the scoring system.

### Sofia defines the product
Building for Marcus (the fantasy-literate player) produces something Sofia won't use. Building for Sofia produces something Marcus can still enjoy. Sofia is the primary persona for all V1 product decisions.

### 2026 host country angle is underleveraged
Every competitor ignores the US/Mexico/Canada host market. USMNT, LigaMX, and Mexican soccer communities are specifically primed for casual engagement with the 2026 World Cup. Spanish-language support could be a meaningful differentiator at low cost.

---

## Generation 2 — Game Design

**Date:** 2026-03-13

### The card is the product, not the game
The game mechanic exists to produce the card. The card is what gets shared. This means visual quality of the card is more important than scoring complexity. A beautiful card with simple scoring beats a sophisticated scoring system with an ugly output.

### V1 can be manual — and that's fine
Technology is irrelevant until we know the card gets shared. A Typeform collecting picks + a Canva template filled in manually + an email with the card image = a complete V1. This can launch in days, not weeks. The lesson from other fantasy products: they built complex backends before validating that anyone wanted to share the result. We validate first.

### The email-to-get-card mechanic is a natural waitlist builder
By requiring an email to receive your result card, we collect emails from every person who plays — without a separate waitlist flow. The waitlist and the product are the same thing. First-match plays become signup data automatically.

### Boldness tiers (not odds numbers) reduce cognitive load for casual players
Showing "Chalk / Bold / Daring / Heroic" is more intuitive than showing odds (e.g., -350 / +220). Casual fans understand "risky vs. safe" without understanding betting markets. The tier system also creates vocabulary — players will say "I went Heroic on the scorer and it paid off" which is inherently shareable language.

### The Upset Meter asymmetry is the key mechanic innovation
Zero downside for calling an upset that doesn't happen (you just get 0 on that pick, same as if you hadn't picked). Full upside if you're right. This removes the fear of committing to a bold prediction — the worst case is neutral. This is what will encourage Sofia to go big rather than hedge, which in turn creates the shareable moments.

### Maximum score (160 pts) must feel narratively achievable
If the max is only achievable by luck, players won't feel like skill matters. If it's easily achievable, there's no aspiration. 160 pts is right: you need a genuine upset AND you need to have committed to it at slider 5 AND your Heroic scorer pick needs to score. It requires luck AND courage simultaneously. That combination is a story.

### Group league is Javier's product; individual cards are Sofia's product
These are two slightly different products sharing the same mechanic. Don't conflate them in the UI. Sofia wants her card. Javier wants his group standings. V1 can serve both with a spreadsheet + card email, but V2 needs to design these as distinct experiences.


---

---

## Generation 3 — Monetization Research

**Date:** 2026-03-13

### The freemium conversion rate benchmark is 2–5%
Sleeper (the closest comparable — social sports app, free core game, premium upgrade) demonstrates 2–5% free-to-paid conversion. At 10,000 players, that's 200–500 paying users. This is the baseline assumption for Copa's revenue model. Don't assume higher without evidence.

### One-time tournament passes beat monthly subscriptions for event-based products
A defined end date (June 18 – July 19) reduces subscription commitment anxiety. Players are more willing to pay $4.99 once for a tournament than $4.99/month for a recurring product they'll cancel. Match the payment structure to the product structure.

### The group organizer (Javier) is the motivated buyer for group features
The person who creates the group has already invested in the experience. $2.99 to create a private league is below conscious deliberation for someone who's already organized a watch party. The joining experience must stay free — the creation fee is Javier's contribution, not Sofia's.

### Cosmetic differentiation has real willingness-to-pay
Sorare proved that digital card aesthetics drive purchasing behavior, even before the NFT mechanic inflated prices. A gold/foil card skin for Pro players is not frivolous — it's identity expression within the social layer, and it creates a passive advertisement when the Pro card is shared publicly.

### The "aha moment" is the right moment to upsell
The optimal conversion moment is immediately after the first card is received — not before. The player has just experienced the product. The upsell email ("want the gold version next time?") should fire automatically after the first card delivery. SaaS conversion research consistently shows that upsells after the value moment outperform pre-experience paywalls.

### FIFA Official Fantasy proves free engagement doesn't imply revenue
FIFA built a product with millions of users and made approximately zero money from it directly. "Lots of users" is not a revenue model. Copa must have Stripe live before the tournament starts — not after.

### The shared card must show what Pro looks like
When a Pro player shares their gold card, every viewer sees the Pro treatment. The card is a passive advertisement for the upgrade. This requires Pro cards to be visually distinct enough that a casual viewer notices, but not so different that it makes free cards look bad. The gold foil border solves this — it's an enhancement, not a replacement.

### Gambling license is the real barrier to rake-based models
DraftKings' entire business model (10–15% rake on entry fees) is blocked by regulatory requirements. Copa cannot pursue this path at zero budget. The one-time pass and creator fee models are the only viable options for a zero-budget operation. This is not a limitation — it's a positioning advantage. Copa is not a gambling product, which makes it accessible in more markets and to younger audiences.
