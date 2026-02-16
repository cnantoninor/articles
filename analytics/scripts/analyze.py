#!/usr/bin/env python3
"""Analyze analytics data and compute trends, projections, and rankings.

Loads combined/weekly_snapshot.csv and computes:
- Subscriber growth rate and projection to 100 subscribers
- Top articles by various metrics
- Channel ROI analysis
- Week-over-week trends

Outputs structured data (JSON) for report.py to consume.

Usage:
    python analytics/scripts/analyze.py [--output json|text]
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

import numpy as np
import pandas as pd
from scipy import stats

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
COMBINED_DIR = DATA_DIR / "combined"
SNAPSHOT_FILE = COMBINED_DIR / "weekly_snapshot.csv"


def load_snapshot() -> pd.DataFrame:
    """Load the combined weekly snapshot."""
    if not SNAPSHOT_FILE.exists():
        print(f"ERROR: Snapshot file not found: {SNAPSHOT_FILE}", file=sys.stderr)
        print("Run merge.py first to create the snapshot.", file=sys.stderr)
        sys.exit(1)
    
    return pd.read_csv(SNAPSHOT_FILE)


def compute_subscriber_growth(snapshot: pd.DataFrame) -> Dict[str, Any]:
    """Compute subscriber growth rate and projection to 100."""
    if "total_subscribers" not in snapshot.columns:
        return {"error": "No subscriber data available"}
    
    # Get unique dates with subscriber data
    subs_data = snapshot[["date", "total_subscribers"]].dropna().drop_duplicates("date")
    if len(subs_data) < 2:
        return {"error": "Insufficient subscriber data (need at least 2 data points)"}
    
    subs_data = subs_data.sort_values("date")
    subs_data["date_ordinal"] = pd.to_datetime(subs_data["date"]).map(pd.Timestamp.toordinal)
    
    # Linear regression
    x = subs_data["date_ordinal"].values
    y = subs_data["total_subscribers"].values
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Current subscriber count (most recent)
    current_subs = int(subs_data["total_subscribers"].iloc[-1])
    current_date_ordinal = subs_data["date_ordinal"].iloc[-1]
    
    # Project to 100 subscribers
    if slope > 0:
        days_to_100 = (100 - intercept) / slope - current_date_ordinal
        days_to_100 = max(0, int(days_to_100))
    else:
        days_to_100 = None
    
    # Confidence interval (simple approximation)
    growth_rate_per_day = slope
    growth_rate_per_week = slope * 7
    
    return {
        "current_subscribers": current_subs,
        "growth_rate_per_day": round(growth_rate_per_day, 2),
        "growth_rate_per_week": round(growth_rate_per_week, 2),
        "r_squared": round(r_value ** 2, 3),
        "days_to_100": days_to_100,
        "data_points": len(subs_data),
    }


def compute_top_articles(snapshot: pd.DataFrame) -> Dict[str, Any]:
    """Compute top articles by various metrics."""
    results = {}
    
    # Filter to article rows (has article_slug)
    articles = snapshot[snapshot["article_slug"].notna() & (snapshot["article_slug"] != "")].copy()
    
    if articles.empty:
        return {"error": "No article data available"}
    
    # Top by pageviews
    if "pageviews" in articles.columns:
        top_pageviews = articles.nlargest(3, "pageviews")[["article_slug", "pageviews", "date"]].to_dict("records")
        results["by_pageviews"] = top_pageviews
    
    # Top by open rate (email metrics)
    if "open_rate" in articles.columns:
        top_open_rate = articles[articles["open_rate"].notna()].nlargest(3, "open_rate")[
            ["article_slug", "open_rate", "date"]
        ].to_dict("records")
        results["by_open_rate"] = top_open_rate
    
    # Top by engagement (likes + comments + restacks)
    if all(col in articles.columns for col in ["likes", "comments", "restacks"]):
        articles["engagement_score"] = (
            articles["likes"].fillna(0) + articles["comments"].fillna(0) + articles["restacks"].fillna(0)
        )
        top_engagement = articles.nlargest(3, "engagement_score")[
            ["article_slug", "engagement_score", "likes", "comments", "restacks", "date"]
        ].to_dict("records")
        results["by_engagement"] = top_engagement
    
    return results


def compute_channel_roi(snapshot: pd.DataFrame) -> Dict[str, Any]:
    """Compute channel ROI (sessions and subscribers by source)."""
    # Load raw traffic_sources data
    traffic_file = DATA_DIR / "ga4" / "traffic_sources.csv"
    if not traffic_file.exists():
        return {"error": "No traffic sources data available"}
    
    traffic = pd.read_csv(traffic_file)
    
    # Aggregate by source
    channel_stats = traffic.groupby("source").agg({
        "sessions": "sum",
        "users": "sum",
        "new_users": "sum",
    }).reset_index()
    
    # Try to correlate with subscriber growth (simplified)
    # This is a rough approximation - in reality would need better attribution
    channel_stats["sessions_per_new_user"] = (
        channel_stats["new_users"].replace(0, np.nan) / channel_stats["sessions"]
    ).fillna(0)
    
    return channel_stats.to_dict("records")


def compute_week_over_week(snapshot: pd.DataFrame) -> Dict[str, Any]:
    """Compute week-over-week changes."""
    results = {}
    
    # Get unique dates
    dates = sorted(snapshot["date"].unique())
    if len(dates) < 2:
        return {"error": "Insufficient data for week-over-week comparison"}
    
    # Compare last two weeks
    last_week = dates[-1]
    prev_week = dates[-2] if len(dates) >= 2 else None
    
    if not prev_week:
        return {"error": "Need at least 2 weeks of data"}
    
    last_data = snapshot[snapshot["date"] == last_week]
    prev_data = snapshot[snapshot["date"] == prev_week]
    
    changes = {}
    
    # Pageviews
    if "pageviews" in snapshot.columns:
        last_pv = last_data["pageviews"].sum()
        prev_pv = prev_data["pageviews"].sum()
        changes["pageviews"] = {
            "last_week": int(last_pv),
            "prev_week": int(prev_pv),
            "change": int(last_pv - prev_pv),
            "change_pct": round((last_pv - prev_pv) / prev_pv * 100, 1) if prev_pv > 0 else 0,
        }
    
    # Subscribers
    if "total_subscribers" in snapshot.columns:
        last_subs = last_data["total_subscribers"].dropna()
        prev_subs = prev_data["total_subscribers"].dropna()
        if not last_subs.empty and not prev_subs.empty:
            last_subs_val = int(last_subs.iloc[-1])
            prev_subs_val = int(prev_subs.iloc[-1])
            changes["subscribers"] = {
                "last_week": last_subs_val,
                "prev_week": prev_subs_val,
                "change": last_subs_val - prev_subs_val,
                "change_pct": round((last_subs_val - prev_subs_val) / prev_subs_val * 100, 1) if prev_subs_val > 0 else 0,
            }
    
    results["changes"] = changes
    results["last_week_date"] = last_week
    results["prev_week_date"] = prev_week
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Analyze analytics data")
    parser.add_argument("--output", choices=["json", "text"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    print("Loading snapshot...", file=sys.stderr)
    snapshot = load_snapshot()
    
    print("Computing subscriber growth...", file=sys.stderr)
    growth = compute_subscriber_growth(snapshot)
    
    print("Computing top articles...", file=sys.stderr)
    top_articles = compute_top_articles(snapshot)
    
    print("Computing channel ROI...", file=sys.stderr)
    channel_roi = compute_channel_roi(snapshot)
    
    print("Computing week-over-week changes...", file=sys.stderr)
    wow = compute_week_over_week(snapshot)
    
    results = {
        "subscriber_growth": growth,
        "top_articles": top_articles,
        "channel_roi": channel_roi,
        "week_over_week": wow,
    }
    
    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        # Text output for readability
        print("\n=== Subscriber Growth ===")
        if "error" in growth:
            print(f"  {growth['error']}")
        else:
            print(f"  Current: {growth['current_subscribers']} subscribers")
            print(f"  Growth rate: {growth['growth_rate_per_week']:.1f} per week")
            if growth.get("days_to_100"):
                print(f"  Projected days to 100: {growth['days_to_100']}")
        
        print("\n=== Top Articles ===")
        for metric, articles in top_articles.items():
            if "error" not in articles:
                print(f"\n  By {metric}:")
                for article in articles[:3]:
                    print(f"    {article['article_slug']}: {article.get('pageviews', article.get('open_rate', article.get('engagement_score', 'N/A')))}")
        
        print("\n=== Channel ROI ===")
        if "error" not in channel_roi:
            for channel in channel_roi[:5]:
                print(f"  {channel['source']}: {channel['sessions']} sessions, {channel['new_users']} new users")


if __name__ == "__main__":
    main()
