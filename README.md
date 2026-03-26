# Copa — World Cup 2026 Partnership Agent

Copa is an autonomous agent focused on one thing: **signing betting platform partners** before June 11, 2026.

## What Copa Is

A B2B engagement product for sports betting platforms. Copa gives bettors a squad-building game tied to their winning bets — 48 days of engagement across all 104 World Cup matches. Revenue share model: partners earn 20% of $10 entry fees.

**One partner per market. Single webhook integration. No platform rebuild required.**

## The Deadline
**World Cup 2026 opens June 11, 2026. Partner integration deadline: April 15, 2026.**

## Agent Priorities
1. Partner pipeline — qualified prospects in PIPELINE.md
2. Outreach execution — pitches sent and tracked in OUTREACH.md
3. Deal progression — move conversations toward signed agreements
4. Pitch materials — PDF deck, demo URL

## State Files
| File | Purpose |
|------|---------|
| `state/CONCEPT.md` | Full product concept and pitch content |
| `state/IDENTITY.md` | Agent mission and rules |
| `state/PHASE.md` | Current phase and exit criteria |
| `state/PIPELINE.md` | All partner prospects and status |
| `state/OUTREACH.md` | Every outreach touch logged |
| `state/ACTIONS.md` | PENDING actions awaiting approval |
| `state/METRICS.md` | Pipeline and deal metrics |
| `state/MONETIZATION.md` | Revenue model and negotiation guidance |
| `state/LEARNINGS.md` | What the agent has learned |
| `state/JOURNAL.md` | Cycle-by-cycle log |

## Running
```bash
python3 scripts/run_cycle.py --root /path/to/worldcup
```

## Approving Actions
```bash
python3 scripts/approve.py --root /path/to/worldcup ACT-001 ACT-002
```
