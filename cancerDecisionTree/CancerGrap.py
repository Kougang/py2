import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

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

# Génération de la représentation textuelle de l'arbre de décision
tree_rules = export_text(tree, feature_names=cancer_data.feature_names.tolist())

# Conversion de la représentation textuelle en une représentation graphique
tree_text_lines = tree_rules.split('\n')
fig, ax = plt.subplots()
ax.axis('off')
ax.set_title('Arbre de décision')
ax.annotate(tree_text_lines[0], xy=(0.5, 1), xytext=(0, 0),
            xycoords='axes fraction', textcoords='offset points',
            size='large', ha='center', va='center')
for i in range(1, len(tree_text_lines)):
    line = tree_text_lines[i]
    indent = len(line) - len(line.lstrip())
    parent_node_id = i - 1
    child_node_id = i
    ax.annotate(line.strip(), xy=(0.5, 1), xytext=(indent * -5, -child_node_id * 30),
                xycoords='axes fraction', textcoords='offset points',
                size='medium', ha='center', va='center',
                arrowprops=dict(arrowstyle='-', connectionstyle='arc3,rad=0'))


