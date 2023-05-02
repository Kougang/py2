
# Détection et positionnement d'un clic de souris dans une fenêtre :
from tkinter import *


def cercle(x, y, r, coul ='green'):
    "tracé d'un cercle de centre (x,y) et de rayon r"
    
    cadre.create_oval(x-r, y-r, x+r, y+r, outline=coul)
   
    
rayon = 15    
def pointeur(event):
    # cadre.delette(ALL)
    
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
    ", Y =" + str(event.y))
    
    cercle(event.x, event.y, rayon)
    

 
fen = Tk()
cadre = Canvas(fen, width =200, height =200, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack(side =TOP, padx =5, pady =5)
chaine = Label(fen)
chaine.pack()
fen.mainloop()


# fen = Tk()
# can = Canvas(fen, width =200, height =200, bg ='ivory')
# can.pack(side =TOP, padx =5, pady =5)
# b1 = Button(fen, text ='dessin 1', command =figure_1)
# b1.pack(side =LEFT, padx =3, pady =3)
# b2 = Button(fen, text ='dessin 2', command =figure_2)
# b2.pack(side =RIGHT, padx =3, pady =3)
# fen.mainloop()
