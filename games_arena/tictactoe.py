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
        while number not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            choice = simpledialog.askinteger("Invalid number", "Enter a number between 1 and 9")
        return number

    def play(self, cell_number: int):
        self.validate_number(cell_number)
        self.validate_cell(cell_number)
        row = (cell_number - 1) // 3
        column = (cell_number - 1) % 3
        if self.count % 2 == 0:
            self.game_board[row][column] = "X"
        else:
            self.game_board[row][column] = "O"
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
            choice = simpledialog.askinteger("Player One Turn", "Enter a number between 1 and 9")
            self.validate_number(choice)
            self.validate_cell(choice)
            return choice
        except AttributeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except CellTakenError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except TypeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except ValueError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()
        except Exception:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_one()

    def __get_board_values(self):
        list1 = []
        for numbers in range(9):
            list1.append(self.get_board_cell(numbers + 1))
        return list1

    def __str__(self):
        list1 = self.__get_board_values()
        count = 0
        return_value = f"{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}\n"
        for values in list1:
            if values == Cellvalues.EMPTY:
                return_value += f" {" "} |"
                count += 1
            else:
                return_value += f" {values} |"
                count += 1
            if count % 3 == 0:
                return_value += "\n" + f"{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}{"-"}\n"
        return return_value

    def display_board(self):
        return self.__str__()

    def player_two(self):
        try:
            choice = simpledialog.askinteger("Player Two Turn", "Enter a number between 1 and 9")
            self.validate_number(choice)
            self.validate_cell(choice)
            return choice
        except AttributeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except CellTakenError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except ValueError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except TypeError:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()
        except Exception:
            messagebox.showerror("Invalid input", "You Entered the wrong input")
            self.player_two()

    def display_numbers(self):
        string = ""
        for numbers in range(9):
            if numbers % 3 == 0:
                string += "\n "
            string += numbers
        return string

    def start_game(self):
        messagebox.showinfo("Game Board", f"{self.display_board()}")
        for number in range(5):
            self.play(self.player_one())
            messagebox.showinfo("Game Board", f"{self.display_board()}")
            if self.result() == "Draw" and self.count != 9:
                self.play(self.player_two())
                messagebox.showinfo("Game Board", f"{self.display_board()}")
            else:
                return messagebox.showinfo("Winner Declaration.", f"{self.result()}")


if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
