import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

#Fenêtre
resolution = (465, 450)
fen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Pac Man") #Titre de la fenêtre BG

loadImg = pygame.image.load
blit = fen.blit

game_icon = loadImg("Images/Pac/Pac_Menu2.png").convert_alpha()
pygame.display.set_icon(game_icon) # Icone de la fenêtre

# Musique
pygame.mixer.music.load("Sons\pacman_beginning.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0)

# Sonsbeginning
soundExtraPac = pygame.mixer.Sound("Sons\pacman_chomp.wav")
soundExtraPac.set_volume(0.5)

#Menu
menubg = loadImg("Images\Menu\Menu.png")

#Pacman
pac_droite1 = loadImg("Images\Pac\Pac_Droite1.png").convert_alpha()
pac_droite2 = loadImg("Images\Pac\Pac_Droite2.png").convert_alpha()
pac_gauche1 = loadImg("Images\Pac\Pac_Gauche1.png").convert_alpha()
pac_gauche2 = loadImg("Images\Pac\Pac_Gauche2.png").convert_alpha()
pac_haut1 = loadImg("Images\Pac\Pac_Haut1.png").convert_alpha()
pac_haut2 = loadImg("Images\Pac\Pac_Haut2.png").convert_alpha()
pac_bas1 = loadImg("Images\Pac\Pac_Bas1.png").convert_alpha()
pac_bas2 = loadImg("Images\Pac\Pac_Bas2.png").convert_alpha()
pac_boule = loadImg("Images\Pac\Pac_Boule.png").convert_alpha()

#Inky
inky_bas1 = loadImg("Images\Fantomes\Inky\Inky_bas1.png").convert_alpha()
inky_bas2 = loadImg("Images\Fantomes\Inky\Inky_bas2.png").convert_alpha()
inky_droite1 = loadImg("Images\Fantomes\Inky\Inky_droite1.png").convert_alpha()
inky_droite2 = loadImg("Images\Fantomes\Inky\Inky_droite2.png").convert_alpha()
inky_gauche1 = loadImg("Images\Fantomes\Inky\Inky_gauche1.png").convert_alpha()
inky_gauche2 =loadImg("Images\Fantomes\Inky\Inky_gauche2.png").convert_alpha()
inky_haut1 = loadImg("Images\Fantomes\Inky\Inky_haut1.png").convert_alpha()
inky_haut2 = loadImg("Images\Fantomes\Inky\Inky_haut2.png").convert_alpha()

#Blinky
blinky_bas1 = loadImg("Images\Fantomes\Blinky\Blinky_bas1.png").convert_alpha()
blinky_bas2 = loadImg("Images\Fantomes\Blinky\Blinky_bas2.png").convert_alpha()
blinky_droite1 = loadImg("Images\Fantomes\Blinky\Blinky_droite1.png").convert_alpha()
blinky_droite2 = loadImg("Images\Fantomes\Blinky\Blinky_droite2.png").convert_alpha()
blinky_gauche1 = loadImg("Images\Fantomes\Blinky\Blinky_gauche1.png").convert_alpha()
blinky_gauche2 =loadImg("Images\Fantomes\Blinky\Blinky_gauche2.png").convert_alpha()
blinky_haut1 = loadImg("Images\Fantomes\Blinky\Blinky_haut1.png").convert_alpha()
blinky_haut2 = loadImg("Images\Fantomes\Blinky\Blinky_haut2.png").convert_alpha()

#Pinky
pinky_bas1 = loadImg("Images\Fantomes\Pinky\Pinky_bas1.png").convert_alpha()
pinky_bas2 = loadImg("Images\Fantomes\Pinky\Pinky_bas2.png").convert_alpha()
pinky_droite1 = loadImg("Images\Fantomes\Pinky\Pinky_droite1.png").convert_alpha()
pinky_droite2 = loadImg("Images\Fantomes\Pinky\Pinky_droite2.png").convert_alpha()
pinky_gauche1 = loadImg("Images\Fantomes\Pinky\Pinky_gauche1.png").convert_alpha()
pinky_gauche2 =loadImg("Images\Fantomes\Pinky\Pinky_gauche2.png").convert_alpha()
pinky_haut1 = loadImg("Images\Fantomes\Pinky\Pinky_haut1.png").convert_alpha()
pinky_haut2 = loadImg("Images\Fantomes\Pinky\Pinky_haut2.png").convert_alpha()

#Clyde
clyde_bas1 = loadImg("Images\Fantomes\Clyde\Clyde_bas1.png").convert_alpha()
clyde_bas2 = loadImg("Images\Fantomes\Clyde\Clyde_bas2.png").convert_alpha()
clyde_droite1 = loadImg("Images\Fantomes\Clyde\Clyde_droite1.png").convert_alpha()
clyde_droite2 = loadImg("Images\Fantomes\Clyde\Clyde_droite2.png").convert_alpha()
clyde_gauche1 = loadImg("Images\Fantomes\Clyde\Clyde_gauche1.png").convert_alpha()
clyde_gauche2 =loadImg("Images\Fantomes\Clyde\Clyde_gauche2.png").convert_alpha()
clyde_haut1 = loadImg("Images\Fantomes\Clyde\Clyde_haut1.png").convert_alpha()
clyde_haut2 = loadImg("Images\Fantomes\Clyde\Clyde_haut2.png").convert_alpha()

#Pac-gommes
pac_gum = loadImg("Images/HUD/pac_gomme.png").convert_alpha()
super_pac_gum = loadImg("Images/HUD/super_pac_gomme.png").convert_alpha()

#Fond
bg = loadImg("Images/HUD/background.png")
laby= loadImg("Images/HUD/laby.png")

# HUD
loseGame = loadImg("Images/HUD/game_over.png").convert_alpha()