from tkinter import *
from Student import Student
from tkinter import messagebox


class Student_infos:
    def __init__(self, classroom, noms, description, participation):
        """
            Description:
                Cette classe permet de gerer les informations des etudiants
            Args:
                classroom: represente le Pannedwindow ou est la salle créer
                noms: Stringvar qui sera utiliser pour stocker les noms des étudiants
                description:  Stringvar qui sera utiliser pour stocker la description des étudiants
                participation: Intvar qui sera utiliser pour stocker les notes des étudiants
            """
        self.classroom = classroom
        self.noms = noms
        self.description = description
        self.participation = participation


    def get_information(self):
        """
        Description:
            Cette fonction permet de recupérer les informations remplies par l'utilisateur
        Return:
             information: dataclasse contenant les informations de l'étudiant

        """
        information = Student(self.noms.get(), self.description.get(), self.participation.get())
        return information

    def verifier_noms(self,salle, photo2):
        """
            Description:
                Cette fonction permet de vérifier si le nom des étudiants est différents sinon il ouvrira la page qui permet de le changer
            Args:
                  salle: la salle concernée
                  photo2: la photo2 de l'étudiant lorsque son nom sera rempli
        """
        index = salle.dictionnaire.get(self)
        count = salle.liste3.copy()
        count.pop(index)
        for i in count:
            try:
                if self.noms.get() == i.noms:
                    page2.destroy()
                    messagebox.showinfo("Information", f"{i.noms} existe dans la salle, veuillez choisir un autre nom")
                    self.create_window(salle, photo2)
                    break
            except:
                continue
        self.modify_information(self.get_information(), salle, photo2)


    def modify_information(self, information, salle, photo2):
        """
            Description:
                Cette fonction permet d'ouvrir une page ou s'affichera les informations de l'étudiant
            Args:
                information : la dataclasse contenant les informations de l'étudiant
                salle: la salle concernée
                photo2: la photo2 de l'étudiant lorsque son nom sera rempli
        """
        global page4
        try:
            page4.destroy()
        except:
            None
        page2.destroy()
        page4 = Toplevel(bg="black")
        label1 = Label(page4, text=f"Noms et prénoms : {information.noms}", font=("Nordic",13), bg="black", fg="white")
        label1.pack()
        label2 = Label(page4, text=f"Description : {information.description}", font=("Nordic",13), bg="black", fg="white")
        label2.pack()
        label3 = Label(page4, text=f"Participation : {information.participation}", font=("Nordic",13), bg="black", fg="white")
        label3.pack()
        bouton = Button(page4, text="Modifier", font=("Nordic",13), bg="pink", relief="raised", borderwidth=5)
        bouton.bind("<Button-1>", lambda event : self.create_window(salle, photo2))
        bouton.pack()
        bouton2 = Button(page4, text="Close", command=page4.destroy, font=("Nordic",13), bg="pink", relief="raised", borderwidth=5)
        bouton2.pack()
        info_eleve = Student(information.noms, information.description, information.participation)
        index = salle.dictionnaire.get(self)
        salle.liste3.pop(index)
        salle.liste3.insert(index, info_eleve)
        salle.liste[index].config(command = lambda : self.modify_information(salle.liste3[index], salle, photo2))
        if information.noms != "":
            salle.liste[index].config(image = photo2, text = salle.liste3[index].noms, compound="bottom" )
            if information.participation in range (0,8):
                salle.liste[index].config(bg="red")
            elif information.participation in range(8,13):
                salle.liste[index].config(bg="orange")
            elif information.participation in range(13,21):
                salle.liste[index].config(bg="green")



    def create_window(self, salle, photo2):
        """
            Description:
                Cette fonction permet d'ouvrir une page dans laquelle on peut modifier les informations de l'étudiant
            Args:
                salle: la salle concernée
                photo2: la photo2 de l'étudiant lorsque son nom sera rempli
        """
        global page2, information
        index = salle.dictionnaire.get(self)
        try:
            page4.destroy()
        except:
            None
        page2 = Toplevel(bg="black")
        page2.title("élève")
        page2.columnconfigure(0, weight=1)
        page2.rowconfigure(0, weight=1)
        page2.columnconfigure(1, weight=1)
        page2.rowconfigure(1, weight=1)
        page2.rowconfigure(3, weight=1)
        page2.rowconfigure(4, weight=1)
        scrollbar = Scrollbar(page2, orient=VERTICAL)
        lb1 = Label(page2, text="Nom(s) et prénom(s) :", font=("Nordic",13), bg="black", fg="white")
        lb1.grid(row=0, column=0)
        lb2 = Label(page2, text="Résumé :", font=("Nordic",13), bg="black",fg="white")
        lb2.grid(row=1, column=0)
        lb3 = Label(page2, text="Participation :", font=("Nordic",13), bg="black",fg="white")
        lb3.grid(row=3, column=0)
        entry_nom = Entry(page2, textvariable=self.noms, width=50, xscrollcommand= scrollbar.set, font=("Nordic",13), bg="pink")
        entry_nom.grid(row=0, column=1)
        text_desc = Entry(page2, textvariable= self.description, width=50, font=("Nordic",13), bg="pink")
        text_desc.grid(row=1, column=1)
        scale = Scale(page2, from_=0, to=20, orient=HORIZONTAL, variable=self.participation, font=("Nordic",13), bg="pink")
        scale.grid(row=3, column=1, sticky="swen")
        close = Button(page2, text="Enregistrer", command= lambda : self.verifier_noms(salle, photo2), font=("Nordic",13), bg="pink", relief="raised", borderwidth=5)
        close.grid(row=4, column=0)
        quitter =Button(page2,text="Fermer", command= page2.destroy, font=("Nordic",13), bg="pink", relief="raised", borderwidth=5)
        quitter.grid(row=4, column=1)
        try:
            self.noms.set(salle.liste3[index].noms)
            self.description.set(salle.liste3[index].description)
            self.participation.set(salle.liste3[index].participation)
        except :
            self.noms.set("")
            self.description.set("")
            self.participation.set(0)
        page2.wait_window()