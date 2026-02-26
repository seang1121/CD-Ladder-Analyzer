# 🪜 CD Ladder Simulator

**Compare CD rates, ladder strategies, and find the best institution for your savings.**

Navy Federal vs. Top Competitors | Pentagon Federal | Connexus | Ally | Marcus | Vanguard

## 📊 Live Dashboard

👉 **[View Live Dashboard](https://seang1121.github.io/CD-Ladder-Analyzer/)**

## Quick Start

```bash
python cd_ladder_simulator.py
```

Generates:
- **Rate comparison** across 6 institutions
- **Ladder strategy analysis** (3-rung, 5-rung, barbell)
- **Navy Federal deep dive** with rate advantages
- **Maturity schedules** showing when funds unlock
- **Recommendations** by eligibility & goals

## What is a CD Ladder?

A **CD ladder** is a savings strategy where you:
- Split money into multiple CDs with different maturity dates
- Get automatic access to funds every X months/years
- Capture higher rates on longer terms
- Adjust to rate changes as each rung matures

### Example: $50K CD Ladder

```
Year 1:  $10K matures → Reinvest or access
Year 2:  $10K matures → Reinvest or access
Year 3:  $10K matures → Reinvest or access
Year 4:  $10K matures → Reinvest or access
Year 5:  $10K matures → Reinvest or access
```

Result: $7,550 interest earned over 5 years

## 6 Institutions Analyzed

| Institution | Type | Best For | 5-Yr Rate |
|-------------|------|----------|-----------|
| Pentagon Federal | Credit Union | DoD/Military families | 5.50% |
| Navy Federal | Credit Union | Military members | 5.45% |
| Connexus | Credit Union | Non-military, open to all | 5.40% |
| Vanguard | Brokerage | Investors, platform integration | 5.45% |
| Ally | Online Bank | Easy access, no fees | 5.25% |
| Marcus | Online Bank | Premium service | 5.20% |

## Ladder Strategies

### 3-Rung Short
- Maturity every 6-8 months
- Quick access to funds
- Good if rates are improving
- **Interest: ~$3,550 on $50K**

### 5-Rung Classic ⭐
- Maturity every year
- Balanced approach
- Most popular strategy
- **Interest: ~$7,550 on $50K**

### 5-Rung Staggered
- Pyramid allocation (more in longer terms)
- Higher yield
- Less frequent access needed
- **Interest: ~$8,200 on $50K**

### Barbell Strategy
- Short + long terms only (skip middle)
- Protect against rate swings
- Flexibility + yield mix
- **Interest: ~$7,420 on $50K**

## Who Should Use CD Ladders?

✅ **Good for:**
- Building emergency fund access
- Locking in current rates
- Reducing decision fatigue
- Consistent savings strategy

❌ **Not ideal for:**
- Needing liquidity <1 year
- Very short-term savings
- Frequent rate-chasing

## Key Advantages

🔓 **Automatic Liquidity** — funds unlock on schedule
📈 **Higher Yields** — capture better rates on longer terms
🛡️ **Rate Insurance** — split bets across market conditions
⏳ **Simplified Reinvestment** — reinvest maturing CDs automatically
💳 **Penalty Protection** — no early withdrawal fees if you wait

## Features

✅ Live rate comparison across 6 institutions
✅ Multiple ladder strategies
✅ Maturity schedule generator
✅ Institution feature comparison
✅ Customizable principal amount
✅ Interest & yield projections

## Running Locally

```bash
# Generate full analysis
python cd_ladder_simulator.py

# Output: Complete report with all strategies
```

## Files

- `cd_ladder_simulator.py` — Main analyzer
- `CD_LADDER_REPORT.md` — Latest generated report
- `index.html` — GitHub Pages dashboard
- `README.md` — This file

## Rates Updated

**Feb 2026** — Current market rates snapshot

## License

Personal use. Rates are for illustration; verify with institutions before opening accounts.

---

**Live Website:** https://seang1121.github.io/CD-Ladder-Analyzer/
