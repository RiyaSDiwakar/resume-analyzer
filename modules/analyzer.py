from modules.parser import detect_sections

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

    # JD matching
    jd_words = set(jd_lower.split())
    resume_words = set(resume_lower.split())
    common = jd_words & resume_words
    jd_match = round((len(common) / len(jd_words)) * 100) if jd_words else 0

    # Section detection
    sections = detect_sections(resume_text)
    found_sections = [s for s, found in sections.items() if found]
    missing_sections = [s for s, found in sections.items() if not found]

    # ATS score — updated to include section score
    ats_score = 0
    if len(resume_text) > 200:  ats_score += 20
    if len(found_skills) >= 5:  ats_score += 30
    if jd_match >= 40:          ats_score += 20
    if sections["Education"]:   ats_score += 10
    if sections["Experience"]:  ats_score += 10
    if sections["Skills"]:      ats_score += 10

    return {
        "found_skills": found_skills,
        "missing_skills": missing_skills[:8],
        "jd_match": jd_match,
        "ats_score": ats_score,
        "found_sections": found_sections,
        "missing_sections": missing_sections
    }