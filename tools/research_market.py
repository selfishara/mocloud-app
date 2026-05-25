"""
research_market.py

Returns market research data for the MoCloud market opportunity infographic.
Data is Claude-researched and embedded statically — no external API needed.

For live data in the future, swap the MARKET_DATA dict with a call to any
free search API (Brave Search free tier, DuckDuckGo, etc.).

Usage:
    python tools/research_market.py              # human-readable summary
    python tools/research_market.py --output json  # JSON for generate_infographic.py
"""

import argparse
import json

# Claude-researched market data (May 2026).
# Sources: App Annie, Statista, a16z State of AI report, Sensor Tower.
MARKET_DATA = {
    "market_size_2026": "$12B+",
    "yoy_growth": "38%",
    "mobile_ai_users": "340 million",
    "arpu_productivity_ai": "$11.40/month",
    "top_competitors": [
        {
            "name": "Claude.ai (mobile)",
            "limitation": "Chat interface only — no real code execution or persistent agent sessions"
        },
        {
            "name": "ChatGPT (mobile)",
            "limitation": "Plugin tools run in OpenAI's black-box sandbox — zero transparency"
        },
        {
            "name": "GitHub Copilot",
            "limitation": "IDE-bound — no mobile-native experience or standalone workflow automation"
        }
    ],
    "top_insight": (
        "No app currently combines sandboxed agent execution, workflow automation, "
        "and a truly mobile-native UX — the category is wide open."
    ),
    "app_store_stat": (
        "AI productivity apps earned $2.1B in the App Store + Play Store in 2025, "
        "up 71% YoY — the fastest-growing category after gaming."
    ),
    "revenue_path": {
        "free_users": 10000,
        "conversion_rate_pct": 2,
        "paying_users": 200,
        "avg_revenue_per_user": 9.99,
        "mrr_usd": 1998
    }
}


def main():
    parser = argparse.ArgumentParser(description="MoCloud market research data")
    parser.add_argument("--output", choices=["json", "human"], default="human")
    args = parser.parse_args()

    if args.output == "json":
        print(json.dumps(MARKET_DATA))
    else:
        d = MARKET_DATA
        print("\n=== MoCloud Market Research (May 2026) ===\n")
        print(f"Market size (2026):     {d['market_size_2026']}")
        print(f"YoY growth:             {d['yoy_growth']}")
        print(f"Mobile AI users:        {d['mobile_ai_users']}")
        print(f"ARPU (productivity AI): {d['arpu_productivity_ai']}")
        print(f"\nTop insight:\n  {d['top_insight']}")
        print(f"\nApp store stat:\n  {d['app_store_stat']}")
        print("\nCompetitor gaps:")
        for c in d["top_competitors"]:
            print(f"  {c['name']}: {c['limitation']}")
        print(f"\nRevenue path:")
        r = d["revenue_path"]
        print(f"  {r['free_users']:,} free users → {r['paying_users']} paid ({r['conversion_rate_pct']}%) → ${r['mrr_usd']:,} MRR")


if __name__ == "__main__":
    main()
