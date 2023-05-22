class Domino(object):
    
    def __init__(self, v1=0, v2=0):
        self.a=v1
        self.b=v2
    
    def affiche_point(self):
        print("face A :",self.a, "face B:", self.b)
    
    def valeur(self):
        
        print("total des points :", self.a + self.b)
        
        return self.a+self.b


        

d = Domino(2,2)
d1 = Domino(3,4)


d.affiche_point()
print("une somme des sommes est", d.valeur() + d1.valeur())

liste_dominos = []
for i in range(7):
    liste_dominos.append(Domino(6, i))
    
print(liste_dominos[3])