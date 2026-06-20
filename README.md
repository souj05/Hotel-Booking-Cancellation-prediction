# Hotel Booking Cancellation Prediction

## Project Overview

This project aims to predict whether a hotel booking will be cancelled using machine learning techniques. Early prediction of cancellations helps hotels optimize revenue management, improve occupancy rates, and reduce financial losses caused by last-minute booking cancellations.

## Problem Statement

Hotel booking cancellations can significantly impact business operations and revenue. The objective of this project is to build a predictive model that identifies bookings that are likely to be cancelled before the arrival date.

## Dataset

* Dataset: Hotel Booking Demand Dataset
* Records: 87,110+
* Features: 71 after preprocessing and encoding
* Target Variable: `is_canceled`

## Project Workflow

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Missing Value Treatment
4. Feature Engineering
5. Label Encoding and One-Hot Encoding
6. Train-Test Split
7. Model Building
8. Cross Validation
9. Hyperparameter Tuning
10. Feature Importance Analysis
11. Model Deployment using Streamlit

## Models Implemented

* Decision Tree Classifier
* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes
* LightGBM

## Model Performance

### LightGBM (Best Model)

* Accuracy: 85.24%
* Cross Validation Accuracy: 85.49%

## Key Insights

The most important features influencing booking cancellations were:

* Lead Time
* Average Daily Rate (ADR)
* Country
* Arrival Date Week Number
* Arrival Month

## Business Impact

The model can help hotel management:

* Identify high-risk bookings
* Reduce cancellation-related losses
* Improve occupancy planning
* Design targeted retention strategies
* Optimize pricing and booking policies

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* LightGBM
* Streamlit

## Future Improvements

* FastAPI Integration
* Docker Containerization
* AWS Deployment
* Real-Time Prediction API
* Advanced Feature Engineering
