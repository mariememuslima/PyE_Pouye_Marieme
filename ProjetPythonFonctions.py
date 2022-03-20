import csv
import datetime
import re
#Fonctions
def verifNom(liste,choice):
    nom = liste['Nom']
    prenom = liste['Prénom']
    if choice == 1 and len(liste['Numero']) == 7 and liste['Numero'].isalnum():
        return liste['Numero']
    elif choice == 2 and len(nom)>1 and nom[0].isalpha():
        return nom
    elif choice == 3 and len(prenom)>4 and prenom[0].isalpha():
        return prenom
    else:
        return 'invalid'
def verifFormatdate(liste):
    d = liste['Date_de_naissance']
    d=d.strip()
    d=(re.split('[- :/;_.,]', d))   
    jour = d[0]
    annee = d[-1]
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
        mafe = datetime.datetime(int(annee),int(mois),int(jour)).strftime("%Y-%m-%d")
        return d
    except ValueError: 
        return 'invalid'
    except IndexError:
        return 'invalid'
def verifClasse(liste):
    n=True
    classes = liste['Classe']
    firstclasse = lastclasse = ""
    classes = classes.strip()
    if classes[0].isnumeric():
        if int(classes[0]) <= 6 and int(classes[0]) >= 3: 
            firstclasse = classes[0]
            if classes[-1] == 'A' or classes[-1] == 'B': 
                lastclasse = classes[-1]
            else:
                n=False
        else :
            n = False
    else:
        n=False
    if n == False:
        return 'invalid'
    else:
        classes = firstclasse +"e "+ lastclasse
        return classes
#note
def verifNote(liste):
    liste_t = []
    note = liste['Note']
    liste_eleves=[]
    if note != '':
        if note[0]=='#':
            note = note[1:]
        note = note.split('#')
        for i in range(len(note)):
            value = note[i].split('[')
            matiere = value[0]
            if matiere.startswith('f') or matiere.startswith('F'):
                matiere = 'Francais'
            elif matiere.startswith('m') or matiere.startswith('M'):
                matiere = 'Maths'
            elif matiere.startswith('a') or matiere.startswith('A'):
                matiere = 'Anglais'
            elif matiere.startswith('p') or matiere.startswith('P') or matiere.startswith('sc') or matiere.startswith('Sc'):
                matiere = 'PC'
            elif matiere.startswith('sv') or matiere.startswith('SV') or matiere.startswith('Sv'):
                matiere = 'SVT'
            elif matiere.startswith('h') or matiere.startswith('H'):
                matiere = 'HG'
            notes = value[-1].split(':')#SVT[13;12;14]
            if len(notes)==2:
                devoirs = notes[0].split(';')
                composition = notes[-1].split(']')
                composition = composition[0]
                liste_t = [matiere,devoirs,composition]
                for i in range(len(devoirs)):
                    devoirs[i] = devoirs[i].replace(',','.')
                    if float(devoirs[i]) >= 0 and float(devoirs[i]) <= 20:
                        devoirs[i] = devoirs[i]
                        if float(composition) >= 0 and float(composition) <= 20:
                            composition=composition
                        else:
                            liste_eleves = 'invalid'
                    else:
                        liste_eleves = 'invalid'
                if liste_eleves != 'invalid':
                    liste_eleves.append(liste_t)
                else:
                    liste_eleves='invalid'
            else:
                liste_eleves='invalid'
    else:
        liste_eleves = 'invalid'
    try:
        return liste_eleves
    except liste_eleves=='invalid':
        return 'invalid'
def Uniformisation(a_uni):
    d = a_uni['Date_de_naissance']
    d=d.strip()
    d=(re.split('[- :/;_.,]', d))   
    jour = d[0]
    annee = d[-1]
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
    a_uni['Date_de_naissance'] = datetime.datetime(int(annee),int(mois),int(jour)).strftime("%Y-%m-%d")
    classes = a_uni['Classe']
    firstclasse = lastclasse = ""
    classes = classes.strip()
    if classes[0].isnumeric():
        if int(classes[0]) <= 6 and int(classes[0]) >= 3: 
            firstclasse = classes[0]
            if classes[-1] == 'A' or classes[-1] == 'B': 
                lastclasse = classes[-1]
            else:
                n=False
        else :
            n = False
    else:
        n=False
    faire = firstclasse +"e "+ lastclasse
    a_uni['Classe'] = faire
    liste_t = []
    note = a_uni['Note']
    liste_eleves=[]
    if note != '':
        if note[0]=='#':
            note = note[1:]
        note = note.split('#')
        for i in range(len(note)):
            value = note[i].split('[')
            matiere = value[0]
            if matiere.startswith('f') or matiere.startswith('F'):
                matiere = 'Francais'
            elif matiere.startswith('m') or matiere.startswith('M'):
                matiere = 'Maths'
            elif matiere.startswith('a') or matiere.startswith('A'):
                matiere = 'Anglais'
            elif matiere.startswith('p') or matiere.startswith('P') or matiere.startswith('sc') or matiere.startswith('Sc'):
                matiere = 'PC'
            elif matiere.startswith('sv') or matiere.startswith('SV') or matiere.startswith('Sv'):
                matiere = 'SVT'
            elif matiere.startswith('h') or matiere.startswith('H'):
                matiere = 'HG'
            notes = value[-1].split(':')#SVT[13;12;14]
            if len(notes)==2:
                devoirs = notes[0].split(';')
                composition = notes[-1].split(']')
                composition = composition[0]
                liste_t = [matiere,devoirs,composition]
                for i in range(len(devoirs)):
                    devoirs[i] = devoirs[i].replace(',','.')
                    if float(devoirs[i]) >= 0 and float(devoirs[i]) <= 20:
                        devoirs[i] = devoirs[i]
                        if float(composition) >= 0 and float(composition) <= 20:
                            composition=composition
                        else:
                            liste_eleves = 'invalid'
                    else:
                        liste_eleves = 'invalid'
                if liste_eleves != 'invalid':
                    liste_eleves.append(liste_t)
                else:
                    liste_eleves='invalid'
            else:
                liste_eleves='invalid'
    else:
        liste_eleves = 'invalid'
    a_uni['Note'] = liste_eleves
    return a_uni
def Tableau_Valide_Moyenne(TableauValide):
    moyenne_eleve =0
    for row in TableauValide:
        notes=row['Note']
        for f in notes:
            devoirs = f[1]
            moyenne_devoirs = 0
            for g in devoirs:
                moyenne_devoirs+=float(g)
            real_moyenne = moyenne_devoirs / len(devoirs)
            examen = float(f[-1])
            moyenne_exam = (real_moyenne+(examen*2))/3
            moyenne_eleve+=moyenne_exam
        moyenne_eleve = moyenne_eleve/6
        row["Moyenne"] = moyenne_eleve
    return TableauValide

def Menu():
    print("Tapez 1 pour voir la liste des élèves valides")
    print("Tapez 2 pour voir la liste des élèves valides")
    print("Tapez le numéro d'un élève pour voir ses informations")
    print("Tapez 4 pour voir les cinq premiers de la liste")
    print("Tapez 5 pour modifier une information invalide")
