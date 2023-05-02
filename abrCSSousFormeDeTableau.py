import pandas as pd
from sklearn.datasets import load_breast_cancer

# Charger les données de cancer du sein
cancer = load_breast_cancer()

# Créer un dataframe pandas avec les données
df = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)

# Ajouter une colonne pour les étiquettes de classe
df['target'] = cancer.target

# Afficher les 10 premières lignes du dataframe
print(df.head(10))

# Oui, il est possible d'afficher le jeu de données "Breast Cancer 
# Wisconsin" sous forme de tableau à l'aide de la bibliothèque pandas.
# Voici un exemple de code qui utilise pandas pour afficher les données
# dans un tableau 

# Ce code crée un objet DataFrame à partir des données de cancer du 
# sein et utilise la méthode head() pour afficher les 10 premières
# lignes du dataframe. Le résultat devrait ressembler à ceci :