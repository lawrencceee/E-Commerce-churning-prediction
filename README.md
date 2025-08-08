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
   - Used XGBoost, RandomForestClassifier and Logistic Regression Model and compare the results to implement a better model
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
| Random Forest       | 0.973357 | 0.987421  | 0.848649| 0.912791 |
| XGBoost             | 0.984014 | 0.988304  | 0.913514| 0.949438 |

<img width="691" height="547" alt="94de24bc-9769-4ea6-a5c0-58df47b4a9be" src="https://github.com/user-attachments/assets/1aa4aac3-f77c-4153-96cb-ee203c2ad44f" />

---

### 🚀 Interactive Interface for Churn Prediction

**💡 What It Does:**  
An interactive web app built with **Gradio** that predicts customer churn probability in real time based on user-inputted data.

**🎯 Features:**
- **Real-Time Predictions:**  
  Input customer details and instantly see the likelihood of churn.

- **Business-Friendly UI:**  
  No coding required — designed for product managers, analysts, and stakeholders.

- **Simulate & Test:**  
  Play with variables like **tenure**, **device usage**, or **satisfaction score** to explore how they influence churn.

- **End-to-End ML Integration:**  
  From preprocessed data to trained model to deployment — all in one smooth interface.

**🔗 Live Demo (on Hugging Face Spaces):**  
👉 [https://astimepassesby-customer-churning-prediction.hf.space/?logs=container&__theme=system&deep_link=uk2_SeqyLTM](https://huggingface.co/spaces/astimepassesby/customer-churning-prediction)

**🖼️ App Screenshot:**  
<img width="1485" height="629" alt="image" src="https://github.com/user-attachments/assets/2ed5c577-a44c-4460-b030-7faf97da7b09" />

