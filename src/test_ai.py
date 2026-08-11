from parser import extract_text
from ai_agent import analyze_candidate


resume_path = "resume/Chethan_Resume.pdf"

resume_text = extract_text(resume_path)


with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as file:

    job_description = file.read()


result = analyze_candidate(
    resume_text,
    job_description
)


print("\n==============================")
print("       AI ANALYSIS")
print("==============================")

print("\nCandidate Summary:")
print(result["candidate_summary"])

print("\nRelevant Experience:")
print(result["relevant_experience"])

print("\nEducation:")
print(result["education"])

print("\nStrengths:")

for strength in result["strengths"]:
    print(f"  ✓ {strength}")

print("\nSkill Gaps:")

for gap in result["skill_gaps"]:
    print(f"  ✗ {gap}")

print("\nRecommendation:")
print(result["recommendation"])

print("\nAI Score:")
print(result["ai_score"])