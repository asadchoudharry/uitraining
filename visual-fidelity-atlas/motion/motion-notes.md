# Motion notes

- S03 (CODE_VERIFIED): `--dur 140ms`, three curves (standard `cubic-bezier(.23,1,.32,1)` class, spring, drawer), dedicated `motion.css` (314 lines) and `states.css` (127 lines) — motion is tokenised, not ad-hoc.
- Original system: 120/160/240ms with the same curve family and a `prefers-reduced-motion` kill-switch (`design-system/tokens/tokens.css`). Dashboard number transitions and chart animations are NOT_VERIFIED in all demo sources (static templates).
