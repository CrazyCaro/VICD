### Pour nombre de victimes pietons et velos
import csv
with open('accidents_2012_2018.csv') as csv_file3:
    accidents3 = csv.reader(csv_file3, delimiter=',')
    dict_vict_velo={}
    dict_vict_pietons={}
    dict_nb_accidents={}
    compteur3 = 0
    for ligne in accidents3:
        if compteur3 < 1:
            compteur3 += 1
        else:
            if not ligne[2][:4] in dict_vict_velo:
                dict_vict_velo.update({ligne[2][:4]:int(ligne[58])})
                dict_vict_pietons.update({ligne[2][:4]:int(ligne[52])})
                dict_nb_accidents.update({ligne[2][:4]:1})
            else:
                dict_vict_velo[ligne[2][:4]]+=int(ligne[58])
                dict_vict_pietons[ligne[2][:4]]+=int(ligne[52])
                dict_nb_accidents[ligne[2][:4]]+=1
    for year in range(1950,3000):
        if str(year) in dict_nb_accidents:
            print("Sur {} accidents en {}, il y a eu comme victimes {} cyclistes et {} pietons.".format(dict_nb_accidents[str(year)],year,dict_vict_velo[str(year)],dict_vict_pietons[str(year)]))
    csv_file3.close()
