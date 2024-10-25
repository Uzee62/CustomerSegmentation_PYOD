# main.py
import streamlit as st
from data_upload import upload_data
from preprocess import preprocess_data
from model import train_model
from predictions import display_predictions
from visualize import visualize_data

# Initializing session state
if 'data' not in st.session_state:
    st.session_state['data'] = None
if 'processed_data' not in st.session_state:
    st.session_state['processed_data'] = None
if 'model' not in st.session_state:
    st.session_state['model'] = None

# Main UI
def main():
    st.title("Customer Segmentation Using PYOD")
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choose a page", ["Upload Data", "Model Accuracy & Predictions", "Graphs"])

    if options == "Upload Data":
        upload_data()
        if st.session_state['data'] is not None:
            preprocess_data()
            train_model()

    elif options == "Model Accuracy & Predictions":
        display_predictions()

    elif options == "Graphs":
        if st.session_state['data'] is None:
            st.warning("Please upload data first.")
        else:
            visualize_data()

if __name__ == "__main__":
    main()
