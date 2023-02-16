import xlrd
import pandas
import pandas as pd
import datetime

df = pandas.read_excel("vraiexcel.xls")


def creer_table_excel():
    date = input("Entrez une date (format JJ/MM/AAAA) : ")
    # Extraire le mois et l'année de la date entrée
    mois, annee = date.split("/")[1:]

    # Construire le nom de fichier du fichier Excel
    nom_fichier = "tab_{}_{}.xls".format(mois, annee)

    # Lire la première ligne du fichier Excel d'origine
    df = pd.read_excel("vraiexcel.xls", nrows=1)

    # Ajouter 100 colonnes supplémentaires
    for i in range(100):
        nom_colonne = "bulle{}".format(i+1)
        df[nom_colonne] = ""

    # Créer un nouveau fichier Excel et écrire la première ligne
    writer = pd.ExcelWriter(nom_fichier, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.close()

    print("Le fichier {} a été créé avec succès.".format(nom_fichier))



def ft_chercher_joueur():
    prenom = input("Entrez un prénom : ")
    nom = input("Entrez un nom de famille : ")
    date = input("Entrez une date (format JJ/MM/AAAA) : ")

    prenom = prenom.lower()
    nom = nom.lower()

    # Extract the month and year from the input date
    mois, annee = date.split("/")[1:]

    # Construct the filename of the Excel file
    nom_fichier = "tab_{}_{}.xls".format(mois, annee)

    try:
        # Read the Excel file
        df = pd.read_excel(nom_fichier)

        # Search for the player
        for index, row in df.iterrows():
            if (str(row[df.columns[0]]).lower() == nom):
                if(str(row[df.columns[1]]).lower() == prenom):
                    ft_information(row)
                    break
        else:
            print("Joueur non trouvé.")
    except FileNotFoundError:
        print("Le fichier correspondant au mois spécifié n'a pas été trouvé.")


def ft_ajouter_joueur():

    # Extraire le mois et l'année de la date courante
    now = datetime.datetime.now()
    mois, annee = now.strftime("%m/%Y").split("/")
    nom_fichier = "tab_{}_{}.xls".format(mois, annee)

    df = pd.read_excel(nom_fichier)
    # Déterminer le nombre de colonnes dans le DataFrame
    num_colonnes = df.shape[1]

    # Créer une liste avec le même nombre d'éléments que le nombre de colonnes dans le DataFrame
    new_row = [None] * num_colonnes

    # Remplacer les valeurs nulles par les valeurs réelles que vous souhaitez inclure dans la nouvelle ligne
    new_row[0] = input("Entrez un nom de famille : ")
    new_row[1] = input("Entrez un prénom : ")
    new_row[2] = input("Entrez le numéro de licence : ")
    new_row[3] = input("Entrez l'adresse : ")
    new_row[4] = input("Entrez le total des indemnités kilométriques : ")
    new_row[5] = input("Entrez le maxi 1 : ")
    new_row[6] = input("Entrez le reste à devoir : ")

    # Ajouter la nouvelle ligne au DataFrame
    df.loc[len(df)] = new_row

    df.to_excel(nom_fichier, index=False)

    print("Le joueur a été ajouté avec succès au fichier {}.".format(nom_fichier))



def affichage_tkt(df):
    for index, row in df.iterrows():
        print(row)

def ft_information(row):
    num_license = 2
    adresse = 4
    total_indemnité_kilometrique = 13
    maxi1 = 33
    reste_a_devoir = 64

    print("num_license = " + str(row[df.columns[num_license]]))
    print("adresse = " + str(row[df.columns[adresse]]))
    print("total_indemnité_kilometrique = " + str(row[df.columns[total_indemnité_kilometrique]]))
    print("maxi1 = " + str(row[df.columns[maxi1]]))
    print("reste_a_devoir = " + str(row[df.columns[reste_a_devoir]]))

def main():
    print("cherchez un joueur ou creé ?")
    choix = input("---- : ")
    if(choix == "cherchez"):
        ft_chercher_joueur()
    elif(choix == "creé"):
        print("creé match ou joueur ?")
        chois = input("---- : ")
        if(chois == "match"):
            creer_table_excel()
        elif(chois== "joueur"):
            ft_ajouter_joueur()
main()