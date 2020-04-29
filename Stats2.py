##Pour les vehicules impliques
dict_vehicules_impliques = {"nb_automobile_camion_leger": 0,
                            "nb_camionLourd_tractRoutier": 0,
                            "nb_outil_equipement": 0,
                            "nb_tous_autobus_minibus": 0,
                            "nb_bicyclette": 0,
                            "nb_cyclomoteur": 0,
                            "nb_motocyclette": 0,
                            "nb_taxi": 0,
                            "nb_urgence": 0,
                            "nb_motoneige": 0,
                            "nb_VHR": 0,
                            "nb_autres_types": 0,
                            "nb_veh_non_precise": 0
                            }
dict_nom_vehicules = {"nb_automobile_camion_leger": "autos ou camoins legers",
                      "nb_camionLourd_tractRoutier": "camions lourds",
                      "nb_outil_equipement": "equipements sur route",
                      "nb_tous_autobus_minibus": "autobus",
                      "nb_bicyclette": "velos",
                      "nb_cyclomoteur": "cyclomoteurs",
                      "nb_motocyclette": "motos",
                      "nb_taxi": "taxis",
                      "nb_urgence": "vehicules d'urgence",
                      "nb_motoneige": "motoneiges",
                      "nb_VHR": "vehicules hors route",
                      "nb_autres_types": "vehicules autres",
                      "nb_veh_non_precise": "vehicules non precises"}
import csv
with open('accidents_2012_2018.csv') as csv_file2:
    accidents2 = csv.reader(csv_file2, delimiter=',')
    compteur2 = 0
    for ligne in accidents2:
        if compteur2==0:
            compteur2 += 1
        elif ligne[2][:4]!='2018':
            pass
        else:
            skipline=0
            for i in range(37,50):
                if ligne[i]=='':
                    skipline=1
                    continue
            if skipline==0:
                dict_vehicules_impliques["nb_automobile_camion_leger"] += int(ligne[37])
                dict_vehicules_impliques["nb_camionLourd_tractRoutier"] += int(ligne[38])
                dict_vehicules_impliques["nb_outil_equipement"] += int(ligne[39])
                dict_vehicules_impliques["nb_tous_autobus_minibus"] += int(ligne[40])
                dict_vehicules_impliques["nb_bicyclette"] += int(ligne[41])
                dict_vehicules_impliques["nb_cyclomoteur"] += int(ligne[42])
                dict_vehicules_impliques["nb_motocyclette"] += int(ligne[43])
                dict_vehicules_impliques["nb_taxi"] += int(ligne[44])
                dict_vehicules_impliques["nb_urgence"] += int(ligne[45])
                dict_vehicules_impliques["nb_motoneige"] += int(ligne[46])
                dict_vehicules_impliques["nb_VHR"] += int(ligne[47])
                dict_vehicules_impliques["nb_autres_types"] += int(ligne[48])
                dict_vehicules_impliques["nb_veh_non_precise"] += int(ligne[49])
    for key2 in dict_vehicules_impliques:
        print("il y a eu {} {} impliques dans des accidents en 2018".format(dict_vehicules_impliques[key2],dict_nom_vehicules[key2]))
    csv_file2.close()
