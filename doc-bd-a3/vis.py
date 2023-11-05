import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/home/doc-bd-a3/res_dpre.csv'
df = pd.read_csv(file_path)

# Create a simple bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['item_name'], df['total_price'])
plt.xlabel('Item Name')
plt.ylabel('Total Price')
plt.title('Total Price by Item Name')
plt.xticks(rotation=90)

# Save the visualization as "vis.png"
plt.savefig('/home/doc-bd-a3/vis.png')

# Display the visualization (optional)
plt.show()

