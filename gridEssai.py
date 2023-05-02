
from tkinter import *
# fen1 = Tk()
# txt1 = Label(fen1, text = 'Premier champ :')
# txt2 = Label(fen1, text = 'Second :')
# entr1 = Entry(fen1)
# entr2 = Entry(fen1)

# txt1.grid(row =0)
# txt2.grid(row =1)

# L’option sticky peut prendre l’une des quatre valeurs N, S, W, E (les quatre
# points cardinaux en anglais). En fonction de cette valeur, on obtiendra un alignement des widgets par
# le haut, par le bas, par la gauche ou par la droite. Remplacez donc les deux premières instructions
# grid() du script par :

# txt1.grid(row =0, sticky =E)
# txt2.grid(row =1, sticky =E)

# entr1.grid(row =0, column =1)
# entr2.grid(row =1, column =1)
# fen1.mainloop()


from tkinter import *
fen1 = Tk()
# création de widgets 'Label' et 'Entry' :
# Utilisation de la méthode grid pour contrôler la disposition des widgets 97
txt1 = Label(fen1, text ='Premier champ :')
txt2 = Label(fen1, text ='Second :')
txt3 = Label(fen1, text ='Troisième :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)
# création d'un widget 'Canvas' contenant une image bitmap :
can1 = Canvas(fen1, width =400, height =400, bg ='white')
photo = PhotoImage(file ='CC.PNG')

# Les deux premiers arguments transmis (80, 80) indiquent les coordonnées x et y du canevas où il
# faut placer le centre de l’image. Les dimensions du canevas étant de 160x160, notre choix aboutira
# donc à un centrage de l’image au milieu du canevas.

item = can1.create_image(80, 80, image =photo)
# Mise en page à l'aide de la méthode 'grid' :
txt1.grid(row =1, sticky =E)
txt2.grid(row =2, sticky =E)
txt3.grid(row =3, sticky =E)
entr1.grid(row =1, column =2)
entr2.grid(row =2, column =2)
entr3.grid(row =3, column =2)
# Les deux premiers arguments indiquent que le canevas sera placé dans la première ligne de la
# troisième colonne. Le troisième (rowspan =3) indique qu’il pourra « s’étaler » sur trois lignes.
# Les deux derniers (padx =10, pady =5) indiquent la dimension de l’espace qu’il faut réserver
# autour de ce widget (en largeur et en hauteur).
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)
# démarrage :
fen1.mainloop()
