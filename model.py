# model.py
from pyod.models.knn import KNN
import streamlit as st

def train_model():
    """Train KNN model and label outliers."""
    if st.session_state['processed_data'] is not None:
        knn = KNN()
        knn.fit(st.session_state['processed_data'])
        st.session_state['model'] = knn
        st.session_state['data']['outlier'] = knn.labels_
        st.success("Model trained and outliers detected!")
