from tabulate import tabulate

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]


def show_board():
    column_headers = ["C0", "C1", "C2"]
    row_index = ["R0", "R1", "R2"]
    print(tabulate(board, headers=column_headers, showindex=row_index, tablefmt="grid"))


def update_board(board, row, col, symbol):
    board[row][col] = symbol
    show_board()


def get_user_choice():
    user_choice_row = input("Choose a row (0-2 or q): ")
    user_choice_col = input("Choose a column (0-2 or q): ")
    return user_choice_row, user_choice_col


def is_winning_line(line):
    check = line[0] == line[1] == line[2]
    if "" in line or not check:
        return False
    return True


def check_if_winning():
    # Rows
    for row in board:
        if is_winning_line(row):
            return True

    # Columns
    for col in range(3):
        column = [board[0][col], board[1][col], board[2][col]]
        if is_winning_line(column):
            return True

    # Diagonals
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    if is_winning_line(diagonal1):
        return True

    diagonal2 = [board[0][2], board[1][1], board[2][0]]
    if is_winning_line(diagonal2):
        return True

    return False


def start_game():
    current_player = "X"

    print("Welcome to this Tic Tac Toe Game")
    show_board()
    print()

    while any("" in row for row in board):

        print(f"{current_player}'s turn")

        row, col = get_user_choice()

        if row.lower() == "q" or col.lower() == "q":
            print("Game ended.")
            break

        row = int(row)
        col = int(col)

        update_board(board, row, col, current_player)
        print()

        if check_if_winning():
            print(f"{current_player} wins!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    else:
        print("It's a draw!")


start_game()
