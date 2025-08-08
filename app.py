import gradio as gr
import joblib
import pandas as pd

# Load your trained pipeline
pipeline = joblib.load("churn_model.pkl")

gradio_inputs = [
    gr.Number(label="Customer Tenure (months)"),
    gr.Dropdown(["Mobile Phone", "Computer"], label="Preferred Login Device"),
    gr.Dropdown([1, 2, 3], label="City Tier"),
    gr.Number(label="Distance from Warehouse to Home (km)"),
    gr.Dropdown(["UPI", "CC", "COD", "Debit Card", "Net Banking"], label="Preferred Payment Mode"),
    gr.Dropdown(["Male", "Female"], label="Gender"),
    gr.Number(label="Hours Spent on App Daily"),
    gr.Number(label="Number of Devices Registered"),
    gr.Dropdown(["Laptop & Accessory", "Mobile", "Fashion", "Others", "Grocery"], label="Preferred Order Category"),
    gr.Dropdown([1, 2, 3, 4, 5], label="Satisfaction Score"),
    gr.Dropdown(["Single", "Divorced", "Married"], label="Marital Status"),
    gr.Number(label="Number of Addresses"),
    gr.Dropdown([0, 1], label="Customer Complained? (0=No, 1=Yes)"),
    gr.Number(label="Order Amount Increase From Last Year"),
    gr.Number(label="Coupons Used"),
    gr.Number(label="Total Order Count"),
    gr.Number(label="Days Since Last Order"),
    gr.Number(label="Cashback Amount")
]

# Prediction function
def predict_churn(*inputs):
    columns = [
        'Tenure', 'PreferredLoginDevice', 'CityTier', 'WarehouseToHome',
        'PreferredPaymentMode', 'Gender', 'HourSpendOnApp', 'NumberOfDeviceRegistered',
        'PreferedOrderCat', 'SatisfactionScore', 'MaritalStatus', 'NumberOfAddress',
        'Complain', 'OrderAmountHikeFromlastYear', 'CouponUsed', 'OrderCount',
        'DaySinceLastOrder', 'CashbackAmount'
    ]
    
    input_df = pd.DataFrame([inputs], columns=columns)
    prob = pipeline.predict_proba(input_df)[0][1]  # Probability of class 1 (Churn)
    if prob >= 0.5:
        label = "Churn"
        return f"{label} ({prob * 100:.1f}% chance to churn)"
    else:
        label = "Not Churn"
        return f"{label} ({(1-prob)*100:.1f}% chance to not churn)"

gr.Interface(fn=predict_churn, inputs=gradio_inputs, outputs=gr.Label(label="Prediction")).launch()