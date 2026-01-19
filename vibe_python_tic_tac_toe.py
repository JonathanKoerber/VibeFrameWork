def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 0-8 (left to right, top to bottom)")
    
    while True:
        print_board(board)
        
        while True:
            try:
                pos = int(input(f"Player {current_player}, enter position (0-8): "))
                if pos < 0 or pos > 8:
                    print("Invalid position!")
                    continue
                row, col = pos // 3, pos % 3
                if board[row][col] != " ":
                    print("Position already taken!")
                    continue
                board[row][col] = current_player
                break
            except ValueError:
                print("Please enter a number between 0 and 8")
        
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()