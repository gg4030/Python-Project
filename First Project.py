import random
def display_board(board):
    print('  |   | ')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   | ')
    print('--------- ')
    print('  |   | ')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   | ')
    print('--------- ')
    print('  |   | ')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   | ')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('P1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):  
    return  ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))  

def choice_first():
    if random.randint(0, 1) == 0:
        return 'P2'
    else:
        return 'P1'

def space_check(board,position):
    return board[position] == ' '       

def full_board(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position between (1-9): "))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')   

print("Welcome to Tic Tac Toe")

while True:
    the_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    P1_marker,P2_marker=player_input()
    turn=choice_first()
    print(turn,'Will go first')
    play_game=input('Ready for game? y or n: ')
    if play_game[0] == 'y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn == 'P1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,P1_marker,position)

            if win_check(the_board,P1_marker):
                display_board(the_board)
                print('P1 has Won')
                game_on=False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('TIE!!')
                    game_on = False
                else:
                    turn = 'P2'

        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,P2_marker,position)

            if win_check(the_board,P2_marker):
                display_board(the_board)
                print('P2 has won!')
                game_on = False
            else:
                if full_board(the_board):
                    display_board(the_board)
                    print('TIE!!')
                    break
                else:
                    turn = 'P1'
    if not replay():
       break
