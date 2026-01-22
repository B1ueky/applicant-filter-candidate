#!/bin/bash

# Candidate Display Script
# Displays filtered candidate information in a formatted view

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
BOLD='\033[1m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python3 is not installed${NC}"
    exit 1
fi

# Check if openpyxl is installed
if ! python3 -c "import openpyxl" 2>/dev/null; then
    echo -e "${YELLOW}Installing required dependencies...${NC}"
    pip3 install openpyxl
fi

echo -e "${BLUE}=========================================${NC}"
echo -e "${BOLD}    Applicant Filter - Candidate View${NC}"
echo -e "${BLUE}=========================================${NC}"
echo ""

# Change to project directory and run Python
cd "$PROJECT_DIR"

python3 << 'PYTHON_SCRIPT'
import sys
import os

from config.settings import settings
from src.filter_manager import FilterManager
from src.filters import AgeFilter, ExperienceFilter, LocationFilter, BackgroundFilter
from src.mock_data import get_mock_candidates

# Setup filters
filter_manager = FilterManager()
filter_settings = settings.filter

filter_manager.add_filter(AgeFilter(filter_settings.min_age, filter_settings.max_age))
filter_manager.add_filter(ExperienceFilter(filter_settings.min_experience_years, filter_settings.max_experience_years))
filter_manager.add_filter(LocationFilter(filter_settings.excluded_locations))
filter_manager.add_filter(BackgroundFilter(filter_settings.preferred_backgrounds, filter_settings.excluded_backgrounds))

# Get and filter candidates
candidates = get_mock_candidates()
filtered = filter_manager.apply_all(candidates)

# Display each candidate
for candidate in filtered:
    print(candidate)
    print()

# Summary
print(f"Total filtered candidates: {len(filtered)}/{len(candidates)}")
PYTHON_SCRIPT

echo ""
echo -e "${BLUE}=========================================${NC}"
echo -e "${GREEN}Export Location: output/candidates.xlsx${NC}"
echo -e "${BLUE}=========================================${NC}"
