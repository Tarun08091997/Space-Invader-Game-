import pygame
import random
from pygame.locals import *

#############################################CREATING BOSS ENEMY###################################################
# will have own movement
# will move around randomly
# shoots at an intervel
from pygame.tests.draw_test import RED, GREEN


class boss_Enemy:
    boss_image = pygame.image.load('Files/Photos/boss1.png')
    boss_x = 64
    boss_y = 64

    posx = 350           # current position and velocity vector
    posy = 100
    speed = 1

    Xmax = 730  # 800 - 35          # boundry of screen
    Xmin = 35
    Ymax = 150
    Ymin = 35
    error = 5
    screen = pygame.display
    boss_move = 0
    teleport = 0
    attack = False
    play_once = True
    running = True

    def __init__(self,screen):
        self.screen = screen
        self.posy = random.randint(self.Ymin + 10 * self.error, self.Ymax - 10 * self.error)
        self.posx = random.randint(self.Xmin + 10 * self.error, self.Xmax - 10 * self.error)
        self.screen.blit(self.boss_image, (self.posx, self.posy))
        pygame.display.update()
    pass

    def showboss(self):
        self.screen.blit(self.boss_image, (self.posx, self.posy))
        pass



    def move_boss(self):
          if ((self.posx > self.Xmin+self.error) and (self.posx < self.Xmax - self.error) and (self.posy > self.Ymin+self.error) and (self.posy < self.Ymax - self.error)) and self.boss_move < 3000:
                x = random.randint(-self.speed, +self.speed)
                y = random.randint(-self.speed, +self.speed)
                self.posx = self.posx + x
                self.posy = self.posy + y
                self.boss_move = self.boss_move + 1
                self.attack = True
                pass
          else:
              if self.teleport <200:
                  self.physical_attack()
                  self.teleport = self.teleport + 1
              else:
                  self.posy = random.randint(self.Ymin + 10 * self.error, self.Ymax - 10 * self.error)
                  self.posx = random.randint(self.Xmin + 10 * self.error, self.Xmax - 10 * self.error)
                  self.boss_move = 0
                  self.teleport = 0

          self.showboss()
    def health_bar(self,health):
        if health > 0 :
          pygame.draw.rect(self.screen,RED, (100,5 ,600,20),1)
          pygame.draw.rect(self.screen, RED, (100, 5, health, 20))
        else:
            if self.play_once :
              b_hit = pygame.mixer.Sound('Files/Music/boss hit.wav')
              b_hit.play(2)
              self.play_once = False
              r =True
              font = pygame.font.Font('freesansbold.ttf', 40)
              msg = font.render('YOU WON', True, GREEN)
              while (r):
                  print("lol")
                  self.screen.blit(msg, (350, 250))
                  self.running = False

                  for event in pygame.event.get():
                      if event.type == MOUSEBUTTONDOWN:
                          r = False


    def physical_attack(self):
       if self.attack :
         self.posy = random.randint(250 + 10 * self.error, 500 - 10 * self.error)
         self.posx = random.randint(self.Xmin + 10 * self.error, self.Xmax - 10 * self.error)
         self.attack = False
       else :
         self.showboss()