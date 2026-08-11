import os
import json
from dotenv import load_dotenv
from groq import Groq


# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")


# Create Groq client
client = Groq(api_key=api_key)


def analyze_candidate(resume_text, job_description):

    prompt = f"""
You are a Resume Screening Assistant.

Your task is to analyze a candidate's resume against a Job Description.

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume_text}

Analyze the candidate based only on the information provided.

Return the result as valid JSON with exactly these fields:

{{
    "candidate_summary": "Short summary of the candidate",
    "relevant_experience": "Relevant experience mentioned in the resume",
    "education": "Relevant education",
    "strengths": [
        "strength 1",
        "strength 2",
        "strength 3"
    ],
    "skill_gaps": [
        "missing or weak skill 1",
        "missing or weak skill 2"
    ],
    "recommendation": "Short recommendation",
    "ai_score": 0
}}

The ai_score must be a number from 0 to 100.

Do not invent information.
If information is not available in the resume, say "Not mentioned".
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a careful and objective resume screening assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    # Remove markdown code fences if the model adds them
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        return {
            "candidate_summary": result,
            "relevant_experience": "Not available",
            "education": "Not available",
            "strengths": [],
            "skill_gaps": [],
            "recommendation": "Unable to parse structured AI response",
            "ai_score": 0
        }