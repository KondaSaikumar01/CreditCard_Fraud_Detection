import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("CreditCard Fraud Prediction (Time & Amount)")

st.write("Enter multiple rows of **Time** and **Amount** to predict fraud.")

# ----------- Input Table -----------
num_rows = st.number_input("How many rows to enter?", min_value=1, max_value=50, value=5)

# Create empty dataframe for user input
data = pd.DataFrame({
    "Time": [0.0] * num_rows,
    "Amount": [0.0] * num_rows
})

edited_df = st.data_editor(data, num_rows="dynamic", key="input_table")

# ----------- Train a simple sample model -----------
# This is a demo model (random synthetic training)
import numpy as np
rng = np.random.RandomState(42)
sample = pd.DataFrame({
    "Time": rng.uniform(0, 100000, 2000),
    "Amount": rng.exponential(100, 2000)
})
sample["Class"] = (sample["Amount"] > 200).astype(int)

X = sample[["Time", "Amount"]]
y = sample["Class"]

model = RandomForestClassifier()
model.fit(X, y)

# ----------- Predict Button -----------
if st.button("Predict Fraud for All Rows"):
    preds = model.predict(edited_df)
    probs = model.predict_proba(edited_df)[:, 1]

    results = edited_df.copy()
    results["Fraud_Prediction"] = preds
    results["Fraud_Probability"] = probs.round(4)

    st.write("### Prediction Results")
    st.dataframe(results)

    st.download_button(
        "Download Results",
        results.to_csv(index=False).encode(),
        "fraud_predictions.csv",
        "text/csv"
    )
