import streamlit as st
from model import ResumeMatcher

# UI setup
st.set_page_config(page_title="AI Resume Matcher", layout="centered")

matcher = ResumeMatcher()

st.title("💼 AI Resume Matcher (Mini ATS System)")
st.write("Compare your resume with job descriptions using AI embeddings")

# Inputs
resume = st.text_area("📄 Paste Your Resume", height=200)
job = st.text_area("📌 Paste Job Description", height=200)

# Button
if st.button("Analyze Match 🚀"):
    if resume and job:
        score = matcher.compute_similarity(resume, job)

        st.subheader(f"🎯 Match Score: {score}%")

        if score > 80:
            st.success("Strong Match ✅")
        elif score > 50:
            st.warning("Moderate Match ⚠️")
        else:
            st.error("Weak Match ❌")
    else:
        st.warning("Please enter both resume and job description")
