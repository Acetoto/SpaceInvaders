# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:34:27 2018

@author: noemie.rolland
"""

from  Tkinter import *
from tkMessageBox import *
import math,random



"""
Fonctions
"""

#Déplacement de l'alien
def deplacement():
    global X,Y,dX,dY,Largeur,Hauteur
    #rebond à gauche
    if X-TailleAlien/2+dX<0:
        X=TailleAlien
        dX=-dX
        Y+=TailleAlien
    #rebond à droite
    if X-TailleAlien/2+dX>Largeur:
        X=Largeur-TailleAlien
        dX=-dX
        Y+=TailleAlien
    X=X+dX
    Y=Y+dY
    #affichage
    Canevas.coords(Alien,X-TailleAlien/2,Y-TailleAlien/2,X+TailleAlien/2,Y+TailleAlien/2)
    #déplacement
    Mafenetre.after(50,deplacement)

def Tir():
    global X,Y,Laser,Larg,Long,touche
    Canevas.unbind('l')
    Long=20
    Larg=5
    Y-=10
    Canevas.coords(Laser,X-Larg,Y-Long,X+Larg,Y+Larg)
    if Y<0:
        Canevas.bind('l',Clavier)
        Canevas.delete(Laser)
    else :
        Mafenetre.after(50,Tir)
    
def Laser():
    global PosX,PosY
    Long=20
    Larg=5
    X=PosX
    Y=PosY
    Laser=Canevas.create_rectangle(X-Larg,Y-Long,X+Larg,Y+Larg,fill='red')
    Tir()
    
def Clavier(event): #Gestion de l'évenement Appui sur une touche du clavier
    global PosX,PosY
    touche=event.keysym
    #déplacement vers la droite
    if touche=='d' :
        PosX+=20
    #déplacement vers la gauche
    if touche=='s' :
        PosX-=20
    if touche=='l':
        Laser()
    #on dessine le vaisseau à sa nouvelle place
    Canevas.coords(Vaisseau,PosX,PosY)
    
    

"""
Programme création affichage
"""

#Création de la fenêtre principale
Mafenetre=Tk()
Mafenetre.title('Space Invaders')

#Création du Canvas
Largeur=880
Hauteur=880
Canevas=Canvas(Mafenetre, height= Hauteur, width=Largeur,bg='white')
Fond=PhotoImage(file='Licorne2.gif')
Canevas.create_image(0,0,anchor=NW,image=Fond)


#Création aliens
TailleAlien=50
Alien=Canevas.create_rectangle(0,0,TailleAlien*2,TailleAlien*2,fill='pink')

#Création vaisseau
PosX=440
PosY=800
Dab=PhotoImage(file='Vaisseau.gif')
Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
Canevas.focus_set()
Canevas.bind('s',Clavier)
Canevas.bind('d',Clavier)
Canevas.bind('l',Clavier)


    
#Position initiale alien
X=0
Y=0

#direction initiale
dX=10
dY=0
Canevas.move(Alien,dX,dY)

    
    
"""
Programme principal
"""

#Création du bouton début jeu
#BoutonJeu=Button(Mafenetre,text='Jouer',command = Jeu)

#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Afichage score
#x=StringVar
#x.set(score())
#LabelScore=Label(Mafenetre,textvariable=x,fg='black',bg='white')

#Affichage vies
#y=StringVar
#y.set(vies())
#LabelVies=Label(Mafenetre,textvariable=y,fg='black',bg='white')

#Mise en page
#LabelScore.grid(row=1,column=1,sticky=W)
#LabelVies.grid(row=1,column=2,sticky=E)
Canevas.grid(row=2,column=1,rowspan=2)
#BoutonJeu.gid(row=2,column=2)
BoutonQuitter.grid(row=3,column=2)

deplacement()
Mafenetre.mainloop()