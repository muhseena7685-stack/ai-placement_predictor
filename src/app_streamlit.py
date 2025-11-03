import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- Load model and encoders safely ---
model_path = '../models/placement_rf.joblib'
encoders_path = '../models/encoders.joblib'

if not os.path.exists(model_path) or not os.path.exists(encoders_path):
    st.error("⚠️ Model or encoder files not found. Please ensure they are saved in '../models/' folder.")
    st.stop()

model = joblib.load(model_path)
encoders = joblib.load(encoders_path)

# --- App title ---
st.title("🎓 AI Placement Prediction App")
st.write("Predict placement outcomes for students — either as a student or a placement officer.")

# --- View selector ---
view = st.sidebar.selectbox("Select View", ["Student View", "Placement Officer View"])

# --- Student View ---
if view == "Student View":
    st.header("👩‍🎓 Student Placement Prediction")

    # Input fields for student
    branch = st.selectbox("Branch", ["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    year = st.number_input("Year of Study", min_value=1, max_value=4, step=1)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
    attendance_pct = st.number_input("Attendance (%)", min_value=0, max_value=100, step=1)
    aptitude_score = st.number_input("Aptitude Test Score", min_value=0, max_value=100, step=1)
    technical_score = st.number_input("Technical Test Score", min_value=0, max_value=100, step=1)
    communication_score = st.number_input("Communication Score", min_value=0, max_value=100, step=1)
    projects_count = st.number_input("No. of Projects", min_value=0, step=1)
    internships_count = st.number_input("No. of Internships", min_value=0, step=1)
    cert_count = st.number_input("No. of Certifications", min_value=0, step=1)
    extracurricular_score = st.number_input("Extracurricular Score", min_value=0, max_value=100, step=1)
    mock_interview_score = st.number_input("Mock Interview Score", min_value=0, max_value=100, step=1)
    softskill_rating = st.number_input("Soft Skill Rating (1–10)", min_value=1, max_value=10, step=1)

    # Create DataFrame
    data = pd.DataFrame([{
        "branch": branch,
        "gender": gender,
        "year": year,
        "cgpa": cgpa,
        "attendance_pct": attendance_pct,
        "aptitude_score": aptitude_score,
        "technical_score": technical_score,
        "communication_score": communication_score,
        "projects_count": projects_count,
        "internships_count": internships_count,
        "cert_count": cert_count,
        "extracurricular_score": extracurricular_score,
        "mock_interview_score": mock_interview_score,
        "softskill_rating": softskill_rating
    }])

    # Encode categorical columns safely
    for col in encoders:
        if col in data.columns:
            le = encoders[col]
            data[col] = data[col].apply(lambda x: x if x in le.classes_ else 'unknown')
            if 'unknown' not in le.classes_:
                le.classes_ = np.append(le.classes_, 'unknown')
            data[col] = le.transform(data[col])

    # Predict
    if st.button("🔮 Predict Placement Chance"):
        try:
            prediction = model.predict(data)[0]
            if prediction == 1:
                st.success("🎉 Congratulations! You are likely to be placed.")
            else:
                st.warning("⚠️ You might need to improve your skills to increase placement chances.")
        except Exception as e:
            st.error(f"Prediction Error: {e}")

elif view == "Placement Officer View":
    st.header("🏢 Placement Officer Portal")

    uploaded_file = st.file_uploader("Upload Student Data CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("✅ Uploaded Data Preview:")
        st.dataframe(df.head())

        # --- Drop columns not used during training ---
        expected_features = model.feature_names_in_ if hasattr(model, "feature_names_in_") else None
        if expected_features is not None:
            extra_cols = [col for col in df.columns if col not in expected_features]
            if extra_cols:
               print(f"Dropping unused columns: {extra_cols}")  # just logs silently in terminal
        df = df.drop(columns=extra_cols)

        # Encode categorical columns safely
        for col in encoders:
            if col in df.columns:
                le = encoders[col]
                df[col] = df[col].apply(lambda x: x if x in le.classes_ else 'unknown')
                if 'unknown' not in le.classes_:
                    le.classes_ = np.append(le.classes_, 'unknown')
                df[col] = le.transform(df[col])

        # Predict for all students
        try:
            df['placement_prediction'] = model.predict(df)
            df['placement_status'] = df['placement_prediction'].apply(lambda x: 'Placed' if x == 1 else 'Not Placed')

            st.subheader("📊 Placement Prediction Results:")
            st.dataframe(df[['placement_status'] + [col for col in df.columns if col not in ['placement_status', 'placement_prediction']]])

            # Option to download
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Results CSV", data=csv, file_name="placement_predictions.csv", mime='text/csv')

        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.info("📁 Please upload a student dataset in CSV format to see predictions.")
