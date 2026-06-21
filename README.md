# Hotel Booking Cancellation Prediction

## Project Overview

This project predicts whether a hotel booking will be canceled using Machine Learning. The objective is to help hotels identify potential cancellations and improve booking management.

## Dataset Information

- Dataset: Hotel Booking Demand Dataset
- Original Records: 119,000+
- Records After Cleaning: 87,110
- Target Variable: `is_canceled`

## Data Preprocessing

- Handled missing values
- Removed duplicate records
- Label Encoded Country column
- One-Hot Encoded categorical features
- Feature Engineering
- Final Dataset Shape: 87,110 × 71

## Machine Learning Models

- Decision Tree Classifier
- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- LightGBM Classifier

## Model Performance

### Best Model: LightGBM

| Metric | Score |
|----------|----------|
| Cross Validation Accuracy | 84% |
| Tuned Accuracy | 85.2% |
| Hyperparameter Tuning | RandomizedSearchCV |

### Top Important Features

1. Lead Time
2. ADR (Average Daily Rate)
3. Country
4. Arrival Date Week Number
5. Arrival Date Day Of Month
6. Agent
7. Stay Duration
8. Total Special Requests
9. Booking Changes

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- LightGBM
- Matplotlib
- Seaborn
- Streamlit
- FastAPI
- Docker
- Joblib

---

# Streamlit Application

Interactive web application built using Streamlit.

![Streamlit Home](images/streamlit-home.png)

![Streamlit Input Form](images/streamlit-form.png)

![Streamlit Prediction Interface](images/streamlit-prediction.png)

---

# FastAPI Deployment

REST API built using FastAPI.

Available Endpoints:

- GET /
- GET /health
- POST /predict

### FastAPI Swagger Documentation

![FastAPI Home Endpoint](images/fastapi-home.png)

![FastAPI Health Endpoint](images/fastapi-health.png)

![FastAPI Predict Endpoint](images/fastapi-predict.png)

---

# Docker Containerization

Application successfully containerized using Docker.

### Docker Build

- Dockerfile created
- Requirements configured
- Image built successfully
- Application executed inside container

---

# Project Workflow

```text
Data Cleaning
      ↓
Feature Engineering
      ↓
Data Preprocessing
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Hyperparameter Tuning
      ↓
Streamlit Deployment
      ↓
FastAPI API Development
      ↓
Docker Containerization
```

## Project Structure

```text
Hotel_Booking_Cancellation_Prediction/
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
├── hotel_cancellation_model.pkl
├── Hotel_Booking_Cancellation.ipynb
├── README.md
│
└── screenshots/
```

## Author

**Sowjanya Tadimarri**

Machine Learning | AI | Data Science
