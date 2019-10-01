import board
import move 

def evaluation(before, after, turn):
    if (turn==move.SOUTH_TURN):
        # print("Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # print(after.getSouthStoreHouse())
        # print(before.getSouthStoreHouse())
        return after.getSouthStoreHouse()-before.getSouthStoreHouse()
    else:
        # print("Bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
        # print(after.getNorthStoreHouse())
        # print(before.getNorthStoreHouse())
        return after.getNorthStoreHouse()-before.getNorthStoreHouse()

def maximum(board, depth):
    print("maksimum")
    arr = []
    for i in range (0, 7):
        if board.board[i]!=0:
            # print(i)
            new_board, next_turn = move.move(board, move.SOUTH_TURN, i)
            # board.printBoard()
            # print("--------------------")
            new_board.printBoard()
            if (depth==0):
                # print("masuk sini1")
                # print(evaluation(board,new_board, 0))
                arr.append(evaluation(board,new_board, 0))
                # print(arr)
            else:
                # print("masuk sini3")
                # print()
                # print()
                arr.append(minimax(new_board, next_turn, depth-1))
    #             print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #             print(arr)
    # print("resultarr")            
    # print(arr)
    # print(max(arr))
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
        return maximum(board, depth)
    else:
        print("opposite turn")
        return minimum(board, depth)

def best_move (state, turn, depth):
    score = []
    if turn == move.SOUTH_TURN:
        init = 0
    else:
        init = 8
    for i in range (init, init+7):
        next_state, next_turn = move.move(state, turn, i)
        score.append(minimax(next_state, next_turn, depth))
    if (turn == move.SOUTH_TURN):    
        return score.index(max(score))
    else:    
        return score.index(min(score))+8

my_board = board.Board()
steps = best_move(my_board, move.SOUTH_TURN, 1)
print(steps)