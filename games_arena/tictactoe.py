import time
class tictactoe:
    def __int__(self):
        self.game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    def display_board(self):
        print('loading... \n ')
        print('this is the game board')
        for num in range(len(self.game_board)):
            if num % 3 == 0:
                print()
                print(self.game_board[num] +  "  ", end="")
            else:
                print(self.game_board[num] +  "  ", end="")
        print()
        return ''
    def display_number(self):
        print('number of positions are: 👇👇.')
        for num in range(1,len(self.game_board)+1):
            if num % 3 == 0:
                print(f'{num}  ', end="\n")
            else:
                print(f'{num}  ', end="  ")
        return ''
    def collect_input_for_player_1(self):
        self.display_board()
        num = int(input('player1 where do you want to play: '))
        while num < 1 or num > 10 or self.game_board[num-1] != '-':
            self.display_number()
            self.display_board()
            num = int(input('pls enter a valid  number of where you want to play😡😡😡: '))
        self.game_board[num-1] = 'x'
        return ''
    def collect_input_for_player_2(self):
        self.display_board()
        num = int(input('player2 where do you want to play: '))
        while (num < 1 or num > 10) or self.game_board[num-1] != '-':
            num = int(input('pls enter a valid  number of where you want to play😡😡😡: '))
        self.game_board[num-1] = 'O'
        return ''
    def check_for_winner(self):
        if self.game_board[0] == self.game_board[1]  == self.game_board[2] =='X':
            return 0
        elif self.game_board[1] == self.game_board[4]  == self.game_board[7] =='X':
            return 0
        elif self.game_board[0] == self.game_board[3]  == self.game_board[6] =='X':
            return 0
        elif self.game_board[3] == self.game_board[4]  == self.game_board[5] =='X':
            return 0
        elif self.game_board[6] == self.game_board[7]  == self.game_board[8] =='X':
            return 0
        elif self.game_board[2] == self.game_board[5]  == self.game_board[8] =='X':
            return 0
        elif self.game_board[0] == self.game_board[4]  == self.game_board[8] =='X':
            return 0
        elif self.game_board[6] == self.game_board[4]  == self.game_board[3] =='X':
            return 0
        elif self.game_board[0] == self.game_board[1] == self.game_board[2] == 'O':
            return 1
        elif self.game_board[1] == self.game_board[4] == self.game_board[7] == 'O':
            return 1
        elif self.game_board[0] == self.game_board[3] == self.game_board[6] == 'O':
            return 1
        elif self.game_board[3] == self.game_board[4] == self.game_board[5] == 'O':
            return 1
        elif self.game_board[6] == self.game_board[7] == self.game_board[8] == 'O':
            return 1
        elif self.game_board[2] == self.game_board[5] == self.game_board[8] == 'O':
            return 1
        elif self.game_board[0] == self.game_board[4] == self.game_board[8] == 'O':
            return 1
        elif self.game_board[6] == self.game_board[4] == self.game_board[3] == 'O':
            return 1
    def play_game(self):
        self.display_number()
        print('Let the game begin☺️☺️☺️☺️!!!!!!')
        for num in range(len(self.game_board)):
            self.collect_input_for_player_1()
            winner = self.check_for_winner()
            if winner == 0:
                return '🎉🎉🎉🤭🤭🥳🎇player1 won🤭🤭🥳🎇🎉🎉🎉'
            elif winner == 1:
                return '🎉🎉🎉🤭🤭🥳🎇player2 won🤭🤭🥳🎇🎉🎉🎉'
            self.collect_input_for_player_2()
            winner = self.check_for_winner()
            if winner == 0:
                return '🎉🎉🎉🤭🤭🥳🎇player1 won🤭🤭🥳🎇🎉🎉🎉'
            elif winner == 1:
                return '🎉🎉🎉🤭🤭🥳🎇player2 won🤭🤭🥳🎇🎉🎉🎉'
        return 0

    def play_game(self):
        print(self.play_game())
