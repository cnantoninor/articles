#!/bin/bash
# Installation script for AI Articles Repository tools
# This script installs the necessary tools for exporting articles and slides.

set -e

echo "=========================================="
echo "Installing AI Articles Repository Tools"
echo "=========================================="

# Detect OS
OS="$(uname -s)"
echo "Detected OS: $OS"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 1. Install Pandoc (for DOCX and PDF export)
if command_exists pandoc; then
    echo "✓ Pandoc is already installed: $(pandoc --version | head -n 1)"
else
    echo "Installing Pandoc..."
    if [[ "$OS" == "Linux" ]]; then
        if command_exists apt-get; then
            sudo apt-get update && sudo apt-get install -y pandoc
        elif command_exists dnf; then
            sudo dnf install -y pandoc
        elif command_exists pacman; then
            sudo pacman -S --noconfirm pandoc
        else
            echo "Error: Could not find a supported package manager (apt, dnf, pacman). Please install pandoc manually."
            exit 1
        fi
    elif [[ "$OS" == "Darwin" ]]; then
        if command_exists brew; then
            brew install pandoc
        else
            echo "Error: Homebrew not found. Please install pandoc manually or install Homebrew."
            exit 1
        fi
    fi
fi

# 2. Install Node.js and npm (required for Marp)
if command_exists npm; then
    echo "✓ npm is already installed: $(npm -v)"
else
    echo "Installing Node.js and npm..."
    if [[ "$OS" == "Linux" ]]; then
        if command_exists apt-get; then
            sudo apt-get update && sudo apt-get install -y nodejs npm
        elif command_exists dnf; then
            sudo dnf install -y nodejs npm
        elif command_exists pacman; then
            sudo pacman -S --noconfirm nodejs npm
        else
            echo "Error: Could not find a supported package manager (apt, dnf, pacman). Please install Node.js and npm manually."
            exit 1
        fi
    elif [[ "$OS" == "Darwin" ]]; then
        if command_exists brew; then
            brew install node
        fi
    fi
fi

# 3. Install Marp CLI (for PPTX and Slide PDF export)
if command_exists marp; then
    echo "✓ Marp CLI is already installed: $(marp --version | head -n 1)"
else
    echo "Installing Marp CLI..."
    # Try to install globally, but fall back to local if permission denied
    if ! npm install --global @marp-team/marp-cli; then
        echo "Global installation failed, trying local installation..."
        npm install @marp-team/marp-cli
        echo "Marp CLI installed locally. Adding to PATH for this session."
        export PATH="$PATH:$(pwd)/node_modules/.bin"
    fi
fi

# 4. Install LaTeX (for PDF export via Pandoc)
if command_exists pdflatex; then
    echo "✓ LaTeX (pdflatex) is already installed."
else
    echo "Installing LaTeX (minimal distribution)..."
    if [[ "$OS" == "Linux" ]]; then
        if command_exists apt-get; then
            sudo apt-get update && sudo apt-get install -y texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
        elif command_exists dnf; then
            sudo dnf install -y texlive-scheme-basic
        elif command_exists pacman; then
            sudo pacman -S --noconfirm texlive-bin texlive-core
        else
            echo "Error: Could not find a supported package manager (apt, dnf, pacman). Please install LaTeX manually."
            exit 1
        fi
    elif [[ "$OS" == "Darwin" ]]; then
        if command_exists brew; then
            brew install --cask mactex-no-gui
        fi
    fi
fi

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo "Note: If 'marp' command is still not found, you may need to restart your terminal"
echo "or add the npm global bin directory to your PATH."
echo ""
echo "Try running: marp --version"
