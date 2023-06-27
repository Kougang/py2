import numpy as np
import DisciplineSportive

def filtrage(nomFichierCSV):
    
    print("fichier externe")
    
    filtre = np.loadtxt(nomFichierCSV, delimiter=',', skiprows=1)
    # print("travaillons sur le premier filtre",filtre)
    
    nbInscrit=filtre[13]
    nbrreussit = filtre[14]
    nbreEchec = nbInscrit - nbrreussit

    # print("le nombre d inscrit est :\n", nbInscrit)
    # print("le nombre d inscrit est :\n", nbrreussit)

    if(nbreEchec>=(nbInscrit/2)):
        print("PRECISION:__ce parcour demande une grande rigueur et beaucoup de travail")
        print("=====================================")
    else:
        print("CONFIRMATION:__vous pouvez suivre cette formation")
        print("=====================================")
        
    # competence sportive
    
    noteSport = filtre[10]
    discipline = filtre[11]
    # print("note de sport",noteSport)
    # print("la discipline est:",discipline)

    
    if(noteSport<=15):
        DisciplineSportive.DefaultDiscipline( discipline)
    else:
        DisciplineSportive.PerformancesCaptivantes(discipline)  
           

if __name__ == '__main__':
    filtrage('1.csv')

