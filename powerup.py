import pygame
from random import *


class Powerups(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.image=pygame.image.load("assets/powerup.PNG").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect=self.image.get_rect()
        self.game = game
        infoObject = pygame.display.Info()
        self.screenh = int(infoObject.current_h)
        self.screenw = int(infoObject.current_w)
        self.rect.x=randrange(1,self.screenw)
        self.rect.y=self.y=randrange(self.screenh/2,self.screenh)






    def remove(self):
        self.game.allpowerup.remove(self)