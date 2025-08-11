# 🔐 Network Security – End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.10-blue.svg?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-black.svg?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-green?logo=githubactions)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen?logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Enabled-orange?logo=tensorflow)
![Data Pipeline](https://img.shields.io/badge/Data-Pipeline-blueviolet)

---

## 💼 Core Skills from This Project
![ETL Pipeline](https://img.shields.io/badge/ETL%20Pipeline-Automated-yellowgreen)
![Data Validation](https://img.shields.io/badge/Data%20Validation-Drift%20Detection-blue)
![Model Training](https://img.shields.io/badge/Model%20Training-Scikit%20Learn-orange)
![Flask API](https://img.shields.io/badge/Flask%20API-Deployment-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green)
![Cloud Ready](https://img.shields.io/badge/Deployment-Cloud%20Ready-lightblue)
![MongoDB](https://img.shields.io/badge/MongoDB-Data%20Storage-brightgreen)

---

🚀 **Project Overview**  
This project is a complete **end-to-end Machine Learning pipeline** 🧠 designed to detect **phishing attacks** in network traffic, built from scratch to deployment. It showcases my skills in **data engineering**, **machine learning**, **API development**, **Dockerization**, and **CI/CD automation** — all in one neat package.  

I started with a **robust ETL pipeline** 📊 that:
- **Extracts** raw data from a source
- **Validates** it for quality & consistency
- **Transforms** it into a clean, model-ready format  

These stages are fully modular — meaning the system can easily adapt to new data sources or models in the future.  
All intermediate files and logs are stored in the `Artifacts/` directory for **full reproducibility**.

---

🎯 **Architecture at a Glance**

      ┌────────────────┐
      │  Data Source   │
      └───────┬────────┘
              │
              ▼
  ┌────────────────────────┐
  │   ETL Pipeline (📦)     │
  │  - Ingestion            │
  │  - Validation           │
  │  - Transformation       │
  └───────────┬─────────────┘
              │
              ▼
  ┌────────────────────────┐
  │ Model Training (🧠)     │
  │ - Preprocessing (pkl)   │
  │ - ML Algorithms         │
  │ - Evaluation Metrics    │
  └───────────┬─────────────┘
              │
              ▼
  ┌────────────────────────┐
  │ Flask API (🌐)          │
  │ - Serve Predictions     │
  │ - Web/API Interface     │
  └───────────┬─────────────┘
              │
              ▼
  ┌────────────────────────┐
  │  Docker Container 🐳    │
  │  - Consistent Env       │
  │  - Easy Deploy          │
  └───────────┬─────────────┘
              │
              ▼
  ┌────────────────────────┐
  │ CI/CD (⚡ GitHub Actions)│
  │ - Test, Build, Deploy   │
  └────────────────────────┘

---

💡 **How It Works – In One Flow**  
The journey begins with raw phishing-related network data. Using my **ETL pipeline**, the data is ingested, validated for schema & drift issues, and transformed into a numerical format ready for machine learning models. This process is entirely automated so it can be rerun whenever new data arrives.  

The **model training** step applies preprocessing (saved as `preprocessing.pkl`) and trains classification algorithms to detect phishing patterns. Evaluation ensures the model meets performance benchmarks before deployment.  

Once the model is ready, it’s integrated into a **Flask application**, which can serve predictions through a web interface or API endpoints. This app is **Dockerized** 🐳 so it can run in any environment without compatibility issues.  

To ensure continuous integration and delivery, I set up a **GitHub Actions CI/CD pipeline** ⚡ that installs dependencies, runs tests, builds the Docker image, and can automatically deploy to cloud services such as AWS, Azure, or GCP.

---

🗂 **Key Components**
- `app.py` → Flask API entry point  
- `main.py` → Triggers the full pipeline  
- `push_data.py` → Loads data into MongoDB 🍃  
- `.github/workflows/main.yml` → CI/CD automation steps  
- `Dockerfile` → Container build instructions  
- `requirements.txt` → Python dependencies  
- `Artifacts/` → Stores processed datasets, models & reports  

---

💻 **Run Locally**
```bash
git clone https://github.com/Harshit0716/Network_Security.git
cd Network_Security
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py

⚙ CI/CD Workflow

Trigger: Push to main branch

Steps:
✅ Install dependencies
✅ Run tests
✅ Build Docker image
✅ Deploy to server/cloud

In short, this project takes an idea from raw data ➡ automated ETL ➡ ML model ➡ Dockerized Flask app ➡ CI/CD deployment, proving my ability to build scalable, production-grade machine learning systems from scratch. 🚀
