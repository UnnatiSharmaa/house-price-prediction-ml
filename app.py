import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("House Price Prediction (Regression)")
st.write("Fill inputs in sidebar and click Predict.")

# Load model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load data to get columns/options
df = pd.read_csv("AmesHousing.csv")
target_col = "SalePrice"
X = df.drop(columns=[target_col])

st.sidebar.header("Input Features")

input_data = {}
for col in X.columns:
    if X[col].dtype == "object":
        options = sorted(X[col].dropna().unique().tolist())
        input_data[col] = st.sidebar.selectbox(col, options)
    else:
        mn = float(X[col].min())
        mx = float(X[col].max())
        default = float(X[col].median())
        input_data[col] = st.sidebar.number_input(col, min_value=mn, max_value=mx, value=default)

input_df = pd.DataFrame([input_data])

if st.button("Predict Price"):
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Price: {pred:,.0f}")