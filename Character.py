import pygame
import pygame.image
import pygame.sprite
import Globals
import AttackState

class Character(pygame.sprite.Sprite):
    SPRITEPACK = None  #the image of all the walk sprites
    jumpSPRITEPACK = None
    attackPACK = None
    WOLFMAN = None
    BOSS = None
    bossDEATH = None
    bossDMG = None
    RATE = 100/1000.0	#time in milliseconds per frame
    wolfDEATH = None
    EDSTILL = None
    wolfDMG = None
    JOCK = None
    jockATTACK = None
    shockwave = None
    BOSSwolf = None
    BOSSfire = None
    def __init__(self):
        self.air_attackDuration = 0
        self.attackDuration = 0
        self.isAttacking = 0
        self.gotHit = False
        self.invincible = False
        self.damageCounter = 0
        self.jumpVelSet = True
        self.jumped = 0
        #self.actionState = 0
        jumpFRAMES = None
        self.tempi = 0
        self.wasgrounded = 0
        self.permawasgrounded = 0
        self.takingdamage = 0
        self.land_delay = 5
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.hadY = False
        self.jumped = 0
        self.elapsed = 0   #the elapsed time since frame was changed
        self.time = 0
        self.jump_delay = 0
        self.runspeed = 140
        self.jumpspeed = -400
        self.direction = 'right'
        #self.runstate = 'stop'
        #keep track of our depressed keys
        self.leftkey = 0
        self.rightkey = 0
        #self.AttackState = AttackState.StillState()
        #remember that y positive is downward
        #this is your acceleration from jumping
        #self.a = (0, 0)
        #the forces on the player (ie gravity)
        self.f = (0, 430)


    def draw(self, screen, camera, time):
        pass
        
    def update(self, camera, delta, platforms):
        #print "action state is: " + str(self.actionState)
        #print "self.jump_delay is: " + str(self.jump_delay)
        #print "self.grounded is: " + str(self.grounded)
        if(delta == 0 or delta > .5):
            delta = 0.01
        #Character.chooseState(self)
        #if self.actionState == 0:
        #    Character.still_Update(self,camera,delta,platforms)
        #elif self.actionState == 1:
        #    Character.run_Update(self,camera,delta,platforms)
        #elif self.actionState == 2:
        #    Character.jump_Update(self,camera,delta,platforms)
        #elif self.actionState == 3:
        #    Character.stillAttack_Update(self,camera,delta,platforms)
        #elif self.actionState == 4:
        #    Character.jumpAttack_Update(self,camera,delta,platforms)
        #elif self.actionState == 5:
        #    Character.runAttack_Update(self,camera,delta,platforms)
        #elif self.actionState == 6:
        #    Character.stillDamage_Update(self,camera,delta,platforms)
        #elif self.actionState == 7:
        #    Character.runDamage_Update(self,camera,delta,platforms)
        #elif self.actionState == 8:
        #    Character.jumpDamage_Update(self,camera,delta,platforms)
        #else:
        #    Character.still_Update(self,camera,delta,platforms)
        self.AttackState.update(self,camera,delta,platforms)

    
    def slapEnemies(self,camera,delta,platforms):
        hitbox = pygame.sprite.Sprite()
        if(self.direction == 'right'):
            hitbox.rect = pygame.Rect(self.rect.topleft[0]+self.image.get_width(), self.rect.topleft[1] + 10,20, 20)
        else:
            hitbox.rect = pygame.Rect(self.rect.topleft[0] - 20,self.rect.topleft[1] + 10,20,20)
        #hitbox is 20x20 pixels, shifted 10 pixels down from edward's top
        enemies = Globals.State.enemies
        for e in enemies:
            if pygame.sprite.collide_rect(hitbox,e):
                e.invincible = False
                e.damageCounter = 1
                e.health -= 50
                e.attackReady = False
                #print "hit enemy!"
        jocks = Globals.State.jocks
        for j in jocks:
            if pygame.sprite.collide_rect(hitbox,j):
                j.invincible = False
                j.damageCounter = 1
                j.health -= 50
                j.attackReady = False
        gargs = Globals.State.gargs
        for g in gargs:
            if pygame.sprite.collide_rect(hitbox,g):
                g.invincible = False
                g.damageCounter = 1
                g.health -= 50
                g.attackReady = False
                
    def sparkleEnemies(self,camera):
        print "Sparkling"
        hitbox = pygame.sprite.Sprite()
        hitbox.rect = pygame.Rect(self.rect.topleft[0] - 80, self.rect.topleft[1] -50 ,196, 152)
        enemies = Globals.State.enemies
        for e in enemies:
            if pygame.sprite.collide_rect(hitbox,e):
                print "hit enemy!"
                e.sparkled()
                
 
    def platCollide(self,camera,delta,platforms):
        self.v = (self.v[0] + self.f[0] * delta, self.v[1] + self.f[1] * delta)
        temp =  (self.p[0] + self.v[0] * delta, self.p[1] + self.v[1] * delta)
        plattemp = temp
        hitplat = False
        #hittop = False
        
        for p in platforms:
            #Bottom of platform collision
            if p.rect.topleft[1] + p.image.get_height() >= temp[1] and p.rect.topleft[1] + p.image.get_height() <= self.p[1]:
                #y collision, need to check if x's overlap
                if p.rect.topleft[0] <= temp[0] + self.image.get_width() - 5 and self.rect.topleft[0] <= (p.rect.topleft[0] + p.image.get_width() - 1):
                    #now we know the x overlaps
                    plattemp = (plattemp[0], p.rect.topleft[1] + p.image.get_height() + 1)
                    #if(self.jump_delay != 0 or self.AttackState != AttackState.JumpState()):
                    self.v = (self.v[0],0)
                    hitplat = True
            #Left of platform collision
            if p.rect.topleft[0] <= temp[0] + self.image.get_width() and p.rect.topleft[0] >= self.p[0] + self.image.get_width():
                #x collision, need to check if y's overlap
                if not p.rect.topleft[1] +4 >= temp[1] + self.image.get_height() and not p.rect.topleft[1] + p.image.get_height() <= temp[1]+4:
                    #now we know the y overlaps
                    plattemp = (p.rect.topleft[0] - self.image.get_width(), plattemp[1])
                    self.v = (0, self.v[1])
                    if self.player==0:
                        self.v = (-self.v[0], self.v[1])
                        self.leftkey = 1
                        self.rightkey = 0
                        self.direction = 'left'
                    hitplat = True
            #Right of platform collision
            if p.rect.topleft[0] + p.image.get_width() >= temp[0] and p.rect.topleft[0] + p.image.get_width() <= self.p[0]:
                #y collision, need to check if x's overlap
                if not p.rect.topleft[1] + 4 >= temp[1] + self.image.get_height() and not p.rect.topleft[1] + p.image.get_height() <= temp[1]+4:
                    #now we know the y overlaps
                    plattemp = (p.rect.topleft[0] + p.image.get_width(), plattemp[1])
                    self.v = (0, self.v[1])
                    if self.player==0:
                        self.v = (-self.v[0], self.v[1])
                        self.rightkey = 1
                        self.leftkey = 0
                        self.direction = 'right'
                    hitplat = True
            #Top of platform collision
            if p.rect.topleft[1] <= temp[1] + self.image.get_height() and p.rect.topleft[1] >= self.p[1] + self.image.get_height():
                #y collision, need to check if x's overlap
                if (p.rect.topleft[0]<= temp[0] + self.image.get_width() and self.rect.topleft[0] <= p.rect.topleft[0] + p.image.get_width()):
                    #now we know the x overlaps
                    plattemp = (plattemp[0], p.rect.topleft[1] - self.image.get_height())
                    #if(self.jump_delay != 0 or self.AttackState != AttackState.JumpState()):
                        #self.hittop = True
                    if self.v[1] > 1000:
                        self.health = 0
                    self.v = (self.v[0], 0)
                    hitplat = True
                    if self.player == 1:
                        print "TOP COLLISION"
                    self.grounded = 1
        #print self.direction
        #for sprite in pygame.sprite.spritecollide(self, platforms, False):
            #if self.player == 1:
                #print sprite
        #    plattemp = (plattemp[0], sprite.rect.topleft[1] - self.image.get_height())
        self.p = plattemp
        if (not hitplat):
            #self.p = temp
        #if not hittop:
            self.grounded = 0
        self.rect.topleft = (int(self.p[0]), int(self.p[1]))

    #chooses state based on the following  variables:
    #self.gotHit --> goes to a taking damage state
    #not self.grounded --> goes to a jump state
    #self.v[0] == 0 --> goes to a stationary state
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
                self.AttackState = AttackState.JumpAttackState()
            elif self.rightkey == 0 and self.leftkey ==0: #x velocity is 0 and grounded --> stationary attack
                #self.actionState = 3
                self.AttackState = AttackState.StillAttackState()
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
        #print "chosen state was (should be 3): " + str(self.actionState)

    def move(self, (xChange, yChange)):
        self.v = (xChange, self.v[1])
        if xChange > 0 and self.direction == 'left':
            self.direction = 'right'
            self.frame = 0
        if xChange < 0 and self.direction == 'right':
            self.direction = 'left'
            self.frame = self.numframes

    def jump(self):
        if self.grounded == 1:
            self.grounded = 0
            self.jumped = 1
            self.v = (self.v[0], self.jumpspeed)
            self.jumped = 0
            #if(self.direction == 'right'):
            #    self.image = char.FRAMES[1]
            #else:
            #    char.image = char.FRAMES[char.numframes+1]
            
"""
    def update(self, delta):
        self.time = delta
        if self.rect.topleft[0] <= 0 and self.v[0] < 0:
            self.stop('x')
        elif self.rect.topleft[0] + self.image.get_width() >= Globals.xRes and self.v[0] > 0:
            self.stop('x')
        elif self.rect.topleft[0] + self.v[0] * self.time <= 0:
            self.stop('x')
            self.rect.topleft = (0, self.rect.topleft[1])
        elif self.rect.topleft[0] + self.image.get_width() + self.v[0] * self.time >= Globals.xRes:
            self.stop('x')
            self.rect.topleft = (Globals.xRes - self.image.get_width(), self.rect.topleft[1])
        else: #update x
            self.rect.topleft = (self.rect.topleft[0] + self.v[0] * self.time + self.a[0] * self.time * self.time, self.rect.topleft[1])


        if self.rect.topleft[1] <= 0 and self.v[1] < 0:
            self.stop('y')
        elif self.rect.topleft[1] + self.image.get_height() >= Globals.yRes and self.v[1] > 0:
            self.stop('y')
        elif self.rect.topleft[1] + self.v[1] * self.time + self.a[1] * self.time * self.time <= 0:
            self.stop('y')
            self.rect.topleft = (self.rect.topleft[0], 0)
        elif self.rect.topleft[1] + self.image.get_height() + self.v[1] * self.time + self.a[1] * self.time * self.time >= Globals.yRes:
            self.stop('y')
            self.rect.topleft = (self.rect.topleft[0], Globals.yRes - self.image.get_height())
        else: #update y
            self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + self.v[1] * self.time + self.a[1] * self.time * self.time)

    def move(self, (xChange, yChange)):
        if (not self.rect.topleft[0] + self.image.get_width() >= Globals.xRes or not self.rect.topleft[0] <= 0) and self.v[0] < 3:
            self.v = (self.v[0] + xChange, self.v[1])
            if xChange > 0 and self.direction == 'left':
                self.direction = 'right'
                self.frame = 0
            if xChange < 0 and self.direction == 'right':
                self.direction = 'left'
                self.frame = self.numframes
        if (not self.rect.topleft[1] >= Globals.yRes or not self.rect.topleft[1] + self.image.get_height() <= 0) and self.v[1] < 3:
            self.v = (self.v[0], self.v[1] + yChange)

    def stop(self, direction):
        if direction == 'x':
            self.v = (0, self.v[1])
        else:
            self.v = (self.v[0],0)
"""
