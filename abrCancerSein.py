from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Charger les données de cancer du sein
cancer = load_breast_cancer()

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

# Créer un modèle d'arbre de décision
tree = DecisionTreeClassifier(max_depth=4, random_state=0)

# Entraîner le modèle sur les données d'entraînement
tree.fit(X_train, y_train)

# Faire des prédictions sur les données de test
y_pred = tree.predict(X_test)

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle : {:.2f}".format(accuracy))

# Bien sûr, voici un exemple plus complet d'un arbre de décision en
# Python. Dans cet exemple, nous allons utiliser le jeu de données
# "Breast Cancer Wisconsin" pour prédire si une tumeur est bénigne 
# ou maligne en fonction de ses caractéristiques. Nous allons 
# utiliser les mêmes étapes de préparation de données que dans 
# l'exemple précédent, puis entraîner et évaluer notre modèle d'arbre
# de décision :


# Dans cet exemple, nous avons chargé les données de cancer du sein à
# partir de la bibliothèque scikit-learn, divisé les données en 
# ensembles d'entraînement et de test à l'aide de la fonction 
# train_test_split, créé un modèle d'arbre de décision avec une 
# profondeur maximale de 4 à l'aide de la classe DecisionTreeClassifier,
# entraîné le modèle sur les données d'entraînement avec la méthode
# fit, fait des prédictions sur les données de test avec la méthode 
# predict, et calculé la précision du modèle à l'aide de la fonction
# accuracy_score. La précision est une mesure de performance qui 
# représente le pourcentage de prédictions correctes par rapport au
# nombre total de prédictions.
