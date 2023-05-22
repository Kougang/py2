class Espaces(object): 
    aa = 33 
    def affiche(self): 
        print(aa, Espaces.aa, self.aa) 
        
aa = 12 # 5
essai = Espaces() # 6
essai.aa = 67 # 7
essai.affiche()