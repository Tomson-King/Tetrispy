class Node :
    def __init__(self,data):
        self.data:list=data
        self.node:Node=None
    def __str__(self):
        return f"{id(self)}"
    def get_Node(self,pos:int)->Node:
        if(pos==1):
            return self
        for i in range (pos-1):
            if(self==None):
                return None
            self=self.node
    def get_Count(self)->int:
        if (self==None):
            return None
        i=1
        while(self.node!=None):
            self=self.node
            i+=1
        return i
    def Display(self):
     
        print(f"Adress {id(self)}")
        while(self!=None):
            for key,value in self.data.items():
                print(f"{key} : {value}\t",end="")
            print() #new line   
            self=self.node
    def add_node(self,newnode,pos)->Node:
        if(pos==1):
            newnode.node=self
            self=newnode
            return self
        elif(pos==self.get_Count()+1):
            temp=self.get_Node(pos-1)
            temp.node=newnode
            return self
        elif(pos>1 and pos<self.get_Count()+1):
            temp=self.get_Node(pos-1)
            newnode.node=temp.node
            temp.node=newnode
            return self
        else:
            print("Invalid Position")
            return self
    def delete_node(self,pos)->Node:
        if(pos<1 or pos>self.get_Count()):
            print("Invalid Position")
            return self
        if(pos==1):
            self=self.node
            return self
        temp=self.get_Node(pos-1)
        temp.node=temp.node.node
        return self    




    

def Main_menu():
    head=None
    opt:int=-1
    while(opt!=0):
        print(f"--------MENU--------\n1:Add node \n2: Delete node\n3:Display\n0:Exit")
        opt:int=int(input("Enter Option :"))
        match(opt):
            case 1:
                Id=int(input("Enter Id: "))
                Name=input("Enter Name: ")
                course=input("Enter Course: ")
                data={
                    "Id":Id,
                    "Name":Name,
                    "Course":course
                }
                if(head==None):
                    head=Node(data)
                else:
                    pos=int(input("Enter Position: "))
                    newnode=Node(data)
                    head=head.add_node(newnode,pos)
            case 2:
                if(head==None):
                    print("List is empty")
                else:
                    pos=int(input("Enter Position: "))
                    head=head.delete_node(pos)
            case 3:
                if(head==None):
                    print("Empty List")
                else:
                    head.Display()
            case 0:
                break
            case _: 
                print("Invalid Option") 





