import pygame
import pygame.image
import pygame.sprite
import Globals

class Platform1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Images/table.png").convert_alpha()
        self.rect = self.image.get_rect()
        #self.image.set_colorkey((3, 254, 62))
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn


class Platform12(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Light-bottom-test.png").convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((3, 254, 62))
        self.rect.topleft = (xSpawn,ySpawn + 32)
        self.image2 = pygame.image.load("Images/Light-top-test.png").convert()
        self.rect2 = self.image.get_rect()
        self.image2.set_colorkey((3, 254, 62))
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn


class Platform3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Images/people.png").convert_alpha()
        self.rect = self.image.get_rect()
        #self.image.set_colorkey((3, 254, 62))
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn


class Platform4(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Images/black_tile.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn


class Platform5(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/ceiling_tile_top.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
        self.image2 = pygame.image.load("Images/ceiling_tile_bottom.png").convert()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn + 39)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn


class Platform6(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("Images/SideBorder.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform7(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/floor_tile_bottom.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 38)
        self.image2 = pygame.image.load("Images/floor_tile_top.png").convert()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform8(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/middlebottomlocker_tile_bottom.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 38)
        self.image2 = pygame.image.load("Images/middlebottomlocker_tile_top.png").convert()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform9(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/doorbottom_tile_bottom.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 38)
        self.image2 = pygame.image.load("Images/doorbottom_tile_top.png").convert()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

#class Platform10(Trigger.Trigger):
#    def __init__(self, (xSpawn,ySpawn)):
#        self.image = pygame.image.load("Images/floor-hole_tile_bottom.png").convert()
#        self.rect = self.image.get_rect()
#        Trigger.__init__(self, self.rect.topleft, (self.image.get_width(), self.image.get_height()))
#        self.rect.topleft = (xSpawn,ySpawn + 38)
#        self.image2 = pygame.image.load("Images/floor-hole_tile_top.png").convert()
#        self.rect2 = self.image.get_rect()
#        self.rect2.topleft = (xSpawn, ySpawn)
#    def draw(self, camera):
#        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
#        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
#    def update(self, camera):
#        Trigger.update(self, camera, Globals.Player)
#        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform11(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/leftbottomlocker_tile_bottom.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 38)
        self.image2 = pygame.image.load("Images/leftbottomlocker_tile_top.png").convert()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/hanging_light_bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn + 4,ySpawn + 90)
        self.image2 = pygame.image.load("Images/hanging_light_top5.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform13(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/hanging_light_bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn + 4,ySpawn + 175)
        self.image2 = pygame.image.load("Images/hanging_light_top6.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Platform14(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/hanging_light_bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn + 4,ySpawn + 140)
        self.image2 = pygame.image.load("Images/hanging_light_top4.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Dirt0(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/dirt.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Dirt1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/dirt-bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 40)
        self.image2 = pygame.image.load("Images/Level2/dirt1-top.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Dirt2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/dirt-bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 40)
        self.image2 = pygame.image.load("Images/Level2/dirt2-top.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Dirt3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/dirt-bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn + 40)
        self.image2 = pygame.image.load("Images/Level2/dirt3-top.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class TreeBottom(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/tree-bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class TreeMiddle(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/tree-middle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Rock(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/rock.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Turtle(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/turtle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Branch1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/branch1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Branch2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level2/branch2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn,ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class OrangeBuilding1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/orange-building1electricboogaloo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
        #self.image2 = pygame.image.load("Images/hanging_light_top5.png").convert_alpha()
        #self.rect2 = self.image.get_rect()
        #self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        #Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class OrangeBuilding2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/orange-building2electricboogaloo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class OrangeBuilding3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/orange-building3electricboogaloo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Gargoyle(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/gargoyle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class RedBuilding1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/red-building1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class RedBuilding2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/red-building2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class RedBuilding3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/red-building3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class YellowBuilding1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/yellow-building1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class YellowBuilding2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/yellow-building2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class YellowBuilding3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/yellow-building3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class YellowBuilding4(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/yellow-building4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class YellowBuilding5(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/yellow-building5.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Steeple3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/steeple3-bottom.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn + 165)
        self.image2 = pygame.image.load("Images/Level3/steeple3-top.png").convert_alpha()
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
        Globals.Screen.blit(self.image2, (self.rect2.topleft[0] - camera.p[0], self.rect2.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Box1(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/box1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn + 251 - 69)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Box2(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/box2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn + 58, ySpawn + 251 - 69 - 67 + 1)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Box3(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/box3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn + 116 , ySpawn + 251 - 69 - 67 - 59 + 2)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Box4(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/box4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn + 167, ySpawn + 251 - 69 - 67 - 59 - 56 + 2)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Flag(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/flag.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Mario(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level3/mariosmall.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Medplat(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level4/level4_medplat.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Longplat(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level4/level4_longplat.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn

class Pipe(pygame.sprite.Sprite):
    def __init__(self, (xSpawn,ySpawn)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Level4/level4_pipeplat.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (xSpawn, ySpawn)
    def draw(self, camera):
        Globals.Screen.blit(self.image, (self.rect.topleft[0] - camera.p[0], self.rect.topleft[1] - camera.p[1]))
    def update(self, camera):
        self.rect.topleft = (xSpawn, ySpawn) #unnecessary filler code for fxn
