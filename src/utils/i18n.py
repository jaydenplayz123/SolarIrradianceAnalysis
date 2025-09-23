"""
Internationalization (i18n) system for Solar Irradiance Analysis
Sistema de internacionalización para Análisis de Irradiación Solar
"""

# Language configurations
LANGUAGES = {
    "en": {
        # General terms
        "analysis": "ANALYSIS",
        "period": "Period",
        "dimension": "Dimension",
        "years": "years",
        "months": "months",
        "global_range": "Global range",
        "analyzing": "ANALYZING",
        "end_analysis": "END ANALYSIS",
        "comparative_analysis": "COMPARATIVE ANALYSIS",
        "comparative_summary": "COMPARATIVE SUMMARY",
        "analysis_completed": "ANALYSIS COMPLETED",
        "solar_irradiance_analysis": "SOLAR IRRADIANCE ANALYSIS",
        "multiple_datasets": "MULTIPLE DATASETS",
        "period_caps": "PERIOD",
        "export": "EXPORT",
        "exported_successfully": "exported successfully!",
        "error_exporting_reports": "Error exporting reports",
        "creating_plots": "Creating plots",
        "saving_images": "Saving images",
        "months_lowercase": "months",
        "years_lowercase": "years",
        "year_lowercase": "year",
        "final_summary": "FINAL SUMMARY",
        "general_trend": "General trend",
        "seasonal_variability": "Seasonal variability",
        "interannual_stability": "Interannual stability",
        "variation": "variation",
        "positive": "positive",
        "negative": "negative",
        "comparison": "Comparison",
        "coefficient_variation": "Coefficient of Variation",
        "irradiance": "Irradiance",
        "years": "years",
        "combined": "Combined",
        "station": "Station",
        "dataset": "Dataset",
        # Statistics
        "detailed_statistics": "DETAILED STATISTICS",
        "global_statistics": "GLOBAL STATISTICS",
        "annual_statistics": "ANNUAL STATISTICS",
        "monthly_climatology": "MONTHLY CLIMATOLOGY",
        "anomaly_analysis": "ANOMALY ANALYSIS",
        "seasonality": "SEASONALITY",
        "interannual_variability": "INTERANNUAL VARIABILITY",
        "final_summary": "FINAL SUMMARY",
        # Statistical measures
        "global_mean": "Global mean",
        "standard_deviation": "Standard deviation",
        "total_range": "Total range",
        "average_annual_mean": "Average annual mean",
        "year_highest_irradiance": "Year with highest irradiance",
        "year_lowest_irradiance": "Year with lowest irradiance",
        "linear_trend": "Linear trend",
        "year_highest_positive_anomaly": "Year with highest positive anomaly",
        "year_highest_negative_anomaly": "Year with highest negative anomaly",
        "years_positive_anomaly": "Years with positive anomaly",
        "years_negative_anomaly": "Years with negative anomaly",
        "standard_deviation_anomalies": "Standard deviation of anomalies",
        "month_highest_irradiance": "Month with highest irradiance",
        "month_lowest_irradiance": "Month with lowest irradiance",
        "seasonal_amplitude": "Seasonal amplitude",
        "annual_coefficient_variation": "Annual coefficient of variation",
        "interannual_range": "Interannual range",
        "general_trend": "General trend",
        "seasonal_variability": "Seasonal variability",
        "interannual_stability": "Interannual stability",
        "variation": "variation",
        # Trend types
        "positive_caps": "POSITIVE",
        "negative_caps": "NEGATIVE",
        "stable": "STABLE",
        # Results summary
        "mean_irradiance": "Mean irradiance",
        "trend": "Trend",
        "variability": "Variability",
        # Plot titles and labels
        "monthly_time_series": "Monthly Time Series",
        "annual_mean_irradiance_evolution": "Annual Mean Irradiance Evolution by Decades",
        "dataset_comparison": "Dataset Comparison",
        "monthly_time_series_subplot": "a) Monthly Time Series",
        "annual_mean_subplot": "b) Annual Mean Irradiance (from monthly values)",
        "climatology_subplot": "c) Climatology: Mean Monthly Irradiance (kWh/m²/day)",
        "anomalies_subplot": "d) Monthly Anomalies Relative to Climatology",
        "annual_means_comparison": "a) Annual Means Comparison",
        "climatologies_comparison": "b) Climatologies Comparison",
        "trends_comparison": "c) Trends Comparison",
        "variability_comparison": "d) Interannual Variability Comparison",
        # Axis labels
        "year_caps": "Year",
        "month": "Month",
        "irradiance_kwh": "Irradiance (kWh/m²/day)",
        "mean_annual_irradiance": "Mean Annual Irradiance (kWh/m²/day)",
        "mean_irradiance_axis": "Mean Irradiance (kWh/m²/day)",
        "anomaly_kwh": "Anomaly (kWh/m²/day)",
        "annual_mean_irradiance": "Annual Mean Irradiance (kWh/m²/day)",
        "monthly_mean_irradiance": "Monthly Mean Irradiance (kWh/m²/day)",
        "trend_mwh": "Trend (mWh/m²/day/year)",
        "coefficient_variation_axis": "Coefficient of Variation (%)",
        # Legend labels
        "annual_mean": "Annual mean",
        "rolling_mean_5_years": "5-year rolling mean",
        "general_trend": "General trend",
        "trend_label": "Trend",
        # Table headers
        "month_header": "Month",
        "average_header": "Average",
        "maximum_header": "Maximum",
        "minimum_header": "Minimum",
        "std_header": "Std",
        # Units
        "kwh_per_m2_day": "kWh/m²/day",
        "kwh_per_m2_year": "kWh/m²/day/year",
        "mwh_per_m2_year": "mWh/m²/day/year",
        "percent": "%",
        # Month names
        "month_names": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    },
    "es": {
        # General terms
        "analysis": "ANÁLISIS",
        "period": "Período",
        "dimension": "Dimensión",
        "years": "años",
        "months": "meses",
        "global_range": "Rango global",
        "analyzing": "ANALIZANDO",
        "end_analysis": "FIN ANÁLISIS",
        "comparative_analysis": "ANÁLISIS COMPARATIVO",
        "comparative_summary": "RESUMEN COMPARATIVO",
        "analysis_completed": "ANÁLISIS COMPLETADO",
        "solar_irradiance_analysis": "ANÁLISIS DE IRRADIACIÓN SOLAR",
        "multiple_datasets": "MÚLTIPLES CONJUNTOS DE DATOS",
        "period_caps": "PERÍODO",
        "export": "EXPORTACIÓN",
        "exported_successfully": "exportado exitosamente!",
        "error_exporting_reports": "Error exportando reportes",
        "creating_plots": "Creando gráficos",
        "saving_images": "Guardando imágenes",
        "months_lowercase": "meses",
        "years_lowercase": "años",
        "year_lowercase": "año",
        "final_summary": "RESUMEN FINAL",
        "general_trend": "Tendencia general",
        "seasonal_variability": "Variabilidad estacional",
        "interannual_stability": "Estabilidad interanual",
        "variation": "variación",
        "positive": "positiva",
        "negative": "negativa",
        "comparison": "Comparación",
        "coefficient_variation": "Coeficiente de Variación",
        "irradiance": "Irradiancia",
        "years": "años",
        "combined": "Combinado",
        "station": "Estación",
        "dataset": "Conjunto de datos",
        # Statistics
        "detailed_statistics": "ESTADÍSTICAS DETALLADAS",
        "global_statistics": "ESTADÍSTICAS GLOBALES",
        "annual_statistics": "ESTADÍSTICAS ANUALES",
        "monthly_climatology": "CLIMATOLOGÍA MENSUAL",
        "anomaly_analysis": "ANÁLISIS DE ANOMALÍAS",
        "seasonality": "ESTACIONALIDAD",
        "interannual_variability": "VARIABILIDAD INTERANUAL",
        "final_summary": "RESUMEN FINAL",
        # Statistical measures
        "global_mean": "Media global",
        "standard_deviation": "Desviación estándar",
        "total_range": "Rango total",
        "average_annual_mean": "Media anual promedio",
        "year_highest_irradiance": "Año con mayor irradiancia",
        "year_lowest_irradiance": "Año con menor irradiancia",
        "linear_trend": "Tendencia lineal",
        "year_highest_positive_anomaly": "Año con mayor anomalía positiva",
        "year_highest_negative_anomaly": "Año con mayor anomalía negativa",
        "years_positive_anomaly": "Años con anomalía positiva",
        "years_negative_anomaly": "Años con anomalía negativa",
        "standard_deviation_anomalies": "Desviación estándar de anomalías",
        "month_highest_irradiance": "Mes más irradiante",
        "month_lowest_irradiance": "Mes menos irradiante",
        "seasonal_amplitude": "Amplitud estacional",
        "annual_coefficient_variation": "Coeficiente de variación anual",
        "interannual_range": "Rango interanual",
        "general_trend": "Tendencia general",
        "seasonal_variability": "Variabilidad estacional",
        "interannual_stability": "Estabilidad interanual",
        "variation": "de variación",
        # Trend types
        "positive_caps": "POSITIVA",
        "negative_caps": "NEGATIVA",
        "stable": "ESTABLE",
        # Results summary
        "mean_irradiance": "Irradiancia media",
        "trend": "Tendencia",
        "variability": "Variabilidad",
        # Plot titles and labels
        "monthly_time_series": "Series Temporales Mensuales",
        "annual_mean_irradiance_evolution": "Evolución de la Irradiancia Media Anual por Décadas",
        "dataset_comparison": "Comparación entre Conjuntos de Datos",
        "monthly_time_series_subplot": "a) Series Temporales Mensuales",
        "annual_mean_subplot": "b) Irradiancia Media Anual (de valores mensuales)",
        "climatology_subplot": "c) Climatología: Irradiancia Media Mensual (kWh/m²/día)",
        "anomalies_subplot": "d) Anomalías Mensuales Relativas a la Climatología",
        "annual_means_comparison": "a) Comparación de Medias Anuales",
        "climatologies_comparison": "b) Comparación de Climatologías",
        "trends_comparison": "c) Comparación de Tendencias",
        "variability_comparison": "d) Comparación de Variabilidad Interanual",
        # Axis labels
        "year_caps": "Año",
        "month": "Mes",
        "irradiance_kwh": "Irradiancia (kWh/m²/día)",
        "mean_annual_irradiance": "Irradiancia Media Anual (kWh/m²/día)",
        "mean_irradiance_axis": "Irradiancia Media (kWh/m²/día)",
        "anomaly_kwh": "Anomalía (kWh/m²/día)",
        "annual_mean_irradiance": "Irradiancia Media Anual (kWh/m²/día)",
        "monthly_mean_irradiance": "Irradiancia Media Mensual (kWh/m²/día)",
        "trend_mwh": "Tendencia (mWh/m²/día/año)",
        "coefficient_variation_axis": "Coeficiente de Variación (%)",
        # Legend labels
        "annual_mean": "Media anual",
        "rolling_mean_5_years": "Media móvil (5 años)",
        "general_trend": "Tendencia general",
        "trend_label": "Tendencia",
        # Table headers
        "month_header": "Mes",
        "average_header": "Promedio",
        "maximum_header": "Máximo",
        "minimum_header": "Mínimo",
        "std_header": "Std",
        # Units
        "kwh_per_m2_day": "kWh/m²/día",
        "kwh_per_m2_year": "kWh/m²/día/año",
        "mwh_per_m2_year": "mWh/m²/día/año",
        "percent": "%",
        # Month names
        "month_names": [
            "Ene",
            "Feb",
            "Mar",
            "Abr",
            "May",
            "Jun",
            "Jul",
            "Ago",
            "Sep",
            "Oct",
            "Nov",
            "Dic",
        ],
    },
}


class I18n:
    """
    Internationalization class for managing language settings
    """

    def __init__(self, print_lang="en", plot_lang="en"):
        """
        Initialize i18n with language settings

        Args:
            print_lang (str): Language for print statements ('en' or 'es')
            plot_lang (str): Language for plots ('en' or 'es')
        """
        self.print_lang = print_lang
        self.plot_lang = plot_lang

        # Validate languages
        if print_lang not in LANGUAGES:
            raise ValueError(
                f"Print language '{print_lang}' not supported. Use 'en' or 'es'"
            )
        if plot_lang not in LANGUAGES:
            raise ValueError(
                f"Plot language '{plot_lang}' not supported. Use 'en' or 'es'"
            )

    def t_print(self, key, default=None):
        """
        Get translation for print statements

        Args:
            key (str): Translation key
            default (str): Default value if key not found

        Returns:
            str: Translated text for prints
        """
        return LANGUAGES[self.print_lang].get(key, default or key)

    def t_plot(self, key, default=None):
        """
        Get translation for plot elements

        Args:
            key (str): Translation key
            default (str): Default value if key not found

        Returns:
            str: Translated text for plots
        """
        return LANGUAGES[self.plot_lang].get(key, default or key)

    def get_months_print(self):
        """Get month names for print statements"""
        return LANGUAGES[self.print_lang]["month_names"]

    def get_months_plot(self):
        """Get month names for plots"""
        return LANGUAGES[self.plot_lang]["month_names"]

    def set_print_language(self, lang):
        """Set language for print statements"""
        if lang not in LANGUAGES:
            raise ValueError(f"Language '{lang}' not supported. Use 'en' or 'es'")
        self.print_lang = lang

    def set_plot_language(self, lang):
        """Set language for plots"""
        if lang not in LANGUAGES:
            raise ValueError(f"Language '{lang}' not supported. Use 'en' or 'es'")
        self.plot_lang = lang


# Global i18n instance (can be configured)
i18n = I18n(print_lang="en", plot_lang="en")
