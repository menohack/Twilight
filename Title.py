import pygame.image
import pygame.event
import pygame.time
import State
import Globals
import Game
import Menu

class Title(State.State):
    def __init__(self):
        #self.background = pygame.image.load("Title-underlay.png").convert()
        #self.foreground = pygame.image.load("Title-overlay.png").convert()
        self.background = pygame.image.load("Images/twi-titlescreen.png").convert()
        self.foreground = pygame.image.load("Images/twi-text2.png").convert()
        self.foreground.set_colorkey((0, 0, 0))
        self.fadetime = float(3500)
        Globals.Curtick = 0
        isloading = 1
        self.isReady = False
    def draw(self):
        Globals.Screen.blit(self.background, (0,0))
        #print Globals.Curtick
        if Globals.Curtick <= self.fadetime + 1000:
            if Globals.Curtick >= 1000:
                temp = self.foreground
                temp.set_alpha(int(((Globals.Curtick - 1000) / self.fadetime) * 255))
                #print int((Globals.Curtick / self.fadetime) * 255)
                Globals.Screen.blit(temp, (0,0))
                if self.isloading == 1:
                    self.loadingtext = Globals.Font.render("Loading", True, (255,255,255))
    	            Globals.Screen.blit(self.loadingtext, (280, 440))
        else:
            Globals.Screen.blit(self.foreground, (0,0))
#        temp = self.foreground
#        temp.set_alpha(20)
#        Globals.Screen.blit(temp, (0,0))
        pygame.display.flip()
    def update(self):
        Globals.Curtick = pygame.time.get_ticks()
        if Globals.Cutscenes == None:
            self.isloading = 1
            return
        elif Globals.Curtick >= 5000 or self.isReady:
            self.isloading = 0
            Globals.State = Menu.Menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Globals.Running = False
            elif event.type == pygame.KEYDOWN:
	        if event.key == pygame.K_ESCAPE:
	            Globals.Running = False
	        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.isReady = True
