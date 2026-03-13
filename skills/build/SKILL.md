# Skill: Build

You are planning and speccing the technical build for Copa's World Cup fantasy game.

## Objective
Define exactly what needs to be built, in what order, using what tools — so a single developer can have something playable before June 18, 2026.

## Constraints
- No backend team — ideally no-code or minimal code for v1
- Must be live before June 18, 2026 (tournament start)
- Zero hosting cost preferred for initial launch

## Build Tasks

### Tech Stack Selection
Evaluate and recommend:
- **Landing page / waitlist**: Carrd, Webflow, or custom? What captures emails?
- **Game engine v1**: Static HTML + JS? Glide/Softr from a spreadsheet? Simple Next.js app?
- **Data source**: Which free/cheap API provides World Cup match data and player stats?
  - football-data.org (free tier), API-Football, Sportmonks — compare
- **Leaderboard**: Airtable backend? Supabase? Google Sheets + formula?
- **Sharing cards**: Auto-generated image (Cloudinary, OG image API, or canvas)?

### Build Sequence
Define the build in ordered milestones:
1. Waitlist page (collect emails before anything is built)
2. Game spec document (rules, scoring, UI mockup — enough to show a developer)
3. Match day prototype (can play one match, manual scoring OK)
4. Automated scoring (pulls from data API)
5. Shareable result card
6. Leaderboard
7. Friend challenge link

### Spec the MVP
Write a clear spec for milestone 3 (match day prototype):
- What a player sees when they arrive
- What picks they make and how
- What they see after the match
- What they share

## Output
Update CONCEPT.md with the tech stack decision and build sequence.
Propose any build actions (domain registration, API signup, repo creation) in ACTIONS.md as PENDING.
Document decisions in JOURNAL.md.

## Rules
- Don't build anything this cycle — spec and propose. Human approves before anything is created.
- One clear tech recommendation beats three options with no decision.
