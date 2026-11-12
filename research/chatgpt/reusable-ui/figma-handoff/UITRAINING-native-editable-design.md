# Native Figma handoff — original enterprise reference implementation

**File:** https://www.figma.com/design/6ilnXLVvHo81h7QIAW5AAw
**Native file created:** 2026-11-12
**Editable Figma node:** 2:3 (page 2:2)
**Scope:** original training interface only; no source replica.

## Design assets actually created
- Semantic color variable collection: 12 variables with Light and Dark modes.
- Spacing variable collection: 8 variables on an 4px-base scale.
- Primary button component: node 1:24; Status/In review chip: 1:26.
- Editable, separately layered approval screen: 1440×900 frame 2:3, sidebar 244px, workspace 1196px.
- Original sample content includes five request rows, four queue metrics, selection/high-priority context and a decision pane.
- Screenshot inspected after correcting text collision; reviewer noted readable layout and no visible collision in right detail.

## Original measured screen reconstruction sheet (not a measurement of external references)
| Region | Measured/constructed specification |
| --- | --- |
| App canvas | 1440×900 CSS px design frame |
| Navigation | Left 244px dark sidebar with 8 items |
| Workspace | 1196px main area, pale neutral surface |
| Metrics | Four equal-width KPI cards in a single horizontal row |
| Toolbar | Search/help content across ~1110px |
| Decision area | ~724px request list + 372px review details, ~14px gap |
| Request density | Five rows, compact 75px row containers |
| Typography | Inter regular/bold in 10–30px references; editable Figma text, not fonts bundled |
| Surface/background | Original semantic JSON and CSS; light/dark variables present |
| Primary command | Button component instance in decision panel |

## Design-to-code parity and limitations
- Figma component/variables are native/editable; one app frame is composed of editable text, components and Auto Layout containers.
- Light and Dark **variable modes** exist. The approved screenshot is a **Light** example; Dark screen and RTL variants have not been visually built or QA tested.
- This is a static visual representation; its Approve/Reject buttons in Figma are not connected to a real backend or prototype transitions.
- No Figma Code Connect mapping, token-sync automation, live API binding, native multi-screen user journey, or 320/390/768 browser screenshot parity has been verified.
- Do not claim pixel parity with external proprietary designs. This is a clean-room original reference inspired by general enterprise UX principles.

## Transfer contract
- Main Figma asset: 2:3. For implementation, use reusable-ui/original-semantic-tokens/tokens.json and the workflow spec WFL-001.
- All operational controls must implement loading, disabled, blocked, success, stale, conflict, and permission-denied states.
- Every finance-impacting action must require backend authorization, version validation and idempotency.
