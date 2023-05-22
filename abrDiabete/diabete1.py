import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


# ================================================================================
# ======================DESCRIPTION DU DATASET ET DU CONTEXETE====================
# ================================================================================


# Voici un exemple de dataset dans le domaine médical :

# Le but est de prédire la présence d'un diabète chez un patient en fonction de 
# certaines caractéristiques. Les caractéristiques sont les suivantes :

# Number of times pregnant (Nombre de grossesses)
# Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
# (Concentration plasmatique de glucose 2 heures après un test de tolérance 
# au glucose oral)
# Diastolic blood pressure (Pression artérielle diastolique)
# Triceps skinfold thickness (Épaisseur du pli cutané du triceps)
# 2-Hour serum insulin (Insuline sérique à 2 heures)
# Body mass index (Indice de masse corporelle)
# Diabetes pedigree function (Fonction de généalogie du diabète)
# Age (Âge)
# Le dataset peut être téléchargé depuis le lien suivant :
# https://www.kaggle.com/uciml/pima-indians-diabetes-database




# Charger les données à partir du fichier CSV
data = np.loadtxt('diabetes.csv', delimiter=',', skiprows=1)

# Diviser les données en variables explicatives et variable cible
X = data[:, :-1]
y = data[:, -1]

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print( X_test)

# Créer et entraîner le classifieur d'arbre de décision
# clf = DecisionTreeClassifier(max_depth=3, random_state=42) #utilise cart pour la classification a cause de ces parametres

clf = DecisionTreeClassifier(criterion='entropy', max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# Prédire les classes pour l'ensemble de test
y_pred = clf.predict(X_test)

# Calculer la précision de la prédiction
accuracy = clf.score(X_test, y_test)
print("Précision de la prédiction : {:.2f}%".format(accuracy * 100))

# Afficher l'arbre de décision
plt.figure(figsize=(15, 10))
plot_tree(clf, filled=True, feature_names=['Nombre de grossesses',
    'Concentration plasmatique de glucose', 
    'Pression artérielle diastolique', 'Épaisseur du pli cutané du triceps', 
    'Insuline sérique à 2 heures', 'Indice de masse corporelle',
    'Fonction de généalogie du diabète', 'Âge'],class_names=['0', '1'],fontsize=9)

# plot_tree(clf, feature_names=diabetes.feature_names, class_names=["0", "1"], filled=True, fontsize=14, node_size=500)

plt.show()
