####Meteo/accidents de 2012 a 2018
import csv
with open('accidents_2012_2018.csv') as csv_file4:
    accidents4=csv.reader(csv_file4,delimiter=',')
    dict_meteo_detail={"11":"claire",
                       "12":"nuageuse",
                       "13":"brumeuse",
                       "15":"avec pluie forte",
                       "16":"avec vents forts",
                       "17":"avec neige ou grele",
                       "18":"avec tempete de neige ou poudrerie",
                       "19":"avec pluie verglassante",
                       "99":"autre"}
    dict_meteo_accident={}
    compteur4=0
    for ligne4 in accidents4:
        if compteur4==0:
            compteur4+=1
        else:
            if not ligne4[26] in dict_meteo_accident:
                dict_meteo_accident.update({ligne4[26]:1})
            else:
                dict_meteo_accident[ligne4[26]]+=1
    for key4 in dict_meteo_detail:
        print("Il y a eu {} accidents lors d'une meteo {}.".format(dict_meteo_accident[key4],dict_meteo_detail[key4]))
    csv_file4.close()
