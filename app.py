import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pyod.models.knn import KNN
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Initializing session state
if 'data' not in st.session_state:
    st.session_state['data'] = None
if 'processed_data' not in st.session_state:
    st.session_state['processed_data'] = None
if 'model' not in st.session_state:
    st.session_state['model'] = None

# Title and sidebar
st.title("Customer Segmentation Using PYOD")
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a page", ["Upload Data", "Model Accuracy & Predictions", "Graphs"])

# To Upload DataSet
if options == "Upload Data":
    st.header("Upload your CSV or Excel file")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            st.session_state['data'] = pd.read_csv(uploaded_file)
        else:
            st.session_state['data'] = pd.read_excel(uploaded_file)

        st.write("Data Preview:")
        st.dataframe(st.session_state['data'])

        # Handling the Categorical data Using OHE
        categorical_cols = ['Country']
        numerical_cols = ['Quantity', 'UnitPrice']

        encoder = OneHotEncoder(drop='first', sparse_output=False)
        encoded_data = encoder.fit_transform(st.session_state['data'][categorical_cols])

        # Scaling  fusing Standard Scaler
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(st.session_state['data'][numerical_cols])
        
        
        #Concatinating Scaled Numerical and ohe categorical columns
        
        processed_data = pd.DataFrame(scaled_data, columns=numerical_cols)
        encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols))
        st.session_state['processed_data'] = pd.concat([processed_data, encoded_df], axis=1)

        # Model Training (KNN)
        knn = KNN()
        knn.fit(st.session_state['processed_data'])
        st.session_state['model'] = knn

        # Predicting outliers (Storing labels in outlier column and adding the column to original dataSet)
        st.session_state['data']['outlier'] = knn.labels_
        st.success("Model trained and outliers detected!")

# Model Accuracy & Predictions Page
if options == "Model Accuracy & Predictions":
    if st.session_state['data'] is None or st.session_state['model'] is None:
        st.warning("Please upload data first.")
    else:
        st.header("Model Accuracy and Predictions")
        st.write(f"Detected Outliers: {st.session_state['data']['outlier'].sum()} / {len(st.session_state['data'])}")

        #Displaying predicted data
        st.write("Predicted Data:")
        st.dataframe(st.session_state['data'])

        # Assume 1 as outliers, 0 as inliers for basic classification metrics
        true_labels = st.session_state['data']['outlier']
        predicted_labels = st.session_state['model'].labels_  

        # Generating a classification report
        report = classification_report(true_labels, predicted_labels, output_dict=True)
        st.write("Classification Report:")
        st.text(classification_report(true_labels, predicted_labels))

        #accuracy metrics
        st.write("Accuracy Metrics:")
        st.write(f"Precision: {report['1']['precision']:.2f}")
        st.write(f"Recall: {report['1']['recall']:.2f}")
        st.write(f"F1-Score: {report['1']['f1-score']:.2f}")

#Visualisations
if options == "Graphs":
    if st.session_state['data'] is None:
        st.warning("Please upload data first.")
    else:
        st.header("Visualize Outliers")
        graph_type = st.selectbox("Select Graph", ["Bar Graph", "Pie Chart", "Scatter Plot"])
# Bar Graph : showing Outlier distribution between different Countries
        if graph_type == "Bar Graph":
            country_outliers = st.session_state['data'][st.session_state['data']['outlier'] == 1]['Country'].value_counts()
            fig, ax = plt.subplots()
            country_outliers.plot(kind='bar', ax=ax)
            ax.set_title("Outliers per Country")
            ax.set_xlabel("Country")
            ax.set_ylabel("Number of Outliers")
            st.pyplot(fig)
#  # Pie chart of outliers vs non-outliers
        elif graph_type == "Pie Chart":
            outlier_counts = st.session_state['data']['outlier'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(outlier_counts, labels=['Non-Outliers', 'Outliers'], autopct='%1.1f%%', colors=['green', 'red'])
            ax.set_title("Outliers vs Non-Outliers")
            st.pyplot(fig)
# Scatter plot of Quantity vs UnitPrice with outliers highlighted
        elif graph_type == "Scatter Plot":
            fig, ax = plt.subplots()
            ax.scatter(st.session_state['data']['Quantity'], st.session_state['data']['UnitPrice'], c=st.session_state['data']['outlier'], cmap='coolwarm', label='Outliers')
            ax.set_title("Scatter Plot: Quantity vs Unit Price")
            ax.set_xlabel("Quantity")
            ax.set_ylabel("Unit Price")
            st.pyplot(fig)
