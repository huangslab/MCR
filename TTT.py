# Tic-Tac-Toe Game Implementation (with intentional defects)

# Board size
BOARD_SIZE = 3

# Initialize the board with empty spaces
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Function to print the current state of the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-----")

# Function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check columns
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full (i.e., a tie)
def is_board_full():
    for row in board:
        if ' ' in row:
            return False
    return True

# Main game loop
def play_game():
    current_player = 'X'

    while True:
        print_board()

        # Get player input
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2, separated by space): ").split())
        except:
            print("Invalid input. Please enter two numbers.")
            continue

        # Validate the input
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            print("Invalid move. Please try again.")
            continue

        # Update the board with the player's move
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        # Check if the current player has won
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (tie)
        if is_board_full():
            print_board()
            print("It's a tie!")
            break

        # Switch to the other player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Main function to start the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()
