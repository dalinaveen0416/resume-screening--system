import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Resume Screening", layout="wide")
st.title("🚀 AI Resume Screening System")


left_col, right_col = st.columns([1, 2])

with left_col:
    st.header("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"]
    )

    if uploaded_file:
        with st.spinner("Uploading resume..."):
            response = requests.post(
                f"{API_URL}/upload_resume",
                files={"file": uploaded_file}
            )

        if response.status_code == 200:
            st.success("Resume uploaded successfully!")
        else:
            st.error("Upload failed.")
            st.write(response.json())

with right_col:
    st.header("📝 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=220
    )

    col1, col2 = st.columns(2)

    with col1:
        evaluate_clicked = st.button(
            "Evaluate",
            use_container_width=True
        )

    with col2:
        rank_clicked = st.button(
            "Rank",
            use_container_width=True
        )

    if evaluate_clicked:

        if not job_description.strip():
            st.warning("Please enter job description.")
        else:
            with st.spinner("Evaluating resumes..."):
                response = requests.post(
                    f"{API_URL}/evaluate_resume",
                    json={"job_description": job_description}
                )

            if response.status_code == 200:
                data = response.json()

                st.subheader("AI Evaluation Results")

                for item in data.get("evaluations", []):
                    with st.container():
                        st.markdown(f"### 📄 {item['resume']}")
                        st.write(item["analysis"])
                        st.divider()
            else:
                st.error("Evaluation failed.")
                st.write(response.json())

    if rank_clicked:

        if not job_description.strip():
            st.warning("Please enter job description.")
        else:
            with st.spinner("Ranking resumes..."):
                response = requests.post(
                    f"{API_URL}/rank",
                    json={"job_description": job_description}
                )

            if response.status_code == 200:
                data = response.json()

                st.subheader("Ranking Results")

                for idx, item in enumerate(data.get("rankings", []), 1):

                    with st.container():

                        st.markdown(f"### {idx}. 📄 {item['resume']}")

                        # Score progress bar
                        st.progress(float(item["score"]))

                        # Status
                        status = item.get("status")

                        if status == "Shortlist":
                            st.success("Status: Shortlisted")
                        elif status == "Reject":
                            st.error("Status: Rejected")

                        st.write(f"Score: {item['score']:.4f}")
                        st.divider()

            else:
                st.error("Ranking failed.")
                st.write(response.json())
