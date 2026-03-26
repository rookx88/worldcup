# Skill: Build

You are building the materials Copa needs to close partnership deals.

## Objective
Produce tangible assets that help partners say yes: pitch decks, demo URLs, integration specs, contract templates.

## Available Actions

### Pitch Deck
- Create a clean PDF or HTML/CSS pitch deck based on CONCEPT.md
- Match the style of the Copa deck: dark header, stat callouts, two-column layout
- Output: `materials/copa-pitch-deck.html` (converts to PDF for email attachment)

### Demo URL
- Build a static demo showing the player experience: squad selection, leaderboard, spin mechanic
- No real backend needed — fake data is fine for demo purposes
- Tool: Framer, Webflow free tier, or plain HTML
- Output: A shareable URL Copa can send to interested partners

### Integration Spec Document
- Create a clear 1-2 page technical spec for the webhook integration
- What the partner sends: bet resolution event (anonymized bet ID, player ID, timestamp, outcome)
- What Copa returns: spin credit confirmation
- Format: simple JSON event spec + example payload
- Output: `materials/copa-integration-spec.md`

### Partnership Agreement Template
- Draft a simple partnership agreement template
- Key terms: market exclusivity, revenue share rate (20% default), integration timeline, launch date, entry fee handling
- Output: `materials/copa-partnership-template.md`

## Rules
1. Build only what's needed to close the next deal — don't over-engineer
2. All materials should be easily customizable per partner (fill-in-the-blank for company name, market, rev share rate)
3. Propose all build tasks in ACTIONS.md as PENDING before starting
4. Document what was built in JOURNAL.md

## Output
Write build artifacts to `materials/` directory.
Log completion in JOURNAL.md.
Update ACTIONS.md (move from PENDING to DONE).
