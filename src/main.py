from src.batch_processor import process_all_resumes

from src.output_generator import (
    save_csv,
    save_json
)


# ==========================================
# 1. Read Job Description
# ==========================================

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()


# ==========================================
# 2. Process All Resumes
# ==========================================

results = process_all_resumes(
    "resumes",
    job_description
)


# ==========================================
# 3. Save Results
# ==========================================

save_csv(
    results,
    "output/ranked_candidates.csv"
)

save_json(
    results,
    "output/ranked_candidates.json"
)


# ==========================================
# 4. Display Ranking
# ==========================================

print("\n")
print("==========================================")
print("       RESUME SCREENING RESULTS")
print("==========================================")


for index, result in enumerate(
    results,
    start=1
):

    print(
        f"\n#{index} "
        f"{result['candidate']}"
    )

    print(
        f"Final Score: "
        f"{result['final_score']:.2f}%"
    )

    print(
        f"Skills: "
        f"{result['skill_score']:.2f}%"
    )

    print(
        f"NLP Similarity: "
        f"{result['similarity_score']:.2f}%"
    )

    print(
        f"Experience: "
        f"{result['experience_score']:.2f}%"
    )

    print(
        f"Education: "
        f"{result['education_score']:.2f}%"
    )

    print(
        f"AI Score: "
        f"{result['ai_score']:.2f}%"
    )

    print(
        f"Recommendation: "
        f"{result['recommendation']}"
    )


print("\n==========================================")

print(
    f"Total Resumes Processed: "
    f"{len(results)}"
)

print("==========================================")

print("\nFiles generated:")

print(
    "✓ output/ranked_candidates.csv"
)

print(
    "✓ output/ranked_candidates.json"
)