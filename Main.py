import random

# Sample tic-tac-toe game 
board = [' ' for _ in range(9)]

def display_board():
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('|'.join(row))
        print('-' * 5)

def player_input(player):
    if player == 'O':
        # steps for computer to make smart moves
        # 1. try to win
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                if check_win() == 'O':
                    print(f"Player O (computer) chooses position {i + 1}")
                    return
                board[i] = ' '
        # 2. block X
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                if check_win() == 'X':
                    board[i] = 'O'
                    print(f"Player O (computer) chooses position {i + 1}")
                    return
                board[i] = ' '
        # 3. otherwise, pick center, corners, or random
        for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            if board[i] == ' ':
                board[i] = 'O'
                print(f"Player O (computer) chooses position {i + 1}")
                return
    else:
        position = int(input(f"Player {player}, enter your position (1-9): ")) - 1
        if board[position] == ' ':
            board[position] = player
        else:
            print("Position already taken. Try again.")
            player_input(player)

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                     (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                     (0, 4, 8), (2, 4, 6)]  
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

# Main loop
current_player = 'X'
while True:
    display_board()
    player_input(current_player)
    winner = check_win()
    if winner:
        display_board()
        print(f"Player {winner} wins!")
        break
    if ' ' not in board:
        display_board()
        print("It's a draw!")
        break
    current_player = 'O' if current_player == 'X' else 'X'