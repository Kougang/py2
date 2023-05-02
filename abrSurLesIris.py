from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Charger les données d'iris
iris = load_iris()

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# Créer un modèle d'arbre de décision
tree = DecisionTreeClassifier(max_depth=3, random_state=0)

# Entraîner le modèle sur les données d'entraînement
tree.fit(X_train, y_train)

# Évaluer les performances du modèle sur les données de test
score = tree.score(X_test, y_test)
print("Score du modèle : {:.2f}".format(score))

# Un exemple simple de modèle d'arbre de décision que vous pouvez
# réaliser en Python est le modèle de classification d'Iris, qui
# prédit les espèces d'iris en fonction de leurs caractéristiques.
# Voici comment vous pouvez créer et entraîner un tel modèle à l'aide 
# de la bibliothèque scikit-learn :

# Dans cet exemple, nous avons chargé les données d'iris à partir de
# la bibliothèque scikit-learn, divisé les données en ensembles 
# d'entraînement et de test à l'aide de la fonction train_test_split,
# créé un modèle d'arbre de décision avec une profondeur maximale de 3 
# à l'aide de la classe DecisionTreeClassifier, entraîné le modèle sur
# les données d'entraînement avec la méthode fit, et évalué les performances
# du modèle sur les données de test à l'aide de la méthode score. Le score est une
# mesure de précision du modèle, qui représente le nombre de prédictions correctes
# par rapport au nombre total de prédictions.