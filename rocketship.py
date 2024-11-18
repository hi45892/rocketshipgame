import pygame, sys
from pygame.locals import *
from time import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("rocket ship")

player = pygame.image.load("animation images/rocketship/chr.png")
background = pygame.image.load("animation images/rocketship/bg1.png")

player_x = 400
player_y = 300



key = [False,False,False,False]
while player_y < 600:
      screen.blit(background,(0,0))
      screen.blit(player,(player_x,player_y))
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key ==K_UP:
                 key[0]=True
            elif event.key==K_LEFT:
                 key[1]=True
            elif event.key==K_DOWN:
                 key[2]=True
            elif event.key==K_RIGHT:
                 key[3]=True

        if event.type==pygame.KEYUP:
            if event.key ==K_UP:
                 key[0]=False
            elif event.key==K_LEFT:
                 key[1]=False
            elif event.key==K_DOWN:
                 key[2]=False
            elif event.key==K_RIGHT:
                 key[3]=False
      if key[0]==True:
       if player_y >0:
          player_y -= 10
      elif key[1]==True:
       if player_x >0:
          player_x -= 10
      elif key[2]==True:
       if player_y <500:
          player_y += 10
      elif key[3]==True:
       if player_x <700:
          player_x += 10
      
      player_y += 5
      sleep(0.07)
print("Game over")