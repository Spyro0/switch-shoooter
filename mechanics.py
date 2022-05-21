from projectile import Projectile
from proj2 import Projectile2
from proj3 import Projectile3
import threading
class MechanicsGP(object):

    def __init__(self, game):
        self.d_level = 1 # par défaut
        self.game = game

    def getLevel(self):
        return self.d_level

    def setLevel(self, level):
        if level in range(1, 4):
            self.d_level = level
        else:
            print('error, bad level')

    def setupMechanics(self):
        # On setup la vélocité du joueur et des projectiles selon le niveau
        # par défaut afin de contourner le problème de FPS --> tick rate %% >> 4
        if len(self.game.player.all_projectile) < 6 or len(self.game.player.all_projectile2) < 6 or len(self.game.player.all_projectile3) < 6:
            self.game.player.launch_projectile()  # méthode
            if self.d_level == 1:
                self.game.player.setSpeed(2)
                pC = Projectile(self.game.player).setSpeed(3)
                self.game.player.launch_projectile(pC)

            elif self.d_level == 2:
                self.game.player.setSpeed(3)
                pC = Projectile2(self.game.player).setSpeed(5)
                self.game.player.launch_projectile2(pC)

            elif self.d_level == 3:
                self.game.player.setSpeed(4)
                pC = Projectile3(self.game.player).setSpeed(10)
                self.game.player.launch_projectile3(pC)
                self.game.player.launch_projectile2(pC)

