import pygame
from blue_proj import White_proj

class Boss(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.health=15000
        self.max_health=15000
        self.image = pygame.image.load("assets/boss1.png").convert_alpha()  # import de l'image
        self.rect = self.image.get_rect()
        self.rect.x=450
        self.rect.y=-100
        self.game=game
        infoObject = pygame.display.Info()
        self.screenh = int(infoObject.current_h)
        self.screenw = int(infoObject.current_w)
        self.onscreen=0
        self.rect.x = int(self.screenw/2)-300
        self.rect.y = 0
        self.allproj=pygame.sprite.Group()


    def decrease_health(self,damage):
        self.health-=damage


    def kill(self):
        self.game.all_boss.remove(self)

    def shoot(self,x,y):
        self.allproj.add(White_proj(x,y,self.game))
