"""
generate_infographic.py

Generates MoCloud brand infographics using Pollinations.ai — completely free,
no API key, no account. Uses the nanobanana-2 model (same as kie.ai Nano Banana 2).

Usage:
    python tools/generate_infographic.py --subject architecture
    python tools/generate_infographic.py --subject agent-flow
    python tools/generate_infographic.py --subject monetization
    python tools/generate_infographic.py --subject wat-framework
    python tools/generate_infographic.py --subject market
    python tools/generate_infographic.py --all

Output: .tmp/infographics/<subject>.png
"""

import argparse
import os
import sys
import time
from pathlib import Path
from urllib.parse import quote

import requests

OUTPUT_DIR = Path(".tmp/infographics")
BASE_URL = "https://gen.pollinations.ai/image"
MODEL = "nanobanana-2"          # same model as kie.ai Nano Banana 2 — free via Pollinations
REQUEST_TIMEOUT = 180           # seconds; generation can take up to 2 min on first request
DELAY_BETWEEN = 8               # seconds between requests to stay within rate limits

# ---------------------------------------------------------------------------
# Claude-written prompts — design system:
#   bg #0F0F12 · primary #6366F1 indigo · accent #A78BFA violet
#   text #F8F8FF · cyan #06B6D4 · emerald #10B981 · amber #F59E0B
# ---------------------------------------------------------------------------

PROMPTS = {

    "architecture": """\
Professional dark-mode technical architecture poster for a mobile AI app called MoCloud.
Dark background color #0F0F12 with subtle dot-grid pattern. Portrait layout.

HEADER: "MoCloud" in large bold white with indigo-violet gradient glow.
Subtitle: "Mobile AI Agent Platform — Architecture" in light gray.
Small pill badges in a row: KMP · FastAPI · Supabase · Claude API · E2B

FIVE STACKED GLASSMORPHISM CARDS connected by glowing downward arrows:

Card 1 — MOBILE APP. Accent indigo #6366F1. Left icon: smartphone.
Title: "KMP + Compose Multiplatform" white bold. Subtitle: "iOS & Android — shared Kotlin codebase".
Right badges: Ktor WebSocket · Supabase SDK · RevenueCat

Card 2 — BACKEND API. Accent purple #8B5CF6. Left icon: server stack.
Title: "FastAPI + Python" white bold. Subtitle: "Async API · WebSocket streaming · Railway Cloud".
Badges: REST · WebSockets · Rate limiting

Card 3 — DATA LAYER. Accent cyan #06B6D4. Left icon: database.
Title: "Supabase" white bold. Subtitle: "PostgreSQL · Auth · Storage · Realtime — EU Frankfurt".
Badges: GDPR compliant · Row Level Security · JWT

Card 4 — two side-by-side cards:
Left: accent violet #A78BFA. Icon: brain. Title: "Claude API". Subtitle: "claude-sonnet-4-6 · Tool use · Streaming". Badges: Prompt caching · BYOK
Right: accent emerald #10B981. Icon: terminal. Title: "E2B Sandbox". Subtitle: "Isolated code execution · Pay-per-use". Badges: Docker isolation · 30s timeout

Card 5 — PAYMENTS. Accent amber #F59E0B. Icon: subscription circle.
Title: "RevenueCat" white bold. Subtitle: "Apple IAP + Stripe · Unified subscriptions".
Badges: iOS · Android · Web

RIGHT SIDEBAR — thin vertical event timeline with colored dots:
● token · ● tool_start · ● tool_output · ● tool_end · ● session_end · ● error

FOOTER: "Built solo · Deployed globally · Designed for developers" — small centered ghost-white text.

Style: glassmorphism frosted cards, 1px white border at 10% opacity, rounded corners, glow arrows, clean sans-serif typography.\
""",

    "agent-flow": """\
Professional dark-mode swimlane flow diagram infographic for MoCloud, a mobile AI agent app.
Dark background #0F0F12. Landscape orientation.

TITLE: "How MoCloud Works" — large bold white centered.
SUBTITLE: "Real-time AI agent execution — from your message to results in seconds" — small gray.

FOUR HORIZONTAL SWIMLANES (full width, top to bottom):
Lane 1 — YOU: left label with phone icon, accent indigo #6366F1, subtle indigo tint.
Lane 2 — BACKEND: server icon, accent purple #8B5CF6.
Lane 3 — CLAUDE AI: brain icon, accent violet #A78BFA.
Lane 4 — E2B SANDBOX: terminal icon, accent emerald #10B981.

EIGHT NUMBERED STEPS flowing left to right:
① You→Backend: "Send message" via WebSocket JWT auth. Indigo arrow.
② Backend→Claude: "History + tool definitions · Streaming ON". Purple arrow.
③ Claude→Backend→You: "Token stream" cascading down. Time badge: "< 200ms first token" in green.
④ Claude→Backend: "tool_call: run_python(code)". Violet arrow intercepted.
⑤ Backend→E2B: "Submit code · Isolated container created". Purple arrow.
⑥ E2B→Backend→You: "stdout lines stream live". Emerald cascading arrows. Time badge: "30s max" amber.
⑦ E2B→Claude: "Container destroyed · result returned". Emerald arrow.
⑧ Backend: "Session costs logged". Coin icon badge.

Right side vertical badge: "< 3s typical end-to-end".
Lane separators: subtle horizontal dashed lines at 8% white opacity.
Numbered circles filled with lane accent color, white number inside 28px.
Arrows thin glowing lines in lane color.\
""",

    "monetization": """\
Beautiful dark-mode SaaS pricing comparison infographic for MoCloud mobile AI agent app.
Background #0F0F12. Subtle radial gradient glow behind center card. Portrait orientation.

HEADER centered: "MoCloud Pricing" large bold white. Subtitle: "Choose the plan that fits your workflow" gray.

THREE PRICING CARDS side by side (equal width, cards fill most of the space):

LEFT CARD — EXPLORER:
Background dark #1A1A2E, gray 1px border. Badge: "FREE" gray pill top.
Price: "$0" very large white, "/month" small gray.
Feature list with gray checkmarks:
✓ 20 messages per day  ✓ 5 code executions per day  ✓ Claude Haiku model
✓ 7-day session history  ✓ 1 active session
CTA button: "Get Started →" outlined gray rounded. Micro-text: "Perfect for exploring".

CENTER CARD — BUILDER (highlighted, slightly taller):
Background indigo gradient #6366F1→#4338CA, bright glowing border, outer glow.
Badge: "⭐ MOST POPULAR" bold white pill top.
Price: "$9.99" very large bold white, "/month". Annual: "$79.99/year — save 33%" small.
Feature list white checkmarks:
✓ 500 messages per day  ✓ 100 code executions per day  ✓ Claude Sonnet — full power
✓ 90-day session history  ✓ BYOK unlimited with own key  ✓ 5 sessions  ✓ 1 GB storage
CTA button: "Start Building →" solid white rounded. Micro-text: "For developers & students".

RIGHT CARD — PRO:
Background dark #1A1A2E, violet #A78BFA 1px border. Badge: "PRO" violet pill.
Price: "$24.99" large white. Annual: "$199.99/year".
Feature list violet checkmarks:
✓ 2,000 messages per day  ✓ 500 code executions per day  ✓ Claude Opus — most powerful
✓ Unlimited history  ✓ Workflow scheduling  ✓ Unlimited sessions  ✓ 10 GB storage  ✓ PDF export
CTA button: "Go Pro →" outlined violet. Micro-text: "For professionals & freelancers".

BELOW CARDS two info pills: "Apple takes 30% on iOS — pricing reflects this" and "EU data storage — GDPR compliant".
FOOTER small: "Team plan $49.99/seat/month · contact us".\
""",

    "wat-framework": """\
Clean dark-mode architecture diagram infographic explaining WAT (Workflows, Agents, Tools) framework for MoCloud AI platform.
Background #0F0F12 with subtle dot-grid. Professional tech aesthetic.

TITLE: "The WAT Framework" large bold white. Subtitle: "How MoCloud separates AI reasoning from deterministic execution" gray.
Small indigo pill: "Reliability through separation of concerns".

THREE GLASSMORPHISM CARDS horizontally with labeled glowing arrows between them:

LEFT CARD — W: WORKFLOWS. Accent indigo #6366F1.
Large "W" or document icon top center.
Title: "Workflows" white bold. Role: "The Instructions" indigo tag.
List: • Markdown SOPs in plain language • Define objective, tools, edge cases • User-uploadable automation scripts • Stored in Supabase
Code preview box (dark monospace):
  ## Research Competitors
  Tools: search_web, read_url
  Output: → Google Sheet
  Schedule: Every Monday 9am

CENTER CARD — A: AGENTS. Accent violet #A78BFA with outer glow.
Brain icon top.
Title: "Agents" white bold. Role: "The Decision-Maker" violet tag.
List: • Reads workflow instructions • Orchestrates tools in sequence • Handles failures gracefully • Powered by Claude API
Large italic quote in light violet:
  "AI handles reasoning.
   Scripts handle execution.
   That's why it's reliable."
Arrows: ← reads (left) and calls → (right).

RIGHT CARD — T: TOOLS. Accent emerald #10B981.
Terminal icon top.
Title: "Tools" white bold. Role: "The Execution" emerald tag.
List: • Deterministic Python scripts • API calls, file operations, DB queries • Consistent, testable, fast • Run in E2B sandboxes
Script list in monospace: run_python.py · read_file.py · write_file.py · search_web.py

BOTTOM SECTION — "Why WAT beats end-to-end AI":
Row 1 ❌ Pure AI: 5 boxes Step 1→2→3→4→5 with decreasing: 90%→81%→73%→66%→59% and red label "59% after 5 steps".
Row 2 ✅ WAT: AI box → Tool → Tool → Tool staying at 90%→90%→90%→90% green label "Reliability maintained".
Footer: "MoCloud is built on WAT. Every agent run follows this pattern."\
""",

    "market": """\
Dark-mode market opportunity infographic for MoCloud, a mobile AI agent platform for developers.
Background #0F0F12. Accent indigo #6366F1 and violet #A78BFA. Portrait orientation. Investor pitch aesthetic.

TITLE: "Why MoCloud. Why Now." large bold white centered.
SUBTITLE: "The mobile AI agent market is wide open" gray.

SECTION 1 — MARKET SIZE:
Large stat: "$12B+" in giant indigo text. Label: "Global Mobile AI App Market 2026".
Trend arrow pointing up. Sub-stat: "38% YoY growth · 340M+ mobile AI users worldwide".

SECTION 2 — THE GAP (two columns):
Left column red/gray tint: "Existing Apps"
Claude.ai app — "Chat only. No real execution."
ChatGPT app — "No persistent agent sessions."
GitHub Copilot — "Desktop-only. Not mobile."
Right column green/indigo tint: "MoCloud"
✓ Full sandboxed code execution
✓ WAT workflow automation
✓ Mobile-native UX (haptics, voice, gestures)
✓ Glass-box agent runs — see every step

SECTION 3 — TARGET USERS (3 persona cards):
🎓 Developer Students — "Need portable AI coding help. No desktop."
💼 Freelancers — "Run automations anywhere, any time."
🚀 Indie Makers — "Build and ship products from their phone."

SECTION 4 — REVENUE PATH (simple funnel):
10,000 free users → 200 paid (2% conversion) → $2,000 MRR
Labels: "Explorer" → "Builder $9.99" → "Pro $24.99"

SECTION 5 — TECH MOAT (4 badges in a row):
"KMP Native" · "WAT Framework" · "Glass-box Execution" · "BYOK Ready"

FOOTER italic ghost-white: "One developer. One platform. Infinite agents."\
""",
}

# ---------------------------------------------------------------------------
# Dimensions per aspect ratio
# ---------------------------------------------------------------------------
DIMENSIONS = {
    "architecture": (1080, 1920),   # 9:16 portrait
    "agent-flow":   (1920, 1080),   # 16:9 landscape
    "monetization": (1080, 1920),   # 9:16 portrait
    "wat-framework":(1920, 1080),   # 16:9 landscape
    "market":       (1080, 1920),   # 9:16 portrait
}

CORE_SUBJECTS = ["architecture", "agent-flow", "monetization", "wat-framework"]


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------

def generate(subject: str) -> Path:
    prompt = PROMPTS[subject]
    width, height = DIMENSIONS.get(subject, (1080, 1920))

    print(f"\n{'='*52}")
    print(f"  Generating: {subject}  ({width}x{height})")
    print(f"  Model: {MODEL} via Pollinations.ai (free)")
    print(f"{'='*52}")

    encoded = quote(prompt, safe="")
    url = f"{BASE_URL}/{encoded}?model={MODEL}&width={width}&height={height}&nologo=true&private=true&enhance=false"

    print(f"  Sending request... (may take up to {REQUEST_TIMEOUT}s)")
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT, stream=True)
        resp.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"  ERROR: Request timed out after {REQUEST_TIMEOUT}s. Try again — Pollinations can be slow on cold starts.", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"  ERROR: HTTP {resp.status_code} — {e}", file=sys.stderr)
        sys.exit(1)

    content_type = resp.headers.get("content-type", "")
    if "image" not in content_type:
        print(f"  ERROR: Unexpected content-type '{content_type}'. Response body:\n{resp.text[:300]}", file=sys.stderr)
        sys.exit(1)

    dest = OUTPUT_DIR / f"{subject}.png"
    dest.parent.mkdir(parents=True, exist_ok=True)

    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)

    size_kb = dest.stat().st_size // 1024
    print(f"  Saved: {dest.resolve()}  ({size_kb} KB)")
    return dest


def main():
    parser = argparse.ArgumentParser(
        description="Generate MoCloud brand infographics — free via Pollinations.ai (no API key needed)"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--subject", choices=list(PROMPTS.keys()), help="Which infographic to generate")
    group.add_argument("--all", action="store_true", help="Generate all 4 core infographics")
    args = parser.parse_args()

    subjects = CORE_SUBJECTS if args.all else [args.subject]
    results = []

    for i, subject in enumerate(subjects):
        if i > 0:
            print(f"\n  Waiting {DELAY_BETWEEN}s before next request...")
            time.sleep(DELAY_BETWEEN)
        dest = generate(subject)
        results.append(dest)

    print(f"\n{'='*52}")
    print(f"  Done. {len(results)} infographic(s) generated.")
    print(f"  Output dir: {OUTPUT_DIR.resolve()}")
    for r in results:
        print(f"    {r.name}")
    print(f"\n  To approve: copy from .tmp/infographics/ → brand_assets/infographics/")
    print(f"{'='*52}\n")


if __name__ == "__main__":
    main()
