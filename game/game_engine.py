
#Callibrations for the board

width = 10
height = 20
shape_size = 4
shapes=[39,99,54,15,275,51]


def randomizer():
    import random
    r=random.randint(0,len(shapes)-1)
    return shapes[r]

#setting Board
class Board:
    board=[]
    #setting row
    def __init__(self,data):
        print("Board init")
        self.board.clear()
        for i in range(height):
            self.board.append(data%(2**width))
            data=data//(2**width)

   


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
        self.cursor.clear()
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
        if (self.col>width-self.size):
            self.col=width-self.size

    def converter(self):
        temp=[]
        if(self.col<=width-self.size):
            for i in range(shape_size):
                temp.append(2**(self.col)*self.cursor[i])
            return temp
        else:
            return
    
        



def get_row(brd,csr):
    temp=csr.converter()
    for i in range(height-shape_size,-1,-1):
        for j in range(shape_size):
            if(brd.board[i+j]&temp[j]!=0):
                j=4
                break
        if(j==4):
            break
    if(j==4):
        return i+1
    else:
        return i


def update_Game(brd,csr):

    rows=[]
    row=get_row(brd,csr)
    for i in range(shape_size):
        rows.append(row+i)
    csrtemp=csr.converter()
    for i in range(height-1,-1,-1):
        temp=brd.board[i]
        for j in range(width):
            if i in rows:
                k=i-row
                brd.board[i]=((temp)|(csrtemp[k]))
    for i in range(height-shape_size-1,-1,-1):
        if(brd.board[i]==(2**(width)-1)):
            brd.board.pop(i)
            brd.board.append(0)


def Game(brd,csr,prm):
    #print(brd.board[(height-shape_size+1)])
    match(prm):
        case 'e':
            return 0
        case 'w':
            csr.rotater()
            return -1
        case 'd':
            csr.col+=1
            if(csr.col==width-csr.size+1):
                csr.col=0
            return -1
        case 'a':
            
            if(csr.col==0):
                csr.col=width-csr.size+1
            csr.col-=1
            return -1
        case '\r':
            
            update_Game(brd,csr) 
            csr=Cursor(randomizer())
            if(brd.board[(height-shape_size+1)]>0):
                brd=Board(0)
                return 1
            return -1
                  




            

                




           
    
        
 
 