import re 

def extract_skills(text, skills_list):
    found_skills = []
    text_lower = text.lower()
    
    for skill in skills_list:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
            
    return found_skills

def calculate_score(resume_text, job_description, skills_list):
    resume_skills = extract_skills(resume_text, skills_list)
    job_skills = extract_skills(job_description, skills_list)
    
    matched = list(set(resume_skills) & set(job_skills))
    score = len(matched) / len(job_skills) * 100 if job_skills else 0
    
    return {
        "matched_skills": matched,
        "score": round(score, 2),
    }        