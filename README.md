                                      ------------ AI Resume Screening Agent---------------

<!-- About the Project -->

This project is an AI-based Resume Screening Agent that helps in the initial screening of candidates.

Normally, a recruiter has to open and check each resume against a Job Description. If there are many resumes, this can take a lot of time.

This project automates that first step.

The application takes a **Job Description and multiple resumes**, analyzes them, calculates a score for each candidate, and ranks the candidates from highest to lowest.

The main goal was to build a simple, practical AI agent that can actually process resumes from start to finish.

-------------------------------------------------

<!-- What the Agent Does -->

The agent follows this process:

Job Description + Resumes
          ↓
Read and extract resume details
          ↓
Compare candidate skills with the job requirements
          ↓
Check how closely the resume matches the job description
          ↓
Evaluate experience and education
          ↓
Use AI to understand the candidate's profile
          ↓
Calculate an overall score
          ↓
Rank candidates from highest to lowest
          ↓
Generate the final results
          ↓
CSV / JSON output


The project also includes a **Streamlit web interface**, so the user does not have to run everything from the terminal.

-------------------------------------------------

<!-- Main Features -->

* Upload a Job Description
* Upload multiple resumes at once
* Supports PDF, DOCX, and TXT resumes
* Extracts text from resumes
* Matches candidate skills with required skills
* Calculates TF-IDF similarity
* Uses cosine similarity to compare resumes with the JD
* Checks basic experience information
* Checks education information
* Uses a Groq LLM for candidate analysis
* Calculates an overall candidate score
* Automatically ranks candidates
* Processes 10+ resumes in a single run
* Shows results through a Streamlit UI
* Generates CSV output
* Generates JSON output
* Shows matched and missing skills
* Provides an AI-generated candidate recommendation

-------------------------------------------------

<!-- Technologies Used -->

<!-- Programming Language -->

* Python 3.13

<!-- AI -->

* Groq API
* Llama model

 <!-- NLP -->

* Scikit-learn
* TF-IDF
* Cosine Similarity

 <!-- Resume Processing -->

* PyPDF
* python-docx

<!-- Web Interface -->

* Streamlit

<!-- Other Libraries -->

* Pandas
* python-dotenv

-------------------------------------------------

<!-- Project Structure -->

ResumeScreeningAgent/
│
├── app.py                         # Streamlit web interface
│
├── data/
│   └── job_description.txt        # Job description used for screening
│
├── resumes/                       # Candidate resumes
│   ├── candidate_01.pdf
│   ├── candidate_02.pdf
│   └── ...
│
├── output/                        # Generated screening results
│   ├── ranked_candidates.csv
│   └── ranked_candidates.json
│
├── src/                           # Main application code
│   ├── __init__.py
│   ├── main.py                    # Runs the screening from terminal
│   ├── parser.py                  # Extracts text from resumes
│   ├── scorer.py                  # Calculates NLP similarity
│   ├── skill_matcher.py           # Compares required and candidate skills
│   ├── candidate_analyzer.py      # Analyzes experience and education
│   ├── ai_agent.py                # Handles AI-based candidate analysis
│   ├── final_scorer.py            # Calculates the final candidate score
│   ├── batch_processor.py         # Processes multiple resumes
│   └── output_generator.py        # Creates CSV and JSON results
│
├── .env                           # Stores the Groq API key
├── .gitignore                     # Files that should not be uploaded
├── requirements.txt               # Required Python packages
├── README.md                      # Project documentation
└── venv/                          # Python virtual environment (local only)

-------------------------------------------------

<!-- How the Scoring Works -->

I did not want the final result to depend completely on the AI model.

Instead, the project combines different scoring methods.

| Factor         |   Weight |
| -------------- | -------: |
| Skill Match    |      40% |
| NLP Similarity |      20% |
| Experience     |      20% |
| Education      |      10% |
| AI Evaluation  |      10% |
| **Total**      | **100%** |

For example, if a candidate gets:

```text
Skill Match       = 90
NLP Similarity    = 80
Experience        = 90
Education         = 100
AI Score          = 85
```

the final score is calculated using the above weights.

This makes the ranking easier to understand instead of simply trusting an AI-generated score.

-------------------------------------------------

<!-- NLP Similarity -->

For the text comparison, I used **TF-IDF and Cosine Similarity**.

The Job Description and resume are converted into numerical vectors using TF-IDF.

Cosine similarity is then used to measure how similar the resume is to the Job Description.

For example:

```text
Job Description
       ↓
     TF-IDF
       ↓
Text Vector
       ↓
Cosine Similarity
       ↑
Text Vector
       ↑
     TF-IDF
       ↑
Resume
```

A higher similarity score means that the resume text is more closely related to the Job Description.

-------------------------------------------------

<!-- Skill Matching -->

The system also checks the skills mentioned in the Job Description against the skills found in the resume.

For example:

```text
Required:

Java
JDBC
MySQL
REST APIs
Git
```

If the candidate has:

```text
Java
JDBC
MySQL
Git
```

the system can show:

```text
Matched Skills:

Java
JDBC
MySQL
Git

Missing Skills:

REST APIs
```

This gives more useful information than using text similarity alone.

-------------------------------------------------

<!-- AI Evaluation -->

The project uses the Groq API with a Llama model to analyze the candidate.

The AI is asked to provide information such as:

* Candidate summary
* Relevant experience
* Education
* Strengths
* Skill gaps
* Recommendation
* AI score

The AI is mainly used for understanding and explaining the resume.

The other scoring components are calculated separately.

This was done to reduce the risk of depending completely on an LLM for candidate ranking.

-------------------------------------------------

<!-- Setting Up the Project -->

<!-- 1. Open the project folder -->

```bash
cd ResumeScreeningAgent
```

<!-- 2. Create a virtual environment -->

This is only required when setting up the project for the first time.

```bash
python -m venv venv
```

<!-- 3. Activate the environment -->

On Windows:

```bash
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

<!-- Install dependencies -->

```bash
python -m pip install -r requirements.txt
```

-------------------------------------------------

 <!-- Groq API Key -->

The project uses a Groq API key.

Create a `.env` file in the main project folder:

```text
GROQ_API_KEY=your_groq_api_key
```

For example:

```text
ResumeScreeningAgent/
│
├── .env
├── app.py
├── README.md
└── ...
```

The `.env` file contains the API key and should **not be uploaded to GitHub**.

-------------------------------------------------

<!-- Adding a Job Description -->

The project can use:

```text
data/job_description.txt
```

For example:

```text
Job Title: Junior Java Developer

Experience: 0–2 years

Required Skills:
Java
JDBC
SQL
MySQL
Git
Data Structures
Algorithms

Good to Have:
Spring MVC
Spring Boot
REST APIs
HTML
CSS
JavaScript
```

The Streamlit interface also allows the user to upload the Job Description.

-------------------------------------------------

<!-- Adding Resumes -->

Resumes can be placed inside:

```text
resumes/
```

Supported formats:

```text
PDF
DOCX
TXT
```

Example:

```text
resumes/
├── candidate_01.pdf
├── candidate_02.pdf
├── candidate_03.pdf
├── candidate_04.docx
└── candidate_05.txt
```

The application can process multiple resumes in one run.

-------------------------------------------------

<!-- Running the Project -->

<!-- Option 1 — Streamlit UI -->

This is the main way to use the application.

First activate the environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local address such as:

```text
http://localhost:8501
```

Open that address in a browser.

The UI allows the user to:

1. Upload the Job Description
2. Upload multiple resumes
3. Click **Screen Resumes**
4. View the ranked candidates
5. View individual candidate details
6. Download CSV results
7. Download JSON results

-------------------------------------------------

<!-- Option 2 — Run from Terminal -->

The project can also be tested without the Streamlit interface.

Run:

```bash
python src/main.py
```

This processes the resumes in the `resumes` folder and displays the ranking in the terminal.

-------------------------------------------------

<!-- Output -->

After processing the resumes, the application creates:

```text
output/
├── ranked_candidates.csv
└── ranked_candidates.json
```

The CSV contains information such as:

```text
Rank
Candidate
Final Score
Skill Score
NLP Similarity
Experience Score
Education Score
AI Score
Matched Skills
Missing Skills
Recommendation
```

The JSON file contains the same information in a structured format.

-------------------------------------------------

<!-- Example Result -->

A result may look like:

```text
Rank  Candidate       Final Score
----------------------------------
1     Candidate_04    91.40%
2     Candidate_07    87.80%
3     Candidate_01    84.60%
4     Candidate_08    81.20%
```

The actual score depends on the Job Description and the resumes being screened.

-------------------------------------------------

<!-- Why I Used This Approach -->

I wanted the project to be simple enough to understand but still show how an AI agent can be used in a real-world task.

Instead of using only an LLM, I combined:

```text
NLP
+
Skill Matching
+
Rule-based Analysis
+
LLM
```

This gives a more explainable result.

The LLM is useful for understanding and summarizing the candidate, while the scoring system handles the measurable parts of the ranking.

-------------------------------------------------

<!-- Limitations -->

There are some limitations to the current version.

* Resume quality can affect the results.
* Different ways of writing the same skill may not always be recognized.
* The experience calculation is currently basic.
* AI-generated scores can vary.
* The system should not be used as the only decision-maker in recruitment.
* A recruiter should review the final candidates before making a hiring decision.

This project is mainly intended for **initial resume screening**.

-------------------------------------------------

<!-- Future Improvements -->

Some improvements I would like to add in the future:

* Better semantic similarity using embeddings
* More accurate experience calculation
* Better skill recognition
* Support for more resume formats
* Candidate comparison charts
* Better handling of synonyms
* Vector database for larger numbers of resumes
* More advanced recruiter dashboard
* Improved AI evaluation

-------------------------------------------------

<!-- Project Status -->

The current project includes:

```text
[x] Project setup
[x] Virtual environment
[x] Groq API integration
[x] Resume parsing
[x] Job Description processing
[x] Skill matching
[x] TF-IDF similarity
[x] Cosine similarity
[x] Experience analysis
[x] Education analysis
[x] AI candidate analysis
[x] Final scoring
[x] Multiple resume processing
[x] Candidate ranking
[x] CSV output
[x] JSON output
[x] Streamlit UI
[ ] Final testing with 10+ resumes
[ ] Final README update with test results
```

-------------------------------------------------

<!-- What I Learned -->

While building this project, I worked with:

* Python project structure
* Virtual environments
* API integration
* LLM prompting
* Resume parsing
* NLP text similarity
* TF-IDF
* Cosine similarity
* File handling
* JSON and CSV generation
* Batch processing
* Streamlit
* Combining traditional programming with AI

The main thing I learned is that an AI agent does not necessarily need to be a complicated system. It can be built by connecting an AI model with useful tools, data processing, and a clear workflow.

-------------------------------------------------

<!-- Author -->

Chethan G

This project was created as an AI Agent challenge project focused on building a practical end-to-end Resume Screening Agent.
