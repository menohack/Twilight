import pygame
import pygame.image
import pygame.sprite
import Globals
import Game
import State
import Victory
import Cutscene

class Cutscenes(State.State):

    def __init__(self):
        self.scene1 = Cutscene.Cutscene1()
        self.scene2 = Cutscene.Cutscene2()
        self.scene3 = Cutscene.Cutscene3()
        self.scene4 = Cutscene.Cutscene4()
        self.scene5 = Cutscene.Cutscene5()

            
        
