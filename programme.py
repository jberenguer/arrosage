#coding:utf-8   #encodage du logiciel, utf 8 étant pour les langues latines
from tkinter import *   #importation de la bibliothèque tkinter

def crud_action_0():
    import mysql.connector as MC    #importation de mysqlconnector permettant d'établir une connexion entre la base de données MYSQL et Python 3
    try:
        conn = MC.connect(host = 'localhost', database = 'stephi_place_bd', user = 'root', password = '')    #on se connecte à la base de données
        cursor = conn.cursor()  #création d'un curseur de connexion

        window_1=Tk() #création de la fenêtre d'authentification
        window_1.title("Arrose'ta plante !")   #caractéristiques de la fenêtre : nom, taille, couleur de fond, icone.
        window_1.maxsize(1200, 600)
        window_1.minsize(1200, 600)
        window_1.configure(bg='#303030')

        window_1.mainloop()

    except MC.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

def see_values_action_0():
    import mysql.connector as MC    #importation de mysqlconnector permettant d'établir une connexion entre la base de données MYSQL et Python 3
    try:
        conn = MC.connect(host = 'localhost', database = 'stephi_place_bd', user = 'root', password = '')    #on se connecte à la base de données
        cursor = conn.cursor()  #création d'un curseur de connexion

        window_2=Tk() #création de la fenêtre d'authentification
        window_2.title("Arrose'ta plante !")   #caractéristiques de la fenêtre : nom, taille, couleur de fond, icone.
        window_2.maxsize(1200, 600)
        window_2.minsize(1200, 600)
        window_2.configure(bg='#303030')

        window_2.mainloop()

    except MC.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()


window_0=Tk() #création de la fenêtre d'authentification
window_0.title("Arrose'ta plante !")   #caractéristiques de la fenêtre : nom, taille, couleur de fond, icone.
window_0.maxsize(1200, 600)
window_0.minsize(1200, 600)
window_0.configure(bg='#303030')

# entrée des données
label_values_user = Label(window_0, width = 64, bg = "#d1a0ad", font = ("Helvetica", 11), text = "Entrez vos données relative à l'arrosage du jour :")
label_values_user.place(x = 300, y = 50)
date_value_user_0 = Entry(window_0, width = 25, bg = "#d1a0ad", font = ("Helvetica", 9))
date_value_user_0.place(x = 300, y = 100)
type_soil_value_user_0 = Entry(window_0, width = 25, bg = "#d1a0ad", font = ("Helvetica", 9))
type_soil_value_user_0.place(x = 500, y = 100)
vegetable_fruit_type_value_user_0 = Entry(window_0, width = 25, bg = "#d1a0ad", font = ("Helvetica", 9))
vegetable_fruit_type_value_user_0.place(x = 700, y = 100)

# bouttons de gestion
crud_button_0 = Button(window_0, width = 20, height = 2,bg = "#D5D5D5", font = ("Helvetica", 8), text = "CRUD", command = crud_action_0)
crud_button_0.place(x = 200, y = 200)
see_values_button_0 = Button(window_0, width = 100, height = 2,bg = "#D5D5D5", font = ("Helvetica", 8), text = "Quand dois-je arroser ?", command = see_values_action_0)
see_values_button_0.place(x = 350, y = 200)

window_0.mainloop()   #affichage de la fenêtre
