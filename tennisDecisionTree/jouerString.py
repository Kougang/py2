from sklearn.tree import DecisionTreeClassifier
import numpy as np

profondeurMaximalDeArbre = DecisionTreeClassifier(max_depth=3)

X_train = np.array([
    
    # [1, 1, 1, 0, 0, 0],
    # [2, 1, 1, 1, 0, 0],
    # [3, 0, 1, 0, 1, 1],
    # [4, 2, 1, 0, 1, 1],
    # [5, 2, 0, 0, 1, 1],
    # [6, 2, 0, 1, 0, 0],
    # [7, 0, 0, 1, 1, 1],
    # [8, 1, 2, 0, 0, 0],
    # [9, 1, 0, 0, 1, 1],
    # [10, 2, 2, 0, 1, 1],
    # [11, 1, 2, 1, 1, 1],
    # [12, 0, 2, 1, 1, 1],
    # [13, 0, 1, 0, 1, 1],
    # [14, 2, 2, 1, 0, 0]
    
    ["1", "Ensoleille", 'chaude', 'élevée', 'faible'],
    ["2", "Ensoleille", 'chaude', 'élevée', 'fort'],
    ["3", "Couvert", 'chaude', 'élevée', 'faible'],
    ["4", "Pluie", 'tiède', 'élevée', 'faible'],
    ["5", "Pluie", 'fraîche', 'normale', 'faible'],
    ["6","Pluie", 'fraîche', 'normale', 'fort'],
    ["7", "Couvert", 'fraîche', 'normale', 'fort'],
    ["8", "Ensoleille", 'tiède', 'élevée', 'faible'],
    ["9", "Ensoleille", 'fraîche', 'normale', 'faible'],
    ["10", "Pluie", 'tiède', 'normale', 'faible'],
    ["11", "Ensoleille", 'tiède', 'normale', 'fort'],
    ["12", "Couvert", 'tiède', 'élevée', 'fort'],
    ["13", "Couvert", 'chaude', 'normale', 'faible'],
    ["14", "Pluie", 'tiède', 'élevée', 'fort']
])


# y_train = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])

# y_train = np.array(["non", "non", "oui", "oui", "oui", "non", "oui", "non", "oui","oui", "oui", "oui", "oui", "non"])

# profondeurMaximalDeArbre.fit(X_train, y_train)



# X_new = np.array([
    
#     [1, "Ensoleille", 'chaude', 'élevée', 'faible'],
#     [2, "Ensoleille", 'chaude', 'élevée', 'fort'],
#     [3, "Couvert", 'chaude', 'élevée', 'faible'],
#     [4, "Pluie", 'tiède', 'élevée', 'faible'],
#     [5, "Pluie", 'fraîche', 'normale', 'faible'],
#     [6,"Pluie", 'fraîche', 'normale', 'fort'],
#     [7, "Couvert", 'fraîche', 'normale', 'fort'],
#     [8, "Ensoleille", 'tiède', 'élevée', 'faible'],
#     [9, "Ensoleille", 'fraîche', 'normale', 'faible'],
#     [10, "Pluie", 'tiède', 'normale', 'faible'],
#     [11, "Ensoleille", 'tiède', 'normale', 'fort'],
#     [12, "Couvert", 'tiède', 'élevée', 'fort'],
#     [13, "Couvert", 'chaude', 'normale', 'faible'],
#     [14, "Pluie", 'tiède', 'élevée', 'fort']
# ])


X_new = np.array([
    [1, 1, 1, 0, 1],
    [2, 0, 1, 1, 0],
    [3, 0, 1, 1, 1],
    [4, 2, 1, 0, 1],
    [5, 2, 1, 0, 1],
    [6, 2, 0, 1, 0],
    [7, 0, 2, 0, 0],
    [8, 1, 2, 0, 0],
    [9, 1, 0, 0, 0],
    [10, 2, 2, 0, 1],
    [11, 1, 2, 1, 1],
    [12, 1, 2, 1, 1],
    [13, 0, 2, 0, 0],
    [14, 1, 1, 1, 1]

])

profondeurMaximalDeArbre.predict(X_new)

