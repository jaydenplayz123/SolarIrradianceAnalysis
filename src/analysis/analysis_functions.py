"""
Functions for solar irradiance data analysis
Funciones para análisis de datos de irradiación solar
"""

import numpy as np
import pandas as pd

from src.data.data_sets import get_dataset_years
from src.utils.i18n import i18n


def is_combined_dataset(dataset_name, location):
    """
    Check if this is a combined dataset from multiple stations
    Verifica si este es un dataset combinado de múltiples estaciones
    """
    return (
        "Combined" in dataset_name
        or "|" in location
        or "Station A:" in location
        or "_" in dataset_name
        and any(char.isdigit() for char in dataset_name.split("_")[-1])
    )


def format_location_for_display(location, is_combined=False, i18n_instance=None):
    """
    Format location string for better display in plots and reports
    Formatea la cadena de ubicación para mejor visualización en gráficos e informes
    """
    if is_combined and "|" in location:
        # Split combined locations into separate lines with translated station labels
        stations = location.split("|")
        formatted_stations = []

        for station in stations:
            station = station.strip()
            # Dynamically replace "Station X:" with translated versions
            if station.startswith("Station ") and ":" in station and i18n_instance:
                station_label = i18n_instance.t_print("station")
                # Extract the station identifier (A, B, C, etc.)
                station_id = station.split(":")[0].replace("Station ", "")
                station_coords = station.split(":", 1)[1].strip()
                station = f"{station_label} {station_id}: {station_coords}"
            formatted_stations.append(station)

        return "\n".join(formatted_stations)
    return location


def create_dataframe(data_dict, months):
    """
    Creates a DataFrame from a data dictionary.
    Crea un DataFrame a partir de un diccionario de datos.

    Args:
        data_dict: Dictionary with years as keys and lists of monthly values
        months: List of month names

    Returns:
        pd.DataFrame: DataFrame with years as index and months as columns
    """
    return pd.DataFrame(data_dict, index=months).T


def print_basic_stats(df, dataset_name=""):
    """
    Prints basic dataset statistics.
    Imprime estadísticas básicas del dataset.

    Args:
        df: DataFrame with data
        dataset_name: Dataset name
    """
    # Split dataset name and location for better formatting
    if " - " in dataset_name:
        name_part, location_part = dataset_name.split(" - ", 1)
        print("═" * 70)
        print(f"{i18n.t_print('analysis')} - {name_part}")
        print(f"{location_part}")
        print("═" * 70)
    else:
        print("═" * 70)
        print(f"{i18n.t_print('analysis')} - {dataset_name}")
        print("═" * 70)
    print(f"{i18n.t_print('period')}: {df.index.min()}-{df.index.max()}")
    print(
        f"{i18n.t_print('dimension')}: {df.shape[0]} {i18n.t_print('years')} × {df.shape[1]} {i18n.t_print('months')}"
    )
    print(
        f"{i18n.t_print('global_range')}: {df.values.min():.2f} - {df.values.max():.2f} {i18n.t_print('kwh_per_m2_day')}"
    )


def calculate_annual_mean(df):
    """
    Calcula la media anual para cada año.
    Calculates the annual mean for each year.

    Args:
        df: DataFrame with monthly data

    Returns:
        pd.Series: Series with annual means
    """
    return df.mean(axis=1)


def calculate_climatology(df):
    """
    Calcula la climatología mensual (promedio de cada mes a través de todos los años).

    Args:
        df: DataFrame with monthly data

    Returns:
        pd.Series: Series with monthly climatology
    """
    return df.mean(axis=0)


def calculate_anomalies(df, climatology):
    """
    Calcula anomalías respecto a la climatología.
    Calculates anomalies relative to the climatology.

    Args:
        df: DataFrame with monthly data
        climatology: Series with monthly climatology

    Returns:
        pd.DataFrame: DataFrame con anomalías
    """
    return df - climatology


def calculate_linear_trend(annual_mean):
    """
    Calcula la tendencia lineal de la serie temporal.
    Calculates the linear trend of the time series.

    Args:
        annual_mean: Series with annual means

    Returns:
        tuple: (coefficients, polynomial function)
    """
    z = np.polyfit(annual_mean.index, annual_mean.values, 1)
    p = np.poly1d(z)
    return z, p


def print_detailed_statistics(
    df, annual_mean, climatology, annual_anomalies, z, months
):
    """
    Prints detailed analysis statistics.
    Imprime estadísticas detalladas del análisis.

    Args:
        df: DataFrame with original data
        annual_mean: Series with annual means
        climatology: Series with monthly climatology
        annual_anomalies: Series with annual anomalies
        z: Linear trend coefficients
        months: List of month names
    """
    print("\n" + "═" * 70)
    print(i18n.t_print("detailed_statistics"))
    print("═" * 70)

    # Basic statistics
    print(f"\n1. {i18n.t_print('global_statistics')}:")
    print(
        f"   • {i18n.t_print('period')}: {df.index.min()}-{df.index.max()} ({len(df)} {i18n.t_print('years')})"
    )
    print(
        f"   • {i18n.t_print('global_mean')}: {df.values.mean():.4f} {i18n.t_print('kwh_per_m2_day')}"
    )
    print(
        f"   • {i18n.t_print('standard_deviation')}: {df.values.std():.4f} {i18n.t_print('kwh_per_m2_day')}"
    )
    print(
        f"   • {i18n.t_print('total_range')}: {df.values.min():.4f} - {df.values.max():.4f} {i18n.t_print('kwh_per_m2_day')}"
    )

    print(f"\n2. {i18n.t_print('annual_statistics')}:")
    print(
        f"   • {i18n.t_print('average_annual_mean')}: {annual_mean.mean():.4f} ± {annual_mean.std():.4f} {i18n.t_print('kwh_per_m2_day')}"
    )
    print(
        f"   • {i18n.t_print('year_highest_irradiance')}: {annual_mean.idxmax()} ({annual_mean.max():.4f})"
    )
    print(
        f"   • {i18n.t_print('year_lowest_irradiance')}: {annual_mean.idxmin()} ({annual_mean.min():.4f})"
    )
    print(
        f"   • {i18n.t_print('linear_trend')}: {z[0]:.6f} {i18n.t_print('kwh_per_m2_year')}"
    )

    # Get dynamic period
    start_year, end_year = get_dataset_years(
        {year: df.loc[year].values for year in df.index}
    )
    print(f"\n3. {i18n.t_print('monthly_climatology')} ({start_year}-{end_year}):")
    print(
        f"   {i18n.t_print('month_header')}  {i18n.t_print('average_header')}    {i18n.t_print('maximum_header')}   {i18n.t_print('minimum_header')}    {i18n.t_print('std_header')}"
    )
    print("   " + "-" * 45)
    for i, month in enumerate(months):
        month_data = df[month]
        print(
            f"   {month}     {climatology.iloc[i]:.4f}    {month_data.max():.4f}    {month_data.min():.4f}    {month_data.std():.4f}"
        )

    print(f"\n4. {i18n.t_print('anomaly_analysis')}:")
    print(
        f"   • {i18n.t_print('year_highest_positive_anomaly')}: {annual_anomalies.idxmax()} ({annual_anomalies.max():.4f})"
    )
    print(
        f"   • {i18n.t_print('year_highest_negative_anomaly')}: {annual_anomalies.idxmin()} ({annual_anomalies.min():.4f})"
    )
    print(f"   • {i18n.t_print('years_positive_anomaly')}: {sum(annual_anomalies > 0)}")
    print(f"   • {i18n.t_print('years_negative_anomaly')}: {sum(annual_anomalies < 0)}")
    print(
        f"   • {i18n.t_print('standard_deviation_anomalies')}: {annual_anomalies.std():.4f}"
    )

    # Seasonality
    print(f"\n5. {i18n.t_print('seasonality')}:")
    max_month = months[np.argmax(climatology.values)]
    min_month = months[np.argmin(climatology.values)]
    seasonal_amplitude = climatology.max() - climatology.min()
    print(
        f"   • {i18n.t_print('month_highest_irradiance')}: {max_month} ({climatology.max():.4f} {i18n.t_print('kwh_per_m2_day')})"
    )
    print(
        f"   • {i18n.t_print('month_lowest_irradiance')}: {min_month} ({climatology.min():.4f} {i18n.t_print('kwh_per_m2_day')})"
    )
    print(
        f"   • {i18n.t_print('seasonal_amplitude')}: {seasonal_amplitude:.4f} {i18n.t_print('kwh_per_m2_day')}"
    )

    # Interannual variability
    print(f"\n6. {i18n.t_print('interannual_variability')}:")
    cv_annual = (annual_mean.std() / annual_mean.mean()) * 100
    print(
        f"   • {i18n.t_print('annual_coefficient_variation')}: {cv_annual:.2f}{i18n.t_print('percent')}"
    )
    print(
        f"   • {i18n.t_print('interannual_range')}: {annual_mean.max() - annual_mean.min():.4f} {i18n.t_print('kwh_per_m2_day')}"
    )

    print(f"\n7. {i18n.t_print('final_summary')}:")
    trend_type = (
        i18n.t_print("positive")
        if z[0] > 0
        else i18n.t_print("negative") if z[0] < 0 else i18n.t_print("stable")
    )
    print(f"   • {i18n.t_print('general_trend')}: {trend_type}")
    print(
        f"   • {i18n.t_print('seasonal_variability')}: {seasonal_amplitude:.4f} {i18n.t_print('kwh_per_m2_day')}"
    )
    print(
        f"   • {i18n.t_print('interannual_stability')}: {cv_annual:.2f}{i18n.t_print('percent')} {i18n.t_print('variation')}"
    )


def analyze_dataset(data_dict, months, dataset_name, location=""):
    """
    Función principal que ejecuta todo el análisis para un conjunto de datos.
    Main function that executes the complete analysis for a dataset.

    Args:
        data_dict: Dictionary with the data
        months: List of month names
        dataset_name: Name of the dataset
        location: Location information

    Returns:
        dict: Dictionary with all the analysis results
    """
    # Create DataFrame
    df = create_dataframe(data_dict, months)

    # Basic statistics
    print_basic_stats(df, f"{dataset_name} - {location}")

    # Main calculations
    annual_mean = calculate_annual_mean(df)
    climatology = calculate_climatology(df)
    anomalies = calculate_anomalies(df, climatology)
    annual_anomalies = anomalies.mean(axis=1)
    z, p = calculate_linear_trend(annual_mean)

    # Detailed statistics
    print_detailed_statistics(df, annual_mean, climatology, annual_anomalies, z, months)

    # Return results
    return {
        "dataframe": df,
        "annual_mean": annual_mean,
        "climatology": climatology,
        "anomalies": anomalies,
        "annual_anomalies": annual_anomalies,
        "trend_coefficients": z,
        "trend_function": p,
    }
