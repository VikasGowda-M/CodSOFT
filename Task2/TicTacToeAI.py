import math


board = [" " for _ in range(9)]


def print_board():
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")


def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
    for pos in win_positions:
        if b[pos[0]] == b[pos[1]] == b[pos[2]] == player:
            return True
    return False


def is_draw(b):
    return " " not in b


def minimax(b, depth, is_max):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best = min(score, best)
        return best


def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def play():
    print("Positions: 0-8")
    print_board()

    while True:
      
        user = int(input("Enter position (0-8): "))
        if board[user] != " ":
            print("Invalid move!")
            continue

        board[user] = "X"
        print_board()

        if check_winner(board, "X"):
            print("You win!")
            break
        if is_draw(board):
            print("Draw!")
            break

        
        ai = best_move()
        board[ai] = "O"
        print("\nAI move:")
        print_board()

        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_draw(board):
            print("Draw!")
            break


play()