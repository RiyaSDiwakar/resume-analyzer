import pdfplumber
import re

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

def detect_sections(text):
    sections = {
        "Education": False,
        "Experience": False,
        "Skills": False,
        "Projects": False,
        "Summary": False,
        "Certifications": False
    }

    keywords = {
        "Education": ["education", "academic", "qualification", "degree", "university", "college"],
        "Experience": ["experience", "work history", "employment", "internship", "job"],
        "Skills": ["skills", "technical skills", "technologies", "tools", "competencies"],
        "Projects": ["projects", "personal projects", "academic projects", "portfolio"],
        "Summary": ["summary", "objective", "about me", "profile", "overview"],
        "Certifications": ["certification", "certifications", "courses", "achievements", "awards"]
    }

    text_lower = text.lower()

    for section, words in keywords.items():
        for word in words:
            if word in text_lower:
                sections[section] = True
                break

    return sections