import pygame

class White_proj(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        super().__init__()
        self.image=pygame.image.load("assets/white_proj.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.damage=1
        self.state=1
        self.game=game

    def remove(self):
        self.game.boss.allproj.delete(self)