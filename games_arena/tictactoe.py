from apps.games_arena.celltakenerror import CellTakenError
from apps.games_arena.cellvalue import Cellvalues
import tkinter as display
from tkinter import simpledialog, messagebox

class TicTacToe:
    root = display.Tk()
    root.withdraw()
    def __init__(self):
        self.game_board = [[Cellvalues.EMPTY, Cellvalues.EMPTY, Cellvalues.EMPTY],
                           [Cellvalues.EMPTY, Cellvalues.EMPTY, Cellvalues.EMPTY],
                           [Cellvalues.EMPTY, Cellvalues.EMPTY, Cellvalues.EMPTY]]
        self.count = 0

    def get_board_cell(self, cell_number: int):
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        return self.game_board[row][column]

    def validate_cell(self, number):
        if not self.get_board_cell(number) == Cellvalues.EMPTY:
            raise CellTakenError

    def validate_number(self, number: int):
        if number < 1 or number > 10:
            raise ValueError

    def play(self, cell_number: int):
        self.validate_cell(cell_number)
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        if self.count % 2 == 0:
            self.game_board[row][column] = Cellvalues.X
        else:
            self.game_board[row][column] = Cellvalues.O
        self.count += 1

    def result(self):
        if self.game_board[0][0] == Cellvalues.X and self.game_board[0][1] == Cellvalues.X and self.game_board[0][
            2] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[1][0] == Cellvalues.X and self.game_board[1][1] == Cellvalues.X and self.game_board[1][
            1] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[2][0] == Cellvalues.X and self.game_board[2][1] == Cellvalues.X and self.game_board[2][
            2] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cellvalues.X and self.game_board[1][0] == Cellvalues.X and self.game_board[2][
            0] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[0][1] == Cellvalues.X and self.game_board[1][1] == Cellvalues.X and self.game_board[2][
            1] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[0][2] == Cellvalues.X and self.game_board[1][2] == Cellvalues.X and self.game_board[2][
            2] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cellvalues.X and self.game_board[1][1] == Cellvalues.X and self.game_board[2][
            2] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[2][0] == Cellvalues.X and self.game_board[1][1] == Cellvalues.X and self.game_board[0][
            2] == Cellvalues.X:
            return "Player one wins."
        elif self.game_board[0][0] == Cellvalues.O and self.game_board[0][1] == Cellvalues.O and self.game_board[0][
            2] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[1][0] == Cellvalues.O and self.game_board[1][1] == Cellvalues.O and self.game_board[1][
            1] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[2][0] == Cellvalues.O and self.game_board[2][1] == Cellvalues.O and self.game_board[2][
            2] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[0][0] == Cellvalues.O and self.game_board[1][0] == Cellvalues.O and self.game_board[2][
            0] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[0][1] == Cellvalues.O and self.game_board[1][1] == Cellvalues.O and self.game_board[2][
            1] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[0][2] == Cellvalues.O and self.game_board[1][2] == Cellvalues.O and self.game_board[2][
            2] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[0][0] == Cellvalues.O and self.game_board[1][1] == Cellvalues.O and self.game_board[2][
            2] == Cellvalues.O:
            return "Player Two wins."
        elif self.game_board[2][0] == Cellvalues.O and self.game_board[1][1] == Cellvalues.O and self.game_board[0][
            2] == Cellvalues.O:
            return "Player Two wins."
        else:
            return "Draw"
        pass

    def player_one(self):
        try:
            choice = simpledialog.askinteger("Game", "Enter a number between 1 and 9")
            self.validate_number(choice)
            self.validate_cell(choice)
            return choice
        except AttributeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except CellTakenError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except ValueError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except Exception:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()

    def start_game(self):
        pass
