import os
import msvcrt
import pygame
from game.game_engine import game_atts
SCR_WDT=game_atts["screen_width"]
SCR_HGT=game_atts["screen_height"]

screen_rect=pygame.Rect(0,0,SCR_WDT,SCR_HGT)

def getch():
    # msvcrt.getch() returns a byte string; decode it to get a standard string
    return msvcrt.getch().decode("utf-8", errors="ignore")
def clear_screen():
    os.system('cls')
def pygame_menu(screen,clock,background):
    running=True
    while (running):
        mouse_click_pos = (0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click_pos = event.pos
        
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background,screen_rect)
        c_x=screen_rect.centerx
        c_y=screen_rect.centery

        newgame_img=pygame.image.load("graphics/newgame.png").convert()
        continue_img=pygame.image.load("graphics/continue.png").convert_alpha()
        exit_img=pygame.image.load("graphics/exit.png").convert_alpha()
        newgame_selected_img=pygame.image.load("graphics/newgameselected.png").convert_alpha()
        continue_selected_img=pygame.image.load("graphics/continueselected.png").convert_alpha()
        exit_selected_img=pygame.image.load("graphics/exitselected.png").convert_alpha()

        newgame_rect=newgame_img.get_rect(center = (c_x,c_y-120))
        continue_rect=continue_img.get_rect(center = (c_x,c_y))
        exit_rect=exit_img.get_rect(center = (c_x,c_y+120))
        newgame_selected_rect=newgame_selected_img.get_rect(center = (c_x,c_y-120))
        continue_selected_rect=continue_selected_img.get_rect(center = (c_x,c_y))
        exit_selected_rect=exit_selected_img.get_rect(center = (c_x,c_y+120))

        newgame_img.set_colorkey((126,196,0))
        continue_img.set_colorkey((126,196,0))
        exit_img.set_colorkey((126,196,0))
        newgame_selected_img.set_colorkey((126,196,0))
        continue_selected_img.set_colorkey((126,196,0))
        exit_selected_img.set_colorkey((126,196,0))

        
        
        screen.blit(newgame_img,newgame_rect)
        screen.blit(continue_img,continue_rect)
        screen.blit(exit_img,exit_rect)

        if(newgame_selected_rect.collidepoint(mouse_pos)):
            screen.blit(newgame_selected_img,newgame_selected_rect)
        elif( continue_selected_rect.collidepoint(mouse_pos)):
            screen.blit(continue_selected_img,continue_selected_rect)
        elif(exit_selected_rect.collidepoint(mouse_pos)):
            screen.blit(exit_selected_img,exit_selected_rect)

        if(newgame_selected_rect.collidepoint(mouse_click_pos)):
            screen.blit(newgame_selected_img,newgame_selected_rect)
            return -1
        elif( continue_selected_rect.collidepoint(mouse_click_pos)):
            screen.blit(continue_selected_img,continue_selected_rect)
            return 1
        elif(exit_selected_rect.collidepoint(mouse_click_pos)):
            screen.blit(exit_selected_img,exit_selected_rect)
            return 0


        pygame.display.flip()

        clock.tick(60) 



def pygame_pause(screen,clock,background):
    running=True
    while (running):
        mouse_click_pos = (0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click_pos = event.pos
        
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background,screen_rect)
        c_x=screen_rect.centerx
        c_y=screen_rect.centery

        newgame_img=pygame.image.load("graphics/newgame.png").convert_alpha()
        continue_img=pygame.image.load("graphics/continue.png").convert_alpha()
        exit_img=pygame.image.load("graphics/exit.png").convert_alpha()
        newgame_selected_img=pygame.image.load("graphics/newgameselected.png").convert_alpha()
        continue_selected_img=pygame.image.load("graphics/continueselected.png").convert_alpha()
        exit_selected_img=pygame.image.load("graphics/exitselected.png").convert_alpha()

        newgame_img.set_colorkey((126,196,0))
        continue_img.set_colorkey((126,196,0))
        exit_img.set_colorkey((126,196,0))
        newgame_selected_img.set_colorkey((126,196,0))
        continue_selected_img.set_colorkey((126,196,0))
        exit_selected_img.set_colorkey((126,196,0))

        newgame_rect=newgame_img.get_rect(center = (c_x,c_y-120))
        continue_rect=continue_img.get_rect(center = (c_x,c_y))
        exit_rect=exit_img.get_rect(center = (c_x,c_y+120))
        newgame_selected_rect=newgame_selected_img.get_rect(center = (c_x,c_y-120))
        continue_selected_rect=continue_selected_img.get_rect(center = (c_x,c_y))
        exit_selected_rect=exit_selected_img.get_rect(center = (c_x,c_y+120))

        
        
        screen.blit(newgame_img,newgame_rect)
        screen.blit(continue_img,continue_rect)
        screen.blit(exit_img,exit_rect)

        if(newgame_selected_rect.collidepoint(mouse_pos)):
            screen.blit(newgame_selected_img,newgame_selected_rect)
        elif( continue_selected_rect.collidepoint(mouse_pos)):
            screen.blit(continue_selected_img,continue_selected_rect)
        elif(exit_selected_rect.collidepoint(mouse_pos)):
            screen.blit(exit_selected_img,exit_selected_rect)

        if(newgame_selected_rect.collidepoint(mouse_click_pos)):
            screen.blit(newgame_selected_img,newgame_selected_rect)
            return -1
        elif( continue_selected_rect.collidepoint(mouse_click_pos)):
            screen.blit(continue_selected_img,continue_selected_rect)
            return 1
        elif(exit_selected_rect.collidepoint(mouse_click_pos)):
            screen.blit(exit_selected_img,exit_selected_rect)
            return 0


        pygame.display.flip()

        clock.tick(60) 
