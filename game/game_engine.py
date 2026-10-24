
#Callibrations for the board

width = 8
height = 20
shape_size = 4
shapes_no = 6




#setting Board
class Board:
    board=[]
    #setting row
    def __init__(self,data):
        print("Starting funcion \n Board init")
        for i in range(height):
            self.board.append(data%(2**width))
            data=data//(2**width)



class Cursor:
    cursor=[]
    col=0
    def __init__(self,data):
        print("Starting funcion \n Cursor init")
        for i in range(shape_size):
            self.board.append(data%(2**shape_size))
            data=data//(2**shape_size)

           
    
        
 
 