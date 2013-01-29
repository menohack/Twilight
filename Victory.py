import State
import pygame.font
import Globals
import pygame.image
import pygame.event
import Menu
import string
import Highscore

class Victory(State.State):
    animationTime = 1.5
    def __init__(self):
        Globals.Font = pygame.font.Font(None,40)
        self.image = pygame.image.load("Images/Highscores.png").convert()
        #self.backgroundTrack = pygame.mixer.Sound("Sounds/badromance.ogg")
        #self.musicplaying = False
    def draw(self):
        Globals.Screen.blit(self.image, (0,0))
        surf = Globals.Font.render("CONGRATULATIONS!", True,(255,255,255))
        Globals.Screen.blit(surf,(150,200))
        pygame.display.flip()
    def update(self):
        #if not self.musicplaying:
        #    self.backgroundTrack.play(-1,0,0)
        #    self.backgroundTrack.set_volume(.1)
        #    self.musicplaying = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Globals.Running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #self.backgroundTrack.stop()
                    Globals.State = Menu.Menu()
                elif event.key == pygame.K_RETURN:
                    #self.backgroundTrack.stop()
                    Globals.State = Highscore.Highscore()
                
