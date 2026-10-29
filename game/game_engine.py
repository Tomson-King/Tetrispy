#Callibrations for the board
import game
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f'log/{__name__}.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)




with open('./game/game_atribute.json', 'r') as file:
    game_atts = json.load(file)
width = game_atts["width"]
height = game_atts["height"]
shape_size = game_atts["shape_size"]
shapes=game_atts["shapes"]


def randomizer():
    logger.debug("Executing randomizer")
    try:
        import random
        r=random.randint(0,len(shapes)-1)
        logger.info(f"Shape no:{r}")
        return shapes[r]
    except Exception as e:
        logger.error(f"Error in randomizer: {e}", exc_info=True)
        raise
    finally:
        logger.debug("Finished randomizer")

#setting Board
class Board:
    board=[]
    #setting row
    def __init__(self,data):
        logger.info(f"Initializing Board with data: {data}")
        try:
            self.board.clear()
            for i in range(height):
                self.board.append(data%(2**width))
                data=data//(2**width)
        except Exception as e:
            logger.error(f"Error in Board.__init__: {e}", exc_info=True)
            raise
        finally:
            logger.info("Finished Board.__init__")
    def log_board(self):
        logger.debug("Executing log_cursor")
        try:
            for i in range(height-shape_size-1,-1,-1):
                line=[]
                temp=self.board[i]
                #print(temp,end=" ")
                for j in range(width):
                    line.append(temp%2)
                    temp=temp//2
                
                logger.info(f"{line}")
            
        except Exception as e:
            logger.error(f"Error in log_cursor: {e}", exc_info=True)
            raise
        finally:
            logger.debug("Finished log_cursor")     

   


class Cursor:
    cursor=[]
    col=0
    size=0
    def __init__(self,data):
        logger.info(f"Initializing Cursor with data: {data}")
        try:
            if(data<0):
                data=0
            data=data//1

            #print("Starting funcion \n Cursor init")
            self.cursor.clear()
            for i in range(shape_size):
                self.cursor.append(data%(2**shape_size))
                data=data//(2**shape_size)
            self._setter()
            

        except Exception as e:
            logger.error(f"Error in Cursor.__init__: {e}", exc_info=True)
            raise
        finally:
            logger.info("Finished Cursor.__init__")
        
    def log_cursor(self):
        logger.debug("Executing log_cursor")
        try:
            for i in range(shape_size-1,-1,-1):
                line=[]
                temp=self.cursor[i]
                #print(temp,end=" ")
                for j in range(shape_size):
                    line.append(temp%2)
                    temp=temp//2
                
                logger.info(f"{line}")
            logger.info(f"current size= {self.size}")
            logger.info(f"current column= {self.col}")
        except Exception as e:
            logger.error(f"Error in log_cursor: {e}", exc_info=True)
            raise
        finally:
            logger.debug("Finished log_cursor")     
    def _rotate(self):
        logger.debug("Executing Cursor._rotate")
        try:
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
        except Exception as e:
            logger.error(f"Error in Cursor._rotate: {e}", exc_info=True)
            raise
        finally:
            logger.debug("Finished Cursor._rotate")

    def _setter(self):
        logger.debug("Executing Cursor._setter")
        try:
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
            self.log_cursor()
        except Exception as e:
            logger.error(f"Error in Cursor._setter: {e}", exc_info=True)
            raise
        finally:
            logger.debug("Finished Cursor._setter")


    def rotater(self):
        logger.debug("Executing Cursor.rotater")
        try:
            self._rotate()
            self._setter()
        except Exception as e:
            logger.error(f"Error in Cursor.rotater: {e}", exc_info=True)
            raise
        finally:
            logger.debug("Finished Cursor.rotater")

    def sizer(self):
        logger.debug("Executing Cursor.sizer")
        try:
            Max=max(self.cursor)
            i=1
            while(Max>1):
                #print(Max)
                Max=Max//2
                i+=1
            self.size=i
            
            if (self.col>width-self.size-1):
                self.col=width-self.size-1
                
        except Exception as e:
            logger.error(f"Error in Cursor.sizer: {e}", exc_info=True)
            raise
        finally:
            logger.debug("Finished Cursor.sizer")

    def converter(self):
        #logger.debug("Executing Cursor.converter")
        try:
            temp=[]
            if(self.col<=width-self.size):
                for i in range(shape_size):
                    temp.append(2**(self.col)*self.cursor[i])
                return temp
            else:
                return
        except Exception as e:
            logger.error(f"Error in Cursor.converter: {e}", exc_info=True)
            raise
        finally:
            pass
            #logger.debug("Finished Cursor.converter")
    
        



def get_row(brd,csr):
    #logger.debug("Executing get_row")
    try:
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
    except Exception as e:
        logger.error(f"Error in get_row: {e}", exc_info=True)
        raise
    finally:
        pass
        #logger.debug("Finished get_row")


def update_Game(brd,csr):
    logger.info("Executing update_Game")
    try:
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
        brd.log_board()
    except Exception as e:
        logger.error(f"Error in update_Game: {e}", exc_info=True)
        raise
    finally:
        logger.info("Finished update_Game")


def Game(brd,csr,prm):
    #logger.debug(f"Executing Game with action: {prm}")
    try:
        match(prm):
            case 'e':
                save(brd)
                return 0
            case 'w':
                csr.rotater()
                return -1
            case 'd':
                csr.col+=1
                if(csr.col==width-csr.size+1):
                    csr.col=0
                logger.info(f"current column= {csr.col}")
                return -1
            case 'a':
                
                if(csr.col==0):
                    csr.col=width-csr.size+1
                csr.col-=1
                logger.info(f"current column= {csr.col}")
                return -1
            case '\r':
                
                update_Game(brd,csr) 
                csr=Cursor(randomizer())
                if(brd.board[(height-shape_size+1)]>0):
                    brd=Board(0)
                    return 1
                return -1
    except Exception as e:
        logger.error(f"Error in Game: {e}", exc_info=True)
        raise
    finally:
        pass
        #logger.debug("Finished Game")
                  
def save(brd):
    logger.info("Executing save")
    try:
        val=0
        for i in range(height):
            val+=(brd.board[i]*(2**(width*i)))
        game_atts["board"]=val
        with open('game/game_atribute.json','w') as file:
            json.dump(game_atts,file,indent=4)
        logger.info(f"Board saved successfully Current value= {val}")
    except Exception as e:
        logger.error(f"Error in save: {e}", exc_info=True)
        raise
    finally:
        logger.info("Finished save")
