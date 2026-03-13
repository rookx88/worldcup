# Copa — World Cup 2026 Daily Fantasy Agent

Copa is an autonomous agent that researches, designs, and launches a unique daily fantasy sports game for the 2026 FIFA World Cup.

Built on the ABA self-improving loop: each generation, Copa assesses its weakest dimension, runs the matching skill, re-assesses, and commits progress.

## Deadline
**World Cup 2026 opens June 18, 2026.**

## Dimensions Tracked
### Phase 1 — Design & Strategy
- `concept-uniqueness` — Is the game mechanic genuinely different?
- `market-positioning` — Clear differentiation vs competitors?
- `viral-mechanics` — Built-in sharing and friend invitation?
- `marketing-reach` — Zero-budget organic channel strategy?
- `product-readiness` — Something buildable / live?

### Phase 2 — Launch & Growth
- `user-acquisition` — Real signups and players
- `engagement-quality` — Retention and organic sharing

## Skills
| Skill | Used when |
|-------|-----------|
| `research` | concept-uniqueness or market-positioning is weak |
| `design` | viral-mechanics or product-readiness is weak |
| `strategize` | marketing-reach is weak |
| `build` | product-readiness needs a technical spec |
| `grow` | user-acquisition is weak (Phase 2) |
| `convert` | engagement-quality is weak (Phase 2) |

## Running
```bash
python3 scripts/run_cycle.py --root /path/to/worldcup
```

## Approving Actions
```bash
python3 scripts/approve.py --root /path/to/worldcup ACT-001 ACT-002
```
