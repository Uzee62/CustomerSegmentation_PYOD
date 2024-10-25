# data_upload.py
import streamlit as st
import pandas as pd

def upload_data():
    """Upload CSV or Excel file and load into session state."""
    
    
    expected_columns = [
        "InvoiceNo", "StockCode", "Description", 
        "Quantity", "InvoiceDate", "CustomerID", "Country"
    ]

    st.write("The Expected Columns in your dataset are:  \n\n" , " , ".join(expected_columns))
    st.header("Upload your CSV or Excel file")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            st.session_state['data'] = pd.read_csv(uploaded_file)
        else:
            st.session_state['data'] = pd.read_excel(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(st.session_state['data'])
