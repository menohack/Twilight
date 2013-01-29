import pygame
import pygame.image
import pygame.sprite
import Globals

#projectile constructor takes two tuples: spawn location and veloctiy pair
class Hud(pygame.sprite.Sprite):
    RATE = 100/1000.0
    HPBARS = None
    RED = None
    YELLOW = None
    GREEN = None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if not Hud.HPBARS:
            Hud.RED = pygame.image.load("Images/red_bar.png").convert_alpha()
            Hud.YELLOW = pygame.image.load("Images/yellow_bar.png").convert_alpha()
            Hud.GREEN = pygame.image.load("Images/green_bar.png").convert_alpha()
        self.FRAMES = []
        self.FRAMES.append(Hud.GREEN.subsurface((2,5),(200,28)))
        self.FRAMES.append(Hud.YELLOW.subsurface((0,0),(110,30)))
        self.FRAMES.append(Hud.RED.subsurface((0,0),(49,30)))
        #Green ->yellow->red AND long->short
        self.hpimage = self.FRAMES[0]
        self.rect = self.hpimage.get_rect()
        self.rect.topleft = (200,150)
        self.p = (200,150)
        self.elapsed = 0

    def draw(self):
        Globals.Screen.blit(self.hpimage,(70,40))

    def update(self, delta):
        if (delta == 0 or delta > .5):
            delta = 0.01
        self.elapsed += delta
        if self.elapsed > Hud.RATE:
            
            self.rect = self.hpimage.get_rect()
            self.rect.topleft = (int(self.p[0]),int(self.p[1]))
            self.elapsed = 0
            hp = float(Globals.State.player.health)
            mh = float(Globals.State.player.maxhealth)
            #print "ratio is: " + str(float(hp/mh))
            #print "length should be: " + str(int(200*(hp/mh)))
            if hp/mh >= .7:
                self.hpimage = pygame.transform.scale(self.FRAMES[0],(int(200*(hp/mh)),self.hpimage.get_height()))
            elif hp/mh < .7 and hp/mh >= .25:
                self.hpimage = pygame.transform.scale(self.FRAMES[1],(int(200*(hp/mh)),self.hpimage.get_height()))
            else:
                self.hpimage = pygame.transform.scale(self.FRAMES[2],(int(200*(hp/mh)),self.hpimage.get_height()))
            
    
"""
            if hp == 250*4:
                self.hpimage = self.FRAMES[0]
            elif hp == 210*4:
                self.hpimage = pygame.transform.scale(self.FRAMES[0],(200,self.hpimage.get_height()))
            elif hp == 170*4:
                self.hpimage = pygame.transform.scale(self.FRAMES[0],(170,self.hpimage.get_height()))
            elif hp == 130*4:
                self.hpimage = pygame.transform.scale(self.FRAMES[1],(130,self.hpimage.get_height()))
            elif hp == 90*4:
                self.hpimage = pygame.transform.scale(self.FRAMES[1],(90,self.hpimage.get_height()))
            elif hp == 50*4:
                self.hpimage = pygame.transform.scale(self.FRAMES[2],(60,self.hpimage.get_height()))
            elif hp == 10*4:
                self.hpimage = pygame.transform.scale(self.FRAMES[2],(30,self.hpimage.get_height()))
"""                
      




