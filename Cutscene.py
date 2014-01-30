import pygame
import pygame.image
import pygame.sprite
import Globals
import Game
import State
import Victory
import Menu

class Cutscene(State.State):

    def init(self):
        self.elapsed = 0   #the elapsed time since frame was changed
        self.FRAMES = []
        self.FRAMES.append(pygame.image.load("Images/Cutscene1/1small.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene1/2.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene1/3.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene1/4.png").convert())
        self.black = pygame.image.load("Images/AlphaBlack.png").convert_alpha()
        self.image = self.FRAMES[0]
        self.frametimes = []
        self.frametimes.append(5)
        self.frametimes.append(3)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.framecounter = 0
        self.frametime = self.frametimes[0]
        self.numframes = 4
        Globals.Elapsed = 0
        Globals.Curtick = pygame.time.get_ticks()
        Globals.Lasttick = 0
        self.fadetime = float(1000)
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsCurse.ogg")
        self.musicplaying = False
        


    def draw(self):
        Globals.Screen.blit(self.black, (0,0))
        Globals.Screen.blit(self.image, (0,0))             
        pygame.display.flip()
        
    def update(self):
        Globals.Lasttick = Globals.Curtick
        Globals.Curtick = pygame.time.get_ticks()
        self.elapsed += Globals.Curtick - Globals.Lasttick
        if self.elapsed < 1000:
            #print int((self.elapsed / self.fadetime) * 255)
            self.image.set_alpha(int((self.elapsed / self.fadetime) * 255))
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        

        if self.elapsed / 1000 > self.frametime:
            self.elapsed = 0
            if self.framecounter == self.numframes - 1:
                Globals.State.backgroundTrack.stop()
                Globals.State = Game.Level1()
            else:
                self.framecounter += 1
                #print self.framecounter
                self.image = self.FRAMES[self.framecounter]
                self.frametime = self.frametimes[self.framecounter]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Globals.Running = False
            elif event.type == pygame.KEYDOWN:
    	        if event.key == pygame.K_ESCAPE:
    	            Globals.State = Menu.Menu()
                    self.backgroundTrack.stop()
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    Globals.State = self.nextLevel
                    self.backgroundTrack.stop()

class Cutscene1(Cutscene):
    def __init__(self):
        self.init()
        self.nextLevel = Game.Level1()

class Cutscene2(State.State):

    def __init__(self):
        self.elapsed = 0   #the elapsed time since frame was changed
        self.FRAMES = []
        self.FRAMES.append(pygame.image.load("Images/Cutscene2/1.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene2/2.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene2/3.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene2/4.png").convert())
        self.black = pygame.image.load("Images/AlphaBlack.png").convert_alpha()
        self.image = self.FRAMES[0]
        self.frametimes = []
        self.frametimes.append(5)
        self.frametimes.append(3)
        self.frametimes.append(3)
        self.frametimes.append(2)
        self.framecounter = 0
        self.frametime = self.frametimes[0]
        self.numframes = 4
        Globals.Elapsed = 0
        Globals.Curtick = pygame.time.get_ticks()
        Globals.Lasttick = 0
        self.fadetime = float(1000)
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsCurse.ogg")
        self.musicplaying = False
        


    def draw(self):
        Globals.Screen.blit(self.black, (0,0))
        Globals.Screen.blit(self.image, (0,0))             
        pygame.display.flip()
        
    def update(self):
        Globals.Lasttick = Globals.Curtick
        Globals.Curtick = pygame.time.get_ticks()
        self.elapsed += Globals.Curtick - Globals.Lasttick
        if self.elapsed < 1000:
            #print int((self.elapsed / self.fadetime) * 255)
            self.image.set_alpha(int((self.elapsed / self.fadetime) * 255))
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        

        if self.elapsed / 1000 > self.frametime:
            self.elapsed = 0
            if self.framecounter == self.numframes - 1:
                Globals.State.backgroundTrack.stop()
                Globals.State = Game.Level2()
            else:
                self.framecounter += 1
                #print self.framecounter
                self.image = self.FRAMES[self.framecounter]
                self.frametime = self.frametimes[self.framecounter]
class Cutscene3(State.State):

    def __init__(self):
        self.elapsed = 0   #the elapsed time since frame was changed
        self.FRAMES = []
        self.numframes = 8
        #for i in range(1,self.numframes):
            #self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-"+ str(i) + ".png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-1.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-2.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-3.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-4.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-5.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-6.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-7.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene3/scene3-8.png").convert())
        self.black = pygame.image.load("Images/AlphaBlack.png").convert_alpha()
        self.image = self.FRAMES[0]
        self.frametimes = []
        self.frametimes.append(5)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(3)
        self.frametimes.append(3)
        self.frametimes.append(2)
        self.frametimes.append(6)
        self.framecounter = 0
        self.frametime = self.frametimes[0]
        Globals.Elapsed = 0
        Globals.Curtick = pygame.time.get_ticks()
        Globals.Lasttick = 0
        self.fadetime = float(1000)
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsCurse.ogg")
        self.musicplaying = False
        


    def draw(self):
        Globals.Screen.blit(self.black, (0,0))
        Globals.Screen.blit(self.image, (0,0))             
        pygame.display.flip()
        
    def update(self):
        Globals.Lasttick = Globals.Curtick
        Globals.Curtick = pygame.time.get_ticks()
        self.elapsed += Globals.Curtick - Globals.Lasttick
        if self.elapsed < 1000:
            #print int((self.elapsed / self.fadetime) * 255)
            self.image.set_alpha(int((self.elapsed / self.fadetime) * 255))
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        

        if self.elapsed / 1000 > self.frametime:
            self.elapsed = 0
            if self.framecounter == self.numframes - 1:
                Globals.State.backgroundTrack.stop()
                Globals.State = Game.Level3()
            else:
                self.framecounter += 1
                #print self.framecounter
                self.image = self.FRAMES[self.framecounter]
                self.frametime = self.frametimes[self.framecounter]
class Cutscene4(State.State):

    def __init__(self):
        self.elapsed = 0   #the elapsed time since frame was changed
        self.FRAMES = []
        self.FRAMES.append(pygame.image.load("Images/Cutscene4/scene4-1.jpg").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene4/scene4-2.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene4/scene4-3.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene4/scene4-4.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene4/scene4-5.png").convert())
        self.black = pygame.image.load("Images/AlphaBlack.png").convert_alpha()
        self.image = self.FRAMES[0]
        self.frametimes = []
        self.frametimes.append(5)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(3)
        self.frametimes.append(2)
        self.framecounter = 0
        self.frametime = self.frametimes[0]
        self.numframes = 5
        Globals.Elapsed = 0
        Globals.Curtick = pygame.time.get_ticks()
        Globals.Lasttick = 0
        self.fadetime = float(1000)
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsCurse.ogg")
        self.musicplaying = False
        


    def draw(self):
        Globals.Screen.blit(self.black, (0,0))
        Globals.Screen.blit(self.image, (0,0))             
        pygame.display.flip()
        
    def update(self):
        Globals.Lasttick = Globals.Curtick
        Globals.Curtick = pygame.time.get_ticks()
        self.elapsed += Globals.Curtick - Globals.Lasttick
        #if self.elapsed < 1000:
            #print int((self.elapsed / self.fadetime) * 255)
            #self.image.set_alpha(int((self.elapsed / self.fadetime) * 255))
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        

        if self.elapsed / 1000 > self.frametime:
            self.elapsed = 0
            if self.framecounter == self.numframes - 1:
                Globals.State.backgroundTrack.stop()
                Globals.State = Game.Level4()
            else:
                self.framecounter += 1
                #print self.framecounter
                self.image = self.FRAMES[self.framecounter]
                self.frametime = self.frametimes[self.framecounter]
class Cutscene5(State.State):

    def __init__(self):
        self.elapsed = 0   #the elapsed time since frame was changed
        self.FRAMES = []
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-1.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-2.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-3.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-4.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-5.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-6.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-7.png").convert())
        self.FRAMES.append(pygame.image.load("Images/Cutscene5/scene5-8.png").convert())
        self.black = pygame.image.load("Images/AlphaBlack.png").convert_alpha()
        self.image = self.FRAMES[0]
        self.frametimes = []
        self.frametimes.append(5)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(2)
        self.frametimes.append(1)
        self.frametimes.append(2)
        self.framecounter = 0
        self.frametime = self.frametimes[0]
        self.numframes = 8
        Globals.Elapsed = 0
        Globals.Curtick = pygame.time.get_ticks()
        Globals.Lasttick = 0
        self.fadetime = float(1000)
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsCurse.ogg")
        self.musicplaying = False
        


    def draw(self):
        Globals.Screen.blit(self.black, (0,0))
        Globals.Screen.blit(self.image, (0,0))             
        pygame.display.flip()
        
    def update(self):
        Globals.Lasttick = Globals.Curtick
        Globals.Curtick = pygame.time.get_ticks()
        self.elapsed += Globals.Curtick - Globals.Lasttick
        if self.elapsed < 1000:
            #print int((self.elapsed / self.fadetime) * 255)
            self.image.set_alpha(int((self.elapsed / self.fadetime) * 255))
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        

        if self.elapsed / 1000 > self.frametime:
            self.elapsed = 0
            if self.framecounter == self.numframes - 1:
                Globals.State.backgroundTrack.stop()
                Globals.State = Victory.Victory()
            else:
                self.framecounter += 1
                #print self.framecounter
                self.image = self.FRAMES[self.framecounter]
                self.frametime = self.frametimes[self.framecounter]
            
        
