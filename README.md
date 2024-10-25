URL :  https://customersegmentationpyod-w4kiqqeb53rqjmrrjawvck.streamlit.app/



**Columns:**

**InvoiceNo**:

A unique identifier for each transaction or invoice generated.
This helps track individual transactions. Each invoice number corresponds to a single sale.

**StockCode**:

A unique code assigned to each product in the inventory.
This allows you to track which specific items were sold in each invoice. Different products have different stock codes.

**Description:**

A text description of the product sold (e.g., "Blue T-shirt").
This gives human-readable information about what the StockCode refers to.

**Quantity:**

Description: The number of units of the product that were sold in the transaction.
Usage: This helps calculate total sales and understand product demand by looking at the quantities purchased.

**InvoiceDate:**

The date and time when the invoice was generated.
This allows you to analyze sales patterns over time, such as daily, monthly, or seasonal trends.

**UnitPrice:**

The price of a single unit of the product.
This helps calculate the total cost for each invoice by multiplying by the Quantity.

**CustomerID:**

A unique identifier for the customer who made the purchase.
This is used to track purchases by individual customers, allowing for customer segmentation and lifetime value analysis.

**Country:**

The country where the customer is located or where the invoice is generated.
This can be useful for geographic segmentation and understanding where your sales are coming from.



This application allows users to segment customers based on specific features from an uploaded dataset. It leverages the PYOD (Python Outlier Detection) library to identify and visualize anomalous patterns in customer data.

**Features**
**Customer Data Upload:**

Users can upload an Excel file containing customer data.
The app reads and processes the Excel file to perform segmentation.
Anomaly Detection:

The app applies various outlier detection algorithms from the PYOD library, helping identify unusual customers or behavior.
Algorithms supported include Isolation Forest, K-Nearest Neighbors, and more.
Interactive Visualizations:

Results of the outlier detection are displayed through interactive visualizations to help users easily understand the anomalies in the dataset.

**Segmentation Insights:**

Customers are segmented based on patterns and outliers, providing insights into potentially fraudulent or unusual customer behavior.
Libraries Used
pandas for data manipulation.
streamlit for building the interactive web application.
pyod for anomaly detection.
matplotlib and seaborn for data visualization.
openpyxl for reading Excel files.
How to Use
Upload your Excel file by clicking the "Upload" button.
The app processes the data and detects any anomalies.
View the visualized results to gain insights into customer behavior.
