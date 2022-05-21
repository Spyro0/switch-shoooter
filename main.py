import pygame


import mechanics
from game import Game
import threading

pygame.init()


#générer la fenêtre
pygame.display.set_caption("switch shooter")#titre
screen=pygame.display.set_mode((0,0))#dimensions

#variable de dimension d'écran
infoObject = pygame.display.Info()
screenh = int(infoObject.current_h)
screenw = int(infoObject.current_w)


#import du bg
background=pygame.image.load("assets/nebula.jpg")

#chargement du jeu
game=Game(screen)

# mechanics --> setup
mechanic = mechanics.MechanicsGP(game)

# clock speed
clock_speed = 120


#label vie boss
police = pygame.font.Font("freesansbold.ttf",20)

#icone vie joueur
icone=pygame.transform.scale(game.player.image,(50,40)) #mise aux dimension de l'image

#chargement du proj
image=pygame.image.load("assets/projectile.png")
#thread autoshoot
def async_perma_shoot():
    global a

    a = threading.Timer(0.50, async_perma_shoot)#timer de shoot
    a.start()#start du thread

    if game.player.health == 2:
        # tir lvl 2 : lag léger. on augmente la vélocité en la mettant au LV 2.
        mechanic.setLevel(2)
        mechanic.setupMechanics()
        # on update la vitesse de tick --> 180
        clock_speed = 300

    elif game.player.health==3:
        # tir lvl 3 : lag. on augmente la vélocité en la mettant au LV 3
        mechanic.setLevel(3) # va voir la classe tu peux ajuster :)
        mechanic.setupMechanics()
        # on update la vitesse de tick une fois de plus. --> 230
        clock_speed = 700
    elif game.player.health==1:
        # de base : pas de lag. on modifie rien mais on setup le tir.
        mechanic.setLevel(1)
        mechanic.setupMechanics()
        # vitesse de base
        clock_speed = 200

"""def p_move():
    global b
    b = threading.Timer(0.03, p_move)  # timer de shoot
    b.start()  # start du thread
    # récup projectile du joueur
    for projectile in game.player.all_projectile:
        projectile.move()
    for projectile in game.player.all_projectile2:
        projectile.move()
    for projectile in game.player.all_projectile3:
        projectile.move()"""

a = async_perma_shoot()
#b = p_move()

def async_spawn_p():#gère l'apparition de powerup
    global p
    p = threading.Timer(2, async_spawn_p)
    p.start()
    game.powerupS()

p = async_spawn_p()

# a --> c --> e
global clock
i=0
#boucle d'ouverture

running = True
clock = pygame.time.Clock()
while running:
    # appliquer le background
    clock.tick(clock_speed)

    screen.blit(background, (0, 0))
    while i<1:
        game.boss.shoot(500,500)
        for proj in game.boss.allproj:
            screen.blit(proj.image,proj.rect)
            print(proj.rect)
            i+=1


    #affichage du joueur
    screen.blit(game.player.image,game.player.rect)
    for boss in game.all_boss:
        screen.blit(boss.image, boss.rect)


    # point de vies boss affichage
    vie = str(game.boss.health)
    pdv_boss = police.render("Vie du boss : "+vie, False, (255, 255, 255))
    screen.blit(pdv_boss, ( 50,  50))

    #vie joueur
    if game.player.health==1:
        screen.blit(icone,(50,90))
    elif game.player.health==2:
        screen.blit(icone, (50, 90))
        screen.blit(icone, (120, 90))
    elif game.player.health==3:
        screen.blit(icone, (50, 90))
        screen.blit(icone, (120, 90))
        screen.blit(icone, (190, 90))



    #s = pygame.display.get_surface()
    #for hit in game.boss.hit_group:
        #s.fill("red", hit)


    # appliquer l'ensemble des projectiles et des images
    game.player.all_projectile.draw(screen)
    game.player.all_projectile2.draw(screen)
    game.player.all_projectile3.draw(screen)
    game.allpowerup.draw(screen)
    for projectile in game.player.all_projectile:
        projectile.move()
    for projectile in game.player.all_projectile2:
        projectile.move()
    for projectile in game.player.all_projectile3:
        projectile.move()



    #vérifie la collision entre le powerup et le joueur
    for item in game.allpowerup:
        if game.check_collision(item,game.all_players):
            game.player.upgrade()
            item.remove()

    #vérifie les collisions entre le boss et les projectiles
    for item in game.player.all_projectile:
        if game.check_collision(item,game.all_boss):
            game.boss.decrease_health(item.damage)
            item.kill()
            item.remove()
            game.player.all_projectile.update()
            game.player.all_projectile.clear(screen, background)
            game.player.all_projectile.draw(screen)

    for item in game.player.all_projectile2:
        if game.check_collision(item,game.all_boss):
            game.boss.decrease_health(item.damage)
            item.kill()
            item.remove()
            game.player.all_projectile2.update()
            game.player.all_projectile2.clear(screen, background)
            game.player.all_projectile2.draw(screen)

    for item in game.player.all_projectile3:
        if game.check_collision(item,game.all_boss):
            game.boss.decrease_health(item.damage)
            item.kill()
            item.remove()
            game.player.all_projectile3.update()
            game.player.all_projectile3.clear(screen, background)
            game.player.all_projectile3.draw(screen)


    for boss in game.all_boss:
        for item in boss.allproj:
            if game.check_collision(item,game.all_players):
                if item.state==1 and game.player.state==0:
                    game.player.health-=1
                    item.kill()

    if game.boss.health<=0:
        game.boss.kill()
    #vérif déplacement
    if game.pressed.get(pygame.K_RIGHT)and game.player.rect.x+game.player.rect.width<screen.get_width():
        game.player.right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.left()
    if game.pressed.get(pygame.K_UP) and game.player.rect.y>0:
        game.player.up()
    if game.pressed.get(pygame.K_DOWN)and game.player.rect.y+game.player.rect.height<screen.get_height():
        game.player.down()
    if game.pressed.get(pygame.K_UP) and game.pressed.get(pygame.K_RIGHT) and game.player.rect.x+game.player.rect.width<screen.get_width() and game.player.rect.y>0:
        game.player.up_right()
    if game.pressed.get(pygame.K_UP) and game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0 and game.player.rect.y>0:
        game.player.up_left()
    if game.pressed.get(pygame.K_DOWN) and game.pressed.get(pygame.K_RIGHT) and game.player.rect.y+game.player.rect.height<screen.get_height() and game.player.rect.x+game.player.rect.width<screen.get_width():
        game.player.down_right()
    if game.pressed.get(pygame.K_DOWN) and game.pressed.get(pygame.K_LEFT) and game.player.rect.y+game.player.rect.height<screen.get_height() and game.player.rect.x>0:
        game.player.down_left()



    #mise a jour de l'écran
    pygame.display.flip()

    for event in pygame.event.get():#fermeture de la fenêtre
        # que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            a.cancel()#ferme le thread a la fermeture de la fenêtre
             #b.cancel()#fin des projectiles
            if p is not None:
                try:
                    p.cancel()
                except:
                    print("Le Thread n'est pas fonctionnel.")
            else:
                p.cancel()
        #détecter si un joueur lache une touche du clavier
        elif event.type==pygame.KEYDOWN:
            game.pressed[event.key]=True
            if event.key==pygame.K_SPACE:
                game.player.switch()
            if event.key==pygame.K_e:
                game.player.shoot()
        elif event.type==pygame.KEYUP:
            game.pressed[event.key]=False



