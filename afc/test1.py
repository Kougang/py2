import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Chargement des données
diabetes = pd.read_csv('diabetes.csv')

# Séparation des données en variables indépendantes et dépendante
X = diabetes.drop('Outcome', axis=1)
y = diabetes['Outcome']

# Normalisation des données
X = (X - X.mean()) / X.std()

# Analyse factorielle des composantes (AFC)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Affichage graphique des données après l'AFC
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('Composante principale 1')
plt.ylabel('Composante principale 2')
plt.title('Données du diabète après l\'analyse factorielle des composantes')

# Entraînement d'un modèle de régression logistique sur les composantes principales
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Prédiction sur les données de test
y_pred = logreg.predict(X_test)

# Évaluation des performances du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}".format(accuracy))


