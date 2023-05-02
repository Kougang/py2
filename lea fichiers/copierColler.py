# from os import

def copieFichier(sourc, dest):
    "copie intégrale d'un fichier" 
    
    try:
        fs = open(sourc, 'r')
        fd = open(dest, 'w')
        while 1:
            txt = fs.read(50)
            if txt =="":
                break
            fd.write(txt)
        fs.close()
        fd.close()
    
    except:
        print("quelque chose ne tourne pas rond")

copieFichier('source.txt','destination.txt')   


# f = open("Fichiertexte.txt", "w")
# f.write("Ceci est la ligne un\nVoici la ligne deux\n")
# f.write("Voici la ligne trois\nVoici la ligne quatre\n")
# f.close() 

#                   NOTES


# Lors des opérations de lecture, les lignes d’un fichier texte peuvent être
# extraites séparément les unes
# des autres. La méthode readline(), par exemple, ne lit qu’une seule ligne à la 
# fois (en incluant le
# caractère de fin de ligne) :

#  Notez bien que readline() est une méthode qui renvoie une chaîne de caractères,
#  alors que la
# méthode readlines() renvoie une liste. À la fin du fichier, readline() renvoie 
# une chaîne vide,
# tandis que readlines() renvoie une liste vide.