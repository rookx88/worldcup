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
  3. Match result (multiple choice: 3 options with team names + boldness tier labels)
  4. First goalscorer (multiple choice: 8 options from curated shortlist + "None / 0-0" option)
  5. Upset meter (rating scale 1–5, labeled: "1 = expected result" to "5 = massive upset")
  6. One moment (multiple choice: 5 options with emoji icons)
  7. Exact score — home goals (number, optional — field label: "Optional bonus: exact score")
  8. Exact score — away goals (number, optional)
  9. Group league code (text, optional — field label: "Group code (if joining a friend's league)")

**URL parameter support:** Test whether Tally.so supports ?group=COPA-JV4K URL parameter to pre-fill field 9. This enables Javier's invite link UX. If Tally doesn't support it natively, use a redirect: copacard.com/join/COPA-JV4K → Tally URL with hidden group code field.

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
- Elements per CONCEPT.md visual spec:
  - Section 1: Dark navy background (#0D1B2A), match header with team flags, final score (72px white bold), date, gold separator line (#C9A84C)
  - Section 2: 5 pick tiles in 2×2 + 1 full-width layout. Each tile: pick label (gray, small), player's pick (white, medium), what happened (light gray), border color (green/red/gold), boldness tier badge
  - Section 3: Score display (96px white + gray /160), narrative label (gold italic), percentile line, Copa wordmark, CTA footer
- Build two versions: standard (free) and Pro (gold foil border, gold score, Copa Pro badge)
- Also build: Group Leaderboard card template (landscape, 1080×1080, shows top 5 players with scores)

**Canva Bulk Create test:**
- Once template is built, test the Bulk Create feature (Canva Pro feature — $13/month or use free trial)
- Bulk Create takes a CSV with variable fields → generates one card per row
- Required CSV columns: PlayerName, MatchResult, GoalscorerPick, UpsetMeter, OneMoment, ExactScore, P1Correct, P2Correct, P3Score, P4Correct, P5Correct, TotalScore, NarrativeLabel, Percentile, NextMatch
- Estimated setup: 2 hours. After setup: all cards for a match generated in 20 minutes from a filled spreadsheet.

**Action required:** Human approval → Copa drafts visual spec (done in CONCEPT.md), human executes in Canva

---

## ACTION-005 — Landing Page (copacard.com)
**Type:** Web page creation
**Status:** PENDING
**Purpose:** The viral loop has no destination without a landing page. This is the single highest-priority build item.

**Platform:** Carrd.co (free tier, single page, no-code, fast)

**Full copy:** Written in CONCEPT.md (Landing Page Copy section). Ready to implement.

**Page structure:**
1. **Hero:** "Prove you called it." + subheadline + CTA button + "Free to play. No account needed. World Cup 2026."
2. **How it works:** Three steps (written in CONCEPT.md)
3. **Example card:** Morocco 2–1 Spain mockup (from 2022 — no current player rights issues)
4. **Waitlist signup:** Email field + "I'm in →" button
5. **Group league hook:** One paragraph, "Create a league →" CTA
6. **Copa Pro mention:** One line callout block
7. **Footer:** Copa wordmark + social links

**Implementation:** Carrd.co free account → publish to copacard.com once domain is registered (ACTION-002 must complete first).

**Action required:** Human approval → build on Carrd.co using copy from CONCEPT.md

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
- Can we create a Canva card (Bulk Create) in under 20 minutes?
- Does the email arrive and include the card correctly?
- Is the card actually shareable / does it look good?
- Does the group code pre-fill from URL parameter?
- What breaks?

**Target event:** Any match with reasonable interest, May 2026.

**Action required:** Human approval → execute internally first (Copa team only), then optionally open to first 20 waitlist members as "founding player beta"

---

## ACTION-011 — Canva Bulk Create Test
**Type:** Product infrastructure test
**Status:** PENDING
**Purpose:** Validate that Canva Bulk Create can generate Copa Cards at scale before tournament starts.

**Spec:**
- Requires Canva Pro ($13/month — or free 30-day trial)
- Build a test CSV with 10 fictional player card data rows
- Upload CSV to Bulk Create against the Copa Card template
- Evaluate: image quality, variable field accuracy, export time
- If it works: Canva Bulk Create is the V1.5 card generation method
- If it breaks: evaluate Bannerbear API as alternative (bannerbear.com — free tier 30 images/month, $49/month for 500)

**Success criteria:** 10 cards generated correctly in < 5 minutes from CSV upload.

**Target date:** Complete before ACTION-010 test run (need it working for May test).

**Action required:** Human approval → execute Canva Bulk Create test

---

## ACTION-012 — Google Sheets Score Calculator Setup
**Type:** Tool setup
**Status:** PENDING
**Purpose:** Build the scoring spreadsheet that converts raw pick data into card scores.

**Spec:**
- Tab 1: Match Data (one row per match: result, first scorer, moments, exact score, boldness tiers)
- Tab 2: Player Picks (Tally.so export — one row per player per match)
- Tab 3: Score Calculator (formulas mapping picks against results, applying multipliers)
- Tab 4: Leaderboard (SUMIF across all matches per player, ranked)
- Tab 5: Group Leaderboard (filtered by group code)

**Formulas needed:**
- Boldness multiplier lookup (VLOOKUP from match data)
- Upset Meter score: IF(Pick1Correct=TRUE, UpsetSlider×6, 0)
- Upset Meter gaming prevention: IF(Pick1Tier="Chalk", 0, standard formula)
- Exact score: IF(AND(HomeGoalsPick=HomeGoalsActual, AwayGoalsPick=AwayGoalsActual), 25, 0)
- Total score: SUM of all pick scores
- Percentile: PERCENTRANK across all players for that match

**Output:** A sheet where entering one row of match results automatically calculates all player scores for that match.

**Action required:** Human approval → build spreadsheet (estimated 2 hours)
