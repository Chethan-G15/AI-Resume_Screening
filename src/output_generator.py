import csv
import json
import os


def save_csv(results, output_path):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Header
        writer.writerow([
            "Rank",
            "Candidate",
            "Final Score",
            "Skill Score",
            "NLP Similarity",
            "Experience Score",
            "Education Score",
            "AI Score",
            "Matched Skills",
            "Missing Skills",
            "Recommendation"
        ])

        # Data
        for rank, result in enumerate(
            results,
            start=1
        ):

            writer.writerow([
                rank,
                result["candidate"],
                result["final_score"],
                result["skill_score"],
                result["similarity_score"],
                result["experience_score"],
                result["education_score"],
                result["ai_score"],
                ", ".join(
                    result["matched_skills"]
                ),
                ", ".join(
                    result["missing_skills"]
                ),
                result["recommendation"]
            ])


def save_json(results, output_path):

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    output_data = []

    for rank, result in enumerate(
        results,
        start=1
    ):

        candidate_data = {
            "rank": rank,
            "candidate": result["candidate"],
            "final_score": result["final_score"],
            "skill_score": result["skill_score"],
            "similarity_score": result["similarity_score"],
            "experience_score": result["experience_score"],
            "education_score": result["education_score"],
            "ai_score": result["ai_score"],
            "matched_skills": result["matched_skills"],
            "missing_skills": result["missing_skills"],
            "recommendation": result["recommendation"],
            "summary": result["summary"]
        }

        output_data.append(candidate_data)

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output_data,
            file,
            indent=4,
            ensure_ascii=False
        )