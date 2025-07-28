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
   - Used RandomForestClassifier for its robustness and interpretability
   - Trained using a pipeline via scikit-learn
   - Evaluated with accuracy, precision, recall, F1, and ROC-AUC

4. **Model Inference via Gradio**
   - Built an interface to enter feature values
   - Returns churn prediction and churn probability in real time

---

## 🧪 Performance

After training and evaluation:

- **Accuracy**: ~0.97
- **ROC-AUC Score**: ~0.98

  <img width="536" height="393" alt="image" src="https://github.com/user-attachments/assets/1971657c-7e97-4a03-bd9c-72476db0f438" />
- **Top Features**:
  - Tenure
  - SatisfactionScore
  - CashbackAmount
- **Correlation Matrix**:
  <img width="1107" height="881" alt="image" src="https://github.com/user-attachments/assets/67004236-729a-43e2-b305-0ec9fa84b4be" />

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
