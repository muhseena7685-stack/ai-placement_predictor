# src/generate_data.py
import pandas as pd
import numpy as np
import random
import os

os.makedirs('../data', exist_ok=True)

np.random.seed(42)
N = 1000
branches = ['CS','IT','EC','ME','CE']
roles = ['SDE','Data Analyst','IT Support','QA','DevOps']

rows = []
for i in range(N):
    sid = "S"+str(i+1).zfill(4)
    branch = random.choice(branches)
    year = random.choice([2,3,4])
    cgpa = round(np.clip(np.random.normal(7.5, 1.0), 4.0, 10.0), 2)
    attendance = int(np.clip(np.random.normal(85,10), 50, 100))
    aptitude = int(np.clip(np.random.normal(65 + (cgpa-7)*5, 15), 20, 100))
    technical = int(np.clip(np.random.normal(65 + (cgpa-7)*6, 18), 20, 100))
    communication = int(np.clip(np.random.normal(60 + (technical-65)*0.2, 15), 20, 100))
    projects = np.random.poisson(1.2)
    internships = np.random.binomial(1, 0.25)
    cert_count = np.random.poisson(1.0)
    extracurricular = int(np.clip(np.random.normal(60, 20), 0, 100))
    mock = int(np.clip(np.random.normal((technical+communication)/2, 12), 20, 100))
    softskill_rating = int(np.clip(np.random.normal((communication+extracurricular)/2, 10), 20, 100))

    score = 0.35*cgpa + 0.15*(aptitude/10) + 0.2*(technical/10) + 0.15*(communication/10) + 0.1*(internships*10) + 0.05*(projects*5)
    prob = 1/(1+np.exp(- (score - 6.5)))
    is_placed = np.random.rand() < prob
    placed_role = random.choice(roles) if is_placed else "NA"

    rows.append([
        sid, branch, 'M' if random.random()<0.6 else 'F', year, cgpa, attendance,
        aptitude, technical, communication, projects, internships, cert_count,
        extracurricular, mock, softskill_rating, int(is_placed), placed_role
    ])

df = pd.DataFrame(rows, columns=[
    'student_id','branch','gender','year','cgpa','attendance_pct',
    'aptitude_score','technical_score','communication_score',
    'projects_count','internships_count','cert_count','extracurricular_score',
    'mock_interview_score','softskill_rating','is_placed','placed_role'
])

df.to_csv('../data/students_synth.csv', index=False)
print("✅ Saved ../data/students_synth.csv with", len(df), "rows")