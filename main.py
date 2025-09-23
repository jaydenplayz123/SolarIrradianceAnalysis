"""
Solar Irradiance Analysis - Interactive Version
Main file with interactive menu for analysis options
Análisis de Irradiación Solar - Versión Interactiva
Archivo principal con menú interactivo para opciones de análisis
"""

from src.analysis.analysis_functions import analyze_dataset
from src.core.config import LANGUAGE_CONFIG

# Import custom modules
from src.data.data_sets import (
    DATASET_METADATA,
    get_all_available_datasets,
    get_all_datasets_period,
    get_dataset_display_name,
    get_dataset_object_and_metadata,
)
from src.export.document_exporter import create_reports
from src.utils.i18n import i18n
from src.visualization.plotting_functions import (
    compare_datasets,
    create_decade_analysis_plot,
    create_main_analysis_plot,
)


def show_menu():
    """
    Show interactive menu for analysis options
    """
    print("\n" + "=" * 80)
    print(
        f"🌞 {i18n.t_print('solar_irradiance_analysis')} - {i18n.t_print('multiple_datasets')}"
    )
    start_year, end_year = get_all_datasets_period()
    print(f"📅 {i18n.t_print('period')}: {start_year}-{end_year}")
    print("=" * 80)

    print(f"\n📊 {i18n.t_print('analysis')} OPTIONS:")
    print("1. 🖥️  Complete console analysis (all datasets)")
    print("2. 📄 Export individual dataset")
    print("3. 📚 Export all datasets (comprehensive document)")
    print("4. 🔄 Console + Export (all datasets)")
    print("5. ⚙️  Configuration")
    print("0. ❌ Exit")

    return input("\n👉 Select option (0-5): ").strip()


def show_dataset_menu():
    """
    Show dataset selection menu
    """
    print("\n📁 Select Dataset:")
    datasets = get_all_available_datasets()
    for i, dataset in enumerate(datasets, 1):
        metadata = DATASET_METADATA[dataset]
        display_name = get_dataset_display_name(dataset, i18n)
        print(f"{i}. {display_name} - {metadata['location']}")

    choice = input(f"\n👉 Select dataset (1-{len(datasets)}): ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(datasets):
            return datasets[idx]
    except ValueError:
        pass
    return None


def show_export_format_menu():
    """
    Show export format selection menu
    """
    print("\n📄 Export Format:")
    print("1. 📝 DOCX only")
    print("2. 📊 PDF only")
    print("3. 📚 Both (DOCX + PDF)")

    choice = input("\n👉 Select format (1-3): ").strip()
    formats = {"1": "docx", "2": "pdf", "3": "both"}
    return formats.get(choice, "both")


def show_config_menu():
    """
    Show configuration menu
    """
    print("\n⚙️  Current Configuration:")
    print(
        f"   Print Language: {LANGUAGE_CONFIG['print_language']} ({'English' if LANGUAGE_CONFIG['print_language'] == 'en' else 'Español'})"
    )
    print(
        f"   Plot Language:  {LANGUAGE_CONFIG['plot_language']} ({'English' if LANGUAGE_CONFIG['plot_language'] == 'en' else 'Español'})"
    )

    print("\n🌍 Language Options:")
    print("1. 🇺🇸 English (prints + plots)")
    print("2. 🇪🇸 Español (prints + plots)")
    print("3. 🔀 Mixed: English plots, Spanish prints")
    print("4. 🔀 Mixed: Spanish plots, English prints")
    print("0. ↩️  Return to main menu")

    choice = input("\n👉 Select option (0-4): ").strip()

    if choice == "1":
        i18n.set_print_language("en")
        i18n.set_plot_language("en")
        print("✅ Configuration: English (both)")
    elif choice == "2":
        i18n.set_print_language("es")
        i18n.set_plot_language("es")
        print("✅ Configuration: Español (both)")
    elif choice == "3":
        i18n.set_print_language("es")
        i18n.set_plot_language("en")
        print("✅ Configuration: English plots, Spanish prints")
    elif choice == "4":
        i18n.set_print_language("en")
        i18n.set_plot_language("es")
        print("✅ Configuration: Spanish plots, English prints")


def run_console_analysis():
    """
    Run complete console analysis for all datasets
    """
    # Get dynamic period for all datasets
    start_year, end_year = get_all_datasets_period()

    print("\n" + "=" * 80)
    print(
        f"{i18n.t_print('solar_irradiance_analysis')} - {i18n.t_print('multiple_datasets')}"
    )
    print(f"{i18n.t_print('period')}: {start_year}-{end_year}")
    print("=" * 80)

    # Dictionary to store all results
    all_results = {}

    # List of datasets to analyze
    # Dynamically build datasets list
    available_datasets = get_all_available_datasets()
    datasets = []
    for dataset_key in available_datasets:
        dataset_obj, metadata = get_dataset_object_and_metadata(dataset_key)
        if dataset_obj and metadata:
            display_name = get_dataset_display_name(dataset_key, i18n)
            datasets.append((display_name, dataset_obj, metadata["location"]))

    # Analyze each dataset
    for dataset_name, data_dict, location in datasets:
        print(f"\n{'='*20} {i18n.t_print('analyzing')} {dataset_name.upper()} {'='*20}")

        # Get months from i18n system (for analysis - use print language for consistency with text output)
        months = i18n.get_months_print()

        # Execute complete analysis
        results = analyze_dataset(data_dict, months, dataset_name, location)

        # Create main plots
        create_main_analysis_plot(
            results["dataframe"],
            results["annual_mean"],
            results["climatology"],
            results["anomalies"],
            results["annual_anomalies"],
            results["trend_coefficients"],
            results["trend_function"],
            months,
            title=f'{i18n.t_plot("monthly_time_series")} - ALLSKY_SFC_SW_DWN\n{dataset_name} - {location}',
        )

        # Create decade analysis plot with dynamic period
        dataset_start, dataset_end = get_all_datasets_period()
        create_decade_analysis_plot(
            results["annual_mean"],
            results["trend_coefficients"],
            results["trend_function"],
            title=f'{i18n.t_plot("annual_mean_irradiance_evolution")}\n{dataset_name} ({dataset_start}-{dataset_end})',
        )

        # Save results
        all_results[dataset_name] = results

        print(
            f"\n{'='*20} {i18n.t_print('end_analysis')} {dataset_name.upper()} {'='*20}"
        )

    # Comparative analysis
    if len(all_results) > 1:
        print(f"\n{'='*20} {i18n.t_print('comparative_analysis')} {'='*20}")
        compare_datasets(all_results, months)

        # Comparative summary
        print(f"\n{i18n.t_print('comparative_summary')}:")
        print("-" * 50)
        for name, results in all_results.items():
            trend = results["trend_coefficients"][0]
            mean_irradiance = results["annual_mean"].mean()
            cv = (results["annual_mean"].std() / results["annual_mean"].mean()) * 100

            print(f"{name}:")
            print(
                f"  • {i18n.t_print('mean_irradiance')}: {mean_irradiance:.4f} {i18n.t_print('kwh_per_m2_day')}"
            )
            print(
                f"  • {i18n.t_print('trend')}: {trend:.6f} {i18n.t_print('kwh_per_m2_year')}"
            )
            print(
                f"  • {i18n.t_print('variability')}: {cv:.2f}{i18n.t_print('percent')}"
            )
            print()

    print("=" * 80)
    print(i18n.t_print("analysis_completed"))
    print("=" * 80)

    return all_results


def run_single_dataset_export():
    """
    Export analysis for a single dataset
    """
    dataset_key = show_dataset_menu()
    if not dataset_key:
        print("❌ Invalid dataset selection")
        return

    format_type = show_export_format_menu()

    # Dataset mapping
    # Dynamically build datasets dictionary
    available_datasets = get_all_available_datasets()
    datasets = {}
    for dataset_key in available_datasets:
        dataset_obj, metadata = get_dataset_object_and_metadata(dataset_key)
        if dataset_obj and metadata:
            datasets[dataset_key] = (dataset_obj, metadata)

    data_dict, metadata = datasets[dataset_key]

    print("\n" + "=" * 80)
    print(f"{i18n.t_print('analyzing')} {dataset_key.upper()}")
    print("=" * 80)

    # Get months from i18n system
    months = i18n.get_months_print()

    # Execute analysis
    results = analyze_dataset(data_dict, months, metadata["name"], metadata["location"])

    # Create results dictionary for export
    all_results = {metadata["name"]: results}

    # Export
    print(f"\n{'='*20} {i18n.t_print('export').upper()} {dataset_key.upper()} {'='*20}")
    try:
        created_files = create_reports(
            all_results, format=format_type, output_dir=f"reports/{dataset_key}"
        )
        print(f"\n✅ {dataset_key} {i18n.t_print('exported_successfully')}")
        for format_type, filepath in created_files.items():
            print(f"   📄 {format_type.upper()}: {filepath}")
    except Exception as e:
        print(f"❌ {i18n.t_print('error_exporting_reports')} {dataset_key}: {e}")

    print("=" * 80)


def run_comprehensive_export():
    """
    Export comprehensive analysis for all datasets
    """
    format_type = show_export_format_menu()

    print("\n" + "=" * 80)
    print(
        f"{i18n.t_print('solar_irradiance_analysis')} - {i18n.t_print('multiple_datasets')}"
    )
    start_year, end_year = get_all_datasets_period()
    print(f"{i18n.t_print('period')}: {start_year}-{end_year}")
    print("=" * 80)

    # Dictionary to store all results
    all_results = {}

    # List of datasets to analyze
    # Dynamically build datasets list
    available_datasets = get_all_available_datasets()
    datasets = []
    for dataset_key in available_datasets:
        dataset_obj, metadata = get_dataset_object_and_metadata(dataset_key)
        if dataset_obj and metadata:
            display_name = get_dataset_display_name(dataset_key, i18n)
            datasets.append((display_name, dataset_obj, metadata["location"]))

    # Analyze each dataset (without plots for faster export)
    for dataset_name, data_dict, location in datasets:
        print(f"\n{'='*20} {i18n.t_print('analyzing')} {dataset_name.upper()} {'='*20}")

        # Get months from i18n system
        months = i18n.get_months_print()

        # Execute analysis
        results = analyze_dataset(data_dict, months, dataset_name, location)

        # Save results
        all_results[dataset_name] = results

        print(
            f"{'='*20} {i18n.t_print('end_analysis')} {dataset_name.upper()} {'='*20}"
        )

    print("=" * 80)
    print(i18n.t_print("analysis_completed"))
    print("=" * 80)

    # Export comprehensive results to documents
    if all_results:
        print(
            f"\n{'='*20} {i18n.t_print('analysis').upper()} {i18n.t_print('export')} {'='*20}"
        )
        try:
            # Export to a comprehensive report directory
            created_files = create_reports(
                all_results,
                format=format_type,
                output_dir="reports/comprehensive_analysis",
            )
            print(
                f"\n✅ {i18n.t_print('analysis')} {i18n.t_print('exported_successfully')}"
            )
            print(
                f"📁 {i18n.t_print('analysis')} completo con {len(all_results)} datasets:"
            )
            for format_type, filepath in created_files.items():
                print(f"   📄 {format_type.upper()}: {filepath}")
        except Exception as e:
            print(f"❌ {i18n.t_print('error_exporting_reports')}: {e}")
        print("=" * 80)


def run_console_and_export():
    """
    Run complete console analysis and export
    """
    format_type = show_export_format_menu()

    # Run console analysis
    all_results = run_console_analysis()

    # Export results to documents
    if all_results:
        print(
            f"\n{'='*20} {i18n.t_print('analysis').upper()} {i18n.t_print('export')} {'='*20}"
        )
        try:
            created_files = create_reports(all_results, format=format_type)
            print(
                f"\n✅ {i18n.t_print('analysis')} {i18n.t_print('exported_successfully')}"
            )
            for format_type, filepath in created_files.items():
                print(f"   📄 {format_type.upper()}: {filepath}")
        except Exception as e:
            print(f"❌ {i18n.t_print('error_exporting_reports')}: {e}")
        print("=" * 80)


def main():
    """
    Main function with interactive menu
    """
    # Initialize i18n with configuration
    i18n.set_print_language(LANGUAGE_CONFIG["print_language"])
    i18n.set_plot_language(LANGUAGE_CONFIG["plot_language"])

    while True:
        choice = show_menu()

        if choice == "0":
            print(f"\n👋 {i18n.t_print('analysis_completed')}!")
            break
        elif choice == "1":
            run_console_analysis()
        elif choice == "2":
            run_single_dataset_export()
        elif choice == "3":
            run_comprehensive_export()
        elif choice == "4":
            run_console_and_export()
        elif choice == "5":
            show_config_menu()
        else:
            print("❌ Invalid option. Please select 0-5.")

        input("\n⏸️  Press Enter to continue...")


if __name__ == "__main__":
    main()
