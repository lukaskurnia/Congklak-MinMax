import board as b
import move as m
import random

def random_move(board, turn):
    idx = m.INVALID_INDEX
    if (turn == m.NORTH_TURN):
        if (not board.checkAllNorthHouseEmpty()):
            idx = random.randint(8,15)
            while (not m.legalMove(board, turn, idx)):
                idx = random.randint(8,15)
    else:
        if (not board.checkAllSouthHouseEmpty()):
            idx = random.randint(0,7)
            while (not m.legalMove(board, turn, idx)):
                idx = random.randint(0,7)
    return idx

# bo = b.Board()
# print(random_move(bo,m.SOUTH_TURN))
    
