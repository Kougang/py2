from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np


data = np.array([
    [ 1, 1, 0, 0, 0],
    [ 1, 1, 1, 0, 0],
    [ 0, 1, 0, 1, 1],
    [ 2, 1, 0, 1, 1],
    [ 2, 0, 0, 1, 1],
    [2, 0, 1, 0, 0],
    [ 0, 0, 1, 1, 1],
    [ 1, 2, 0, 0, 0],
    [ 1, 0, 0, 1, 1],
    [ 2, 2, 0, 1, 1],
    [ 1, 2, 1, 1, 1],
    [ 0, 2, 1, 1, 1],
    [ 0, 1, 0, 1, 1],
    [ 2, 2, 1, 0, 0]
])

X_train = data[:, :-1]
y_train = data[:, -1]

# print(X_train)
# print(y_train)

clf = DecisionTreeClassifier(max_depth=10)
clf.fit(X_train, y_train)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 4), dpi=300)
plot_tree(clf, feature_names=["Outlook", "Temperature", "Humidity", "Wind"], class_names=["Don't Play", "Play"], filled=True, ax=axes)
plt.show()
