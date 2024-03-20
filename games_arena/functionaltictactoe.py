game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def display_board():
    print('loading...')
    print('this is the game board')
    for num in range(0, len(game_board)):
        if num % 3 == 0:
            print()
            print(game_board[num], "  ", end="")
        else:
            print(game_board[num], "  ", end="")
    print()
    pass


def display_number():
    print('number of positions are: 👇👇.')
    for num in range(1, len(game_board) + 1):
        if num % 3 == 0:
            print(f'{num}  ')
        else:
            print(f'{num}  ', end="  ")
    pass


def collect_input_for_player_1():
    display_board()
    num = int(input('player1 where do you want to play: '))
    while num < 1 or num > 10 or game_board[num - 1] != '-':
        display_number()
        num = int(input('pls enter a valid  number of where you want to play😡😡😡: '))
    game_board[num - 1] = 'X '
    pass


def collect_input_for_player_2():
    display_board()
    num = int(input('player2 where do you want to play: '))
    while (num < 1 or num > 10) or game_board[num - 1] != '-':
        num = int(input('pls enter a valid  number of where you want to play😡😡😡: '))
    game_board[num - 1] = 'O'
    pass


def check_for_winner():
    if game_board[0] == 'X' and game_board[1] == 'X' and game_board[2] == 'X':
        return 0
    elif game_board[3] == 'X' and game_board[4] == 'X' and game_board[5] == 'X':
        return 0
    elif game_board[6] == 'X' and game_board[7] == 'X' and game_board[8] == 'X':
        return 0
    elif game_board[0] == 'X' and game_board[3] == 'X' and game_board[6] == 'X':
        return 0
    elif game_board[1] == 'X' and game_board[4] == 'X' and game_board[7] == 'X':
        return 0
    elif game_board[2] == 'X' and game_board[5] == 'X' and game_board[8] == 'X':
        return 0
    elif game_board[0] == 'X' and game_board[4] == 'X' and game_board[8] == 'X':
        return 0
    elif game_board[6] == 'X' and game_board[4] == 'X' and game_board[2] == 'X':
        return 0
    elif game_board[0] == 'O' and game_board[1] == 'O' and game_board[2] == 'O':
        return 1
    elif game_board[1] == 'O' and game_board[4] == 'O' and game_board[7] == 'O':
        return 1
    elif game_board[0] == 'O' and game_board[3] == 'O' and game_board[6] == 'O':
        return 1
    elif game_board[3] == 'O' and game_board[4] == 'O' and game_board[5] == 'O':
        return 1
    elif game_board[6] == 'O' and game_board[7] == 'O' and game_board[8] == 'O':
        return 1
    elif game_board[2] == 'O' and game_board[5] == 'O' and game_board[8] == 'O':
        return 1
    elif game_board[0] == 'O' and game_board[4] == 'O' and game_board[8] == 'O':
        return 1
    elif game_board[6] == 'O' and game_board[4] == 'O' and game_board[2] == 'O':
        return 1
    else:
        return -1


def play_game():
    display_number()
    print('Let the game begin☺️☺️☺️!!!')
    for num in range(0, 9):
        if num == 8 or num == 7:
            break
        collect_input_for_player_1()
        winner = check_for_winner()
        if winner == 0:
            display_board()
            return '🎉🎉🎉🤭🤭🥳🎇player1 won🤭🤭🥳🎇🎉🎉🎉'
        if num == 8 or num == 7:
            break
        collect_input_for_player_2()
        winner = check_for_winner()

        if winner == 1:
            display_board()
            return '🎉🎉🎉🤭🤭🥳🎇player2 won🤭🤭🥳🎇🎉🎉🎉'
        if num == 7 or num == 8:
            break
    return 'draw'
    pass


def game():
    winner = play_game()
    if winner == "draw":
        game()


if __name__ == '__main__':
    print(game())
