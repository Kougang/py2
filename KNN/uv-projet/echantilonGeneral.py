import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# entete du csv: math,physique,informatique,chimie,philosophie,svt,hist,geo,ecm,anglais,sport,formation

# 0=>mathematicien
# 1=>physicien
# 2=>informaticien
# 3=>chimiste

diabetes = np.loadtxt('echantillonGeneral.csv', delimiter=',')

X_train = diabetes[:, :-1]
y_train =diabetes[:, -1]

X_test=np.array([
    [20,11,16,14,9,9,10,11,17,12,13]
])

y_test=np.array([0])

# Create an instance of the classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the data
knn.fit(X_train, y_train)

# Predict the class labels for the test set
y_pred = knn.predict(X_test)

# determiner la precision
accuracy = knn.score(X_test, y_test)
print("Précision de la prédiction : {:.2f}%".format(accuracy * 100))



# Get the distances and indices of the k nearest neighbors
n_neighbors=8
distances, indices = knn.kneighbors(X_test, n_neighbors)

# Print the indices of the three nearest neighbors for each instance

# print("differentes distance:")
# print(distances)

# print("Indices of the three nearest neighbors:")
# print(indices)

# Get the classes of the three nearest neighbors
neighbor_classes = y_train[indices]

# Print the classes of the three nearest neighbors

# print("Classes of the three nearest neighbors:")
# print(neighbor_classes)
mat=0  
ph=0  
inf=0 
ch=0
print('les',n_neighbors,' plus proche voisins sont :')
for row in neighbor_classes:
    for element in row:
        if(element==0.0):
            print("mathematicien")
            
            mat+=1
        if(element==1.0):
            print("physcien")
            
            ph+=1
        if(element==2.0):
                print("informaticien")
                
                inf+=1
        if(element==3.0):
            print("chimiste")
            
            ch+=1

maximum=max(mat,ph,inf,ch)

# print(maximum)

if(maximum==mat):
    print("plus disposé a faire une formation en mathematique")
if(maximum==ph):
    print("plus disposé a faire une formation en physique")
if(maximum==inf):
    print("plus disposé a faire une formation en informatique")
if(maximum==ch):
    print("plus disposé a faire une formation en chimie")
        
        
        
        


# for i in len(neighbor_classes):
#     print( 'essai personalisé',neighbor_classes[i])
