import pygame
import random
##################################Bullet class which will be shooted by both enemy and player#####
class fire_bullet:
    fire_state = True
    screen = pygame.display
    s_bullet = pygame.image.load('Files/Photos/Single_bullet.png')
    d_bullet = pygame.image.load('Files/Photos/Double_bullet.png')
    t_bullet = pygame.image.load('Files/Photos/triple_bullets.png')
    st_bullet = pygame.image.load('Files/Photos/Single_lightning.png')
    dt_bullet = pygame.image.load('Files/Photos/Doublethunder_bullet.png')

    fireball = pygame.image.load('Files/Photos/fireball.png')
    thunderball = pygame.image.load('Files/Photos/thunder_ball.png')




    b_type = 0

    bullettype = [s_bullet, d_bullet, t_bullet, st_bullet, dt_bullet, fireball, thunderball ]
    x = 0
    y = 0
    speed = 1
    def __init__(self, b_type, screen, x, y):
        self.x = x
        self.y = y

        self.screen = screen
        self.b_type = b_type

        screen.blit(self.bullettype[self.b_type], (x + 15 , y + 15))
        pass
    def show(self):
        self.screen.blit(self.bullettype[self.b_type], (self.x, self.y))

    def fire(self):
        if self.y > 5:
            self.y = self.y - self.speed
            self.screen.blit(self.bullettype[self.b_type], (self.x, self.y))
            self.fire_state = True
        else:
            self.fire_state = False



#bullettype : 0.1. 2.  bullet (single,double,triple)
#  3.4. single, double thunder
# 5.6. fire and thunder ball

class bullet_image:
    screen = pygame.display
    s_bullet = pygame.image.load('Files/Photos/Single_bullet.png')
    d_bullet = pygame.image.load('Files/Photos/Double_bullet.png')
    t_bullet = pygame.image.load('Files/Photos/triple_bullets.png')
    st_bullet = pygame.image.load('Files/Photos/Single_lightning.png')
    dt_bullet = pygame.image.load('Files/Photos/Doublethunder_bullet.png')

    fireball = pygame.image.load('Files/Photos/fireball.png')
    thunderball = pygame.image.load('Files/Photos/thunder_ball.png')

    #empty_image = s_bullet


    bullettype = [s_bullet, d_bullet, t_bullet, st_bullet, dt_bullet, fireball, thunderball]




    def __init__(self,screen):
       self.screen = screen

    def createImage(self,b_type,x,y):
        bullet_image = self.bullettype[b_type]
        self.screen.blit(bullet_image,(x,y))


class Boss_shoot:
    fire_state = True
    screen = pygame.display

    boss_bullet = pygame.image.load('Files/Photos/Enemy_bullet.png')
    x = 0
    y = 0
    speed = 1

    def __init__(self, screen, x, y):
        self.x = x
        self.y = y

        self.screen = screen

        screen.blit(self.boss_bullet, (x + 15, y + 15))
        pass

    def show(self):
        self.screen.blit(self.boss_bullet, (self.x, self.y))

    def fire(self):
        if self.y > 5 and self.y < 590:
            self.y = self.y + self.speed
            self.screen.blit(self.boss_bullet, (self.x, self.y))
            self.fire_state = True
        else:
            self.fire_state = False

# create power level , attack , Health for player

class powerType :
    fire_state = True
    screen = pygame.display
    s_bullet = pygame.image.load('Files/Photos/Single_bullet.png')
    d_bullet = pygame.image.load('Files/Photos/Double_bullet.png')
    t_bullet = pygame.image.load('Files/Photos/triple_bullets.png')
    st_bullet = pygame.image.load('Files/Photos/Single_lightning.png')
    dt_bullet = pygame.image.load('Files/Photos/Doublethunder_bullet.png')

    fireball = pygame.image.load('Files/Photos/fireball.png')
    thunderball = pygame.image.load('Files/Photos/thunder_ball.png')

    medkit = pygame.image.load('Files/Photos/mediKit.png')
    b_type = 0

    bullettype = [s_bullet, d_bullet, t_bullet, st_bullet, dt_bullet, fireball, thunderball , medkit]
    attackLevel = [10,20,30,30,60,100,100]

    y = 20
    x = 0

    def __init__(self,screen):
        self.b_type =random.randint(0, 7)
        self.screen = screen
        self.x = random.randint(100,700)
        self.screen.blit(self.bullettype[self.b_type], (self.x,self.y))
        pass

    def fire(self):
        if self.y < 590 :
            self.y = self.y + 0.5
            self.fire_state =True
            self.show()
        else:
            self.fire_state = False
    def show(self):
        self.screen.blit(self.bullettype[self.b_type], (self.x, self.y))