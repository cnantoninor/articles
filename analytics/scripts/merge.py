#!/usr/bin/env python3
"""Merge GA4 and manual data into unified weekly snapshot.

Reads all CSV files from data/ga4/ and data/manual/, joins on date and
article_slug where applicable, and writes a unified weekly_snapshot.csv.

Usage:
    python analytics/scripts/merge.py
"""

import csv
from pathlib import Path
from typing import Optional

import pandas as pd

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
GA4_DIR = DATA_DIR / "ga4"
MANUAL_DIR = DATA_DIR / "manual"
COMBINED_DIR = DATA_DIR / "combined"


def load_ga4_data() -> dict[str, pd.DataFrame]:
    """Load all GA4 CSV files."""
    data = {}
    
    for csv_file in GA4_DIR.glob("*.csv"):
        if csv_file.name == ".gitkeep":
            continue
        try:
            df = pd.read_csv(csv_file)
            if not df.empty:
                data[csv_file.stem] = df
        except Exception as e:
            print(f"Warning: Failed to load {csv_file.name}: {e}")
    
    return data


def load_manual_data() -> dict[str, pd.DataFrame]:
    """Load all manual CSV files."""
    data = {}
    
    for csv_file in MANUAL_DIR.glob("*.csv"):
        if csv_file.name == ".gitkeep":
            continue
        try:
            df = pd.read_csv(csv_file)
            if not df.empty:
                data[csv_file.stem] = df
        except Exception as e:
            print(f"Warning: Failed to load {csv_file.name}: {e}")
    
    return data


def merge_data(ga4_data: dict[str, pd.DataFrame], manual_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Merge GA4 and manual data into unified snapshot."""
    # Start with pageviews as base (has date + article_slug)
    if "pageviews" not in ga4_data:
        print("Warning: No pageviews data found. Creating empty snapshot.")
        return pd.DataFrame()
    
    snapshot = ga4_data["pageviews"].copy()
    
    # Merge traffic sources (aggregate by date)
    if "traffic_sources" in ga4_data:
        traffic = ga4_data["traffic_sources"].groupby("date").agg({
            "sessions": "sum",
            "users": "sum",
            "new_users": "sum",
            "bounce_rate": "mean",
        }).reset_index()
        snapshot = snapshot.merge(traffic, on="date", how="left", suffixes=("", "_traffic"))
    
    # Merge user behavior (by date)
    if "user_behavior" in ga4_data:
        behavior = ga4_data["user_behavior"][["date", "bounce_rate", "session_duration"]].copy()
        snapshot = snapshot.merge(behavior, on="date", how="left", suffixes=("", "_behavior"))
    
    # Merge manual data: subscribers (by date only)
    if "subscribers" in manual_data:
        subs = manual_data["subscribers"][["date", "total_subscribers", "free_subscribers", "paid_subscribers", "net_new"]].copy()
        snapshot = snapshot.merge(subs, on="date", how="left")
    
    # Merge email metrics (by date_published + article_slug)
    if "email_metrics" in manual_data:
        email = manual_data["email_metrics"].copy()
        email = email.rename(columns={"date_published": "date"})
        snapshot = snapshot.merge(email, on=["date", "article_slug"], how="left", suffixes=("", "_email"))
    
    # Merge substack engagement (by date_published + article_slug)
    if "substack_engagement" in manual_data:
        substack = manual_data["substack_engagement"].copy()
        substack = substack.rename(columns={"date_published": "date"})
        snapshot = snapshot.merge(substack, on=["date", "article_slug"], how="left", suffixes=("", "_substack"))
    
    # Merge social engagement (by date_posted + article_slug + platform)
    # This is trickier - we'll aggregate by article_slug and date
    if "social_engagement" in manual_data:
        social = manual_data["social_engagement"].copy()
        social = social.rename(columns={"date_posted": "date"})
        # Aggregate social metrics by date + article_slug (sum across platforms)
        social_agg = social.groupby(["date", "article_slug"]).agg({
            "impressions": "sum",
            "likes": "sum",
            "comments": "sum",
            "shares": "sum",
            "link_clicks": "sum",
        }).reset_index()
        snapshot = snapshot.merge(social_agg, on=["date", "article_slug"], how="left", suffixes=("", "_social"))
    
    # Sort by date, then article_slug
    snapshot = snapshot.sort_values(["date", "article_slug"]).reset_index(drop=True)
    
    return snapshot


def main():
    print("Loading GA4 data...")
    ga4_data = load_ga4_data()
    print(f"  Loaded {len(ga4_data)} GA4 file(s)")
    
    print("Loading manual data...")
    manual_data = load_manual_data()
    print(f"  Loaded {len(manual_data)} manual file(s)")
    
    if not ga4_data and not manual_data:
        print("ERROR: No data files found.")
        return
    
    print("Merging data...")
    snapshot = merge_data(ga4_data, manual_data)
    
    if snapshot.empty:
        print("Warning: Merged snapshot is empty.")
        return
    
    # Write to combined directory
    COMBINED_DIR.mkdir(parents=True, exist_ok=True)
    output_file = COMBINED_DIR / "weekly_snapshot.csv"
    snapshot.to_csv(output_file, index=False)
    
    print(f"Wrote {len(snapshot)} rows to {output_file}")
    print(f"Columns: {', '.join(snapshot.columns)}")


if __name__ == "__main__":
    main()
