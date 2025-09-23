"""
Functions for solar irradiance data visualization
Funciones para visualización de datos de irradiación solar
"""

import matplotlib.pyplot as plt
import numpy as np

from src.analysis.analysis_functions import (
    format_location_for_display,
    is_combined_dataset,
)
from src.data.data_sets import get_dataset_years
from src.utils.i18n import i18n


def create_main_analysis_plot(
    df,
    annual_mean,
    climatology,
    anomalies,
    annual_anomalies,
    z,
    p,
    months,
    title="Monthly Time Series - ALLSKY_SFC_SW_DWN",
    location="",
):
    """
    Creates the main plot with 4 subplots for analysis.
    Crea el gráfico principal con 4 subplots del análisis.

    Args:
        df: DataFrame with data
        annual_mean: Series with annual means
        climatology: Series with monthly climatology
        anomalies: DataFrame with anomalies
        annual_anomalies: Series with annual anomalies
        z: Trend coefficients
        p: Trend function
        months: List of month names
        title: Main plot title
    """
    # Plot style configuration
    plt.style.use("default")
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Use figtext for better control over title positioning and line breaks
    # Extract dataset name from title for better formatting
    if " - ALLSKY_SFC_SW_DWN" in title:
        title_parts = title.split(" - ALLSKY_SFC_SW_DWN")
        title_line1 = title_parts[0]
        title_line2 = "ALLSKY_SFC_SW_DWN" + (
            title_parts[1] if len(title_parts) > 1 else ""
        )

        # Add title with proper spacing - positioned at top center
        fig.text(
            0.5,
            0.96,
            title_line1,
            ha="center",
            va="top",
            fontsize=16,
            fontweight="bold",
        )
        fig.text(
            0.5,
            0.93,
            title_line2,
            ha="center",
            va="top",
            fontsize=14,
            fontweight="bold",
        )

        # Add location information for combined datasets
        if location and is_combined_dataset(title_line1, location):
            formatted_location = format_location_for_display(location, True, i18n)
            fig.text(
                0.5,
                0.90,
                formatted_location,
                ha="center",
                va="top",
                fontsize=10,
                fontweight="normal",
                style="italic",
                color="gray",
            )
    else:
        # Fallback for other title formats
        fig.text(
            0.5, 0.95, title, ha="center", va="top", fontsize=16, fontweight="bold"
        )

        # Add location for single datasets if provided
        if location:
            formatted_location = format_location_for_display(location, False, i18n)
            fig.text(
                0.5,
                0.92,
                formatted_location,
                ha="center",
                va="top",
                fontsize=10,
                fontweight="normal",
                style="italic",
                color="gray",
            )

    # Get plot months (for plot language)
    plot_months = i18n.get_months_plot()

    # 1. MONTHLY TIME SERIES
    ax1 = axes[0, 0]
    colors = plt.cm.tab20(np.linspace(0, 1, len(months)))
    for i, month in enumerate(months):
        ax1.plot(
            df.index,
            df[month],
            label=plot_months[i],
            linewidth=1,
            alpha=0.7,
            color=colors[i],
        )

    ax1.set_title(
        i18n.t_plot("monthly_time_series_subplot"), fontweight="bold", loc="left"
    )
    ax1.set_xlabel(i18n.t_plot("year"))
    ax1.set_ylabel(i18n.t_plot("irradiance_kwh"))
    ax1.grid(True, alpha=0.3)
    ax1.legend(ncol=4, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.15))
    ax1.set_xlim(df.index.min(), df.index.max())

    # Dynamic Y-axis limits based on data range
    y_min = df.values.min()
    y_max = df.values.max()
    y_margin = (y_max - y_min) * 0.1  # 10% margin
    ax1.set_ylim(y_min - y_margin, y_max + y_margin)

    # 2. ANNUAL MEAN
    ax2 = axes[0, 1]
    ax2.plot(
        annual_mean.index,
        annual_mean.values,
        linewidth=2.5,
        color="red",
        marker="o",
        markersize=3,
    )
    ax2.set_title(i18n.t_plot("annual_mean_subplot"), fontweight="bold", loc="left")
    ax2.set_xlabel(i18n.t_plot("year"))
    ax2.set_ylabel(i18n.t_plot("mean_annual_irradiance"))
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(annual_mean.index.min(), annual_mean.index.max())

    # Dynamic Y-axis limits for annual mean
    annual_min = annual_mean.min()
    annual_max = annual_mean.max()
    annual_margin = (annual_max - annual_min) * 0.15  # 15% margin
    ax2.set_ylim(annual_min - annual_margin, annual_max + annual_margin)

    # Linear trend
    ax2.plot(
        annual_mean.index,
        p(annual_mean.index),
        "r--",
        alpha=0.8,
        linewidth=1.5,
        label=f'{i18n.t_plot("trend_label")}: {z[0]:.4f} {i18n.t_plot("kwh_per_m2_year")}',
    )
    ax2.legend()

    # 3. MONTHLY CLIMATOLOGY
    ax3 = axes[1, 0]
    ax3.plot(
        plot_months,
        climatology.values,
        marker="o",
        linewidth=2.5,
        color="green",
        markerfacecolor="darkgreen",
        markersize=6,
    )

    # Get dynamic period for subtitle
    start_year, end_year = get_dataset_years(
        {year: df.loc[year].values for year in df.index}
    )
    climatology_title = (
        f"{i18n.t_plot('climatology_subplot')} - {start_year}-{end_year}"
    )
    ax3.set_title(climatology_title, fontweight="bold", loc="left")
    ax3.set_xlabel(i18n.t_plot("month"))
    ax3.set_ylabel(i18n.t_plot("mean_irradiance"))
    ax3.grid(True, alpha=0.3)

    # Dynamic Y-axis limits for climatology
    clim_min = climatology.min()
    clim_max = climatology.max()
    clim_margin = (clim_max - clim_min) * 0.15  # 15% margin for better visibility
    ax3.set_ylim(clim_min - clim_margin, clim_max + clim_margin)
    ax3.fill_between(plot_months, climatology.values, alpha=0.2, color="green")

    # 4. MONTHLY ANOMALIES
    ax4 = axes[1, 1]

    # Monthly anomalies
    for i, month in enumerate(months):
        ax4.plot(
            anomalies.index, anomalies[month], alpha=0.2, linewidth=0.5, color=colors[i]
        )

    # Annual mean anomalies
    ax4.plot(
        annual_anomalies.index,
        annual_anomalies.values,
        linewidth=2.5,
        color="black",
        label=i18n.t_plot("annual_mean"),
        marker="o",
        markersize=3,
    )

    # 5-year rolling mean
    rolling_mean = annual_anomalies.rolling(window=5, center=True).mean()
    ax4.plot(
        rolling_mean.index,
        rolling_mean.values,
        linewidth=2,
        color="blue",
        label=i18n.t_plot("rolling_mean_5_years"),
    )

    ax4.set_title(i18n.t_plot("anomalies_subplot"), fontweight="bold", loc="left")
    ax4.set_xlabel(i18n.t_plot("year"))
    ax4.set_ylabel(i18n.t_plot("anomaly_kwh"))
    ax4.grid(True, alpha=0.3)
    ax4.axhline(y=0, color="black", linestyle="-", alpha=0.7)
    ax4.set_xlim(anomalies.index.min(), anomalies.index.max())

    # Dynamic Y-axis limits for anomalies
    anom_min = min(anomalies.values.min(), annual_anomalies.min())
    anom_max = max(anomalies.values.max(), annual_anomalies.max())
    anom_margin = max(abs(anom_min), abs(anom_max)) * 0.2  # 20% margin, symmetric
    ax4.set_ylim(-anom_margin - abs(anom_min), anom_margin + abs(anom_max))
    ax4.legend()

    plt.tight_layout()
    # Adjust spacing to accommodate the two-line title
    plt.subplots_adjust(top=0.90)
    plt.show()


def create_decade_analysis_plot(
    annual_mean, z, p, title="Annual Mean Irradiance Evolution by Decades"
):
    """
    Creates a decade analysis plot.
    Crea un gráfico de análisis por décadas.

    Args:
        annual_mean: Series with annual means
        z: Trend coefficients
        p: Trend function
        title: Plot title
    """
    plt.figure(figsize=(12, 6))
    decades = [(1984, 1993), (1994, 2003), (2004, 2013), (2014, 2024)]
    decade_colors = ["blue", "green", "orange", "red"]

    for i, (start, end) in enumerate(decades):
        dec_data = annual_mean[
            (annual_mean.index >= start) & (annual_mean.index <= end)
        ]
        if len(dec_data) > 0:
            plt.plot(
                dec_data.index,
                dec_data.values,
                "o-",
                color=decade_colors[i],
                label=f"{start}-{end}",
                alpha=0.7,
                markersize=4,
            )

    plt.plot(
        annual_mean.index,
        p(annual_mean.index),
        "k--",
        linewidth=2,
        label=f'{i18n.t_plot("general_trend")} ({z[0]:.4f}/{i18n.t_plot("year")})',
    )
    # Improve title formatting for better readability
    if "\n" in title:
        plt.title(title, fontweight="bold", pad=20)
    else:
        # Split long titles for better display
        if len(title) > 50:
            words = title.split()
            mid = len(words) // 2
            title_line1 = " ".join(words[:mid])
            title_line2 = " ".join(words[mid:])
            formatted_title = f"{title_line1}\n{title_line2}"
            plt.title(formatted_title, fontweight="bold", pad=20)
        else:
            plt.title(title, fontweight="bold", pad=20)

    plt.xlabel(i18n.t_plot("year"))
    plt.ylabel(i18n.t_plot("annual_mean_irradiance"))
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def compare_datasets(results_dict, months):
    """
    Creates comparative plots between multiple datasets.
    Crea gráficos comparativos entre múltiples conjuntos de datos.

    Args:
        results_dict: Dictionary with results from multiple analyses
        months: List of month names
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle(i18n.t_plot("dataset_comparison"), fontsize=16, fontweight="bold")

    colors = ["blue", "red", "green", "orange", "purple", "brown"]
    plot_months = i18n.get_months_plot()

    # 1. Annual means comparison
    ax1 = axes[0, 0]
    for i, (name, results) in enumerate(results_dict.items()):
        ax1.plot(
            results["annual_mean"].index,
            results["annual_mean"].values,
            label=name,
            color=colors[i % len(colors)],
            linewidth=2,
            alpha=0.8,
        )

    ax1.set_title(i18n.t_plot("annual_means_comparison"), fontweight="bold", loc="left")
    ax1.set_xlabel(i18n.t_plot("year"))
    ax1.set_ylabel(i18n.t_plot("annual_mean_irradiance"))
    ax1.grid(True, alpha=0.3)
    ax1.legend()

    # 2. Climatologies comparison
    ax2 = axes[0, 1]
    for i, (name, results) in enumerate(results_dict.items()):
        ax2.plot(
            plot_months,
            results["climatology"].values,
            label=name,
            color=colors[i % len(colors)],
            linewidth=2,
            alpha=0.8,
            marker="o",
        )

    ax2.set_title(
        i18n.t_plot("climatologies_comparison"), fontweight="bold", loc="left"
    )
    ax2.set_xlabel(i18n.t_plot("month"))
    ax2.set_ylabel(i18n.t_plot("monthly_mean_irradiance"))
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # 3. Trends comparison
    ax3 = axes[1, 0]
    trends = []
    names = []
    for name, results in results_dict.items():
        trends.append(
            results["trend_coefficients"][0] * 1000
        )  # Convert to mWh/m²/day/year
        names.append(name)

    bars = ax3.bar(names, trends, color=colors[: len(names)], alpha=0.7)
    ax3.set_title(i18n.t_plot("trends_comparison"), fontweight="bold", loc="left")
    ax3.set_ylabel(i18n.t_plot("trend_mwh"))
    ax3.grid(True, alpha=0.3, axis="y")
    ax3.axhline(y=0, color="black", linestyle="-", alpha=0.5)

    # Add values on bars
    for bar, trend in zip(bars, trends):
        height = bar.get_height()
        ax3.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + (0.01 if height >= 0 else -0.05),
            f"{trend:.2f}",
            ha="center",
            va="bottom" if height >= 0 else "top",
        )

    # 4. Variability comparison
    ax4 = axes[1, 1]
    variabilities = []
    for name, results in results_dict.items():
        cv = (results["annual_mean"].std() / results["annual_mean"].mean()) * 100
        variabilities.append(cv)

    bars = ax4.bar(names, variabilities, color=colors[: len(names)], alpha=0.7)
    ax4.set_title(i18n.t_plot("variability_comparison"), fontweight="bold", loc="left")
    ax4.set_ylabel(i18n.t_plot("coefficient_variation"))
    ax4.grid(True, alpha=0.3, axis="y")

    # Add values on bars
    for bar, cv in zip(bars, variabilities):
        height = bar.get_height()
        ax4.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 0.01,
            f'{cv:.2f}{i18n.t_plot("percent")}',
            ha="center",
            va="bottom",
        )

    plt.tight_layout()
    plt.subplots_adjust(top=0.93)
    plt.show()
