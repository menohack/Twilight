import pygame.image
import pygame.time
import pygame.event
import Globals
import State
import Player
import Enemy
import Highscore
import Menu
import Platform
import Camera
import random as R
import Trigger
import Victory
import Jock
import Projectile
import Hud
import Bambi
import Cutscene
import Gargoyle
import Cutscene
import os
if os.name == 'nt':
    print "Disabling Wiimote; you're using windows!"
else:
    import cwiid
import Wiimote

class Game(State.State):
    def __init__(self):
        pass

    def draw(self):
        self.camera.p = (int(self.camera.p[0]),int(self.camera.p[1])) 
        #Globals.Screen.blit(self.background, (-self.camera.p[0], -self.camera.p[1]))
        #print self.player.p
        Globals.Screen.blit(self.background.subsurface(self.camera.p, (Globals.xRes, Globals.yRes)), (0,0))
        for p in self.platforms:
            p.draw(self.camera)
        for s in self.nocollideplatforms:
            s.draw(self.camera)
        for e in self.enemies:
            e.draw(Globals.Screen, self.camera, Globals.Elapsed/1000.0)
        for j in self.jocks:
            j.draw(Globals.Screen, self.camera, Globals.Elapsed/1000.0)
        for a in self.projectiles:
            a.draw(Globals.Screen, self.camera, Globals.Elapsed/1000.0)
        for pw in self.powerups:
            pw.draw(Globals.Screen,self.camera)
        for g in self.gargs:
            g.draw(Globals.Screen,self.camera, Globals.Elapsed/1000.0)
        self.player.draw(Globals.Screen, self.camera, Globals.Elapsed/1000.0)
        #print self.player.p
        self.Hud.draw()
        #if Globals.Elapsed > 0:
        #    self.counter = Globals.Font.render("FPS: %1.0f" % (1000/Globals.Elapsed), True, (0,0,0))
    	#    Globals.Screen.blit(self.counter, (250, 24))
        pygame.display.flip();

        #if (self.player.p[0] == 0 or self.player.p[0] == Globals.xRes - self.player.image.get_width()-1) and self.borderState == False:
        #    self.borderSound.play()
        #    self.borderState = True
        #elif not (self.player.p[0] == 0 or self.player.p[0] == Globals.xRes - self.player.image.get_width()-1):
        #    self.borderState = False
	#    self.borderState = 1
        #if self.borderState == 1 and not (self.player.rect.topleft[0] <= 0 or self.player.rect.topleft[0] + self.player.image.get_width() >= Globals.xRes or self.player.rect.topleft[1] <= 0 or self.player.rect.topleft[1] + self.player.image.get_height() >= Globals.yRes):
	#    self.borderState = 0

    def update(self):
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        Globals.Lasttick = Globals.Curtick
        Globals.Curtick = pygame.time.get_ticks()
        Globals.Elapsed = Globals.Curtick - Globals.Lasttick
        for pw in self.powerups:
            pw.update(self.camera, Globals.Elapsed/1000.0)
        for e in self.enemies:
            e.update(self.camera, Globals.Elapsed/1000.0, self.platforms)
        for j in self.jocks:
            j.update(self.camera, Globals.Elapsed/1000.0, self.platforms)
        for p in self.projectiles:
            p.update(self.camera, Globals.Elapsed/1000.0, self.platforms)
        for g in self.gargs:
            g.update(self.camera, Globals.Elapsed/1000.0, self.platforms)
        self.player.update(self.camera, Globals.Elapsed/1000.0,self.platforms, self.enemies)
        for p in self.pits:
            if p.update(self.camera, self.player) == 1:
                Globals.State.backgroundTrack.stop()
                #Globals.State = Menu.Menu()
                #return
                Globals.State = Level1()
            for e in self.enemies:
                if p.update(self.camera, e) == 1:
                    self.enemies.remove(e)
                
        self.Hud.update(Globals.Elapsed/1000.0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Globals.Running = False
            elif event.type == pygame.KEYDOWN:
    	        if event.key == pygame.K_ESCAPE:
    	            Globals.State = Menu.Menu()
                    self.backgroundTrack.stop()
                #elif event.key == pygame.K_UP or event.key == pygame.K_w:
                #    self.player.jump()
                #elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #    self.player.move((0,1))
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    #self.player.move((140,0))
                    self.player.move('right_down')
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    #self.player.move((-140,0))
                    self.player.move('left_down')
                elif event.key == pygame.K_RETURN:
                    Globals.State = Highscore.Highscore()
                    self.backgroundTrack.stop()
                elif event.key == pygame.K_SPACE:
                    self.player.jump()
                elif event.key == pygame.K_s:
                    self.player.attack()
                elif event.key == pygame.K_x:
                    self.player.sparkle()
            elif event.type == pygame.KEYUP:
                #if event.key == pygame.K_UP or event.key == pygame.K_w:
                #    self.player.stop('y')
                #elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #    self.player.stop('y')
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    #self.player.move((0,0))
                    self.player.move('right_up')
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    #self.player.move((0,0))
                    self.player.move('left_up')
        if isinstance(Globals.Wiimote, Wiimote.Wiimote):
            print Globals.Wiimote.lastbutton
            self.wiimotestate = Globals.Wiimote.w.state
            if self.wiimotestate['acc'][cwiid.Z] > 180:
                self.player.jump()
            if self.wiimotestate['buttons'] == 4 or self.wiimotestate['buttons'] == 260 or self.wiimotestate['buttons'] == 516:
                self.player.attack()
                Globals.Wiimote.lastbutton = 4
            elif self.wiimotestate['buttons'] == 256 or self.wiimotestate['buttons'] == 260:
                self.player.move('left_down')
                Globals.Wiimote.lastbutton = 256
            elif self.wiimotestate['buttons'] == 512 or self.wiimotestate['buttons'] == 516:
                self.player.move('right_down')
                Globals.Wiimote.lastbutton = 512
            elif self.wiimotestate['buttons'] == 0:
                self.player.move('left_up')
                self.player.move('right_up')
                Globals.Wiimote.lastbutton = 0


    def loadLevel1(self, tiles):
        tiles.append(pygame.image.load("Images/blueposter_tile.png"))          #0
        tiles.append(pygame.image.load("Images/ceiling_tile.png"))             #1
        tiles.append(pygame.image.load("Images/clock_tile.png"))               #2
        tiles.append(pygame.image.load("Images/doorbottom_tile.png"))          #3 
        tiles.append(pygame.image.load("Images/doortop_tile.png"))             #4
        tiles.append(pygame.image.load("Images/floor-hole_tile.png"))          #5 
        tiles.append(pygame.image.load("Images/floor_tile1.png"))              #6
        tiles.append(pygame.image.load("Images/greenposter_tile.png"))         #7
        tiles.append(pygame.image.load("Images/leftbottomlocker_tile.png"))    #8
        tiles.append(pygame.image.load("Images/lefttoplocker_tile.png"))       #9
        tiles.append(pygame.image.load("Images/middlebottomlocker_tile.png"))  #10
        tiles.append(pygame.image.load("Images/middletoplocker_tile.png"))           #11
        tiles.append(pygame.image.load("Images/multipapers_tile.png"))         #12 
        tiles.append(pygame.image.load("Images/righttoplocker_tile.png"))      #13 
        tiles.append(pygame.image.load("Images/wall_tile copy.png"))           #14 
        tiles.append(pygame.image.load("Images/window_tile.png"))              #15 
        tiles.append(pygame.image.load("Images/bell_tile.png"))                #16
        

    def loadLevel2(self, tiles):
        tiles.append(pygame.image.load("Images/Level2/dirt1.png"))          #17
        tiles.append(pygame.image.load("Images/Level2/dirt2.png"))          #18
        tiles.append(pygame.image.load("Images/Level2/dirt3.png"))          #19
        tiles.append(pygame.image.load("Images/Level2/dirt-hole.png"))          #20


    def drawMap(self, level):
        tiles = []

        tiles.append(pygame.image.load("Images/blueposter_tile.png"))          #0
        tiles.append(pygame.image.load("Images/ceiling_tile.png"))             #1
        tiles.append(pygame.image.load("Images/clock_tile.png"))               #2
        tiles.append(pygame.image.load("Images/doorbottom_tile.png"))          #3 
        tiles.append(pygame.image.load("Images/doortop_tile.png"))             #4
        tiles.append(pygame.image.load("Images/floor-hole_tile.png"))          #5 
        tiles.append(pygame.image.load("Images/floor_tile1.png"))              #6
        tiles.append(pygame.image.load("Images/greenposter_tile.png"))         #7
        tiles.append(pygame.image.load("Images/leftbottomlocker_tile.png"))    #8
        tiles.append(pygame.image.load("Images/lefttoplocker_tile.png"))       #9
        tiles.append(pygame.image.load("Images/middlebottomlocker_tile.png"))  #10
        tiles.append(pygame.image.load("Images/middletoplocker_tile.png"))           #11
        #Hack-a-riffic!
        if (level == "4"):
            tiles.append(pygame.image.load("Images/Level4/redtile.png"))          #21
        else:
            #print "Not 4"
            tiles.append(pygame.image.load("Images/multipapers_tile.png"))         #12 
        tiles.append(pygame.image.load("Images/righttoplocker_tile.png"))      #13 
        tiles.append(pygame.image.load("Images/wall_tile copy.png"))           #14 
        tiles.append(pygame.image.load("Images/window_tile.png"))              #15 
        tiles.append(pygame.image.load("Images/bell_tile.png"))                #16
        tiles.append(pygame.image.load("Images/Level2/dirt1.png"))          #17
        tiles.append(pygame.image.load("Images/Level2/dirt2.png"))          #18
        tiles.append(pygame.image.load("Images/Level2/dirt3.png"))          #19
        tiles.append(pygame.image.load("Images/Level2/dirt-hole.png"))          #20
        #tiles.append(pygame.image.load("Images/Level2/dirt.png"))          #21


        if level == '1':
            infile = open('data/level1.txt','r')
        elif level == '2':
            infile = open('data/level2.txt', 'r')
        elif level == '3':
            infile = open('data/level3.txt', 'r')
        elif level == '4':
            infile = open('data/level4.txt', 'r')
        lines = infile.readlines()
        j = 0
        i = 0
        for l in lines:
            if l == "\n":
                break
            j = j + 1
        for t in lines[0]:
            i = i + 1
        self.level0 = pygame.surface.Surface((i*80 + 200 + 1000, j*80 + 200 + 1000))
        #self.level0 = pygame.surface.Surface((i*80 + 1000, j*80 + 1000))
        if level == '2':
            for x in range(9):
                self.level0.blit(self.backgroundimages[1], (640*x + 200,200 + 160))
                self.level0.blit(self.backgroundimages[0], (640*x + 200,200 + 480 + 160))
        elif level == '3':
            for x in range(11):
                y = 0
                while y < 5:
                    self.level0.blit(self.backgroundimages[1], (640*x + 200, 201 + y*480 + 160))
                    y = y + 1
                self.level0.blit(self.backgroundimages[0], (640*x + 200,201 + y*480 + 160))
        elif level == '4':
            for x in range(12):
                self.level0.blit(self.backgroundimages[1], (640*x + 200,200 + 160))
                self.level0.blit(self.backgroundimages[0], (640*x + 200,200 + 480 + 160))
                self.level0.blit(self.lava, (640*x + 200,200 + 480 + 160))
        y = 0
        for l in lines:
            if y == j - 1:
                break
            x = 0
            for t in lines[y]:
                if t != '\n':
                    if t == 'H':
                        self.platforms.append(Platform.Platform4((x*80 + 200, y*80 + 200)))
                        #self.platforms.append(Platform.Platform4((x*80, y*80)))
                    elif t == '1':
                        self.platforms.append(Platform.Platform5((x*80 + 200, y*80 + 200)))
                        #self.platforms.append(Platform.Platform5((x*80, y*80)))
                        #self.level0.blit(tiles[ord(t) - ord('0')], (x*80 + 200, y*80 + 200))
                    elif t == '6':
                        self.platforms.append(Platform.Platform7((x*80 + 200, y*80 + 200)))
                        #self.platforms.append(Platform.Platform7((x*80, y*80)))
                        #self.level0.blit(tiles[ord(t) - ord('0')], (x*80 + 200, y*80 + 200))
                    elif t == 'A':
                        self.platforms.append(Platform.Platform8((x*80 + 200, y*80 + 200)))
                        #self.platforms.append(Platform.Platform8((x*80, y*80)))
                    elif t == '3':
                        self.platforms.append(Platform.Platform9((x*80 + 200, y*80 + 200)))
                        #self.platforms.append(Platform.Platform9((x*80, y*80)))
                    elif t == '5':
                        self.pits.append(Trigger.Trigger1((x*80+200, y*80 + 200 + 40), (80, 40)))
                        #self.pits.append(Trigger.Trigger1((x*80, y*80 + 40), (80, 40)))
                        #self.platforms.append(Platform.Platform10((x*80 + 200, y*80 + 200)))
                        self.level0.blit(tiles[ord(t) - ord('0')], (x*80 + 200, y*80 + 200))
                        #self.level0.blit(tiles[ord(t) - ord('0')], (x*80, y*80))
                    elif t == '8':
                        self.platforms.append(Platform.Platform11((x*80 + 200, y*80 + 200)))
                        #self.platforms.append(Platform.Platform11((x*80, y*80)))
                    elif t == 'I':
                        self.platforms.append(Platform.Dirt1((x*80 + 200, y*80 + 200)))
                    elif t == 'J':
                        self.platforms.append(Platform.Dirt2((x*80 + 200, y*80 + 200)))
                    elif t == 'K':
                        self.platforms.append(Platform.Dirt3((x*80 + 200, y*80 + 200)))
                    elif t == 'Z':
                        pass
                    elif t == 'L':
                        self.platforms.append(Platform.Dirt0((x*80 + 200, y*80 + 200)))
                    elif ord(t) > ord('9'):
                        self.level0.blit(tiles[ord(t) - ord('A') + 10], (x*80 + 200, y*80 + 200))
                        #self.level0.blit(tiles[ord(t) - ord('A') + 10], (x*80, y*80))
                        #print ord(t) - ord('A')
                    else:
                        #if t == '6':
                        #    self.platforms.append(Platform.Platform5((x*80 + 200, y*80 + 200)))
                        #else:
                        #print str(t)
                        self.level0.blit(tiles[ord(t) - ord('0')], (x*80 + 200, y*80 + 200))
                        #self.level0.blit(tiles[ord(t) - ord('0')], (x*80, y*80))
                        #print ord(t) - ord('0')
                    x = x + 1
            y = y + 1

        for t in range(y+2,len(lines)):
            l = lines[t].split()
            if l[0] == 'h1':
                #self.platforms.append(Platform.Platform2((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Platform2((int(l[1]),int(l[2]))))
            elif l[0] == 'h2':
                #self.platforms.append(Platform.Platform14((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Platform14((int(l[1]),int(l[2]))))
            elif l[0] == 'h3':
                #self.platforms.append(Platform.Platform13((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Platform13((int(l[1]),int(l[2]))))
            elif l[0] == 't':
                #self.platforms.append(Platform.Platform1((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Platform1((int(l[1]),int(l[2]))))
            elif l[0] == 'p':
                #self.platforms.append(Platform.Platform3((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Platform3((int(l[1]),int(l[2]))))
            elif l[0] == 'r':
                #self.platforms.append(Platform.Rock((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Rock((int(l[1]),int(l[2]))))
            elif l[0] == 'tu':
                #self.platforms.append(Platform.Turtle((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Turtle((int(l[1]),int(l[2]))))
            elif l[0] == 'b1':
                #self.platforms.append(Platform.Branch1((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Branch1((int(l[1]),int(l[2]))))
            elif l[0] == 'b2':
                #self.platforms.append(Platform.Branch2((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.Branch2((int(l[1]),int(l[2]))))
            elif l[0] == 'tb':
                #self.platforms.append(Platform.TreeBottom((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.TreeBottom((int(l[1]),int(l[2]))))
            elif l[0] == 'tm':
                #self.platforms.append(Platform.TreeMiddle((int(l[1])+200,int(l[2])+200)))
                self.platforms.append(Platform.TreeMiddle((int(l[1]),int(l[2]))))
            elif l[0] == 'b':
		self.powerups.append(Bambi.Bambi((int(l[1]),int(l[2]))))
            elif l[0] == 'o1':
		self.platforms.append(Platform.OrangeBuilding1((int(l[1]),int(l[2]))))
            elif l[0] == 'o2':
		self.platforms.append(Platform.OrangeBuilding2((int(l[1]),int(l[2]))))
            elif l[0] == 'o3':
		self.platforms.append(Platform.OrangeBuilding3((int(l[1]),int(l[2]))))
            elif l[0] == 'g':
		self.platforms.append(Platform.Gargoyle((int(l[1]),int(l[2]))))
            elif l[0] == 'r1':
		self.platforms.append(Platform.RedBuilding1((int(l[1]),int(l[2]))))
            elif l[0] == 'r2':
		self.platforms.append(Platform.RedBuilding2((int(l[1]),int(l[2]))))
            elif l[0] == 'r3':
		self.platforms.append(Platform.RedBuilding3((int(l[1]),int(l[2]))))
            elif l[0] == 'y1':
		self.platforms.append(Platform.YellowBuilding1((int(l[1]),int(l[2]))))
            elif l[0] == 'y2':
		self.platforms.append(Platform.YellowBuilding2((int(l[1]),int(l[2]))))
            elif l[0] == 'y3':
		self.platforms.append(Platform.YellowBuilding3((int(l[1]),int(l[2]))))
            elif l[0] == 'y4':
		self.platforms.append(Platform.YellowBuilding4((int(l[1]),int(l[2]))))
            elif l[0] == 'y5':
		self.platforms.append(Platform.YellowBuilding5((int(l[1]),int(l[2]))))
            elif l[0] == 's3':
		self.platforms.append(Platform.Steeple3((int(l[1]),int(l[2]))))
            elif l[0] == 'box1':
		self.platforms.append(Platform.Box1((int(l[1]),int(l[2]))))
            elif l[0] == 'box2':
		self.platforms.append(Platform.Box2((int(l[1]),int(l[2]))))
            elif l[0] == 'box3':
		self.platforms.append(Platform.Box3((int(l[1]),int(l[2]))))
            elif l[0] == 'box4':
		self.platforms.append(Platform.Box4((int(l[1]),int(l[2]))))
            elif l[0] == 'flag':
		self.nocollideplatforms.append(Platform.Flag((int(l[1]),int(l[2]))))
            elif l[0] == 'mario':
		self.platforms.append(Platform.Mario((int(l[1]),int(l[2]))))
	    elif l[0] == '4m':
		self.platforms.append(Platform.Medplat((int(l[1]),int(l[2]))))
	    elif l[0] == '4l':
		self.platforms.append(Platform.Longplat((int(l[1]),int(l[2]))))
	    elif l[0] == '4p':
		self.platforms.append(Platform.Pipe((int(l[1]),int(l[2]))))

class Level1(Game):
    def __init__(self):
        self.player = Player.Player((338,1574))
        #self.player = Player.Player((3920,1466))
        #self.borderSound = pygame.mixer.Sound("boundaryCollision.wav")
        self.backgroundTrack = pygame.mixer.Sound("Sounds/Level1.wav")
        self.musicplaying = False
        Globals.Elapsed = 0
        Globals.Curtick = 0
        self.enemies = []
        self.jocks = []
        self.powerups = []
        self.platforms = []
        self.nocollideplatforms = []
        self.projectiles = []
        self.gargs = []
        #self.projectiles.append(Projectile.Projectile((500,1600),(0,0)))
        self.pits = []
        #self.numPlatforms = 7
        #self.borderState = False
        #self.numEnemies = 10
        self.camera = Camera.Camera((200,200))
        #self.camera = Camera.Camera((0,0))
        #self.background = pygame.image.load("Images/background-school-test.png")
        #self.remembertogetridofthis = 0
        self.level0 = None
        self.backgroundimages = []
        self.numBackgrounds = 0
        self.level = '1'
        self.drawMap(self.level)
        self.background = self.level0
        self.winTrigger = Trigger.Trigger1((4120,1566), (80, 80))

        self.Hud = Hud.Hud()
        #pygame.image.save(self.level0, "OHMYGOD.png")

	#self.enemies.append(Enemy.Boss((550,1474)))
        self.jocks.append(Jock.Jock((300,501)))
        self.jocks.append(Jock.Jock((1422,1550)))
        self.jocks.append(Jock.Jock((1882,598)))
        self.jocks.append(Jock.Jock((3464,598)))
        self.jocks.append(Jock.Jock((3020,1008)))
        self.jocks.append(Jock.Jock((3390,1520)))
        self.jocks.append(Jock.Jock((600,1604)))

        self.jocks.append(Jock.Jock((1140,655)))
        self.jocks.append(Jock.Jock((1180,655)))
        self.jocks.append(Jock.Jock((1220,655)))
        self.jocks.append(Jock.Jock((1350,655)))
        self.jocks.append(Jock.Jock((1400,655)))
        self.jocks.append(Jock.Jock((1500,655)))

        self.jocks.append(Jock.Jock((2000,655)))
        self.jocks.append(Jock.Jock((2200,655)))

        self.jocks.append(Jock.Jock((2490,655)))
        self.jocks.append(Jock.Jock((3000,655)))

        #Game.__init__(self)

    def draw(self):
        Game.draw(self)

    def update(self):
        if self.winTrigger.update(self.camera,self.player):
            self.backgroundTrack.stop()
            #Globals.State.level = '2'
            #Globals.State.drawMap('2')
            #Globals.State.background = Globals.State.level0
            #self.p = (400, 400)
            Globals.State = Cutscene.Cutscene2()
            return
            #Globals.State = Victory.Victory()
            
        if self.player.health <= 0:
            self.backgroundTrack.stop()
            #Globals.State = Menu.Menu()
            Globals.State = Level1()
        Game.update(self)

    #def drawMap(self, level):
    #    Game.drawMap(self)



class Level2(Game):
    def __init__(self):
        self.player = Player.Player((400,600))
        #self.player = Player.Player((4900, 500))
        #self.borderSound = pygame.mixer.Sound("boundaryCollision.wav")
        self.backgroundTrack = pygame.mixer.Sound("Sounds/Level2.wav")
        self.musicplaying = False
        Globals.Elapsed = 0
        Globals.Curtick = 0
        self.enemies = []
        self.platforms = []
        self.nocollideplatforms = []
        self.powerups = []
        self.projectiles = []
        self.pits = []
        self.jocks = []
        self.gargs = []
        #self.numPlatforms = 7
        #self.borderState = False
        #self.numEnemies = 10
        self.camera = Camera.Camera((200,200))
        #self.camera = Camera.Camera((0,0))
        #self.background = pygame.image.load("Images/background-school-test.png")
        #self.remembertogetridofthis = 0
        self.level0 = None
        self.backgroundimages = []
        self.backgroundimages.append(pygame.image.load("Images/Level2/level2-background1.png"))
        self.backgroundimages.append(pygame.image.load("Images/Level2/level2-background2.png"))
        self.numBackgrounds = 2
        self.level = '2'
        self.drawMap(self.level)
        #self.background = pygame.surface.Surface((i*80 + 200 + 1000, j*80 + 200 + 1000))
        self.background = self.level0
        self.winTrigger = Trigger.Trigger1((5180,252), (80, 580))
        self.bossBattle = False
        self.boss = None
        self.bossSpawned = False
        #pygame.image.save(self.level0, "Level2Printout.png")
        self.Hud = Hud.Hud()
        self.enemies.append(Enemy.Enemy((1990,880)))
        #self.enemies.append(Enemy.Enemy((400,400)))
        self.enemies.append(Enemy.Enemy((2914,1198)))
        self.enemies.append(Enemy.Enemy((3106,602)))
        self.enemies.append(Enemy.Enemy((1054,738)))
        #self.enemies.append(Enemy.Enemy((3390,1520)))

    def draw(self):
        Game.draw(self)

    def update(self):
        #dont forget to put back "and len(self.enemies) == 0"
        if self.winTrigger.update(self.camera,self.player) == 1 and self.bossBattle == False and len(self.enemies) == 0:
            self.bossBattle = True
            self.backgroundTrack.stop()
            #Globals.State.level = '2'
            #Globals.State.drawMap('2')
            #Globals.State.background = Globals.State.level0
            #self.p = (400, 400)
            #Globals.State = Victory.Victory()
            self.boss = Enemy.Boss((5580, 770))
            self.enemies.append(self.boss)
            self.bossSpawned = True
            self.bossTransition()
            self.backgroundTrack = pygame.mixer.Sound("Sounds/finalcountdown.ogg")
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.4)
            self.musicplaying = True
            
        if self.player.health <= 0:
            self.backgroundTrack.stop()
            #Globals.State = Menu.Menu()
            Globals.State = Level2()
        if self.bossBattle:
            turn = R.randint(0,200)
            if self.player.p[0] < self.camera.p[0]:
                self.player.p = (self.camera.p[0], self.player.p[1])
            elif self.player.p[0] + self.player.image.get_width() > self.camera.p[0] + Globals.xRes:
                self.player.p = (self.camera.p[0] + Globals.xRes - self.player.image.get_width(), self.player.p[1])
            if self.boss.p[0] < self.camera.p[0]:
                self.boss.p = (self.camera.p[0], self.boss.p[1])
                self.boss.direction = 'right'
                self.boss.rightkey = 1
                self.boss.leftkey = 0
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif self.boss.p[0] + self.boss.image.get_width() > self.camera.p[0] + Globals.xRes:
                self.boss.p = (self.camera.p[0] + Globals.xRes - self.boss.image.get_width(), self.boss.p[1])
                self.boss.direction = 'left'
                self.boss.rightkey = 0
                self.boss.leftkey = 1
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif (turn == 63 or self.boss.p[0] - self.player.p[0] <= -250) and self.boss.direction == 'left':
                self.boss.direction = 'right'
                self.boss.rightkey = 1
                self.boss.leftkey = 0
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif (turn == 122 or self.boss.p[0] - self.player.p[0] >= 250) and self.boss.direction == 'right':
                self.boss.direction = 'left'
                self.boss.rightkey = 0
                self.boss.leftkey = 1
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
        Game.update(self)

        if self.bossSpawned and len(self.enemies) == 0:
            Globals.State = Cutscene.Cutscene3()
            self.backgroundTrack.stop()

    def bossTransition(self):
        sliding = True
        self.camera.stopScrolling = True
        elapsed = 0
        #i = 0
        #self.camera.xScrolling = 'none'
        cameraStart = self.camera.p[0]
        cameraFinal = cameraStart + 400
        cameraFinalY = 504
        speed = 0.15
        ySpeed = 0.05
        while self.camera.p[0] < cameraFinal or self.camera.p[1] > cameraFinalY:
            #print "cameraX: " + str(self.camera.p[0]) + ", cameraFinal: " + str(cameraFinal)
            #print "camera.p: " + str(self.camera.p) + ", player.p: " + str(self.player.p)
            Globals.Lasttick = Globals.Curtick
            #pygame.time.wait(20)
            Globals.Curtick = pygame.time.get_ticks()
            Globals.Elapsed = Globals.Curtick - Globals.Lasttick
            elapsed += Globals.Elapsed
            #print "Globals.Elapsed: " + str(Globals.Elapsed) + ", elapsed " + str(elapsed) + ", Globals.Curtick " + str(Globals.Curtick) + ", Globals.Lasttick:" + str(Globals.Lasttick)
            #print "elapsed: " + str(elapsed)
            if elapsed > 20:
                #print "camera.p before: " + str(self.camera.p)
                self.camera.p = (self.camera.p[0] + elapsed * speed, self.camera.p[1])
                if self.camera.p[1] > cameraFinalY:
                    self.camera.p = (self.camera.p[0], self.camera.p[1] - elapsed * ySpeed)
                #print "camera.p: " + str(self.camera.p)
                self.camera.update(self.player.p, self.player.image.get_width(), self.player.image.get_height())
                self.draw()
                elapsed = 0
                #print "now"
                #i = i + 1
                #if i > 20:
                #    sliding = False


class Level3(Game):
    def __init__(self):
        self.player = Player.Player((300,2200))
        #self.player = Player.Player((550, 2900))
        #self.player = Player.Player((4100,2100))
        #testing spawn
        #self.player = Player.Player((6150,2271))
        #self.borderSound = pygame.mixer.Sound("boundaryCollision.wav")
        self.backgroundTrack = pygame.mixer.Sound("Sounds/Level2.wav")
        self.musicplaying = False
        Globals.Elapsed = 0
        Globals.Curtick = 0
        self.enemies = []
        self.platforms = []
        self.nocollideplatforms = []
        self.powerups = []
        self.projectiles = []
        self.pits = []
        self.jocks = []
        self.gargs = []
        self.gargs.append(Gargoyle.Gargoyle((500,3040)))
        self.gargs.append(Gargoyle.Gargoyle((1300,2950)))
        self.gargs.append(Gargoyle.Gargoyle((1900,2830)))
        self.gargs.append(Gargoyle.Gargoyle((2300,2795)))
        self.gargs.append(Gargoyle.Gargoyle((2900,2700)))
        self.gargs.append(Gargoyle.Gargoyle((3700,2480)))
        self.gargs.append(Gargoyle.Gargoyle((4300,2600)))
        self.gargs.append(Gargoyle.Gargoyle((4900,2800)))
        self.gargs.append(Gargoyle.Gargoyle((5500,3000)))
        #self.numPlatforms = 7
        #self.borderState = False
        #self.numEnemies = 10
        self.camera = Camera.Camera((200,200))
        #self.camera = Camera.Camera((0,0))
        #self.background = pygame.image.load("Images/background-school-test.png")
        #self.remembertogetridofthis = 0
        self.level0 = None
        self.backgroundimages = []
        self.backgroundimages.append(pygame.image.load("Images/Level3/italy-background1.png"))
        self.backgroundimages.append(pygame.image.load("Images/Level3/italy-background2test.png"))
        self.numBackgrounds = 2
        self.level = '3'
        self.drawMap(self.level)
        self.background = self.level0
        self.winTrigger = Trigger.Trigger1((6370,2871), (80, 580))
        self.deathTrigger = Trigger.Trigger1((1100,3230),(4350,80))
        self.bossBattle = False
        self.boss = None
        self.bossSpawned = False
        #pygame.image.save(self.level0, "Level3Printout.png")
        self.Hud = Hud.Hud()
        self.camera.bottomBorder =(0.85) *  Globals.yRes
        #self.enemies.append(Enemy.Enemy((1990,880)))
        #self.enemies.append(Enemy.Enemy((400,400)))
        #self.enemies.append(Enemy.Enemy((2914,1198)))
        #self.enemies.append(Enemy.Enemy((3106,602)))
        #self.enemies.append(Enemy.Enemy((1054,738)))
        #self.enemies.append(Enemy.Enemy((3390,1520)))

    def draw(self):
        Game.draw(self)

    def update(self):
        #dont forget to put back "and len(enemies) == 0"
        #if False:
        if self.winTrigger.update(self.camera,self.player) == 1 and self.bossBattle == False and len(self.enemies) == 0:
            self.bossBattle = True
            self.backgroundTrack.stop()
            #Globals.State.level = '2'
            #Globals.State.drawMap('2')
            #Globals.State.background = Globals.State.level0
            #self.p = (400, 400)
            #Globals.State = Victory.Victory()
            self.boss = Enemy.Boss((6780, 3160))
            self.enemies.append(self.boss)
            self.bossSpawned = True
            self.bossTransition()
            self.backgroundTrack = pygame.mixer.Sound("Sounds/finalcountdown.ogg")
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.4)
            self.musicplaying = True
            
        if self.player.health <= 0 or self.deathTrigger.update(self.camera,self.player) == 1:
            self.backgroundTrack.stop()
            #Globals.State = Menu.Menu()
            Globals.State = Level3()
        if self.bossBattle:
            turn = R.randint(0,150)
            if self.player.p[0] < self.camera.p[0]:
                self.player.p = (self.camera.p[0], self.player.p[1])
            elif self.player.p[0] + self.player.image.get_width() > self.camera.p[0] + Globals.xRes:
                self.player.p = (self.camera.p[0] + Globals.xRes - self.player.image.get_width(), self.player.p[1])
            if self.boss.p[0] < self.camera.p[0]:
                self.boss.p = (self.camera.p[0], self.boss.p[1])
                self.boss.direction = 'right'
                self.boss.rightkey = 1
                self.boss.leftkey = 0
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif self.boss.p[0] + self.boss.image.get_width() > self.camera.p[0] + Globals.xRes:
                self.boss.p = (self.camera.p[0] + Globals.xRes - self.boss.image.get_width(), self.boss.p[1])
                self.boss.direction = 'left'
                self.boss.rightkey = 0
                self.boss.leftkey = 1
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif (turn == 33 or self.boss.p[0] - self.player.p[0] <= -250) and self.boss.direction == 'left' and self.boss.jumping == False:
                self.boss.direction = 'right'
                self.boss.rightkey = 1
                self.boss.leftkey = 0
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif (turn == 83 or self.boss.p[0] - self.player.p[0] >= 250) and self.boss.direction == 'right' and self.boss.jumping == False:
                self.boss.direction = 'left'
                self.boss.rightkey = 0
                self.boss.leftkey = 1
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
        Game.update(self)

        if self.bossSpawned and len(self.enemies) == 0:
        #if self.winTrigger.update(self.camera,self.player) == 1:
            Globals.State = Cutscene.Cutscene4()
            self.backgroundTrack.stop()

    def bossTransition(self):
        sliding = True
        self.camera.stopScrolling = True
        elapsed = 0
        #i = 0
        #self.camera.xScrolling = 'none'
        cameraStart = self.camera.p[0]
        cameraFinal = cameraStart + 400
        cameraFinalY = 2800
        speed = 0.15
        ySpeed = 0.05
        while self.camera.p[0] < cameraFinal or self.camera.p[1] > cameraFinalY:
            #print "cameraX: " + str(self.camera.p[0]) + ", cameraFinal: " + str(cameraFinal)
            #print "camera.p: " + str(self.camera.p) + ", player.p: " + str(self.player.p)
            Globals.Lasttick = Globals.Curtick
            #pygame.time.wait(20)
            Globals.Curtick = pygame.time.get_ticks()
            Globals.Elapsed = Globals.Curtick - Globals.Lasttick
            elapsed += Globals.Elapsed
            #print "Globals.Elapsed: " + str(Globals.Elapsed) + ", elapsed " + str(elapsed) + ", Globals.Curtick " + str(Globals.Curtick) + ", Globals.Lasttick:" + str(Globals.Lasttick)
            #print "elapsed: " + str(elapsed)
            if elapsed > 20:
                #print "camera.p before: " + str(self.camera.p)
                self.camera.p = (self.camera.p[0] + elapsed * speed, self.camera.p[1])
                if self.camera.p[1] > cameraFinalY:
                    self.camera.p = (self.camera.p[0], self.camera.p[1] - elapsed * ySpeed)
                elif self.camera.p[1] < cameraFinalY:
                    self.camera.p = (self.camera.p[0], self.camera.p[1] + elapsed * ySpeed)
                #print "camera.p: " + str(self.camera.p)
                self.camera.update(self.player.p, self.player.image.get_width(), self.player.image.get_height())
                self.draw()
                elapsed = 0

class Level4(Game):
    def __init__(self):
        self.player = Player.Player((300,400))
        #self.player = Player.Player((550, 2900))
        #testing spawn
        #self.player = Player.Player((6100,300))
        #self.borderSound = pygame.mixer.Sound("boundaryCollision.wav")
        self.backgroundTrack = pygame.mixer.Sound("Sounds/Level4.ogg")
        self.musicplaying = False
        Globals.Elapsed = 0
        Globals.Curtick = 0
        self.enemies = []
        self.platforms = []
        self.nocollideplatforms = []
        self.powerups = []
        self.projectiles = []
        self.pits = []
        self.jocks = []
        self.gargs = []
        #self.numPlatforms = 7
        #self.borderState = False
        #self.numEnemies = 10
        self.camera = Camera.Camera((200,200))
        #self.camera = Camera.Camera((0,0))
        #self.background = pygame.image.load("Images/background-school-test.png")
        #self.remembertogetridofthis = 0
        self.level0 = None
        self.backgroundimages = []
        self.backgroundimages.append(pygame.image.load("Images/Level4/level4_background1.png"))
        self.backgroundimages.append(pygame.image.load("Images/Level4/level4_background2.png"))
        self.lava = pygame.image.load("Images/Level4/level4_lava.png").convert_alpha();
        self.numBackgrounds = 2
        self.level = '4'
        self.drawMap(self.level)
        self.background = self.level0
        self.winTrigger = Trigger.Trigger1((6500,200), (80, 1000))
        self.bossBattle = False
        self.boss = None
        self.bossSpawned = False
        #pygame.image.save(self.level0, "Level3Printout.png")
        self.Hud = Hud.Hud()
        self.camera.bottomBorder =(0.80) *  Globals.yRes
        self.gargs.append(Gargoyle.Gargoyle((1258,1087)))
        self.gargs.append(Gargoyle.Gargoyle((2409,959)))
        self.gargs.append(Gargoyle.Gargoyle((2671,1019)))
        self.gargs.append(Gargoyle.Gargoyle((1095,477)))
        self.gargs.append(Gargoyle.Gargoyle((3005,729)))
        self.gargs.append(Gargoyle.Gargoyle((3307,1080)))
        self.gargs.append(Gargoyle.Gargoyle((4964,1005)))
        self.gargs.append(Gargoyle.Gargoyle((5578,1157)))
        self.gargs.append(Gargoyle.Gargoyle((6057,410)))

    def draw(self):
        Game.draw(self)

    def update(self):
        #dont forget to put back "and len(enemies) == 0"
        #if False:
        if self.winTrigger.update(self.camera,self.player) == 1 and self.bossBattle == False and len(self.enemies) == 0:
            self.bossBattle = True
            self.backgroundTrack.stop()
            #Globals.State.level = '2'
            #Globals.State.drawMap('2')
            #Globals.State.background = Globals.State.level0
            #self.p = (400, 400)
            #Globals.State = Victory.Victory()
            self.boss = Enemy.Boss((6900, 820))
            self.enemies.append(self.boss)
            self.bossSpawned = True
            self.bossTransition()
            self.backgroundTrack = pygame.mixer.Sound("Sounds/finalcountdown.ogg")
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.4)
            self.musicplaying = True
            
        if self.player.health <= 0:
            self.backgroundTrack.stop()
            #Globals.State = Menu.Menu()
            Globals.State = Level4()
        if self.bossBattle:
            turn = R.randint(0,100)
            if self.player.p[0] < self.camera.p[0]:
                self.player.p = (self.camera.p[0], self.player.p[1])
            elif self.player.p[0] + self.player.image.get_width() > self.camera.p[0] + Globals.xRes:
                self.player.p = (self.camera.p[0] + Globals.xRes - self.player.image.get_width(), self.player.p[1])
            if self.boss.p[0] < self.camera.p[0]:
                self.boss.p = (self.camera.p[0], self.boss.p[1])
                self.boss.direction = 'right'
                self.boss.rightkey = 1
                self.boss.leftkey = 0
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif self.boss.p[0] + self.boss.image.get_width() > self.camera.p[0] + Globals.xRes:
                self.boss.p = (self.camera.p[0] + Globals.xRes - self.boss.image.get_width(), self.boss.p[1])
                self.boss.direction = 'left'
                self.boss.rightkey = 0
                self.boss.leftkey = 1
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif (turn == 1 or self.boss.p[0] - self.player.p[0] <= -250) and self.boss.direction == 'left' and self.boss.jumping == False:
                self.boss.direction = 'right'
                self.boss.rightkey = 1
                self.boss.leftkey = 0
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
            elif (turn == 99 or self.boss.p[0] - self.player.p[0] >= 250) and self.boss.direction == 'right' and self.boss.jumping == False:
                self.boss.direction = 'left'
                self.boss.rightkey = 0
                self.boss.leftkey = 1
                self.boss.v = (-self.boss.v[0], self.boss.v[1])
        Game.update(self)

        if self.bossSpawned and len(self.enemies) == 0:
        #if self.winTrigger.update(self.camera,self.player) == 1:
            Globals.State = Cutscene.Cutscene5()
            self.backgroundTrack.stop()

    def bossTransition(self):
        sliding = True
        self.camera.stopScrolling = True
        elapsed = 0
        #i = 0
        #self.camera.xScrolling = 'none'
        cameraStart = self.camera.p[0]
        cameraFinal = cameraStart + 400
        cameraFinalY = 504
        speed = 0.15
        ySpeed = 0.05
        while self.camera.p[0] < cameraFinal or self.camera.p[1] > cameraFinalY:
            #print "cameraX: " + str(self.camera.p[0]) + ", cameraFinal: " + str(cameraFinal)
            #print "camera.p: " + str(self.camera.p) + ", player.p: " + str(self.player.p)
            Globals.Lasttick = Globals.Curtick
            #pygame.time.wait(20)
            Globals.Curtick = pygame.time.get_ticks()
            Globals.Elapsed = Globals.Curtick - Globals.Lasttick
            elapsed += Globals.Elapsed
            #print "Globals.Elapsed: " + str(Globals.Elapsed) + ", elapsed " + str(elapsed) + ", Globals.Curtick " + str(Globals.Curtick) + ", Globals.Lasttick:" + str(Globals.Lasttick)
            #print "elapsed: " + str(elapsed)
            if elapsed > 20:
                #print "camera.p before: " + str(self.camera.p)
                self.camera.p = (self.camera.p[0] + elapsed * speed, self.camera.p[1])
                if self.camera.p[1] > cameraFinalY:
                    self.camera.p = (self.camera.p[0], self.camera.p[1] - elapsed * ySpeed)
                #print "camera.p: " + str(self.camera.p)
                self.camera.update(self.player.p, self.player.image.get_width(), self.player.image.get_height())
                self.draw()
                elapsed = 0
