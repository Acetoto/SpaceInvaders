# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:34:27 2018

@author: noemie.rolland
"""

from  tkinter import *
from tkinter import messagebox
import math,random


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
Programme création
"""

#Création de la fenêtre principale
Mafenetre=Tk()
Mafenetre.title('Space Invaders')

#Création du Canvas
Largeur=900
Hauteur=900
Canevas=Canvas(Mafenetre, height= Hauteur, width=Largeur,bg='white')
Fond=PhotoImage(file='Licorne2.gif')
Canevas.create_image(0,0,anchor=NW,image=Fond)


#Création aliens
Caca=PhotoImage(file='CacaMulti.gif')
Alien1=Canevas.create_rectangle(200,200,250,250,fill='pink')
Alien2=Canevas.create_rectangle(400,200,450,250,fill='pink')
Aliens=[Alien1,Alien2]

#Création vaisseau
PosX=450
PosY=650
Dab=PhotoImage(file='Vaisseau3.gif')
Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
Canevas.focus_set()
Canevas.bind('s',Clavier)
Canevas.bind('d',Clavier)
Canevas.bind('l',Clavier)

#Image laser
Arc=PhotoImage(file='Laser.gif')

"""
Conditions initiales
"""

#Position initiale aliens
X=200
X1=200
Y1=200
X2=400
Y2=200

#direction initiale
dX=10
dY=0
Canevas.move(Alien1,dX,dY)
Canevas.move(Alien2,dX,dY)

PosBas=650
    


"""
Fonctions
"""

#Déplacement de l'alien
def deplacement():
    global X,X1,Y1,X2,Y2,dX,dY,Largeur,Hauteur
    TailleAlien=50
    X1=X
    #rebond à gauche
    if X1+dX<0:
        X1=0
        dX=-dX
        Y1+=TailleAlien
    #rebond à droite
    if X1+200+TailleAlien/2+dX>Largeur:
        X1=Largeur-TailleAlien-200
        dX=-dX
        Y1+=TailleAlien
    X1=X1+dX
    X=X1
    Y1=Y1+dY
    #affichage
    for i in range(0,2):
        Canevas.coords(Aliens[i],X1,Y1,X1+TailleAlien,Y1+TailleAlien)
        X1+=200
    #déplacement
    Mafenetre.after(50,deplacement)

def Laser():
    global PosX,PosY
    x=PosX
    y=PosY
    Laser=Canevas.create_image(x,y,image=Arc)
    Tir()
    
def Tir():
    global PosX,Laser,touche,PosBas
    Canevas.unbind('l')
    if PosBas<=0:
        Canevas.bind('l',Clavier)
        Canevas.delete(Laser)
    else :
        PosBas-=10
        Canevas.coords(Laser,PosX,PosBas)
        Mafenetre.after(50,Tir)
    
    
"""
Programme interface graphique
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
