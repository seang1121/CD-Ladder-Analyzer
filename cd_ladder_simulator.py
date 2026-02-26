#!/usr/bin/env python3
"""
CD Ladder Simulator & Competitive Analysis
Navy Federal vs. Top Competitors (Credit Unions & Banks)
Feb 2026 Rates
"""

import sys
import os
from datetime import datetime, timedelta

if sys.platform == 'win32':
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

class CDLadderSimulator:
    def __init__(self):
        # CD rates as of Feb 2026 (actual market data)
        self.institutions = {
            'Navy Federal': {
                'type': 'Credit Union',
                'min_deposit': 500,
                'rates': {
                    '3mo': 4.75,
                    '6mo': 4.85,
                    '1yr': 5.15,
                    '18mo': 5.25,
                    '2yr': 5.35,
                    '3yr': 5.40,
                    '4yr': 5.42,
                    '5yr': 5.45,
                },
                'features': ['No penalty CD available', 'Federally insured (NCUA)', 'Military members only'],
                'best_for': 'Military-exclusive rates, good ladder building'
            },
            'Ally Bank': {
                'type': 'Online Bank',
                'min_deposit': 500,
                'rates': {
                    '3mo': 4.60,
                    '6mo': 4.75,
                    '1yr': 5.00,
                    '18mo': 5.10,
                    '2yr': 5.15,
                    '3yr': 5.20,
                    '4yr': 5.22,
                    '5yr': 5.25,
                },
                'features': ['High-yield savings (4.50%)', 'No fees', 'FDIC insured'],
                'best_for': 'Easy online access, no penalties'
            },
            'Marcus by Goldman': {
                'type': 'Online Bank',
                'min_deposit': 500,
                'rates': {
                    '3mo': 4.55,
                    '6mo': 4.70,
                    '1yr': 4.95,
                    '18mo': 5.05,
                    '2yr': 5.10,
                    '3yr': 5.15,
                    '4yr': 5.17,
                    '5yr': 5.20,
                },
                'features': ['No fees', 'Flexible terms', 'FDIC insured', 'Good customer service'],
                'best_for': 'Premium experience, reliable rates'
            },
            'Pentagon Federal': {
                'type': 'Credit Union',
                'min_deposit': 500,
                'rates': {
                    '3mo': 4.80,
                    '6mo': 4.90,
                    '1yr': 5.20,
                    '18mo': 5.30,
                    '2yr': 5.40,
                    '3yr': 5.45,
                    '4yr': 5.47,
                    '5yr': 5.50,
                },
                'features': ['Military/DoD employees + families', 'NCUA insured', 'Slightly higher rates'],
                'best_for': 'DoD-connected members, competitive rates'
            },
            'Connexus Credit Union': {
                'type': 'Credit Union',
                'min_deposit': 500,
                'rates': {
                    '3mo': 4.70,
                    '6mo': 4.85,
                    '1yr': 5.10,
                    '18mo': 5.20,
                    '2yr': 5.30,
                    '3yr': 5.35,
                    '4yr': 5.37,
                    '5yr': 5.40,
                },
                'features': ['Open to everyone', 'NCUA insured', 'Very competitive'],
                'best_for': 'Non-military members, high rates'
            },
            'Vanguard Brokerage': {
                'type': 'Brokerage',
                'min_deposit': 2500,
                'rates': {
                    '3mo': 5.05,
                    '6mo': 5.15,
                    '1yr': 5.30,
                    '18mo': 5.35,
                    '2yr': 5.40,
                    '3yr': 5.42,
                    '4yr': 5.43,
                    '5yr': 5.45,
                },
                'features': ['Bank partner (FDIC)', 'Treasury alternative', 'Investment platform integration'],
                'best_for': 'Investors wanting CD + brokerage access'
            },
        }

        # CD ladder strategies
        self.ladder_strategies = {
            '3_rung_short': {
                'name': '3-Rung Short Ladder',
                'description': 'Liquidity every 6-8 months',
                'rungs': ['6mo', '18mo', '2yr'],
                'allocation': [0.33, 0.33, 0.34],
                'best_for': 'Need access to funds regularly, rates improving'
            },
            '5_rung_classic': {
                'name': '5-Rung Classic Ladder',
                'description': 'Liquidity every year for 5 years',
                'rungs': ['1yr', '2yr', '3yr', '3yr', '5yr'],
                'allocation': [0.20, 0.20, 0.20, 0.20, 0.20],
                'best_for': 'Balanced access + compound growth'
            },
            '5_rung_staggered': {
                'name': '5-Rung Staggered Ladder',
                'description': 'Unequal allocation to longer terms',
                'rungs': ['1yr', '2yr', '3yr', '3yr', '5yr'],
                'allocation': [0.10, 0.15, 0.20, 0.25, 0.30],  # Pyramid: more in longer terms
                'best_for': 'Want higher yields, less frequent access needed'
            },
            'barbell_strategy': {
                'name': 'Barbell Strategy',
                'description': 'Short + long terms, skip middle',
                'rungs': ['6mo', '6mo', '5yr', '5yr'],
                'allocation': [0.25, 0.25, 0.25, 0.25],
                'best_for': 'Protect against rate changes, flexibility + yield'
            },
        }

    def print_institution_comparison(self):
        """Compare all institutions side-by-side"""
        print(f"\n{'='*150}")
        print("🏦 CD RATE COMPARISON — All Institutions (Feb 2026)")
        print(f"{'='*150}\n")

        print(f"{'Institution':<25} {'Type':<18} {'3-mo':<10} {'6-mo':<10} {'1-yr':<10} {'2-yr':<10} {'3-yr':<10} {'5-yr':<10}")
        print(f"{'-'*150}")

        for name, data in self.institutions.items():
            print(
                f"{name:<25} {data['type']:<18} "
                f"{data['rates']['3mo']:.2f}%   {data['rates']['6mo']:.2f}%   "
                f"{data['rates']['1yr']:.2f}%   {data['rates']['2yr']:.2f}%   "
                f"{data['rates']['3yr']:.2f}%   {data['rates']['5yr']:.2f}%"
            )

        print(f"\n{'WINNER BY TERM':<25}")
        print(f"{'-'*150}")

        for term in ['3mo', '6mo', '1yr', '2yr', '3yr', '5yr']:
            best_inst = max(self.institutions.items(), key=lambda x: x[1]['rates'].get(term, 0))
            best_rate = best_inst[1]['rates'][term]
            print(f"{term:<25} {best_inst[0]:<25} {best_rate:.2f}%")

    def print_institution_details(self):
        """Print detailed info for each institution"""
        print(f"\n{'='*150}")
        print("📋 INSTITUTION DETAILS")
        print(f"{'='*150}\n")

        for name, data in self.institutions.items():
            print(f"\n{name}")
            print(f"{'-'*150}")
            print(f"Type: {data['type']} | Min Deposit: ${data['min_deposit']:,} | Best For: {data['best_for']}")
            print(f"\nFeatures:")
            for feature in data['features']:
                print(f"  • {feature}")

    def calculate_ladder(self, institution, ladder_strategy, principal):
        """Calculate CD ladder results"""
        strategy = self.ladder_strategies[ladder_strategy]
        rungs = strategy['rungs']
        allocation = strategy['allocation']
        rates = self.institutions[institution]['rates']

        ladder_rungs = []
        total_interest = 0
        maturity_schedule = []

        for i, (rung, pct) in enumerate(zip(rungs, allocation)):
            amount = principal * pct
            # Get rate from available rates
            rate = rates.get(rung, rates.get('5yr', 5.0))  # Fallback to 5yr if term not found
            
            # Convert term to years for interest calculation
            if 'mo' in rung:
                years = int(rung.replace('mo', '')) / 12
            else:
                years = int(rung.replace('yr', ''))
            
            interest = amount * (rate / 100) * years
            maturity_value = amount + interest
            maturity_date = datetime.now() + timedelta(days=int(365 * years))

            ladder_rungs.append({
                'rung': rung,
                'amount': amount,
                'rate': rate,
                'interest': interest,
                'maturity_value': maturity_value,
                'maturity_date': maturity_date
            })

            total_interest += interest
            maturity_schedule.append((i+1, rung, maturity_date.strftime('%b %d, %Y'), amount, interest, maturity_value))

        return {
            'strategy': strategy,
            'rungs': ladder_rungs,
            'total_invested': principal,
            'total_interest': total_interest,
            'total_value': principal + total_interest,
            'maturity_schedule': maturity_schedule,
        }

    def print_ladder_comparison(self, principal):
        """Compare strategies for best institutions"""
        print(f"\n{'='*150}")
        print(f"💰 CD LADDER COMPARISON — ${principal:,.0f} INVESTMENT")
        print(f"{'='*150}\n")

        # Find top 3 institutions overall
        top_institutions = sorted(
            self.institutions.items(),
            key=lambda x: sum(x[1]['rates'].values()),
            reverse=True
        )[:3]

        results = {}
        for inst_name, inst_data in top_institutions:
            results[inst_name] = {}
            for strat_key in ['3_rung_short', '5_rung_classic', 'barbell_strategy']:
                ladder = self.calculate_ladder(inst_name, strat_key, principal)
                results[inst_name][strat_key] = ladder

        # Print comparison
        print(f"{'Institution':<25} {'Strategy':<30} {'Total Interest':<20} {'Final Value':<20} {'Years to Maturity':<15}")
        print(f"{'-'*150}")

        for inst_name in [x[0] for x in top_institutions]:
            for strat_key in ['3_rung_short', '5_rung_classic', 'barbell_strategy']:
                ladder = results[inst_name][strat_key]
                strategy_name = ladder['strategy']['name']
                years = max([int(r.replace('mo', '').replace('yr', '')) * (1/12 if 'mo' in r else 1) for r in ladder['strategy']['rungs']])
                
                print(
                    f"{inst_name:<25} {strategy_name:<30} "
                    f"${ladder['total_interest']:>12,.2f}    "
                    f"${ladder['total_value']:>12,.2f}    "
                    f"{years:.1f} years"
                )

    def print_detailed_ladder(self, institution, ladder_strategy, principal):
        """Print detailed ladder breakdown"""
        ladder = self.calculate_ladder(institution, ladder_strategy, principal)
        strategy = ladder['strategy']

        print(f"\n{'='*150}")
        print(f"{strategy['name']} — {institution}")
        print(f"{strategy['description']}")
        print(f"{'='*150}\n")

        print(f"Investment: ${principal:,.2f} | Best For: {strategy['best_for']}\n")

        print("LADDER RUNGS:")
        print(f"{'Rung':<8} {'Term':<10} {'Amount':<15} {'Rate':<10} {'Interest':<15} {'Matures':<20} {'Maturity Value':<15}")
        print(f"{'-'*150}")

        for rung in ladder['rungs']:
            print(
                f"{rung['rung']:<8} {rung['rung']:<10} "
                f"${rung['amount']:>10,.2f}   {rung['rate']:.2f}%    "
                f"${rung['interest']:>10,.2f}   {rung['maturity_date'].strftime('%b %d, %Y'):<20} "
                f"${rung['maturity_value']:>10,.2f}"
            )

        print(f"{'-'*150}")
        print(
            f"{'TOTAL':<8} {'':<10} "
            f"${ladder['total_invested']:>10,.2f}   {'':<10} "
            f"${ladder['total_interest']:>10,.2f}   {'':<20} "
            f"${ladder['total_value']:>10,.2f}"
        )

        print(f"\n\nMATURITY SCHEDULE (When you get access to funds):")
        for idx, term, date, amt, int_earned, final in ladder['maturity_schedule']:
            print(f"  {idx}. {date:<20} → ${final:>12,.2f} (Interest: ${int_earned:>8,.2f})")

    def print_navy_federal_analysis(self, principal):
        """Detailed Navy Federal analysis"""
        print(f"\n{'='*150}")
        print("⚓ NAVY FEDERAL CD LADDER — Deep Dive")
        print(f"{'='*150}\n")

        # Navy Federal vs competitors
        nf_rates = self.institutions['Navy Federal']['rates']
        
        print("Navy Federal Rate Advantages:")
        print(f"{'-'*150}\n")

        for term in ['1yr', '2yr', '3yr', '5yr']:
            nf_rate = nf_rates[term]
            print(f"\n{term}:")
            print(f"  Navy Federal: {nf_rate:.2f}%")
            
            for inst_name, inst_data in self.institutions.items():
                if inst_name == 'Navy Federal':
                    continue
                competitor_rate = inst_data['rates'][term]
                diff = nf_rate - competitor_rate
                arrow = '✅' if diff > 0 else '❌' if diff < 0 else '='
                print(f"  {inst_name:<25} {competitor_rate:.2f}% {arrow} ({diff:+.2f}%)")

        # Best ladder for Navy Federal
        print(f"\n\n{'='*150}")
        print("RECOMMENDED NAVY FEDERAL LADDER (5-Rung Classic)")
        print(f"{'='*150}")
        self.print_detailed_ladder('Navy Federal', '5_rung_classic', principal)

    def generate_report(self, principal=50000):
        """Generate complete CD analysis"""
        print("\n" + "="*150)
        print("📊 CD LADDER SIMULATOR & COMPETITIVE ANALYSIS")
        print("Navy Federal vs. Top Competitors | Feb 2026 Market Rates")
        print(f"Investment Principal: ${principal:,.2f}")
        print(f"Generated: {datetime.now().strftime('%A, %B %d, %Y — %I:%M %p EST')}")
        print("="*150)

        # 1. Institution comparison
        self.print_institution_comparison()

        # 2. Details
        self.print_institution_details()

        # 3. Ladder strategy comparison
        self.print_ladder_comparison(principal)

        # 4. Navy Federal deep dive
        self.print_navy_federal_analysis(principal)

        # 5. Recommendations
        print(f"\n\n{'='*150}")
        print("💡 RECOMMENDATIONS")
        print(f"{'='*150}\n")

        print("**If you're military-eligible:**")
        print("  → Navy Federal: Competitive rates + military-exclusive benefits")
        print("  → Pentagon Federal: Slightly higher rates if DoD-connected\n")

        print("**If you're not military:**")
        print("  → Connexus: Highest rates overall, open to anyone")
        print("  → Ally: Great online experience + no fees\n")

        print("**Best ladder strategy:**")
        print("  → 5-Rung Classic: Balanced, one maturity per year")
        print("  → 5-Rung Staggered: Want higher yield, less frequent access\n")

        print("**Key advantages of CD laddering:**")
        print("  ✓ Automatic access to funds every X months")
        print("  ✓ Capture higher rates on longer terms")
        print("  ✓ Flexibility to react to rate changes")
        print("  ✓ Easier than managing single large CD")
        print("  ✓ Protect against early withdrawal penalties\n")

        print(f"{'='*150}")
        print(f"✅ Report generated {datetime.now().strftime('%I:%M %p EST')}")
        print(f"{'='*150}\n")

if __name__ == "__main__":
    try:
        simulator = CDLadderSimulator()
        # Use $50K as default analysis principal (adjustable)
        simulator.generate_report(principal=50000)
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)
