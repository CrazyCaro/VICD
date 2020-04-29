##Gravite des accidents (Nombre de vehicules moyen impliques, nombre de blesses legers a morts) il y a ausssi une col GRAVITE
import csv
with open('accidents_2012_2018.csv') as csv_file5:
    accidents5 = csv.reader(csv_file5, delimiter=',')
    dict_gravite_detail={"Dommages materiels inferieurs au seuil de rapportage":"degats materiels legers",
                         "Dommages materiels seulement":"degats considerables sans victimes",
                         "Leger":"victimes blessees legerement",
                         "Grave":"victimes blessees gravement",
                         "Mortel":"morts"}
    dict_gravite_pourcent={}
    compteur5 = -1
    for ligne5 in accidents5:
        if compteur5 == -1:
            compteur5 += 1
        else:
            if not ligne5[34] in dict_gravite_pourcent:
                dict_gravite_pourcent.update({ligne5[34]: 1})
            else:
                dict_gravite_pourcent[ligne5[34]] += 1
            compteur5+=1
    for key5 in dict_gravite_detail:
        dict_gravite_pourcent[key5]/=(compteur5/100)
        print("de 2012 a 2018,il y a eu {} % accidents avec {}.".format(dict_gravite_pourcent[key5], dict_gravite_detail[key5]))
