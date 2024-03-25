board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

game_over = False
player = "X"

def have_game_over(board, player):
    # Check the rows
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Check the columns
    for j in range(len(board)):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # Check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    return False

def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
            if j < len(board[i]) - 1:
                print("|", end=" ")
        print("")
        if i < len(board) - 1:
            print("-" * (len(board) * 3))

while not game_over:
    print_board()
    print("Enter", player, "enter!")
    r = int(input())
    c = int(input())

    if board[r][c] == " ":
        board[r][c] = player
        game_over = have_game_over(board, player)
        if game_over:
            print("Player", player, "won!")
            print_board()
        else:
            player = "O" if player == "X" else "X"
    else:
        print("Invalid move, please try again")
