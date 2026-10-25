
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
    def update(self,cursor):
        pass



class Cursor:
    cursor=[]
    col=0
    row=0
    size=0
    def __init__(self,data):
        if(data<0):
            data=0
        data=data//1

        #print("Starting funcion \n Cursor init")
        for i in range(shape_size):
            self.cursor.append(data%(2**shape_size))
            data=data//(2**shape_size)
        self._setter()
        
    def _rotate(self):
         #print("\n Cursor rotate")
        temp=self.cursor
        new=[]
        for i in range(shape_size):
            new.append(0)
            for j in range(shape_size):
                new[i]=new[i]+((2**j)*(temp[j]%2))
                temp[j]=temp[j]//2
        for i in range(shape_size):
            temp[i]=new[shape_size-1-i]
        new=temp 
        self.cursor=new
    def _setter(self):
        if(max(self.cursor)==0):
            return
        while(self.cursor[0]==0):
            self.cursor.append(self.cursor.pop(0))
        self._rotate()
        
        self._rotate()
        self._rotate()
        while(self.cursor[0]==0):
            self.cursor.append(self.cursor.pop(0))
        self._rotate()
        self.sizer()
    def rotater(self):
        self._rotate()
        self._setter()

    def sizer(self):
        Max=max(self.cursor)
        i=1
        while(Max>1):
            #print(Max)
            Max=Max//2
            i+=1
        self.size=i    


    
            

                




           
    
        
 
 