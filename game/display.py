
from game.game_engine import *
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
def display_Game(brd,csr):
    clear_screen()

   

    print("\nBoard")
    rows=[]
    row=get_row(brd,csr)
    for i in range(shape_size):
        rows.append(row+i)
    csrtemp=csr.converter()
    for i in range(height-shape_size-1,-1,-1):
        print("|",end="")
        temp=brd.board[i]
        #print(temp,end=" ")
        for j in range(width):
            if i in rows:
                k=i-row
                pr=((temp%2)+(csrtemp[k]%2*2))
                temp=temp//2
                csrtemp[k]=csrtemp[k]//2

            else:
                pr=temp%2
                temp=temp//2
            match(pr):
                case 0:
                    print(" ",end="")
                case 1:
                    print("$",end="")
                case 2:
                    print("#",end="")
        print("|")


