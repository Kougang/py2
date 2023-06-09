import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load the diabetes dataset
diabetes = np.loadtxt('diabetes.csv', delimiter=',')

# Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(diabetes[:, :-1], diabetes[:, -1], test_size=0.2)
X_train = diabetes[:, :-1]
y_train =diabetes[:, -1]
# train_test_split(diabetes[:, :-1], diabetes[:, -1])

X_test=np.array([
    [1,93,70,31,0,30.4,0.315,23]
])

y_test=np.array([0])



# Create an instance of the classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the data
knn.fit(X_train, y_train)

# Predict the class labels for the test set
y_pred = knn.predict(X_test)

# Get the distances and indices of the k nearest neighbors
distances, indices = knn.kneighbors(X_test, n_neighbors=3)

# Print the indices of the three nearest neighbors for each instance
print("differentes distance:")
print(distances)

print("Indices of the three nearest neighbors:")
print(indices)

# Get the classes of the three nearest neighbors
neighbor_classes = y_train[indices]

# Print the classes of the three nearest neighbors
print("Classes of the three nearest neighbors:")
print(neighbor_classes)

# print(tp)
# Plot the data points
# plt.figure()
# for i in range(len(X_test)):
#     color = 'red' if y_pred[i] != y_test[i] else 'blue'
#     plt.scatter(X_test[i, 0], X_test[i, 1], c=color)

# # Plot the training data points
# plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', marker='x', label='Training Data')

# plt.title('k-NN: Nearest Neighbors')
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.legend()
# plt.show()
