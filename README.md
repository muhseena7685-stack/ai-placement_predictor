# 🎓 AI Placement Predictor

This project predicts a student's placement chances using Machine Learning.  
It analyzes academic, technical, and soft skill data to estimate whether a student is likely to be placed.

---

## 🚀 Features
- Student and Placement Officer views
- Random Forest–based prediction model
- Interactive Streamlit web interface
- Encoded feature preprocessing with LabelEncoder
- SHAP-based explainability (feature importance)

---

## 🧠 Tech Stack
- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- Joblib
- SHAP

---

## 📊 Dataset Fields
| Field | Description |
|--------|-------------|
| `branch` | Student's branch (CSE, ECE, etc.) |
| `cgpa` | Cumulative Grade Point Average |
| `aptitude_score` | Aptitude test score |
| `technical_score` | Technical test score |
| `communication_score` | Communication skill score |
| ... | (Add more if needed) |

---

## 🧰 How to Run
```bash
# Clone the repo
git clone https://github.com/muhseena7685-stack/ai-placement_predictor.git

# Navigate to folder
cd ai-placement_predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run src/app_streamlit.py
