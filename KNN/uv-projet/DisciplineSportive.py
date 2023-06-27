# 0=>football
# 1=>basket
# 2=>saut en hauteur
# 3=>handBall
# 4=>VolleyBall

def DefinitionInterne(el):
    if(el==0):
        return "football"
    if(el==1):
        return "basket"
    if(el==2):
        return "saut en hauteur"
    if(el==3):
        return "handBall"
    if(el==4):
        return "VolleyBall"
    else:
        return "discipline non prise en charge"
    

def DefaultDiscipline(element):
    tmp = DefinitionInterne(element)
    
    print("votre discipline sportive est:",tmp)
    print("=====================================")

def PerformancesCaptivantes(elem):
    tmp = DefinitionInterne(elem)
    print("cet(te) etudiant(e) peut integrer l'equipe universitaire en:",tmp)
    print("=====================================")
    
if __name__ == '__main__':
    PerformancesCaptivantes(0)