import pygame
import pygame.image
import pygame.sprite
import random as R
import Globals
import Character
import Enemy
import AttackState

Character = Character.Character

class Enemy(Character):
    def __init__(self,(xSpawn,ySpawn)):
        Character.__init__(self)
	#xSpawn = R.randint(0,Globals.xRes - 40)
	#ySpawn = R.randint(0,Globals.yRes - 40)
        xSpawn = xSpawn
        ySpawn = ySpawn
        self.dead = False
        self.deathCounter = 0
        self.deathSound = pygame.mixer.Sound("Sounds/WolfGrowl.ogg")
        if not Character.WOLFMAN:
            #Enemy.IMAGE = pygame.image.load("sonic.gif").convert_alpha()
            #Enemy.IMAGE = pygame.image.load("ed-jake.png").convert_alpha()
             Character.WOLFMAN = pygame.image.load("Images/wolfman_walk_shrunk.png").convert_alpha()
        #frames.append(Enemy.IMAGE.subsurface( (2, 46), (22, 35)))
        if not Character.wolfDEATH:
             Character.wolfDEATH = pygame.image.load("Images/wolf_death_shrunk.png").convert_alpha()
        if not Character.wolfDMG:
             Character.wolfDMG = pygame.image.load("Images/wolf_dmg_shrunk.png").convert_alpha()
        self.deathFRAMES = []
        self.deathFRAMES.append(Character.wolfDEATH.subsurface((0,15),(54,27))) #left
        self.deathFRAMES.append(pygame.transform.flip(Character.wolfDEATH.subsurface((0,15),(54,27)),1,0))#right
        self.dmgFRAMES = []
        self.dmgFRAMES.append(Character.wolfDMG.subsurface((9,0),(23,44)))#left dmg
        self.dmgFRAMES.append(pygame.transform.flip(Character.wolfDMG.subsurface((9,0),(23,44)),1,0))
        blank = pygame.Surface((23,44))

        blank.fill((0,0,0))

        blank.set_colorkey((0,0,0))

        self.dmgFRAMES.append(blank)

        self.jumpFRAMES = []
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[5])
        self.FRAMES = []
        self.FRAMES.append(pygame.transform.flip(Character.WOLFMAN.subsurface((0, 0), (23, 44)), 1, 0).convert_alpha())
        self.FRAMES.append(pygame.transform.flip(Character.WOLFMAN.subsurface((24, 0), (23, 44)), 1, 0).convert_alpha())
        self.FRAMES.append(pygame.transform.flip(Character.WOLFMAN.subsurface((48, 0), (23, 44)), 1, 0).convert_alpha())
        self.FRAMES.append(pygame.transform.flip(Character.WOLFMAN.subsurface((71, 0), (23, 44)), 1, 0).convert_alpha())
        self.numframes = 4 #NOT AFFECTING ANYTHING
        self.FRAMES.append(Character.WOLFMAN.subsurface( (0, 0), (23, 44)))
        self.FRAMES.append(Character.WOLFMAN.subsurface( (24, 0), (23, 44)))
        self.FRAMES.append(Character.WOLFMAN.subsurface( (48, 0), (23, 44)))
        self.FRAMES.append(Character.WOLFMAN.subsurface( (71, 0), (23, 44)))
        self.FRAMES.append(self.FRAMES[1]) #STILL RIGHT
        self.FRAMES.append(self.FRAMES[5]) #STILL LEFT
        #frames[0].set_colorkey((255,255,255))
        self.image = self.FRAMES[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
        #self.rect.right = xSpawn + self.image.get_width()
        #self.rect.left = xSpawn
	#self.rect.bottom = ySpawn + self.image.get_height()
        #self.rect.top = ySpawn
        #self.v = (R.randint(-2,2),R.randint(-2,2))
        self.direction = 'left'
        self.elapsed = 0

        self.rightkey = 0
        self.leftkey = 1
        self.p = (float(xSpawn), float(ySpawn))

        self.v = (0,0)
        self.runspeed = 90

        self.grounded = 1

        self.player = 0
        self.inSparkle = 0
        self.health = 200
        self.attackReady = True
        self.AttackState = AttackState.StillState()

    def draw(self, screen, camera, time):
        #Globals.Screen.blit(self.image, self.rect.topleft)
        #if self.direction == 'left':
        #    self.image = self.FRAMES[0]
        #elif self.direction == 'right':
        #    self.image = self.FRAMES[1]
        #print "self.frame is:" + str(self.frame)
        #print "self.grounded is:" + str(self.grounded)
        #print "self.rightkey is:" + str(self.rightkey)
        #print "self.leftkey is:" + str(self.leftkey)
        #print "self.direction is:" + str(self.direction)
        #Character.draw(self, screen, camera, time)
        Globals.Screen.blit(self.image, (self.rect.topleft[0]-camera.p[0],self.rect.topleft[1]-camera.p[1]))
    
    def update(self, camera, delta, platforms):
        
        jumpRand = R.randint(0,100)
        #if jumpRand == 3 and self.grounded == 1:
        #    self.v = (self.v[0],-370)
        #if self.rect.topleft[0] + self.image.get_width() >= camera.p[0]+ Globals.xRes - 1:
        #    self.leftkey = 1
        #    self.rightkey = 0
        #    self.direction = 'left'
        #elif self.rect.topleft[0] <= camera.p[0]:
        #    self.rightkey = 1
        #    self.leftkey = 0
        #    self.direction = 'right'
        if self.health == 0:
            self.dead = True
            self.deathSound.play(0,0,0)
        self.chooseState()
        Character.update(self, camera, delta, platforms)

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

    def slapPlayer(self,camera,delta,platforms):
        hitbox = pygame.sprite.Sprite()
        if(self.direction == 'right'):
            hitbox.rect = pygame.Rect(self.rect.topleft[0]+self.image.get_width(), self.rect.topleft[1] + 10,20, 40)
        else:
            hitbox.rect = pygame.Rect(self.rect.topleft[0] - 20,self.rect.topleft[1] + 10,20,40)
        player = Globals.State.player
        if pygame.sprite.collide_rect(hitbox,player):
            #dmg state
            if self.inSparkle == 0:
                player.gotHit = True
   
class Boss(Enemy):
    def __init__(self,(xSpawn, ySpawn)):
        Character.__init__(self)
        self.madeFIRE = False
        self.dead = False
        self.deathCounter = 0
        self.inSparkle = 0
        self.blindLength = 1.5
        self.howlSound = pygame.mixer.Sound("Sounds/wolfHowl.ogg")
        self.deathSound = pygame.mixer.Sound("Sounds/WolfGrowl.ogg")
        self.hitGroundSound = pygame.mixer.Sound("Sounds/hitGround.ogg")
        self.wolfSlashSound = pygame.mixer.Sound("Sounds/wolfSlash.ogg")
        self.wolfHitSound = pygame.mixer.Sound("Sounds/wolfHit.ogg")
        if not Character.BOSSfire:
            Character.BOSSfire = pygame.image.load("Images/jake-fireball_shrunk.png").convert_alpha()
        if not Character.BOSS:
            Character.BOSS = pygame.image.load("Images/jake_run_final.png").convert_alpha()
        if not Character.BOSSwolf:
            Character.BOSSwolf = pygame.image.load("Images/jake_wolf_run_final.png").convert_alpha()
        if not Character.bossDEATH:
            #Character.bossDEATH = pygame.image.load("Images/wolf_death_shrunk.png").convert_alpha()
            Character.bossDEATH = pygame.image.load("Images/jake_wolf_run_final.png").convert_alpha()
        #if not Character.bossDMG:
        #    Character.bossDMG = pygame.image.load("Images/wolf_dmg_shrunk.png").convert_alpha()
        #self.normalAttackPACK = None
        #if not self.normalAttackPACK:
        self.fireFRAMES = [] #left then right facing frames
        self.fireFRAMES.append(Character.BOSSfire.subsurface((107,7),(53,108)))
        self.fireFRAMES.append(Character.BOSSfire.subsurface((54,8),(53,108)))
        self.fireFRAMES.append(pygame.transform.flip(self.fireFRAMES[0],1,0))
        self.fireFRAMES.append(pygame.transform.flip(self.fireFRAMES[1],1,0))
        

        self.transPACK = pygame.image.load("Images/jake_transform.png").convert_alpha()
        self.transFRAMES = []
        self.transFRAMES.append(pygame.transform.flip(self.transPACK.subsurface((53,0),(53,108)),1,0))
        self.transFRAMES.append(pygame.transform.flip(self.transPACK.subsurface((0,0),(53,108)),1,0))
        self.transFRAMES.append(self.transPACK.subsurface((53,0),(53,108)))
        self.transFRAMES.append(self.transPACK.subsurface((0,0),(53,108)))
        self.normalAttackPACK = pygame.image.load("Images/jake_normal_attack.png").convert_alpha()
        self.normalAttackFRAMES = []
        self.normalAttackFRAMES.append(pygame.transform.flip(self.normalAttackPACK.subsurface((106,0), (53, 108)).convert_alpha(),1,0))
        self.normalAttackFRAMES.append(pygame.transform.flip(self.normalAttackPACK.subsurface((53,0), (53, 108)).convert_alpha(),1,0))
        self.normalAttackFRAMES.append(pygame.transform.flip(self.normalAttackPACK.subsurface((0,0), (53, 108)).convert_alpha(),1,0))

        self.normalAttackFRAMES.append(self.normalAttackPACK.subsurface((106,0), (53, 108)).convert_alpha())
        self.normalAttackFRAMES.append(self.normalAttackPACK.subsurface((53,0), (53, 108)).convert_alpha())
        self.normalAttackFRAMES.append(self.normalAttackPACK.subsurface((0,0), (53, 108)).convert_alpha())

        self.jumpAttackPACK = pygame.image.load("Images/jake_jumpattack_final2.png").convert_alpha()
        self.jumpAttackFRAMES = []
        self.jumpAttackFRAMES.append(pygame.transform.flip(self.jumpAttackPACK.subsurface((0,0), (53, 108)).convert_alpha(),1,0))
        self.jumpAttackFRAMES.append(pygame.transform.flip(self.jumpAttackPACK.subsurface((53,0), (53, 108)).convert_alpha(),1,0))
        self.jumpAttackFRAMES.append(pygame.transform.flip(self.jumpAttackPACK.subsurface((106,0), (53, 108)).convert_alpha(),1,0))
        self.jumpAttackFRAMES.append(pygame.transform.flip(self.jumpAttackPACK.subsurface((159,0), (41, 108)).convert_alpha(),1,0))
        self.jumpAttackFRAMES.append(pygame.transform.flip(self.jumpAttackPACK.subsurface((200,0), (65, 108)).convert_alpha(),1,0))

        self.jumpAttackFRAMES.append(self.jumpAttackPACK.subsurface((0,0), (53, 108)).convert_alpha())
        self.jumpAttackFRAMES.append(self.jumpAttackPACK.subsurface((53,0), (53, 108)).convert_alpha())
        self.jumpAttackFRAMES.append(self.jumpAttackPACK.subsurface((106,0), (53, 108)).convert_alpha())
        self.jumpAttackFRAMES.append(self.jumpAttackPACK.subsurface((159,0), (41, 108)).convert_alpha())
        self.jumpAttackFRAMES.append(self.jumpAttackPACK.subsurface((200,0), (65, 108)).convert_alpha())

        self.wolfAttackPACK = pygame.image.load("Images/jake_wolf_attack.png").convert_alpha()
        #Wolf Attack
        self.wolfAttackFRAMES = []
        self.wolfAttackFRAMES.append(pygame.transform.flip(self.wolfAttackPACK.subsurface((0,0), (53, 108)).convert_alpha(),1,0))
        self.wolfAttackFRAMES.append(pygame.transform.flip(self.wolfAttackPACK.subsurface((53,0), (53, 108)).convert_alpha(),1,0))
        self.wolfAttackFRAMES.append(pygame.transform.flip(self.wolfAttackPACK.subsurface((106,0), (53, 108)).convert_alpha(),1,0))
        self.wolfAttackFRAMES.append(self.wolfAttackPACK.subsurface((0,0), (53, 108)).convert_alpha())
        self.wolfAttackFRAMES.append(self.wolfAttackPACK.subsurface((53,0), (53, 108)).convert_alpha())
        self.wolfAttackFRAMES.append(self.wolfAttackPACK.subsurface((106,0), (53, 108)).convert_alpha())
        #self.shockwavePACK = pygame.image.load("Images/shockwave.png").convert_alpha()
        #self.shockwaveFRAMES = []
        #self.shockwaveFRAMES.append(self.shockwavePACK.subsurface((0,0), (29, 23)))
        #self.shockwaveFRAMES.append(self.shockwavePACK.subsurface((29,0), (29, 23)))
        self.deathFRAMES = []
        self.deathFRAMES.append(pygame.transform.rotate(Character.bossDEATH.subsurface((212,0),(53,108)),90))
        self.deathFRAMES.append(pygame.transform.flip(self.deathFRAMES[0],1,0))#right
        #self.deathFRAMES.append(Character.bossDEATH.subsurface((0,15),(54,27))) #left
        #self.deathFRAMES.append(pygame.transform.flip(Character.bossDEATH.subsurface((0,15),(54,27)),1,0))#right
       
        self.madeWave = False
        self.jumpFRAMES = []
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[1])
        self.jumpFRAMES.append(self.FRAMES[5])
        self.FRAMES = []
        self.FRAMES.append(pygame.transform.flip(Character.BOSS.subsurface((0, 0), (53, 108)), 1, 0).convert_alpha())
        self.FRAMES.append(pygame.transform.flip(Character.BOSS.subsurface((53, 0), (53, 108)), 1, 0).convert_alpha())
        self.FRAMES.append(pygame.transform.flip(Character.BOSS.subsurface((106, 0), (53, 108)), 1, 0).convert_alpha())
        self.FRAMES.append(pygame.transform.flip(Character.BOSS.subsurface((159, 0), (53, 108)), 1, 0).convert_alpha())
        self.numframes = 4 #NOT AFFECTING ANYTHING
        self.FRAMES.append(Character.BOSS.subsurface( (0, 0), (53, 108)))
        self.FRAMES.append(Character.BOSS.subsurface( (53, 0), (53, 108)))
        self.FRAMES.append(Character.BOSS.subsurface( (106, 0), (53, 108)))
        self.FRAMES.append(Character.BOSS.subsurface( (159, 0), (53, 108)))
        self.FRAMES.append(self.FRAMES[1]) #STILL RIGHT
        self.FRAMES.append(self.FRAMES[5]) #STILL LEFT
        #Wolf walk cycle, etc.
        self.wolfFRAMES = []
        self.wolfFRAMES.append(pygame.transform.flip(Character.BOSSwolf.subsurface((0, 0), (53, 108)), 1, 0).convert_alpha())
        self.wolfFRAMES.append(pygame.transform.flip(Character.BOSSwolf.subsurface((53, 0), (53, 108)), 1, 0).convert_alpha())
        self.wolfFRAMES.append(pygame.transform.flip(Character.BOSSwolf.subsurface((106, 0), (53, 108)), 1, 0).convert_alpha())
        self.wolfFRAMES.append(pygame.transform.flip(Character.BOSSwolf.subsurface((159, 0), (53, 108)), 1, 0).convert_alpha())
        self.numframes = 4 #NOT AFFECTING ANYTHING
        self.wolfFRAMES.append(Character.BOSSwolf.subsurface( (0, 0), (53, 108)))
        self.wolfFRAMES.append(Character.BOSSwolf.subsurface( (53, 0), (53, 108)))
        self.wolfFRAMES.append(Character.BOSSwolf.subsurface( (106, 0), (53, 108)))
        self.wolfFRAMES.append(Character.BOSSwolf.subsurface( (159, 0), (53, 108)))
        self.wolfFRAMES.append(self.FRAMES[1]) #STILL RIGHT
        self.wolfFRAMES.append(self.FRAMES[5]) #STILL LEFT
        self.dmgFRAMES = []
        self.dmgFRAMES.append(self.FRAMES[1])#left dmg
        self.dmgFRAMES.append(self.FRAMES[5])
        blank = pygame.Surface((53,108))

        blank.fill((0,0,0))

        blank.set_colorkey((0,0,0))
        self.fire = None
        self.dmgFRAMES.append(blank)
        self.image = self.FRAMES[4]
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
        self.direction = 'right'
        self.rightkey = 0
        self.leftkey = 1
        self.jumping = False
        self.p = (float(xSpawn), float(ySpawn))
        self.v = (-100,0)
        self.grounded = 1
        self.runspeed = 100
        self.player = 0
        self.health = 800
        self.attackReady = True
        self.whichAttack = 0
        self.isWolf = 0
        self.transCounter = -1
        

    def draw(self, screen, camera, time):
        Enemy.draw(self, screen, camera, time)
        
    def sparkled(self):
        self.inSparkle = 1

    def update(self, camera, delta, platforms):
        if(self.isWolf):
            self.dmgFRAMES[0]=self.wolfFRAMES[1]
            self.dmgFRAMES[1]=self.wolfFRAMES[5]
        Enemy.update(self, camera, delta, platforms)
        
    def chooseState(self):
        if self.inSparkle == 1:
            self.AttackState = AttackState.SparkledState()
            return
        if self.health < 499 and self.transCounter == -1:
            self.transCounter = 0
            if self.direction == 'right':
                self.image = self.transFRAMES[0]
            else:
                self.image = self.transFRAMES[2]
            self.rect = self.image.get_rect()
            self.rect.topleft = (int(self.p[0]), int(self.p[1]))
            self.AttackState = AttackState.WolfTransState()
            self.howlSound.play()
            return
        if self.transCounter >= 0 and self.transCounter < 5:
            self.AttackState = AttackState.WolfTransState()
            self.runspeed = 200
            self.isWolf = 1
            self.jumping = False
            return
        attackRand = R.randint(0,100)
        #print attackRand
        if attackRand == 5 and self.isAttacking == 0 and self.attackReady == True:
            self.isAttacking = 1
            #print "Attack"
        if self.dead == True:
            self.AttackState = AttackState.deadState()
        elif self.damageCounter != 0: #some type of taking damage
            #self.wolfHitSound.play()
            if self.grounded == 0: #jump damage
                #self.actionState = 8
                self.AttackState = AttackState.JumpDamageState()
            elif self.rightkey == 0 and self.leftkey == 0: #x velocity is 0 and grounded --> stationary damage
                #self.actionState = 6
                self.AttackState = AttackState.StillDamageState()
            else: #moving damage
                #self.actionState = 7
                self.AttackState = AttackState.RunDamageState()
        elif self.isAttacking == 1 and self.attackReady == True: #some type of attacking and not taking damage
            self.attackReady = False
            #if self.isWolf == 0:
            self.whichAttack = R.randint(0,1)
            #print whichAttack
            if self.whichAttack == 1 and self.isWolf == 0 and (Globals.State.level == '3' or Globals.State.level == '4'):
                 #self.runspeed = 200
                self.jumping = False
                self.hitGroundSound.play()
                self.AttackState = AttackState.SmashAttackState()
            elif self.jumping == False and self.isWolf == 0:
                #print "shockwave"
            #self.runspeed = 100
                self.hitGroundSound.play()
                self.AttackState = AttackState.ShockwaveAttackState()
            elif self.jumping == False and self.isWolf == 1 and self.whichAttack == 1:
                #print "Nug"
                self.wolfSlashSound.play()
                self.AttackState = AttackState.SlashAttackState()
            elif self.jumping == False and self.isWolf == 1 and (Globals.State.level == '4'):
                #print "Nug"
                self.AttackState = AttackState.FireAttackState()
        elif self.isAttacking == 0: #not taking damage or attacking
            if self.grounded == 0: #jump
                #self.actionState = 2
                self.AttackState = AttackState.JumpState()
            elif self.leftkey == 0 and self.rightkey==0: #still
                #self.actionState = 0
                self.AttackState = AttackState.StillState()
            else: #running
                #self.actionState = 1
                if self.isWolf == 1:
                   self.OLDFRAMES = self.FRAMES
                   self.FRAMES = self.wolfFRAMES
                self.AttackState = AttackState.RunState()
        #print "chosen state was (should be 3): " + str(self.AttackState)
                

                    
