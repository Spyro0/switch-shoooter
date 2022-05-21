import pygame
from projectile import Projectile
from proj2 import Projectile2
from proj3 import Projectile3

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health=1 #vie actuelle
        self.maxhealth=3 #vie max
        self.attack=5 #dégat par projectile
        self.speed=2 #vitesse de déplacement
        self.state=0 #état du switch (couleur)
        self.image=pygame.image.load("assets/red.png").convert_alpha() #import de l'image
        self.image=pygame.transform.scale(self.image,(60,50)) #mise aux dimension de l'image
        self.rect=self.image.get_rect()#hitbox
        self.rect.x=600#apparition en x
        self.rect.y=700#apparition en y
        self.all_projectile = pygame.sprite.Group()
        self.all_projectile2=pygame.sprite.Group()
        self.all_projectile3 = pygame.sprite.Group()
        self.proj=pygame.image.load("assets/projectile.png").convert_alpha()



#déplacements
    def up(self):

        self.rect.y-=self.speed

    def down(self):
        self.rect.y+=self.speed

    def right(self):

        self.rect.x+=self.speed

    def left(self):

        self.rect.x-=self.speed

    def up_right(self):
        self.rect.x+=(self.speed)/5
        self.rect.y-=(self.speed)/5

    def up_left(self):
        self.rect.x-=(self.speed)/5
        self.rect.y-=(self.speed)/5

    def down_right(self):
        self.rect.x+=(self.speed)/5
        self.rect.y+=(self.speed)/5

    def down_left(self):
        self.rect.x-=(self.speed)/5
        self.rect.y+=(self.speed)/5

    def switch(self):
        if self.state==0:
            self.image=pygame.image.load("assets/blue.png")
            self.image = pygame.transform.scale(self.image, (60, 50))
            self.state=1
        else:
            self.image = pygame.image.load("assets/red.png")
            self.image = pygame.transform.scale(self.image, (60, 50))
            self.state = 0
#lancements des projectiles
    def launch_projectile(self, p=None): #proj milieu
        if p == None:
            self.all_projectile.add(Projectile(self))
        else:
            if self.all_projectile_i < 5:
                self.all_projectile.add(p(self))

    def launch_projectile2(self,p = None):#proj droite
        if p == None:
            self.all_projectile2.add(Projectile2(self))
        else:
            if self.all_projectile2_i < 5:
                self.all_projectile2.add(p(self))

    def launch_projectile3(self,p = None):#proj gauche
        if p == None:
            self.all_projectile3.add(Projectile3(self))
        else:
            if self.all_projectile3_i < 5:
                self.all_projectile3.add(p(self))


    def upgrade(self):#fait monter la vie du joueur
        if self.health<3:
            self.health+=1

    def setSpeed(self, speed):
        self.speed = speed