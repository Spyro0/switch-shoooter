import pygame
from player import Player
from powerup import Powerups
from boss import Boss
class Game():
    def __init__(self,ecran):
        self.player=Player(self)
        self.boss=Boss(self)
        self.all_boss=pygame.sprite.Group()
        self.all_boss.add(self.boss)
        self.all_players=pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed={}
        self.allpowerup=pygame.sprite.Group()
        self.screen=ecran




    def powerupS(self):#apparition des powerup
        self.allpowerup.add(Powerups(self))


    def check_collision(self,sprite,group):#méthode pour les collisions
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

