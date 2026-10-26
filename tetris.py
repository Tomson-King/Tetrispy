
from game import *
print("Starting funcion")
board=Board(0)
cursor=Cursor(randomizer())
prm=4
display_Game(board,cursor)
while(prm!=0):
    prm=getch()
    prm=controller(board,cursor,prm)
    if(prm==2):
        cursor=Cursor(randomizer())
    display_Game(board,cursor)
    
    
