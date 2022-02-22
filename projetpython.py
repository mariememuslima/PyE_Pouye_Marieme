def verifNumero(numero):
    if numero.isalnum() and len(numero)==7 and numero.isupper():
        return('Valid')
    else:
        return('Invalid')

def verifNom(nom):
    if nom[0].isupper() and len(nom)>=2:
        return('Valid')
    else:
        return('Invalid')

def verifPrenom(prenom):
    if prenom[0].isupper() and len(prenom)>=3:
        return('Valid')
    else:
        return('Invalid')

import re
import datetime
def verifFormatdate(d):
    d=(re.split('[- :/;_.]', d))   
    jour = d[0]
    annee = d[2]
    if d[1].startswith('ja'):
        mois = "01"
    elif d[1].startswith('f'):
        mois = "02"
    elif d[1].startswith('mar'):
        mois = "03"
    elif d[1].startswith('av'):
        mois = "04"
    elif d[1].startswith('mai'):
        mois = "05"
    elif d[1].startswith('juin'):
        mois = "06"
    elif d[1].startswith('juil'):
        mois = "07"
    elif d[1].startswith('ao'):
        mois = "08"
    elif d[1].startswith('s'):
        mois = "09"
    elif d[1].startswith('o'):
        mois = "10"
    elif d[1].startswith('n'):
        mois = "11"
    elif d[1].startswith('d'):
        mois = "12"
    else:
        mois = d[1]
    try:
        mafe = datetime.datetime(int(annee),int(mois),int(jour)).strftime("%d/%m/%Y")
        return mafe
    except ValueError: 
        return 'Invalid'

def verifClasse(classes):
    firstclasse = lastclasse = ""
    classes = classes.strip()
    po = len(classes)
    if classes[0].isnumeric():
        if int(classes[0]) <= 6 and int(classes[0]) >= 3: 
            firstclasse = classes[0]
            if classes[po-1] == 'A' or classes[po-1] == 'B': 
                lastclasse = classes[po-1]
        else :
            False
    try:
        classes = firstclasse +"e "+ lastclasse
        return classes
    except False:
        return 'Invalid'
    
def verifNote(indexnote):
    liste = []
    moyenne_generale = 0
    if indexnote != '':
        if indexnote[0]=='#':
            indexnote = indexnote[1:]
        indexnote = indexnote.split('#')
        for i in range(len(indexnote)) :
            indexnotes = indexnote[i].split('[')
            matière = indexnotes[0]
            if indexnote[0] !='':
                notes = indexnotes[1].split(':')
            else:
                notes = indexnotes[2].split(':')
            devoirs = notes[0].split(';')
            composition = notes[1].split(']')
            composition = composition[0]
            composition = composition.replace(',','.')
            for i in range(len(devoirs)):
                devoirs[i] = devoirs[i].replace(',','.')
            if float(composition) >= 0 and float(composition) <= 20:
                composition = composition
                for i in range(len(devoirs)):
                    if float(devoirs[i]) >= 0 and float(devoirs[i]) <= 20:
                        devoirs[i] = devoirs[i]
                    else:
                        devoirs[i] = 'Invalid'
            else:
                composition = 'Invalid'
            notesdevoirs = {matière : [devoirs, composition]}
            mpo = len(indexnote)
            verif1 = ('Invalid' in devoirs)
            verif = False
            for value in notesdevoirs.values():
                if ('Invalid' in value):
                    verif = True
                    break
            if verif == False and verif1 == False:
                    pod = len(devoirs)
                    moyennedevoirs =0
                    for i in range (len(devoirs)):
                        moyennedevoirs += float(devoirs[i])
                    moyennedevoirs = (moyennedevoirs/pod)
                    moyenne = ((moyennedevoirs + (float(composition)*2))/3)
                    notesdevoirs['Moyenne'] = moyenne
            moyenne_generale+=moyenne

            liste.append(notesdevoirs)
            moyenne_generale1 = {'Moyenne Générale' : [(moyenne_generale/(len(indexnote)))]}
        liste.append(moyenne_generale1)
        return liste
    else:
        return indexnote

def Menu():
    print("Tapez 1 pour voir la liste des élèves valides")
    print("Tapez 2 pour voir la liste des élèves valides")
    print("Tapez le numéro d'un élève pour voir ses informations")
    print("Tapez 4 pour voir les cinq premiers de la liste")
    print("Tapez 5 pour modifier une information invalide")

import csv
import re
import datetime
tableaueleve = []
dictnom = {}
count = 0
dictionfinale = []
with open('ProjetPython.csv', mode='r') as inp:
    reader = csv.reader(inp)
    for row in reader:
        if count == 0:
            dictionfinale = row[1:]
        else:
            if row[0]!='' and row[1]!='' and row[2]!='':
                verifier = dict(zip(dictionfinale, row[1:]))
                tableaueleve.append(verifier)
        count += 1
for i in range (len(tableaueleve)):
    tableaueleve[i]['Nom'] = (tableaueleve[i]['Nom']).replace(',', '.')
TableauValide = []
TableauInvalide = []
#print(tableaueleve)
for i in range(len(tableaueleve)): 
    testnumero = verifNumero((tableaueleve[i]['Numero']))
    testnom = verifNom((tableaueleve[i]['Nom']))
    testprenom = verifPrenom((tableaueleve[i]['Prénom']))
    testclasse = verifClasse((tableaueleve[i]['Classe']))
    tableaueleve[i]['Classe']=testclasse
    try:
        testnote = verifNote((tableaueleve[i]['Note']))
        tableaueleve[i]['Note']=testnote
    except IndexError:
        tableaueleve[i]['Note']=tableaueleve[i]['Note']
    if testnumero == 'Valid' and testnom == 'Valid'and testprenom == 'Valid' and testclasse != 'Invalid':
        TableauValide.append(tableaueleve[i])
    else:
        TableauInvalide.append(tableaueleve[i])
classification =[]
#Rang/Moyenne
#for i in range(len(TableauValide)): 
 #   rang = verifRang((tableaueleve[i]))
  #  TableauValide.append(rang)
Menu()
validité= input("saisissez 1 pour les tableaux valides et n'importe quel nombre pour les tableaux invalides")
ans = True

while ans == True : 
    if int(validité) =="1": 
        print(TableauValide) 
    elif int(validité) =="2":
        print(TableauInvalide) 
    elif int(validité)=="3":
        for i in range(len(TableauValide)):
            for value in TableauValide[i].values():
                if (TableauValide[i]['Numero']) == validnuméro :
                    infos = value
        print(infos) 
    elif int(validité) =="4": 
        print(TableauValide) 
    elif int(validité) =="5": 
        print(TableauValide) 
    elif int(validité)=="6":
        break
    elif int(validité) !="":
        ans == False
#numéro valide KMNLW0W


