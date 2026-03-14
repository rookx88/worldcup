# Actions

*All external actions require PENDING → APPROVED before Copa executes.*

---

## PENDING: Register Domain

**Action:** Register `copafc.com` (or `copa-calls.com` as backup)
**Tool:** Namecheap or Cloudflare Registrar (~$12/year)
**Urgency:** Before any public posts — the URL needs to be on the Copa Card mockup
**Blocking:** All marketing actions depend on this

**Success metric:** Domain registered, DNS configured, Carrd page live at the domain.

---

## PENDING: Build Waitlist Landing Page

**Action:** Create a one-page waitlist site at copafc.com
**Tool:** Carrd ($19/year)
**Required before any marketing begins**

**Page must include:**
- Copa Card mockup (fabricated for a real historical match — 2022 WC Final)
- One-sentence hook: "Copa asks you five yes-or-no questions about each World Cup match. You answer by gut. The match answers for real. You get a card like this."
- Email capture (Beehiiv embed)
- Nation selector at signup (sets card skin)
- No password. No account creation.
- `copa.fc/play` URL shown (or actual domain)

**Success metric:** Page converts >20% of visitors to email signups.

---

## PENDING: Design Copa Card V1 Template

**Action:** Design Copa Card in Canva using fabricated 2022 World Cup Final scenario
**Specifications:** (Full spec in CONCEPT.md — Copa Card section)

**Fabricated calls to use for the 2022 Final mockup:**
- "Does the team that scores first win?" — YES submitted → ✗ wrong (France equalized)
- "Red card in this match?" — NO submitted → ✓ correct
- "At least one set piece goal?" — YES submitted → ✓ correct
- "Does this match go to extra time?" — YES submitted, marked as **Bold Call** → ✓ correct (Bold Call hit — gold band on card)
- "More or fewer than 2.5 total goals?" — MORE submitted → ✓ correct (7 goals total)
- In-match call: "Does Argentina score before half time?" — NO submitted → ✓ correct

**Result:** 5/6 correct, Bold Call landed. Score: ~75 pts. Shows a realistic, exciting card.

**Card must show:**
- Argentina flag + player name (use "You" or "Copa Player") + blue/white background
- "5 / 6 CORRECT · 75 pts"
- Bold Call gold band: "BOLD CALL ✓ — Called extra time before 75'"
- Call list with ✓/✗ and crowd splits
- `copa.fc/play` in footer

**This card is the primary marketing asset.** No Reddit or Twitter posts until this exists.

---

## PENDING: Post to r/soccer — Seed Thread

**Action:** Post discussion thread to r/soccer
**Post title:** "Serious question — does a good World Cup game actually exist? I always just end up live-tweeting 'I knew that was going in'"
**Content:** Genuine discussion post about the gap in World Cup games. Does NOT mention Copa. Collects community signal. Reply personally to comments.
**Timing:** Post this week (March 2026)
**Do not post if:** Subreddit has pinned mod note about promotional posts — read rules first.

---

## PENDING: Post Copa Card Mockup to r/worldcup

**Action:** Post Copa Card mockup to r/worldcup
**Post title:** "Working on a new kind of World Cup game — here's what the player card looks like after a match. Would you share this?"
**Content:** Show the 2022 Final mockup card. Ask for honest feedback. Collect email signups in comments from interested people.
**Timing:** April 2026 (after card design is complete)

---

## PENDING: Post Copa Card Mockup to Twitter/X

**Action:** Post Copa Card mockup to Copa Twitter/X account
**Copy:** "Building a World Cup game where you call match moments in real time. You get a card like this after every match. The gold band is your Bold Call — one call per match where you go all in. Would you post this?"
**Attach:** Copa Card mockup image (2022 Final scenario)
**Timing:** Same week as r/worldcup post (April 2026)

---

## PENDING: Send Podcast Pitch Emails

**Action:** Send pitch email to all 10 podcast targets (see PIPELINE.md)
**Email template:** (See CHANNELS.md — Podcast Strategy section)
**Attachments:** Copa Card mockup image
**Timing:** May 1, 2026 (not before — too early, tournament not close enough for urgency)
**Follow-up:** May 15 for non-responders (one follow-up only)

---

## PENDING: Post "Copa is live" to Reddit (Pre-Tournament)

**Action:** Launch announcement post to r/worldcup, r/USMNT, r/mexico, r/england, r/brasil
**Timing:** June 1, 2026 (stagger by 3 days between subreddits)
**Content:** "Copa is live for World Cup 2026 signups. [Brief explanation of Copa Calls + Bold Call mechanic]. Copa Card from a practice match attached. Sign up here: [link]"
**Note:** Requires waitlist page live and Airtable crew flow functional.

---

## PENDING: Build Airtable Scoring Base

**Action:** Set up Airtable base for call scoring, player records, and Crew leaderboards
**Structure needed:**
- Players table (name, email, nation, total points, calls correct, calls total, Pro status)
- Calls table (match, call text, correct answer, crowd split YES%, crowd split NO%)
- Submissions table (player → call → answer → points awarded)
- Crews table (crew name, creator, members list, total score)
- Formula fields: crowd split contrarian detection, Bold Call 3x multiplier, nation average score

**Success metric:** Can input 20 test players, simulate one match, generate accurate scores and a Crew leaderboard.
**Timing:** Build before June 1.

---

## PENDING: Build Beehiiv Email Flow

**Action:** Set up Beehiiv for Copa Card delivery and in-match broadcast emails
**Flows needed:**
1. Welcome email (signup confirmation + nation selection confirmed)
2. Pre-match reminder (sent 2hrs before kickoff: "Your Copa call form is open →")
3. In-match broadcast (manual send at 30' or 75' trigger: "In-match call now open — [call text] → [form link]")
4. Copa Card delivery (sent within 30min of final whistle: subject = "Your Copa Card — [Match]", preview = "[X/Y correct]. [Bold Call result].")
5. Pro upsell (sent with second Copa Card if player has shared first card — see CONVERSION.md)

**Success metric:** Can send broadcast email to 100-person test list in under 2 minutes.

---

## APPROVED: None yet
