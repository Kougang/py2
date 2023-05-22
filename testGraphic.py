
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np


data = np.array([
    [ 1, 1, 0, 0, 0],
    [ 1, 1, 1, 0, 0],
    [ 0, 1, 0, 1, 1],
    [ 2, 1, 0, 1, 1],
    [ 2, 0, 0, 1, 1],
    [2, 0, 1, 0, 0],
    [ 0, 0, 1, 1, 1],
    [ 1, 2, 0, 0, 0],
    [ 1, 0, 0, 1, 1],
    [ 2, 2, 0, 1, 1],
    [ 1, 2, 1, 1, 1],
    [ 0, 2, 1, 1, 1],
    [ 0, 1, 0, 1, 1],
    [ 2, 2, 1, 0, 0]
])

# X_train = data[:, :-1]
# y_train = data[:, -1]

X_train = np.array([
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [2, 1, 0, 1],
    [2, 0, 0, 1],
    [2, 0, 1, 0],
    [0, 0, 1, 1],
    # [ 1, 1, 0, 0, 0],
    # [ 1, 1, 1, 0, 0],
    # [ 0, 1, 0, 1, 1],
    # [ 2, 1, 0, 1, 1],
    # [ 2, 0, 0, 1, 1],
    # [2, 0, 1, 0, 0],
    # [ 0, 0, 1, 1, 1],
    # [ 1, 2, 0, 0, 0],
    # [ 1, 0, 0, 1, 1],
    # [ 2, 2, 0, 1, 1],
    # [ 1, 2, 1, 1, 1],
    # [ 0, 2, 1, 1, 1],
    # [ 0, 1, 0, 1, 1],
    # [ 2, 2, 1, 0, 0]
])
    
# ])

y_train = np.array(['Ne pas jouer', 'Ne pas jouer', 'Jouer','Jouer', 'Jouer', 
                    'Ne pas jouer','Jouer'])
                  
# y_test = np.array([ 'Ne pas jouer','Jouer','Jouer','Jouer','Jouer','Jouer','Ne pas jouer'  ])



clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 8), dpi=300)
plot_tree(clf, feature_names=['Temps', 'Temperature', 'Humidite', 'Vent'], class_names=['Ne pas jouer', 'Jouer'], filled=True, ax=axes)
plt.show()


# from sklearn.tree import DecisionTreeClassifier, export_graphviz
# # from sklearn.tree import export_graphviz

# # from IPython.display import Image
# import graphviz
# import pydotplus
# from IPython.display import Image
# import numpy as np


# # Création de l'arbre de décision

# X_train = np.array([
#     [1, 1, 0, 0],
#     [1, 1, 1, 0],
#     [0, 1, 0, 1],
#     [2, 1, 0, 1],
#     [2, 0, 0, 1],
#     [2, 0, 1, 0],
#     [0, 0, 1, 1]
    
# ])

# y_train = np.array(['Ne pas jouer', 'Ne pas jouer', 'Jouer','Jouer', 'Jouer', 'Ne pas jouer','Jouer'])

# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# # Export de l'arbre de décision au format DOT
# dot_data = export_graphviz(clf, out_file=None, 
#                            feature_names=['Temps', 'Temperature', 'Humidite', 'Vent'], 
#                            class_names=['Ne pas jouer', 'Jouer'],
#                            filled=True, rounded=True,
#                            special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data)

# # Affichage de l'arbre de décision
# Image(graph.create_png())