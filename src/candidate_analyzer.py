import re


def analyze_experience(resume_text, job_description):
    """
    Basic experience analysis.
    """

    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    # Look for internship / experience keywords
    experience_keywords = [
        "intern",
        "internship",
        "developer",
        "software engineer",
        "work experience",
        "professional experience"
    ]

    has_experience = any(
        keyword in resume_lower
        for keyword in experience_keywords
    )

    # Extract years of experience from JD
    jd_year_match = re.search(
        r"(\d+)\s*[-–]?\s*(\d+)?\s*years?",
        jd_lower
    )

    required_years = 0

    if jd_year_match:
        required_years = int(jd_year_match.group(1))

    # Basic score
    if has_experience:
        score = 100
    elif required_years == 0:
        score = 80
    else:
        score = 40

    return {
        "score": score,
        "has_experience": has_experience,
        "required_years": required_years
    }


def analyze_education(resume_text, job_description):
    """
    Basic education matching.
    """

    resume_lower = resume_text.lower()
    jd_lower = job_description.lower()

    education_keywords = [
        "bca",
        "bachelor",
        "bachelor's",
        "bachelor of computer application",
        "mca",
        "master",
        "master's",
        "master of computer application",
        "computer science",
        "information technology"
    ]

    resume_education = []

    for education in education_keywords:

        if education in resume_lower:
            resume_education.append(education)

    required_education = []

    for education in education_keywords:

        if education in jd_lower:
            required_education.append(education)

    # Remove duplicates
    resume_education = sorted(set(resume_education))
    required_education = sorted(set(required_education))

    if resume_education and required_education:
        score = 100
    elif resume_education:
        score = 80
    else:
        score = 0

    return {
        "score": score,
        "resume_education": resume_education,
        "required_education": required_education
    }