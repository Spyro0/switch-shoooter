import pygame


#classe projectile

class Projectile3(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.speed=8
        self.player=player
        self.image=self.player.proj
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect=self.image.get_rect()
        self.rect.x=player.rect.x
        self.rect.y=player.rect.y-50
        self.origin_image=self.image
        self.angle=0
        self.damage = 10

    def move(self):
        self.rect.y-=self.speed
        # vérif si le projectile est sur l'écran
        if self.rect.y < 100:
            # supprimer
            self.remove()

    def remove(self):
        self.player.all_projectile3.remove(self)

    def setSpeed(self, speed):
        self.speed = speed