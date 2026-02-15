#!/bin/bash
# Export to PDF format
# Usage: ./scripts/export-pdf.sh <topic-directory> [article|slides|both|<md-file-path>]
#
# Example: ./scripts/export-pdf.sh epistemic_debt article
#          ./scripts/export-pdf.sh epistemic_debt slides
#          ./scripts/export-pdf.sh epistemic_debt both
#          ./scripts/export-pdf.sh epistemic_debt custom.md

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <topic-directory> [article|slides|both|<md-file-path>]"
    echo "Example: $0 epistemic_debt article"
    exit 1
fi

TOPIC="$1"
MODE="${2:-both}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TOPIC_DIR="$REPO_ROOT/topics/$TOPIC"

# Validate topic directory exists
if [ ! -d "$TOPIC_DIR" ]; then
    echo "Error: Topic directory '$TOPIC_DIR' does not exist"
    exit 1
fi

# Create exports directory if it doesn't exist
mkdir -p "$TOPIC_DIR/exports"

# Generate timestamp for filename
TIMESTAMP=$(date +%Y%m%d)

export_generic_pdf() {
    local input_path="$1"
    local output_name="$2"
    local engine="${3:-pdflatex}"
    
    if [ ! -f "$input_path" ]; then
        echo "Warning: No file found at '$input_path', skipping PDF export"
        return 1
    fi
    
    OUTPUT_FILE="$TOPIC_DIR/exports/$output_name-$TIMESTAMP.pdf"
    
    echo "Exporting $input_path to PDF..."
    if [[ "$output_name" == "slides" ]] || [[ "$(basename "$input_path")" == "slides.md" ]]; then
        marp "$input_path" \
            -o "$OUTPUT_FILE" \
            --allow-local-files \
            --pdf
    else
        pandoc "$input_path" \
            -o "$OUTPUT_FILE" \
            --from=markdown \
            --to=pdf \
            --pdf-engine="$engine" \
            --standalone
    fi
    
    echo "Created: $OUTPUT_FILE"
    
    # Also create a latest version without timestamp
    cp "$OUTPUT_FILE" "$TOPIC_DIR/exports/$output_name.pdf"
    echo "Updated: $TOPIC_DIR/exports/$output_name.pdf"
}

case "$MODE" in
    article)
        export_generic_pdf "$TOPIC_DIR/article.md" "article"
        ;;
    slides)
        export_generic_pdf "$TOPIC_DIR/slides.md" "slides"
        ;;
    both)
        export_generic_pdf "$TOPIC_DIR/article.md" "article" || true
        export_generic_pdf "$TOPIC_DIR/slides.md" "slides" || true
        ;;
    *)
        # Check if MODE is a file path
        if [[ "$MODE" == /* ]] || [[ "$MODE" == .* ]]; then
            INPUT_PATH="$MODE"
        else
            INPUT_PATH="$TOPIC_DIR/$MODE"
        fi
        
        if [ -f "$INPUT_PATH" ]; then
            BASENAME=$(basename "$INPUT_PATH" .md)
            export_generic_pdf "$INPUT_PATH" "$BASENAME"
        else
            echo "Error: Invalid mode or file path '$MODE'. Use 'article', 'slides', 'both', or a valid .md file path"
            exit 1
        fi
        ;;
esac

echo "Done!"
