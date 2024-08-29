# InnoByte Amazon Sales Report Analysis
# Author : Kevin
# Mail : kevin.a.aakash@gmail.com

import pandas as pd
import matplotlib.pyplot as plt

# Define data types for columns
dtype_dict = {
    'index': 'float64',
    'Order ID': 'object',
    'date': 'object',
    'Status': 'object',
    'Fulfilment': 'object',
    'Sales Channel': 'object',
    'ship-service-level': 'object',
    'category': 'object',
    'Size': 'object',
    'Courier Status': 'object',
    'Qty': 'float64',
    'INR': 'object',
    'amount': 'float64',
    'ship-city': 'object',
    'ship-state': 'object',
    'ship-postal-code': 'float64',
    'ship-country': 'object',
    'B2B': 'object',
    'fulfilled-by': 'object',
    'New': 'float64',
    'PendingS': 'float64'
}

# Load the dataset
file_path = 'report.csv'
data = pd.read_csv(file_path, dtype=dtype_dict, low_memory=False)

# Display the column names
print("Column names:", data.columns)

# Handle missing values
data = data.dropna()

# Convert data types if necessary
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Display cleaned data information
print(data.info())

# Check for any rows with null dates after conversion
null_dates = data[data['date'].isnull()]
print(f"Rows with null dates after conversion: {len(null_dates)}")

# Drop rows with null dates
data = data.dropna(subset=['date'])

# Display sample data
print("Sample data after cleaning:")
print(data.head())

# Display statistics for key columns
print("Unique values in 'ship-city':", data['ship-city'].nunique())
print("Sample values in 'ship-city':", data['ship-city'].unique()[:10])
print("Unique values in 'category':", data['category'].nunique())
print("Sample values in 'category':", data['category'].unique()[:10])
print("Unique values in 'Fulfilment':", data['Fulfilment'].nunique())
print("Sample values in 'Fulfilment':", data['Fulfilment'].unique()[:10])

# Sales trends over time
data['month'] = data['date'].dt.to_period('M')
monthly_sales = data.groupby('month')['amount'].sum()

# Check if monthly_sales is empty
if monthly_sales.empty:
    print("No data available for monthly sales.")
else:
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line')
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Sales Amount')
    plt.show()

# Most popular product categories (using 'category' column)
product_categories = data['category'].value_counts()

# Check if product_categories is empty
if product_categories.empty:
    print("No data available for product categories.")
else:
    plt.figure(figsize=(12, 6))
    product_categories.plot(kind='bar')
    plt.title('Product Category Distribution')
    plt.xlabel('Product Category')
    plt.ylabel('Count')
    plt.show()

# Distribution of orders by fulfillment method (using 'Fulfilment' column)
fulfillment_methods = data['Fulfilment'].value_counts()

# Check if fulfillment_methods is empty
if fulfillment_methods.empty:
    print("No data available for fulfillment methods.")
else:
    plt.figure(figsize=(12, 6))
    fulfillment_methods.plot(kind='bar')
    plt.title('Fulfillment Method Distribution')
    plt.xlabel('Fulfillment Method')
    plt.ylabel('Count')
    plt.show()

# Segment customers by location (using 'ship-city' column)
customer_location = data['ship-city'].value_counts()

# Check if customer_location is empty
if customer_location.empty:
    print("No data available for customer locations.")
else:
    plt.figure(figsize=(12, 6))
    customer_location.plot(kind='bar')
    plt.title('Customer Location Distribution')
    plt.xlabel('Location')
    plt.ylabel('Count')
    plt.show()

# Sales by state and city (using 'ship-state' column)
state_sales = data.groupby('ship-state')['amount'].sum()

# Check if state_sales is empty
if state_sales.empty:
    print("No data available for state sales.")
else:
    plt.figure(figsize=(12, 6))
    state_sales.plot(kind='bar')
    plt.title('State-wise Sales Distribution')
    plt.xlabel('State')
    plt.ylabel('Sales Amount')
    plt.show()