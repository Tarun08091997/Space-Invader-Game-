import pygame
import random
from pygame.locals import *
from pygame import mixer

#////////////////////////////////create a player class/////////////////////////////////////////////////////////////////
# This class is for main player
# posx and posy are the current position of the player
# speed is no. of pixel moved by player
# p_x and p_y are size of player
# Xmax,Xmin ,Ymax and Ymin are boundry of game
#  Left,Right,Up and Down functions
# Shoot function
from pygame.tests.draw_test import GREEN, RED


class player :
    # Player image is 64*64
    player_image = pygame.image.load('Files/Photos/player.png')
    posx = 350
    posy = 500
    speed = 0.2
    speedmax = 2
    speedmin = 1
    p_x = 64
    p_y = 64
    Xmax = 730    # 800 - 35
    Xmin = 35
    Ymax = 530
    Ymin = 350
    error = 5
    screen = pygame.display
    play_once = True
    running = True

    def __init__(self, screen):
       self.screen = screen
       self.screen.blit(self.player_image, (self.posx, self.posy))
       pass
    def show(self):
        self.screen.blit(self.player_image, (self.posx, self.posy))
        pass

    def move_Right(self):
        if self.posx < self.Xmax and self.posx > (self.Xmin-self.error):
            self.posx = self.posx + self.speed

    def move_Left(self):
        if self.posx < (self.Xmax+self.error) and self.posx > self.Xmin :
            self.posx = self.posx - self.speed

    def move_Up(self):
        if self.posy > self.Ymin and self.posy < (self.Ymax+ self.error) :
            self.posy = self.posy - self.speed

    def move_Down(self):
        if self.posy > (self.Ymin-self.error) and self.posy < self.Ymax :
            self.posy = self.posy + self.speed

    def health_bar(self,player_health,player_maxhealth):
        if player_health > 0 :
           pygame.draw.rect(self.screen, GREEN, (100,580,600,20),1)
           pygame.draw.rect(self.screen, GREEN, (100, 580, player_health, 20))
        else:
            if self.play_once :
                p_dead = pygame.mixer.Sound('Files/Music/player_dead.wav')
                p_dead.play(2)
                self.play_once = False
                r = True
                font = pygame.font.Font('freesansbold.ttf', 40)
                msg = font.render('YOU LOST', True, RED)
                while (r):
                    self.screen.blit(msg, (350, 250))
                    self.running = False

                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            r = False