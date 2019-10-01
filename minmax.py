import board as b
import move as mv

def evaluation(state, my_turn):
    if (my_turn==mv.SOUTH_TURN):
        return state.getSouthStoreHouse()-state.getNorthStoreHouse()
    else:
        return state.getNorthStoreHouse()-state.getSouthStoreHouse()

def maximum(state, depth, my_turn, alpha, beta, is_prune):
    print("maksimum")
    if my_turn == mv.SOUTH_TURN:
        init = 0
    else:
        init = 8
    max_value = -999
    for i in range (init, init+7):
        new_state, next_turn = mv.move(state, my_turn, i)
        new_state.printBoard()
        score = minimax(new_state, next_turn, depth-1, my_turn, alpha, beta, my_turn)
        max_value = max(max_value, score)
        alpha = max(alpha, score)
        if is_prune and beta <= alpha:
            break
    return max_value

def minimum(state, depth, my_turn, alpha, beta, is_prune):
    print("minimum")
    if mv.nextTurn(my_turn) == mv.SOUTH_TURN:
        init = 0
    else:
        init = 8

    min_value = 999
    for i in range (init, init+7):
        new_state, next_turn =  mv.move(state, mv.nextTurn(my_turn), i)
        new_state.printBoard()
        score = minimax(new_state, next_turn, depth-1, my_turn, alpha, beta, mv.nextTurn(my_turn))
        min_value = min(min_value, score)
        beta = min(beta, min_value)
        if is_prune and beta <= alpha:
            break
    return min_value

def minimax(state, current_turn, depth, my_turn, alpha, beta, parent_turn):
    if depth == 0:
        return evaluation(state, current_turn)

    if (current_turn==my_turn):
        return maximum(state, depth, my_turn, alpha, beta, parent_turn != current_turn)
    else:
        return minimum(state, depth, my_turn, alpha, beta, parent_turn != current_turn)

def best_move (state, turn, depth):
    score = []
    if turn == mv.SOUTH_TURN:
        init = 0
    else:
        init = 8
    for i in range (init, init+7):
        print("****", i)
        next_state, next_turn = mv.move(state, turn, i)
        score.append(minimax(next_state, next_turn, depth-1, turn, -999, 999, turn))
    if (turn == mv.SOUTH_TURN):    
        return score.index(max(score))
    else:    
        return score.index(min(score))+8


my_board = b.Board()
my_board, nextTurn = mv.move(my_board, mv.SOUTH_TURN, 0)
my_board, nextTurn = mv.move(my_board, mv.SOUTH_TURN, 1)
my_board, nextTurn = mv.move(my_board, mv.SOUTH_TURN, 3)
depth = 5
steps = best_move(my_board, mv.SOUTH_TURN, depth)
print(steps)
