import pandas as pd

# Load the dataset
file_path = '/home/doc-bd-a3/res_dpre.csv'
df = pd.read_csv(file_path)

# Insight 1: Summary Statistics
summary_stats = df.describe()
with open('/home/doc-bd-a3/eda-in-1.txt', 'w') as file:
    file.write("Insight 1: Summary Statistics\n")
    file.write(summary_stats.to_string())

# Insight 2: Count of Unique Items
unique_items_count = df['item_name'].nunique()
with open('/home/doc-bd-a3/eda-in-2.txt', 'w') as file:
    file.write(f"Insight 2: Count of Unique Items: {unique_items_count}\n")

# Insight 3: Check for another column in your dataset, as 'transaction_type' doesn't exist
# For example, if 'transaction_amount' exists, you can check its summary statistics
if 'transaction_amount' in df.columns:
    transaction_amount_stats = df['transaction_amount'].describe()
    with open('/home/doc-bd-a3/eda-in-3.txt', 'w') as file:
        file.write("Insight 3: Transaction Amount Summary Statistics\n")
        file.write(transaction_amount_stats.to_string())
else:
    with open('/home/doc-bd-a3/eda-in-3.txt', 'w') as file:
        file.write("Insight 3: 'transaction_amount' column not found in the dataset.\n")

# You can add more insights as needed

# Save the insights to text files
# E.g., add more insights and save them in separate text files

