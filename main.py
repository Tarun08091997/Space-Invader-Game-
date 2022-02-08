import pygame
import random
import pygame_gui
from player import player
from enemy import *
from bullet import *
import math
from pygame.tests.draw_test import GREEN
from pygame.tests.draw_test import RED
from pygame.locals import *
#initialize the pygame
pygame.init()


#Title and Icon use 32*32 bit png for logo flaticon.com
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('Files/Photos/icon.png')
background = pygame.image.load('Files/Photos/background.png')
pygame.display.set_icon(icon)

#Create the screen
screen = pygame.display.set_mode((800, 600))      # it is written later so the we only see the icon and title not the
screen.blit(background, (0, 0))                                                   # default first
font = pygame.font.SysFont(None,14,True)

#getting music
background_music = pygame.mixer.music.load('Files/Music/background_music.wav')
pygame.mixer.music.play(-1)
b_hit = pygame.mixer.Sound('Files/Music/boss hit.wav')
b_shoot = pygame.mixer.Sound('Files/Music/boss shoot.wav')
g_reload = pygame.mixer.Sound('Files/Music/gun reload.wav')
p_hit = pygame.mixer.Sound('Files/Music/player hit.wav')
p_shoot = pygame.mixer.Sound('Files/Music/player shoot.wav')





# variables for player
p = player(screen)
player_health = 500
player_maxhealth = 500

bullet_type = 0
bulletimage_number = 3
fired_bullet = 0
b_image = bullet_image(screen)
bulletlist = []
powertime =0
power = powerType(screen)

reload = False

use_once = False

def showbullets(b_type, b_number):
    x=0
    reload = False
    for i in range (0,b_number):
        b_image.createImage(b_type, x, 0)
        x =x+20

def show():
    for i in range(0, fired_bullet):
        if bulletlist[i].fire_state:
                bulletlist[i].show()





#variables for boss enemy

b = boss_Enemy(screen)
boss_health = 600
boss_Damage = 10
boss_fire_time = 0
enemy_bnumber = 0
bullet_E = []



def show_enemyBullet(enemy_bnumber):
  if enemy_bnumber > 0:
    for i in range(0, enemy_bnumber):
        if bullet_E[i] !=0 and bullet_E[i].fire_state:
                bullet_E[i].show()
        else:
            bullet_E[i] = 0
            pass

def empty_Blist(enemy_bnumber):
    for a in bullet_E[:]:
        if a == 0 :
            bullet_E.remove(0)
            enemy_bnumber = enemy_bnumber - 1
    return enemy_bnumber

collision_happened = False
def collision(Ex,Ey,Bx,By,i):
  a = [600 , 600]
  distance = 50000
  if By <= Ey+40 and By >= Ey - 40:
    distance = math.pow((Ex-Bx+10), 2) + math.pow((Ey-10-By),2)
  if distance < a[i]:
    return True
  else:
       return False
       pass


# Function that should be run after every Key press
def run_key():
    p.show()
    b.move_boss()
    showbullets(bullet_type, bulletimage_number)
    show()
    show_enemyBullet(enemy_bnumber)
    b.health_bar(boss_health)
    p.health_bar(player_health,player_maxhealth)
    power.show()


running = True
# Main loop for game
while running:
    screen.blit(background, (0, 0))
    showbullets(bullet_type, bulletimage_number)
    p.show()
    b.move_boss()
    b.health_bar(boss_health)
    p.health_bar(player_health,player_maxhealth)
    boss_fire_time = boss_fire_time + 1
    enemy_bnumber = empty_Blist(enemy_bnumber)
    powertime = powertime + 1
    power.show()

    #Enemy physical atteck
    if(b.attack == False):
        coll = collision(p.posx, p.posy, b.posx, b.posy, 0)
        if coll:
            p_hit.play()
            player_health = player_health - 5


    #Enemy bullet fire

    for i in range(0, enemy_bnumber):
        if bullet_E[i].fire_state:
            p_collision_happened = collision(p.posx, p.posy, bullet_E[i].x, bullet_E[i].y,0)
            if p_collision_happened == False:
                bullet_E[i].fire()
            else:
                bullet_E[i].fire_state = False
                p_hit.play()
                player_health = player_health - 20


    # firing bullet
    for i in range(0, fired_bullet):
        if bulletlist[i].fire_state :
            collision_happened = collision(b.posx,b.posy, bulletlist[i].x,bulletlist[i].y,1)
            if collision_happened == False:
                bulletlist[i].fire()
            else:
                bulletlist[i].fire_state = False
                b_hit.play()
                boss_health = boss_health - power.attackLevel[bullet_type]

    # Enemy shoot
    if(boss_fire_time > 600):
       enemy_bnumber = enemy_bnumber +1
       boss_fire_time = 0
       bullet_E.append(Boss_shoot(screen, b.posx, b.posy))
       b_shoot.play()
       if(bullet_E[enemy_bnumber-1].fire_state):
           bullet_E[enemy_bnumber-1].fire()


    # create power ups

    if (power.fire_state == False ):
            power = powerType(screen)
            if power.b_type == 7 :
                use_once = True
            powertime = 0

    else:
         power.fire()
         powertime = 0



     # power catch and b_type is less than 6 than bullettype if else than healthtype
    if power.fire_state :
         p_catch = collision(p.posx, p.posy, power.x, power.y,0)
         if p_catch == False:
                 power.fire()
         else:
             if power.b_type <= 6:
                power.fire_state = False
                bullet_type = power.b_type
             elif power.b_type == 7 :
                 if use_once:
                    player_health = player_health + 20
                 power.fire_state = False
                 use_once = False
                 pass



    #to show the reloading and bullet image

    if bulletimage_number == 0:
        if fired_bullet > 2:
         if(bulletlist[2].fire_state):
            pass
         else:
            g_reload.play()
            bulletlist.clear()
            fired_bullet = 0
            bulletimage_number = 3




# key Events

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if(bulletimage_number > 0 ):
                  bulletimage_number = bulletimage_number - 1
                  bulletlist.append(fire_bullet(bullet_type, screen, p.posx, p.posy))       # create and add new bullet object to fire
                  p_shoot.play()
                  fired_bullet = fired_bullet + 1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        screen.blit(background, (0, 0))
        p.move_Right()
        run_key()
        pass
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        screen.blit(background, (0, 0))
        p.move_Left()
        run_key()
        pass
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        screen.blit(background, (0, 0))
        p.move_Up()
        run_key()
        pass
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        screen.blit(background, (0, 0))
        p.move_Down()
        run_key()
        pass
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        p.speed = p.speedmax
    else:
        p.speed = p.speedmin

    if keys[pygame.K_SPACE]:
        showbullets(bullet_type, bulletimage_number)

        pass

    pygame.display.update()
    if b.running and p.running and running:
        running = True
    else :
        running = False
