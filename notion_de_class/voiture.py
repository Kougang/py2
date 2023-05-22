class Voiture(object):
    
    def __init__(self,marque = 'Ford', couleur = 'rouge', pilote = 'personne', vitesse = 0):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse
    
    def choix_conducteur(self,nom='cette voiture n as pas de conducteur'):
        
        self.pilote = nom
        
        
    def accelerer(self,taux, duree):
        
        if(self.pilote == 'personne'):
            print("vous n etes pas autorisez!! car cette voiture n a pas de conducteur")
           
        else : 
            self.vitesse= taux*duree
            print("conductuer",self.pilote)

        
    def affiche_tout(self):
        print("marque:",self.marque,"couleur:",self.couleur,"piloté par", self.pilote, "ayant une vitesse de :", self.vitesse)
    
# v1 = Voiture()

# v1.affiche_tout()

a1 = Voiture('Peugeot', 'bleue')
a2 = Voiture(couleur = 'verte')
a3 = Voiture('Mercedes','blue','manick')

a1.choix_conducteur('Roméo')
# a2.choix_conducteur('Juliette')
# a2.accelerer(1.8, 12)
a3.accelerer(1.9, 11)


        
    
        
        