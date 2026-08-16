# AI Analytics Copilot

An AI-powered analytics platform that automatically profiles, cleans, analyzes, visualizes, and interprets structured datasets.

## Project Goal

Build a placement-ready Data Analytics + Machine Learning + Generative AI application by **August 27, 2026**.

### Core Pipeline

```text
CSV / Excel
    ↓
Upload
    ↓
Data Profiling
    ↓
Data Cleaning
    ↓
Automated EDA
    ↓
Visualization
    ↓
Machine Learning
    ↓
AI Insights
    ↓
Business Recommendations
    ↓
Ask Your Data
```

---

# Current Progress

## Day 1 — Project Setup ✅
- Created project on D: drive
- Created Python virtual environment
- Set up Flask
- Created basic frontend
- Created project structure
- Verified Flask application locally

## Day 2 — Dataset Upload ✅
- CSV upload
- Excel upload
- File storage in `uploads/`
- Pandas DataFrame creation
- Dataset preview

## Day 3 — Dataset Profiling ✅
- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Numerical columns
- Categorical columns

Created:
```text
analysis/profile.py
```

## Day 4 — Data Cleaning ✅
- Duplicate row removal
- Missing-value detection
- Numerical missing values → median
- Categorical missing values → mode
- Cleaning report
- Cleaned DataFrame

Created:
```text
analysis/cleaning.py
```

## Day 5 — Automated EDA ✅
- Statistical summary
- Numerical column analysis
- Categorical column analysis
- Unique-value analysis
- Most-common categorical values
- Correlation matrix

Created/updated:
```text
analysis/statistics.py
analysis/eda.py
```

---

# Current Project Structure

```text
AI-Analytics/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── analysis/
│   ├── profile.py
│   ├── cleaning.py
│   ├── statistics.py
│   └── eda.py
│
├── uploads/
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── dashboard_backup.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── venv/
```

> `venv/` and uploaded datasets should not be pushed to GitHub.

---

# Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Plotly
- HTML
- CSS
- JavaScript
- SQL / SQLite
- Generative AI / LLM API
- Git & GitHub

---

# Team Division

## Person A — Backend / Data / ML
- Flask backend
- Pandas
- Data profiling
- Data cleaning
- Statistics
- EDA
- Machine Learning
- AI integration
- Database logic

## Person B — Frontend / Visualization / Deployment
- HTML
- CSS
- JavaScript
- Dashboard UI
- Plotly presentation
- Frontend integration
- Deployment
- UI improvements

Both members should understand the complete project before the final presentation.

---

# Upcoming Roadmap

## Day 6 — Automatic Visualization
Build a Plotly visualization engine that automatically chooses charts based on column types.

```text
Numerical
    ├── Histogram
    ├── Box Plot
    └── Scatter Plot

Categorical
    └── Bar Chart

Date
    └── Line Chart
```

## Day 7 — Dashboard V1
Combine:
- Dataset summary
- Data quality
- KPIs
- EDA
- Visualizations
- Basic filters

Milestone:

```text
Upload → Clean → Analyze → Visualize
```

## Day 8–9 — Machine Learning
Start with one useful prediction task.

Initial planned model:
```text
RandomForestRegressor
```

Evaluate using:
- R²
- MAE
- RMSE

## Day 10–11 — AI Integration

Use the LLM to interpret verified analytical results.

```text
Dataset
   ↓
Python/Pandas Analysis
   ↓
Verified Results
   ↓
LLM
   ↓
Natural-Language Insights
```

## Day 12 — AI Recommendations
Generate:
- Key insights
- Trends
- Business recommendations
- Potential areas of concern

## Day 13 — Ask Your Data
Support questions such as:
- Which region has the highest profit?
- Which product generated the most revenue?
- What is the average order value?
- Which category should we focus on?

The system should calculate actual results using Python/Pandas and then use AI to explain them.

## Day 14 — Full UI Integration
Integrate:
- Backend
- Analytics
- Charts
- ML
- AI
- Dashboard

## Day 15 — Testing & Deployment
Test:
- CSV
- Excel
- Missing values
- Duplicates
- Numerical-only datasets
- Categorical datasets
- Invalid files
- ML
- AI

Then deploy.

## Day 16 — Finalization
Prepare:
- GitHub README
- Screenshots
- Architecture diagram
- Presentation
- Demo
- Resume description

---

# Git Workflow

Because this is a two-person project, both contributors should keep the repository synchronized.

### Before starting work

```bash
git pull --rebase origin main
```

### After completing work

```bash
git status
git add .
git commit -m "Describe your changes"
git push origin main
```

Example:

```bash
git add .
git commit -m "Day 4-5: data cleaning and EDA"
git push origin main
```

Do not use:

```bash
git push --force
```

unless the team explicitly decides to rewrite repository history.

---

# Important Project Rules

### Working > Fancy
Prioritize a complete working MVP over unnecessary features.

### Understanding > Copy-Pasting
Every team member should understand the code they present in an interview.

### Reliable AI > Random AI
AI should interpret verified analytics rather than invent numerical results.

### Complete MVP > Too Many Features
Do not add unnecessary technologies such as React, microservices, or custom LLM training.

---

# Placement Value

The final project should demonstrate:

- Python
- Pandas
- Data Cleaning
- EDA
- Statistics
- Data Visualization
- Machine Learning
- Model Evaluation
- Generative AI
- Prompt Design
- AI Reliability
- Flask
- APIs
- SQL
- Git/GitHub
- Deployment

---

# Planned Resume Description

### AI Analytics Copilot

**Python, Pandas, Scikit-learn, Flask, SQL, Plotly, GenAI**

> Developed an AI-powered analytics platform that automatically profiles, cleans, visualizes, and analyzes structured datasets, generates ML-based predictions, and converts analytical findings into natural-language business insights and recommendations.

---

# Current Milestone

```text
Day 1  ✅ Project Setup
Day 2  ✅ Dataset Upload
Day 3  ✅ Dataset Profiling
Day 4  ✅ Data Cleaning
Day 5  ✅ Automated EDA
Day 6  ⏳ Automatic Visualization
Day 7  ⏳ Dashboard V1
...
Day 16 ⏳ Final Deployment & Presentation
```

---

# Final Product Vision

```text
Upload Dataset
      ↓
Automatic Data Quality Report
      ↓
Automatic EDA
      ↓
Interactive Visualizations
      ↓
ML Prediction
      ↓
AI Insights
      ↓
Business Recommendations
      ↓
Ask Questions About Your Data
```

The target is a **working, deployable, explainable AI + Data Analytics project that can be confidently demonstrated and defended in placement interviews.**
