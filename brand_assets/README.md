# Brand Assets

Version-controlled brand materials for MoCloud.

## Structure

```
brand_assets/
├── README.md           ← this file
├── logo/               ← app icon, wordmark, logo variants (TBD)
└── infographics/       ← approved infographics, copied from .tmp/infographics/
```

## Logo

Not yet defined. When ready, place files here:
- `logo/mocloud-icon.png` — square app icon (1024×1024)
- `logo/mocloud-wordmark.svg` — horizontal logo with text
- `logo/mocloud-wordmark-dark.svg` — dark-background variant
- `logo/mocloud-wordmark-light.svg` — light-background variant

**Design direction:** indigo #6366F1 primary, violet #A78BFA accent, ghost white #F8F8FF text.
Mood: clean, developer-focused, modern mobile tech.

## Infographics

Generated via `python tools/generate_infographic.py --all`.
Raw outputs land in `.tmp/infographics/` (gitignored).
Once reviewed and approved, copy here:

| File | Description |
|---|---|
| `infographics/architecture.png` | 5-layer tech stack poster |
| `infographics/agent-flow.png` | Agent execution swimlane diagram |
| `infographics/monetization.png` | Pricing tier comparison |
| `infographics/wat-framework.png` | WAT architecture + reliability diagram |
| `infographics/market.png` | Market opportunity (optional, uses Perplexity) |

See [workflows/create_infographics.md](../workflows/create_infographics.md) for generation instructions.

## Design System

| Token | Value | Use |
|---|---|---|
| Background | `#0F0F12` | Dark canvas |
| Primary | `#6366F1` | Indigo — main brand color |
| Accent | `#A78BFA` | Violet — highlights, streaming |
| Text | `#F8F8FF` | Ghost white |
| Cyan | `#06B6D4` | Data layer accents |
| Emerald | `#10B981` | Execution / success states |
| Amber | `#F59E0B` | Warnings / payments |
| Code font | JetBrains Mono | All code blocks |
