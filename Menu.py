import State
import pygame.font
import Globals
import pygame.image
import pygame.event
import Highscore
import Game
import Cutscene
import Victory

class Menu(State.State):
    def __init__(self):
        self.alpha_image = pygame.image.load("Images/AlphaBlack.png").convert_alpha()
        self.screen_image = pygame.image.load("Images/MenuScreen.png").convert_alpha()
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsLullaby.ogg")
        self.musicplaying = False
        self.slider = MenuSlider()
        self.volume_slider = HeartSlider(304,199)
        self.brightness_slider = HeartSlider(304,257)

    def draw(self):
        Globals.Screen.blit(self.alpha_image, (0,0))
        Globals.Screen.blit(self.screen_image, (0,0))
        Globals.Screen.blit(self.slider.menu_slider, (self.slider.x,self.slider.y))
        Globals.Screen.blit(self.volume_slider.heart_slider, (self.volume_slider.x,self.volume_slider.y))
        Globals.Screen.blit(self.brightness_slider.heart_slider, (self.brightness_slider.x,self.brightness_slider.y))
        pygame.display.flip()
        
    def update(self):
        if not self.musicplaying:
            self.backgroundTrack.play(-1,0,0)
            self.backgroundTrack.set_volume(.1)
            self.musicplaying = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Globals.Running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Globals.Running = False
                elif event.key == pygame.K_RETURN:
                    if self.slider.position == 4:
                        Globals.Running = False
                    elif self.slider.position == 3:
                        self.backgroundTrack.stop()
                        Globals.State = Highscore.Highscore()
                    elif self.slider.position == 0:
                        #Globals.State = Game.Game()
                        self.backgroundTrack.stop()
                        Globals.State = Cutscene.Cutscene1()
                        #Globals.State = Game.Level3()
                        #Globals.State = Victory.Victory()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.slider.advance()
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.slider.retract()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                   if self.slider.position == 1:
			self.volume_slider.advance()
                   elif self.slider.position == 2:
                        self.brightness_slider.advance()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                   if self.slider.position == 1:
			self.volume_slider.retract()
                   elif self.slider.position == 2:
                        self.brightness_slider.retract()

class MenuSlider():
    def __init__(self):
        self.x = 62;
        self.y = 138;
        self.position = 0
        self.menu_slider = pygame.image.load("Images/MenuSlider.png").convert_alpha()
    def advance(self):
        if(self.position < 4):
            self.position += 1
            self.y += 60
        else:
            self.position = 0
            self.y = 138
    def retract(self):
        if(self.position > 0):
            self.position -= 1
            self.y -= 60
        else:
            self.position = 4
            self.y = 378

class HeartSlider():
    def __init__(self, x, y):
        self.x = x
        self.x_initial = x
        self.y = y
        self.position = 0
        self.heart_slider = pygame.image.load("Images/HeartSlider.png").convert_alpha()
    def advance(self):
        if(self.position < 5):
            self.position += 1
            self.x += 50
        #else:
           # self.position = 0
           # self.x = self.x_initial
    def retract(self):
        if(self.position > 0):
            self.position -= 1
            self.x -= 50
        #else:
        #    self.position = 5
        #    self.x = self.x_initial + 250
    


