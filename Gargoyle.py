import pygame
import pygame.image
import pygame.sprite
import Globals
import Character
import Enemy
import Victory
import AttackState
Character = Character.Character
Enemy = Enemy.Enemy

class Gargoyle(Enemy):
    gSPRITEPACK = None
    deathPACK = None
    RATE = 100/1000.0

    def __init__(self,(xSpawn,ySpawn)):#,xVel):#,travelDistance):
        if not Gargoyle.gSPRITEPACK:
            Gargoyle.gSPRITEPACK = pygame.image.load("Images/gargoyle-fly_shrunk.png").convert_alpha()
        if not Gargoyle.deathPACK:
            Gargoyle.deathPACK = pygame.image.load("Images/gargoyle-death_shrunk.png").convert_alpha()
        self.FRAMES = []
        self.FRAMES.append(Gargoyle.gSPRITEPACK.subsurface((5,55),(63,76)))
        self.FRAMES.append(Gargoyle.gSPRITEPACK.subsurface((68,55),(63,76)))
        self.FRAMES.append(Gargoyle.gSPRITEPACK.subsurface((133,55),(63,76)))
        self.FRAMES.append(pygame.transform.flip(self.FRAMES[0],1,0))
        self.FRAMES.append(pygame.transform.flip(self.FRAMES[1],1,0))
        self.FRAMES.append(pygame.transform.flip(self.FRAMES[2],1,0))
        self.numframes = 3
        blank = pygame.Surface((63,76))
        blank.fill((0,0,0))
        blank.set_colorkey((0,0,0))
        self.dmgFRAMES = []
        self.dmgFRAMES.append(self.FRAMES[1])
        self.dmgFRAMES.append(self.FRAMES[4])
        self.dmgFRAMES.append(blank)

        self.deathFRAMES = []
        self.deathFRAMES.append(Gargoyle.deathPACK.subsurface((23,63),(100,91)))
        self.deathFRAMES.append(Gargoyle.deathPACK.subsurface((142,108),(130,54)))
        self.deathFRAMES.append(pygame.transform.flip(self.deathFRAMES[0],1,0))
        self.deathFRAMES.append(pygame.transform.flip(self.deathFRAMES[1],1,0))

        Character.__init__(self)
        self.player = 0
        self.dead = False
        self.deathCounter = 0
        self.State = None
        self.p = (xSpawn,ySpawn)
        self.v = (180,0)
        self.travelDistance = 300
        self.invincible = False
        self.xInitial = xSpawn
        self.image = self.FRAMES[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
        self.elapsed = 0
        self.attackReady = True
        self.gotHit = False
        self.AttackState = AttackState.gRunState()
        self.f = (0,0)
        self.health = 400

        #self.numFrames = 


    def draw(self,screen,camera,time):
        Globals.Screen.blit(self.image, (self.rect.topleft[0]-camera.p[0],self.rect.topleft[1]-camera.p[1]))

    def update(self, camera, delta, platforms):
        if self.health == 0:
            self.dead = True
        self.chooseState()
        #print "Garg at x: " + str(self.p[0]) + "and y: " + str(self.p[1])
        Character.update(self,camera,delta,platforms)

    def chooseState(self):
        if self.dead == True:
            self.AttackState = AttackState.gdeadState()
        elif self.damageCounter != 0:
            self.AttackState = AttackState.gRunDamageState()
        else:
            self.AttackState = AttackState.gRunState()


       
   
