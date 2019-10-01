import board
import move 

def evaluation(before, after, turn):
    if (turn):
        return after.getSouthStoreHouse()-after.getSouthStoreHouse()
    else:
        return after.getNorthStoreHouse()-before.getNorthStoreHouse()

def maximum(board, depth):
    print("maksimum")
    arr = []
    for i in range (0, 7):
        if board.board[i]!=0:
            print(i)
            new_board, next_turn = move.move(board, move.SOUTH_TURN, i)
            new_board.printBoard()
            if (depth==0):
                print("masuk sini1")
                arr.append(evaluation(board,new_board, 0))
            else:
                print("masuk sini3")
                print()
                print()
                arr.append(minimax(new_board, next_turn, depth-1))
    return max(arr)

def minimum(board, depth):
    arr = []
    for i in range (8, 15):
        if board.board[i]!=0:
            new_board, next_turn =  move.move(board, move.NORTH_TURN, i)
            if (depth==0):
                arr.append(evaluation(board,new_board, 1))
            # if (board[i]==0):
            #     return arr.append(0)
            else:
                arr.append(minimax(new_board, next_turn, depth-1))
    return min(arr)


def minimax(board, myTurn, depth):
    if (myTurn==move.SOUTH_TURN):
        print("my turn")
        maximum(board, depth)
    else:
        print("opposite turn")
        minimum(board, depth)

my_board = board.Board()
steps = print(minimax(my_board, move.SOUTH_TURN, 1))
my_board, a = move.move(my_board, move.SOUTH_TURN, 1)
my_board.printBoard()
