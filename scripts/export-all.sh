#!/bin/bash
# Export all formats for a topic (DOCX, PPTX, PDF)
# Usage: ./scripts/export-all.sh <topic-directory> [md-file-path]
#
# Example: ./scripts/export-all.sh epistemic_debt
#          ./scripts/export-all.sh epistemic_debt custom.md

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <topic-directory> [md-file-path]"
    echo "Example: $0 epistemic_debt"
    exit 1
fi

TOPIC="$1"
MD_FILE="$2"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TOPIC_DIR="$REPO_ROOT/$TOPIC"

# Validate topic directory exists
if [ ! -d "$TOPIC_DIR" ]; then
    echo "Error: Topic directory '$TOPIC_DIR' does not exist"
    exit 1
fi

# Create exports directory if it doesn't exist
mkdir -p "$TOPIC_DIR/exports"

echo "=========================================="
echo "Exporting formats for: $TOPIC"
[ -n "$MD_FILE" ] && echo "Target file: $MD_FILE"
echo "=========================================="
echo ""

# Track if we exported anything
EXPORTED=0

if [ -n "$MD_FILE" ]; then
    # If a specific file is provided, try to export it in all relevant formats
    # Check if it's a slide or an article
    if [[ "$MD_FILE" == *"slides"* ]]; then
        echo "--- PPTX Export ---"
        "$SCRIPT_DIR/export-slides.sh" "$TOPIC" "$MD_FILE"
        EXPORTED=1
        echo ""
    else
        echo "--- DOCX Export ---"
        "$SCRIPT_DIR/export-docx.sh" "$TOPIC" "$MD_FILE"
        EXPORTED=1
        echo ""
    fi
    
    echo "--- PDF Export ---"
    "$SCRIPT_DIR/export-pdf.sh" "$TOPIC" "$MD_FILE"
    EXPORTED=1
    echo ""
else
    # Default behavior: export article.md and slides.md if they exist
    # Export DOCX (if article.md exists)
    if [ -f "$TOPIC_DIR/article.md" ]; then
        echo "--- DOCX Export ---"
        "$SCRIPT_DIR/export-docx.sh" "$TOPIC"
        EXPORTED=1
        echo ""
    fi

    # Export PPTX (if slides.md exists)
    if [ -f "$TOPIC_DIR/slides.md" ]; then
        echo "--- PPTX Export ---"
        "$SCRIPT_DIR/export-slides.sh" "$TOPIC"
        EXPORTED=1
        echo ""
    fi

    # Export PDFs
    echo "--- PDF Export ---"
    "$SCRIPT_DIR/export-pdf.sh" "$TOPIC" both
    EXPORTED=1
    echo ""
fi

if [ $EXPORTED -eq 0 ]; then
    echo "Warning: No article.md or slides.md found in '$TOPIC_DIR'"
    exit 1
fi

echo "=========================================="
echo "All exports complete!"
echo "Output directory: $TOPIC_DIR/exports/"
echo "=========================================="
