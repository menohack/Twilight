import pygame
import pygame.image
import Globals

class Camera():
    def __init__(self, (xStart, yStart)):
        #the position of the top-left corner of the screen on the world
        self.p = (xStart, yStart)
        #Edward's position in world coordinates
        self.edwardWorld = (0, 0)
        #Edward's position in camera coordinates
        self.edwardScreen = (0, 0)
        #the direction we are scrolling
        self.xScrolling = 'none'
        self.yScrolling = 'none'
        #the pixel values at which scrolling occurs
        self.rightBorder = (0.75) * Globals.xRes
        self.leftBorder = (0.25) * Globals.xRes
        self.topBorder = (0.1) * Globals.yRes
        self.bottomBorder =(0.95) *  Globals.yRes
        self.stopScrolling = False

    def update(self, (edwardX, edwardY), edwardWidth, edwardHeight):
        self.edwardWorld = (edwardX, edwardY)
        self.edwardScreen = (edwardX - self.p[0], edwardY - self.p[1])
        #scroll right
        tempright = self.edwardScreen[0] + edwardWidth - self.rightBorder
        templeft = self.edwardScreen[0] - self.leftBorder
        if tempright > 0 and not self.stopScrolling:
            self.p = (self.p[0] + tempright, self.p[1])
            self.xScrolling = 'right'
        #scroll left
        elif templeft < 0 and not self.stopScrolling:
            self.p = (self.p[0] + templeft, self.p[1])
            self.xScrolling = 'left'
        #not scrolling horizontally
        else:
            self.xScrolling = 'none'
       
        tempdown = self.edwardScreen[1] + edwardHeight - self.bottomBorder
        tempup = self.edwardScreen[1] - self.topBorder
        #scroll down
        if tempdown > 0 and not self.stopScrolling:
            self.p = (self.p[0], self.p[1] + tempdown)
            self.yScrolling = 'down'
        #scroll up
        elif tempup < 0 and not self.stopScrolling:
            self.p = (self.p[0], self.p[1] + tempup)
            self.yScrolling = 'up'
        #not scrolling vertically
        else:
            self.yScrolling = 'none'
