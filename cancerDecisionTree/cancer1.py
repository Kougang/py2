import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Chargement de l'ensemble de données Breast Cancer Wisconsin Diagnostic
cancer_data = load_breast_cancer()

# Création des tableaux numpy X et y pour l'entraînement du modèle
X = cancer_data.data
y = cancer_data.target

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création d'un objet d'arbre de décision
tree = DecisionTreeClassifier()


# Entraînement du modèle
tree.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = tree.predict(X_test)

# Calcul de la précision de prédiction
accuracy = accuracy_score(y_test, y_pred)

print("Précision : {:.2f}%".format(accuracy * 100))

# Affichage de l'arbre de décision résultant
# tree_rules = export_text(tree, feature_names=cancer_data.feature_names.tolist())
# print("Règles de l'arbre de décision :")
# print(tree_rules)

# Affichage de l'arbre de décision
plt.figure(figsize=(20,10))
plot_tree(tree, filled=True, feature_names=X.columns, class_names=['0', '1'], fontsize=14)
plt.show()
