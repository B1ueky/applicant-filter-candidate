"""Configuration settings for the applicant filter system."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class FilterSettings:
    """Filter criteria configuration."""
    # Age filter settings
    min_age: int = 20
    max_age: int = 40

    # Experience filter settings
    min_experience_years: float = 1.0
    max_experience_years: float = 3.0

    # Location filter settings
    excluded_locations: List[str] = field(default_factory=lambda: ["Sydney"])

    # Background filter settings (中文和英文背景)
    preferred_backgrounds: List[str] = field(default_factory=lambda: [
        # 中文背景
        "China", "Taiwan", "Hong Kong", "Macau", "Singapore",
        # 英文背景
        "UK", "United Kingdom", "England", "Australia", "New Zealand", "USA", "Canada"
    ])
    excluded_backgrounds: List[str] = field(default_factory=lambda: [
        "India", "Pakistan", "Bangladesh",  # South Asia
        "Saudi Arabia", "UAE", "United Arab Emirates", "Qatar", "Kuwait",
        "Bahrain", "Oman", "Iran", "Iraq", "Jordan", "Lebanon", "Syria",
        "Yemen", "Egypt", "Israel", "Palestine"  # Middle East
    ])


@dataclass
class LinkedInAPISettings:
    """LinkedIn API configuration (placeholder for future integration)."""
    api_key: str = ""
    api_secret: str = ""
    access_token: str = ""
    base_url: str = "https://api.linkedin.com/v2"


@dataclass
class ExportSettings:
    """Export configuration."""
    output_directory: str = "output"
    excel_filename: str = "candidates.xlsx"


@dataclass
class Settings:
    """Main settings container."""
    filter: FilterSettings = field(default_factory=FilterSettings)
    linkedin_api: LinkedInAPISettings = field(default_factory=LinkedInAPISettings)
    export: ExportSettings = field(default_factory=ExportSettings)

    # Target positions
    target_positions: List[str] = field(default_factory=lambda: [
        "Operation Manager",
        "Compliance Advisor",
        "Business Development Manager"
    ])


# Global settings instance
settings = Settings()
