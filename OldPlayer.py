import pygame
import pygame.image
import pygame.sprite
import Globals

class Player(pygame.sprite.Sprite):
    FRAMES = None
    SPRITEPACK = None  #the image of all the sprites
    jumpSPRITEPACK = None
    jumpFRAMES = None
    RATE = 100/1000.0	#time in milliseconds per frame
    def __init__(self, (xSpawn, ySpawn)):
        self.tempi = 0
        self.wasgrounded = 0
        self.permawasgrounded = 0
        self.land_delay = 0
        pygame.sprite.Sprite.__init__(self)
        if not Player.SPRITEPACK:
            #Player.SPRITEPACK = pygame.image.load("sonic.gif").convert_alpha()
            Player.SPRITEPACK = pygame.image.load("ed_run_transparent_trimmed.png").convert_alpha()
            #Player.SPRITEPACK = pygame.image.load("blacktest.png").convert_alpha()
            #self.spritePack = pygame.image.load("ed-jake.png").convert_alpha()
        if not Player.jumpSPRITEPACK:
            Player.jumpSPRITEPACK = pygame.image.load("jump_sprites_normalized_alpha.png")
        Player.jumpFRAMES = []
        for j in range(3):
            Player.jumpFRAMES.append(Player.jumpSPRITEPACK.subsurface((j*40,0),(40,63)).convert_alpha())        for j in range(3):
            Player.jumpFRAMES.append(pygame.transform.flip(Player.jumpSPRITEPACK.subsurface((j*40, 0), (40, 63)), 1, 0).convert_alpha())        Player.FRAMES = []
       # self.numjframes = 6 #
        #frames.append(self.spritePack.subsurface( (14, 6), (23, 78)))        for x in range(12):
            Player.FRAMES.append(Player.SPRITEPACK.subsurface((x*40, 0), (40, 63)))
        #number of right-facing frames (left facing come after)
        self.numframes = len(Player.FRAMES)
        for x in range(12):
            Player.FRAMES.append(pygame.transform.flip(Player.SPRITEPACK.subsurface((x*40, 0), (40, 63)), 1, 0))
        #for x in range(24):
            #Player.FRAMES[x].set_colorkey((255,255,255))
        self.frame = 0
        
        self.hadY = False
        self.jumped = 0
        self.image = Player.FRAMES[self.frame]
        self.elapsed = 0   #the elapsed time since frame was changed
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
        #print self.rect.topleft
        self.direction = 'right'
        self.time = 0
        self.jump_delay = 0 
        self.p = (float(xSpawn), float(ySpawn))
        self.v = (0,0)
        #remember that y positive is downward
        #this is your acceleration from jumping
        self.a = (0, 0)
        #the forces on the player (ie gravity)
        self.f = (0, 430)
        if self.rect.topleft[1] + self.image.get_height() == Globals.yRes - 2:
            self.grounded = 1
        else:
            self.grounded = 0    def draw(self, screen, time):        #Globals.Screen.blit(Player.FRAMES[1],(0,0))
        self.elapsed += time
        #print self.wasgrounded
        if self.elapsed > Player.RATE:
            if self.wasgrounded == 1 and self.jumped == 1:
               if (self.jump_delay < 1):
                    print self.jump_delay
                    if self.direction == 'right':
                        self.image = Player.jumpFRAMES[self.jump_delay + 1]
                    else:
                        self.image = Player.jumpFRAMES[self.jump_delay + 4]
                    self.jump_delay += 1
                    self.rect = self.image.get_rect()
                    self.rect.topleft = (int(self.p[0]), int(self.p[1]))
                    self.elapsed = 0
                    Globals.Screen.blit(self.image, self.rect.topleft)
                    return
                    print "Did not return"
               self.v = (self.v[0], -350)
               self.jumped = 0  
               self.jump_delay = 0             
            if self.grounded==1:
                if(self.land_delay < 2):
                    self.land_delay += 1
                    if(self.direction == 'right'):
                        self.image = Player.jumpFRAMES[1]
                    else:
                        self.image = Player.jumpFRAMES[4]
                else:
                    if self.direction == 'right':
                        if self.frame == self.numframes - 1:
                            self.frame = 0
                        else:
                            self.frame += 1
                    else:
                        if self.frame == (self.numframes * 2 - 1):
                            self.frame = self.numframes
                        else:
                            self.frame += 1
                    self.image = Player.FRAMES[self.frame]
            else:
                if(self.direction == 'right'):
                    self.image = Player.FRAMES[1]
                else:
                    self.image = Player.FRAMES[13]
            self.rect = self.image.get_rect()
            self.rect.topleft = (int(self.p[0]), int(self.p[1]))
            self.elapsed = 0
        else:
            self.permawasgrounded = self.wasgrounded
        #self.image = Player.jumpFRAMES[1]
        Globals.Screen.blit(self.image, self.rect.topleft)

    def update(self, delta, platforms):
        self.wasgrounded = self.grounded
        if delta == 0 or delta > .5:
            delta = 0.01
        self.v = (self.v[0] + self.f[0] * delta + self.a[0] * delta, self.v[1] + self.f[1] * delta + self.a[1] * delta)
        #temp0 = self.p[0] + self.v[0] * delta #calculation of new x position
        #temp1 =  self.p[1] + self.v[1] * delta # calculation of new y position
        temp =  (self.p[0] + self.v[0] * delta, self.p[1] + self.v[1] * delta)
        plattemp = temp
        #self.p = temp
        #self.rect.topleft = (int(temp[0]), int(temp[1]))
        #check platform collisions
        hitplat = False
        hitbound = False
        for p in platforms:
            #Top of platform collision
            if p.rect.topleft[1] <= temp[1] + self.image.get_height() and p.rect.topleft[1] >= self.p[1] + self.image.get_height():
                #y collision, need to check if x's overlap
                if p.rect.topleft[0] <= temp[0] + self.image.get_width() and self.rect.topleft[0] <= p.rect.topleft[0] + p.image.get_width():
                    #now we know the x overlaps
                    plattemp = (temp[0], p.rect.topleft[1] - self.image.get_height())
                    self.v = (self.v[0], 0)
                    hitplat = True
                    #print "TOP COLLISION"
                    self.grounded = 1
                    if self.wasgrounded == 0:
                        self.land_delay = 0
                    break
            #Bottom of platform collision
            if p.rect.topleft[1] + p.image.get_height() >= temp[1] and p.rect.topleft[1] + p.image.get_height() <= self.p[1]:
                #y collision, need to check if x's overlap
                if p.rect.topleft[0] <= temp[0] + self.image.get_width() and self.rect.topleft[0] <= p.rect.topleft[0] + p.image.get_width():
                    #now we know the x overlaps
                    plattemp = (temp[0], p.rect.topleft[1] + p.image.get_height() + 1)
                    self.v = (self.v[0], 0)
                    #print "BOTTOM COLLISION"
                    hitplat = True
                    break
            #Left of platform collision
            if p.rect.topleft[0] <= temp[0] + self.image.get_width() and p.rect.topleft[0] >= self.p[0] + self.image.get_width():
                #x collision, need to check if y's overlap
                if not p.rect.topleft[1] >= temp[1] + self.image.get_height() and not p.rect.topleft[1] + p.image.get_height() <= temp[1]:
                    #now we know the x overlaps
                    plattemp = (p.rect.topleft[0] - self.image.get_width(), temp[1])
                    #self.v = (0, self.v[1])
                    hitplat = True
                    #print "LEFT COLLISION"
                    break
            #Right of platform collision
            if p.rect.topleft[0] + p.image.get_width() >= temp[0] and p.rect.topleft[0] + p.image.get_width() <= self.p[0]:
                #y collision, need to check if x's overlap
                if not p.rect.topleft[1] >= temp[1] + self.image.get_height() and not p.rect.topleft[1] + p.image.get_height() <= temp[1]:
                    #now we know the x overlaps
                    plattemp = (p.rect.topleft[0] + p.image.get_width(), temp[1])
                    #print "RIGHT COLLISION"
                    #self.v = (0, self.v[1])
                    hitplat = True
                    break
        self.p = plattemp

        #check screen border collisions
        if temp[0] < 0:
            self.p = (0, temp[1])
            temp = (0, temp[1])
            hitbound = True
            #print "bottom"
        if temp[0] + self.image.get_width() >= Globals.xRes - 1:
            if hitplat:
                self.p = (Globals.xRes - self.image.get_width() - 1, self.p[1])
                temp = (Globals.xRes - self.image.get_width() - 1, self.p[1])
            else:
                self.p = (Globals.xRes - self.image.get_width() - 1, temp[1])
                temp = (Globals.xRes - self.image.get_width() - 1, temp[1])
            hitbound = True
        if temp[1] < 0:
            self.p = (self.p[0], 0)
            hitbound = True
            self.v = (self.v[0], 0)
        if temp[1] + self.image.get_height() >= Globals.yRes - 1:
            self.p = (280,0)
            hitbound = True
            self.grounded = 1

        if (not hitplat) and (not hitbound):
            self.p = temp
            self.grounded = 0
       # else:
       #     self.grounded = 1
        #self.p = (temp[0], self.p[1])
        self.rect.topleft = (int(self.p[0]), int(self.p[1]))
        #check if we are on the ground
        #if self.rect.topleft[1] > Globals.yRes - 5 - self.image.get_height():
        #    self.grounded = 1
        #else:
        #    self.grounded = 0
       # print "acceleration: "
       # print self.a
       # print "velocity: "
       # print self.v
       # print "position: "
       # print self.p
       # print "coordinates: "
       # print self.rect.topleft
       # self.a = (0, 0)
       # if self.grounded == 0:
       #    self.wasgrounded = 1   

    def move(self, (xChange, yChange)):
        self.v = (xChange, self.v[1])
        if xChange > 0 and self.direction == 'left':
            self.direction = 'right'
            self.frame = 0
        if xChange < 0 and self.direction == 'right':
            self.direction = 'left'
            self.frame = self.numframes

    def jump(self):
        if self.grounded == 1:            self.jumped = 1
            
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
