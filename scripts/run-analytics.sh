#!/bin/bash
# Convenience script to run the full analytics pipeline.
#
# Usage:
#   ./scripts/run-analytics.sh [--skip-fetch] [--skip-merge] [--date YYYY-MM-DD]
#
# Options:
#   --skip-fetch    Skip GA4 data fetch (use existing data)
#   --skip-merge    Skip merge step (use existing snapshot)
#   --date          Report date (default: today)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ANALYTICS_DIR="$REPO_ROOT/analytics"
SCRIPTS_DIR="$ANALYTICS_DIR/scripts"

SKIP_FETCH=false
SKIP_MERGE=false
REPORT_DATE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --skip-fetch)
            SKIP_FETCH=true
            shift
            ;;
        --skip-merge)
            SKIP_MERGE=true
            shift
            ;;
        --date)
            REPORT_DATE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            echo "Usage: $0 [--skip-fetch] [--skip-merge] [--date YYYY-MM-DD]"
            exit 1
            ;;
    esac
done

echo "=== Analytics Pipeline ==="
echo ""

# Step 1: Fetch GA4 data
if [ "$SKIP_FETCH" = false ]; then
    echo "Step 1: Fetching GA4 data..."
    python3 "$SCRIPTS_DIR/fetch_ga4.py" || {
        echo "Warning: GA4 fetch failed. Continuing with existing data..."
    }
    echo ""
else
    echo "Step 1: Skipping GA4 fetch (--skip-fetch)"
    echo ""
fi

# Step 2: Merge data
if [ "$SKIP_MERGE" = false ]; then
    echo "Step 2: Merging GA4 + manual data..."
    python3 "$SCRIPTS_DIR/merge.py" || {
        echo "Error: Merge failed. Check your data files."
        exit 1
    }
    echo ""
else
    echo "Step 2: Skipping merge (--skip-merge)"
    echo ""
fi

# Step 3: Generate report
echo "Step 3: Generating report..."
if [ -n "$REPORT_DATE" ]; then
    python3 "$SCRIPTS_DIR/report.py" --date "$REPORT_DATE"
else
    python3 "$SCRIPTS_DIR/report.py"
fi

echo ""
echo "=== Done ==="
echo ""
echo "Next steps:"
echo "  1. Review the report in analytics/reports/"
echo "  2. Collect manual data if needed (see analytics/COLLECTION-CHECKLIST.md)"
echo "  3. Run ingest.py to add manual data, then re-run this script"
