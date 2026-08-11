def calculate_final_score(
    skill_score,
    similarity_score,
    experience_score,
    education_score,
    ai_score
):

    final_score = (
        (skill_score * 0.40)
        + (similarity_score * 0.20)
        + (experience_score * 0.20)
        + (education_score * 0.10)
        + (ai_score * 0.10)
    )

    return round(final_score, 2)