"""Candidate data model."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Candidate:
    """
    Represents a candidate for filtering.

    Attributes:
        name: Full name of the candidate
        age: Age in years
        experience_years: Years of relevant work experience
        location: Current location (city)
        nationality: Nationality of the candidate
        education_background: List of countries where education was obtained
        work_background: List of countries where work experience was gained
        linkedin_url: LinkedIn profile URL
        current_position: Current or most recent job title
        skills: List of skills (optional)
        languages: List of languages spoken (optional)
    """
    name: str
    age: int
    experience_years: float
    location: str
    nationality: str
    education_background: List[str]
    work_background: List[str]
    linkedin_url: str
    current_position: str
    skills: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    email: Optional[str] = None
    phone: Optional[str] = None

    def has_background_in(self, countries: List[str]) -> bool:
        """
        Check if candidate has education or work background in any of the specified countries.

        Args:
            countries: List of country names to check

        Returns:
            True if candidate has background in at least one of the countries
        """
        countries_lower = [c.lower() for c in countries]
        all_backgrounds = self.education_background + self.work_background
        return any(bg.lower() in countries_lower for bg in all_backgrounds)

    def to_dict(self) -> dict:
        """Convert candidate to dictionary representation."""
        return {
            "name": self.name,
            "age": self.age,
            "experience_years": self.experience_years,
            "location": self.location,
            "nationality": self.nationality,
            "education_background": self.education_background,
            "work_background": self.work_background,
            "linkedin_url": self.linkedin_url,
            "current_position": self.current_position,
            "skills": self.skills,
            "languages": self.languages,
            "email": self.email,
            "phone": self.phone
        }

    def __str__(self) -> str:
        """String representation for display."""
        return (
            f"=========================================\n"
            f"姓名: {self.name}\n"
            f"职位: {self.current_position}\n"
            f"经验: {self.experience_years}年\n"
            f"地点: {self.location}\n"
            f"LinkedIn: {self.linkedin_url}\n"
            f"========================================="
        )
