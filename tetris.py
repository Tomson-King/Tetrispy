

from game import *
import pygame
import time
print("Starting funcion")
board=Board(0)
cursor=Cursor(randomizer())
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
prm=1

"""
terminal_Game(board,cursor)
while(prm!=0):
   prm=getch()
   prm=controller(board,cursor,prm)
   time.sleep(1)
   update_Game(board,cursor)
   if(prm==2):
        cursor=Cursor(randomizer())
    terminal_Game(board,cursor)
"""
    
display_Game(board,cursor,screen,clock,prm)
pygame.quit()
