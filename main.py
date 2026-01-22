#!/usr/bin/env python3
"""
Applicant Filter System - Main Entry Point

This system filters candidates based on configurable criteria:
- Age: 20-40 years
- Experience: 1-3 years
- Location: Excludes Sydney
- Background: Prefers China/UK, excludes India/Middle East

Usage:
    python main.py [--verbose] [--detailed]

Options:
    --verbose   Show detailed filtering results
    --detailed  Export detailed Excel report
"""

import sys
import os
import argparse

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.settings import settings
from src.candidate import Candidate
from src.filter_manager import FilterManager
from src.filters import (
    AgeFilter,
    ExperienceFilter,
    LocationFilter,
    BackgroundFilter
)
from src.mock_data import get_mock_candidates
from src.exporter import ExcelExporter


def setup_filters(filter_manager: FilterManager) -> None:
    """
    Configure and add all filters to the filter manager.

    Args:
        filter_manager: The filter manager instance
    """
    filter_settings = settings.filter

    # Add age filter
    filter_manager.add_filter(
        AgeFilter(
            min_age=filter_settings.min_age,
            max_age=filter_settings.max_age
        )
    )

    # Add experience filter
    filter_manager.add_filter(
        ExperienceFilter(
            min_years=filter_settings.min_experience_years,
            max_years=filter_settings.max_experience_years
        )
    )

    # Add location filter
    filter_manager.add_filter(
        LocationFilter(
            excluded_locations=filter_settings.excluded_locations
        )
    )

    # Add background filter
    filter_manager.add_filter(
        BackgroundFilter(
            preferred_backgrounds=filter_settings.preferred_backgrounds,
            excluded_backgrounds=filter_settings.excluded_backgrounds
        )
    )


def display_candidate(candidate: Candidate) -> None:
    """Display a single candidate's information."""
    print(candidate)


def main():
    """Main entry point for the applicant filter system."""
    parser = argparse.ArgumentParser(
        description="Filter candidates based on specified criteria"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show detailed filtering results"
    )
    parser.add_argument(
        "--detailed", "-d",
        action="store_true",
        help="Export detailed Excel report"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("       Applicant Filter System")
    print("=" * 60)
    print()

    # Initialize filter manager
    filter_manager = FilterManager()
    setup_filters(filter_manager)

    print(f"Active filters: {filter_manager.list_filters()}")
    print()

    # Get candidates (using mock data for now)
    print("Loading candidates...")
    candidates = get_mock_candidates()
    print(f"Total candidates loaded: {len(candidates)}")
    print()

    # Apply filters
    print("Applying filters...")
    if args.verbose:
        results = filter_manager.apply_all_with_details(candidates)
        filtered_candidates = results['passed']

        print("\n--- Filter Details ---")
        for filter_name in filter_manager.list_filters():
            failed_key = f"failed_{filter_name}"
            failed_count = len(results.get(failed_key, []))
            print(f"  {filter_name}: {failed_count} failed")
        print()
    else:
        filtered_candidates = filter_manager.apply_all(candidates)
        results = None

    print(f"Candidates after filtering: {len(filtered_candidates)}")
    print()

    # Display filtered candidates
    print("=" * 60)
    print("       FILTERED CANDIDATES")
    print("=" * 60)

    if filtered_candidates:
        for candidate in filtered_candidates:
            display_candidate(candidate)
            print()
    else:
        print("No candidates passed all filters.")
        print()

    # Export to Excel
    print("Exporting to Excel...")
    exporter = ExcelExporter(output_directory=settings.export.output_directory)

    # Export basic report
    basic_path = exporter.export(
        filtered_candidates,
        filename=settings.export.excel_filename
    )
    print(f"  Basic report: {basic_path}")

    # Export detailed report if requested
    if args.detailed:
        detailed_path = exporter.export_detailed(
            filtered_candidates,
            filename="candidates_detailed.xlsx"
        )
        print(f"  Detailed report: {detailed_path}")

    # Export summary if verbose
    if args.verbose and results:
        summary_path = exporter.export_summary(
            total_candidates=len(candidates),
            filtered_candidates=len(filtered_candidates),
            filter_details=results,
            filename="filter_summary.xlsx"
        )
        print(f"  Summary report: {summary_path}")

    print()
    print("=" * 60)
    print("       SUMMARY")
    print("=" * 60)
    print(f"  Total candidates: {len(candidates)}")
    print(f"  Passed filters: {len(filtered_candidates)}")
    print(f"  Pass rate: {len(filtered_candidates)/len(candidates)*100:.1f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
