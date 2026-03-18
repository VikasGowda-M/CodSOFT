#tic-tac-toe AI:
import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
def ai_move(board):
    moves = get_available_moves(board)
    return random.choice(moves) if moves else None
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print_board(board)
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 1 1): ")
            row, col = map(int, move.split())
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "X"
            print_board(board)
            if check_winner(board, "X"):
                print("Congratulations! You win!")
                break
            ai_row, ai_col = ai_move(board)
            if ai_row is not None:
                board[ai_row][ai_col] = "O"
                print("AI's move:")
                print_board(board)
                if check_winner(board, "O"):
                    print("AI wins! Better luck next time.")
                    break
            else:
                print("It's a draw!")
                break
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 0 and 2.")
    if __name__ == "__main__":
        main()
    #end of code