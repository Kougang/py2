from turtle import *

def traceTriangle(couleur,nom,absc,ordo):
    
     a=0
     goto(absc,ordo)
    
     
     while a <3:
         
        down()
        a = a +1
       
        color(couleur)
        forward(100)
        left(120)
        write(nom) 
     up()
     
     
    
# traceTriangle('blue','socrate',1,1)

# traceTriangle('red','sankara',150,100)

# traceTriangle('greenyellow','chinois',-150,-100)

# traceTriangle('green','majesté',1,100)