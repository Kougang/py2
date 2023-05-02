
from math import *




# a=1

# if(a>2): print(a,"plus grand que 2")
# else: print("2 plus grand que ",a)


embranchement="vertebres"
classe="mammiferes"
famille="felins"
ordre ="carnivores"


if embranchement == "vertebres": # 1
     if classe == "mammiferes": # 2
        if ordre == "carnivores": # 3
            if famille == "felins": # 4
                 print("c’est peut-être un chat") # 5
        print("c’est en tous cas un mammifère") # 6
     elif classe == "oiseaux": # 7
      print("c’est peut-être un canari") # 8
      print("la classification des animaux est complexe") 


                    # ETUDE DES BOUCLES 
# b=0                   
# while (b < 7): # (n’oubliez pas le double point !)
#     b= b + 1   # (n’oubliez pas l’indentation !)
#     print(b)

# e=1
# while(e<=16384):
    
#     d = e*1.65
    
#     print(e,"euro(s) = ", d ,"dollar(s)" )
    
#     e=e*2

s=1
while(s<7):
    if(s==1):
        print("*")
        s=s+1
    if(s==2):
        print("**")  
        s=s+1
    if(s==3):
        print("***") 
        s=s+1 
    if(s==4):
        print("****")
        s=s+1
    if(s==5):
        print("*****")
        s=s+1
    if(s==6):
        print("******")
        s=s+1
    if(s==7):
        print("*******")
        s=s+1
        
        # CHAINE DE CARRACTERES ET TABLEAU
        
# ch = "Christine"
#  print(ch[0], ch[3], ch[5])
# C i t

            # AUTRES STYLE

# a = 'Petit poisson'
# b = ' deviendra grand'
# c = a + b

            # LES LISTES
            
# jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
# print(jour)
# ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']


#               LES FONCTIONS INTEGRES
# LEN()->determine la longueur
# DEL()->supprimer un element
# AAPEND()->ajjout dans une liste


#                       ENTRE 

# print("Veuillez entrer un nombre positif quelconque : ", end=" ")
# ch = input()
# nn = int(ch) # conversion de la chaîne en un nombre entier
# print("Le carré de", nn, "vaut", nn**2)


# racine = sqrt(4) 
# print(racine)

# sinusx = sin(60) 
# print(sinusx)

#               VARIALBLE GOLBAL PEUT ETRE DEFINIT A L'INTERIEUR OU A L'EXTERIEUR D UNE FONCTION VIA LE MOT CLÉ  GLOBAL
        # exp: global a

def table(base):
    resultat = []               # resultat est d’abord une liste vide
    n = 1
    while n < 11:
        b = n * base
        resultat.append(b)      # ajout d’un terme à la liste
        n = n +1                # (voir explications ci-dessous)
    return resultat

a=table(2)

print(a)
