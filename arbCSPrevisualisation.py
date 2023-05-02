import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

# Charger les données de cancer du sein
cancer = load_breast_cancer()

# Obtenir les noms des caractéristiques
feature_names = cancer.feature_names

# Obtenir les étiquettes de classe
target_names = cancer.target_names

# Créer un sous-ensemble de données pour les caractéristiques sélectionnées
selected_features = ['mean radius', 'mean texture', 'mean area', 'mean concavity']
X = cancer.data[:, [feature_names.tolist().index(feature) for feature in selected_features]]

# Obtenir les étiquettes de classe
y = cancer.target

# Visualiser les caractéristiques sélectionnées
for feature_idx, feature_name in enumerate(selected_features):
    malignant = X[y == 0, feature_idx]
    benign = X[y == 1, feature_idx]

    plt.figure()
    plt.hist(malignant, bins=20, color='red', alpha=0.5, label='Malignant')
    plt.hist(benign, bins=20, color='blue', alpha=0.5, label='Benign')
    plt.xlabel(feature_name)
    plt.ylabel('Frequency')
    plt.title('Distribution of {} by Class'.format(feature_name))
    plt.legend()

# Afficher un diagramme de dispersion des caractéristiques sélectionnées
plt.figure()
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='red', label='Malignant')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='blue', label='Benign')
plt.xlabel(selected_features[0])
plt.ylabel(selected_features[1])
plt.title('Scatter Plot of {} vs {}'.format(selected_features[0], selected_features[1]))
plt.legend()

# Afficher les diagrammes en boîte des caractéristiques sélectionnées
plt.figure()
plt.boxplot([X[y == 0, 2], X[y == 1, 2]], labels=['Malignant', 'Benign'])
plt.xlabel('Class')
plt.ylabel(selected_features[2])
plt.title('Box Plot of {} by Class'.format(selected_features[2]))

# Afficher les graphiques
plt.show()

# Pour visualiser le jeu de données "Breast Cancer Wisconsin",
# vous pouvez utiliser différentes techniques de visualisation
# des données. L'une des approches courantes consiste à utiliser 
# la bibliothèque Matplotlib en combinaison avec des graphiques 
# tels que les diagrammes en barres, les diagrammes en boîte, ou 
# les diagrammes de dispersion. Voici un exemple qui utilise 
# Matplotlib pour afficher quelques visualisations de base :

# Cet exemple utilise les caractéristiques sélectionnées 'mean radius',
# 'mean texture', 'mean area', et 'mean concavity'. Il affiche un histogramme
# pour chaque caractéristique, montrant la distribution de chaque classe (maligne et bénigne). 
# Ensuite, un diagramme de dispersion est affiché pour mettre en évidence la relation entre les 
# deux premières caractéristiques. Enfin, un diagramme en boîte est affiché pour comparer la
# distribution de la troisième caractéristique entre les deux classes.