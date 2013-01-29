import pygame
import pygame.image
import pygame.sprite
import Globals
import Menu
import Character
import pygame.font as pf
import Victory
import Trigger
import random as R
import AttackState
import Game

Character = Character.Character

class Player(Character):
    EAT_BAMBI_1 = None
    EAT_BAMBI_2 = None
    EAT_BAMBI_3 = None

    def __init__(self, (xSpawn, ySpawn)):
        Character.__init__(self)
        Globals.Font = pf.Font(None,40)
        if not Player.EAT_BAMBI_1:
            Player.EAT_BAMBI_1 = pygame.image.load("Images/ed-eatbambi1_shrunk.png").convert_alpha()
        if not Player.EAT_BAMBI_2:
            Player.EAT_BAMBI_2 = pygame.image.load("Images/ed-eatbambi2_shrunk.png").convert_alpha()
        if not Player.EAT_BAMBI_3:
            Player.EAT_BAMBI_3 = pygame.image.load("Images/ed-eatbambi3_shrunk.png").convert_alpha()
        if not Character.EDSTILL:
            Character.EDSTILL = pygame.image.load("Images/ed-still-transparent.png").convert_alpha()

        self.BAMBI_FRAMES = []
        #RIGHT THEN LEFT
        self.BAMBI_FRAMES.append(Player.EAT_BAMBI_1.subsurface((10,6),(40,63)))
        self.BAMBI_FRAMES.append(Player.EAT_BAMBI_2.subsurface((10,6),(40,63)))
        self.BAMBI_FRAMES.append(Player.EAT_BAMBI_3.subsurface((10,6),(40,63)))
        self.BAMBI_FRAMES.append(pygame.transform.flip(self.BAMBI_FRAMES[0],1,0))
        self.BAMBI_FRAMES.append(pygame.transform.flip(self.BAMBI_FRAMES[1],1,0))
        self.BAMBI_FRAMES.append(pygame.transform.flip(self.BAMBI_FRAMES[2],1,0))
        self.bambiCounter = 0
        
            #Character.EDSTILL.set_colorkey((255,255,255))
        
        if not Character.SPRITEPACK:
            Character.SPRITEPACK = pygame.image.load("Images/ed_run_transparent_trimmed.png").convert_alpha()
        if not Character.jumpSPRITEPACK:
            Character.jumpSPRITEPACK = pygame.image.load("Images/jump_sprites_normalized_alpha.png")
        Character.jumpFRAMES = []

        Player.sparklePACK = pygame.image.load("Images/ed-sparkle-normalized.png")
        self.sparkleFrames = []
        for a in range(2):
            self.sparkleFrames.append(Player.sparklePACK.subsurface((a*40,0),(40,63)).convert_alpha())
        for a in range(2):
            self.sparkleFrames.append(pygame.transform.flip(Player.sparklePACK.subsurface((a*40,0),(40,63)).convert_alpha(),1,0))
        if not Player.attackPACK:
            Player.attackPACK = pygame.image.load("Images/ed-still-slap_normalized2.png")
        Player.jumpAttackPACK = pygame.image.load("Images/ed-jump-slap_normalized2.png")
        self.stillFRAMES = []
        self.stillFRAMES.append(Character.EDSTILL.subsurface((0,0),(40,63)))
        self.stillFRAMES.append(pygame.transform.flip(Character.EDSTILL.subsurface((0,0),(40,63)),1,0))
        self.jumpAttackFRAMES = []
        self.jumpAttackFRAMES.append(Player.jumpAttackPACK.subsurface((0,0),(40,63)).convert_alpha())
        self.jumpAttackFRAMES.append(pygame.transform.flip(Player.jumpAttackPACK.subsurface((0,0),(40,63)).convert_alpha(),1,0))
        self.dead = False
        self.attackFRAMES = []
        for a in range(2):
            self.attackFRAMES.append(Player.attackPACK.subsurface((a*40,0),(40,63)).convert_alpha())
        for a in range(2):
            self.attackFRAMES.append(pygame.transform.flip(Player.attackPACK.subsurface((a*40,0),(40,63)).convert_alpha(),1,0))
        self.numAttackFrames = 2
        self.attackSound = pygame.mixer.Sound("Sounds/Ed_Slap.wav")
        self.sparkleSound = pygame.mixer.Sound("Sounds/SparkleCharge.ogg")
        self.sparkleFireSound = pygame.mixer.Sound("Sounds/SparkleFire.ogg")
        self.shortHitSounds = []
        self.shortHitSounds.append(pygame.mixer.Sound("Sounds/EdShortHit1.ogg"))
        self.shortHitSounds.append(pygame.mixer.Sound("Sounds/EdShortHit2.ogg"))
        self.shortHitSounds.append(pygame.mixer.Sound("Sounds/EdShortHit3.ogg"))
        self.longDamageSounds = []
        self.longDamageSounds.append(pygame.mixer.Sound("Sounds/EdwardDamage2.ogg"))
        self.longDamageSounds.append(pygame.mixer.Sound("Sounds/EdwardDamage3.ogg"))
        self.imissyou = pygame.mixer.Sound("Sounds/imissyouquiet.ogg")
        self.missYouTrigger = Trigger.Trigger1((1230,1280), (80,80))
        #self.missedyou = False
        self.isSparkling = 0
        self.sparkleSoundPlayed = 0
        self.sparkleCloud = 0
        self.sparkleCloudImage = pygame.image.load("Images/sparkleCloud.png")
        self.gotBambi = False
        for j in range(3):
            self.jumpFRAMES.append(Character.jumpSPRITEPACK.subsurface((j*40,0),(40,63)).convert_alpha())
        for j in range(3):
            self.jumpFRAMES.append(pygame.transform.flip(Character.jumpSPRITEPACK.subsurface((j*40, 0), (40, 63)), 1, 0).convert_alpha())
        Character.FRAMES = []
        for x in range(12):
            self.FRAMES.append(Character.SPRITEPACK.subsurface((x*40, 0), (40, 63)))
        #number of right-facing frames (left facing come after)
        self.numframes = len(self.FRAMES)
        for x in range(12):
            self.FRAMES.append(pygame.transform.flip(Character.SPRITEPACK.subsurface((x*40, 0), (40, 63)), 1, 0))
        self.dmgFRAMES = []
        self.dmgFRAMES.append(pygame.image.load("Images/ed_hit_shrunk.png").convert_alpha())
        self.dmgFRAMES.append(pygame.transform.flip(pygame.image.load("Images/ed_hit_shrunk.png").convert_alpha(),1,0))
        blank = pygame.Surface((40,63))
        blank.fill((0,0,0))
        blank.set_colorkey((0,0,0))
        self.dmgFRAMES.append(blank)
        self.frame = 0
        self.image = self.FRAMES[self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
        self.p = (float(xSpawn), float(ySpawn))
        self.v = (0,0)
        self.damagetime = 0
        self.takingdamage = 0
        self.hpsurf= Globals.Font.render("100",True,(255,0,0))
        self.maxhealth = 1000
        self.health = self.maxhealth
        #self.winTrigger = Trigger.Trigger1((4120,1566), (80, 80))
        self.player = 1
        if self.rect.topleft[1] + self.image.get_height() == Globals.yRes - 2:
            self.grounded = 1
        else:
            self.grounded = 0
        self.hitTimes = 0
        self.AttackState = AttackState.StillState()
        self.paused = False
    
    def draw(self, screen, camera, time):
        Character.draw(self, screen, camera, time)
        if camera.xScrolling == 'right':
            temp = (camera.rightBorder - self.image.get_width(), camera.edwardScreen[1])
        elif camera.xScrolling == 'left':
            temp = (camera.leftBorder, camera.edwardScreen[1])
        else:
            temp = camera.edwardScreen

        if camera.yScrolling == 'down':
            temp = (temp[0], camera.bottomBorder - self.image.get_height())
        elif camera.yScrolling == 'up':
            temp = (temp[0], camera.topBorder)
        if self.sparkleCloud > 0:
            self.sparkleEnemies(camera)
            temp1 = (temp[0] - 80, temp[1] - 50)
            Globals.Screen.blit(self.sparkleCloudImage, temp1)
        Globals.Screen.blit(self.image, temp)

        #Globals.Screen.blit(self.hpsurf,(100 ,150))

    def update(self, camera, delta, platforms, enemies):
        #print "Player at x: " + str(self.p[0]) + "and y: " + str(self.p[1])
        #triggers moved to Game
        miss = R.randint(0,30000)
        if self.sparkleCloud > 0:
            self.sparkleCloud -= 1
        else:
            self.sparkleCloud = 0
        if miss == 765:
            self.imissyou.play(0,0,0)
            #self.missedyou = True
        Player.checkTriggers(self, camera)
        #update hp
        self.hpsurf = Globals.Font.render("HP: " + str(self.health),True,(255,0,0))



        #enemies = Globals.State.enemies
        for e in enemies:
            if pygame.sprite.collide_rect(self,e) and not self.invincible and e.attackReady:
                self.gotHit = True
        if isinstance(Globals.State, Game.Game):
            gargs = Globals.State.gargs
            for g in gargs:
                if pygame.sprite.collide_rect(self,g) and not self.invincible and g.attackReady:
                    self.gotHit = True

        if isinstance(Globals.State, Game.Game):
            projectiles = Globals.State.projectiles
            for p in projectiles:
                if pygame.sprite.collide_rect(self,p) and not self.invincible:
                    self.gotHit = True

            powerups = Globals.State.powerups
            for pw in powerups:
                if pygame.sprite.collide_rect(self,pw) and self.grounded == 1:
                    self.gotBambi = True
                    Globals.State.powerups.remove(pw)

        if self.gotHit and not self.invincible:
            self.damageCounter = 1
            self.health -= 40
            if(self.hitTimes < 3):
                self.shortHitSounds[R.randint(0,2)].play(0,0,0)
                self.hitTimes += 1
            else:
                self.longDamageSounds[R.randint(0,1)].play(0,0,0)
                self.hitTimes = 0
        self.gotHit = False
        if isinstance(Globals.State, Game.Level4) and self.p[1] > 1250:
            Globals.State.backgroundTrack.stop()
            Globals.State = Game.Level4()
           
        self.chooseState()
        Character.update(self, camera, delta, platforms)

#        if self.damagetime >= 1:
#            self.takingdamage = 0
#        if self.takingdamage == 1:
#            self.damagetime += delta
#        for e in enemies:
#            if pygame.sprite.collide_rect(self, e):
#                if self.takingdamage == 0:
#                    self.health -= 40
#                    self.takingdamage = 1
#                    self.damageCounter = 1
#                    break
        camera.update(self.p, self.image.get_width(), self.image.get_height())

    #chooses state based on the following  variables:
    #self.gotHit --> goes to a taking damage state
    #not self.grounded --> goes to a jump state
    #self.v[0] == 0 --> goes to a stationary state
    def chooseState(self):
        if self.gotBambi == True and self.grounded==1:
            self.AttackState = AttackState.StillBambiState()
            return
        if self.dead == True:
            self.AttackState = AttackState.deadState()
        if self.paused == True:
            self.AttackState = AttackState.StillState()
        elif self.damageCounter != 0: #some type of taking damage
            self.isSparkling = 0
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
        elif self.isSparkling == 1:
            self.AttackState = AttackState.SparkleAttackState()
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

    def checkTriggers(self, camera):
        pass
        #if self.missYouTrigger.update(camera, self) == 1 and not self.missedyou:
        #    self.imissyou.play(0,0,0)
        #    self.missedyou = True
        #if self.winTrigger.update(camera,self) == 1 and Globals.State.level == '1':
        #    Globals.State.backgroundTrack.stop()
            #Globals.State.level = '2'
            #Globals.State.drawMap('2')
            #Globals.State.background = Globals.State.level0
            #self.p = (400, 400)
        #    Globals.State = Game.Level2()
            #Globals.State = Victory.Victory()
            
        #if self.health <= 0:
        #    Globals.State.backgroundTrack.stop()
        #    Globals.State = Menu.Menu()
                
    def move(self, command):
        #self.v = (xChange, self.v[1])
        #if xChange > 0 and self.direction == 'left':
        #if command == 'right_down' and self.direction == 'left':
        #    self.direction = 'right'
        #    self.frame = 0
        #if xChange < 0 and self.direction == 'right':
        #elif command == 'left_down' and self.direction == 'right':
        #    self.direction = 'left'
        #    self.frame = self.numframes
        if command == 'right_down':
            self.rightkey = 1
        elif command == 'left_down':
            self.leftkey = 1
        elif command == 'right_up':
            self.rightkey = 0
        elif command == 'left_up':
            self.leftkey = 0


    def jump(self):
        Character.jump(self)

    def attack(self):
        if not self.isAttacking:
            self.isAttacking = 1
    def sparkle(self):
        if isinstance(Globals.State, Game.Game):
            if Globals.State.level == '3' or Globals.State.level == '4':
                if Globals.State.bossSpawned == 1:
                    self.isSparkling = 1
                    self.sparkleSoundPlayed = 0
        

