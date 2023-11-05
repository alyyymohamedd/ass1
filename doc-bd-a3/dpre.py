import pandas as pd

# Load the dataset from the specified path
file_path = '/home/doc-bd-a3/1.csv'
df = pd.read_csv(file_path)

# Data Cleaning
# Task 1: Remove rows with missing values
df = df.dropna()

# Task 2: Remove duplicate rows
df = df.drop_duplicates()

# Data Transformation
# Task 1: Convert the 'date' column to a datetime data type with the correct format
#df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')  # Use 'format' to specify the date format

# Task 2: Create a new column 'total_price' by multiplying 'item_price' and 'quantity'
df['total_price'] = df['item_price'] * df['quantity']

# Data Reduction
# Task 1: Remove unnecessary columns
columns_to_remove = ['order_id', 'received_by', 'time_of_sale']
df = df.drop(columns=columns_to_remove)

# Task 2: Aggregate data by 'item_name' and calculate the sum of 'total_price' for each item
df_agg = df.groupby('item_name')['total_price'].sum().reset_index()

# Data Discretization
# Task 1: Bin 'total_price' into three categories (Low, Medium, High)
bins = [0, 100, 500, df_agg['total_price'].max()]
labels = ['Low', 'Medium', 'High']
df_agg['price_category'] = pd.cut(df_agg['total_price'], bins=bins, labels=labels)

# Task 2: Reset the index of the aggregated DataFrame
df_agg = df_agg.reset_index()

# Save the resulting DataFrame as a new CSV file
df_agg.to_csv('/home/doc-bd-a3/res_dpre.csv', index=False)

