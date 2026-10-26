

from game.game_engine import *
from game.main_menu import pygame_menu,pygame_pause
#import curses
import pygame
import os
import msvcrt
import time

SCR_WDT=game_atts["screen_width"]
SCR_HGT=game_atts["screen_height"]

screen_rect=pygame.Rect(0,0,SCR_WDT,SCR_HGT)



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
    while(True):

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
        key=getch()
        clear_screen()
        game=Game(brd,csr,key)
        if(game==0):
            break


def Pygame_init(board,cursor):
    pygame.init()
    screen = pygame.display.set_mode((SCR_WDT, SCR_HGT))
    background=pygame.image.load("graphics/background.png").convert()
    clock = pygame.time.Clock()
   
    prm=1

  
    out=-1
    running=True
    opt=pygame_menu(screen,clock,background)

    while(running):
        if(opt==0):
            break
        elif(opt==-1):
            board=Board(0)
        out=display_Game(board,cursor,screen,clock,prm,background)
        if(out==1):
            print(out)
        elif(out==0):
            print(out)
            running=False
        

    pygame.quit()   


    
def display_Game(brd,csr,screen,clock,prm,background):
    length=game_atts["length"]
    csr_colour=game_atts["csr_colour"]
    tetris_colour=game_atts["tetris_colour"]
    notetris_colour=game_atts["notetris_colour"]
    bg_colour=game_atts["bg_colour"]
    tetris_img=pygame.image.load("graphics/tetris.png").convert_alpha()
    board_img=pygame.image.load("graphics/board.png").convert_alpha()
    prm=1
    running = True
    pause=False
    start=int(time.time())
    
    c_x=screen_rect.centerx
    c_y=screen_rect.centery
    
    board_surf=pygame.Surface((400,640))
    #board_surf.fill("red")
    board_rect=board_surf.get_rect(center=(c_x,c_y))
    coords=board_rect.topleft
    


    while running:
        screen.blit(background,screen_rect)
        screen.blit(board_img,board_rect)
        
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                prm='e'
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    prm='w'
                elif event.key == pygame.K_a:
                    prm='a'
                elif event.key == pygame.K_d:
                    prm='d'
                elif event.key == pygame.K_RETURN or event.key == pygame.K_s:
                    prm='\r'
                elif event.key == pygame.K_ESCAPE:
                    pause=True
                    

      
           
    # RENDER YOUR GAME HERE

        rows=[]
        row=height-shape_size
        rjump=int(time.time())-start
        row-=rjump
        opt=None
        if(pause):
            opt=pygame_pause(screen,clock,background)
            pause=False
        
        if(opt==-1):
            brd=Board(0)
            csr=Cursor(randomizer())
            start=int(time.time())
            rjump=int(time.time())-start
            continue
        elif(opt==1):
            start=int(time.time())-rjump
        elif(opt==0):
            prm='e'

        if(row<=get_row(brd,csr)):
            row=get_row(brd,csr)
            prm='\r'
        game=Game(brd,csr,prm) 
        if(game==1 or game==0):
            break
        if(prm=='\r'):
            start=int(time.time())
        
        prm=1
        
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
                tetris=pygame.Rect(coords[0]+(j*length),coords[1]+((height-shape_size-1-i)*length),length,length)
                match(pr):
                    case 0:
                        pass
                        
                       
                    case 1:
                        screen.blit(tetris_img,tetris)
                       
                    case 2:
                        screen.blit(tetris_img,tetris)
                               


    # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60)  # limits FPS to 6
    return game
    