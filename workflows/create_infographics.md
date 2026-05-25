# Workflow: Create MoCloud Brand Infographics

## Objective
Generate the 4 core MoCloud infographics (plus an optional market opportunity infographic)
using kie.ai Nano Banana 2 for rendering and Perplexity for market research.
All visual content is Claude-written and stored in the prompts inside `generate_infographic.py`.

## Inputs Required
- **Nothing.** Generation uses Pollinations.ai — free, no API key, no account needed.
- Optional: `PERPLEXITY_API_KEY` in `.env` if you want to upgrade `research_market.py` to fetch live data.

## Outputs
- `.tmp/infographics/architecture.png` — tech stack poster
- `.tmp/infographics/agent-flow.png` — swimlane execution diagram
- `.tmp/infographics/monetization.png` — pricing tier comparison
- `.tmp/infographics/wat-framework.png` — WAT architecture diagram
- `.tmp/infographics/market.png` (optional) — market opportunity infographic

## Steps

### 1. Add API keys to `.env`
```
KIE_AI_API_KEY=your_key_here
PERPLEXITY_API_KEY=your_key_here   # only if generating market infographic
```

### 2. Install dependencies (first time only)
```bash
pip install requests
```

### 3. Generate all 4 core infographics
```bash
python tools/generate_infographic.py --all
```

Or generate a single one:
```bash
python tools/generate_infographic.py --subject architecture
python tools/generate_infographic.py --subject agent-flow
python tools/generate_infographic.py --subject monetization
python tools/generate_infographic.py --subject wat-framework
```

### 4. Generate the market opportunity infographic (optional, uses Perplexity)
```bash
python tools/generate_infographic.py --subject market
```
This automatically calls `research_market.py` first to fetch live market stats,
then injects them into the infographic prompt.

## Infographic Descriptions

| Subject | Aspect | Content |
|---|---|---|
| `architecture` | 9:16 portrait | 5-layer tech stack glassmorphism poster (KMP→FastAPI→Supabase→Claude/E2B→RevenueCat) |
| `agent-flow` | 16:9 landscape | 4-lane swimlane diagram showing a full agent execution request/response cycle |
| `monetization` | 9:16 portrait | 3-tier pricing comparison (Explorer/Builder/Pro) with feature lists |
| `wat-framework` | 16:9 landscape | WAT architecture diagram + reliability math showing why WAT beats pure AI |
| `market` | 9:16 portrait | Market opportunity with live Perplexity-sourced stats + competitor gap analysis |

## Design System
All infographics share the same visual language:
- Background: `#0F0F12` near-black
- Primary: `#6366F1` indigo
- Accent: `#A78BFA` violet
- Text: `#F8F8FF` ghost white
- Tech accents: cyan `#06B6D4`, emerald `#10B981`, amber `#F59E0B`
- Style: glassmorphism cards, dark mode, clean sans-serif

## Edge Cases

**If generation times out (> 180s):** kie.ai may be under load. Wait a few minutes and retry
the same command. The `taskId` is printed to console — if you want to manually check status,
visit https://kie.ai/logs.

**If image URL is missing in response:** The response schema from kie.ai may have changed.
Check `data.output` structure at https://docs.kie.ai/market/common/get-task-detail and update
the `poll_task()` function in `tools/generate_infographic.py` accordingly.

**If Perplexity returns non-JSON:** `research_market.py` strips markdown code fences before
parsing. If the model still returns prose, check that `PERPLEXITY_API_KEY` is correct and
that the `sonar-pro` model is available on your plan.

**To regenerate with updated prompts:** Edit the `PROMPTS` dict in `generate_infographic.py`,
then re-run. Old files in `.tmp/infographics/` will be overwritten.

## Placing Final Assets
Once generated and approved:
1. Copy chosen images from `.tmp/infographics/` to `brand_assets/infographics/`
2. `.tmp/` is gitignored — `brand_assets/` is committed and version-controlled
3. See `brand_assets/README.md` for naming conventions
