import pygame
import pygame.image
import pygame.sprite
import random as R
import Globals
import Character
import Enemy
import AttackState

Character = Character.Character

class Jock(Character):
    def __init__(self,(xSpawn,ySpawn)):
        Character.__init__(self)
        xSpawn = xSpawn
        ySpawn = ySpawn
        self.deathSound = pygame.mixer.Sound("Sounds/PitFall2.ogg")
        self.dead = False
        self.deathCounter = 0
        self.player = 0
#        self.deathSound = pygame.mixer.Sound("")
        #walk cycle sprite sheet
        if not Character.JOCK:
            Character.JOCK = pygame.image.load("Images/jock-walk_normalized.png").convert_alpha()
        if not Character.jockATTACK:
            Character.jockATTACK = pygame.image.load("Images/jock-walk-attack_normalized.png").convert_alpha()
#        if not Character.jockDMG:
#            Character.jockDMG = pygame.image.load("Images/").convert_alpha()
        self.deathFRAMES = []
        self.deathFRAMES.append(pygame.transform.rotate(Character.JOCK.subsurface((0,0),(29,55)),90))
        self.deathFRAMES.append(pygame.transform.flip(self.deathFRAMES[0],1,0))
        self.dmgFRAMES = []
        self.dmgFRAMES.append(Character.JOCK.subsurface((0,0),(29,55)))
        self.dmgFRAMES.append(pygame.transform.flip(self.dmgFRAMES[0],1,0))
        #keep this surface the same size as rest of sprites
        blank = pygame.Surface((29,55))
        blank.fill((0,0,0))
        blank.set_colorkey((0,0,0))
        self.dmgFRAMES.append(blank)
        self.jumpFRAMES = []
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpAttackFRAMES = []
        self.jumpAttackFRAMES.append(self.FRAMES[1])
        self.jumpAttackFRAMES.append(pygame.transform.flip(self.dmgFRAMES[0],1,0))
        self.FRAMES = []
        #self.stillFRAMES = []
        #self.stillFRAMES.append(self.FRAMES[1])
        #walkframes
        for i in range(4):
            self.FRAMES.append(pygame.transform.flip(Character.JOCK.subsurface((i*29,0),(29,55)),1,0))
        for i in range(4):
            self.FRAMES.append(pygame.transform.flip(self.FRAMES[i],1,0))
        self.numframes = 4
        self.attackFRAMES = []
        self.numAttackFrames = 4
        for i in range(4):
            self.attackFRAMES.append(pygame.transform.flip(Character.jockATTACK.subsurface((i*29,0),(29,55)),1,0))
        for i in range(4):
            self.attackFRAMES.append(pygame.transform.flip(self.attackFRAMES[i],1,0))
        self.image = self.FRAMES[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
        self.direction = 'right'
        self.rightkey = 1
        self.leftkey = 0
        self.p = (float(xSpawn),float(ySpawn))
        self.v = (0,0)
        self.runspeed = 90
        self.isJock = 1;
        self.grounded = 1
        self.player = 0
        self.health = 200
        self.attackReady = True
        self.AttackState = AttackState.StillState()

    def draw(self, screen, camera, time):
        Globals.Screen.blit(self.image, (self.rect.topleft[0]-camera.p[0],self.rect.topleft[1]-camera.p[1]))

    def update(self, camera, delta, platforms):
        attackRand = R.randint(0,100)
        if (attackRand > 92 and self.attackReady==1 and self.grounded==1):
            self.isAttacking = 1
        if self.health == 0:
            self.dead = True
            self.deathSound.play(0,0,0)
        Character.update(self, camera, delta, platforms)
        self.chooseState()

    def chooseState(self):
        if self.dead == True:
            self.AttackState = AttackState.deadState()
        elif self.damageCounter != 0: #some type of taking damage
            if self.grounded == 0: #jump damage
                #self.actionState = 8
                self.AttackState = AttackState.JumpDamageState()
            elif self.rightkey == 0 and self.leftkey == 0: #x velocity is 0 and grounded --> stationary damage
                #self.actionState = 6
                self.AttackState = AttackState.StillDamageState()
            else: #moving damage
                #self.actionState = 7
                self.AttackState = AttackState.RunDamageState()
        elif self.isAttacking == 1: #some type of attacking and not taking damage
            if self.grounded == 0: #jump attack
                #self.actionState = 4
                self.AttackState = AttackState.RunAttackState()
            elif self.rightkey == 0 and self.leftkey ==0: #x velocity is 0 and grounded --> stationary attack
                #self.actionState = 3
                self.AttackState = AttackState.RunAttackState()
            else: #run attack
                #self.actionState = 5
                self.AttackState = AttackState.RunAttackState()
        else: #not taking damage or attacking
            if self.grounded == 0: #jump
                #self.actionState = 2
                self.AttackState = AttackState.JumpState()
            elif self.leftkey == 0 and self.rightkey==0: #still
                #self.actionState = 0
                self.AttackState = AttackState.StillState()
            else: #running
                #self.actionState = 1
                self.AttackState = AttackState.RunState()
        #print "chosen state w

    def slapPlayer(self,camera,delta,platforms):
        hitbox = pygame.sprite.Sprite()
        if(self.direction == 'right'):
            hitbox.rect = pygame.Rect(self.rect.topleft[0]+self.image.get_width(), self.rect.topleft[1] + 10,20, 20)
        else:
            hitbox.rect = pygame.Rect(self.rect.topleft[0] - 20,self.rect.topleft[1] + 10,20,20)
        #hitbox is 20x20 pixels, shifted 10 pixels down from Jock's top
        player = Globals.State.player
        if pygame.sprite.collide_rect(hitbox,player):
            #dmg state
            player.gotHit = True
