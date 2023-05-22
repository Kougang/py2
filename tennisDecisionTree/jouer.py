from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# from sklearn.metrics import accuracy_score


# dataset
data = np.array([
    [1, 1, 1, 0, 0, 0],
    [2, 1, 1, 1, 0, 0],
    [3, 0, 1, 0, 1, 1],
    [4, 2, 1, 0, 1, 1],
    [5, 2, 0, 0, 1, 1],
    [6, 2, 0, 1, 0, 0],
    [7, 0, 0, 1, 1, 1],
    [8, 1, 2, 0, 0, 0],
    [9, 1, 0, 0, 1, 1],
    [10, 2, 2, 0, 1, 1],
    [11, 1, 2, 1, 1, 1],
    [12, 0, 2, 1, 1, 1],
    [13, 0, 1, 0, 1, 1],
    [14, 2, 2, 1, 0, 0]
])
# print(data)


# La variable profondeurMaximalDeArbre est initialisée avec le
# paramètre max_depth fixé à 10. Cette valeur peut être considérée 
# comme trop élevée pour l'exemple donné. En effet, il y a seulement 14
# observations dans l'ensemble de données, et une profondeur maximale 
# de 10 pourrait entraîner un surapprentissage. Il est recommandé de 
# fixer cette valeur à un nombre plus faible.

# profondeurMaximalDeArbre = DecisionTreeClassifier(max_depth=10)


profondeurMaximalDeArbre = DecisionTreeClassifier(max_depth=4)


# donnes sans etiquet
X_train = np.array([
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [2, 1, 0, 1],
    [2, 0, 0, 1],
    [2, 0, 1, 0],
    [0, 0, 1, 1]
    
])

# ou encore: X_train = data[:, :-1]
#            y_train = data[:, -1]

X_test = np.array([
    [1, 2, 0, 0],
    [1, 0, 0, 1],
    [2, 2, 0, 1],
    [1, 2, 1, 1],
    [0, 2, 1, 1],
    [0, 1, 0, 1],
    [2, 2, 1, 0]
])

y_test =  np.array(["non", "oui","oui", "oui", "oui", "oui", "non"])

# les etiquet
# y_train = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

y_train = np.array(["non", "non", "oui", "oui", "oui", "non", "oui"])



# Entraînez votre modèle en utilisant la méthode fit() de l'objet DecisionTreeClassifier :

profondeurMaximalDeArbre.fit(X_train, y_train)

# Évaluez les performances de votre modèle sur les données de test
# en utilisant la méthode score() de l'objet DecisionTreeClassifier :

y_perf=profondeurMaximalDeArbre.score(X_test, y_test)

print("performance du model:",y_perf)

# Enfin, une fois que vous êtes satisfait des performances de 
# votre modèle, vous pouvez l'utiliser pour faire des prédictions
# sur de nouvelles données en utilisant la méthode predict() de
# l'objet DecisionTreeClassifier :


# Faire des prédictions sur de nouvelles données
y_pred = profondeurMaximalDeArbre.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Précision du modèle : {:.2f}".format(accuracy))

# La fonction predict() et la fonction score() sont toutes deux des méthodes de l'objet DecisionTreeClassifier de la bibliothèque scikit-learn utilisé pour entraîner et évaluer un modèle d'arbre de décision.

# La fonction predict() est utilisée pour faire des prédictions sur de nouvelles données après que le modèle a été entraîné. Elle prend en entrée un ensemble de données (un tableau numpy) et renvoie une prédiction pour chaque observation de ce tableau. Par exemple, dans le code fourni, profondeurMaximalDeArbre.predict(X_test) renvoie les prédictions pour les données de test stockées dans X_test.

# La fonction score(), quant à elle, est utilisée pour évaluer les performances du modèle sur un ensemble de données. Elle prend en entrée un ensemble de données et les vraies étiquettes correspondantes, et renvoie le score de précision du modèle pour ces données. Par exemple, dans le code fourni, profondeurMaximalDeArbre.score(X_test, y_test) renvoie le score de précision du modèle pour les données de test stockées dans X_test et les étiquettes stockées dans y_test.

# En résumé, predict() renvoie les prédictions du modèle pour de nouvelles données, tandis que score() est utilisée pour évaluer la précision du modèle sur un ensemble de données existant.

# 
# La fonction accuracy_score() est une fonction de la bibliothèque scikit-learn qui permet de calculer la précision (accuracy) d'un modèle de classification. Elle prend en entrée les vraies étiquettes (y_true) et les étiquettes prédites (y_pred) et renvoie la précision du modèle. La précision est définie comme le nombre de prédictions correctes divisé par le nombre total de prédictions.

# La fonction score() de la classe DecisionTreeClassifier renvoie également la précision du modèle, mais elle prend en entrée uniquement les données de test et les étiquettes correspondantes, et calcule la précision en interne en faisant appel à la fonction predict().

# Ainsi, la fonction accuracy_score() peut être utilisée pour évaluer la précision de n'importe quel modèle de classification, alors que la fonction score() est spécifique à la classe DecisionTreeClassifier de scikit-learn.

# =======================partie graphique====================

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 8), dpi=300)
plot_tree(profondeurMaximalDeArbre, feature_names=["Outlook", "Temperature", "Humidity", "Wind"], class_names=["Don't Play", "Play"], filled=True, ax=axes)
plt.show()

