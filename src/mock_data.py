"""Mock data for development and testing."""

from typing import List
from .candidate import Candidate


def get_mock_candidates() -> List[Candidate]:
    """
    Generate a list of mock candidates for testing.

    Returns:
        List of Candidate objects with varied profiles
    """
    return [
        # Should PASS: Chinese background, 25yo, 2yr exp, Melbourne
        Candidate(
            name="张伟 (Wei Zhang)",
            age=25,
            experience_years=2.0,
            location="Melbourne",
            nationality="Chinese",
            education_background=["China"],
            work_background=["China", "Australia"],
            linkedin_url="https://linkedin.com/in/weizhang",
            current_position="Operation Manager",
            skills=["Project Management", "Supply Chain", "Mandarin"],
            languages=["Mandarin", "English"]
        ),

        # Should PASS: UK background, 28yo, 2.5yr exp, Brisbane
        Candidate(
            name="James Wilson",
            age=28,
            experience_years=2.5,
            location="Brisbane",
            nationality="British",
            education_background=["UK"],
            work_background=["UK", "Australia"],
            linkedin_url="https://linkedin.com/in/jameswilson",
            current_position="Business Development Manager",
            skills=["Sales", "B2B", "CRM"],
            languages=["English"]
        ),

        # Should FAIL: Sydney location
        Candidate(
            name="李明 (Ming Li)",
            age=30,
            experience_years=2.0,
            location="Sydney",
            nationality="Chinese",
            education_background=["China", "UK"],
            work_background=["Australia"],
            linkedin_url="https://linkedin.com/in/mingli",
            current_position="Compliance Advisor",
            skills=["Compliance", "Risk Management"],
            languages=["Mandarin", "English"]
        ),

        # Should FAIL: Too old (45)
        Candidate(
            name="Sarah Thompson",
            age=45,
            experience_years=2.0,
            location="Melbourne",
            nationality="British",
            education_background=["UK"],
            work_background=["UK", "Australia"],
            linkedin_url="https://linkedin.com/in/sarahthompson",
            current_position="Operation Manager",
            skills=["Leadership", "Operations"],
            languages=["English"]
        ),

        # Should FAIL: Too much experience (5 years)
        Candidate(
            name="王芳 (Fang Wang)",
            age=32,
            experience_years=5.0,
            location="Perth",
            nationality="Chinese",
            education_background=["China"],
            work_background=["China", "Singapore", "Australia"],
            linkedin_url="https://linkedin.com/in/fangwang",
            current_position="Business Development Manager",
            skills=["Strategy", "Business Analysis"],
            languages=["Mandarin", "English"]
        ),

        # Should FAIL: Indian background
        Candidate(
            name="Raj Patel",
            age=27,
            experience_years=2.0,
            location="Melbourne",
            nationality="Indian",
            education_background=["India"],
            work_background=["India", "Australia"],
            linkedin_url="https://linkedin.com/in/rajpatel",
            current_position="Operation Manager",
            skills=["Operations", "Team Management"],
            languages=["Hindi", "English"]
        ),

        # Should FAIL: Middle East background
        Candidate(
            name="Ahmed Hassan",
            age=29,
            experience_years=2.5,
            location="Perth",
            nationality="Egyptian",
            education_background=["Egypt", "UK"],
            work_background=["UAE", "Australia"],
            linkedin_url="https://linkedin.com/in/ahmedhassan",
            current_position="Compliance Advisor",
            skills=["Compliance", "Financial Regulations"],
            languages=["Arabic", "English"]
        ),

        # Should PASS: UK educated, Chinese work experience, 23yo, 1.5yr
        Candidate(
            name="Emily Chen",
            age=23,
            experience_years=1.5,
            location="Perth",
            nationality="Australian",
            education_background=["UK"],
            work_background=["China", "Australia"],
            linkedin_url="https://linkedin.com/in/emilychen",
            current_position="Compliance Advisor",
            skills=["Regulatory Compliance", "Policy Analysis"],
            languages=["English", "Mandarin"]
        ),

        # Should FAIL: Too young (19)
        Candidate(
            name="刘洋 (Yang Liu)",
            age=19,
            experience_years=1.0,
            location="Melbourne",
            nationality="Chinese",
            education_background=["China"],
            work_background=["China"],
            linkedin_url="https://linkedin.com/in/yangliu",
            current_position="Business Development Manager",
            skills=["Sales", "Marketing"],
            languages=["Mandarin", "English"]
        ),

        # Should FAIL: No experience (0.5 years)
        Candidate(
            name="Michael Brown",
            age=24,
            experience_years=0.5,
            location="Brisbane",
            nationality="British",
            education_background=["UK"],
            work_background=["UK"],
            linkedin_url="https://linkedin.com/in/michaelbrown",
            current_position="Operation Manager",
            skills=["Entry Level", "Eager to Learn"],
            languages=["English"]
        ),

        # Should PASS: Chinese background, 35yo, 3yr exp, Perth
        Candidate(
            name="陈静 (Jing Chen)",
            age=35,
            experience_years=3.0,
            location="Perth",
            nationality="Chinese",
            education_background=["China", "Australia"],
            work_background=["China", "Australia"],
            linkedin_url="https://linkedin.com/in/jingchen",
            current_position="Operation Manager",
            skills=["Process Optimization", "Team Leadership"],
            languages=["Mandarin", "English"]
        ),

        # Should FAIL: No preferred background (only US/Canada)
        Candidate(
            name="John Smith",
            age=30,
            experience_years=2.0,
            location="Melbourne",
            nationality="American",
            education_background=["USA"],
            work_background=["USA", "Canada"],
            linkedin_url="https://linkedin.com/in/johnsmith",
            current_position="Business Development Manager",
            skills=["Sales Strategy", "Client Relations"],
            languages=["English"]
        ),

        # Should PASS: England education (UK variant), 27yo, 2yr, Adelaide
        Candidate(
            name="Sophie Williams",
            age=27,
            experience_years=2.0,
            location="Adelaide",
            nationality="British",
            education_background=["England"],
            work_background=["United Kingdom", "Australia"],
            linkedin_url="https://linkedin.com/in/sophiewilliams",
            current_position="Compliance Advisor",
            skills=["Legal Compliance", "Risk Assessment"],
            languages=["English"]
        ),
    ]
