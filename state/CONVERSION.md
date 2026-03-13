# Conversion

*The full post-pick funnel: from first form submission to paying customer.*

---

## The Funnel

### Step 1: Discovery
**Source:** Shared Copa Card → copacard.com
**Drop-off risk:** High if landing page doesn't immediately show the product
**Conversion goal:** Visitor → Picks submitted
**Key lever:** Example card visible above the fold. No account wall. Direct CTA to pick form.

### Step 2: First Pick Submission
**What happens:** Player fills Tally.so form (5 picks + email). Submits.
**Barrier:** Email required (non-negotiable — this is how the card is delivered)
**Confirmation message (shown in Tally after submit):**
> "Your picks are locked. ⚽ Your Copa Card arrives 15 minutes after the final whistle. Check your inbox — it'll be worth the wait."

**Drop-off risk:** Email field. Some players won't give email.
**Mitigation:** Frame the email ask as delivery mechanism, not marketing: "We need your email to send your card." No checkbox. No newsletter opt-in language.

---

### Step 3: Card Delivery Email
**Trigger:** 15 minutes after final whistle
**Subject line options (A/B test):**
- "Your Copa Card is ready — [Team A] vs [Team B]"
- "You were right about [Team]." (only when Pick 1 correct)
- "Your card: [Score] / 160" 

**Email body:**
1. Card image (the shareable visual — full-width)
2. Score + narrative label (repeated in text for email clients that block images)
3. "Make your next pick →" button (primary CTA — keeps them in the loop)
4. Upsell block (secondary CTA):

---

### Step 4: Pro Upsell (in card delivery email)

**Upsell block — free card recipients only:**

> ---
> **Want the gold version?**
>
> Copa Pro ($4.99) gives you the gold card treatment for every match in the tournament. Plus: pick breakdown, streak tracking, and a crown badge in your group league.
>
> One coffee. 32 days of World Cup.
>
> [Upgrade to Copa Pro →] *(Stripe Checkout link)*
> ---

**Timing rationale:** The player has just received their card. They've experienced the product. This is the highest-conversion moment. The upsell fires at the aha moment, not before it.

**Upsell block — Pro card recipients:**
No upsell. Instead: streak information + "Share your card" reminder.

---

### Step 5: Group League Conversion (Javier path)

**Trigger:** Player receives card + has made 2+ picks (has demonstrated retention)

**Email #3 (after second card):**

> ---
> **Playing with friends?**
>
> Create a private Copa league and see how your picks stack up against your crew.
>
> First 500 leagues are free. After that, creating a league costs $2.99 — joining is always free.
>
> [Create my league →] *(goes to group creation flow)*
> ---

**Group creation flow:**
1. Name (text)
2. Email (pre-filled if known)
3. Group name (e.g., "Friday Night Crew")
4. Submit → redirect to Stripe Checkout ($2.99 or free if under 500)
5. After payment: receive group code + shareable invite link

**Invite link format:** copacard.com/join/[GROUP-CODE]
This link pre-fills the group code field in the Tally form. Players click → form opens → group code is already there.

---

## Conversion Rate Targets

| Stage | Target conversion | Volume (base scenario) |
|-------|-------------------|----------------------|
| Landing page visitor → picks submitted | 25% | 10,000 visitors → 2,500 players |
| Picks submitted → card received (email opens) | 70% | 2,500 → 1,750 opens |
| Card received → Pro upsell clicked | 10% | 1,750 → 175 clicks |
| Pro upsell clicked → purchased | 30% | 175 clicks → 52 purchases |
| **Overall: players → Pro purchase** | **~3%** | **2,500 → ~75 purchases** |
| Players → group created (Javier conversion) | 2% | 2,500 → 50 groups |
| Groups created → paid ($2.99) | 60% (after free 500 exhausted) | — |

**Note:** 3% overall Pro conversion aligns with Sleeper freemium benchmark. The upsell timing (post-card) should outperform a pre-play upsell by 2–3×.

---

## Email Sequence (Full Tournament)

| Email # | Trigger | Subject | Purpose |
|---------|---------|---------|---------|
| 1 | Pick submission | "Picks locked — your card is coming" | Confirmation + build anticipation |
| 2 | 15 min post-match | "Your Copa Card is ready" | Card delivery + Pro upsell |
| 3 | After 2nd card | "Play with your crew?" | Group league CTA |
| 4 | After 5th card | "Your Copa record so far" | Streak recap + retention |
| 5 | Day before USMNT/Mexico match | "Tomorrow's pick form is open" | Re-engagement for casual players |
| 6 | Group stage ends | "Knockout round picks open now" | Tournament milestone |
| 7 | Day before final | "Last Copa Card of 2026" | Final engagement + "See you at Euro 2028" |

---

## Referral Mechanic (V1.5)

**Trigger:** After Pro purchase
**Mechanic:** Pro purchaser receives a unique referral link. If a friend goes Pro via their link, the referrer gets a "Copa Legend" badge on their card for the rest of the tournament.

**Why not a cash reward:** Cash referral programs require backend infrastructure. A badge is free to implement and hits the same identity-expression nerve as the Pro card skin.

**Implementation V1:** Manual. After purchase, send referral code by email. Track manually in spreadsheet.
**Implementation V2:** Referral link with UTM tracking → Stripe webhooks → automatic badge grant.

---

## Conversion Anti-Patterns (What Not to Do)

1. **Don't upsell before the first card is delivered.** Players haven't experienced the product yet. Pre-play upsells have low conversion and high resentment.
2. **Don't make the Pro card look so different that free cards look bad.** Free cards must look good enough to share. Pro cards look *better* — not free cards looking *worse*.
3. **Don't add a newsletter checkbox to the pick form.** Every additional field drops conversion. The email field is already a barrier. The "you'll receive your card" framing is the only required context.
4. **Don't paywall group joining.** Every gate on the Javier invite link breaks the viral loop for his friends. Javier pays. Sofia joins free. Non-negotiable.
5. **Don't send more than one email per match day.** Over-emailing will kill deliverability and cause unsubscribes. One email per match: the card. Pre-match reminders only for big matches (semis, final, user's national team).
