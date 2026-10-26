
from game import shape_size
from game.game_engine import *
#import curses
import pygame
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
def terminal_Game(brd,csr):
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

    
    
def display_Game(brd,csr,screen,clock,prm):
    length=40
    csr_colour="red"
    tetris_colour="white"
    bg_colour="black"
    prm=1
    running = True

    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    prm='w'
                elif event.key == pygame.K_a:
                    prm='a'
                elif event.key == pygame.K_d:
                    prm='d'
                elif event.key == pygame.K_RETURN:
                    prm='\r'

    # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        
           
    # RENDER YOUR GAME HERE
        game=Game(brd,csr,prm)
        prm=1
        rows=[]
        row=get_row(brd,csr)
        for i in range(shape_size):
            rows.append(row+i)
        csrtemp=csr.converter()
        for i in range(height-shape_size-1,-1,-1):
            
            temp=brd.board[i]
            
            for j in range(width):
                if i in rows:
                    k=i-row
                    pr=((temp%2)+(csrtemp[k]%2*2))
                    temp=temp//2
                    csrtemp[k]=csrtemp[k]//2

                else:
                    pr=temp%2
                    temp=temp//2
                tetris=pygame.Rect(j*length,(height-shape_size-i)*length,length,length)
                match(pr):
                    case 0:
                        pygame.draw.rect(screen,bg_colour,tetris)
                       
                    case 1:
                        pygame.draw.rect(screen,tetris_colour,tetris)
                       
                    case 2:
                        pygame.draw.rect(screen,csr_colour,tetris)
                               


    # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60)  # limits FPS to 60

    

   
"""pip 
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
"""
