Credit Card Fraud Detection — End-to-End ML Project

A complete, production-style machine learning pipeline for detecting fraudulent credit card transactions.
Fraud cases are extremely rare (~0.17%), making this a perfect real-world example of imbalanced classification, threshold tuning, and model interpretability.

📌 Overview

This project builds an end-to-end ML workflow that:

Understands data distribution

Handles extreme class imbalance

Trains multiple ML models

Compares performance using correct metrics

Applies oversampling (SMOTE)

Tunes decision thresholds for optimal business performance

Provides model explainability through feature importance

🔹 Notebook Structure

Importing Libraries & Loading Data

Exploratory Data Analysis (EDA)

Preprocessing & Scaling

Train–Test Split (Stratified)

Baseline Model — Logistic Regression

Random Forest — Ensemble Model

Oversampling — SMOTE + Random Forest

Threshold Tuning

Feature Importance Analysis (Optional SHAP)

Model Comparison Table

Conclusion & Insights

🚀 Final Model

After experimentation, the best performing model is:

✔️ Random Forest + SMOTE Oversampling + Custom Threshold (0.40)

This combination achieves high recall (critical for fraud detection) while keeping precision acceptable to reduce false alarms.

Best suited for:

ML beginners

Kaggle learners

Interview preparation

Portfolio-building projects

🔄 Project Workflow
1. Business Understanding

Credit card fraud detection is a high-impact use case in finance. Because fraud accounts for a tiny fraction of transactions, models must be designed to maximize recall without overwhelming analysts with false positives.

2. Data Understanding

The dataset contains anonymized credit card transaction details.

Features:

Time → seconds elapsed since first transaction

Amount → transaction amount

V1 to V28 → PCA-transformed features

Class → target label (0 = Not Fraud, 1 = Fraud)

Key analysis tasks:

Class distribution

Statistical summary

Basic correlations

Fraud vs non-fraud behavior

3. Exploratory Data Analysis (EDA)

EDA explores:

Imbalance visualization

Transaction amount patterns

Time-of-day trends

Boxplots / histograms

Optional correlation heatmap

Why EDA matters:

Builds intuition

Guides preprocessing choices

Provides interview-ready insights

4. Data Preprocessing

Steps include:

✔ Stratified Train–Test Split

Preserves fraud ratio.

✔ Feature Scaling

Standardize Amount and Time

PCA features are already scaled

✔ Handling Class Imbalance

Two methods tested:

Class-weighted models

SMOTE oversampling (train set only)

Why?

Prevents data leakage

Balances minority fraud class

Improves recall significantly

5. Model Building

Models trained:

🔹 Baseline

Logistic Regression (class_weight="balanced")

🔹 Tree-Based Models

Random Forest

🔹 Oversampling Models

Logistic Regression + SMOTE

Random Forest + SMOTE

🔹 Optional

Isolation Forest (unsupervised anomaly detection)

Why multiple models?
To evaluate linear vs non-linear performance, oversampling benefits, and fraud anomaly behavior.

6. Model Evaluation

Correct metrics for imbalanced data:

Recall (most important)

Precision

F1-score

ROC-AUC

PR-AUC (more informative than ROC-AUC here)

Confusion Matrix

Why not accuracy?
Predicting all transactions as “Not Fraud” gives 99.8% accuracy but catches zero fraud cases.

7. Model Comparison

Models compared using:

Fraud Recall

Precision

ROC-AUC

PR-AUC

Random Forest + SMOTE consistently performs best.

8. Conclusion

The combination of Random Forest + SMOTE + threshold tuning provides the strongest fraud detection capability.

Real-world deployment requires careful threshold selection to balance losses vs false alerts.

Fraud prediction is a cost-sensitive problem requiring domain-specific metrics.

9. Possible Deployment Ideas

Real-time fraud detection API

Dashboard for fraud scoring

Adjustable threshold UI for analysts

Continuous retraining pipeline

Integration with Kafka/Spark streaming

🧰 Technologies Used

Python

Pandas, NumPy

Scikit-learn

Imbalanced-learn (SMOTE)

Matplotlib, Seaborn

Jupyter Notebook

Streamlit 
