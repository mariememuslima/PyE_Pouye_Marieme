import csv
import datetime
import re
from fonctions_py_sql import*
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
unicite_classe = []
unicite_matiere = []
unicite_matiere1 = []
count = 0
########################################################
# RECUP CSV
########################################################
with open ('/home/marieme/Documents/Cursus/voir.csv','r',encoding="latin-1") as my_file:
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
        unicite_classe.append(r['Classe'])
        TableauValide.append(r)  
print(TableauValide[0])
########################################################
# CONNECT DATABASE
########################################################
db = mysql.connector.connect(
    host="localhost",
    user="marieme",
    password="marieme",
    database="ProjetPytHonCSV"   
)
mycursor = db.cursor()
########################################################
#
########################################################
Liste_Moyenne_Eleve=Tableau_Valide_Moyenne(TableauValide)

# for value in sql_matiere_1:
#     if matiere==value[-1]:
#         id_matiere = value[0]
#         for val in notes:
#             for k in val[1]:
########################################################
#
########################################################
unicite_classe1 = list(Counter(unicite_classe).keys())
unicite_matiere=TableauValide[0]
unicite_matiere=unicite_matiere['Note']
for k in unicite_matiere:
    unicite_matiere1.append(k[0])

    #done# nom_classe = row
    #done# mycursor.execute("INSERT INTO classe (nom_classe) VALUES (%s)",(nom_classe,))
########################################################
#INSERTION CLASSE
########################################################
# for row in TableauValide:
    # done# nom_classe = row['Classe']
########################################################
#INSERTION MATIERE
# done#for i in unicite_matiere1:
#done#     nom_matiere = i
#done#     mycursor.execute("INSERT INTO matiere (nom_matiere) VALUES (%s)",(nom_matiere,))
#done# for i in unicite_classe1:
########################################################

request_classe = "select id_classe,nom_classe from classe"
request_matiere = "select * from matiere"
request_moyenne = "select id_moyenne from moyenne order by id_moyenne"
with db.cursor() as c:
    c.execute(request_matiere)
    sql_matiere_1 = c.fetchall()
    c.execute(request_classe)
    sql_classe = c.fetchall()
    c.execute(request_moyenne)
    sql_moyenne = c.fetchall()
liste_id_moyenne = []
for im in sql_moyenne:
    liste_id_moyenne.append(im[0])
# for idm in liste_id_moyenne:
#     mycursor.execute("INSERT INTO eleve (id_moyenne) VALUES (%s)",(int(idm),))
########################################################
#
########################################################          

#print(sql_classe)
# with db.cursor() as c:
#     c.execute(request)
#     sql_classe = c.fetchall()
#print(sql_classe)
#DONE# with db.cursor() as c:
#DONE#     c.execute(request1)
#DONE#     sql_matiere = c.fetchall()

########################################################
#INSERTION ELEVE
########################################################
# for row in TableauValide:
    # done# id_eleve = row['Numero']
    # done# nom_eleve = row['Nom']
    # done# prenom_eleve = row['Prénom']
    # done# date_de_naissance = row['Date_de_naissance']
    # done# nom_classe = row['Classe']
    # done# for value in sql_classe:
    # done#     if nom_classe==value[-1]:
    # done#         id_classe = value[0]
    # done#         mycursor.execute("INSERT INTO eleve (id_eleve,nom,prenom,date_de_naissance,id_classe) VALUES (%s,%s,%s,%s,%s)",(id_eleve,nom_eleve,prenom_eleve,date_de_naissance,id_classe))
########################################################
#
########################################################
# for row in TableauValide:
#done#     id_eleve = row['Numero']
#done#     notes = row['Note']
#done#     matiere = notes[0]
#done#     matiere=matiere[0]
#done#     for value in sql_matiere_1:
#done#         if matiere==value[-1]:
#done#             id_matiere = value[0]
#done#             for val in notes:
#done#                 for k in val[1]:
#done#                     note = k
#done#                     type_note = 'devoir'
#done#                     mycursor.execute("INSERT INTO note (type_note,note,id_eleve,id_matiere) VALUES (%s,%s,%s,%s)", (type_note,note,id_eleve,id_matiere))                
#done#                 note = val[-1]
#done#                 type_note = 'exam'
#done#                 mycursor.execute("INSERT INTO note (type_note,note,id_eleve,id_matiere) VALUES (%s,%s,%s,%s)", (type_note,note,id_eleve,id_matiere))      
    # done#         mycursor.execute("INSERT INTO eleve (id_eleve,nom,prenom,date_de_naissance,id_classe) VALUES (%s,%s,%s,%s,%s)",(id_eleve,nom_eleve,prenom_eleve,date_de_naissance,id_classe))

########################################################
#INSERSION MOYENNE
########################################################
# for my in Liste_Moyenne_Eleve:
#     id_eleve = my['Numero']
#     moyenne_eleve=my['Moyenne']
#     mycursor.execute("INSERT INTO moyenne (moyenne_eleve,id_eleve) VALUES (%s,%s)",(moyenne_eleve,id_eleve))

db.commit()
