# Tools

Deterministic Python scripts. Each script does one thing reliably.

## Conventions
- Accept inputs via CLI args or a small config dict at the top
- Print clear success/error output
- Exit with code 0 on success, non-zero on failure
- Load credentials from `.env` via `python-dotenv`

## Scripts
| Script | Purpose |
|--------|---------|
| `generate_infographic.py` | Generate brand infographics via kie.ai Nano Banana 2 API. Use `--all` for all 4 core infographics or `--subject <name>` for one. |
| `research_market.py` | Fetch mobile AI market stats via Perplexity API. Used automatically by `generate_infographic.py --subject market`. |

## Dependencies
Install before running any tool:
```bash
pip install requests python-dotenv
```
