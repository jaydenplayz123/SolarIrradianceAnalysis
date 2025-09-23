# PowerShell script for Windows development setup
# Usage: .\scripts\setup-dev.ps1

Write-Host "🔧 Setting up Solar Irradiance Analysis development environment..." -ForegroundColor Green

# Check if Python is available
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Check Python version
$pythonVersion = python --version 2>&1
Write-Host "🐍 Found: $pythonVersion" -ForegroundColor Blue

# Create virtual environment if it doesn't exist
if (!(Test-Path ".venv")) {
    Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}

# Activate virtual environment
Write-Host "⚡ Activating virtual environment..." -ForegroundColor Yellow
& .\.venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "⬆️ Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install development dependencies
Write-Host "📚 Installing development dependencies..." -ForegroundColor Yellow
pip install -r requirements-dev.txt

# Install pre-commit hooks
Write-Host "🔗 Installing pre-commit hooks..." -ForegroundColor Yellow
pre-commit install

# Run initial checks
Write-Host "🔍 Running initial code checks..." -ForegroundColor Yellow
Write-Host "  - Formatting with black..." -ForegroundColor Gray
black --check src/ main.py

Write-Host "  - Import sorting with isort..." -ForegroundColor Gray
isort --check-only src/ main.py

Write-Host "  - Linting with flake8..." -ForegroundColor Gray
flake8 src/ main.py

Write-Host "✅ Development environment setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 Available commands:" -ForegroundColor Blue
Write-Host "  - make format    # Format code"
Write-Host "  - make lint      # Run linting"
Write-Host "  - make test      # Run tests"
Write-Host "  - make run       # Run application"
Write-Host "  - make clean     # Clean cache files"
Write-Host ""
Write-Host "🚀 Ready to develop! Run 'python main.py' to start the application." -ForegroundColor Green
