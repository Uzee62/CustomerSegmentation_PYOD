
import streamlit as st
from sklearn.metrics import classification_report
import pandas as pd

def display_predictions():
    #Displaying model accuracy and predictions.
    if st.session_state['data'] is None or st.session_state['model'] is None:
        st.warning("Please upload data first.")
    else:
        st.write(f"Detected Outliers: {st.session_state['data']['outlier'].sum()} / {len(st.session_state['data'])}")
        st.write("Predicted Data:")
        st.dataframe(st.session_state['data'][st.session_state['data']["outlier"]==1])

        true_labels = st.session_state['data']['outlier']
        predicted_labels = st.session_state['model'].labels_
        
        
        # report = classification_report(true_labels, predicted_labels, output_dict=True)
        # classification_report_df = pd.DataFrame(report).transpose
        
        
        
        # st.write("Classification Report:")
        # st.dataframe(classification_report_df)
        # # st.write("Accuracy Metrics:")
        # # st.write(f"Precision: {report['1']['precision']:.2f}")
        # # st.write(f"Recall: {report['1']['recall']:.2f}")
        # # st.write(f"F1-Score: {report['1']['f1-score']:.2f}")
        
        report = classification_report(true_labels, predicted_labels, output_dict=True)

# Converting classification report to DataFrame
        report_df = pd.DataFrame(report).transpose()

        # Display the Classification Report in tabular form
        st.write("**Classification Report**")
        st.dataframe(report_df)

        # Calculate the accuracy metrics separately if needed
        accuracy_metrics = {
            "Precision": [report['1']['precision']],
            "Recall": [report['1']['recall']],
            "F1-Score": [report['1']['f1-score']]
        }

        # Converting accuracy metrics to DataFrame
        accuracy_df = pd.DataFrame(accuracy_metrics)

        # Display the Accuracy Metrics in tabular form
        st.write("**Accuracy Metrics for Outliers:**")
        st.dataframe(accuracy_df)
