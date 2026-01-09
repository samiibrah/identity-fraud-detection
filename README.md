Identity Fraud Detection System

## Overview

This project provides an end-to-end framework for detecting identity fraud using machine learning, large-scale data processing, and real-time risk scoring components. It simulates an identity verification system similar to those used in financial services, fintech, and government identity workflows. The goal is to demonstrate how profile data, device signals, behavioral features, and external attributes can be combined to build a fraud-scoring model deployed as a production API.

The project includes synthetic datasets, feature engineering pipelines, supervised learning models, and an example FastAPI microservice to serve real-time risk scores.



## Fraud Background

Identity fraud occurs when individuals use stolen, synthetic, or manipulated personal information to bypass verification systems. Common types include:

* Synthetic identity fraud
* First-party fraud
* Account takeover (ATO)
* Duplicate identity creation
* Promotion or bonus abuse
* Coordinated fraud networks

Fraudsters often exploit patterns that only appear when analyzing behavior, devices, and identifiers at scale. This project demonstrates how a systematic data science workflow can uncover these patterns.

## Project Objectives

1. Generate a synthetic but realistic identity dataset containing both legitimate users and fraud cases.
2. Build feature engineering pipelines that mimic production identity verification workflows.
3. Develop supervised fraud detection models using XGBoost, Random Forest, and logistic regression.
4. Evaluate model performance and compare algorithms using standard fraud metrics.
5. Deploy the trained model in a FastAPI microservice capable of real-time inference.
6. Provide notebooks and scripts for extending the system further.


## How the Data Was Built

### 1. Synthetic Identity Generation

The synthetic dataset simulates:

* Personal attributes (name, age, email, phone, address)
* Device information (IP, device ID, user agent)
* Behavioral events (session start, asset load, click activity)
* Fraud indicators (mismatched attributes, velocity anomalies, risky geolocation)

Fraud labels include patterns such as:

* Reused device or IP across multiple identities
* High-risk email or phone patterns
* Implausible demographic combinations
* Rapid account creation velocity
* Risky behavioral sequences

### 2. Data Storage

The data is stored in `data/raw/` and transformed outputs are stored in `data/processed/`.


## Feature Engineering

The project builds a complete feature transformation pipeline that includes:

### Identity-level features

* Age validity
* Name-email similarity
* Email pattern risk scores
* Phone number riskiness
* Address consistency

### Device and IP features

* IP reputation heuristics
* Device reuse across multiple identities
* Browser fingerprint anomalies
* Geo-velocity and country mismatch

### Behavioral features

* Time on page
* Interaction velocity
* Time-of-day risk score
* Returning vs. new session

### Frequency-based features

* Counts of emails, phones, and devices linked to an identity
* Many-to-one signal patterns

All features are assembled in a reproducible pipeline (`src/feature_engineering/`).


## Machine Learning Models

The project compares the following algorithms:

### Logistic Regression

* Baseline, interpretable
* Better calibrated scores
* Good for production explainability

### Random Forest

* Handles non-linearities
* Robust to missing and noisy data

### XGBoost

* Best performance on synthetic dataset
* High recall and precision for fraud targets
* Handles sparse and imbalanced data effectively

## Model Evaluation

Models are evaluated using metrics appropriate for fraud detection:

* Precision, Recall, and F1
* ROC-AUC
* PR-AUC (more informative for imbalanced fraud datasets)
* Confusion matrix
* Top-k precision (fraud catch rate at highest scores)

Performance results are stored in `models/evaluation/`.


## FastAPI Service

The project includes a production-style microservice (`api/fastapi_app.py`) that:

* Loads the trained fraud model
* Performs validation and real-time inference
* Returns JSON risk scores and fraud explanations
* Includes example request payloads and Swagger documentation

To run the service:

```
uvicorn api.fastapi_app:app --reload
```




## How to Run the Project
Install dependencies:

```
pip install -r requirements.txt
```
Run ETL:

```
python src/etl/run_etl.py
```

Build features:

```
python src/feature_engineering/build_features.py
```

Train models:

```
python src/modeling/train_model.py
```

Start API:

```
uvicorn api.fastapi_app:app --reload
```


<a href="https://trackgit.com">
<img src="https://us-central1-trackgit-analytics.cloudfunctions.net/token/ping/mk68ypbkw6xme0btexmk" alt="trackgit-views" />
</a> 

