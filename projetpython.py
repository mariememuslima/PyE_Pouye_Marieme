
import csv
import datetime
import re
from ProjetPythonFonctions import*
import mysql.connector
from collections import Counter
#note
#Code
liste_eleves = []
TableauValide = []
TableauInvalide = []
TableauFinale = []
liste_entete = []
dictnom = {}
count = 0
########################################################
# RECUP CSV
########################################################
with open ('/home/marieme/Documents/TP/Python/Projet Pyhton/PyE_Pouye_Marieme/PyE_Pouye_Marieme/ProjetPython.csv','r',encoding="latin-1") as my_file:
    reader = csv.reader(my_file)
    for row in reader:
        if count==0:
            liste_entete = row[1:]
            liste_entete[3]='Date_de_naissance'
        else:
            if row[0]!='' and row[1]!='' and row[2]!='':
                verifier =dict(zip(liste_entete,row[1:]))
                liste_eleves.append(verifier)
        count+=1
count=0
########################################################
# Recupération Tableaux des élèves avec des infos valides
########################################################
for value in liste_eleves:
    r=value
    if 'invalid' in verifNom(value,1) or 'invalid' in verifNom(value,2) or 'invalid' in verifNom(value,3) or 'invalid' in verifFormatdate(value) or 'invalid' in verifClasse(value) or 'invalid' in verifNote(value):
        TableauInvalide.append(r)
        count+=1
    else :
        r = Uniformisation(r)
        TableauValide.append(r)  
########################################################
#LISTE AVEC MOYENNE
########################################################
Liste_Moyenne_Eleve=Tableau_Valide_Moyenne(TableauValide)
Menu()

########################################################
#
########################################################
# validité= input("saisissez 1 pour les tableaux valides et n'importe quel nombre pour les tableaux invalides")
# ans = True

# while ans == True : 
#     if int(validité) =="1": 
#         print(TableauValide) 
#     elif int(validité) =="2":
#         print(TableauInvalide) 
#     elif int(validité)=="3":
#         for i in range(len(TableauValide)):
#             for value in TableauValide[i].values():
#                 if (TableauValide[i]['Numero']) == validité :
#                     infos = value
#         print(infos) 
#     elif int(validité) =="4": 
#         print(TableauValide) 
#     elif int(validité) =="5": 
#         print(TableauValide) 
#     elif int(validité)=="6":
#         break
#     elif int(validité) !="":
#         ans == False
#numéro valide KMNLW0W


