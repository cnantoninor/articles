#!/usr/bin/env python3
"""Validate and append semi-manual CSV data.

Accepts CSV rows from stdin or a file, validates against schema, checks for
duplicates, and appends to the appropriate manual data file.

Usage:
    # From stdin (paste CSV rows)
    echo "2026-02-15,42,40,2,3,\"LinkedIn post\"" | python analytics/scripts/ingest.py --target subscribers
    
    # From file
    python analytics/scripts/ingest.py --target email_metrics --file new_data.csv
    
    # Dry run (validate without writing)
    python analytics/scripts/ingest.py --target subscribers --dry-run < data.csv
"""

import argparse
import csv
import sys
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data" / "manual"

# Schema definitions
SCHEMAS = {
    "subscribers": {
        "file": "subscribers.csv",
        "columns": ["date", "total_subscribers", "free_subscribers", "paid_subscribers", "net_new", "source_notes"],
        "types": {"date": str, "total_subscribers": int, "free_subscribers": int, "paid_subscribers": int, "net_new": int, "source_notes": str},
        "duplicate_key": ["date"],
    },
    "email_metrics": {
        "file": "email_metrics.csv",
        "columns": ["date_published", "article_slug", "emails_sent", "opens", "open_rate", "clicks", "click_rate"],
        "types": {"date_published": str, "article_slug": str, "emails_sent": int, "opens": int, "open_rate": float, "clicks": int, "click_rate": float},
        "duplicate_key": ["date_published", "article_slug"],
    },
    "substack_engagement": {
        "file": "substack_engagement.csv",
        "columns": ["date_published", "article_slug", "likes", "comments", "restacks"],
        "types": {"date_published": str, "article_slug": str, "likes": int, "comments": int, "restacks": int},
        "duplicate_key": ["date_published", "article_slug"],
    },
    "social_engagement": {
        "file": "social_engagement.csv",
        "columns": ["date_posted", "article_slug", "platform", "impressions", "likes", "comments", "shares", "link_clicks", "notes"],
        "types": {"date_posted": str, "article_slug": str, "platform": str, "impressions": int, "likes": int, "comments": int, "shares": int, "link_clicks": int, "notes": str},
        "duplicate_key": ["date_posted", "article_slug", "platform"],
    },
}


def parse_value(value: str, expected_type: type) -> any:
    """Parse a CSV value according to expected type."""
    value = value.strip()
    if not value:
        return None
    
    if expected_type == int:
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Expected integer, got: {value}")
    elif expected_type == float:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Expected float, got: {value}")
    elif expected_type == str:
        return value
    else:
        return value


def validate_row(row: dict, schema: dict) -> tuple[bool, list[str]]:
    """Validate a row against schema. Returns (is_valid, errors)."""
    errors = []
    
    # Check all required columns present
    for col in schema["columns"]:
        if col not in row:
            errors.append(f"Missing column: {col}")
    
    # Check for extra columns
    for col in row:
        if col not in schema["columns"]:
            errors.append(f"Unexpected column: {col}")
    
    # Type validation
    for col, expected_type in schema["types"].items():
        if col in row and row[col]:
            try:
                parsed = parse_value(row[col], expected_type)
                row[col] = parsed
            except ValueError as e:
                errors.append(f"Column '{col}': {e}")
    
    return len(errors) == 0, errors


def check_duplicate(filepath: Path, new_row: dict, duplicate_key: list[str]) -> bool:
    """Check if a row with the same duplicate_key already exists."""
    if not filepath.exists():
        return False
    
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for existing_row in reader:
            if all(existing_row.get(key) == str(new_row.get(key)) for key in duplicate_key):
                return True
    
    return False


def read_csv_input(filepath: Optional[Path] = None) -> list[dict]:
    """Read CSV rows from file or stdin."""
    if filepath:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    else:
        # Read from stdin
        reader = csv.DictReader(sys.stdin)
        return list(reader)


def main():
    parser = argparse.ArgumentParser(description="Validate and append semi-manual CSV data")
    parser.add_argument("--target", required=True, choices=list(SCHEMAS.keys()),
                       help="Target data file (subscribers, email_metrics, substack_engagement, social_engagement)")
    parser.add_argument("--file", type=Path, help="Input CSV file (default: read from stdin)")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing")
    
    args = parser.parse_args()
    
    schema = SCHEMAS[args.target]
    filepath = DATA_DIR / schema["file"]
    
    # Read input
    try:
        rows = read_csv_input(args.file)
    except Exception as e:
        print(f"ERROR: Failed to read input: {e}", file=sys.stderr)
        sys.exit(1)
    
    if not rows:
        print("No rows to process.", file=sys.stderr)
        sys.exit(1)
    
    # Validate rows
    valid_rows = []
    all_errors = []
    
    for i, row in enumerate(rows, start=1):
        is_valid, errors = validate_row(row, schema)
        if not is_valid:
            all_errors.append(f"Row {i}: {', '.join(errors)}")
        else:
            # Check duplicates
            if check_duplicate(filepath, row, schema["duplicate_key"]):
                key_str = ", ".join(f"{k}={row.get(k)}" for k in schema["duplicate_key"])
                all_errors.append(f"Row {i}: Duplicate entry ({key_str})")
            else:
                valid_rows.append(row)
    
    # Report errors
    if all_errors:
        print("Validation errors:", file=sys.stderr)
        for error in all_errors:
            print(f"  {error}", file=sys.stderr)
        if not valid_rows:
            sys.exit(1)
        print(f"\nProceeding with {len(valid_rows)} valid row(s)...", file=sys.stderr)
    
    if not valid_rows:
        print("No valid rows to append.", file=sys.stderr)
        sys.exit(1)
    
    # Write (or dry run)
    if args.dry_run:
        print(f"DRY RUN: Would append {len(valid_rows)} row(s) to {filepath}")
        for row in valid_rows:
            print(f"  {row}")
    else:
        # Append to file
        filepath.parent.mkdir(parents=True, exist_ok=True)
        file_exists = filepath.exists()
        
        with open(filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=schema["columns"])
            if not file_exists:
                writer.writeheader()
            writer.writerows(valid_rows)
        
        print(f"Appended {len(valid_rows)} row(s) to {filepath}")


if __name__ == "__main__":
    main()
