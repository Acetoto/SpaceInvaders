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
Largeur=880
Hauteur=880
Canevas=Canvas(Mafenetre, height= Hauteur, width=Largeur,bg='white')
Fond=PhotoImage(file='Licorne2.gif')
Canevas.create_image(0,0,anchor=NW,image=Fond)


#Création aliens
Caca=PhotoImage(file='CacaMulti.gif')
Alien=Canevas.create_image(100,50,image=Caca)

#Création vaisseau
PosX=440
PosY=700
Dab=PhotoImage(file='Vaisseau2.gif')
Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
Canevas.focus_set()
Canevas.bind('s',Clavier)
Canevas.bind('d',Clavier)
Canevas.bind('l',Clavier)

"""
Conditions initiales
"""

#Position initiale alien
X=0
Y=0

#direction initiale
dX=10
dY=0
Canevas.move(Alien,dX,dY)
    


"""
Fonctions
"""

#Déplacement de l'alien
def deplacement():
    global X,Y,dX,dY,Largeur,Hauteur
    TailleAlien=50
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
    Canevas.coords(Alien,X,Y)
    #déplacement
    Mafenetre.after(50,deplacement)

def Laser():
    global PosX,PosY
    Long=20
    Larg=5
    x=PosX
    y=PosY
    Laser=Canevas.create_rectangle(x-Larg,y-Long,x+Larg,y+Larg,fill='red')
    Tir()
    
def Tir():
    global PosX,PosY,Laser,touche,Larg,Long
    Long=20
    Larg=5
    Canevas.unbind('l')
    x=PosX
    y=PosY
    dx=0
    dy=-10
    if y<0:
        Canevas.bind('l',Clavier)
        Canevas.delete(Laser)
    else :
        Canevas.move(Laser,dx,dy)
    
    
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
