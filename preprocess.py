# preprocess.py
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import streamlit as st

def preprocess_data():
   
    if st.session_state['data'] is not None:
        categorical_cols = ['Country']
        numerical_cols = ['Quantity', 'UnitPrice']
         """Using OHE for handling Categorical data"""
        encoder = OneHotEncoder(drop='first', sparse_output=False)
        encoded_data = encoder.fit_transform(st.session_state['data'][categorical_cols])
        """Using Stadard scaler on Numerical data for scaling"""
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(st.session_state['data'][numerical_cols])

        processed_data = pd.DataFrame(scaled_data, columns=numerical_cols)
        encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols))
        st.session_state['processed_data'] = pd.concat([processed_data, encoded_df], axis=1)
