# 📉 Customer Churn Prediction with Machine Learning

This project is a supervised machine learning pipeline that predicts **customer churn** using an e-commerce dataset. It includes **data preprocessing**, **feature engineering**, **model training**, and a live **Gradio web interface** for real-time churn probability prediction.

---

## 🔍 Problem Statement

Churn is one of the most critical KPIs in any customer-facing business. This project aims to:
   - Predict whether a customer is likely to **churn (leave)** or **stay**
   - Identify the **factors** that influence churn
   - Provide an **interactive interface** for business users to test scenarios and improve retention strategies

---

## 📁 Dataset

The dataset is sourced from an e-commerce platform and includes:

- **Behavioral data** (e.g. HourSpendOnApp, OrderCount, Tenure)
- **Demographic data** (e.g. CityTier, Gender, MaritalStatus)
- **Transactional info** (e.g. OrderAmountHikeFromlastYear, CashbackAmount)
- **Target variable**: Churn (Yes/No)

## 🧾 Feature Descriptions

| Feature Name                 | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `CustomerID`                | Unique customer ID                                                          |
| `Churn`                     | Flag indicating whether the customer churned (`1`) or not (`0`)             |
| `Tenure`                    | Tenure of the customer in the organization                                  |
| `PreferredLoginDevice`      | Preferred device used to log in (e.g., mobile, web)                         |
| `CityTier`                  | City tier classification (e.g., Tier 1, Tier 2, Tier 3)                     |
| `WarehouseToHome`           | Distance between the warehouse and the customer’s home                     |
| `PreferredPaymentMode`      | Preferred payment method (e.g., credit card, debit card, cash on delivery) |
| `Gender`                    | Gender of the customer                                                      |
| `HourSpendOnApp`            | Number of hours spent on the app or website                                 |
| `NumberOfDeviceRegistered`  | Number of devices registered to the account                                 |
| `PreferedOrderCat`          | Preferred order category in the last month                                 |
| `SatisfactionScore`         | Customer satisfaction score                                                 |
| `MaritalStatus`             | Marital status of the customer                                              |
| `NumberOfAddress`           | Number of addresses linked to the account                                   |
| `OrderAmountHikeFromlastYear` | % increase in order amount compared to last year                        |
| `CouponUsed`                | Number of coupons used in the last month                                    |
| `OrderCount`                | Total number of orders in the last month                                    |
| `DaySinceLastOrder`         | Days since the last order                                                   |
| `CashbackAmount`            | Average cashback received in the last month                                 |


Remarks: The dataset is from https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction?resource=download

---

## 🧠 Model Workflow

1. **Data Preprocessing**
   - Handled missing values
   - Encoded categorical variables using OneHotEncoder
   - Scaled numerical features with StandardScaler

2. **Feature Engineering**
   - Removed non-informative fields (e.g. CustomerID)
   - Checked correlations and feature importances

3. **Model Training**
   - Used RandomForestClassifier and Logistic Regression Model and compare the results to implement a better model
   - Trained using a pipeline via scikit-learn
   - Evaluated with accuracy, precision, recall, F1, and ROC-AUC

5. **Model Inference via Gradio**
   - Built an interface to enter feature values
   - Returns churn prediction and churn probability in real time

---
## 📊 Model Performance Comparison

After training and evaluation, Random Forest is used at the end for Churn prediction it has a better performance compared to Logistic Regression.

| Model                | Accuracy | Precision | Recall  | F1 Score |
|---------------------|----------|-----------|---------|----------|
| Logistic Regression | 0.915631 | 0.868852  | 0.572973| 0.690554 |
| Random Forest       | 0.975133 | 0.993711  | 0.854054| 0.918605 |

<img width="790" height="590" alt="image" src="https://github.com/user-attachments/assets/e016500b-9eec-4d8d-8d99-717031397e14" />

---

## 🚀 Interactive Interface For Churn Prediction


1. **Interactive Churn Prediction App built with Gradio**
   - Users can input customer information and receive a real-time prediction of churn probability

2. **Live ML demo powered by Gradio**
   - Test how customer attributes like tenure, device usage, and satisfaction score influence churn likelihood

3. **Gradio front-end for churn prediction**
   - Provides a user-friendly interface to simulate customer profiles and explore model behavior

4. **No-code interface for testing model predictions**
   - Easily evaluate churn risk without writing a single line of code—ideal for business users or stakeholders
  
5. **End-to-end ML workflow with Gradio UI**
   - From raw data to real-time predictions—see how your data transforms into insights


<img width="1242" height="850" alt="image" src="https://github.com/user-attachments/assets/7611a6ab-fe46-4657-9560-dd76fb085c06" />
