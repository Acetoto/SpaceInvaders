# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:34:27 2018

@author: noemie.rolland
"""

from  tkinter import *
from tkinter import messagebox
import math,random
from random import randint


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
        CreationTir()
        MouvTir()
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

#Création vaisseau
Dab=PhotoImage(file='Vaisseau3.gif')
Vaisseau=""
Canevas.focus_set()
Canevas.bind('s',Clavier)
Canevas.bind('d',Clavier)
Canevas.bind('l',Clavier)

#Création ilots
Bloc=PhotoImage(file='Bloc2.gif')
def CreationIlots(X,Y):
    Ilot=Canevas.create_image(X,Y,anchor=NW,image=Bloc)
    return Ilot
Ilots=""

#Création aliens
Caca=PhotoImage(file='CacaMulti.gif')
def CreationAliens(X,Y):
    Alien=Canevas.create_image(X,Y,anchor=NW,image=Caca)
    return Alien
Aliens=""

#Image laser
Arc=PhotoImage(file='Laser.gif')


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

def CreationTir():
    global PosX,PosY,Laser,VerifLaser
    XLaser=PosX
    YLaser1=PosY
    Laser=Canevas.create_image(XLaser,YLaser1,image=Arc)
    Canevas.unbind('l')
    VerifLaser=True
    VerificationLaser()
    
def MouvTir():
    global touche,YLaser,Laser,VerifLaser
    if VerifLaser:
        if Canevas.coords(Laser)[1]<=0:
            Canevas.bind('l',Clavier)
            Canevas.delete(Laser)
            VerifLaser=False
        else :
            Canevas.move(Laser,0,-30)
            Mafenetre.after(50,MouvTir)
        
def VerificationLaser():
    global VerifLaser
    if VerifLaser:
        DestructionLaser()
        Mafenetre.after(50,VerificationLaser)

def CreationTirAlien():
    global Aliens,TirAlien,YAlien
    TirAlien=[]
    i=randint(0,len(Aliens))
    XAlien=Canevas.coords(Aliens[i])[0]
    YAlien=Canevas.coords(Aliens[i])[1]
    TirAlien.append(Canevas.create_rectangle(XAlien,YAlien,XAlien+10,YAlien+25,fill='pink'))
    DestructionTirAlien()
    Mafenetre.after(2000,CreationTirAlien)

def MouvTirAlien():
    global Aliens,TirAlien,YAlien
    for k in range(len(TirAlien)):
        if YAlien>=900:
            Canevas.delete(TirAlien[k])
        else : 
            Canevas.move(TirAlien[k],0,30)
    Mafenetre.after(50,MouvTirAlien)

def DestructionLaser():
    global Laser,TirAlien,Aliens,Ilots,Vaisseau,VerifLaser
    #on cherche les éléments qui ont la même position que le laser
    collision=False
    x1Laser=Canevas.coords(Laser)[0]
    y1Laser=Canevas.coords(Laser)[1]
    x2Laser=x1Laser+30
    y2Laser=y1Laser+60
    Impact1=Canevas.find_overlapping(x1Laser,y1Laser,x2Laser,y2Laser)
    #retourne la liste des éléments touchés
    #suppression des éléments qui sont entrés en collision
    for i in Impact1:
        for i1 in Ilots:
            if i==i1:
                Canevas.delete(i1)
                collision=True
        for i2 in TirAlien:
            if i==i2:
                Canevas.delete(i2)
                collision=True
        for i3 in Aliens:
            if i==i3:
                Canevas.delete(i3)
                collision=True
        if collision:
            Canevas.delete(Laser)
            VerifLaser=False
            Canevas.bind('l',Clavier)
            return VerifLaser

def DestructionTirAlien():
    global Laser,TirAlien,Aliens,Ilots,Vaisseau,VerifLaser
    #on cherche les éléments qui ont la même position que les tirs des aliens
    if len(TirAlien)!=0:
        for j in TirAlien:
            x1TirAlien=Canevas.coords(j)[0]
            y1TirAlien=Canevas.coords(j)[1]
            x2TirAlien=Canevas.coords(j)[2]
            y2TirAlien=Canevas.coords(j)[3]
            Impact2=Canevas.find_overlapping(x1TirAlien,y1TirAlien,x2TirAlien,y2TirAlien) #retourne la liste des éléments touchés
            #suppression des éléments qui sont entrés en collision
            for k in Impact2:
                for k2 in Ilots:
                    if k==k2:
                        Canevas.delete(k)
                        Canevas.delete(j)
                if k==Vaisseau:
                    Canevas.delete(k)
                    Canevas.delete(j)
    Mafenetre.after(50,DestructionTirAlien)


def Jeu():
    global PosX,PosY,X,Y,XP,YP,dX,dY,VerifLaser,YLaser,Vaisseau,Ilots,Aliens
    Canevas.delete(Vaisseau)
    for i in Ilots:
        Canevas.delete(i)
    for i in Aliens:
        Canevas.delete(i)
    #Création vaisseau
    PosX=450
    PosY=650
    Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
    #Création ilots de défense
    Ilots=[]
    XIlot=45
    YIlot=500
    for i in range (0,54):
        Ilots.append(CreationIlots(XIlot,YIlot))
        if XIlot==195 or XIlot==510:
            XIlot+=135
        if XIlot==825:
            XIlot=45
            YIlot+=30
        else :
            XIlot+=30
    #Création aliens
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
    #Position initiale premier alien
    XP=200
    YP=0
    #direction initiale
    dX=4
    dY=0
    for i in range (0,18):
        Canevas.move(Aliens[i],dX,dY)
    #Conditions initiales
    VerifLaser=False
    YLaser=800
    #Lancement du jeu
    deplacement()
    CreationTirAlien()
    MouvTirAlien()


"""
Programme interface graphique
"""

#Création du bouton début jeu
BoutonJeu=Button(Mafenetre,text='Jouer',command = Jeu)

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
BoutonJeu.grid(row=2,column=2)
BoutonQuitter.grid(row=3,column=2)

Mafenetre.mainloop()
