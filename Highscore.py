import State
import pygame.font
import Globals
import pygame.image
import pygame.event
import Menu
import string

class Highscore(State.State):
    animationTime = 1.5
    def __init__(self):
        Globals.Font = pygame.font.Font(None,40)
        infile = open('highscores.txt','r')
        self.scores = infile.readlines()
        self.image = pygame.image.load("Images/BigRedHeart.png").convert()
        self.backgroundTrack = pygame.mixer.Sound("Sounds/EdwardsCurse.ogg")
        self.musicplaying = False
        self.counter = 0
        self.numscores = 8
    def draw(self):
        Globals.Screen.blit(self.image, (0,0))
        x = 0
        for s in self.scores[self.counter:]:
            s = string.replace(s, "\n","")
            if x < self.numscores:
                surf = Globals.Font.render(s,True,(0,0,0))
                Globals.Screen.blit(surf,(200,50+50*x))	
                x = x+1
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
                    Globals.State.backgroundTrack.stop()
                    Globals.State = Menu.Menu()
                elif event.key == pygame.K_DOWN:
                    if self.counter < 7:
                        self.counter = self.counter+1
                        self.draw()
                elif event.key == pygame.K_UP:
                    if self.counter > 0:
                        self.counter = self.counter-1
                        self.draw()
