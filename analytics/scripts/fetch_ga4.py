#!/usr/bin/env python3
"""Fetch GA4 data and write to CSV files.

Pulls page views, traffic sources, referrals, and user behavior from GA4
property 361268692 via the Google Analytics Data API. Writes data to CSV files
in analytics/data/ga4/.

Usage:
    python analytics/scripts/fetch_ga4.py [--start YYYY-MM-DD] [--end YYYY-MM-DD] [--replace]
    python analytics/scripts/fetch_ga4.py --property-id 361268692 --days 7

Environment variables:
    GOOGLE_APPLICATION_CREDENTIALS: Path to GCP service account JSON (default: analytics/credentials/ga4-service-account.json)
    GA4_PROPERTY_ID: GA4 property ID (default: 361268692)
"""

import argparse
import csv
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
except ImportError:
    print("ERROR: google-analytics-data is required. Install with: pip install google-analytics-data")
    sys.exit(1)


# Default configuration
DEFAULT_PROPERTY_ID = "361268692"
DEFAULT_CREDENTIALS_PATH = Path(__file__).parent.parent.parent / "analytics" / "credentials" / "ga4-service-account.json"
DEFAULT_DAYS = 7
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data" / "ga4"


def derive_article_slug(page_path: str) -> str:
    """Extract article slug from GA4 page_path.
    
    Substack articles use /p/<slug> format.
    Returns empty string for homepage or non-article paths.
    """
    if not page_path:
        return ""
    if page_path.startswith("/p/"):
        return page_path[3:]  # Strip "/p/" prefix
    return ""  # Homepage or other paths


def get_credentials_path() -> str:
    """Get path to GCP service account credentials."""
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if creds_path:
        return creds_path
    return str(DEFAULT_CREDENTIALS_PATH)


def get_property_id() -> str:
    """Get GA4 property ID from env or default."""
    return os.getenv("GA4_PROPERTY_ID", DEFAULT_PROPERTY_ID)


def parse_date_range(start_str: str = None, end_str: str = None, days: int = None) -> tuple[str, str]:
    """Parse date range from strings or compute from days offset."""
    if days:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
    
    if end_str:
        end_date = datetime.strptime(end_str, "%Y-%m-%d")
    else:
        end_date = datetime.now()
    
    if start_str:
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
    else:
        start_date = end_date - timedelta(days=DEFAULT_DAYS)
    
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")


def fetch_pageviews(client: BetaAnalyticsDataClient, property_id: str, start_date: str, end_date: str) -> list[dict]:
    """Fetch page view data from GA4."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date"), Dimension(name="pagePath")],
        metrics=[
            Metric(name="screenPageViews"),
            Metric(name="sessions"),
            Metric(name="averageSessionDuration"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    
    response = client.run_report(request)
    results = []
    
    for row in response.rows:
        date_val = row.dimension_values[0].value
        page_path = row.dimension_values[1].value
        pageviews = int(row.metric_values[0].value)
        sessions = int(row.metric_values[1].value)
        avg_duration = float(row.metric_values[2].value) if row.metric_values[2].value else 0.0
        
        results.append({
            "date": date_val,
            "page_path": page_path,
            "article_slug": derive_article_slug(page_path),
            "pageviews": pageviews,
            "unique_pageviews": sessions,  # Using sessions as proxy for unique pageviews
            "avg_time_on_page": avg_duration,
        })
    
    return results


def fetch_traffic_sources(client: BetaAnalyticsDataClient, property_id: str, start_date: str, end_date: str) -> list[dict]:
    """Fetch traffic source data from GA4."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date"), Dimension(name="sessionSource"), Dimension(name="sessionMedium")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="totalUsers"),
            Metric(name="newUsers"),
            Metric(name="bounceRate"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    
    response = client.run_report(request)
    results = []
    
    for row in response.rows:
        date_val = row.dimension_values[0].value
        source = row.dimension_values[1].value
        medium = row.dimension_values[2].value
        sessions = int(row.metric_values[0].value)
        users = int(row.metric_values[1].value)
        new_users = int(row.metric_values[2].value)
        bounce_rate = float(row.metric_values[3].value) if row.metric_values[3].value else 0.0
        
        results.append({
            "date": date_val,
            "source": source,
            "medium": medium,
            "sessions": sessions,
            "users": users,
            "new_users": new_users,
            "bounce_rate": bounce_rate,
        })
    
    return results


def fetch_referrals(client: BetaAnalyticsDataClient, property_id: str, start_date: str, end_date: str) -> list[dict]:
    """Fetch referral data from GA4."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date"), Dimension(name="fullPageUrl")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    
    response = client.run_report(request)
    results = []
    
    for row in response.rows:
        date_val = row.dimension_values[0].value
        referrer = row.dimension_values[1].value
        sessions = int(row.metric_values[0].value)
        pageviews = int(row.metric_values[1].value)
        
        results.append({
            "date": date_val,
            "full_referrer": referrer,
            "sessions": sessions,
            "pageviews": pageviews,
        })
    
    return results


def fetch_user_behavior(client: BetaAnalyticsDataClient, property_id: str, start_date: str, end_date: str) -> list[dict]:
    """Fetch user behavior metrics from GA4."""
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="bounceRate"),
            Metric(name="averageSessionDuration"),
        ],
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )
    
    response = client.run_report(request)
    results = []
    
    for row in response.rows:
        date_val = row.dimension_values[0].value
        bounce_rate = float(row.metric_values[0].value) if row.metric_values[0].value else 0.0
        session_duration = float(row.metric_values[1].value) if row.metric_values[1].value else 0.0
        
        results.append({
            "date": date_val,
            "bounce_rate": bounce_rate,
            "session_duration": session_duration,
            "scroll_depth": "",  # Not available in standard GA4; placeholder for future custom events
        })
    
    return results


def write_csv(filepath: Path, data: list[dict], append: bool = True):
    """Write data to CSV file."""
    if not data:
        return
    
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    mode = "a" if append and filepath.exists() else "w"
    fieldnames = list(data[0].keys())
    
    with open(filepath, mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if mode == "w":
            writer.writeheader()
        writer.writerows(data)


def main():
    parser = argparse.ArgumentParser(description="Fetch GA4 data and write to CSV files")
    parser.add_argument("--start", help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", help="End date (YYYY-MM-DD)")
    parser.add_argument("--days", type=int, help=f"Number of days back from today (default: {DEFAULT_DAYS})")
    parser.add_argument("--replace", action="store_true", help="Replace existing CSV files instead of appending")
    parser.add_argument("--property-id", help=f"GA4 property ID (default: {DEFAULT_PROPERTY_ID})")
    
    args = parser.parse_args()
    
    # Get credentials path
    creds_path = get_credentials_path()
    if not os.path.exists(creds_path):
        print(f"ERROR: Credentials file not found: {creds_path}")
        print("Please create a GCP service account and download the JSON key.")
        print("See docs/mcp-setup.md for setup instructions.")
        sys.exit(1)
    
    # Set credentials in environment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path
    
    # Get property ID
    property_id = args.property_id or get_property_id()
    
    # Parse date range
    start_date, end_date = parse_date_range(args.start, args.end, args.days)
    
    print(f"Fetching GA4 data for property {property_id}")
    print(f"Date range: {start_date} to {end_date}")
    
    # Initialize client
    try:
        client = BetaAnalyticsDataClient()
    except Exception as e:
        print(f"ERROR: Failed to initialize GA4 client: {e}")
        print("Check that GOOGLE_APPLICATION_CREDENTIALS points to a valid service account JSON.")
        sys.exit(1)
    
    # Fetch data
    try:
        print("Fetching pageviews...")
        pageviews_data = fetch_pageviews(client, property_id, start_date, end_date)
        write_csv(DATA_DIR / "pageviews.csv", pageviews_data, append=not args.replace)
        print(f"  Wrote {len(pageviews_data)} rows to pageviews.csv")
        
        print("Fetching traffic sources...")
        traffic_data = fetch_traffic_sources(client, property_id, start_date, end_date)
        write_csv(DATA_DIR / "traffic_sources.csv", traffic_data, append=not args.replace)
        print(f"  Wrote {len(traffic_data)} rows to traffic_sources.csv")
        
        print("Fetching referrals...")
        referrals_data = fetch_referrals(client, property_id, start_date, end_date)
        write_csv(DATA_DIR / "referrals.csv", referrals_data, append=not args.replace)
        print(f"  Wrote {len(referrals_data)} rows to referrals.csv")
        
        print("Fetching user behavior...")
        behavior_data = fetch_user_behavior(client, property_id, start_date, end_date)
        write_csv(DATA_DIR / "user_behavior.csv", behavior_data, append=not args.replace)
        print(f"  Wrote {len(behavior_data)} rows to user_behavior.csv")
        
        print("\nDone! Data written to analytics/data/ga4/")
        
    except Exception as e:
        print(f"ERROR: Failed to fetch GA4 data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
