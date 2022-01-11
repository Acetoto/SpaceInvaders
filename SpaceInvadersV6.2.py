# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:34:27 2018

@author: noemie.rolland
"""

from  Tkinter import *
from tkMessageBox import *
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
def CreationAliens(X,Y):
    Alien=Canevas.create_image(X,Y,anchor=NW,image=Caca)
    return Alien
Aliens=[]
X=200
Y=0
for i in range (0,18):
    Aliens.append(CreationAliens(X,Y))
    if X==700:
        X=200
        Y+=100
    else :
        X+=100

#Création vaisseau
PosX=450
PosY=800
Dab=PhotoImage(file='Vaisseau3.gif')
Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
Canevas.focus_set()
Canevas.bind('s',Clavier)
Canevas.bind('d',Clavier)
Canevas.bind('l',Clavier)

#Création ilots
Bloc=PhotoImage(file='Bloc2.gif')
def CreationIlots(X,Y):
    Ilot=Canevas.create_image(X,Y,anchor=NW,image=Bloc)
    return Ilot
Ilots=[]
XIlot=45
YIlot=600
for i in range (0,54):
    Ilots.append(CreationIlots(XIlot,YIlot))
    if XIlot==195 or XIlot==510:
        XIlot+=135
    if XIlot==825:
        XIlot=45
        YIlot+=30
    else :
        XIlot+=30

#Image laser
Arc=PhotoImage(file='Laser.gif')

"""
Conditions initiales
"""

#Position initiale premier alien
XP=200
YP=0

#direction initiale
dX=6
dY=0
for i in range (0,18):
    Canevas.move(Aliens[i],dX,dY)

YLaser=800

"""
Fonctions
"""

#Déplacement de l'alien
def deplacement():
    global X,Y,XP,YP,dX,dY,Largeur,Hauteur
    TailleAlien=50
    X=XP
    Y=YP
    #rebond à gauche
    if X+dX<0:
        X=0
        dX=-dX
        Y+=TailleAlien
    #rebond à droite
    if X+500+TailleAlien+dX>Largeur:
        X=Largeur-TailleAlien-500
        dX=-dX
        Y+=TailleAlien
    #nouvelle direction
    X=X+dX
    XP=X
    Y=Y+dY
    YP=Y
    #affichage
    for i in range(0,18):
        Canevas.coords(Aliens[i],X,Y)
        X+=100
        if i==5:
            X-=600
            Y+=100
        if i==11:
            X-=600
            Y+=100
    #déplacement
    Mafenetre.after(50,deplacement)

def Laser():
    global PosX,PosY,touche,YLaser
    x=PosX
    y=PosY
    Laser=Canevas.create_image(x,y,image=Arc)
    XLaser=x
    Canevas.unbind('l')
    if YLaser<=0:
        Canevas.bind('l',Clavier)
        Canevas.delete(Laser)
        Mafenetre.after_cancel(Laser)
    else :
        YLaser-=10
        Canevas.delete(Laser)
        Laser=Canevas.create_image(XLaser,YLaser,image=Arc)
        print (XLaser)
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
