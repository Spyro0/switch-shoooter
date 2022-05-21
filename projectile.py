import pygame

#classe projectile

class Projectile(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.speed=8#vitesse projectile
        self.player=player #import du joueur
        self.image=self.player.proj#image du projectile
        self.image=pygame.transform.scale(self.image,(20,20))#mise a l'échelle de l'échelle
        self.rect=self.image.get_rect() #récup de la hitbox
        self.rect.x=player.rect.x+20 #apparition en x(par rapport au joueur)
        self.rect.y=player.rect.y-50 #apparition en y
        self.damage=10
        self.origin_image=self.image #image d'origine
        self.angle=0

    def move(self): #déplace le projectile vers le haut
        self.rect.y-=self.speed
        # vérif si le projectile est sur l'écranv
        if self.rect.y < 100:
            # supprimer
            self.remove()

    def remove(self): #supprime le projectile
        self.player.all_projectile.remove(self)

    def setSpeed(self, speed):
        self.speed = speed
