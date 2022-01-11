# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:34:27 2018

@author: noemie.rolland
"""

from  tkinter import *
import math,random
from random import randint,randrange

TirAlien=[]

def Clavier(event): #Gestion de l'évenement Appui sur une touche du clavier
    global PosX,PosY
    touche=event.keysym
    #déplacement vers la droite
    if touche=='d' :
        if PosX<850:
            PosX+=10
    #déplacement vers la gauche
    if touche=='s' :
        if PosX>50:
            PosX-=10
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

#Images
Bonus=PhotoImage(file='Bonus3.gif')
EnnemiBonus=""
Arc=PhotoImage(file='Laser4.gif')
Victoire=PhotoImage(file='Victoire3.gif')
Defaite=PhotoImage(file='Defaite2.gif')

Vies=3
Score=0
Morts=0


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
    for i in range(len(Aliens)):
        Canevas.coords(Aliens[i],X,Y)
        X+=100
        if i==5:
            X-=600
            Y+=100
        if i==11:
            X-=600
            Y+=100
    #déplacement
    Mafenetre.after(40,deplacement)

def CreationEnnemiBonus():
    global EnnemiBonus
    Canevas.move(EnnemiBonus,-10,0)
    Canevas.after(50,CreationEnnemiBonus)

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
    i=randint(0,len(Aliens)-1)
    XAlien=Canevas.coords(Aliens[i])[0]
    YAlien=Canevas.coords(Aliens[i])[1]
    TirAlien.append(Canevas.create_rectangle(XAlien,YAlien,XAlien+10,YAlien+25,fill='pink'))
    DestructionTirAlien()
    Mafenetre.after(1000,CreationTirAlien)

def MouvTirAlien():
    global Aliens,TirAlien,YAlien
    for k in range(len(TirAlien)):
        yTirAlien=Canevas.coords(TirAlien[k])[1]
        if yTirAlien>920:
            TirAlien.pop(k)
        else : 
            Canevas.move(TirAlien[k],0,30)
    Mafenetre.after(10,MouvTirAlien)

def DestructionLaser():
    global Laser,TirAlien,Aliens,Ilots,Vaisseau,VerifLaser,Score,Morts
    #on cherche les éléments qui ont la même position que le laser
    collision=False
    x1Laser=Canevas.coords(Laser)[0]
    y1Laser=Canevas.coords(Laser)[1]
    x2Laser=x1Laser+15
    y2Laser=y1Laser+45
    Impact1=Canevas.find_overlapping(x1Laser,y1Laser,x2Laser,y2Laser)
    #retourne la liste des éléments touchés
    #suppression des éléments qui sont entrés en collision
    for i in Impact1:
        for i1 in Ilots:
            if i==i1:
                Canevas.delete(i1)
                collision=True
                Score+=10
        for i2 in TirAlien:
            if i==i2:
                Canevas.delete(i2)
                collision=True
                Score+=20
        for i3 in Aliens:
            if i==i3:
                Canevas.delete(i3)
                collision=True
                Score+=50
                Morts+=1
            if Morts==18:
                Canevas.create_image(0,0,anchor=NW,image=Victoire)
        if collision:
            Canevas.delete(Laser)
            VerifLaser=False
            Canevas.bind('l',Clavier)
            return VerifLaser

def DestructionTirAlien():
    global Laser,TirAlien,Aliens,Ilots,Vaisseau,VerifLaser,Vies
    #on cherche les éléments qui ont la même position que les tirs des aliens
    if len(TirAlien)!=0:
        for j in TirAlien:
            n=Canevas.coords(j)
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
                        TirAlien.pop(TirAlien.index(j))
                if k==Vaisseau:
                    Canevas.delete(j)
                    TirAlien.pop(TirAlien.index(j))
                    Vies-=1
                    y.set("Vies restantes: "+str(Vies))
                    if Vies==0:
                        Canevas.delete(k)
                        Canevas.after_cancel(TirAlien)
                        Canevas.unbind('l')
                        Canevas.create_image(0,0,anchor=NW,image=Defaite)
    Mafenetre.after(10,DestructionTirAlien)

def Jeu():
    global PosX,PosY,X,Y,XP,YP,dX,dY,VerifLaser,YLaser,Vaisseau,Ilots,Aliens,EnnemiBonus,TirAlien,Vies,Score,Morts
    Canevas.delete(Vaisseau)
    for i in Ilots:
        Canevas.delete(i)
    for i in Aliens:
        Canevas.delete(i)
    Canevas.create_image(0,0,anchor=NW,image=Fond)
    Morts=0
    Vies=3
    y.set("Vies restantes: "+str(Vies))
    Score=0
    x.set("Score: "+str(Score))
    #Création vaisseau
    PosX=450
    PosY=650
    Vaisseau=Canevas.create_image(PosX,PosY,image=Dab)
    Canevas.bind('l',Clavier)
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
    dX=3
    dY=0
    for i in range (0,18):
        Canevas.move(Aliens[i],dX,dY)

    EnnemiBonus=Canevas.create_image(900,20,anchor=NW,image=Bonus)
    #Conditions initiales
    VerifLaser=False
    YLaser=800
    #Lancement du jeu
    deplacement()
    CreationTirAlien()
    MouvTirAlien()
    Mafenetre.after(randrange(60000,100000,100),CreationEnnemiBonus)


"""
Programme interface graphique
"""

#Création du bouton début jeu
BoutonJeu=Button(Mafenetre,text='Jouer',command = Jeu)

#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Afichage score
x=StringVar()
x.set("Score: "+str(Score))
LabelScore=Label(Mafenetre,textvariable=x,fg='black',bg='white')

#Affichage vies
y=StringVar()
y.set("Vies restantes: "+str(Vies))
LabelVies=Label(Mafenetre,textvariable=y,fg='black',bg='white')

#Mise en page
LabelScore.grid(row=1,column=1,sticky=W)
LabelVies.grid(row=1,column=2,sticky=E)
Canevas.grid(row=2,column=1,rowspan=2)
BoutonJeu.grid(row=2,column=2)
BoutonQuitter.grid(row=3,column=2)

Jeu()
Mafenetre.mainloop()
