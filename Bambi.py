import pygame
import pygame.image
import pygame.sprite
import random as R
import Globals
import Character
import Enemy

class Bambi(pygame.sprite.Sprite):
    Bambi1 = None
    Bambi2 = None
    RATE = 100/1000.0
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.animToggle = 0
        if not Bambi.Bambi1:
            Bambi1 = pygame.image.load("Images/bambi_sit1_shrunk.png").convert_alpha()
        if not Bambi.Bambi2:
            Bambi2 = pygame.image.load("Images/bambi_sit2_shrunk.png").convert_alpha()
        self.FRAMES = []
        self.FRAMES.append(Bambi1.subsurface((8,12),(62,55)))
        self.FRAMES.append(Bambi2.subsurface((8,12),(62,55)))
        self.p = (xSpawn,ySpawn)
        self.image = self.FRAMES[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
        self.elapsed = 0

    def draw(self, screen, camera):
        #print "locx: " + str(self.rect.topleft[0]-camera.p[0]) + "locy: " + str(self.rect.topleft[1]-camera.p[1])
        Globals.Screen.blit(self.image, (self.rect.topleft[0]-camera.p[0],self.rect.topleft[1]-camera.p[1]))
        #Globals.Screen.blit(self.image,(300,200))

    def update(self, camera, delta):
        if(delta == 0 or delta > .5):
            delta = 0.01
        self.elapsed += delta
        if self.elapsed > Bambi.RATE:
            if self.animToggle < 2:
                self.image = self.FRAMES[0]
                self.animToggle += 1
            elif self.animToggle >= 2 and self.animToggle <= 7:
                self.image = self.FRAMES[1]
                self.animToggle += 1
            else:
                self.image = self.FRAMES[0]
                self.animToggle = 0

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.p[0],self.p[1])
