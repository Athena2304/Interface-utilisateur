from fonctions import *  #import des fonctions
from tkinter import *

def main():
    root = Tk() #creation de la page mère
    root.title("Gestionnaire d'étudiants")
    root.config(width=500,height=500)  #modification de la page mère
    noms = StringVar()
    description = StringVar()
    participation = IntVar() #creation des variables
    photo2 = PhotoImage(file="eleve.png")
    photo = PhotoImage(file="12.png") #definir les images qu'on utilisera
    frame = Frame(root,bg="black")
    frame.pack(side=BOTTOM)
    new_classroom = Button(frame, text="New classroom", command = lambda: length_class(root,photo,photo2,frame,new_classroom, noms, description, participation),relief="raised",borderwidth=3, bg="pink", font=("Nordic",12))
    new_classroom.grid(row=0, column=0) #bouton qui va permettre la creation de la première classe et agencement de celui ci
    quitter = Button(frame, text="Quitter", command=root.quit,relief="raised",borderwidth=3, bg="pink", font=("Nordic",12))
    quitter.grid(row=0, column=2) #agencement du bouton qui permet de quitter la page principale

    root.mainloop()

if __name__ == "__main__":  #lancement du code
    main()