# Tic Tac Toe Game

def display_board(board):
    """Displays the current state of the board"""
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def is_position_available(board, row, col):
    """Checks if the chosen position is available"""
    return board[row][col] == '-'


def place_symbol(board, row, col, symbol):
    """Places the player's symbol on the board"""
    if is_position_available(board, row, col):
        board[row][col] = symbol
        return True
    return False


def check_winner(board, symbol):
    """Checks if the current player has won"""
    # Check rows and columns
    for i in range(3):
        if all([cell == symbol for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == symbol for j in range(3)]):  # Check column
            return True

    # Check diagonals
    if all([board[i][i] == symbol for i in range(3)]) or all([board[i][2-i] == symbol for i in range(3)]):
        return True

    return False


def check_draw(board):
    """Checks if the game is a draw"""
    return all([cell != '-' for row in board for cell in row])


def switch_player(current_player):
    """Switches the current player between 'X' and 'O'"""
    return 'O' if current_player == 'X' else 'X'


def play_game():
    """Main function to play Tic Tac Toe"""
    # Initialize the board
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    # Game loop
    while not game_over:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        # Get user input for the row and column
        try:
            row = int(input('Enter row (0, 1, 2): '))
            col = int(input('Enter column (0, 1, 2): '))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue

        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        # Place the symbol if the position is valid
        if place_symbol(board, row, col, current_player):
            # Check if there's a winner
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                game_over = True
            # Check for a draw
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                game_over = True
            else:
                # Switch to the other player
                current_player = switch_player(current_player)
        else:
            print("Position is already occupied, try again.")


# Start the game
if __name__ == "__main__":
    play_game()
