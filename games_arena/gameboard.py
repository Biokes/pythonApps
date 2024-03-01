class Game1:
    def __init__(self):
        self.game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def display_board(self):

        print('loading...')
        print('this is the game board')
        for num in range(0, len(self.game_board)):
            if num % 3 == 0:
                print()
                print(self.game_board[num], "  ", end="")
            else:
                print(self.game_board[num], "  ", end="")
        print()
        pass

    def display_number(self):
        print('number of positions are: 👇👇.')
        for num in range(1, len(self.game_board) + 1):
            if num % 3 == 0:
                print(f'{num}  ')
            else:
                print(f'{num}  ', end="  ")
        pass

    def collect_input_for_player_1(self):
        self.display_board()
        num = int(input('player1 where do you want to play: '))
        while num < 1 or num > 10 or self.game_board[num - 1] != '-':
            self.display_number()
            num = int(input('pls enter a valid  number of where you want to play😡😡😡: '))
        self.game_board[num - 1] = 'X '
        pass

    def collect_input_for_player_2(self):
        self.display_board()
        num = int(input('player2 where do you want to play: '))
        while (num < 1 or num > 10) or self.game_board[num - 1] != '-':
            num = int(input('pls enter a valid  number of where you want to play😡😡😡: '))
        self.game_board[num - 1] = 'O'
        pass

    def check_for_winner(self):
        if self.game_board[0] == 'X' and self.game_board[1] == 'X' and self.game_board[2] == 'X':
            return 0
        elif self.game_board[3] == 'X' and self.game_board[4] == 'X' and self.game_board[5] == 'X':
            return 0
        elif self.game_board[6] == 'X' and self.game_board[7] == 'X' and self.game_board[8] == 'X':
            return 0
        elif self.game_board[0] == 'X' and self.game_board[3] == 'X' and self.game_board[6] == 'X':
            return 0
        elif self.game_board[1] == 'X' and self.game_board[4] == 'X' and self.game_board[7] == 'X':
            return 0
        elif self.game_board[2] == 'X' and self.game_board[5] == 'X' and self.game_board[8] == 'X':
            return 0
        elif self.game_board[0] == 'X' and self.game_board[4] == 'X' and self.game_board[8] == 'X':
            return 0
        elif self.game_board[6] == 'X' and self.game_board[4] == 'X' and self.game_board[2] == 'X':
            return 0
        elif self.game_board[0] == 'O' and self.game_board[1] == 'O' and self.game_board[2] == 'O':
            return 1
        elif self.game_board[1] == 'O' and self.game_board[4] == 'O' and self.game_board[7] == 'O':
            return 1
        elif self.game_board[0] == 'O' and self.game_board[3] == 'O' and self.game_board[6] == 'O':
            return 1
        elif self.game_board[3] == 'O' and self.game_board[4] == 'O' and self.game_board[5] == 'O':
            return 1
        elif self.game_board[6] == 'O' and self.game_board[7] == 'O' and self.game_board[8] == 'O':
            return 1
        elif self.game_board[2] == 'O' and self.game_board[5] == 'O' and self.game_board[8] == 'O':
            return 1
        elif self.game_board[0] == 'O' and self.game_board[4] == 'O' and self.game_board[8] == 'O':
            return 1
        elif self.game_board[6] == 'O' and self.game_board[4] == 'O' and self.game_board[2] == 'O':
            return 1
        else:
            return -1

    def play_game(self):
        self.display_number()
        print('Let the game begin☺️☺️☺️!!!')
        for num in range(0, 9):
            if num == 6 or num == 8 or num == 7:
                break
            self.collect_input_for_player_1()
            winner = self.check_for_winner()
            if winner == 0:
                self.display_board()
                return '🎉🎉🎉🤭🤭🥳🎇player1 won🤭🤭🥳🎇🎉🎉🎉'
            if num == 6 or num == 8 or num == 7:
                break
            self.collect_input_for_player_2()
            winner = self.check_for_winner()

            if winner == 1:
                self.display_board()
                return '🎉🎉🎉🤭🤭🥳🎇player2 won🤭🤭🥳🎇🎉🎉🎉'
            if num == 7 or num == 8:
                break
        return 'draw'
        pass

    def game(self):
        winner = self.play_game()
        if winner == "draw":
            self.game()


if __name__ == '__main__':
    game1 = Game1()
    print(game1.game())
