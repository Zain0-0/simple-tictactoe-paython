import random

# 1. Create the board as a list of 9 spaces
# board = [' '] * 9
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

# 2. Function to display the board
def show_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print('|' + '|'.join(row) + '|')
    print()

# 3. Function to check for a win
def is_winner(letter):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diags
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] == letter:
            return True
    return False

# 4. Main game loop (max 9 turns)
for turn in range(9):
    letter = 'X' if turn % 2 == 0 else 'O'

    show_board()

    if letter == 'X':
        # Human move
        move = None
        while move not in range(9) or board[move] != ' ':
            move = int(input("X, choose 0–8: "))
    else:
        # # Random computer move
        # empties = [i for i, v in enumerate(board) if v == ' ']
        empties = []
        for i in range(9):
            if board[i] == ' ':
                empties.append(i)
        move = random.choice(empties)

    board[move] = letter

    # Check for a win
    if is_winner(letter):
        show_board()
        print(letter, "wins!")
        break
    else:
        # If we never 'break', it's a tie
        show_board()
        print("It's a tie!")
