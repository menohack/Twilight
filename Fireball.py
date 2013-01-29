import pygame
import pygame.image
import pygame.sprite
import Globals
import Projectile
import Enemy
import Character

Projectile = Projectile.Projectile
#Character = Character.Character
class Fireball(Projectile):
    FIREBALL = None
    def __init__(self,(xSpawn,ySpawn),(vx,vy)):
        Projectile.__init__(self,(xSpawn,ySpawn),(vx,vy))
        if not Fireball.FIREBALL:
            Fireball.FIREBALL = pygame.image.load("Images/jake-fireball_shrunk.png").convert_alpha()
        self.FRAMES = []
        self.FRAMES.append(Fireball.FIREBALL.subsurface((22,26),(30,20)))
        self.FRAMES.append(Fireball.FIREBALL.subsurface((4,54),(30,20)))
        self.FRAMES.append(pygame.transform.flip(self.FRAMES[0],1,0))
        self.FRAMES.append(pygame.transform.flip(self.FRAMES[1],1,0))
        

    def draw(self,screen,camera,time):
        Projectile.draw(self,screen,camera,time)

    def update(self,camera,delta,platforms):
        Projectile.update(self,camera,delta,platforms)
        if self.v[0] < 0:
            if(self.animToggle):
                self.image = self.FRAMES[0]
            else:
                self.image = self.FRAMES[1]
        else:
            if(self.animToggle):
                self.image = self.FRAMES[2]
            else:
                self.image = self.FRAMES[3]
        self.animToggle = not self.animToggle
