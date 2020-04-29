#Tableau eclairement14/localisation20
import csv
with open('accidents_2012_2018.csv') as csv_file6:
    accidents6=csv.reader(csv_file6,delimiter=',')
    compteur6=0
    dict_localisation={"31":"dans un rond point",
                       "32":"dans une intersection",
                       "33":"pres d'une intersection ou d'un rond point",
                       "34":"a 100 metres d'une intersection",
                       "35":"a un passage a niveau",
                       "36":"sur un pont",
                       "37":"sur un viaduc",
                       "38":"dans un tunnel",
                       "39":"sous un viaduc",
                       "40":"dans une zone circulable sans voies(ex:stationnement)",
                       "99":" dans un endroit autre"}
    dict_eclairages={"1":"le jour en pleine clarte",
                     "2":"le jour a demi-obscurite",
                     "3":"la nuit avec eclairage",
                     "4":"la nuit sans eclairage"}
    d1={"31":0,"32":0,"33":0,"34":0,"35":0,"36":0,"37":0,"38":0,"39":0,"40":0,"99":0}
    d2={"31":0,"32":0,"33":0,"34":0,"35":0,"36":0,"37":0,"38":0,"39":0,"40":0,"99":0}
    d3={"31":0,"32":0,"33":0,"34":0,"35":0,"36":0,"37":0,"38":0,"39":0,"40":0,"99":0}
    d4={"31":0,"32":0,"33":0,"34":0,"35":0,"36":0,"37":0,"38":0,"39":0,"40":0,"99":0}
    dict_eclairage_accidents={"1":d1,
                              "2":d2,
                              "3":d3,
                              "4":d4}
    for ligne6 in accidents6:
        if compteur6==0:
            compteur6+=1
        elif not ligne6[14]!='':
            pass
        elif not ligne6[20]!='':
            pass
        else:
            dict_eclairage_accidents[ligne6[14]][ligne6[20]]+=1
    csv_file6.close()
    print(dict_eclairage_accidents)
