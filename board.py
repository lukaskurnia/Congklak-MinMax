#Repreentasi Board
#     8  9  10  11  12  13  14  15
#  7  6  5  4    3   2   1   0  

PLAYER_NORTH = 1
PLAYER_SOUTH = 0

def initBoard():
    board = [7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,0]
    return board

def printBoard(board):
    print('    _________________________________')
    print('    |',board[8],'|',board[9],'|',board[10],'|',board[11],'|',board[12],'|',board[13],'|',board[14],'|',board[15],'|')
    print(' ___|___|___|___|___|___|___|___|___|')
    print('|',board[7],'|',board[6],'|',board[5],'|',board[4],'|',board[3],'|',board[2],'|',board[1],'|',board[0],'|')
    print('|___|___|___|___|___|___|___|___|')


state = initBoard()
printBoard(state)
