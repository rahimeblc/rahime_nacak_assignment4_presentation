# 420-976-VA — Data Mining Project: Assignment 4 (A4)
## End-to-End MLOps Lifecycle Presentation (A1 – A3)

**Student Name:** Rahime Nacak (ID: 2134135)  
**Course:** LEA.EU — Artificial Intelligence & Data Science (Fall 2026)  
**Institution:** Vanier College  
**Repository:** [rahime_nacak_assignment4_presentation](https://github.com/rahimeblc/rahime_nacak_assignment4_presentation)

---

## 📌 Presentation Overview

This repository contains the comprehensive 18-slide final project presentation synthesized from **Assignments 1, 2, and 3** of the Data Mining Project course:

- **Part 1 — Model Training & Evaluation:** Dataset exploration, NLP preprocessing pipeline, Logistic Regression vs. XGBoost evaluation, and serialized model export.
- **Part 2 — API Deployment & Containerization:** Operationalizing an AG News Topic Classification REST service using FastAPI, Docker containerization, and public deployment on Render Cloud.
- **Part 3 — Versioning, Drift Analysis & Monitoring:** Dataset versioning (`mlflow.data`), statistical drift detection (Population Stability Index / PSI), MLflow Model Registry lifecycle governance, interactive Streamlit application, and real-time Grafana telemetry dashboards.

---

## 📂 Deliverables

| File | Description |
|---|---|
| [`A4_Presentation_Rahime_Nacak.pptx`](./A4_Presentation_Rahime_Nacak.pptx) | The master 18-slide PowerPoint presentation deck |
| [`generate_presentation.py`](./generate_presentation.py) | Python automation script to programmatically compile the entire slide deck |
| [`420-976-VA_A4_Project-Presentation.pdf`](./420-976-VA_A4_Project-Presentation.pdf) | Assignment 4 instructions and rubrics |
| `*.png` | High-resolution dashboard screenshots, confusion matrices, and drift comparison figures |

---

## 📑 Slide Structure (18 Slides)

1. **Cover / Title:** Vanier College, Project Title, Topic Navigation, Author Information
2. **Part 1 Divider:** Model Training & NLP Exploration
3. **Dataset Overview:** AG News 4-class benchmark (v1.0.0 balanced vs. v2.0.0 drifted)
4. **Preprocessing Pipeline:** Cleaning, TF-IDF vectorizer configuration, hyperparameter tuning table
5. **Model Training & Results:** Baseline benchmark (89.31%), drift evaluation (95.06%), retrained Model v2 (95.69%)
6. **Model Performance Verification:** Empirical comparison between Logistic Regression (88.50%) and XGBoost (82.25%)
7. **Part 2 Divider:** API Deployment & Container Architecture
8. **Deployment Architecture (Docker):** FastAPI REST architecture, service dependencies, readiness probes
9. **Interface for Model Invocation:** Interactive Swagger UI schemas (`POST /predict`, `GET /health`) and Streamlit inference panel
10. **Part 3 Divider:** Versioning, Dashboards & Monitoring
11. **MLflow Model Registry:** Staged model lifecycle (`Archived_Baseline` vs `Production`) and artifact tracking
12. **Streamlit Interactive UI:** Live prediction test bench, class probability distribution, latency meters
13. **Grafana Monitoring Dashboard:** Provisioned SQLite datasource, PSI drift indicators (0.1818), telemetry gauges
14. **Live Demo & Docker Quick Launch:** Direct service links and multi-container startup commands
15. **Key Insights & Recommendations:** Statistical drift impact, retraining effectiveness, and automated CI/CD triggers
16. **Limitations & Future Work:** Architectural constraints and planned production enhancements (Transformers, Cloud Run)
17. **AI Use Disclosure:** Academic integrity statement detailing learning and code assistance via Google Gemini
18. **Thank You & Q&A:** Closing slide and final discussion contact

---

## 🔗 Related Repositories & Live Services

- **A2 API Deployment Repository:** [rahimeblc/420-976-VA-A2-Deployment_Rahime_Nacak](https://github.com/rahimeblc/420-976-VA-A2-Deployment_Rahime_Nacak)
- **A3 MLOps & Dashboards Repository:** [rahimeblc/420-976-VA-A3-MLOps_Rahime_Nacak](https://github.com/rahimeblc/420-976-VA-A3-MLOps_Rahime_Nacak)
- **Live Public REST Service (Render):** [https://news-topic-classifier-rahime.onrender.com](https://news-topic-classifier-rahime.onrender.com)
- **Interactive Swagger Documentation:** [https://news-topic-classifier-rahime.onrender.com/docs](https://news-topic-classifier-rahime.onrender.com/docs)

---

## 🛠️ Regenerating the Presentation

To recompile or customize the presentation programmatically:

```bash
# 1. Install dependencies
pip install python-pptx

# 2. Run the compiler script
python generate_presentation.py
```

The compiled presentation will be output to `A4_Presentation_Rahime_Nacak.pptx`.
