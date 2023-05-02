from sklearn.tree import DecisionTreeClassifier

import numpy as np

# Charger les données
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])

# Créer le modèle
clf = DecisionTreeClassifier()

# Entraîner le modèle sur les données
clf.fit(X, y)


# Prédire de nouvelles données
clf.predict([[2, 2]])
print('fin du script')
print(clf)
