# 10-Minute Presentation Script (Oral Defense & Presentation)
**Course:** 420-976-VA — Data Mining Project (Fall 2026)  
**Institution:** Vanier College, Montreal  
**Presenter:** Rahime Nacak (Student ID: 2134135)  
**Project:** AG News Topic Classification — End-to-End MLOps Lifecycle Pipeline  
**Target Duration:** 10 to 11 Minutes (Targeting 10–12 Minute Course Requirement)  
**GitHub Repository:** [rahimeblc/rahime_nacak_assignment4_presentation](https://github.com/rahimeblc/rahime_nacak_assignment4_presentation)

---

## ⏱️ Timing Roadmap

| Section | Slides | Allocated Time | Cumulative Time |
|---|---|---|---|
| **Introduction & Overview** | Slide 1–2 | 1 min 00 s | 0:00 – 1:00 |
| **Part 1: Model Training & Evaluation** | Slide 3–6 | 3 min 00 s | 1:00 – 4:00 |
| **Part 2: API Deployment & Containerization** | Slide 7–9 | 1 min 50 s | 4:00 – 5:50 |
| **Part 3: Versioning, Drift & Monitoring** | Slide 10–13 | 2 min 40 s | 5:50 – 8:30 |
| **Live Demo, Insights & Governance** | Slide 14–15 | 1 min 30 s | 8:30 – 10:00 |
| **Limitations, Ethics Disclosure & Q&A** | Slide 16–18 | 1 min 00 s | 10:00 – 11:00 |

---

## 🎙️ Slide-by-Slide Spoken Script

### Slide 1: Title & Cover
**Duration:** 0:00 – 0:40 (40 seconds)  
**Visual:** Cover slide with project title, author, and GitHub link.

> *"Good morning, Professor and fellow colleagues. My name is Rahime Nacak, and today I am excited to present my final Data Mining Capstone Project for course 420-976-VA at Vanier College.*
> 
> *Our project is titled **AG News Topic Classification: An End-to-End MLOps Lifecycle Pipeline**.*
> 
> *Over the past semester, we progressed from training and cross-validating natural language models in Assignment 1, to containerizing and serving real-time REST predictions in Assignment 2, and ultimately building an enterprise-grade observability, drift monitoring, and model governance stack in Assignment 3. Today, I will walk you through each phase of this engineering journey, demonstrate our live services, and share key production insights."*

---

### Slide 2: Part 1 Section Divider
**Duration:** 0:40 – 1:00 (20 seconds)  
**Visual:** Part 1 divider with agenda bullets.

> *"We begin with **Part 1: Model Training**.*
> 
> *In this initial phase, our primary objective was to build a robust, reproducible natural language processing pipeline capable of categorizing incoming news text into four distinct topics, while rigorously establishing an empirical baseline for subsequent deployment."*

---

### Slide 3: Dataset Overview
**Duration:** 1:00 – 1:45 (45 seconds)  
**Visual:** Side-by-side cards comparing Dataset v1.0.0 and Dataset v2.0.0.

> *"To establish our machine learning foundation, we utilized the AG News benchmark corpus.*
> 
> *As shown on the left, our **Dataset v1.0.0** comprises eight thousand samples strictly balanced across four uniform categories: World, Sports, Business, and Sci/Tech—exactly two thousand articles per class.*
> 
> *However, production NLP systems rarely encounter static data. To simulate real-world data evolution, we constructed **Dataset v2.0.0** as an evaluation corpus for covariate shift. Here, we injected contemporary technological concepts like Generative AI, LLMs, and Cloud GPUs, alongside business shifts like Crypto Regulation.*
> 
> *Furthermore, we introduced class imbalance, increasing Sci/Tech to forty percent and Business to thirty percent, while reducing Sports and World to fifteen percent each. Both versions were tracked with cryptographically secure SHA-256 digest hashing through MLflow Data for complete auditing."*

---

### Slide 4: Preprocessing Pipeline & Hyperparameter Tuning
**Duration:** 1:45 – 2:30 (45 seconds)  
**Visual:** 5-stage pipeline diagram and parameter tuning comparison table.

> *"Turning to text preprocessing, our pipeline follows five clean stages: raw news ingestion, token cleaning—which removes HTML tags, URLs, and punctuation—followed by NLTK English stopword removal and Porter Stemming.*
> 
> *The cleaned tokens are then transformed using a TF-IDF vectorizer before entering our classifier.*
> 
> *The table below highlights our hyperparameter evolution. For our baseline Model v1, we configured five thousand TF-IDF features with unigram and bigram ranges and standard L-BFGS regularization at C equals one point zero.*
> 
> *When addressing data drift in Model v2, we expanded our feature space to eight thousand n-grams including trigrams, enabled sublinear term frequency to temper extreme word counts, adjusted regularization to C equals two point five, and applied balanced class weighting to handle the newly skewed distribution."*

---

### Slide 5: Model Training & Results (MLflow Experiments)
**Duration:** 2:30 – 3:15 (45 seconds)  
**Visual:** 3 scenario cards (89.31%, 95.06%, 95.69%) and MLflow summary table.

> *"Here we examine the training results tracked systematically in MLflow.*
> 
> *Our baseline **Model v1** achieved an initial accuracy of **89.31%** and an F1-score of **89.26%** on held-out test data.*
> 
> *When we subjected this baseline model to the shifted vocabulary of Dataset v2, we observed significant covariate impact. While accuracy registered at **95.06%** due to class concentration in dominant topics, the model exhibited class confusion on low-frequency classes.*
> 
> *By retraining our pipeline with expanded n-grams and balanced class weights, **Model v2** achieved a top accuracy of **95.69%** and a macro F1-score of **95.41%**, demonstrating successful adaptation to newly emerging industry terminology."*

---

### Slide 6: Model Performance Verification (LR vs. XGBoost)
**Duration:** 3:15 – 4:00 (45 seconds)  
**Visual:** Validation/Test comparison cards between Logistic Regression and XGBoost.

> *"An essential component of Assignment 1 was cross-verifying whether an advanced ensemble classifier would outperform our linear baseline.*
> 
> *As cross-referenced directly from our notebook execution, our Logistic Regression model scored **88.33%** validation accuracy and **88.50%** final test accuracy.*
> 
> *In contrast, our tuned XGBoost classifier achieved **82.25%** validation accuracy.*
> 
> *Empirically, Logistic Regression outperformed XGBoost by **six point zero eight percent**. This is a well-documented phenomenon in NLP: high-dimensional sparse TF-IDF matrices naturally favor linear hyperplanes over orthogonal decision tree splits. Furthermore, linear models execute inference in under a quarter of a millisecond with a tiny memory footprint. Consequently, Logistic Regression was selected as our baseline production engine."*

---

### Slide 7: Part 2 Section Divider
**Duration:** 4:00 – 4:20 (20 seconds)  
**Visual:** Part 2 divider (API Deployment).

> *"Next, in **Part 2**, we transitioned from offline experimentation to production serving: **API Deployment & Containerization**.*
> 
> *The goal here was to package our serialized model pipeline into a stateless, high-throughput microservice accessible via standard HTTP protocols."*

---

### Slide 8: Deployment Architecture (Docker & FastAPI)
**Duration:** 4:20 – 5:05 (45 seconds)  
**Visual:** Multi-service block diagram and docker-compose snippet.

> *"Our deployment architecture leverages FastAPI running on an asynchronous Uvicorn server, packaged within a lightweight Docker container.*
> 
> *As illustrated in the diagram, client applications submit inference requests over port 8000.*
> 
> *Crucially, our serialized pipeline—weighing just **339 kilobytes**—is loaded strictly once into memory during application startup rather than per request, guaranteeing microsecond response times.*
> 
> *The service exposes health check probes to support container orchestrators like Kubernetes or Docker Compose, rejecting unverified payloads with standard HTTP 422 codes while enforcing schema validation across all endpoints."*

---

### Slide 9: Interface for Model Invocation
**Duration:** 5:05 – 5:50 (45 seconds)  
**Visual:** FastAPI Swagger UI schema contracts and Streamlit live prediction window.

> *"On Slide 9, you can see our live API contracts.*
> 
> *On the left, the interactive Swagger UI at `/docs` defines our `POST /predict` endpoint. Clients submit a clean JSON payload containing the article text, and receive a comprehensive response including the predicted category—such as Sci/Tech—an exact confidence score of eighty-nine point nine percent, and the full multi-class probability distribution.*
> 
> *On the right, we display our Streamlit prediction interface, where users can toggle active model versions in real time, view confidence progress bars, and observe per-sample inference latencies of just zero point two milliseconds."*

---

### Slide 10: Part 3 Section Divider
**Duration:** 5:50 – 6:10 (20 seconds)  
**Visual:** Part 3 divider (Versioning & Monitoring).

> *"This brings us to **Part 3: Versioning, Dashboards & Monitoring**.*
> 
> *Deploying a model is only day one of MLOps. To keep a system reliable in production, we require structured lifecycle governance and automated observability."*

---

### Slide 11: MLflow Model Registry
**Duration:** 6:10 – 7:00 (50 seconds)  
**Visual:** 5-step lifecycle protocol and MLflow UI screenshot.

> *"Slide 11 illustrates our model governance workflow managed through the MLflow Model Registry.*
> 
> *Every experiment run captures parameters, execution signatures, and evaluation metrics.*
> 
> *When a model satisfies our accuracy and latency gates, it is registered under `AGNews-TopicClassifier`.*
> 
> *Through stage tagging, Model v1 was transitioned to `Archived_Baseline`, while the retrained Model v2 was promoted directly into `Production`.*
> 
> *This guarantees clear audit trails: any consumer service can query the registry to load the verified production artifact without downtime or configuration drift."*

---

### Slide 12: Streamlit Dashboard Visuals
**Duration:** 7:00 – 7:45 (45 seconds)  
**Visual:** Streamlit UI screenshot and feature breakdown.

> *"Our Streamlit application running on port 8501 acts as our operational user cockpit.*
> 
> *It features four dedicated tabs:*
> * *Tab 1 explores dataset class balances and character length distributions.*
> * *Tab 2 provides interactive model serving, allowing operators to type custom headlines and observe real-time predictions.*
> * *Tab 3 displays multi-metric radar plots comparing precision, recall, and F1 across model iterations.*
> * *And Tab 4 queries our persistent SQLite database to display historical inference audit trails."*

---

### Slide 13: Grafana Monitoring Visuals
**Duration:** 7:45 – 8:30 (45 seconds)  
**Visual:** Live Grafana dashboard screenshot with gauges (95.7%, 0.182 PSI, 0.470ms).

> *"For real-time telemetry, we deployed a containerized Grafana dashboard on port 3005, backed by an automated SQLite datasource.*
> 
> *As verified by the live screenshot on the right, Grafana monitors three vital signals:*
> 1. *First, accuracy gauges show Production Model v2 operating at **95.7%**.*
> 2. *Second, our Population Stability Index gauge reads **0.182**, alerting engineers to moderate distribution drift between v1 and v2.*
> 3. *Third, inference latency telemetry averages zero point four seven milliseconds, confirming zero latency regression."*

---

### Slide 14: Live Demo & Service Endpoints
**Duration:** 8:30 – 9:00 (30 seconds)  
**Visual:** 4 service cards with URLs and docker compose command.

> *"All four application services are fully integrated and accessible locally via Docker Compose:*
> * *Streamlit on port 8501*
> * *FastAPI on port 8000*
> * *MLflow on port 5001*
> * *And Grafana on port 3005.*
> 
> *A single terminal command—`docker compose up -d`—provisions the complete multi-service stack within seconds, ensuring seamless local reproducibility."*

---

### Slide 15: Key Insights & Recommendations
**Duration:** 9:00 – 9:35 (35 seconds)  
**Visual:** 4 insight cards and operational recommendation banner.

> *"From an engineering perspective, this project yielded four major takeaways:*
> 1. *Data drift is measurable: our PSI metric of zero point one eight one eight accurately flagged distribution shift before fatal degradation occurred.*
> 2. *Targeted retraining works: expanding n-grams and rebalancing class weights fully recovered macro F1 to **95.41%**.*
> 3. *Schema enforcement is vital: Pydantic guards prevent corrupted payloads from crashing ASGI worker processes.*
> 4. *And end-to-end traceability via MLflow and Docker eliminates environment drift between developer machines and cloud production.*
> 
> *Our core operational recommendation is to implement automated CI/CD retraining triggers whenever PSI exceeds zero point one eight or macro F1 drops by more than three percent."*

---

### Slide 16: Limitations & Future Work
**Duration:** 9:35 – 10:05 (30 seconds)  
**Visual:** Constraints vs Future Extensions comparison.

> *"We also acknowledge current system constraints:*
> * *TF-IDF relies on bag-of-words representations, omitting deep contextual semantics.*
> * *Additionally, SQLite is ideal for local development but limits high-concurrency write throughput.*
> 
> *For future extensions, we plan to benchmark lightweight transformer embeddings such as DistilBERT, integrate live streaming RSS news feeds via Kafka, and migrate our backend to Google Cloud Run and managed BigQuery storage."*

---

### Slide 17: AI Use Disclosure
**Duration:** 10:05 – 10:30 (25 seconds)  
**Visual:** Academic integrity statement and Google Gemini use cases.

> *"In accordance with Vanier College's academic integrity policies, Slide 17 details our AI Use Disclosure.*
> 
> *Google Gemini was utilized strictly as an educational and troubleshooting copilot. Key use cases included clarifying TF-IDF sublinear scaling mathematics, debugging Docker volume mounts, verifying FastAPI lifespan handlers, and refining our Grafana SQLite target query syntax.*
> 
> *All model implementations, code pipelines, and data evaluations were independently verified and validated."*

---

### Slide 18: Thank You & Q&A
**Duration:** 10:30 – 11:00 (30 seconds)  
**Visual:** Closing slide with GitHub repo link and contact details.

> *"In conclusion, this project demonstrates a complete, closed-loop MLOps pipeline—from raw news tokens to live, monitored cloud services.*
> 
> *The entire codebase, presentation slides, and container configurations are publicly available on GitHub at the link displayed on screen.*
> 
> *Thank you very much for your time and attention. I would now be delighted to answer any questions."*

---

## 💡 Quick Defense & Q&A Cheat Sheet (Jüri Sorularına Hazırlık)

| Soru / Topic | Hazır İngilizce Cevap (Key Talking Points) |
|---|---|
| **Why Logistic Regression over XGBoost?** | *"On sparse, high-dimensional TF-IDF vectors (5,000+ features), linear models establish clean hyperplanes without the tree-splitting overhead. LR gave us 88.50% test accuracy vs 82.25% for XGBoost, while being 10x faster to train and evaluate."* |
| **What does PSI = 0.1818 mean?** | *"Population Stability Index measures distribution divergence. Standard industry benchmarks state: PSI < 0.10 means no shift; 0.10 <= PSI <= 0.20 indicates moderate shift; PSI > 0.20 indicates significant drift requiring immediate retraining. Our score of 0.1818 caught the shift early."* |
| **Why load the model at startup in FastAPI?** | *"Loading `model.pkl` once during the lifespan event keeps the pipeline resident in RAM. If we loaded the artifact on each request, latency would spike by 50 to 100 milliseconds due to continuous disk I/O."* |
| **How does Model v2 recover from drift?** | *"Model v2 incorporated (1,3)-grams with 8,000 features to capture emerging multi-word terms like 'Generative AI', enabled sublinear term frequency to normalize repeated keywords, and applied balanced class weighting to counter class skew."* |
