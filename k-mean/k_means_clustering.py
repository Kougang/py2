# K-Means Clustering

# Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importation du dataset
dataset = pd.read_csv('Mall_Customers.csv')

# Extraction de variables indépendantes
X = dataset.iloc[:, [3, 4]].values

# Trouver le nombre optimal de clusters en utilisant la méthode du coude
from sklearn.cluster import KMeans
wcss = []

# Utilisation de la boucle for pour des iterations allant de 1 to 10. 
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 10), wcss)
plt.title('La Méthode Elbow')
plt.xlabel('Nombre de Clusters')
plt.ylabel('WCSS')
plt.show()

# Former le modèle K-means sur le dataset 
kmeans = KMeans(n_clusters=5, init='k-means++', random_state= 42)  
y_predict= kmeans.fit_predict(X)  

#visulaizing the clusters  
plt.scatter(X[y_predict == 0, 0], X[y_predict == 0, 1], s = 50, c = 'blue', label = 'Cluster 1') #for first cluster  
plt.scatter(X[y_predict == 1, 0], X[y_predict == 1, 1], s = 50, c = 'green', label = 'Cluster 2') #for second cluster  
plt.scatter(X[y_predict== 2, 0], X[y_predict == 2, 1], s = 50, c = 'red', label = 'Cluster 3') #for third cluster  
plt.scatter(X[y_predict == 3, 0], X[y_predict == 3, 1], s = 50, c = 'cyan', label = 'Cluster 4') #for fourth cluster  
plt.scatter(X[y_predict == 4, 0], X[y_predict == 4, 1], s = 50, c = 'magenta', label = 'Cluster 5') #for fifth cluster  
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroid')   
plt.title('Clusters des Clients')  
plt.xlabel('Annual Income (k$)')  
plt.ylabel('Spending Score (1-100)')  
plt.legend()  
plt.show() 






































