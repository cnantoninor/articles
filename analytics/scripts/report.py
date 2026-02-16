#!/usr/bin/env python3
"""Generate weekly analytics report in Markdown format.

Runs merge.py if needed, calls analyze.py, and generates a Markdown report.

Usage:
    python analytics/scripts/report.py [--date YYYY-MM-DD]
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
COMBINED_DIR = DATA_DIR / "combined"
REPORTS_DIR = SCRIPT_DIR.parent / "reports"


def run_merge():
    """Run merge.py to ensure snapshot is up to date."""
    merge_script = SCRIPT_DIR / "merge.py"
    result = subprocess.run([sys.executable, str(merge_script)], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: merge.py failed: {result.stderr}", file=sys.stderr)
    return result.returncode == 0


def run_analyze() -> dict:
    """Run analyze.py and return results as dict."""
    analyze_script = SCRIPT_DIR / "analyze.py"
    result = subprocess.run([sys.executable, str(analyze_script), "--output", "json"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: analyze.py failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse analyze.py output: {e}", file=sys.stderr)
        sys.exit(1)


def generate_report(analysis: dict, report_date: str) -> str:
    """Generate Markdown report from analysis results."""
    lines = []
    
    lines.append(f"# Weekly Analytics Report — {report_date}")
    lines.append("")
    lines.append(f"*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")
    
    # Subscriber Growth Summary
    lines.append("## Subscriber Growth Summary")
    lines.append("")
    growth = analysis.get("subscriber_growth", {})
    if "error" in growth:
        lines.append(f"⚠️  {growth['error']}")
    else:
        lines.append(f"- **Current subscribers**: {growth['current_subscribers']}")
        lines.append(f"- **Growth rate**: {growth['growth_rate_per_week']:.1f} subscribers per week")
        if growth.get("days_to_100"):
            lines.append(f"- **Projected days to 100 subscribers**: {growth['days_to_100']} days")
        else:
            lines.append("- **Projected days to 100**: Unable to project (negative or zero growth)")
        lines.append(f"- **Data quality**: R² = {growth.get('r_squared', 'N/A')} ({growth.get('data_points', 0)} data points)")
    lines.append("")
    
    # Traffic Breakdown
    lines.append("## Traffic Breakdown")
    lines.append("")
    channel_roi = analysis.get("channel_roi", [])
    if isinstance(channel_roi, list) and channel_roi:
        lines.append("| Channel | Sessions | Users | New Users |")
        lines.append("|---------|----------|-------|-----------|")
        for channel in channel_roi[:10]:  # Top 10
            lines.append(f"| {channel.get('source', 'N/A')} | {channel.get('sessions', 0)} | {channel.get('users', 0)} | {channel.get('new_users', 0)} |")
    else:
        lines.append("⚠️  No traffic source data available")
    lines.append("")
    
    # Top Articles
    lines.append("## Top Performing Articles")
    lines.append("")
    top_articles = analysis.get("top_articles", {})
    if top_articles:
        if "by_pageviews" in top_articles and top_articles["by_pageviews"]:
            lines.append("### By Page Views")
            for i, article in enumerate(top_articles["by_pageviews"][:3], 1):
                slug = article.get("article_slug", "N/A")
                pv = article.get("pageviews", 0)
                date = article.get("date", "N/A")
                lines.append(f"{i}. **{slug}** — {pv} views ({date})")
            lines.append("")
        
        if "by_open_rate" in top_articles and top_articles["by_open_rate"]:
            lines.append("### By Email Open Rate")
            for i, article in enumerate(top_articles["by_open_rate"][:3], 1):
                slug = article.get("article_slug", "N/A")
                rate = article.get("open_rate", 0)
                date = article.get("date", "N/A")
                lines.append(f"{i}. **{slug}** — {rate:.1%} open rate ({date})")
            lines.append("")
        
        if "by_engagement" in top_articles and top_articles["by_engagement"]:
            lines.append("### By Engagement (Likes + Comments + Restacks)")
            for i, article in enumerate(top_articles["by_engagement"][:3], 1):
                slug = article.get("article_slug", "N/A")
                score = article.get("engagement_score", 0)
                likes = article.get("likes", 0)
                comments = article.get("comments", 0)
                restacks = article.get("restacks", 0)
                date = article.get("date", "N/A")
                lines.append(f"{i}. **{slug}** — {score} total ({likes} likes, {comments} comments, {restacks} restacks) ({date})")
            lines.append("")
    else:
        lines.append("⚠️  No article performance data available")
    lines.append("")
    
    # Week-over-Week Changes
    lines.append("## Week-over-Week Changes")
    lines.append("")
    wow = analysis.get("week_over_week", {})
    if "error" in wow:
        lines.append(f"⚠️  {wow['error']}")
    else:
        changes = wow.get("changes", {})
        if changes:
            if "pageviews" in changes:
                pv = changes["pageviews"]
                change_str = f"{pv['change']:+d}" if pv['change'] != 0 else "0"
                pct_str = f"({pv['change_pct']:+.1f}%)" if pv['change_pct'] != 0 else ""
                lines.append(f"- **Page views**: {pv['last_week']} (prev: {pv['prev_week']}) {change_str} {pct_str}")
            
            if "subscribers" in changes:
                subs = changes["subscribers"]
                change_str = f"{subs['change']:+d}" if subs['change'] != 0 else "0"
                pct_str = f"({subs['change_pct']:+.1f}%)" if subs['change_pct'] != 0 else ""
                lines.append(f"- **Subscribers**: {subs['last_week']} (prev: {subs['prev_week']}) {change_str} {pct_str}")
        else:
            lines.append("⚠️  No week-over-week data available")
    lines.append("")
    
    # Actionable Recommendations
    lines.append("## Actionable Recommendations")
    lines.append("")
    recommendations = []
    
    # Growth recommendations
    if "error" not in growth:
        if growth.get("days_to_100") and growth["days_to_100"] > 90:
            recommendations.append("⚠️  Growth rate is slow — projected timeline exceeds 90 days. Consider increasing posting frequency or improving distribution.")
        elif growth.get("days_to_100") and growth["days_to_100"] < 30:
            recommendations.append("✅ Growth rate is strong — on track to reach 100 subscribers soon. Maintain current cadence.")
    
    # Channel recommendations
    if isinstance(channel_roi, list) and len(channel_roi) > 0:
        top_channel = max(channel_roi, key=lambda x: x.get("sessions", 0))
        if top_channel.get("sessions", 0) > 0:
            recommendations.append(f"📈 Top traffic source: **{top_channel.get('source')}** ({top_channel.get('sessions')} sessions). Consider doubling down on this channel.")
    
    # Article recommendations
    if top_articles:
        if "by_pageviews" in top_articles and top_articles["by_pageviews"]:
            top_article = top_articles["by_pageviews"][0]
            recommendations.append(f"🔥 Top article: **{top_article.get('article_slug')}** ({top_article.get('pageviews')} views). Analyze what made it successful and replicate.")
    
    if recommendations:
        for rec in recommendations:
            lines.append(f"- {rec}")
    else:
        lines.append("No specific recommendations at this time. Continue tracking metrics.")
    
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*For detailed data, see `analytics/data/combined/weekly_snapshot.csv`*")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate weekly analytics report")
    parser.add_argument("--date", help="Report date (YYYY-MM-DD, default: today)")
    
    args = parser.parse_args()
    
    # Determine report date
    if args.date:
        report_date = args.date
    else:
        report_date = datetime.now().strftime("%Y-%m-%d")
    
    # Ensure merge has run
    print("Ensuring data is merged...", file=sys.stderr)
    run_merge()
    
    # Run analysis
    print("Running analysis...", file=sys.stderr)
    analysis = run_analyze()
    
    # Generate report
    print("Generating report...", file=sys.stderr)
    report_content = generate_report(analysis, report_date)
    
    # Write report
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_file = REPORTS_DIR / f"weekly-{report_date}.md"
    
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"Report written to {report_file}", file=sys.stderr)
    print(f"\n{report_file}", file=sys.stdout)


if __name__ == "__main__":
    main()
