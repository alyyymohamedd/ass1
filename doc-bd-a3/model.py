import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset
file_path = '/home/doc-bd-a3/res_dpre.csv'
df = pd.read_csv(file_path)

# Select columns suitable for K-means (e.g., 'total_price')
data = df[['total_price']]

# Create and fit the K-means model with k=3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(data)

# Get cluster labels for each data point
cluster_labels = kmeans.labels_

# Calculate the number of records in each cluster
cluster_counts = pd.Series(cluster_labels).value_counts()

# Save the number of records in each cluster to a text file
with open('/home/doc-bd-a3/k.txt', 'w') as file:
    for cluster, count in cluster_counts.items():
        file.write(f'Cluster {cluster}: {count} records\n')

# Print cluster information (for reference)
print(cluster_counts)

