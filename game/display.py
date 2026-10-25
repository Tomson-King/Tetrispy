
from game.game_engine import width,height,shape_size
#import curses
#import pygame
import os
import msvcrt

def getch():
    # msvcrt.getch() returns a byte string; decode it to get a standard string
    return msvcrt.getch().decode("utf-8", errors="ignore")
def clear_screen():
    os.system('cls')



def display_board(brd):
    clear_screen()

    print("\nBoard")
    for i in range(height-shape_size-1,-1,-1):
        print("")
        temp=brd.board[i]
        #print(temp,end=" ")
        for j in range(width):
            print((temp%2),end=" ")
            temp=temp//2
def display_cursor(crs):
    
    print(f"\nCursor size {crs.size}")
    for i in range(shape_size-1,-1,-1):
        print("")
        temp=crs.cursor[i]
        #print(temp,end=" ")
        for j in range(shape_size):
            print((temp%2),end=" ")
            temp=temp//2



