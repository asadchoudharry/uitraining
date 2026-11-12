# Responsive matrix (original standard, applied in specs)

| Breakpoint | Shell | Tables | Stepper |
|---|---|---|---|
| 1920/1440 desktop | sidebar 252, gutter 24 | full columns | vertical rail |
| 1024 laptop | sidebar 64 (icons) or 252 toggled | hide low-priority columns into detail | vertical rail compact |
| 768 tablet | sidebar as drawer | card-rows for key lists | horizontal compact (current + next named) |
| 390 mobile | top bar + bottom-safe drawer nav | stacked record cards; amounts stay tabular | "Step X of N" + current/next names |

Per-screen verification status lives in each screen spec; demo sources' own responsive behaviour is NOT_VERIFIED in this pass except S03 (dedicated responsive.css, 355 lines, CODE_VERIFIED as existing).
