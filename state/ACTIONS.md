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

**Action:** Build Copa Card Canva template using the full spec in CONCEPT.md (Copa Card — Canva Template Build Spec section)
**Estimated time:** 45 minutes to build template; 5 min per card thereafter

**Fabricated calls to use for the 2022 Final mockup:**
- "Does the team that scores first win?" — YES submitted → ✗ wrong (France equalized)
- "Red card in this match?" — NO submitted → ✓ correct
- "At least one set piece goal?" — YES submitted → ✓ correct
- "Does this match go to extra time?" — YES submitted, marked as **Bold Call** → ✓ correct (Bold Call hit — gold band on card)
- "More or fewer than 2.5 total goals?" — MORE submitted → ✓ correct (7 goals total)
- In-match call: "Does Argentina score before half time?" — NO submitted → ✓ correct

**Result:** 5/6 correct, Bold Call landed. Score: ~75 pts. Shows a realistic, exciting card.

**Card must show:**
- Argentina flag + player name ("Copa Player") + light blue background
- "5 / 6 CORRECT · 75 pts"
- Bold Call gold band: "🎯 BOLD CALL ✓ — Called extra time before 75'"
- Call list with ✓/✗ and crowd splits
- `copa.fc/play` in footer

**This card is the primary marketing asset.** No Reddit or Twitter posts until this exists.

---

## PENDING: Build Airtable Scoring Base

**Action:** Set up Airtable base using exact schema specified in CONCEPT.md (Airtable Schema section)
**Estimated time:** 2–3 hours to build and test

**Build order:**
1. Create base "Copa 2026"
2. Build Table 1: Players (all fields as specified)
3. Build Table 2: Matches
4. Build Table 3: Calls
5. Build Table 4: Submissions (largest table — do formulas last)
6. Build Table 5: Crews
7. Create the five named views specified in the schema
8. Test with 20 mock players, one mock match, 6 mock calls, 20 mock submissions
9. Verify: crowd split calculates correctly, contrarian bonus fires when <30%, Bold Call 30 pts correct / 0 pts wrong

**Success metric:** 20 mock players scored correctly for a single match. Nation leaderboard shows correct average. Crew leaderboard shows correct totals.

---

## PENDING: Build Typeform Pre-Match Call Form

**Action:** Build Typeform template using exact spec in CONCEPT.md (Typeform Build Spec section)
**Estimated time:** 30 minutes

**Build order:**
1. Create form "Copa Calls — Pre-Match Template"
2. Add screens 1-11 as specified
3. Set up Zapier integration: Typeform → Airtable Submissions table
4. Test end-to-end: submit test response → verify row appears in Airtable with correct fields
5. Set form close time to a past time → verify "closed" message displays correctly

**Also build:** In-match call form (simpler — one screen, 5 fields)

**Success metric:** Test submission flows through to Airtable correctly. Form shows correct closed message after deadline.

---

## PENDING: Build Beehiiv Email Flows

**Action:** Set up Beehiiv for Copa Card delivery and in-match broadcast emails
**Estimated time:** 1 hour

**Build the following templates:**
1. Welcome email: "You're in — your first Copa call form opens before [match name]"
2. Pre-match reminder: "[Team A vs Team B] — your Copa calls are open → [form link]"
3. In-match broadcast: "[LIVE] Copa in-match call — [call text] → YES/NO [form link]"
4. HT check-in (group stage): "Half time — how's your Copa card looking? [brief match context]"
5. Text Copa Card delivery (free tier): use exact template in CONCEPT.md (Beehiiv Text Copa Card section)
6. Pro upsell (sent with second text Copa Card): "Want the visual card? Copa Pro — $6.99 for the tournament → [Stripe link]"

**Success metric:** Can send a test Copa Card email to 5 test addresses. Card displays correctly on Gmail mobile, Gmail desktop, and Apple Mail.

---

## PENDING: Post to r/soccer — Seed Thread

**Action:** Post discussion thread to r/soccer
**Post title:** "Serious question — does a good World Cup game actually exist? I always just end up live-tweeting 'I knew that was going in'"
**Content:** Genuine discussion post about the gap in World Cup games. Does NOT mention Copa. Collects community signal. Reply personally to comments.
**Timing:** Post this week (March 2026)
**Do not post if:** Subreddit has pinned mod note about promotional posts — read rules first.
**Prerequisite:** None — this post requires no build work.

---

## PENDING: Post Copa Card Mockup to r/worldcup

**Action:** Post Copa Card mockup to r/worldcup
**Post title:** "Working on a new kind of World Cup game — here's what the player card looks like after a match. Would you share this?"
**Content:** Show the 2022 Final mockup card. Ask for honest feedback. Collect email signups in comments from interested people.
**Timing:** April 2026 (after card design is complete)
**Prerequisite:** Copa Card V1 Template must be built first.

---

## PENDING: Post Copa Card Mockup to Twitter/X

**Action:** Post Copa Card mockup to Copa Twitter/X account
**Copy:** "Building a World Cup game where you call match moments in real time. You get a card like this after every match. The gold band is your Bold Call — one call per match where you go all in. Would you post this?"
**Attach:** Copa Card mockup image (2022 Final scenario)
**Timing:** Same week as r/worldcup post (April 2026)
**Prerequisite:** Copa Card V1 Template must be built first.

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
**Prerequisite:** Landing page live, Airtable base functional, Typeform built.

---

## APPROVED: None yet
