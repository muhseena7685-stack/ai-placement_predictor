# src/dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Placement Insights Dashboard", layout="wide")

st.title("📊 Placement Insights Dashboard")

# Load data
df = pd.read_csv('../data/students_synth.csv')

# Basic Stats
st.subheader("Overall Placement Summary")
total = len(df)
placed = df['is_placed'].sum()
placement_rate = (placed / total) * 100

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", total)
col2.metric("Placed Students", placed)
col3.metric("Placement Rate", f"{placement_rate:.2f}%")

# Branch-wise placement
st.subheader("Branch-wise Placement Analysis")
branch_stats = df.groupby('branch')['is_placed'].mean().sort_values(ascending=False) * 100
fig1, ax1 = plt.subplots()
ax1.bar(branch_stats.index, branch_stats.values)
ax1.set_ylabel("Placement %")
ax1.set_xlabel("Branch")
st.pyplot(fig1)

# Correlation between CGPA and Placement
st.subheader("CGPA vs Placement")
fig2, ax2 = plt.subplots()
ax2.scatter(df['cgpa'], df['is_placed'], alpha=0.3)
ax2.set_xlabel("CGPA")
ax2.set_ylabel("Placement (1 = Yes, 0 = No)")
st.pyplot(fig2)

# Year-wise placement
st.subheader("Year-wise Placement Trend")
year_stats = df.groupby('year')['is_placed'].mean() * 100
fig3, ax3 = plt.subplots()
ax3.plot(year_stats.index, year_stats.values, marker='o')
ax3.set_xlabel("Year")
ax3.set_ylabel("Placement %")
st.pyplot(fig3)

st.success("✅ Dashboard Loaded Successfully!")