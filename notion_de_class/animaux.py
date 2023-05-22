class Mammifere(object):
    caract1 = "il allaite ses petits ;"
class Carnivore(Mammifere):
    caract2 = "il se nourrit de la chair de ses proies ;"
class Chien(Carnivore):
    caract3 = "son cri s'appelle aboiement ;"

m=Mammifere()
m.caract1
c = Carnivore()
c.caract2

ch = Chien()
ch.caract3
ch.caract2
ch.caract1