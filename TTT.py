# Tic-Tac-Toe Game Implementation (Improved)



# Function to print the current state of the board
def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(BOARD_SIZE)):  # Check columns
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):  # Main diagonal
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):  # Anti-diagonal
        return True

    return False

# Function to check if the board is full (i.e., a tie)
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Main game loop
def play_game():
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get player input
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2, separated by space): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers.")
            continue

        # Validate the input
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE or board[row][col] != ' ':
            print("Invalid move. Please try again.")
            continue

        # Update the board with the player's move
        board[row][col] = current_player

        # Check if the current player has won
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (tie)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

# Main function to start the game
if __name__ == "__main__":
    
    print("Welcome to Tic-Tac-Toe!")
    print("Welcome to Tic-Tac-Toe!")
    
    # Get board size from the user
    try:
        BOARD_SIZE = int(input(f"Enter the size of the board ({MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}): "))
        if board_SIZE < MIN_BOARD_SIZE or board_size > MAX_BOARD_SIZE:
            print(f"Board size must be between {MIN_BOARD_SIZE} and {MAX_BOARD_SIZE}.")
        else:
            play_game(board_size)
