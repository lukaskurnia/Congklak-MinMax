#Repreentasi Board
#     8  9  10  11  12  13  14  15
#  7  6  5  4    3   2   1   0  

SOUTH_STOREHOUSE = 7
NORTH_STOREHOUSE = 15


class Board:
    #Inisialisasi papan congklak
    def __init__(self):
        self.board = [7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,0]

    #Menampilkan papan congklak
    def printBoard(self):
        print('    _________________________________')
        print('    |',self.board[8],'|',self.board[9],'|',self.board[10],'|',self.board[11],'|',self.board[12],'|',self.board[13],'|',self.board[14],'|',self.board[15],'|')
        print(' ___|___|___|___|___|___|___|___|___|')
        print('|',self.board[7],'|',self.board[6],'|',self.board[5],'|',self.board[4],'|',self.board[3],'|',self.board[2],'|',self.board[1],'|',self.board[0],'|')
        print('|___|___|___|___|___|___|___|___|')

    #Mengecek house kosong atau tidak
    def isEmptyHouse(self,index):
        return self.board[index]==0

    #Mengembalikan house lawan yang berada di seberang 
    def getOpponentIndex(self, currentIndex):
        return (14 - currentIndex)

    #Mengembalikan nilai dari storehouse South
    def getSouthStoreHouse(self):
        return self.board[SOUTH_STOREHOUSE]

    #Mengembalikan nilai dari storehouse North
    def getNorthStoreHouse(self):
        return self.board[NORTH_STOREHOUSE]

    #Menambahkan shell pada house dengan index tertentu
    def addShell(self,index,shell):
        self.board[index] = self.board[index] + shell

    #Mengambil seluruh shell dalam sebuah house
    def getShell(self,index):
        temp = self.board[index]
        self.board[index] = 0
        return temp

    #True jika daerah house berada di north
    def northSite(self, index):
        return index==8 or index==9 or index==10 or index==11 or index==12 or index==13 or index==14

    #True jika daerah house berada di south
    def southSite(self, index):
        return index==0 or index==1 or index==2 or index==3 or index==4 or index==5 or index==6

    #True jika index berada di storehouse South
    def isSouthStoreHouse(self, index):
        return SOUTH_STOREHOUSE == index

    #True jika index berada di storehouse North
    def isNorthStoreHouse(self, index):
        return NORTH_STOREHOUSE == index

    #True jika seluruh house di south kosong    
    def checkAllSouthHouseEmpty(self):
        for i in range(0,7):
            if(not(self.isEmptyHouse(i))):
                return False
        return True

    #True jika seluruh house di north kosong
    def checkAllNorthHouseEmpty(self):
        for i in range(8,15):
            if(not(self.isEmptyHouse(i))):
                return False
        return True


    #True jika seluruh House kosong
    def checkAllHouseEmpty(self):
        return self.checkAllNorthHouseEmpty() and self.checkAllSouthHouseEmpty()