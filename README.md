# 🔐 Network Security – End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.10-blue.svg?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-black.svg?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?logo=docker)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-green?logo=githubactions)
![AWS](https://img.shields.io/badge/Cloud-AWS-orange?logo=amazonaws)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-brightgreen?logo=mongodb)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Enabled-orange?logo=tensorflow)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 💼 Core Skills from This Project
![ETL Pipeline](https://img.shields.io/badge/ETL%20Pipeline-Automated-yellowgreen)
![Data Validation](https://img.shields.io/badge/Data%20Validation-Drift%20Detection-blue)
![Model Training](https://img.shields.io/badge/Model%20Training-Scikit%20Learn-orange)
![Flask API](https://img.shields.io/badge/Flask%20API-Deployment-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green)
![AWS EC2](https://img.shields.io/badge/AWS-EC2%20Hosting-orange?logo=amazonec2)
![AWS S3](https://img.shields.io/badge/AWS-S3%20Storage-gold?logo=amazons3)
![MongoDB](https://img.shields.io/badge/MongoDB-Data%20Storage-brightgreen)

---

🚀 **Project Overview**  
This project is a complete **end-to-end Machine Learning pipeline** 🧠 for detecting **phishing attacks** in network traffic, built from scratch to production deployment. It demonstrates my expertise in **data engineering**, **machine learning**, **API development**, **Dockerization**, **CI/CD automation**, and **AWS cloud deployment**.  

I began by designing a **modular ETL pipeline** 📊 to:
- **Extract** raw network data
- **Validate** it for quality & drift detection
- **Transform** it into model-ready features  

All intermediate datasets and reports are stored in the `Artifacts/` directory for **traceability** and reproducibility.

---

💡 **How It Works – In One Flow**  
The journey starts with raw phishing-related network data. My automated **ETL pipeline** ingests the data, validates schema & drift, and transforms it for machine learning. The **model training** step applies preprocessing (saved as `preprocessing.pkl`) and trains algorithms to detect phishing patterns.  

The trained model is wrapped in a **Flask application** 🌐 that serves predictions via both a web interface and an API endpoint. This app is **Dockerized** 🐳 to ensure consistency across environments.  

For deployment:  
- The **Docker image** is hosted and run on **AWS EC2**, making the service publicly accessible.  
- Static files and artifacts are stored in an **AWS S3 bucket**, ensuring fast and reliable content delivery.  
- A **CI/CD pipeline** in **GitHub Actions** automates build, test, and deployment steps, so every update is pushed seamlessly to production.

---

🗂 **Key Components**
- `app.py` → Flask API entry point  
- `main.py` → Full pipeline trigger  
- `push_data.py` → MongoDB data loader 🍃  
- `.github/workflows/main.yml` → CI/CD automation  
- `Dockerfile` → Container build setup  
- `requirements.txt` → Python dependencies  
- `Artifacts/` → Data & model storage  
- **AWS S3** → Static asset storage  
- **AWS EC2** → Docker container hosting  

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
✅ Push to AWS EC2
✅ Sync static files to AWS S3

In short, this project takes an idea from raw data ➡ automated ETL ➡ ML model ➡ Dockerized Flask app ➡ AWS deployment with CI/CD, proving my ability to build, automate, and deploy scalable production-grade ML systems in the cloud. 🚀
