# Actions

*All external actions (posts, DMs, sign-ups, deploys) require PENDING → APPROVED before Copa executes.*

## Format
Each action: ID, type, description, draft content, status.

---

## ACTION-001 — Community Validation Post (r/worldcup)
**Type:** Reddit post
**Status:** PENDING
**Purpose:** Validate that the prediction card mechanic resonates with casual fans before building anything.
**Target date:** April 15–22, 2026

**Proposed post title:**
"I got tired of World Cup fantasy requiring you to know every player's stats, so I designed something different — feedback welcome"

**Proposed post body:**
---
Every World Cup fantasy game I've tried assumes you know squad depths, player salaries, injury reports. I don't, and most people I watch with don't either.

So I've been designing something simpler. Before each match, you fill out a **prediction card** — five picks:

1. Match winner (or draw)
2. First goalscorer — from a shortlist of 8 names, not the full squad
3. Upset meter — how big an upset would your pick be? Bigger upset call = bigger payout if you're right
4. One moment — clean sheet, red card, stoppage time goal, VAR drama. Pick one.
5. Exact score (optional bonus)

After the match, you get back a card showing what you got right. It's designed to look good as a screenshot. The idea is that if you called the upset, you have something to show for it.

No roster building. No salary cap. No need to know who plays left back for Portugal.

Two questions:
- Does this sound like something you'd actually use?
- What would you add or change?

(Building this for 2026 — still in design phase, not live yet)
---

**Notes:** Post should go up 6–8 weeks before tournament. No link to a product — this is purely feedback-seeking.

---

## ACTION-002 — Domain Registration
**Type:** Domain purchase
**Status:** PENDING
**Purpose:** Secure a domain before launch.

**Recommended domain:** `copacard.com`
**Rationale:** 
- "Copa" alone (.com/.gg) likely taken or expensive
- "copacard" is descriptive — the card is the product
- `.com` for trust with casual users (not `.gg` which signals gaming/niche)
- Check availability: copacard.com, playacopa.com, copa.cards

**Cost:** ~$12/year via Namecheap or Cloudflare Registrar
**Action required:** Human approval + purchase

---

## ACTION-003 — Tally.so Form Setup (V1 Pick Form)
**Type:** Tool setup
**Status:** PENDING
**Purpose:** Create the prediction card form for V1 — the mechanism for collecting picks before each match.

**Spec:**
- Platform: Tally.so (free, generous limits, Typeform-like UX, supports conditional logic)
- Fields:
  1. Nickname (text)
  2. Email (email — required to receive card)
  3. Match result (multiple choice: 3 options with team names)
  4. First goalscorer (multiple choice: 8 options from curated shortlist)
  5. Upset meter (rating scale 1–5)
  6. One moment (multiple choice: 5 options)
  7. Exact score — home goals (number, optional)
  8. Exact score — away goals (number, optional)
  9. Group league code (text, optional — for Javier-created groups)

**Notes:** Each match requires a new form instance (or form logic update). V1 accepts this as a manual task — ~10 minutes per match to update.

**Action required:** Human approval → set up Tally.so account (free)

---

## ACTION-004 — Canva Card Template
**Type:** Design asset creation
**Status:** PENDING
**Purpose:** Create the visual template for the shareable Copa Card.

**Spec:**
- Platform: Canva (free)
- Dimensions: 1080×1920 (Instagram Story / vertical)
- Elements:
  - Dark navy background (#0D1B2A or similar)
  - Match header: team flags (emoji or image), team names, final score, date
  - 5 pick tiles: each showing pick label, player choice, result, color (green/red/gold)
  - Score display: large, centered
  - Narrative label: 1 line of text (manually chosen from template phrases)
  - Percentile line: "Better than X% of Copa players"
  - Footer: copacard.com + Copa wordmark

**Output:** A Canva template where the variable fields can be edited in ~5 minutes per player per match (V1: manually done for each card; V2: automated via Canva API or equivalent)

**Action required:** Human approval → Copa drafts the visual spec in more detail next generation, human executes in Canva

---

## ACTION-005 — Landing Page (copacard.com)
**Type:** Web page creation
**Status:** PENDING
**Purpose:** The viral loop has no destination without a landing page. This is the single highest-priority build item.

**Platform:** Carrd.co (free tier, single page, no-code, fast)

**Page structure:**
1. **Hero:** "Pick five things. Get your card. Prove you called it." — with a mockup Copa Card image
2. **How it works:** Three steps. Illustrated. 30 words max.
   - "Make 5 predictions before kickoff"
   - "Watch the match"
   - "Get your Copa Card — share if you called it"
3. **Example card:** A real-looking Copa Card showing a completed pick (design it for a past WC match — e.g., 2022 Morocco vs. Spain)
4. **Waitlist signup:** Email field. CTA: "Get your first Copa Card free — World Cup 2026"
5. **Group league hook:** "Playing with friends? One person creates a league. Everyone else joins free."
6. **Copa Pro mention:** One line. "Copa Pro ($4.99) unlocks gold cards and pick breakdowns." No hard sell.

**Implementation:** Carrd.co free account → publish to copacard.com once domain is registered.

**Copywriting note:** The headline must be about the outcome ("Prove you called it"), not the mechanic ("Make predictions"). Sofia doesn't want to fill out a form. She wants bragging rights.

**Action required:** Human approval → Copa drafts full landing page copy next generation

---

## ACTION-006 — Copa Social Account Setup (Instagram + Twitter/X)
**Type:** Account creation
**Status:** PENDING
**Purpose:** Establish social presence before launch. Accounts need time to age before the tournament.

**Instagram:**
- Handle: @copacard or @playacopa (check availability)
- Bio: "World Cup predictions. Get your card. Share if you called it. ⚽ 2026 🏆 copacard.com"
- First 3 posts (teasers): "Something's coming for 2026." / A mockup card / "Make your pick. Get your card."

**Twitter/X:**
- Handle: @copacard or @playacopa
- Bio: same as Instagram
- Strategy: participate in #WorldCup2026 discussions, not just broadcast

**Action required:** Human approval → create accounts (5 minutes)

---

## ACTION-007 — r/USMNT and r/LigaMX Community Posts
**Type:** Reddit posts
**Status:** PENDING
**Purpose:** Reach the casual fan in the host country markets where World Cup energy is highest now.

**r/USMNT post title:**
"Built a World Cup prediction game for the 2026 home crowd — no fantasy expertise required"

**r/USMNT post body:**
---
2026 is in our backyard. A lot of people in my life who don't follow soccer regularly are going to be watching every USMNT match.

Existing fantasy games don't work for them — too complex, requires knowing squad depths they've never heard of.

So I'm building something different: before each match, you fill out a prediction card (takes 90 seconds). Match result, first goalscorer from a curated shortlist, one moment you think happens. After the match you get a card showing what you got right — designed to look good as a share.

No roster building. No salary cap. You don't need to know who plays left back for Portugal. You just need to have a feeling about the match.

Targeting casual fans — the people who'll show up for USMNT matches and the final but won't grind stats all tournament. Sound like something people in your circle would use?

(Still building — opening day June 18. Happy to answer questions about the design.)
---

**r/LigaMX post:** Similar framing in Spanish. Mexico host angle. WhatsApp group use case front and center.

**Target date:** April 15, 2026

**Action required:** Human approval

---

## ACTION-008 — Stripe Checkout Setup (Copa Pro Pre-Sale)
**Type:** Payment infrastructure
**Status:** PENDING
**Purpose:** Have payment live before tournament. Optional: run early-bird pre-sale at $3.99 to build revenue and commitment before June 18.

**Spec:**
- Create Stripe account (free)
- Create two products: Copa Pro ($4.99) and Group League Creator ($2.99)
- Generate Checkout links for each
- Copa Pro early-bird: $3.99 for anyone who pre-purchases before June 1

**Implementation:** Stripe Checkout link embedded in landing page and in the Pro upsell email that fires after first card delivery.

**Action required:** Human approval → Stripe account setup (30 minutes)

---

## ACTION-009 — Outreach to American Soccer Analysis and US Soccer Journalists
**Type:** Twitter DM outreach
**Status:** PENDING
**Purpose:** Get Copa mentioned by journalists/analysts whose audiences are the exact USMNT casual fan demographic.

**Targets:**
- American Soccer Analysis (@americansoccer)
- Ives Galarcep (@SoccerByIves)
- Sebastian Salazar (ESPN)
- Extratime Show (US Soccer's official podcast) (@ExtraTimeShow)

**Draft DM (Twitter):**
---
Hey — building a prediction game for casual fans for the 2026 World Cup. No salary cap, no roster building — just pick five things before each match and get a shareable card after. Targeting the home crowd audience that'll watch USMNT but hasn't touched DFS. Happy to share what I've built if it might be useful content for your audience.
---

**Action required:** Human approval → send DMs April 15

---

## ACTION-010 — Test Run: Full Loop on a Warm-Up Match
**Type:** Product test
**Status:** PENDING
**Purpose:** Before the tournament, run one complete Copa cycle on a real match (a USMNT friendly, a Copa América match, or a WC qualifier) to test the full loop: form → submission → card creation → email delivery.

**What this tests:**
- Does the Tally.so form work as expected?
- Can we create a Canva card in under 10 minutes?
- Does the email arrive and include the card correctly?
- Is the card actually shareable / does it look good?
- What breaks?

**Target event:** Any match with reasonable interest, May 2026.

**Action required:** Human approval → execute internally first (Copa team only), then optionally open to first 20 waitlist members as "founding player beta"
