# Customer Churn Prediction AI System

## Overview
This project is a **Customer Churn Prediction system** designed for SaaS businesses. It predicts whether a customer is likely to churn based on usage, subscription, and support data. The system includes:

- Data generation and preprocessing
- Feature engineering
- Model training and evaluation
- FastAPI deployment for real-time predictions

---

## Dataset
- Generated a **synthetic SaaS dataset** with 5000 records
- Features include:
  - Industry, Subscription Type, Country
  - Usage Frequency, Login Activity
  - Support Tickets, Monthly Spend, Payment History
  - Derived features: Engagement Score, Support Ratio
- Dataset contains some missing values to simulate real-world scenarios
- Location: `data/churn_dataset.csv`

---

## Preprocessing & Feature Engineering
- Missing values filled with **median values**
- Categorical variables encoded using **LabelEncoder**
- Feature engineering:
  - **Engagement Score:** `usage_frequency + login_activity`
  - **Support Ratio:** `support_tickets / (usage_frequency + 1)`
- Train/Test split: 80/20
- Scaling optional (used only if required by model)

---

## Model Development
- **Models trained:**
  - Logistic Regression
  - Random Forest Classifier
- **Evaluation metrics:**
  - Accuracy, Precision, Recall, F1-score
  - Confusion Matrix
- **Final model:** Random Forest
- Model saved at: `models/churn_model.pkl`

---

## Deployment
- FastAPI server exposing endpoint:


---
## Example input JSON:

```json
{
  "industry": 0,
  "subscription_type": 1,
  "country": 3,
  "usage_frequency": 10,
  "login_activity": 20,
  "support_tickets": 1,
  "monthly_spend": 100,
  "payment_history": 0,
  "engagement_score": 30,
  "support_ratio": 0.1
}


