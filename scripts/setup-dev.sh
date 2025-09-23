#!/bin/bash
# Bash script for Linux/macOS development setup
# Usage: ./scripts/setup-dev.sh

set -e

echo "🔧 Setting up Solar Irradiance Analysis development environment..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1)
echo "🐍 Found: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
python -m pip install --upgrade pip

# Install development dependencies
echo "📚 Installing development dependencies..."
pip install -r requirements-dev.txt

# Install pre-commit hooks
echo "🔗 Installing pre-commit hooks..."
pre-commit install

# Run initial checks
echo "🔍 Running initial code checks..."
echo "  - Formatting with black..."
black --check src/ main.py || echo "  ⚠️ Code needs formatting (run 'make format')"

echo "  - Import sorting with isort..."
isort --check-only src/ main.py || echo "  ⚠️ Imports need sorting (run 'make format')"

echo "  - Linting with flake8..."
flake8 src/ main.py || echo "  ⚠️ Linting issues found (run 'make lint' for details)"

echo "✅ Development environment setup complete!"
echo ""
echo "📝 Available commands:"
echo "  - make format    # Format code"
echo "  - make lint      # Run linting"
echo "  - make test      # Run tests"
echo "  - make run       # Run application"
echo "  - make clean     # Clean cache files"
echo ""
echo "🚀 Ready to develop! Run 'python main.py' to start the application."
