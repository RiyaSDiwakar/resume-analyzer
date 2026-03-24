COMMON_SKILLS = [
    "python", "java", "javascript", "flask", "django", "react",
    "sql", "html", "css", "machine learning", "nlp", "git",
    "rest api", "docker", "typescript", "pandas", "numpy",
    "scikit-learn", "spacy", "nltk", "postgresql", "mongodb"
]

def analyze_resume(resume_text, jd_text):
    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    # Keywords found in resume
    found_skills = [s for s in COMMON_SKILLS if s in resume_lower]
    
    # Keywords missing from resume
    missing_skills = [s for s in COMMON_SKILLS if s not in resume_lower]

    # JD matching — how many JD words appear in resume
    jd_words = set(jd_lower.split())
    resume_words = set(resume_lower.split())
    common = jd_words & resume_words
    jd_match = round((len(common) / len(jd_words)) * 100) if jd_words else 0

    # ATS score — simple rules
    ats_score = 0
    if len(resume_text) > 200: ats_score += 30
    if len(found_skills) >= 5:  ats_score += 40
    if jd_match >= 40:          ats_score += 30

    return {
        "found_skills": found_skills,
        "missing_skills": missing_skills[:8],
        "jd_match": jd_match,
        "ats_score": ats_score
    }