import streamlit as st
import os
import shutil

from src.batch_processor import process_all_resumes
from src.output_generator import save_csv, save_json


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("📄 AI Resume Screening Agent")

st.write(
    "Upload a Job Description and candidate resumes "
    "to automatically screen and rank candidates."
)


# ==========================================
# Job Description
# ==========================================

st.header("1. Job Description")

jd_file = st.file_uploader(
    "Upload Job Description",
    type=["txt"]
)


# ==========================================
# Resumes
# ==========================================

st.header("2. Upload Resumes")

resume_files = st.file_uploader(
    "Upload candidate resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)


# ==========================================
# Screen Button
# ==========================================

if st.button(
    "🚀 Screen Resumes",
    type="primary"
):

    if jd_file is None:

        st.error(
            "Please upload a Job Description."
        )

        st.stop()


    if not resume_files:

        st.error(
            "Please upload at least one resume."
        )

        st.stop()


    # ======================================
    # Read Job Description
    # ======================================

    job_description = jd_file.read().decode(
        "utf-8"
    )


    # ======================================
    # Create resume folder
    # ======================================

    resume_folder = "resumes"

    os.makedirs(
        resume_folder,
        exist_ok=True
    )


    # Remove old uploaded resumes

    for old_file in os.listdir(
        resume_folder
    ):

        old_path = os.path.join(
            resume_folder,
            old_file
        )

        if os.path.isfile(old_path):

            os.remove(old_path)


    # ======================================
    # Save uploaded resumes
    # ======================================

    for resume in resume_files:

        file_path = os.path.join(
            resume_folder,
            resume.name
        )

        with open(
            file_path,
            "wb"
        ) as file:

            file.write(
                resume.getbuffer()
            )


    # ======================================
    # Process resumes
    # ======================================

    with st.spinner(
        "Analyzing resumes... This may take some time."
    ):

        results = process_all_resumes(
            resume_folder,
            job_description
        )


    # ======================================
    # Check results
    # ======================================

    if not results:

        st.error(
            "No resumes could be processed."
        )

        st.stop()


    # ======================================
    # Save output
    # ======================================

    os.makedirs(
        "output",
        exist_ok=True
    )

    save_csv(
        results,
        "output/ranked_candidates.csv"
    )

    save_json(
        results,
        "output/ranked_candidates.json"
    )


    st.success(
        f"Successfully processed "
        f"{len(results)} resume(s)."
    )


    # ======================================
    # Results
    # ======================================

    st.header("3. Ranked Candidates")


    # Create table data

    table_data = []

    for rank, result in enumerate(
        results,
        start=1
    ):

        table_data.append({

            "Rank": rank,

            "Candidate":
                result["candidate"],

            "Final Score":
                f"{result['final_score']:.2f}%",

            "Skills":
                f"{result['skill_score']:.2f}%",

            "NLP":
                f"{result['similarity_score']:.2f}%",

            "Experience":
                f"{result['experience_score']:.2f}%",

            "Education":
                f"{result['education_score']:.2f}%",

            "AI":
                f"{result['ai_score']:.2f}%"
        })


    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )


    # ======================================
    # Candidate Details
    # ======================================

    st.header("4. Candidate Details")


    for rank, result in enumerate(
        results,
        start=1
    ):

        with st.expander(
            f"#{rank} - "
            f"{result['candidate']} - "
            f"{result['final_score']:.2f}%"
        ):

            col1, col2 = st.columns(2)


            with col1:

                st.subheader(
                    "Scores"
                )

                st.write(
                    f"**Final Score:** "
                    f"{result['final_score']:.2f}%"
                )

                st.write(
                    f"**Skill Match:** "
                    f"{result['skill_score']:.2f}%"
                )

                st.write(
                    f"**NLP Similarity:** "
                    f"{result['similarity_score']:.2f}%"
                )

                st.write(
                    f"**Experience:** "
                    f"{result['experience_score']:.2f}%"
                )

                st.write(
                    f"**Education:** "
                    f"{result['education_score']:.2f}%"
                )

                st.write(
                    f"**AI Score:** "
                    f"{result['ai_score']:.2f}%"
                )


            with col2:

                st.subheader(
                    "Skills"
                )

                st.write(
                    "**Matched Skills**"
                )

                for skill in result[
                    "matched_skills"
                ]:

                    st.write(
                        f"✅ {skill}"
                    )


                st.write(
                    "**Missing Skills**"
                )

                for skill in result[
                    "missing_skills"
                ]:

                    st.write(
                        f"❌ {skill}"
                    )


            st.subheader(
                "AI Recommendation"
            )

            st.write(
                result["recommendation"]
            )


            st.subheader(
                "Candidate Summary"
            )

            st.write(
                result["summary"]
            )


    # ======================================
    # Download Results
    # ======================================

    st.header("5. Download Results")


    with open(
        "output/ranked_candidates.csv",
        "rb"
    ) as file:

        st.download_button(
            label="⬇️ Download CSV",
            data=file,
            file_name="ranked_candidates.csv",
            mime="text/csv"
        )


    with open(
        "output/ranked_candidates.json",
        "rb"
    ) as file:

        st.download_button(
            label="⬇️ Download JSON",
            data=file,
            file_name="ranked_candidates.json",
            mime="application/json"
        )