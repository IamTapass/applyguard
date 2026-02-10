import streamlit as st

st.set_page_config(page_title="ApplyGuard")

st.title("🛡️ ApplyGuard")
st.write("Apply less. Apply right.")

st.file_uploader("Upload your resume (PDF)")
st.text_area("Paste Job Description")



