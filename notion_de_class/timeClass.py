class Time(object):
    
    # la fonction ci dessous est un constructeur qui initialise le valuer
    # les valeurs des champs par defaut donc si a l instanciation la 
    # methode affiche_heure n est pas appele avec les arguments sur une 
    # instance de la classe alors alors le constructeur init se charge 
    # d initialiser ces champs par defaut
    
     
    def __init__(self, hh =12, mm =0, ss =0): 
        self.heure =hh
        self.minute =mm 
        self.seconde =ss
    
    "Nouvelle classe temporelle"
    def affiche_heure(self):
        print("{0}:{1}:{2}".format(self.heure, self.minute, self.seconde))
   
    
# ===================================================================
# ===================ZONE D'INSTANCIATION============================
# ===================================================================

now = Time()

now.affiche_heure()

now.heure = 2
now.minute = 4
now.seconde = 10

now.affiche_heure()

recreation = Time(10, 15, 18) #appel du constructeur a trois argument de la classe, les elements sont initialisé et transmis a la methode d affichage
recreation.affiche_heure()



