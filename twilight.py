import pygame
import sys
import random
import pygame.display
import pygame.draw
import pygame.event
import pygame.font
import pygame.time
import pygame.mixer
import pygame.image
import Globals
import Player
import Enemy
import Title
import Cutscenes
import thread
import os
if os.name == 'nt':
    print "Disabling Wiimote; you're using windows!"
else:
    import cwiid
    import Wiimote


def init():
    #Globals.Wiimote = Wiimote.Wiimote()
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()

    Globals.xRes = 640
    Globals.yRes = 480
    Globals.Screen = pygame.display.set_mode((Globals.xRes,Globals.yRes), pygame.FULLSCREEN)
    #Globals.Screen = pygame.display.set_mode((Globals.xRes,Globals.yRes))

    pygame.mouse.set_visible(False)

    pygame.mixer.init(44100, -16, 2, 4096)

    Globals.Clock = pygame.time.Clock()
    Globals.Font = pygame.font.Font(None, 28)
    thread.start_new_thread(assignCutscenes, ())
    Globals.State = Title.Title()


def loop():
    while Globals.Running:
        Globals.State.draw()
        Globals.State.update()

def assignCutscenes():
    Globals.Cutscenes = Cutscenes.Cutscenes()


def main():
    init()
    loop()
    finalize()

def finalize():
    pygame.display.quit()
    sys.exit()

if __name__ == "__main__":
    main()
