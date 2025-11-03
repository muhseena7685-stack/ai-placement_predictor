
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import shap
import os

os.makedirs('../models', exist_ok=True)

df = pd.read_csv('../data/students_synth.csv')

X = df.drop(['is_placed', 'placed_role', 'student_id'], axis=1)
y = df['is_placed']

encoders = {}
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, '../models/placement_rf.joblib')
joblib.dump(encoders, '../models/encoders.joblib')

print("✅ Model trained and saved successfully!")

# Optional: Explain model with SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_train)
shap.summary_plot(shap_values.values, X_train, show=False)

# Visualize feature importance
import matplotlib.pyplot as plt
import shap

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)
shap.summary_plot(shap_values, X_train, show=False)
plt.savefig('../models/shap_summary.png')
print("📈 Saved SHAP summary plot in /models folder")


