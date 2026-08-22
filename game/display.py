from game.game_engine import width,height,shape_size
import pygame

screen=pygame.display.set_mode((width*100,height*100))
def display(board,cursor):
    row=board.get_row(cursor)
    row=row+shape_size-1
    col=board.col
    current=board.head
    size=cursor.get_size()

    
    current=board.get_Node(height)
    for i in range(height+shape_size-1,0,-1):
        if(i>height):
            current=current.node
            continue
        for j in range(width):
            if(i<=row and i>row-shape_size and j>=col and j<col+size):
                if(cursor.shape[i-row][j-col]==0):
                    print("  ")
                else:
                    print("==")
            else:
                if(current.data[j]==0):
                    print("  ")
                else:
                    print("++")

     
        current=current.node

