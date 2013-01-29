import pygame
import pygame.image
import pygame.sprite
import Globals

#projectile constructor takes two tuples: spawn location and veloctiy pair
class Projectile(pygame.sprite.Sprite):
    RATE = 100/1000.0
    SHOCKWAVE = None
    def __init__(self,(xSpawn,ySpawn),(vx,vy)):
        pygame.sprite.Sprite.__init__(self)
        if not Projectile.SHOCKWAVE:
            Projectile.SHOCKWAVE = pygame.image.load("Images/shockwave.png").convert_alpha()
        self.FRAMES = []
        #append the two images
        self.FRAMES.append(Projectile.SHOCKWAVE.subsurface((0,0),(29,23)))
        self.FRAMES.append(Projectile.SHOCKWAVE.subsurface((29,0),(29,23)))
        self.image = self.FRAMES[0]
        self.animToggle = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
        self.p = (float(xSpawn),float(ySpawn))
        self.v = (vx,vy)
        self.elapsed = 0

    def draw(self, screen, camera, time):
        #if camera.xScrolling == 'right':
        #    temp = (camera.rightBorder - self.image.get_width(), camera.edwardScreen[1])
        #elif camera.xScrolling == 'left':
        #    temp = (camera.leftBorder, camera.edwardScreen[1])
        #else:
        #    temp = camera.edwardScreen

        #if camera.yScrolling == 'down':
        #    temp = (temp[0], camera.bottomBorder - self.image.get_height())
        #elif camera.yScrolling == 'up':
        #    temp = (temp[0], camera.topBorder)
   




        #Globals.Screen.blit(self.image,(200,150))
        Globals.Screen.blit(self.image, (self.p[0] - camera.p[0], self.p[1] - camera.p[1]))

    def update(self, camera, delta, platforms):
        if (delta == 0 or delta > .5):
            delta = 0.01
        self.elapsed += delta
        if self.elapsed > Projectile.RATE:
            self.p = (self.p[0]+(self.v[0]*self.elapsed),self.p[1]+(self.v[1]*self.elapsed))
            self.rect = self.image.get_rect()
            self.rect.topleft = (int(self.p[0]),int(self.p[1]))
            self.elapsed = 0
            if(self.animToggle):
                self.image = self.FRAMES[0]
            else:
                self.image = self.FRAMES[1]
            self.animToggle = not self.animToggle
        if self.p[0] < camera.p[0] or self.p[0] > camera.p[0] + Globals.xRes:
            Globals.State.projectiles.remove(self)



