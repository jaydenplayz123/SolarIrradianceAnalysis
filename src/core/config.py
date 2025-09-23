"""
Configuration for solar irradiance analysis
Configuración para el análisis de irradiación solar
"""

# Language configuration
LANGUAGE_CONFIG = {
    "print_language": "en",  # Language for print statements: 'en' or 'es'
    "plot_language": "en",  # Language for plots: 'en' or 'es'
}

# Visualization configurations
PLOT_CONFIG = {
    "figure_size": (16, 12),
    "dpi": 300,
    "style": "default",
    "colors": {
        "trend": "red",
        "climatology": "green",
        "anomalies": "black",
        "rolling_mean": "blue",
    },
}

# Analysis configurations
ANALYSIS_CONFIG = {
    "rolling_window": 5,  # Window for rolling mean
    "trend_degree": 1,  # Polynomial degree for trend
    "y_limits": {
        "time_series": (3.0, 6.5),
        "annual_mean": (4.2, 5.2),
        "climatology": (4.0, 5.4),
        "anomalies": (-1.0, 1.0),
    },
}

# Data configurations
DATA_CONFIG = {
    "units": "kWh/m²/day",
    "decimal_places": 4,
    # Note: Period is now calculated dynamically from datasets using get_all_datasets_period()
}

# Export configurations
EXPORT_CONFIG = {"formats": ["png", "pdf"], "dpi": 300, "bbox_inches": "tight"}
