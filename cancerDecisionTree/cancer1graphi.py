import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Définition des tailles et des espacements des cadres
node_width = 150
node_height = 50
label_width = 80
label_height = 30
leaf_width = 100
leaf_height = 30
node_margin_x = 20
node_margin_y = 30
label_margin_x = 10
label_margin_y = 10
leaf_margin_x = 10
leaf_margin_y = 10

# Définition des couleurs des cadres
node_color = '#f8d7da'
label_color = '#d4edda'
leaf_color = '#cce5ff'
border_color = 'black'

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

# Transformation de la représentation textuelle en un dictionnaire de nœuds
tree_dict = {}
for line in tree_rules.split('\n'):
    if line.strip():
        node_id, feature_name, threshold, _, _, impurity, n_samples = line.split()
        if feature_name != '<=':
            feature_name += ' ' + threshold
        tree_dict[int(node_id)] = {'feature_name': feature_name, 'impurity': impurity, 'n_samples': n_samples}

# Fonction récursive pour dessiner chaque nœud, étiquette et feuille du graphe
# def draw_node(node_id, x, y, ax):
#     if node_id in tree_dict:
#         feature_name = tree_dict[node_id]['feature_name']
#         impurity = tree_dict[node_id]['impurity']
#         n_samples = tree_dict[node_id]['n_samples']
#         node_label = feature_name + '\nimpurity={:.2f}\nsamples={}'.format(float(impurity), int(n_samples))
#         node_rect = plt.Rectangle((x - node_width / 2, y - node_height / 2), node_width, node_height,
#         edgecolor=border_color, facecolor=leaf_color)

def draw_node(node_id, x, y, ax):
    if node_id in tree_dict:
        feature_name = tree_dict[node_id]['feature_name']
        impurity = tree_dict[node_id]['impurity']
        n_samples = tree_dict[node_id]['n_samples']
        node_label = feature_name + '\nimpurity={:.2f}\nsamples={}'.format(float(impurity), int(n_samples))
        node_rect = plt.Rectangle((x - node_width / 2, y - node_height / 2), node_width, node_height, edgecolor=border_color, facecolor=node_color)
        ax.add_patch(node_rect)
        text_x = x - label_width / 2 + label_margin_x
        text_y = y - label_height / 2 + label_margin_y
        ax.text(text_x, text_y, node_label, ha='left', va='top', fontsize=8, color='black')
        left_child_id = tree.children_left[node_id]
        right_child_id = tree.children_right[node_id]
        if left_child_id != right_child_id:
            child_x = x - node_margin_x / 2
            draw_node(left_child_id, child_x, y - node_height - node_margin_y, ax)
            child_x = x + node_margin_x / 2
            draw_node(right_child_id, child_x, y - node_height - node_margin_y, ax)
        else:
            leaf_value = tree.value[node_id][0]
            leaf_text = 'class={}\nvalue={}'.format(np.argmax(leaf_value), leaf_value)
            leaf_rect = plt.Rectangle((x - leaf_width / 2, y - leaf_height / 2), leaf_width, leaf_height, edgecolor=border_color, facecolor=leaf_color)
            ax.add_patch(leaf_rect)
            text_x = x - leaf_width / 2 + leaf_margin_x
            text_y = y - leaf_height / 2 + leaf_margin_y
            ax.text(text_x, text_y, leaf_text, ha='left', va='top', fontsize=8, color='black')
plt.show()