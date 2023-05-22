class CompteBancaire():
    
    def __init__(self,nom='Dupont',solde=1000):
        self.nom=nom
        self.solde=solde
    
    def depot(self,somme):
        
        self.solde = self.solde + somme
        return self.solde
        
    def retrait(self,somme): 
        
        self.solde=self.solde-somme
        
        return self.solde
    
    def affiche(self):
        print("le nom du titulaire est",self.nom, "le solde courant est:",self.solde)
        
compte1 = CompteBancaire('Duchmol', 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()

