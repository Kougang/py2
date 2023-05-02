
from turtle import *
from triangle import*

def carre(taille, couleur,absc,ordo):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    
    c =0
    goto(absc,ordo)
    while c <4:
        down()
        forward(taille)
        right(90)
        c = c+1
    up()    


coulr=['green','blue','yellow','black','greenyellow','red']

cordo=[1,1,1,130,130,130,1,-130,-130,-130,180,180]


# for i in coulr:
#     for c in cordo:
#         while i:
#             carre(70,i,c,c+1)
#             break

carre(70,'green',1,1)
carre(70,'blue',90,1)
carre(70,'yellow',-90,1)
carre(70,'black',-170,1)
carre(70,'greenyellow',170,1)

traceTriangle('blue',"sankara",-170,170)
# carre(70,'red',1,200)