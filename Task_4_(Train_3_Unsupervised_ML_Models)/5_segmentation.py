import streamlit as st
import pandas as pd
import numpy as np
import joblib


scaler = joblib.load("Task_4_(Train_3_Unsupervised_ML_Models)/scaler.pkl")
pca = joblib.load("Task_4_(Train_3_Unsupervised_ML_Models)/pca.pkl")
kmeans = joblib.load("Task_4_(Train_3_Unsupervised_ML_Models)/kmeans.pkl")
features = joblib.load("Task_4_(Train_3_Unsupervised_ML_Models)/features.pkl")


# X_new_scaled = scaler.transform(X_new)

# X_new_pca = pca.transform(X_new_scaled)

# cluster = kmeans.predict(X_new_pca)

st.title("hello world")
