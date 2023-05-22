import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Chargement des données
data = load_breast_cancer()

# Création des tableaux numpy X et y pour l'entraînement du modèle
X = data.data
y = data.target

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




from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus

# Exportation du modèle sous forme de graphique Graphviz
dot_data = export_graphviz(tree, out_file=None, feature_names=data.feature_names, class_names=data.target_names, filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)

# Affichage du graphique
Image(graph.create_png())
