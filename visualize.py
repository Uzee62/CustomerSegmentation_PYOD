# visualize.py
import streamlit as st
import matplotlib.pyplot as plt

def visualize_data():
    """Display visualization options."""
    st.header("Visualize Outliers")
    graph_type = st.selectbox("Select Graph", ["Bar Graph", "Pie Chart", "Scatter Plot"])
    if graph_type == "Bar Graph":
        plot_bar_chart()
    elif graph_type == "Pie Chart":
        plot_pie_chart()
    elif graph_type == "Scatter Plot":
        plot_scatter_plot()

def plot_bar_chart():
    """Plot bar chart for outliers per country."""
    country_outliers = st.session_state['data'][st.session_state['data']['outlier'] == 1]['Country'].value_counts()
    fig, ax = plt.subplots()
    country_outliers.plot(kind='bar', ax=ax)
    ax.set_title("Outliers per Country")
    ax.set_xlabel("Country")
    ax.set_ylabel("Number of Outliers")
    st.pyplot(fig)

def plot_pie_chart():
    """Plot pie chart for outliers vs non-outliers."""
    outlier_counts = st.session_state['data']['outlier'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(outlier_counts, labels=['Non-Outliers', 'Outliers'], autopct='%1.1f%%', colors=['green', 'red'])
    ax.set_title("Outliers vs Non-Outliers")
    st.pyplot(fig)

def plot_scatter_plot():
    """Plot scatter plot for Quantity vs Unit Price with outliers highlighted."""
    fig, ax = plt.subplots()
    ax.scatter(st.session_state['data']['Quantity'], st.session_state['data']['UnitPrice'], 
               c=st.session_state['data']['outlier'], cmap='coolwarm', label='Outliers')
    ax.set_title("Scatter Plot: Quantity vs Unit Price")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Unit Price")
    st.pyplot(fig)
