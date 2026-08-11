import os

from src.parser import extract_text
from src.score import calculate_similarity
from src.skill_matcher import calculate_skill_match
from src.candidate_analyzer import (
    analyze_experience,
    analyze_education
)
from src.ai_agent import analyze_candidate
from src.final_score import calculate_final_score


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}


def process_resume(resume_path, job_description):

    # -----------------------------
    # Candidate name
    # -----------------------------

    file_name = os.path.basename(resume_path)

    candidate_name = os.path.splitext(
        file_name
    )[0]


    # -----------------------------
    # Extract resume text
    # -----------------------------

    resume_text = extract_text(
        resume_path
    )


    # -----------------------------
    # NLP similarity
    # -----------------------------

    similarity_score = calculate_similarity(
        job_description,
        resume_text
    )


    # -----------------------------
    # Skill matching
    # -----------------------------

    skill_result = calculate_skill_match(
        job_description,
        resume_text
    )


    # -----------------------------
    # Experience
    # -----------------------------

    experience_result = analyze_experience(
        resume_text,
        job_description
    )


    # -----------------------------
    # Education
    # -----------------------------

    education_result = analyze_education(
        resume_text,
        job_description
    )


    # -----------------------------
    # AI analysis
    # -----------------------------

    ai_result = analyze_candidate(
        resume_text,
        job_description
    )


    # -----------------------------
    # Final score
    # -----------------------------

    final_score = calculate_final_score(

        skill_score=skill_result["score"],

        similarity_score=similarity_score,

        experience_score=experience_result["score"],

        education_score=education_result["score"],

        ai_score=ai_result["ai_score"]
    )


    return {

        "candidate": candidate_name,

        "file": file_name,

        "final_score": final_score,

        "skill_score": skill_result["score"],

        "similarity_score": similarity_score,

        "experience_score": experience_result["score"],

        "education_score": education_result["score"],

        "ai_score": ai_result["ai_score"],

        "matched_skills":
            skill_result["matched_skills"],

        "missing_skills":
            skill_result["missing_skills"],

        "recommendation":
            ai_result["recommendation"],

        "summary":
            ai_result["candidate_summary"]
    }


def process_all_resumes(
    resumes_folder,
    job_description
):

    results = []


    for file_name in os.listdir(
        resumes_folder
    ):

        file_path = os.path.join(
            resumes_folder,
            file_name
        )


        # Ignore folders

        if not os.path.isfile(file_path):
            continue


        # Check extension

        extension = os.path.splitext(
            file_name
        )[1].lower()


        if extension not in SUPPORTED_EXTENSIONS:
            continue


        print(
            f"\nProcessing: {file_name}"
        )


        try:

            result = process_resume(
                file_path,
                job_description
            )

            results.append(result)


        except Exception as error:

            print(
                f"Error processing "
                f"{file_name}: {error}"
            )


    # Sort highest score first

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )


    return results