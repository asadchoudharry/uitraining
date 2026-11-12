# Typography system (original synthesis)

Evidence base: S03 code-verified scale (Geist; 11–23px, base 13.5px); S09 artwork (large bold marketing headline vs small grey helper text); S04–S06 demo corpus (dense admin type, candidate families NOT_VERIFIED per page — see screen specs); S10 corpus (29 dashboard screens: KPI numerals dominate; one image, UIMG-040, is an actual type spec sheet naming **Inter Display** with canvas `#F7F7F7` and ink `#2B3749` for the Kravio dashboard UIMG-038).

## Decisions (original, brand-neutral)
- **Primary family: Inter** (open licence, SIL OFL) — chosen because it is the only family *evidenced inside the corpus itself* (UIMG-040 spec sheet) and covers dense UI, tabular figures and broad language support. Fallbacks: system sans stack in `tokens.json`.
- **Mono: JetBrains Mono** (OFL) for IDs, codes, amounts in audit contexts.
- **Base size 14px** for product UI (S03's 13.5px proves denser works for expert tools; 14px is the safer enterprise default). Compact density may drop table text to 13px, never below 12px for content.

## Roles
| Role | Size | Weight | Line-height | Use |
|---|---|---|---|---|
| Display | 30px | 700 | 1.25 | empty-state / onboarding heroes only |
| H1 page title | 24px | 650 | 1.25 | one per page |
| H2 section | 20px | 600 | 1.3 | section heads |
| H3 card | 17px | 600 | 1.35 | card titles |
| Body | 14px | 400 | 1.45 | default text |
| Body-sm | 13px | 400 | 1.45 | table cells (comfortable) |
| Label | 12px | 500 | 1.35 | form labels, column heads (uppercase only for table heads, +0.04em tracking) |
| Caption | 11px | 400 | 1.4 | helper text, timestamps |
| KPI number | 24–30px | 650 | 1.1 | tabular-nums mandatory |
| Money | inherits | 500 | — | tabular-nums, right-aligned in tables, currency code never hidden in exports |

## Rules drawn from the corpus
1. **Numerals are a type role, not an afterthought.** Every KPI, price, balance and count uses tabular figures (S10: dashboards fail visually when proportional figures jitter in live-updating cards).
2. **Four-step text ramp** (primary/secondary/tertiary/disabled) replaces ad-hoc greys (S03 code-verified ramp).
3. **Helper text is part of the field**, placed under the label or field with the error message replacing it in place (S09 form sections; S03 onboarding inline error with icon).
4. **Density dual-scale**: dashboards may use 20–30px numerals with 12px labels; forms stay at 14px with 12px labels — never mix form density into data grids.
5. **Arabic/RTL**: Inter lacks Arabic; for Arabic locales pair with *Noto Naskh Arabic / IBM Plex Sans Arabic* (both OFL), mirror layout (never mirror numerals or charts' time axes without a product decision), keep Latin brand/ID strings LTR-isolated with `bdi`. Line-height +10% for Arabic body text. This guidance is a **proposal**, not observed in sources (all sources are LTR; S03 RTL = NOT_VERIFIED).
6. **Truncation**: single-line ellipsis only in table cells and breadcrumbs, always with full value in tooltip/detail; never truncate amounts, statuses or primary actions.
