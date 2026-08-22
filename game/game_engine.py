from Linkedlist import Node
#Callibrations for the board
width = 10
height = 20
shape_size = 4
shapes_no = 6




#setting Board
class Board(Node):
    #setting row
    
    def row_init():
        row=[]
        for i in range(width):
            row.append(0)   
        return row
    
    def __init__(self):
        for i in range(height+shape_size):
            row=self.row_init()
            self.add_node(row,i+1)
        self.col=0
    def get_row(self,cursor):
       
        self.shape=Cursor(0)
        current=self.head
        p=current
        size=cursor.get_size()
        row = height+shape_size
        while(row>=shape_size):
 
            for i in range(0,shape_size,-1):
                for j in range(0,size,1):
                    self.shape[i][j]=current.data[self.col+j]
                
                current=current.next
            

            for i in range(0,shape_size,1):
                for j in range(0,shape_size,1):
                    if(self.shape[i][j]+cursor.shape[i][j]==2):
                        break
                
                if(self.shape[i][j]+cursor.shape[i][j]==2):
                    break
            

        
            if(self.shape[i][j]+cursor.shape[i][j]==2):
                row-=1
                break
            p=p.next
        if(row==shape_size-1):
            row=shape_size
                
            return row  
    def move_cursor(self,cursor,pos):
        size=cursor.get_size()
        if(pos==-1):
            self.col-=1
        elif(pos==1):
            self.col+=1
        else:
            self.col=self.col
        if(self.col>width-size):
            self.col=0
        if(self.col<0):
            self.col=width-size

    def update_board(self,cursor):
        size=cursor.get_size()
        row=self.get_row(cursor)
        current=self.head
        for i in range(row,shape_size-1,-1):
            for j in range(self.col,self.col+size,1):
                current.data[j+self.col]=current.data[j+self.col]+cursor.shape[i][j]
                if(current.data[j+self.col]!=0):
                    current.data[j+self.col]=1
            current=current.next

        current=self.head
        while(1):
            p=current
            current=current.next
            if(current==None):
                break
            Line=0
            for j in range(0,width,1):
                Line=Line+current.data[j]
            if(Line>=width):
                self.remove_row(p)
                current=p

        if(self.get_count()<height+shape_size):
            for i in range(self.get_count(),height+shape_size,1):
                self.add_row()
   


class Cursor:
    def __init__(self,ID):
        self.shape=[]
        self.ID=ID
        row=[]
        for i in range (shape_size):
            for j in range (shape_size):
                row.append(ID%2)
            self.shape.append(row)

    def rotate(self):
        newshape=[]
        for i in range(shape_size):
            for j in range(shape_size):
                newshape.append(self.shape[j][3-i])
            self.shape=newshape

        while(self.shape[0][0]+self.shape[1][0]+self.shape[2][0]+self.shape[3][0]==0):
            for i in range(shape_size):
                for j in range(shape_size):
                    if(j!=3):
                        self.shape[i][j]= self.shape[i][j+1]
                    else:
                        self.shape[i][j]= 0
        while(self.shape[0][0]+self.shape[0][1]+self.shape[0][2]+self.shape[0][3]==0):
            for i in range(shape_size):
                for j in range(shape_size):
                    if(i!=3):
                        self.shape[i][j]= self.shape[i+1][j]
                    else:
                        self.shape[i][j]= 0


    def get_size(self):
        size=0
        temp=0
        for i in range(shape_size):
            for j in range(shape_size):
                if(self.shape[i][j]>=1):
                    temp=j+1
            if(temp>=size):
                size=temp
            temp=0
        return size

        
    
  
        






  