import re


SKILLS = [
    "java",
    "python",
    "c",
    "c++",
    "c#",
    "javascript",
    "html",
    "css",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "jdbc",
    "spring",
    "spring mvc",
    "spring boot",
    "hibernate",
    "rest api",
    "rest apis",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "openstack",
    "data structures",
    "algorithms",
    "oop",
    "object oriented programming",
    "exception handling",
    "collections",
    "react",
    "node.js",
    "nodejs"
]


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text


def extract_skills(text):

    text = normalize_text(text)

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return sorted(set(found_skills))


def calculate_skill_match(job_description, resume_text):

    jd_skills = extract_skills(job_description)

    resume_skills = extract_skills(resume_text)

    matched_skills = []

    missing_skills = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    if len(jd_skills) == 0:
        score = 0

    else:
        score = (
            len(matched_skills) /
            len(jd_skills)
        ) * 100

    return {
        "score": score,
        "job_skills": jd_skills,
        "resume_skills": resume_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }