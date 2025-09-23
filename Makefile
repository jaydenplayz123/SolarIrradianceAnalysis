# Makefile for Solar Irradiance Analysis Project
# Usage: make <target>

.PHONY: help install install-dev format lint test clean setup-dev run

# Default target
help:
	@echo "Solar Irradiance Analysis - Available Commands:"
	@echo ""
	@echo "  setup-dev     - Set up development environment"
	@echo "  install       - Install production dependencies"
	@echo "  install-dev   - Install development dependencies"
	@echo "  format        - Format code with black and isort"
	@echo "  lint          - Run linting checks (flake8, mypy)"
	@echo "  test          - Run tests with pytest"
	@echo "  clean         - Clean cache and build files"
	@echo "  run           - Run the main application"
	@echo "  pre-commit    - Install pre-commit hooks"
	@echo ""

# Development setup
setup-dev:
	@echo "🔧 Setting up development environment..."
	pip install -r requirements-dev.txt
	pre-commit install
	@echo "✅ Development environment ready!"

# Install dependencies
install:
	@echo "📦 Installing production dependencies..."
	pip install -r requirements.txt

install-dev:
	@echo "📦 Installing development dependencies..."
	pip install -r requirements-dev.txt

# Code formatting
format:
	@echo "🎨 Formatting code..."
	black src/ main.py
	isort src/ main.py
	@echo "✅ Code formatted!"

# Linting
lint:
	@echo "🔍 Running linting checks..."
	flake8 src/ main.py
	mypy src/ main.py
	@echo "✅ Linting complete!"

# Testing
test:
	@echo "🧪 Running tests..."
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term
	@echo "✅ Tests complete!"

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .coverage htmlcov/ .pytest_cache/ .mypy_cache/
	@echo "✅ Cleanup complete!"

# Run application
run:
	@echo "🚀 Running Solar Irradiance Analysis..."
	python main.py

# Pre-commit
pre-commit:
	@echo "🔗 Installing pre-commit hooks..."
	pre-commit install
	@echo "✅ Pre-commit hooks installed!"

# Development workflow
dev-check: format lint
	@echo "✅ Development checks complete!"
