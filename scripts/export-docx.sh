#!/bin/bash
# Export article.md to DOCX format for Google Docs
# Usage: ./scripts/export-docx.sh <topic-directory> [md-file-path]
#
# Example: ./scripts/export-docx.sh epistemic_debt
#          ./scripts/export-docx.sh epistemic_debt article.md

set -e

if ! command -v pandoc &>/dev/null; then
    echo "Error: pandoc not found. Run ./scripts/setup.sh first."
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: $0 <topic-directory> [md-file-path]"
    echo "Example: $0 epistemic_debt"
    exit 1
fi

TOPIC="$1"
MD_FILE="${2:-article.md}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TOPIC_DIR="$REPO_ROOT/topics/$TOPIC"

# If MD_FILE is an absolute path or starts with ./ or ../, use it directly
# Otherwise, assume it's relative to TOPIC_DIR
if [[ "$MD_FILE" == /* ]] || [[ "$MD_FILE" == .* ]]; then
    INPUT_PATH="$MD_FILE"
else
    INPUT_PATH="$TOPIC_DIR/$MD_FILE"
fi

# Validate topic directory exists
if [ ! -d "$TOPIC_DIR" ]; then
    echo "Error: Topic directory '$TOPIC_DIR' does not exist"
    exit 1
fi

# Validate input markdown file exists
if [ ! -f "$INPUT_PATH" ]; then
    echo "Error: No markdown file found at '$INPUT_PATH'"
    exit 1
fi

# Create exports directory if it doesn't exist
mkdir -p "$TOPIC_DIR/exports"

# Generate timestamp for filename
TIMESTAMP=$(date +%Y%m%d)

# Get base filename without extension for the output
BASENAME=$(basename "$INPUT_PATH" .md)

# Export to DOCX
OUTPUT_FILE="$TOPIC_DIR/exports/$BASENAME-$TIMESTAMP.docx"

echo "Exporting $INPUT_PATH to DOCX..."
pandoc "$INPUT_PATH" \
    -o "$OUTPUT_FILE" \
    --from=markdown \
    --to=docx \
    --standalone

echo "Created: $OUTPUT_FILE"

# Also create a latest version without timestamp
cp "$OUTPUT_FILE" "$TOPIC_DIR/exports/$BASENAME.docx"
echo "Updated: $TOPIC_DIR/exports/$BASENAME.docx"
