# coding: utf-8
# On importe les modules nécessaires à la création du jeu 
import pygame
import random
from math import *
from pygame.locals import *
pygame.init()


pygame.display.set_caption("Choice") #Titre du jeu
pygame.display.set_icon(pygame.image.load("img/icon{}.png".format(random.randint(0,2)))) #Icone du jeu choisie aléatoirement entre 3
size = 800,550 # Taille de la fenêtre
fps = 60 #Vitesse du jeu en images par secondes
clock=pygame.time.Clock() #On défint "l'horloge" du jeu
 
#########################-  Texte du jeu  -############################

couleur_texte= 0, 0, 0 # noir
couleur_texte2= 14, 216, 31 # vert
couleur_texte3= 255, 0, 0 # rouge
couleur_texte4= 240, 197, 31 # or
couleur_texte5= 255, 255, 255 # blanc
police = pygame.font.Font(None, 50) # police et taille du texte

#########################-  Images du jeu  -###########################

logo = pygame.image.load("img/logo.png")
logorect = logo.get_rect()
go = pygame.image.load("img/go.png")
gorect = go.get_rect()
bg1 = pygame.image.load("img/bg1.png")
bg1rect = bg1.get_rect()
bg2 = pygame.image.load("img/bg2.png")
bg2rect = bg2.get_rect()
bg3 = pygame.image.load("img/bg3.png")
bg3rect = bg3.get_rect()
bg4 = pygame.image.load("img/bg4.png")
bg4rect = bg4.get_rect()
bg5 = pygame.image.load("img/bg5.png")
bg5rect = bg5.get_rect()
bg6 = pygame.image.load("img/bg6.png")
bg6rect = bg6.get_rect()
bg7 = pygame.image.load("img/bg7.png")
bg7rect = bg7.get_rect()
bg8 = pygame.image.load("img/bg8.png")
bg8rect = bg8.get_rect()
d1 = pygame.image.load("img/d1.png")
d1rect = d1.get_rect()
d2 = pygame.image.load("img/d2.png")
d2rect = d2.get_rect()
ch = pygame.image.load("img/ch.png")
chrect = ch.get_rect()
ch1 = pygame.image.load("img/ch1.png")
ch1rect = ch1.get_rect()
ch2 = pygame.image.load("img/ch2.png")
ch2rect = ch2.get_rect()
ch3 = pygame.image.load("img/ch3.png")
ch3rect = ch3.get_rect()
ch4 = pygame.image.load("img/ch4.png")
ch4rect = ch4.get_rect()
bs = pygame.image.load("img/bs.png")
bsrect = bs.get_rect()
c1 = pygame.image.load("img/c1.png")
c1rect = c1.get_rect()
c2 = pygame.image.load("img/c2.png")
c2rect = c2.get_rect()
c3 = pygame.image.load("img/c3.png")
c3rect = c3.get_rect()
c4 = pygame.image.load("img/c4.png")
c4rect = c4.get_rect()
c5 = pygame.image.load("img/c5.png")
c5rect = c5.get_rect()
c6 = pygame.image.load("img/c6.png")
c6rect = c6.get_rect()
hbgd = pygame.image.load("img/hbgd.png")
hbgdrect = hbgd.get_rect()
light = pygame.image.load("img/light.png")
lightrect = light.get_rect()
light2 = pygame.image.load("img/light2.png")
light2rect = light2.get_rect()
oya = pygame.image.load("img/oya.png")
oyarect = oya.get_rect()
zero = pygame.image.load("img/0zero.png")
zerorect = zero.get_rect()
un = pygame.image.load("img/1slime.png")
unrect = un.get_rect()
deux = pygame.image.load("img/2chauvesouris.png")
deuxrect = deux.get_rect()
trois = pygame.image.load("img/3espritdefeu.png")
troisrect = trois.get_rect()
quatre = pygame.image.load("img/4dragonkrok.png")
quatrerect = quatre.get_rect()
cinq = pygame.image.load("img/5ghost.png")
cinqrect = cinq.get_rect()
six = pygame.image.load("img/6ovni.png")
sixrect = six.get_rect()
sept = pygame.image.load("img/7yinyon.png")
septrect = sept.get_rect()
huit = pygame.image.load("img/8espritforet.png")
huitrect = huit.get_rect()

############################-  Combat  -################################

f1 = pygame.image.load("img/f1.png")
f1rect = f1.get_rect()
f2 = pygame.image.load("img/f2.png")
f2rect = f2.get_rect()
f3 = pygame.image.load("img/f3.png")
f3rect = f3.get_rect()
f4 = pygame.image.load("img/f4.png")
f4rect = f4.get_rect()
f5 = pygame.image.load("img/f5.png")
f5rect = f5.get_rect()
f6 = pygame.image.load("img/f6.png")
f6rect = f6.get_rect()
f7 = pygame.image.load("img/f7.png")
f7rect = f7.get_rect()
f8 = pygame.image.load("img/f8.png")
f8rect = f8.get_rect()
f9 = pygame.image.load("img/f9.png")
f9rect = f9.get_rect()
f10 = pygame.image.load("img/f10.png")
f10rect = f10.get_rect()
f11 = pygame.image.load("img/f11.png")
f11rect = f11.get_rect()
f12 = pygame.image.load("img/f12.png")
f12rect = f12.get_rect()
f13 = pygame.image.load("img/f13.png")
f13rect = f13.get_rect()
f14 = pygame.image.load("img/f14.png")
f14rect = f14.get_rect()
f15 = pygame.image.load("img/f15.png")
f15rect = f15.get_rect()
f16 = pygame.image.load("img/f16.png")
f16rect = f16.get_rect()
f17 = pygame.image.load("img/f17.png")
f17rect = f17.get_rect()
f18 = pygame.image.load("img/f18.png")
f18rect = f18.get_rect()
f19 = pygame.image.load("img/f19.png")
f19rect = f19.get_rect()
f20 = pygame.image.load("img/f20.png")
f20rect = f20.get_rect()
f21 = pygame.image.load("img/f21.png")
f21rect = f21.get_rect()
f22 = pygame.image.load("img/f22.png")
f22rect = f22.get_rect()
f23 = pygame.image.load("img/f23.png")
f23rect = f23.get_rect()
f24 = pygame.image.load("img/f24.png")
f24rect = f24.get_rect()
f25 = pygame.image.load("img/f25.png")
f25rect = f25.get_rect()
f26 = pygame.image.load("img/f26.png")
f26rect = f26.get_rect()
f27 = pygame.image.load("img/f27.png")
f27rect = f27.get_rect()
f28 = pygame.image.load("img/f28.png")
f28rect = f28.get_rect()
f29 = pygame.image.load("img/f29.png")
f29rect = f29.get_rect()
f30 = pygame.image.load("img/f30.png")
f30rect = f30.get_rect()
f31 = pygame.image.load("img/f31.png")
f31rect = f31.get_rect()
f32 = pygame.image.load("img/f32.png")
f32rect = f32.get_rect()
f33 = pygame.image.load("img/f33.png")
f33rect = f33.get_rect()
f34 = pygame.image.load("img/f34.png")
f34rect = f34.get_rect()
f35 = pygame.image.load("img/f35.png")
f35rect = f35.get_rect()
f36 = pygame.image.load("img/f36.png")
f36rect = f36.get_rect()
f37 = pygame.image.load("img/f37.png")
f37rect = f37.get_rect()
f38 = pygame.image.load("img/f38.png")
f38rect = f38.get_rect()
f39 = pygame.image.load("img/f39.png")
f39rect = f39.get_rect()
f40 = pygame.image.load("img/f40.png")
f40rect = f40.get_rect()
f41 = pygame.image.load("img/f41.png")
f41rect = f41.get_rect()
f42 = pygame.image.load("img/f42.png")
f42rect = f42.get_rect()
f43 = pygame.image.load("img/f43.png")
f43rect = f43.get_rect()
f44 = pygame.image.load("img/f44.png")
f44rect = f44.get_rect()
f45 = pygame.image.load("img/f45.png")
f45rect = f45.get_rect()
f46 = pygame.image.load("img/f46.png")
f46rect = f46.get_rect()
f47 = pygame.image.load("img/f47.png")
f47rect = f47.get_rect()
at1 = pygame.image.load("img/at1.png")
at1rect = at1.get_rect()
at2 = pygame.image.load("img/at2.png")
at2rect = at2.get_rect()
at3 = pygame.image.load("img/at3.png")
at3rect = at3.get_rect()
at4 = pygame.image.load("img/at4.png")
at4rect = at4.get_rect()
at5 = pygame.image.load("img/at5.png")
at5rect = at5.get_rect()
at6 = pygame.image.load("img/at6.png")
at6rect = at6.get_rect()
at7 = pygame.image.load("img/at7.png")
at7rect = at7.get_rect()
lvl1 = pygame.image.load("img/lvl1.png")
lvl1rect = lvl1.get_rect()
lvl2 = pygame.image.load("img/lvl2.png")
lvl2rect = lvl2.get_rect()

###########################-  Dialogues -###############################

dial1 = pygame.image.load("img/dial1.png")
dial1rect = dial1.get_rect()
dial2 = pygame.image.load("img/dial2.png")
dial2rect = dial2.get_rect()
dial3 = pygame.image.load("img/dial3.png")
dial3rect = dial3.get_rect()
dial4 = pygame.image.load("img/dial4.png")
dial4rect = dial4.get_rect()
dial5 = pygame.image.load("img/dial5.png")
dial5rect = dial5.get_rect()
dial6 = pygame.image.load("img/dial6.png")
dial6rect = dial6.get_rect()
dial7 = pygame.image.load("img/dial7.png")
dial7rect = dial7.get_rect()
dial8 = pygame.image.load("img/dial8.png")
dial8rect = dial8.get_rect()
dial9 = pygame.image.load("img/dial9.png")
dial9rect = dial9.get_rect()
dial10 = pygame.image.load("img/dial10.png")
dial10rect = dial10.get_rect()
dial11 = pygame.image.load("img/dial11.png")
dial11rect = dial11.get_rect()
dial12 = pygame.image.load("img/dial12.png")
dial12rect = dial12.get_rect()
dial13 = pygame.image.load("img/dial13.png")
dial13rect = dial13.get_rect()
dial14 = pygame.image.load("img/dial14.png")
dial14rect = dial14.get_rect()
dial15 = pygame.image.load("img/dial15.png")
dial15rect = dial15.get_rect()
dial16 = pygame.image.load("img/dial16.png")
dial16rect = dial16.get_rect()
dial17 = pygame.image.load("img/dial17.png")
dial17rect = dial17.get_rect()
dial18 = pygame.image.load("img/dial18.png")
dial18rect = dial18.get_rect()
dial19 = pygame.image.load("img/dial19.png")
dial19rect = dial19.get_rect()
dial20 = pygame.image.load("img/dial20.png")
dial20rect = dial20.get_rect()
dial21 = pygame.image.load("img/dial21.png")
dial21rect = dial21.get_rect()
dial22 = pygame.image.load("img/dial22.png")
dial22rect = dial22.get_rect()
dial23 = pygame.image.load("img/dial23.png")
dial23rect = dial23.get_rect()
dial24 = pygame.image.load("img/dial24.png")
dial24rect = dial24.get_rect()
dial25 = pygame.image.load("img/dial25.png")
dial25rect = dial25.get_rect()
dial26 = pygame.image.load("img/dial26.png")
dial26rect = dial26.get_rect()
dial27 = pygame.image.load("img/dial27.png")
dial27rect = dial27.get_rect()
dial28 = pygame.image.load("img/dial28.png")
dial28rect = dial28.get_rect()
dial29 = pygame.image.load("img/dial29.png")
dial29rect = dial29.get_rect()
dial30 = pygame.image.load("img/dial30.png")
dial30rect = dial30.get_rect()
dial31 = pygame.image.load("img/dial31.png")
dial31rect = dial31.get_rect()
dial32 = pygame.image.load("img/dial32.png")
dial32rect = dial32.get_rect()
dial33 = pygame.image.load("img/dial33.png")
dial33rect = dial33.get_rect()
dial34 = pygame.image.load("img/dial34.png")
dial34rect = dial34.get_rect()
dial35 = pygame.image.load("img/dial35.png")
dial35rect = dial35.get_rect()
dial36 = pygame.image.load("img/dial36.png")
dial36rect = dial36.get_rect()
dial37 = pygame.image.load("img/dial37.png")
dial37rect = dial37.get_rect()
dial38 = pygame.image.load("img/dial38.png")
dial38rect = dial38.get_rect()
dial39 = pygame.image.load("img/dial39.png")
dial39rect = dial39.get_rect()
dial40 = pygame.image.load("img/dial40.png")
dial40rect = dial40.get_rect()
dial41 = pygame.image.load("img/dial41.png")
dial41rect = dial41.get_rect()
dial42 = pygame.image.load("img/dial42.png")
dial42rect = dial42.get_rect()
dial43 = pygame.image.load("img/dial43.png")
dial43rect = dial43.get_rect()
dial44 = pygame.image.load("img/dial44.png")
dial44rect = dial44.get_rect()
dial45 = pygame.image.load("img/dial45.png")
dial45rect = dial45.get_rect()
dial46 = pygame.image.load("img/dial46.png")
dial46rect = dial46.get_rect()
dial47 = pygame.image.load("img/dial47.png")
dial47rect = dial47.get_rect()
dial48 = pygame.image.load("img/dial48.png")
dial48rect = dial48.get_rect()
dial49 = pygame.image.load("img/dial49.png")
dial49rect = dial49.get_rect()
dial50 = pygame.image.load("img/dial50.png")
dial50rect = dial50.get_rect()
dial51 = pygame.image.load("img/dial51.png")
dial51rect = dial51.get_rect()
dial52 = pygame.image.load("img/dial52.png")
dial52rect = dial52.get_rect()
dial53 = pygame.image.load("img/dial53.png")
dial53rect = dial53.get_rect()
dial54 = pygame.image.load("img/dial54.png")
dial54rect = dial54.get_rect()
dial55 = pygame.image.load("img/dial55.png")
dial55rect = dial55.get_rect()
dial56 = pygame.image.load("img/dial56.png")
dial56rect = dial56.get_rect()
dial57 = pygame.image.load("img/dial57.png")
dial57rect = dial57.get_rect()
dial58 = pygame.image.load("img/dial58.png")
dial58rect = dial58.get_rect()
dial59 = pygame.image.load("img/dial59.png")
dial59rect = dial59.get_rect()
dial60 = pygame.image.load("img/dial60.png")
dial60rect = dial60.get_rect()
dial61 = pygame.image.load("img/dial61.png")
dial61rect = dial61.get_rect()


################-  Images déplacement du personnage  -##################

df1 = pygame.image.load("img/df1.png")
df1rect = df1.get_rect()
df2 = pygame.image.load("img/df2.png")                  #face
df2rect = df2.get_rect()
df3 = pygame.image.load("img/df3.png")
df3rect = df3.get_rect()
db1 = pygame.image.load("img/db1.png")
db1rect = db1.get_rect()
db2 = pygame.image.load("img/db2.png")                   #dos
db2rect = db2.get_rect()
db3 = pygame.image.load("img/db3.png")
db3rect = db3.get_rect()
dl1 = pygame.image.load("img/dl1.png")
dl1rect = dl1.get_rect()
dl2 = pygame.image.load("img/dl2.png")                  #gauche
dl2rect = dl2.get_rect()
dl3 = pygame.image.load("img/dl3.png")
dl3rect = dl3.get_rect()
dr1 = pygame.image.load("img/dr1.png")
dr1rect = dr1.get_rect()
dr2 = pygame.image.load("img/dr2.png")                  #droite
dr2rect = df2.get_rect()
dr3 = pygame.image.load("img/dr3.png")
dr3rect = dr3.get_rect()

#########################-  SFX du jeu  -##############################

avilis1 = pygame.mixer.Sound("sound/avilis1.mp3")
avilis2 = pygame.mixer.Sound("sound/avilis2.wav")
avilisburst1 = pygame.mixer.Sound("sound/avilisburst1.wav")
avilisburst2 = pygame.mixer.Sound("sound/avilisburst2.wav")
batsound = pygame.mixer.Sound("sound/batsound.mp3")
click = pygame.mixer.Sound("sound/click.wav")
damage = pygame.mixer.Sound("sound/damage.wav")
damagemagic = pygame.mixer.Sound("sound/damagemagic.wav")
dragonsound = pygame.mixer.Sound("sound/dragonsound.wav")
feysound = pygame.mixer.Sound("sound/feysound.wav")
firesound = pygame.mixer.Sound("sound/firesound.wav")
firespiritsound = pygame.mixer.Sound("sound/firespiritsound.wav")
ghostsound = pygame.mixer.Sound("sound/ghostsound.wav")
healsound = pygame.mixer.Sound("sound/healsound.wav")
magicsound = pygame.mixer.Sound("sound/magicsound.ogg")
ovnisound = pygame.mixer.Sound("sound/ovnisound.wav")
powersound = pygame.mixer.Sound("sound/powersound.wav")
slimesound= pygame.mixer.Sound("sound/slimesound.ogg")
sword1 = pygame.mixer.Sound("sound/sword1.wav")
sword2 = pygame.mixer.Sound("sound/sword2.wav")
sword3 = pygame.mixer.Sound("sound/sword3.wav")
sword4 = pygame.mixer.Sound("sound/sword4.wav")
sword5 = pygame.mixer.Sound("sound/sword5.wav")
treesound = pygame.mixer.Sound("sound/treesound.ogg")
winsound = pygame.mixer.Sound("sound/winsound.wav")
yinyonsound = pygame.mixer.Sound("sound/yinyonsound.wav")
swordsound = [sword1, sword2, sword3, sword4, sword5]
monstersound = [slimesound, batsound, firespiritsound, dragonsound, ghostsound, ovnisound, yinyonsound, treesound]


#######-  Variables nécessaires au bon fonctionnement du jeu  -########

story = 0      #Gère les différentes actions du jeu
scenario = 0   #Gère une action spécifique
restart = 0    #Point de sauvegarde en cas de mort
meet = 0       #Rencontres de monstres dans les hautes herbes 
meet2 = 0      #Rencontres de monstres dans les hautes herbes 
fight = 0      #Enclenche les combats
power = 1      #Gère la "puissance"
fey = 1        #Gère l'attaque de Fey
dgt = 0        #Dégâts pris
pr1 = 1        #Précision des attaques
pr2 = 1        #Précision des attaques
crit = 0       #Gère les coups critiques
lvl = 5        #Niveau de l'utilisateur 
lvlm = 4       #Niveau du monstre
xp = 50        #Expérience de l'utilisateur 
bxp = 50       #Gère l'expérience que rapporte les monstres une fois vaincus 
weak = 0       #Gère la faiblesse cachée des monstres
cm = 1         #Coefficient multiplicateur pour le calcul des dégâts (utilisateur)
cm2 = 1        #Coefficient multiplicateur pour le calcul des dégâts (monstre)
cmb = 1        #Coefficient multiplicateur pour le calcul des dégâts (base) 
x = 1          #Orientation du personnage
x1 = 0         #Permet de choisir le monstre qui va être combattu
dx = 330       #Déplacement horizontal du personnage
dx2 = 330      #Bloquage horizontal du personnage
dy = 250       #Déplacement vertical du personnage
dy2 = 250      #Bloquage vertical du personnage
vit = 15       #Vitesse permettant le déplacement du personnage
s1 = [20, 5, 5, 5, 0.95]   #Statistiques de l'utilisateur  
s2 = [50]                  #Staistiiques du mosntre 
pvi = 20 + (5*lvl-25)      #Points de vie initiaux du personnage 
pv = 20                    #Points de vie du de l'utilisateur
pvm = 20                   #Points de vie du monstre 
mov = [df3,df1,df2,df1,db3,db1,db2,db1,dl3,dl1,dl2,dl1,dr3,dr1,dr2,dr1] #On choisit ici l'orientation du personnage
mon1 = [un,deux,trois,quatre,cinq,six,sept,huit]        #On choisit ici quel monstre affrontera l'utilisateur
f = 0           #Variable pour l'animation des mouvements du personnage (face)
b = 0           #Variable pour l'animation des mouvements du personnage (bottom)    
l = 0           #Variable pour l'animation des mouvements du personnage (left)        
r = 0           #Variable pour l'animation des mouvements du personnage (right) 
haut = 1        #Variable pour l'orientation du personnage vers le haut
bas = 0         #Variable pour l'orientation du personnage vers le bas
gauche = 0      #Variable pour l'orientation du personnage vers la gauche
droite = 0      #Variable pour l'orientation du personnage vers la droite
boss = 0        #Gère les attaques aléatoires du boss
avilis = 1      #Gère l'attaque spéciale du boss
rage = 1        #Gère la "colère" du boss
music = 0       #Gère les changements de musique

#######################-  Fonctions du jeu  -##########################

def move(): #fonction qui permet au joueur de se déplacer
    global dx, dy, dx2, dy2, base, f, b, l, r, haut, bas, gauche, droite, meet, meet2
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:               #Vers le haut
                dy2 = dy
                dy = dy - vit
                haut = 1                        #Le personnage s'oriente vers le haut
                bas = 0                         #Ce qui annule les autres orientations     
                gauche = 0
                droite = 0
                b = ((b + 1) % 4)               #Change la sprite d'animation du personnage tous les 4 "pas"
                meet2 = random.randint(1,10)    
                if meet2 == 10:                 #Nous donne 1 chance sur 10 de rencontrer un    
                    meet = 1                    #monstre lorsque l'on marche dans la zone prévue
                
            if event.key == K_DOWN:             #Vers le bas
                dy2 = dy  
                dy = dy + vit  
                haut = 0
                bas = 1
                gauche = 0
                droite = 0
                f = ((f + 1) % 4)
                meet2 = random.randint(1,10)
                if meet2 == 10:
                    meet = 1
                
            if event.key == K_LEFT:             #Vers la gauche
                dx2 = dx   
                dx = dx - vit
                haut = 0
                bas = 0
                gauche = 1
                droite = 0
                l = ((l + 1) % 4)
                meet2 = random.randint(1,10)
                if meet2 == 10:
                    meet = 1
                
            if event.key == K_RIGHT:            #Vers la droite
                dx2 = dx   
                dx = dx + vit 
                haut = 0
                bas = 0
                gauche = 0
                droite = 1
                r = ((r + 1) % 4) 
                meet2 = random.randint(1,10)
                if meet2 == 10:
                    meet = 1
                
def ori():  #Fonction qui permet de gérer l'orientation du personnage lorsqu'il bouge
    global haut, bas, gauche, droite
    if haut == 1:
        anib()        #Active la fonction d'animation du personnage correspondante (bottom)
    if bas == 1:
        anif()        #(face)
    if gauche == 1:
        anil()        #(left)
    if droite == 1:
        anir()        #(right)  
    
                
def anif(): #Fonction qui gère les sprites quand le personnage bouge (Vers le bas)
    global f, b, l, r, x
    if f >= 0:
        b = 0
        l = 0   #Réinitialise les sprites des directions autres que celle choisie
        r = 0
        x = f   #La sprite affichée à l'écran correspond à celle piochée dans le tableau (l.375)
        
def anib(): #(Vers le haut)
    global f, b, l, r, x
    if b >= 0:
        f = 0
        l = 0
        r = 0
        x = b + 4 #On ajoute +4 pour piocher les 4 sprites suivantes du tableau (l.375)
        
def anil(): #(Vers la gauche)
    global f, b, l, r, x   
    if l >= 0:
        b = 0
        f = 0
        r = 0
        x = l + 8  
        
def anir(): #(Vers la droite)
    global f, b, l, r, x
    if r >= 0:
        b = 0
        l = 0
        f = 0
        x = r + 12
        
def winlose(): #fonction qui vérifie en combat si il y'a une condition de victoire ou défaite
    global lvlm, pvm, pv, xp, story, bxp, scenario, rage, avilis, music, lvl
    if pvm <= 0:                #Si le monstre meurt
        if scenario == 2:       #Si c'est contre le boss:
            pygame.mixer.Sound.play(avilis1)
            pygame.mixer.Sound.play(winsound)
            story = 75          #On affiche l'écran de victoire du boss
        else:
            pygame.mixer.Sound.play(winsound)
            story = 51          #Sinon on affiche l'écran de victoire basique
        if lvl + 2 < lvlm:
            xp = xp + (bxp*lvlm*2)    #On gagne de l'expérience en fonction de son niveau
        else:
            xp = xp + (bxp*lvlm)    #On gagne de l'expérience en fonction de son niveau
        exp()                   #On vérifie la condition de passage au niveau supérieur    
        
    if pv <= 0:                 #Si on meurt
        if pv < 0:
            pv = 0
        if scenario == 2:
            story = -3          #On indique que l'utilisateur n'a plus de points de vie
        else:
            story = -2          #Game over
        scenario = 0            #On réinitialise la variable scénario
     
    if scenario == 2 and story >= 66: 
        if pvm <= 25 and rage == 1: #Lorsque le boss perd la moitié de ses PV:
            pygame.mixer.Sound.play(avilis2)
            story = 76
            rage = 0
            music = 0               #Changement de musique
            s2[1] = s2[1]*1.5       #On augmente l'attaque du boss
            s2[3] = s2[3]*1.5       #On augmente la défense du boss
            s2[4] = 2               #On améliore sa précision

          
def clic(): #Variable essentielle pour faire fonctionner le jeu
    global story, meet2, meet, fight, power, fey, crit, pv, pvi, cm, dgt, cmb, pr1, pr2, lvlm, sm, pvm, cm2, xp, dx, dy, x, music, boss, avilis, scenario, bxp, haut, bas, gauche, droite, r, f, rage
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and story ==0:
                        pygame.mixer.Sound.play(click)
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #On clique pour commencer l'histoire
                                music = 0           #Changement de la musique
                                if restart == 0:    #Si c'est la première fois qu'on commence:
                                    dx = 330            #On définit les coordonnées du personnage
                                    dy = 250
                                    story = 1           #On passe à l'image suivante
                                if restart == 1:    #Si l'utilisateur avait atteint le premier point de sauvegarde
                                    dx = 330            #On change ses coordonnées 
                                    dy = 300
                                    bas = 1             #On oriente le personnage vers le bas
                                    f = 1      
                                    story = 40          #On passe à la dernière image de sauvegarde (dans la cabane)
                                    pv = pvi            #On lui rend tous ses points de vie
                                    meet = 0            #On annule toute rencontre avec un monstre
                                    meet2 = 0
                                    fight = 0           #On annule tout combat
                                    power = 1           #On réinitialise les compétences utilisées avant de perdre            
                                    cm = 1              #On réinitialise le coefficient multiplicateur de dégâts
                                    fey = 1             #On réinitialise les compétences utilisées avant de perdre 
                                    s1[1] = 5 + lvl     #On redéfinit la force de l'utilisateur
                                    s1[2] = 5 + lvl     #On redéfinit la magie de l'utilisateur
                                    s1[3] = 5 + lvl     #On redéfinit la défense de l'utilisateur
                                    s1[4] = 0.95        #On redéfinit la précision de l'utilisateur
                                if restart == 2:
                                    dx = 330
                                    dy = 300
                                    bas = 1
                                    f = 1
                                    story = 52
                                    scenario = 1
                                    pv = pvi
                                    meet = 0
                                    meet2 = 0
                                    fight = 0
                                    power = 1
                                    cm = 1
                                    fey = 1
                                    rage = 1            #On réinitialise la "colère" du boss
                                    avilis = 1          #On réinitialise la compétence utilisée par le boss
                                    s1[1] = 5 + lvl
                                    s1[2] = 5 + lvl
                                    s1[3] = 5 + lvl
                                    s1[4] = 0.95
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 1:   #L'écran de séléction des personnages est affiché
                        if 0 < event.pos[0] < 250 and 0 < event.pos[1] < 550:
                                story = 2   #Permet de choisir l'épéiste
                                pygame.mixer.Sound.play(click)
                     
                        if 250 < event.pos[0] < 500 and 0 < event.pos[1] < 550:
                                story = 3   #Permet de choisir l'archer
                                pygame.mixer.Sound.play(click)
                                
                        if 500 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 4   #Permet de choisir la magicienne
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 2:                  #/
                        if 350 < event.pos[0] < 690 and 130 < event.pos[1] < 230:  #/
                                story = 5
                                pygame.mixer.Sound.play(click)                     #/
                        if 350 < event.pos[0] < 690 and 260 < event.pos[1] < 355:  #/
                                story = 1  #Retour 
                                pygame.mixer.Sound.play(click)                     #/    
                                                                                   #/ Peu importe le personnage choisi
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 3:                  #/ on demande à l'utilisateur s'il
                        if 350 < event.pos[0] < 690 and 130 < event.pos[1] < 230:  #/ est sûr de son choix
                                story = 5
                                pygame.mixer.Sound.play(click)                     #/
                        if 350 < event.pos[0] < 690 and 260 < event.pos[1] < 355:  #/
                                story = 1   #Retour
                                pygame.mixer.Sound.play(click)                     #/    
                                                                                   #/
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 4:                  #/
                        if 350 < event.pos[0] < 690 and 130 < event.pos[1] < 230:  #/
                                story = 5 
                                pygame.mixer.Sound.play(click)                     #/
                        if 350 < event.pos[0] < 690 and 260 < event.pos[1] < 355:  #/
                                story = 1   #Retour                                #/
                                pygame.mixer.Sound.play(click)
       
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 5: #On lui renvoie un autre personnage qui sera celui qu'il utilisera
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 6
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 6 <= story <= 9:         #Version plus compacte pour éviter   
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:  #les répétitions
                                pygame.mixer.Sound.play(click)
                                story = story + 1   
                                music = 0   #Crée une des conditions nécessaires au changement de musique
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 10:   #Sépare la zone de "clic" en deux pour pouvoir choisir entre deux propositions
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 225:
                                story = 11
                                pygame.mixer.Sound.play(click)
                        if 0 < event.pos[0] < 800 and 226 < event.pos[1] < 550:
                                story = 12
                                pygame.mixer.Sound.play(click)
       
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 11:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 111                                     #Premier choix
                                pygame.mixer.Sound.play(click)
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 111:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 13  #Retour au scénario initial
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 12:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 121
                                pygame.mixer.Sound.play(click)
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 121:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #Second choix
                                story = 122
                                pygame.mixer.Sound.play(click)
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 122:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 13  #Retour au scénario initial
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 13 <= story <= 16:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:  #Version compacte du passage des dialogues 
                                story = story + 1
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story ==18:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:  #Dialogue 
                                story = 19
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 20 <= story <= 24:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = story + 1        
                                music = 0
                                pygame.mixer.Sound.play(click)
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 25:  #Nouvelle séparation de la zone de "clic" pour un autre choix
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 225:
                                story = 26
                                pygame.mixer.Sound.play(click)
                        if 0 < event.pos[0] < 800 and 226 < event.pos[1] < 550:
                                story = 27
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 26:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 261                                     #Choix 1
                                pygame.mixer.Sound.play(click)
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 261:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 28
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 27:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #Choix 2
                                story = 28
                                pygame.mixer.Sound.play(click)
        
        elif event.type == pygame.MOUSEBUTTONDOWN and 28 <= story <= 30:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = story + 1
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 31:  #Troisième choix
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 225:
                                story = 32
                                pygame.mixer.Sound.play(click)
                        if 0 < event.pos[0] < 800 and 226 < event.pos[1] < 550:
                                story = 33
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 33:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 31  #Le deuxième choix renvoie à la séléction des choix précédente
                                pygame.mixer.Sound.play(click)
        
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 32:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 34  #Alors que le premier permet de continuer l'histoire 
                                pygame.mixer.Sound.play(click)                      
        
        elif event.type == pygame.MOUSEBUTTONDOWN and 34 <= story <= 39:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = story + 1
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 411: #Transition entre la zone de la cabane et celle des monstres
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550: 
                                story = 42
                                music = 0
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 412: #Transition entre la zone des monstres et celle de la cabane
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 41
                                music = 0
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 43:  #Quand un monstre apparaît:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 44
                                sm()    #On donne ses statistiques au monstre
                                lvlmn() #On donne son niveau au monstre
                                pvm = s2[0]  #Les pv du monstre correspondent à la statistique de pv comprise dans le tableau des statistiques choisi
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 44:  #Dans l'écran de choix d'une action:
                        if 520 < event.pos[0] < 750 and 330 < event.pos[1] < 400:   #On peut choisir d'attaquer
                                story = 45
                                pygame.mixer.Sound.play(click)
                        if 520 < event.pos[0] < 750 and 430 < event.pos[1] < 510:   #On peut utiliser le kit
                                story = 46
                                pygame.mixer.Sound.play(click)
                        if 20 < event.pos[0] < 200 and 400 < event.pos[1] < 500:    #On peut fuir
                                story = 42
                                pygame.mixer.Sound.play(click)
                                meet = 0    #Réinitialise la condition de rencontre 
                                meet2 = 0
                                fight = 0    #Annule le combat
                                power = 1    #Restaure la puissance (si utilisée)
                                cm = 1       #Réinitialise le coefficient multiplicateur
                                fey = 1      #Restaure la capacité spéciale (si utilisée)
                                s1[4] = 0.95 #Restaure la précision de base
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 46:  #Dans le kit:
                        if 490 < event.pos[0] < 750 and 335 < event.pos[1] < 415: #Si santé est choisi:
                                story = 47
                                pygame.mixer.Sound.play(healsound)
                                pygame.mixer.Sound.play(click)
                                pv = pv + (1/2)*pvi #Cela nous pestaure la moitié de nos pv totaux
                                if pv > pvi:        #Si les pv restaurés dépasse les pv totaux    
                                    pv = pvi        #Les pv seront égaux aux pv totaux
                                
                        if 520 < event.pos[0] < 750 and 435 < event.pos[1] < 515 and power == 1: #Si puissance est choisi (et qu'il n'a pas déja été utilisé):   
                                story = 471
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(powersound)
                                power = 0   #On met power à 0 pour ne pas qu'il soit réutilisé au prochain tour
                                cm = cm*2   #On quadruple le coefficent multiplicateur de dégâts
                                s1[4] = 2   #On augmente la précision
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and ((story == 47) or (story == 471)): #Après notre action (dans le kit), le monstre attaque
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)      #Un nombre aléatoire entre 1 et 100 est généré
                                pr2 = s2[4]*100                  #La précision de base du monstre est multipliée par 100        
                                if pr1 <= pr2:                   #Si le nombre aléatoire est inférieur à la précision du monstre:
                                    story = 50
                                    crit = random.randint(1,16)         #On génère un nombre aléatoire entre 1 et 16 (1 chance sur 16 de mettre un coup critique)
                                    if crit == 1:                       #Si ce chiffre est égal à 1:
                                        cm2 = cm2*1.5                       #Coup critique : On multiplie le coefficient multiplicateur de dégâts    
                                    if weak == 0:                               #Si la faiblesse cachée du monstre est la force:
                                        dgt = ((2.5*s2[2])/s1[3])*cm2                #Il frappera avec sa magie divisé par la défense du personnage x le coefficient multiplicateur
                                        pygame.mixer.Sound.play(damage)
                                        pygame.mixer.Sound.play(damagemagic)
                                    else:                                       #Si sa faiblesse cachée est la magie
                                        dgt = ((2.5*s2[1])/s1[3])*cm2                 #Il frappera avec sa force divisé par la défense du personnage x le coefficient multiplicateur
                                        pygame.mixer.Sound.play(damage)
                                    pv = pv - dgt                    #On retire au pv de l'utilisateur le résultat du calcul 
                                    cm2 = cmb                         #On réinitialise le coefficient multiplicateur
                                    winlose()                          #On vérifie si l'utilisateur a succombé à l'attaque
                                else:                              #Si le nombre aléatoire est supérieur à la précision du monstre:
                                    winlose()               
                                    story = 502                         #Le monstre rate son attaque
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 45: #Dans l'onglet Attaque:
                        if 535 < event.pos[0] < 765 and 330 < event.pos[1] < 395: #Si on utilise Force:
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)         
                                pr2 = s1[4]*100
                                if pr1 <= pr2:                   #Si le nombre aléatoire est inférieur à la précision de l'utilisateur:
                                    
                                    story = 48
                                    if power == 1:
                                        crit = random.randint(1,16)
                                    elif power == 0:                    #Si la puissance est activée:
                                        crit = random.randint(1,6)          #Les chances de coup critique sont plus élévées
                                    if crit == 1:
                                        cm = cm*1.5
                                    if weak == 0:                       #Si la faiblessse du monstre est la Force:
                                        cm = cm*1.5                         #On augmente les dégâts infligés
                                        dgt = ((2.5*s1[2])/s2[3])*cm        
                                    else:
                                        dgt = ((2.5*s1[1])/s2[3])*cm        #On calcule la force de l'utilisateur sur la défense du monstre x le coefficient multiplicateur
                                    pvm = pvm - dgt                     #On enlève au pv du monstre les dégâts infligés 
                                    if pvm > 0:
                                        pygame.mixer.Sound.play(swordsound[random.randint(0,4)])
                                    cm = cmb                            #On réinitialise le coefficient multiplicateur
                                    winlose()                           #On vérifie si le monstre a succombé à l'attaque
                                else:                           #Si le nombre aléatoire est supérieur à la précision de l'utilisateur:
                                    winlose()
                                    story = 501                         #On rate l'attaque
                        
                                            
                        if 435 < event.pos[0] < 765 and 400 < event.pos[1] < 453: #Si on utilise Magie:
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s1[4]*100
                                if pr1 <= pr2:
                                    story = 481
                                    if power == 1:
                                        crit = random.randint(1,16)
                                    elif power == 0:
                                        crit = random.randint(1,6)
                                    if crit == 1:
                                        cm = cm*1.5
                                    if weak == 1:                      #Si la faiblessse du monstre est la Magie:
                                        cm = cm*1.5                        #On augmente les dégâts infligés     
                                        dgt = ((2.5*s1[2])/s2[3])*cm
                                    else:
                                        dgt = ((2.5*s1[2])/s2[3])*cm
                                    pvm = pvm - dgt
                                    if pvm > 0:
                                        pygame.mixer.Sound.play(magicsound)
                                    cm = cmb
                                    winlose()
                                else:
                                    winlose()
                                    story = 501
                                    
                        if 535 < event.pos[0] < 765 and 460 < event.pos[1] < 517 and fey == 1: #Si on utilise Fey:
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(feysound)
                                story = 482
                                fey = 0         #On active la compétence spéciale de Fey                                        
        
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 51:  #En cas de victoire
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = 42 #On retourne dans la zone avec les monstres
                                meet = 0
                                meet2 = 0
                                fight = 0
                                power = 1
                                cm = 1
                                fey = 1
                                s1[4] = 0.95
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and ((story == 48) or (story == 481) or (story == 501)):
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550: #Après notre action (Force, Magie, Raté...), le monstre attaque
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s2[4]*100
                                if pr1 <= pr2:
                                    story = 50
                                    crit = random.randint(1,16)
                                    if crit == 1:
                                        cm2 = cm2*1.5
                                    if weak == 0:
                                        dgt = ((2.5*s2[2])/s1[3])*cm2
                                        pygame.mixer.Sound.play(damage)
                                        pygame.mixer.Sound.play(damagemagic)
                                    else:
                                        dgt = ((2.5*s2[1])/s1[3])*cm2
                                        pygame.mixer.Sound.play(damage)
                                    pv = pv - dgt
                                    cm2 = cmb
                                    winlose()
                                else:
                                    winlose()
                                    story = 502
                                    
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 50: #Après action du monstre
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 44  #Le tour de combat est terminé et on en recommence un nouveau
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 482: #Quand Fey est activé:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(firesound)
                                pygame.mixer.Sound.play(click)
                                dgt = ((9.5*s1[1])/s2[3])   #On change le "2.5" en "9.5" pour augmenter drastiquement les dégâts
                                pvm = pvm - dgt
                                winlose()
                                story = 49    
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 49: #Après l'attaque de Fey, le monstre attaque
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s2[4]*100
                                if pr1 <= pr2:
                                    story = 50
                                    crit = random.randint(1,16)
                                    if crit == 1:
                                        cm = cm*1.5
                                    if weak == 0:
                                        dgt = ((2.5*s2[2])/s1[3])*cm2
                                        pygame.mixer.Sound.play(damage)
                                        pygame.mixer.Sound.play(damagemagic)
                                    else:
                                        dgt = ((2.5*s2[1])/s1[3])*cm2
                                        pygame.mixer.Sound.play(damage)
                                    pv = pv - dgt
                                    cm2 = cmb
                                    winlose()
                                else:
                                    winlose()
                                    story = 502  
                                    
        elif event.type == pygame.MOUSEBUTTONDOWN and (story == -2): #Si on n'a plus de pv, l'écran nous l'indique
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = -1
                                music = 0
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and  (story == -3): #Si on n'a plus de pv (boss), l'écran nous l'indique
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = -1
                                music = 0         
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == -1:  #Game over
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = 0 
                                music = 0
                                
        if event.type == pygame.MOUSEBUTTONDOWN and ((story == 45) or (story == 46) or (story == 502)): #Si on clique "Retour" ou "Suite" (quand le monstre a raté son attaque)
                        if 20 < event.pos[0] < 200 and 400 < event.pos[1] < 500:
                                pygame.mixer.Sound.play(click)
                                story = 44  #Le tour est terminé et on en recommence un nouveau                     
       
        elif event.type == pygame.MOUSEBUTTONDOWN and 401 <= story <= 404:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550: #Dialogue : Conseils donnés par le Vieillard
                                story = story + 1
                                pygame.mixer.Sound.play(click)
        
        elif event.type == pygame.MOUSEBUTTONDOWN and 401 <= story <= 405:  #Fin de dialogue 
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 40  #Retour dans la cabane 
                                pygame.mixer.Sound.play(click)                      
        
        elif event.type == pygame.MOUSEBUTTONDOWN and 52 <= story <= 57: #Dialogue : Le Vieillard parle du boss
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = story + 1        
                                music = 0
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 58:  #On sépare la zone de" clic" en deux
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 225:
                                story = 581                                         #Choix 1
                                pygame.mixer.Sound.play(click)
                        if 0 < event.pos[0] < 800 and 226 < event.pos[1] < 550:
                                story = 582                                         #Choix 2
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and ((story == 581) or (story == 582)):   #Suite du dialogue
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:       
                                story = 59
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 59:  #Suite du dialogue
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = story + 1
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 60:  #Fin du dialogue
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 40   
                                pygame.mixer.Sound.play(click)                
         
                                    #-- Boss --
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 61: #Dernier choix avant d'entrer dans la salle du boss
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 220:   #Si on accepte d'entrer:
                                pygame.mixer.Sound.play(click)
                                story = 62  #On accède au boss
                                music = 0
                                dx = 60     #On change les coordonnées du personnage
                                dy = 180
                                droite = 1  #On oriente le personnage face au boss
                                gauche = 0  
                                haut = 0        #On annule les autres orientations
                                bas = 0
                                r = 1
                        if 0 < event.pos[0] < 800 and 221 < event.pos[1] < 390: #Si on refuse d'entrer:
                                pygame.mixer.Sound.play(click)
                                story = 41
                                dx = 690
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 62 <= story <= 65: #Dialogue avec le boss et début du combat
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                if story == 62:
                                       pygame.mixer.Sound.play(avilis1)
                                elif story == 64:
                                       pygame.mixer.Sound.play(avilis2)
                                story = story + 1  
                                music = 0
                                pvm = s2[0]     #On change les points de vie du boss pour ceux compris dans ses statistiques
                                avilis = 1      #On initialise son coup spécial
                                scenario = 2    #On augmente le scénario                   
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 66:  #Choix d'action
                        if 520 < event.pos[0] < 750 and 330 < event.pos[1] < 400:
                                story = 67
                                pygame.mixer.Sound.play(click)
                        if 520 < event.pos[0] < 750 and 430 < event.pos[1] < 510:
                                story = 68
                                pygame.mixer.Sound.play(click)

        elif event.type == pygame.MOUSEBUTTONDOWN and story == 68:  #Santé
                        if 490 < event.pos[0] < 750 and 335 < event.pos[1] < 415:
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(healsound)
                                story = 69
                                pv = pv + (1/2)*pvi
                                if pv > pvi:
                                    pv = pvi
                                
                        if 520 < event.pos[0] < 750 and 435 < event.pos[1] < 515 and power == 1: #Puissance
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(powersound)
                                story = 691
                                power = 0
                                cm = cm*4
                                s1[4] = 2
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and ((story == 69) or (story == 691)): #Le boss attaque 
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s2[4]*100
                                if pr1 <= pr2:
                                    if avilis == 1:                     #Si le boss n'a pas encore utilisé son coup spécial:
                                        boss = random.randint(1,15)        #On génère un nombre aléatoire entre 1 et 15 (1/15 chances de faire le coup spécial)
                                        if boss == 15 :                    #Si le nombre aléatoire est égal à 15:
                                            story = 73                          #Il utilise son coup spécial
                                            if story == 73:
                                                pygame.mixer.Sound.play(avilis2)
                                            avilis = 0                          #On désactive son coup spécial pour les tours suivants   
                                        else:
                                            story = 72
                                            crit = random.randint(1,16)
                                            if crit == 1:
                                                cm2 = cm2*1.5
                                            dgt = ((2.5*s2[1])/s1[3])*cm2
                                            pygame.mixer.Sound.play(damage)
                                            pv = pv - dgt
                                            cm2 = cmb
                                            winlose()
                                    elif avilis == 0:                   #Si il l'a déjà utilisé, il attaque normalement:
                                        story = 72
                                        crit = random.randint(1,16)
                                        if crit == 1:
                                            cm2 = cm2*1.5
                                        dgt = ((2.5*s2[1])/s1[3])*cm2
                                        pygame.mixer.Sound.play(damage)
                                        pv = pv - dgt
                                        cm2 = cmb
                                        winlose()   #winlose() vérifie aussi si les pv du boss sont en dessous de la moitié (si c'est le cas voir l.509)
                                else:
                                    winlose()
                                    story = 722     
                                    
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 67:  #Attaque
                        if 535 < event.pos[0] < 765 and 330 < event.pos[1] < 395:   #Force
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s1[4]*100
                                if pr1 <= pr2:
                                    story = 70
                                    if power == 1:
                                        crit = random.randint(1,16)
                                    elif power == 0:
                                        crit = random.randint(1,6)
                                    if crit == 1:
                                        cm = cm*1.5
                                    if weak == 0:
                                        dgt = ((2.5*s1[2])/s2[3])*cm
                                    else:
                                        dgt = ((2.5*s1[1])/s2[3])*cm
                                    pvm = pvm - dgt
                                    if pvm > 0:
                                        pygame.mixer.Sound.play(swordsound[random.randint(0,4)])
                                    cm = cmb
                                    winlose()
                                else:
                                    winlose()
                                    story = 721
                        
                                            
                        if 435 < event.pos[0] < 765 and 400 < event.pos[1] < 453:   #Magie
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s1[4]*100
                                if pr1 <= pr2:
                                    story = 701
                                    if power == 1:
                                        crit = random.randint(1,16)
                                    elif power == 0:
                                        crit = random.randint(1,6)
                                    if crit == 1:
                                        cm = cm*1.5
                                    if weak == 1:
                                        cm = cm*1.5
                                    dgt = ((2.5*s1[2])/s2[3])*cm
                                    pvm = pvm - dgt
                                    if pvm > 0:
                                        pygame.mixer.Sound.play(magicsound)
                                    cm = cmb
                                    winlose()
                                else:
                                    winlose()
                                    story = 721
                        
                        if 535 < event.pos[0] < 765 and 460 < event.pos[1] < 517 and fey == 1: #Fey
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(feysound)
                                story = 702 #Activation du coup spécial
                                fey = 0
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 75: #Si on gagne:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = 771 #On affiche l'écran de victoire contre le boss
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 771: #Écran de transition entre le boss et la fin
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = 77   
                                music = 0
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and ((story == 70) or (story == 701) or (story == 721)): #Après notre action (Force, Magie, Raté...), le boss attaque 
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pr1 = random.randint(1,100)
                                pr2 = s2[4]*100
                                if pr1 <= pr2:
                                    if avilis == 1:
                                        boss = random.randint(1,15)
                                        if boss == 15 :
                                            story = 73
                                            avilis = 0
                                        else:
                                            story = 72
                                            crit = random.randint(1,16)
                                            if crit == 1:
                                                cm2 = cm2*1.5
                                            dgt = ((2.5*s2[1])/s1[3])*cm2
                                            pygame.mixer.Sound.play(damage)
                                            pv = pv - dgt
                                            cm2 = cmb
                                            winlose()
                                    elif avilis == 0:
                                        story = 72
                                        crit = random.randint(1,16)
                                        if crit == 1:
                                            cm2 = cm2*1.5
                                        dgt = ((2.5*s2[1])/s1[3])*cm2
                                        pygame.mixer.Sound.play(damage)
                                        pv = pv - dgt
                                        cm2 = cmb
                                        winlose()
                                else:
                                    winlose()
                                    story = 722 
                                    
                                    
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 72:  #Après l'attaque du boss
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = 66  #Le tour se termine et un autre commence                 
                                         
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 702: #Attaque de Fey
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(firesound)
                                dgt = ((12*s1[1])/s2[3])
                                s1[1] = s1[1]*1.5   #On augmente la Force du personnage
                                s1[2] = s1[2]*1.5   #On augmente le Magie du personnage
                                pvm = pvm - dgt
                                winlose()
                                story = 71  
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 73:  #Coup spécial du boss
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pygame.mixer.Sound.play(avilisburst1)
                                pygame.mixer.Sound.play(avilisburst2)
                                story = 731 #Activation du coup spécial
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 731: #Coup spécial du boss
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:     
                                pygame.mixer.Sound.play(click)                  
                                dgt = ((4*s2[1])/s1[3]) #On change le "2.5" en "20" pour augmenter les dégâts subis
                                s1[3] = s1[3]*0.67       #On baisse la défense du personnage
                                pv = pv - dgt
                                winlose()
                                story = 66  #Nouveau tour
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 76:  #Le boss s'énerve
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = 66  #Nouveau tour
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 71: #Après l'action (Fey), le boss attaque
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pr1 = random.randint(1,100)
                                pr2 = s2[4]*100
                                if pr1 <= pr2:
                                    if avilis == 1:
                                        boss = random.randint(1,15)
                                        if boss == 15 :
                                            story = 73
                                            avilis = 0
                                        else:
                                            story = 72
                                            crit = random.randint(1,16)
                                            if crit == 1:
                                                cm2 = cm2*1.5
                                            dgt = ((2.5*s2[1])/s1[3])*cm2
                                            pv = pv - dgt
                                            cm2 = cmb
                                            winlose()
                                    elif avilis == 0:
                                        story = 72
                                        crit = random.randint(1,16)
                                        if crit == 1:
                                            cm2 = cm2*1.5
                                        dgt = ((2.5*s2[1])/s1[3])*cm2
                                        pv = pv - dgt
                                        cm2 = cmb
                                        winlose()
                                else:
                                    winlose()
                                    story = 722
                                    
        if event.type == pygame.MOUSEBUTTONDOWN and ((story == 67) or (story == 68) or (story == 722)): #Si on appuie sur "Retour" ou "Suite" (Quand une attaque est ratée):
                        if 20 < event.pos[0] < 200 and 400 < event.pos[1] < 500:
                                pygame.mixer.Sound.play(click)
                                story = 66     #Nouveau tour 
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 77 <= story <= 80:    #Dialogue de fin dans la cabane
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                story = story + 1
                                music = 0
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 81:  #Dernier choix du jeu
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 225:
                                story = 811 #Fin 1
                                pygame.mixer.Sound.play(click)
                        if 0 < event.pos[0] < 800 and 226 < event.pos[1] < 550:
                                story = 82  #Fin 2
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 811 <= story <= 817:     
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #Fin 1
                                story = story + 1
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 818:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #Mot final
                                story = 89
                                music = 0       
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and 82 <= story <= 87:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #Fin 2 
                                story = story + 1    
                                pygame.mixer.Sound.play(click)
        
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 88:
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:   #Mot final
                                story = 89
                                music = 0
                                pygame.mixer.Sound.play(click)
        
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 89:  #Écran de fin
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                story = 90
                                pygame.mixer.Sound.play(click)
                                
        elif event.type == pygame.MOUSEBUTTONDOWN and story == 90:  #Écran de fin
                        if 0 < event.pos[0] < 800 and 0 < event.pos[1] < 550:
                                pygame.mixer.Sound.play(click)
                                pygame.quit()   #Ferme le jeu quand on clique
               

def sm(): #fonction qui permet de piocher les stats des monstres à affronter
    global x1,s2, weak, bxp
    if x1 == 0: #Slime
        s2 = [15, 5, 5, 4, 0.7] #[pv, force, magie, défense, chance]
        weak = 0                #définit une faiblesse cachée à la force ou à la magie
        bxp = 5                 #définit l'expérience gagnée en le vaincant
    if x1 == 1: #Chauve-souris
        s2 = [10, 5, 2, 4, 0.8]
        weak = 1                #0 = faible à la force/ 1 = faible à la magie    
        bxp = 6
    if x1 == 2: #Esprit de feu
        s2 = [15, 2, 7, 4, 0.9]
        weak = 0
        bxp = 8
    if x1 == 3: #Dragon krok
        s2 = [20, 10, 5, 4, 0.9]
        weak = 1
        bxp = 15
    if x1 == 4: #Fantôme
        s2 = [20, 7, 4, 4, 0.9]
        weak = 1
        bxp = 7
    if x1 == 5: #O.V.N.I.
        s2 = [30, 5, 5, 6, 1]
        weak = 0
        bxp = 20
    if x1 == 6: #Yin-Yon
        s2 = [20, 2, 6, 5, 2]
        weak = 0
        bxp = 9
    if x1 == 7: #Esprit de la forêt
        s2 = [25, 12, 6, 4, 0.75]
        weak = 1
        bxp = 11
    return s2


def lvlmn():    #fonction qui définit le niveau et les statistiques du monstre
    global lvl, s2, lvlm
    for i in range (1,4):
        s2[i] = s2[i] + (lvlm-5) #On augmente les stats du monstre en fonction du niveau du joueur
    s2[0] = s2[0] + (s1[0]-20)  #Calcul spécial pour les pv
    lvlm = random.randint(lvl-2,lvl+5) 
    
    
def combat():   #Fonction qui permet d'engager un combat
    global fight, story, x1
    if fight == 1:
        if story == 42: #Lorsque l'on est dans la bonne zone, le combat s'enclenche
            story = 43
            x1 = random.randint(0,7) #Nous donne 1/8 d'affronter un certain monstre
            pygame.mixer.Sound.play(monstersound[x1])
            
def exp():  #Définit la montée de niveau
    global lvl, xp, s1, pvi
    if xp > lvl**3:         #Quand l'expérience a dépassée le seuil limite du niveau actuel
        xp = 50
        lvl = lvl + 1       #Le niveau augmente
        for i in range (1,4):
            s1[i] = s1[i] + 1       #On augmente les stats (sauf la chance) de 1
            pvi = 20 + (5*lvl-30)   #Calcul spécial pour les pv
  
        
def jukebox():  #fonction qui permet de changer de musique selon la zone
    global story, music, scenario
    if story == 0 and music == 0:   #Si l'utilisateur remplit les conditions requises :
        pygame.mixer.music.load(r"music/ecrantitre.mp3")   #On charge une musique
        pygame.mixer.music.play(-1)                   #On joue la musique
        music = 1   #On annule une des conditions requises pour que la musique ne se recommence pas en boucle
    elif story == 1 and music == 0:
        pygame.mixer.music.load(r"music/select.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif (story == 7 or story == 41) and music == 0:
        pygame.mixer.music.load(r"music/foret.mp3")
        pygame.mixer.music.play(-1) #On boucle la musique lorsqu'elle est suceptible d'être trop courte
        music = 1
    elif story == 42 and music == 0:
        pygame.mixer.music.load(r"music/foret2.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == 53 and music == 0:
        pygame.mixer.music.load(r"music/trouble.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == 62 and music == 0:
        pygame.mixer.music.load(r"music/avant-avilis.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == 65 and music == 0:
        pygame.mixer.music.load(r"music/avilis.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == -1 and music == 0:
        pygame.mixer.music.load(r"music/gameover.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == 76 and music == 0:
        pygame.mixer.music.load(r"music/avilis50.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == 78 and music == 0:
        pygame.mixer.music.load(r"music/ending.mp3")
        pygame.mixer.music.play(-1)
        music = 1
    elif story == 89 and music == 0:
        pygame.mixer.music.load(r"music/thanks.mp3")
        pygame.mixer.music.play()
        music = 1
####################-  Initialisation du jeu  -#########################
screen = pygame.display.set_mode(size)  #On donne sa taille à l'écran
pygame.key.set_repeat(50)               #Permet un mouvement "fluide" quand on bouge

while True:
        jukebox()                   #On démarre les musiques
        ori()                       #On active l'orientation du personnage pour toute la durée du jeu
        clic()                      #On permet à l'utilisateur de cliquer sur l'interface  
        pv = ceil(pv)               #Permet d'arrondir la valeur des pv
        if story == 0: #Début du jeu
            
            screen.blit(bg1, bg1rect)    #Permet d'afficher l'image séléctionée
            screen.blit(logo, [150,100])
            if restart == 0:
                texte = police.render("-Cliquez pour commencer-", 0, couleur_texte)
                screen.blit(texte,(190,350)) #Affiche le texte
            else:
                texte = police.render("-Cliquez pour continuer-", 0, couleur_texte)
                screen.blit(texte,(200,350)) #Affiche le texte
            pygame.display.flip()        #Met à jour l'interface


        if story == 1: #Écran de séléction des personnages 
         
            screen.blit(ch, chrect)
            screen.blit(d1, [0,400])
            pygame.display.flip()
          
            
  
        elif story == 2:    #Héros à l'épée
    
            screen.blit(ch1, ch1rect)
            screen.blit(d2, d2rect)
            pygame.display.flip()
         
                            
        elif story == 3:    #Archer
           
            screen.blit(ch2, ch2rect)
            screen.blit(d2, d2rect)
            pygame.display.flip()
        
                            
        elif story == 4:    #Magicienne
           
            screen.blit(ch3, ch3rect)
            screen.blit(d2, d2rect)
            pygame.display.flip()
           
            
        elif story == 5:    #Tous les choix renvoient finalement à ce personnage
            screen.blit(ch4, ch4rect)
            pygame.display.flip()
           
                            
                        
        elif story == 6:    #Écran de sauvegarde
            screen.blit(bs, bsrect)
            screen.blit(logo, [150,100])
            pygame.display.flip()
       
            
        elif story == 7:    #On affiche la forêt et les personnages
            haut = 1
            b = 1
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            pygame.display.flip()
       
           
        elif story ==8:     #La fée parle
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial1, dial1rect)
            pygame.display.flip()
          
            
        elif story ==9:     #La fée parle   
            gauche = 1
            haut = 0
            l = 1
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial2, dial2rect)
            pygame.display.flip()
            
        elif story == 10:     #On effectue un premier choix
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(c1, c1rect)
            pygame.display.flip()
            
        elif story == 11:     #Choix 1: La fée donne son nom : Fey
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial6, dial6rect)
            pygame.display.flip()
        
        elif story == 111:  #Choix 1 : Fey parle
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial7, dial7rect)
            pygame.display.flip()
        
        elif story == 12:   #Choix 2: la fée parle de la forêt
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial3, dial3rect)
            pygame.display.flip()
            
        elif story == 121:  #Choix 2: la fée parle
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial4, dial4rect)
            pygame.display.flip()
        
        elif story == 122:  #Choix 2: la fée donne son nom : Fey
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial5, dial5rect)
            pygame.display.flip()
        
        elif story == 13:   #Le personnage principal ne sait pas qui il est
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial8, dial8rect)
            pygame.display.flip()
        
        elif story == 14:   #Fey parle
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial9, dial9rect)
            pygame.display.flip()
            
        elif story == 15:   #Fey parle   
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial10, dial10rect)
            pygame.display.flip()
        
        elif story == 16:   #Fey parle
            screen.blit(bg2, bg2rect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            screen.blit(dial11, dial11rect)
            pygame.display.flip()
        
        elif story == 17:   #On se déplace dans la forêt
            screen.blit(bg2, bg2rect)
            screen.blit(hbgd, hbgdrect)
            screen.blit(light2, light2rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(light, lightrect)
            move()  #On active le déplacement
            pygame.display.flip()
            if  (dx < 100 or dx > 600) or (dy > 300) or (((100 < dx < 200) or (450 < dx < 600)) and (dy < 80)): #Zones de bloquage
                dx = dx2
                dy = dy2
        
            if 200 < dx < 450 and dy <= 15: #Permet de passer dans la zone suivante
                story = 18
                dx = 330
                dy = 400
                dx2 = 330
                dy2 = 400
                haut = 1
                gauche = 0
                droite = 0
                bas = 0
                b = 1
                
        elif story == 18:   #Fey parle (de la cabane)
                screen.blit(bg3, bg3rect)
                screen.blit(mov[x], [dx,dy])
                screen.blit(dial12, dial12rect)
                pygame.display.flip()
                
        elif story == 19:   #On se déplace dans la forêt
            screen.blit(bg3, bg3rect)
            screen.blit(mov[x], [dx,dy])
            move()
            pygame.display.flip()
            if (0 < dx < 260 and 0 < dy < 150) or (0 < dx < 260 and 275 < dy < 550) or (415 < dx < 800 and 0 < dy < 150) or (420 < dx < 800 and 275 < dy < 550) or (dy > 450) or (dx < 5 or dx > 700):
                dx = dx2
                dy = dy2 
            if 260 < dx < 420 and dy <= 100:
                story = 20
                dx = 330
                dy = 300
                dx2 = 330
                dy2 = 300
                haut = 1
                gauche = 0
                droite = 0
                bas = 0
                b = 1
                
        elif story == 20: #Point de sauvegarde
            restart = 1 #On ajoute 1 à restart pour sauvegarder 
            screen.blit(bs, bsrect)
            screen.blit(logo, [150, 100])
            pygame.display.flip()
            
        elif story == 21:   #On affiche l'intérieur de la cabane
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])  #On affiche le vieillard
            screen.blit(mov[x], [dx,dy])
            pygame.display.flip()
        
        elif story == 22:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial13, dial13rect)
            pygame.display.flip()
            
        elif story == 23:   #Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial14, dial14rect)
            pygame.display.flip() 
            
        elif story == 24:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial15, dial15rect)
            pygame.display.flip() 
        
        elif story == 25:   #On fait notre deuxième choix
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(c2, c2rect)
            pygame.display.flip()
        
        elif story == 26:   #Choix 1: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial16, dial16rect)
            pygame.display.flip()
        
        elif story == 261:   #Choix 1: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial17, dial17rect)
            pygame.display.flip()
        
        elif story == 27:   #Choix 2: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial18, dial18rect)
            pygame.display.flip()
            
        elif story == 28:   #Requête du vieillard
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial19, dial19rect)
            pygame.display.flip()
            
        elif story == 29:   #Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial20, dial20rect)
            pygame.display.flip()
            
        elif story == 30:   #Le vieillard demande de l'aide
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial21, dial21rect)
            pygame.display.flip()
         
        elif story == 31:   #On fait un troisième choix
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(c3, c3rect)
            pygame.display.flip()
            
        elif story == 32:   #Choix 1: On accepte sa requête
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial23, dial23rect)
            pygame.display.flip()    
        
        elif story == 33:   #Choix 2: On refuse mais il insiste
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial22, dial22rect)
            pygame.display.flip()
        
        elif story == 34:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial24, dial24rect)
            pygame.display.flip()
            
        elif story == 35:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial25, dial25rect)
            pygame.display.flip()
        
        elif story == 36:   #Le vieillard nous donne le -Kit de base-
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial26, dial26rect)
            pygame.display.flip()
        
        elif story == 37:      #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial27, dial27rect)
            pygame.display.flip()
        
        elif story == 38:      #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial28, dial28rect)
            pygame.display.flip()
            
        elif story == 39:      #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial29, dial29rect)
            pygame.display.flip()
         
        elif story == 40:   #On peur sortir de la cabane
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            move()
            pygame.display.flip()
            if (130 < dx < 550 and 0 < dy < 150) or (((120 < dx < 130) or (550 < dx < 570)) and dy < 150) or (dy > 450 or dy < 10) or (dx < 5 or dx > 700): #Zones de bloquage
                dx = dx2
                dy = dy2 
            if 220 < dx < 450 and 430 <= dy <= 450:
                dx = 320
                dy = 125
                dx2 = dx
                dy2 = dy
                story = 41
        
        elif story == 41:   #On sort de la cabane
            screen.blit(bg3, bg3rect)
            screen.blit(mov[x], [dx,dy])
            move()
            pygame.display.flip()
            if (0 < dx < 260 and 0 < dy < 150) or (0 < dx < 260 and 275 < dy < 550) or (420 < dx < 800 and 0 < dy < 150) or (420 < dx < 800 and 275 < dy < 550) or (dy > 450): #Zones de bloquage
                dx = dx2
                dy = dy2
            if 260 < dx < 420 and dy <= 100:
                if lvl < 10:
                    story = 401
                else:
                    if scenario == 0:
                        story = 52
                        scenario = 1
                    else:
                        story = 40    
                dx = 330
                dy = 350
                dx2 = 330
                dy2 = 350
            if (dx < 5): #Permet d'aller dans la zone de combat
                story = 411
                dx = 700
                dy = 170
                dx2 = 700
                dy2 = 170
            if (dx > 700): #Zone de bloquage situationnelle (Atteindre le niveau 10)
                if lvl >= 10 and scenario >= 1:
                    story = 61
                else :
                    dx = dx2
                    dy = dy2
        
        elif story == 42: #Zone de combat
            screen.blit(bg5, bg5rect)
            screen.blit(mov[x], [dx,dy])
            move()
            combat()
            pygame.display.flip()
            if (dy < 50) or (dx < 65) or (dy > 325) or (700 < dx < 800 and 0 < dy < 140) or (660 < dx < 800 and 250 < dy < 550):
                dx = dx2
                dy = dy2
            if dx > 735:    #Pour revenir dans la zone précédente
                story = 412
                dx = 20
                dy = 212
                dx2 = 20
                dy2 = 212
            if (65 < dx < 245): #Permet de rencontrer aléatoirement un monstre quand on marche dans les herbes mortes
                if meet == 1:
                    fight = 1
                    
        elif story == 43:  #Un monstre apparaît
             screen.blit(f1, f1rect)          #On affiche l'écran de combat
             screen.blit(zero, [100,110])     #On affiche le personnage en position de combat  
             screen.blit(mon1[x1], [500,80])  #On affiche le monstre 
             screen.blit(lvl1, lvl1rect) 
             if lvl + 2 < lvlm:
                 texte2 = police.render("LVL "+str(lvlm), 0, couleur_texte3)
                 screen.blit(texte2,(553,50))
             else:    
                 texte2 = police.render("LVL "+str(lvlm), 0, couleur_texte4)
                 screen.blit(texte2,(553,50))
             texte3 = police.render("LVL "+str(lvl), 0, couleur_texte4)
             screen.blit(texte3,(135,50))
             pygame.display.flip()

        elif story == 44:  #Que faire ?
             screen.blit(f2, f2rect)
             screen.blit(zero, [100,110])
             texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)   #On donne au texte la valeur des pv et des pv max
             screen.blit(texte,(35,345))    #On affiche le texte
             screen.blit(mon1[x1], [500,80])
             pygame.display.flip()
             
        elif story == 45: #Attaque
            if fey ==1: #Si l'on a pas utilisé Fey:
                screen.blit(f3, f3rect) #On affiche l'écran 1/1
            else:
                screen.blit(f8, f8rect) #Sinon on affiche l'écran 0/1
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip()
            
        elif story == 46:   #Kit
             if power == 1: #Si l'on a pas utisé la Puissance:
                screen.blit(f4, f4rect) #On affiche l'écran 1/1
             else:
                screen.blit(f5, f5rect) #Sinon on affiche l'écran 0/1
             screen.blit(zero, [100,110])
             texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
             screen.blit(texte,(35,345))
             screen.blit(mon1[x1], [500,80])
             pygame.display.flip()
             
        elif story == 47:   #Santé restaure les PV
            screen.blit(f6, f6rect)  
            screen.blit(zero, [100,110])
            screen.blit(at6, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip()
             
        elif story == 471:  #Puissance augmente l'attaque et la chance
            screen.blit(f7, f7rect) 
            screen.blit(zero, [100,110])
            screen.blit(at5, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip()
            
        elif story == 48: #Force est utilisée
            if crit == 1:   #Si on met un coup critique:
                if weak == 0: #Si la faiblesse du monstre est la Force
                    screen.blit(f45, f45rect) #On affiche Super efficace + Coup critique !
                else :                    
                    screen.blit(f10, f10rect) #On affiche Coup Critique !
            else:
                if weak == 0:
                    screen.blit(f44, f44rect) #On affiche Super efficace !
                else:
                    screen.blit(f9, f9rect) #Sinon on affiche l'écran normal
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            screen.blit(at1, [500,80])
            pygame.display.flip()
        
        elif story == 481:  #Magie est utilisée
            if crit == 1:
                if weak == 1: #Si la faiblesse du monstre est la Magie
                    screen.blit(f47, f47rect) #On affiche Super efficace + Coup critique !
                else :                    
                    screen.blit(f12, f12rect) 
            else:
                if weak == 1:
                    screen.blit(f46, f46rect) #On affiche Super efficace !
                else:
                    screen.blit(f11, f11rect) 
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            screen.blit(at2, [500,80])
            pygame.display.flip()
        
        elif story == 482:  #Fey : Je m'en charge !
            screen.blit(f13, f13rect)
            pygame.display.flip()
        
        elif story == 49: #Monstre reçoit d'énormes dégâts !
            screen.blit(f14, f14rect)
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            screen.blit(at3, [500,80])
            pygame.display.flip()
        
        elif story == 50: #Le monstre attaque
            if crit == 1:
                screen.blit(f16, f16rect)
            else:
                screen.blit(f15, f15rect)
            screen.blit(zero, [100,110])
            screen.blit(at4, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip()
            
        elif story == 501:  #Attaque manquée
            screen.blit(f17, f17rect)
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip()
        
        elif story == 502: #Attaque du monstre manquée
            screen.blit(f18, f18rect)
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip()
         
        elif story == 51:   #Victoire ! Vous gagnez de l'EXP !
            screen.blit(f19, f19rect)
            screen.blit(zero, [100,110])
            texte = police.render("LVL "+str(lvl), 0, couleur_texte4)
            screen.blit(texte,(35,345))
            pygame.display.flip()
            
        elif story == -2: #Vous n'avez plus de PV..
            screen.blit(f20, f20rect)
            screen.blit(zero, [100,110])
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(mon1[x1], [500,80])
            pygame.display.flip() 
            
        elif story == -1:   #Game over
            screen.blit(go, gorect)
            texte = police.render("-Cliquez pour recommencer-", 0, couleur_texte5)
            screen.blit(texte,(164,320))
            pygame.display.flip()
        
        elif story == 401:  #Le vieillard nous donne des conseils
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial30, dial30rect)
            pygame.display.flip()
        
        elif story == 402:  #Le vieillard nous donne des conseils
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial31, dial31rect)
            pygame.display.flip()
        
        elif story == 403:  #Le vieillard nous donne des conseils
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial32, dial32rect)
            pygame.display.flip()
        
        elif story == 404:  #Le vieillard nous donne des conseils
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial33, dial33rect)
            pygame.display.flip()
            
        elif story == 405:  #Le vieillard nous donne des conseils
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial34, dial34rect)
            pygame.display.flip()
        
        elif story == 52:   #Écran de sauvegarde
            restart = 2     #On ajoute 1 à restart pour sauvegarder à nouveau
            screen.blit(bs, bsrect)
            screen.blit(logo, [150, 100])
            pygame.display.flip()
   
        elif story == 53:   #Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial35, dial35rect)
            pygame.display.flip()
            
        elif story == 54:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial36, dial36rect)
            pygame.display.flip()
            
        elif story == 55:   #Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial37, dial37rect)
            pygame.display.flip()
            
        elif story == 56:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial38, dial38rect)
            pygame.display.flip()
            
        elif story == 57:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial39, dial39rect)
            pygame.display.flip()
        
        elif story == 58:   #On fait un choix
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(c4, c4rect)
            pygame.display.flip()
            
        elif story == 581:  #Choix 1: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial41, dial41rect)
            pygame.display.flip()
            
        elif story == 582:  #Choix 2: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial40, dial40rect)
            pygame.display.flip()
            
        elif story == 59:   #Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial42, dial42rect)
            pygame.display.flip()
            
        elif story == 60:   #Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial43, dial43rect)
            pygame.display.flip()
       
        elif story == 61:   #On fait un choix pour entrer dans la salle du boss
            screen.blit(bg3, bg3rect)
            screen.blit(mov[x], [dx,dy])
            screen.blit(c5, c5rect)
            pygame.display.flip()

        elif story == 62:   #Zone du boss
            screen.blit(bg6, bg6rect)   #On affiche le boss et sa zone
            screen.blit(mov[x], [dx,dy])
            pygame.display.flip()
        
        elif story == 63:   #Avilis parle
            screen.blit(bg6, bg6rect)
            screen.blit(dial44, dial44rect)
            screen.blit(mov[x], [dx,dy])
            pygame.display.flip()
            
        elif story == 64:   #Avilis parle
            screen.blit(bg6, bg6rect)
            screen.blit(dial45, dial45rect)
            screen.blit(mov[x], [dx,dy])
            pygame.display.flip()
            
        elif story == 65:   #Avilis vous défie !
            screen.blit(f21, f21rect)
            pv = pvi                     #On soigne tous les pv
            s2 = [50, 50, 50, 25, 0.95] #On donne ses statistiques au boss
            screen.blit(zero, [100,110])
            screen.blit(lvl2, lvl2rect)
            texte2 = police.render("LVL ??", 0, couleur_texte3)
            screen.blit(texte2,(653,50))
            texte3 = police.render("LVL "+str(lvl), 0, couleur_texte4)
            screen.blit(texte3,(135,50))
            pygame.display.flip()
            
        elif story == 66:   #Que faire ?
            screen.blit(f22, f22rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()

        elif story == 67: #Attaque
            if fey ==1:
                screen.blit(f23, f23rect)
            else:
                screen.blit(f28, f28rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()

        elif story == 68:   #Kit
            if power ==1:
                screen.blit(f24, f24rect)
            else:
                screen.blit(f25, f25rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()
            
        elif story == 69:   #Santé restaure les PV
            screen.blit(f26, f26rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at6, [100,110])
            pygame.display.flip()
            
        elif story == 691:  #Puissance augment l'attaque et le chance !
            screen.blit(f27, f27rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at5, [100,110])
            pygame.display.flip()

        elif story == 70:   #Force est utilisée
            if crit == 1:
                screen.blit(f30, f30rect) 
            else:
                screen.blit(f29, f29rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at1, [500,80])
            pygame.display.flip()
            
        elif story == 701:  #Magie est utilisée
            if crit == 1:
                screen.blit(f32, f32rect) 
            else:
                screen.blit(f31, f31rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at2, [500,80])
            pygame.display.flip()
        
        elif story == 702:  #Fey : Je m'en charge !
            screen.blit(f33, f33rect)
            pygame.display.flip()
         
        elif story == 71:   #Avilis reçoit d'énormes dégâts ! Hausse d'attaque !
            screen.blit(f34, f34rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at3, [500,80])
            pygame.display.flip()
            
        elif story == 72:   #Avilis attaque
            if crit == 1:
                screen.blit(f36, f36rect) 
            else:
                screen.blit(f35, f35rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at4, [100,110])
            pygame.display.flip()   
            
        elif story == 721:  #Attaque manquée
            screen.blit(f37, f37rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()
            
        elif story == 722:  #Attaque d'Avilis manquée
            screen.blit(f38, f38rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()
            
        elif story == 73:   #Avilis: Hors de ma vue !
            screen.blit(f41, f41rect)
            pygame.display.flip()
            
        elif story == 731: #Avilis fait d'énormes dégêts ! Baisse de défense ! 
            screen.blit(f42, f42rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            screen.blit(at7, [100,110])
            pygame.display.flip()
        
   
        
        elif story == 75:   #Victoire ! Vous avez vaincu Avilis !
            screen.blit(f39, f39rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()
            
        elif story == -3:   #Vous n'avez plus de PV..
            screen.blit(f40, f40rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()
            
        elif story == 76:   #Avilis s'énerve ! Toutes ses stats augmentent !
            screen.blit(f43, f43rect)
            texte = police.render(str(pv)+"/"+str(pvi)+" PV", 0, couleur_texte4)
            screen.blit(texte,(35,345))
            screen.blit(zero, [100,110])
            pygame.display.flip()
        
        elif story == 78:   #Le vieillard parle 
            dx = 330
            dy = 300
            x = 3
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial46, dial46rect)
            pygame.display.flip()
         
        elif story == 79:   #Le vieillard parle 
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial47, dial47rect)
            pygame.display.flip() 
            
        elif story == 80:   #Fey parle 
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial48, dial48rect)
            pygame.display.flip()
            
        elif story == 81:   #Dernier choix
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(c6, c6rect)
            pygame.display.flip()
        
        elif story == 811:  #Choix 1: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial49, dial49rect)
            pygame.display.flip()    
        
        elif story == 812:  #Choix 1: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial50, dial50rect)
            pygame.display.flip()
            
        elif story == 813:  #Choix 1: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial51, dial51rect)
            pygame.display.flip()
            
        elif story == 814: #Choix 1: Le personnage parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial52, dial52rect)
            pygame.display.flip()
        
        elif story == 815:  #Choix 1: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial53, dial53rect)
            pygame.display.flip()
            
        elif story == 816:  #Choix 1: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial54, dial54rect)
            pygame.display.flip()
            
        elif story == 817:  #Choix 1: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial55, dial55rect)
            pygame.display.flip()
            
        elif story == 82:   #Choix 2: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial57, dial57rect)
            pygame.display.flip()
            
        elif story == 83:   #Choix 2: Le personnage parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial52, dial52rect)
            pygame.display.flip()
        
        elif story == 84:   #Choix 2: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial58, dial58rect)
            pygame.display.flip()
        
        elif story == 85:   #Choix 2: Le vieillard parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial59, dial59rect)
            pygame.display.flip()
            
        elif story == 86:   #Choix 2: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial60, dial60rect)
            pygame.display.flip()
            
        elif story == 87:   #Choix 2: Fey parle
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial61, dial61rect)
            pygame.display.flip()
            
        elif story == 88 or story == 818:   #Partons à l'aventure !
            screen.blit(bg4, bg4rect)
            screen.blit(oya, [350,20])
            screen.blit(mov[x], [dx,dy])
            screen.blit(dial56, dial56rect)
            pygame.display.flip()
            
        elif story == 89:   #Fin du jeu
            screen.blit(bg7, bg7rect)
            pygame.display.flip()
            
        elif story == 90:   #Crédits
            screen.blit(bg8, bg8rect)
            pygame.display.flip()
      
               
#Pour les changements de musique
        elif story == 411 or story == 412 or story == 771: 
            screen.blit(bs, bsrect)
            screen.blit(logo, [150, 100])
            pygame.display.flip()
 
        
        pygame.display.flip()   #Met à jour le tout
        clock.tick(fps)

        #Debug
        #print(clock.get_fps())
        #print("Héros :"+str(s1)+" PV : "+str(pv))
        #print("Monstre :"+str(s2)+" PV : "+str(pvm))