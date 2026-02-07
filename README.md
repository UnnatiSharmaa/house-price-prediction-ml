
# 🏠 Predicting House Prices Using Machine Learning

## 📌 Problem Overview
Accurate house price prediction is a critical challenge in the real estate industry. Buyers, sellers, and investors rely on reliable estimates to make informed decisions. However, property data is often messy, incomplete, and inconsistent.  
This project builds an **end-to-end machine learning solution** to predict house prices using property and location features. The workflow covers the complete ML lifecycle—from data collection and cleaning to model training, evaluation, and deployment.

## 📊 Data Source
The dataset was collected from publicly available real estate listings and property records.  
- **Size:** ~1000+ rows  
- **Features:** ~15+ columns (numerical & categorical)  
- **Target:** House price  

## ⚙️ Models Used
We experimented with multiple regression techniques:  
- **Linear Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor**  

After evaluation and hyperparameter tuning, **XGBoost Regressor** was selected as the final model due to its superior performance on test data.

## 🚀 Deliverables
- `dataset.csv` → Cleaned dataset  
- `notebook.ipynb` → Complete ML lifecycle (EDA, preprocessing, training, evaluation)  
- `model.pkl` → Saved best model  
- `app.py` → Streamlit deployment script  
- `README.md` → Project overview  

## ▶️ Running the Streamlit App Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Open the local URL  in the terminal to interact with the app.

