import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from scorer import calculate_score
from skills import skills_list

st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("📄 AI-Powered Resume Screener")
st.markdown("Upload a PDF resume and compare it with a job description!")

# Job Description Input
job_desc = st.text_area("📝 Paste Job Description here")

# Resume Upload
uploaded_files = st.file_uploader("📤 Upload Resumes (PDF)", accept_multiple_files=True, type=["pdf"])

# Analyze Button
if st.button("🔍 Analyze Resumes"):

    if not job_desc:
        st.warning("Please enter a job description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        for uploaded_file in uploaded_files:
            with st.spinner(f"Analyzing {uploaded_file.name}..."):

                # Save temporarily
                temp_path = os.path.join("resumes", uploaded_file.name)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                resume_text = extract_text_from_pdf(temp_path)
                result = calculate_score(resume_text, job_desc, skills_list)

                # Display results
                st.subheader(f"📌 {uploaded_file.name}")
                st.write("✅ Matched Skills:", ", ".join(result["matched_skills"]))
                st.progress(int(result["score"]))
                st.info(f"⭐ Matching Score: {result['score']}%")
