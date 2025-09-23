# Solar Irradiance Analysis - Professional Edition

A comprehensive Python toolkit for analyzing **NASA POWER satellite-derived solar irradiance data**
with professional statistical methods and visualization capabilities. This project provides
scientific-grade analysis tools for solar resource assessment, climate research, and renewable
energy applications.

Originally developed from Google Colab research code, now restructured as a professional, modular
Python package with advanced features including multi-language support, document export, and
comparative analysis capabilities.

## 🏗️ Project Structure

```text
Solar Irradiance Analysis/
├── main.py                      # 🚀 Main interactive application
├── README.md                    # 📖 This documentation
├── requirements.txt             # 📦 Python dependencies
├── backup/                      # 🗄️ Original code backup
│   └── original_colab_code.py   # Original Google Colab code
│
├── src/                         # 📁 Source code modules
│   ├── __init__.py
│   ├── core/                    # ⚙️ Core configuration
│   │   ├── __init__.py
│   │   └── config.py           # Configuration settings
│   ├── data/                    # 📊 Data management
│   │   ├── __init__.py
│   │   └── data_sets.py        # Dataset definitions and utilities
│   ├── analysis/                # 🔬 Statistical analysis
│   │   ├── __init__.py
│   │   └── analysis_functions.py # Analysis algorithms
│   ├── visualization/           # 📈 Data visualization
│   │   ├── __init__.py
│   │   └── plotting_functions.py # Interactive plotting
│   ├── export/                  # 📄 Document generation
│   │   ├── __init__.py
│   │   └── document_exporter.py # DOCX/PDF export system
│   └── utils/                   # 🛠️ Utilities
│       ├── __init__.py
│       └── i18n.py             # Internationalization system
│
├── docs/                        # 📚 Documentation
├── tests/                       # 🧪 Test files
├── reports/                     # 📋 Generated reports
├── .venv/                       # 🐍 Virtual environment
└── __pycache__/                # 🗂️ Python cache
```

## 🚀 Quick Start

### 1. Environment Setup

```powershell
# Activate virtual environment
.\.venv\Scripts\activate

# Install dependencies (if needed)
pip install -r requirements.txt

# Set execution policy (PowerShell)
Set-ExecutionPolicy Unrestricted -Scope Process
```

### 2. Run Interactive Application

```powershell
python main.py
```

This launches an interactive menu with options:

- 🖥️ **Console Analysis**: Complete analysis with interactive plots
- 📄 **Individual Export**: Export specific dataset to documents
- 📚 **Comprehensive Export**: All datasets in one document
- 🔄 **Console + Export**: Analysis + automatic document generation
- ⚙️ **Configuration**: Language and display settings

## 📊 Analysis Features

### 1. Statistical Analysis

- Basic statistics (mean, std, min, max)
- Linear trend analysis
- Anomaly detection
- Seasonal analysis
- Interannual variability

### 2. Visualizations

- Monthly time series
- Annual mean evolution
- Monthly climatology
- Relative anomalies
- Decade analysis
- **Comparative analysis** between datasets

### 3. Professional Features

- 🌍 **Multi-language support** (English/Spanish)
- 📊 **Dynamic scaling** for all datasets
- 🎨 **Professional formatting** with proper titles
- 📈 **High-quality plots** (300 DPI)
- 📄 **Document export** to DOCX and PDF
- 🔧 **Interactive menu system**

## 🛰️ Data Source: NASA POWER

### About NASA POWER

This project analyzes solar irradiance data from **NASA's POWER (Prediction of Worldwide Energy
Resources)** project, accessed through the
[NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/).

### Why NASA POWER?

- **🌍 Global Coverage**: Satellite-based data covering the entire Earth
- **📊 High Quality**: NASA's rigorous data validation and processing
- **🕰️ Long-term Records**: Historical data spanning multiple decades
- **🔬 Scientific Standards**: Peer-reviewed methodologies and algorithms
- **🆓 Open Access**: Free, publicly available data for research and analysis

### Data Characteristics

- **Parameter**: Solar Irradiance (kWh/m²/day)
- **Temporal Resolution**: Monthly averages
- **Spatial Resolution**: 0.5° x 0.625° (approximately 50km x 50km)
- **Coverage Period**: Multi-decade historical records
- **Source**: MERRA-2 reanalysis and satellite observations
- **Quality**: Validated against ground-based measurements worldwide

### Scientific Context

Solar irradiance analysis is crucial for:

- **☀️ Solar Energy Planning**: Site assessment and energy potential
- **🌱 Climate Research**: Understanding long-term climate patterns
- **📈 Trend Analysis**: Detecting changes in solar resource availability
- **⚡ Renewable Energy**: Supporting sustainable energy transitions
- **🌍 Environmental Studies**: Climate change impact assessment

## 📁 Data Structure

The project handles multiple datasets with data organized as:

- **Keys**: Years (dynamically calculated from datasets)
- **Values**: Monthly arrays with 12 irradiance values
- **Metadata**: Location information and descriptions
- **Source**: NASA POWER satellite-derived data

## 🌍 Internationalization (i18n)

### Language Configuration

Configure languages independently in `src/core/config.py`:

```python
LANGUAGE_CONFIG = {
    'print_language': 'en',  # Console output: 'en' or 'es'
    'plot_language': 'en'    # Plot labels: 'en' or 'es'
}
```

### Available Combinations

1. **English (both)**: `print: 'en', plot: 'en'`
2. **Spanish (both)**: `print: 'es', plot: 'es'`
3. **Mixed EN/ES**: `print: 'en', plot: 'es'`
4. **Mixed ES/EN**: `print: 'es', plot: 'en'`

## 📄 Document Export

### Automatic Export Features

- **Professional formatting** with tables and statistics
- **Complete analysis information** (matching console output)
- **High-quality plots** automatically generated and embedded
- **Comparative summary plot** for multiple datasets
- **Multilingual support** (follows i18n configuration)
- **Automatic timestamping** for file organization
- **Organized directory structure**

### Export Options

#### Interactive Menu (Recommended)

```powershell
python main.py
# Select option 2, 3, or 4 from the menu
```

#### Alternative: Direct Module Usage

```powershell
# For advanced users - direct module usage
python -c "
from src.export.document_exporter import create_reports
from src.data.data_sets import dataset_1, DATASET_METADATA
from src.analysis.analysis_functions import analyze_dataset
# ... custom analysis code
"
```

## 🔧 Configuration

### Display Settings

- **Plot styles**: Professional formatting with dynamic scales
- **Figure sizes**: Optimized for both screen and document display
- **Colors**: Consistent color schemes across all visualizations
- **Titles**: Multi-line formatting with proper spacing

### Analysis Parameters

- **Dynamic periods**: Automatically calculated from data
- **Trend analysis**: Linear regression with confidence intervals
- **Anomaly detection**: Based on climatological means
- **Seasonal analysis**: Monthly climatology with statistics

## 📦 Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical calculations
- **matplotlib**: Interactive and exportable visualizations
- **python-docx**: Professional DOCX document generation
- **reportlab**: Advanced PDF document creation

## 🎯 Key Improvements

### From Original Version

- ✅ **Organized structure** with proper Python packages
- ✅ **Interactive menu system** instead of multiple scripts
- ✅ **Professional document export** with embedded plots
- ✅ **Multi-language support** with independent configuration
- ✅ **Dynamic scaling** that works with all datasets
- ✅ **Complete information preservation** from console to documents
- ✅ **Comparative analysis** visualization
- ✅ **Error-free execution** with proper dependency management

### Technical Enhancements

- 🔧 **Modular architecture** for maintainability
- 🎨 **Professional plot formatting** with proper titles
- 📊 **Dynamic period calculation** (no hardcoded dates)
- 🌍 **Centralized internationalization** system
- 📄 **Advanced document generation** with images and tables
- ⚡ **Reliable data processing** with pandas
- 🔧 **Stable and mature** data processing ecosystem

## 🧪 Development Tools & Quality Assurance

### Code Quality Tools

This project includes comprehensive code quality and formatting tools:

#### 🎨 **Code Formatting**

- **Black**: Python code formatter (equivalent to Prettier for Python)
- **isort**: Import statement organizer
- **Prettier**: Markdown, JSON, and YAML formatter

#### 🔍 **Linting & Analysis**

- **Flake8**: Python linting (equivalent to ESLint for Python)
- **MyPy**: Static type checking
- **Bandit**: Security vulnerability scanner

#### 🔗 **Pre-commit Hooks**

Automated quality checks before each commit:

- Code formatting validation
- Import organization
- Linting checks
- Type checking
- Security scanning

### Development Setup

```powershell
# Windows setup
.\scripts\setup-dev.ps1

# Linux/macOS setup
./scripts/setup-dev.sh

# Manual setup
pip install -r requirements-dev.txt
pre-commit install
```

### Available Commands

```powershell
# Development workflow
make setup-dev          # Complete development environment setup
make format              # Format all code automatically
make lint                # Run all linting checks
make test                # Run tests with coverage
make clean               # Clean cache and build files
make run                 # Run the main application

# Individual tools
black src/ main.py       # Format Python code
isort src/ main.py       # Sort imports
flake8 src/ main.py      # Lint Python code
mypy src/ main.py        # Type checking

# Documentation formatting
npm run format           # Format all Markdown, JSON, YAML files
npm run format:check     # Check formatting without changing files
prettier --write "**/*.md" "**/*.json"  # Direct prettier usage
```

### Configuration Files

- **`pyproject.toml`**: Centralized Python tool configuration
- **`.flake8`**: Linting rules and exclusions
- **`.prettierrc`**: Formatting rules for documentation
- **`.pre-commit-config.yaml`**: Automated quality checks
- **`requirements-dev.txt`**: Development dependencies
- **`package.json`**: Node.js dependencies and npm scripts
- **`.gitignore`**: Files and directories to ignore in version control

## 🧪 Testing

```powershell
# Test individual components
python -c "from src.data.data_sets import dataset_1; print('✅ Data import OK')"
python -c "from src.utils.i18n import i18n; print('✅ i18n system OK')"

# Run full test suite
make test                # With coverage report
pytest tests/ -v         # Verbose output
```

## 📚 Scientific Methodology

### Statistical Analysis Methods

- **📊 Descriptive Statistics**: Mean, standard deviation, min/max analysis
- **📈 Trend Analysis**: Linear regression with least squares fitting
- **🌡️ Anomaly Detection**: Deviation from climatological means
- **📅 Seasonal Analysis**: Monthly climatology and variability
- **📊 Comparative Analysis**: Multi-dataset statistical comparison

### Visualization Techniques

- **📊 Time Series Analysis**: Temporal evolution visualization
- **📈 Trend Visualization**: Linear trend representation with confidence intervals
- **🌡️ Anomaly Mapping**: Relative deviation from normal patterns
- **📅 Climatological Patterns**: Monthly and seasonal cycle analysis
- **📊 Multi-Dataset Comparison**: Comparative statistical visualization

### Quality Assurance

- **✅ Data Validation**: Automated checks for data integrity
- **📊 Statistical Consistency**: Cross-validation with climatological norms
- **🔍 Outlier Detection**: Identification and handling of extreme values
- **📈 Trend Significance**: Statistical evaluation of temporal changes

## 📖 References & Citations

### Primary Data Source

- **NASA POWER Project**: NASA Prediction of Worldwide Energy Resources (POWER). "Data Access Viewer
  (DAV)." NASA Langley Research Center. Available at:
  <https://power.larc.nasa.gov/data-access-viewer/>
- **NASA POWER Methodology**: NASA POWER Data Services Documentation. "Data Sources and
  Methodology." Available at: <https://power.larc.nasa.gov/docs/methodology/data/sources/>
- **NASA POWER Services**: NASA POWER. "Data Services and APIs." Available at:
  <https://power.larc.nasa.gov/docs/services/>

### Data Sources and Technical Background

- **CERES Project**: NASA Clouds and the Earth's Radiant Energy System (CERES) - provides solar
  irradiance and cloud property data
- **MERRA-2 Reanalysis**: NASA Global Modeling and Assimilation Office (GMAO) Modern-Era
  Retrospective analysis for Research and Applications, Version 2
- **Surface Radiation Budget (SRB)**: NASA project providing surface radiation flux estimates

### Scientific Applications

- **Solar Resource Assessment**: NASA POWER data is widely used for renewable energy planning and
  solar resource evaluation
- **Climate Research**: Long-term solar irradiance analysis for climate change studies and trend
  detection
- **Agricultural Applications**: Solar radiation data for crop modeling and agricultural
  decision-making

### How to Cite NASA POWER Data

When using NASA POWER data in publications or projects, use the following citation format:

```text
NASA POWER Project. Prediction Of Worldwide Energy Resources (POWER) Data Access Viewer.
NASA Langley Research Center. Available at: https://power.larc.nasa.gov/data-access-viewer/
```

### Additional Resources

- **NASA Earthdata POWER Overview**: <https://www.earthdata.nasa.gov/data/tools/power-dav>
- **POWER User Guides and Tutorials**: <https://power.larc.nasa.gov/docs/tutorials/>
- **POWER FAQ**: <https://power.larc.nasa.gov/docs/faqs/data/>

## 🤝 Contributing

1. Follow the established package structure
2. Update imports when moving files
3. Maintain i18n compatibility
4. Test with multiple datasets
5. Ensure document export functionality
6. **Cite data sources appropriately** when using NASA POWER data
7. **Follow scientific best practices** for data analysis and visualization

## 📈 Future Enhancements

### 📊 **Advanced Statistical Analysis**

- [ ] **Statistical Tests**:
  - [ ] Normality tests (Shapiro-Wilk, Kolmogorov-Smirnov)
  - [ ] Trend tests (Mann-Kendall, Sen's slope)
  - [ ] Cross-correlation analysis between datasets
  - [ ] Statistical significance testing
  - [ ] Temporal autocorrelation analysis
- [ ] **Advanced Metrics**:
  - [ ] Extreme value analysis (GEV, GPD)
  - [ ] Return period calculations
  - [ ] Drought/excess indices
  - [ ] Climate change detection indices

### 🌐 **Interactive Web Dashboard**

- [ ] **Web Interface**:
  - [ ] Flask/Django/Streamlit implementation
  - [ ] Interactive plots with Plotly/Bokeh
  - [ ] Real-time data visualization
  - [ ] Responsive design for mobile/desktop
- [ ] **User Features**:
  - [ ] Dynamic dataset selection
  - [ ] Interactive temporal filters
  - [ ] Custom analysis parameters
  - [ ] Export options from web interface

### 🗄️ **Database Integration**

- [ ] **Database Support**:
  - [ ] PostgreSQL/MySQL connectivity
  - [ ] Dataset storage and versioning
  - [ ] Analysis history tracking
  - [ ] Metadata management
- [ ] **Data Management**:
  - [ ] Automated data ingestion
  - [ ] Data quality checks
  - [ ] Backup and recovery systems
  - [ ] Optimized SQL queries

### 🔌 **API Endpoints**

- [ ] **REST API**:
  - [ ] FastAPI/Flask implementation
  - [ ] Automated analysis endpoints
  - [ ] Authentication and authorization
  - [ ] Rate limiting and caching
- [ ] **Documentation**:
  - [ ] Automatic API documentation (Swagger)
  - [ ] Client libraries (Python, R, JavaScript)
  - [ ] Usage examples and tutorials

### 🤖 **Machine Learning & Predictions**

- [ ] **Predictive Models**:
  - [ ] Solar irradiance forecasting (ARIMA, LSTM)
  - [ ] Trend prediction algorithms
  - [ ] Seasonal decomposition with ML
  - [ ] Anomaly detection with unsupervised learning
- [ ] **Advanced Analytics**:
  - [ ] Pattern recognition in temporal data
  - [ ] Classification of climate patterns
  - [ ] Principal Component Analysis (PCA)
  - [ ] Clustering analysis for similar periods

### 📊 **Enhanced Comparative Analysis**

- [ ] **Advanced Comparisons**:
  - [ ] Multi-dimensional cluster analysis
  - [ ] Temporal heatmaps and correlation matrices
  - [ ] Cross-spectral analysis (FFT)
  - [ ] Wavelet analysis for frequency decomposition
- [ ] **Visualization Improvements**:
  - [ ] 3D surface plots for temporal-spatial data
  - [ ] Interactive correlation networks
  - [ ] Animated time series evolution
  - [ ] Geographic mapping integration

### 🧪 **Testing & Quality Assurance**

- [ ] **Test Coverage**:
  - [ ] Unit tests for all modules
  - [ ] Integration tests for workflows
  - [ ] Performance benchmarking
  - [ ] Data validation tests
- [ ] **Code Quality**:
  - [ ] Automated code formatting (Black, isort)
  - [ ] Linting with pylint/flake8
  - [ ] Type hints with mypy
  - [ ] Documentation generation (Sphinx)

### 🔧 **Performance & Scalability**

- [ ] **High-Performance Backend**
- [ ] **Advanced Optimization**:
  - [ ] Parallel processing for large datasets
  - [ ] Advanced caching mechanisms
  - [ ] Streaming data processing
  - [ ] GPU acceleration with cuPolars
- [ ] **Deployment**:
  - [ ] Docker containerization
  - [ ] Cloud deployment (AWS, GCP, Azure)
  - [ ] CI/CD pipelines
  - [ ] Monitoring and logging systems

### 📚 **Documentation & Tutorials**

- [ ] **Enhanced Documentation**:
  - [ ] Scientific methodology documentation
  - [ ] API reference documentation
  - [ ] User guides and tutorials
  - [ ] Video tutorials and demos
- [ ] **Educational Content**:
  - [ ] Jupyter notebook examples
  - [ ] Case studies with real data
  - [ ] Best practices guide
  - [ ] Troubleshooting documentation

---

**Version**: 1.0.0  
**Architecture**: Modular Python Package  
**Compatibility**: Windows/Linux/macOS  
**Python**: 3.8+
