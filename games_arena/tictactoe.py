import tkinter as display

from apps.games_arena.celltakenerror import CellTakenError
from apps.games_arena.cellvalue import Cell_Values



class TicTacToe:
    root = display.Tk()
    root.withdraw()

    def __init__(self):
        self.game_board = [
            [Cell_Values.EMPTY, Cell_Values.EMPTY, Cell_Values.EMPTY],
            [Cell_Values.EMPTY, Cell_Values.EMPTY, Cell_Values.EMPTY],
            [Cell_Values.EMPTY, Cell_Values.EMPTY, Cell_Values.EMPTY]
        ]
        self.count = 0

    def get_board_cell(self, cell_number: int):
        number = cell_number - 1
        row = number // 3
        column = number % 3
        return self.game_board[row][column]


    def validate_cell(self, number):
        if self.get_board_cell(number) is not Cell_Values.EMPTY:
            raise CellTakenError

    def play(self, cell_number: int):
        self.validate_cell(cell_number)
        cell_number -= 1
        row = int(cell_number / 3)
        column = int(cell_number % 3)
        if self.count % 2 == 0:
            self.game_board[row][column] = Cell_Values.X
        else:
            self.game_board[row][column] = Cell_Values.O
        self.count += 1

    def result(self):
        if self.game_board[0][0] == Cell_Values.X and self.game_board[0][1] == Cell_Values.X and self.game_board[0][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[1][0] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[1][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[2][0] == Cell_Values.X and self.game_board[2][1] == Cell_Values.X and self.game_board[2][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cell_Values.X and self.game_board[1][0] == Cell_Values.X and self.game_board[2][
            0] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][1] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[2][
            1] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][2] == Cell_Values.X and self.game_board[1][2] == Cell_Values.X and self.game_board[2][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[2][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[2][0] == Cell_Values.X and self.game_board[1][1] == Cell_Values.X and self.game_board[0][
            2] == Cell_Values.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cell_Values.O and self.game_board[0][1] == Cell_Values.O and self.game_board[0][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[1][0] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[1][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[2][0] == Cell_Values.O and self.game_board[2][1] == Cell_Values.O and self.game_board[2][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][0] == Cell_Values.O and self.game_board[1][0] == Cell_Values.O and self.game_board[2][
            0] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][1] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[2][
            1] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][2] == Cell_Values.O and self.game_board[1][2] == Cell_Values.O and self.game_board[2][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[0][0] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[2][
            2] == Cell_Values.O:
            return "Player Two wins."
        elif self.game_board[2][0] == Cell_Values.O and self.game_board[1][1] == Cell_Values.O and self.game_board[0][
            2] == Cell_Values.O:
            return "Player Two wins."
        pass

    def player_one(self):
        while True:
            try:
                choice = int(input("Player One Turn: \nEnter a number between 1 and 9: "))
                if 1 <= choice <= 9:
                    return choice
                else:
                    print("Invalid input! Please enter a number between 1 and 9.")
            except TypeError as error:
                print("Invalid input", f"\n{error}\n\n")
                self.player_one()
            except ValueError as error:
                print("Invalid input", f"\n{error}\n\n")
                self.player_one()

    def __str__(self):
        output = f"  {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"}\n"
        for row in range(3):
            for column in range(3):
                if self.game_board[row][column] == Cell_Values.EMPTY:
                    output += f" {"  "} {" | "}"
                elif self.game_board[row][column] == Cell_Values.X:
                    output += f" {'X'} {" | "}"
                elif self.game_board[row][column] == Cell_Values.O:
                    output += f" {"O"} {" | "}"
            output += f"\n  {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"} {"-"}\n"
        return output

    def display_board(self):
        return f"{self.display_numbers()}\n{self.__str__()}"

    def player_two(self):
        while True:
            try:
                choice = int(input("Player Two Turn: \nEnter a number between 1 and 9: "))
                if 1 <= choice <= 9:
                    self.count += 1
                    return choice
                else:
                    print("Invalid input! Please enter a number between 1 and 9.")
            except TypeError as error:
                print("Invalid input", f"\n{error}\n\n")
                self.player_two()
            except ValueError as error:
                print("Invalid input", f"\n{error}\n\n")
                self.player_two()


    def display_numbers(self):
        string = ""
        for numbers in range(9):
            if numbers % 3 == 0:
                string += "\n| "
            string += f" {numbers + 1} |"
        return string

    def __game1ErrorCheck(self):
        try:
            self.play(self.player_one())
        except CellTakenError as error:
            print(error)
            self.__game1ErrorCheck()

    def __game2ErrorCheck(self):
        try:
            self.play(self.player_two())
        except CellTakenError as error:
            print(error)
            self.__game2ErrorCheck()

    def start_game(self):
        try:
            while self.result() is None and self.count != 9:
                print("Board\n\n", f" {self.display_board()}\n\n")
                self.__game1ErrorCheck()
                print("Board: \n\n", f"{self.display_board()}\n\n")
                if self.result() is not None:
                    break
                self.__game2ErrorCheck()
            print("Winner::\n", self.result())
        except KeyboardInterrupt as error:
            print(error)
            self.start_game()


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
