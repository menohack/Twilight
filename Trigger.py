import pygame
import pygame.image
import pygame.sprite
import Globals

class Trigger1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn), (width, height)):
        pygame.sprite.Sprite.__init__(self)
        #self.image= pygame.image.load("Images/table.png").convert_alpha()
        self.rect = pygame.rect.Rect((xSpawn,ySpawn), (width, height))
        #self.image.set_colorkey((3, 254, 62))
        #self.rect.topleft = (xSpawn,ySpawn)
        self.triggered = 0
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera, player):
        #self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn
        if pygame.sprite.collide_rect(self, player) == 1:
            self.triggered = 1
            return 1
        else:
            self.triggered = 0
            return 0
