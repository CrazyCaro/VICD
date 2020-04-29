#accidents par jor de la semaine a montrel, en 2018
import csv
with open('accidents_2012_2018.csv') as csv_file:
    accidents=csv.reader(csv_file,delimiter=',')
    compteur=0
    dict_jr_sem_2018={}
    for ligne in accidents:
        if compteur==0:
            compteur=1
        else:
            if "2018/" in ligne[2]:
                if not ligne[1] in dict_jr_sem_2018:
                    dict_jr_sem_2018.update({ligne[1]:1})
                else:
                    dict_jr_sem_2018[ligne[1]]+=1
    jours={"DI":"dimanche",
           "LU":"lnudi",
           "MA":"mardi",
           "ME":"mercredi",
           "JE":"jeudi",
           "VE":"vendredi",
           "SA":"samedi"}
    for j in jours:
        print("Il y a eu {} accidents les {} en 2018".format(dict_jr_sem_2018[j],jours[j]))

    csv_file.close()
