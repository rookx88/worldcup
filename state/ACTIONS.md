# Actions

*All external actions (posts, DMs, sign-ups, deploys) require PENDING → APPROVED before Copa executes.*

## Format
Each action: ID, type, description, draft content, status.

---

## ACTION-001 — Community Validation Post (r/worldcup)
**Type:** Reddit post
**Status:** PENDING
**Purpose:** Validate that the prediction card mechanic resonates with casual fans before building anything.

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

**Notes:** Post should go up 6–8 weeks before tournament. Can go up sooner for early feedback if concept is ready. No link to a product — this is purely feedback-seeking.

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

## ACTION-003 — Typeform Setup (V1 Pick Form)
**Type:** Tool setup
**Status:** PENDING
**Purpose:** Create the prediction card form for V1 — the mechanism for collecting picks before each match.

**Spec:**
- Platform: Typeform (free tier supports up to 10 responses/month — need paid for launch, OR use Google Forms as fallback)
- Alternative: Tally.so (free, more generous limits, Typeform-like UX)
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

**Notes:** Each match requires a new form instance (or form logic update) since the teams/players change. V1 accepts this as a manual task — takes ~10 minutes per match to update.

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
