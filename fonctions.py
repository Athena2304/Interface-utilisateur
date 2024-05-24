from main import *
from Classrooms import *
from tkinter import simpledialog
from Student_infos import *
#import des fonctions nécessaires


dict3 = {}
def reinitialise(root,photo,photo2,frame,new_classroom, noms, description, participation):
    """
    Description:
        Cette fonction permet de recommencer de 0 la salle créée
    Args:
        root: page principale
        photo: photo initiale (de la table)
        photo2: photo lorsqu'il y a un étudiant
        frame: l'espace ou sera situé la salle créé
        new_classroom: le bouton qui a permis de lancer la création de la salle
        noms: Stringvar qui sera utiliser pour stocker les noms des étudiants
        description:  Stringvar qui sera utiliser pour stocker la description des étudiants
        participation: Intvar qui sera utiliser pour stocker les notes des étudiants
    """
    erase = messagebox.askyesno("Recommencer","Voulez vous recommencer ? Votre travail ne sera pas sauvegardé", )
    if erase == True:
        classroom.destroy()
        restart.destroy()
        length_class(root,photo,photo2,frame,new_classroom, noms, description, participation)


def list_by_grades():
    """
    Description:
        Cette fonction permet de retourner les étudiants en fonctions classés en fonction de leurs notes (ordre décroissant)
    """
    dict4 = {}
    for i in salle.dictionnaire.values():
        try:
            dict4[salle.liste3[i].noms] = salle.liste3[i].participation
        except :
            continue
    noms_alph = []
    participation_alph = []
    for i in sorted(dict4.values(), reverse=True):
        valeur = str(i)
        participation_alph.append(valeur)
    for i in sorted(dict4.values(), reverse=True) :
        for key, value in dict4.items():
            if i == value :
                noms_alph.append(key)
                break
    page5 = Toplevel(bg="black")
    label1 = Label(page5, text= f" Noms : \n {"\n".join(noms_alph)}", font=("Nordic",13), bg="black", fg="white", relief="sunken")
    label1.grid(row=0, column=0)
    label2 = Label(page5, text=f" Participation : \n {"\n".join(participation_alph)}",font=("Nordic",13), bg="black", fg="white", relief="raised")
    label2.grid(row=0, column=1)
    close = Button(page5, text="Fermer", command= page5.destroy,borderwidth=3, bg="pink", font=("Nordic",12), relief="raised")
    close.grid(row=1, columnspan=2)
def list_by_name():
    """
        Description:
            Cette fonction permet de retourner les étudiants en fonctions classés en fonction de leurs noms
        """
    for i in salle.dictionnaire.values():
        try:
            salle.dictionnaire2[salle.liste3[i].noms] = salle.liste3[i].participation
        except :
            continue
    noms_alph = sorted(salle.dictionnaire2.keys())
    participation_alph = []
    for i in noms_alph:
        participation_alph.append(str(salle.dictionnaire2[i]))
    page5 = Toplevel(bg="black")
    label1 = Label(page5, text= f" Noms : \n {"\n".join(noms_alph)}", font=("Nordic",13), bg="black", fg="white", relief="sunken")
    label1.grid(row=0, column=0)
    label2 = Label(page5, text=f" Participation : \n {"\n".join(participation_alph)}",font=("Nordic",13), bg="black", fg="white", relief="sunken")
    label2.grid(row=0, column=1)
    close = Button(page5, text="Fermer", command= page5.destroy,borderwidth=3, bg="pink", font=("Nordic",12), relief="raised")
    close.grid(row=1, columnspan=2)


def determiner_classe(event):
    """
    Description:
        Determiner la salle concernée
    """
    global salle
    salle = dict3[event.widget]
    return salle
def create_classroom(root, photo, photo2, frame, new_classroom, noms, description, participation):
    """
        Description:
            Cette fonction permet de créer une salle avec pour étudiants des boutons qui une fois préssé afficheront les infos de l'étudiant
        Args:
            root: page principale
            photo: photo initiale (de la table)
            photo2: photo lorsqu'il y a un étudiant
            frame: l'espace ou sera situé la salle créé
            new_classroom: le bouton qui a permis de lancer la création de la salle
            noms: Stringvar qui sera utiliser pour stocker les noms des étudiants
            description:  Stringvar qui sera utiliser pour stocker la description des étudiants
            participation: Intvar qui sera utiliser pour stocker les notes des étudiants
        """
    global student, classroom, restart, liste3, liste2,liste,dict,dict2
    liste3 = []
    liste2 = []
    liste = []
    dict = {}
    dict2 = {}
    classroom = PanedWindow(root, bg="black")
    classroom.pack()
    for i in range(0, col_number):
        for j in range(0, row_number):
            classroom.rowconfigure(j, weight=1)
            eleve = Student_infos(classroom,noms,description, participation)
            classroom.columnconfigure(i, weight=1)
            student = Button(classroom, image=photo, borderwidth=5, bg="grey",command= lambda i=i, j=j, eleve=eleve: eleve.create_window(salle,photo2))
            student.grid(row=j+1, column=i, sticky="swen")
            liste.append(student)
            item = " "
            liste2.append(eleve)
            liste3.append(item)
    label = Label(classroom, text= class_name, font=("Nordic",12),background="pink",borderwidth=10)
    label.grid(row=0, columnspan=col_number,sticky="swen")
    index = 0
    for i in liste2:
        dict[i] = index
        index += 1
    restart = Button(frame, text="Nouvelle classe", command = lambda: reinitialise(root,photo,photo2,frame,new_classroom, noms, description, participation),borderwidth=3, bg="pink", font=("Nordic",12))
    restart.grid(row=0, column=1)
    new_classroom.destroy()
    add = Button(frame,text="Ajouter une classe", command = lambda :ajouter_classe(root,photo, photo2, frame, new_classroom, noms, description, participation),relief="raised",borderwidth=3, bg="pink", font=("Nordic",12))
    add.grid(row=0, column=0)
    menu_btn1 = Menubutton(classroom, text="Menu",relief="sunken",borderwidth=3, bg="pink", font=("Nordic",12))
    menu = Menu(menu_btn1, bg= "grey")
    menu.add_command(label="Elèves par ordre alphabétique ",command= list_by_name, activeforeground="pink")
    menu.add_command(label="Elèves par ordre de mérite ", command=list_by_grades , activeforeground="pink")
    menu_btn1.config(menu=menu)
    menu_btn1.grid(row=row_number+2, columnspan = col_number)
    salle = Class(liste,liste2,liste3,dict,dict2)
    dict3[menu_btn1] = salle
    menu_btn1.bind("<Button-1>", determiner_classe)
    for i in liste:
        dict3[i] = salle
        i.bind("<Button-1>", determiner_classe)



def length_class(root,photo,photo2,frame,new_classroom, noms, description, participation):
    """
        Description:
            Cette fonction demande à l'utilisateur les élements dont il aura besoin
        Args:
            root: page principale
            photo: photo initiale (de la table)
            photo2: photo lorsqu'il y a un étudiant
            frame: l'espace ou sera situé la salle créé
            new_classroom: le bouton qui a permis de lancer la création de la salle
            noms: Stringvar qui sera utiliser pour stocker les noms des étudiants
            description:  Stringvar qui sera utiliser pour stocker la description des étudiants
            participation: Intvar qui sera utiliser pour stocker les notes des étudiants
        """
    global row_number, col_number, class_name
    row_number = simpledialog.askinteger("Nombre de lignes", "Entrez le nombre de lignes",minvalue=1)
    col_number = simpledialog.askinteger("Nombre de colonnes", "Entrez le nombre de colonnes",minvalue=1)
    class_name = simpledialog.askstring("Nom de la salle", "Entrez le nom de la salle", initialvalue="Salle de classe")
    root.config(bg="black")
    create_classroom(root,photo,photo2,frame,new_classroom, noms, description, participation)

def ajouter_classe(root,photo,photo2,frame,new_classroom, noms, description, participation):
    """
        Description:
            Cette fonction d'ajoouter une deuxième salle à la page principale
        Args:
            root: page principale
            photo: photo initiale (de la table)
            photo2: photo lorsqu'il y a un étudiant
            frame: l'espace ou sera situé la salle créé
            new_classroom: le bouton qui a permis de lancer la création de la salle
            noms: Stringvar qui sera utiliser pour stocker les noms des étudiants
            description:  Stringvar qui sera utiliser pour stocker la description des étudiants
            participation: Intvar qui sera utiliser pour stocker les notes des étudiants
        """
    length_class(root,photo,photo2,frame,new_classroom, noms, description, participation)
